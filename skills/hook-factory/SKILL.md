---
name: hook-factory
description: >-
  Generate and install agent hooks from natural language or a menu.
  Triggers on "set up hooks," "hook factory," "add guardrails,"
  "auto-format," "block dangerous commands," "log agent activity,"
  or any request involving PreToolUse, PostToolUse, lifecycle events,
  or settings.json hook configuration.
---

# Hook Factory

Build Claude Code hooks by picking from a menu or describing what you want in plain English. This skill reads your existing config, generates the hooks JSON and any helper scripts, writes everything to disk, and sets permissions.

## Step 1: Show the Menu and Gather Input

Present this menu. The user picks numbers, describes custom hooks, or both.

```
Which hooks do you want? Pick numbers, describe your own, or both.

SAFETY (block actions before they happen)
 1. Block dangerous commands — deny rm -rf, DROP TABLE, git push --force in Bash
 2. Protect paths — deny Write/Edit to specific files (.env, generated/, configs)
 3. Command allowlist — only permit Bash commands matching approved patterns

QUALITY (run checks after edits)
 4. Auto-format on save — run your formatter after every Write/Edit
 5. Auto-lint on save — run linter after Write/Edit, feed errors back to Claude
 6. Auto-test on save — run relevant test file after editing source code

NOTIFICATIONS (know when Claude needs you)
 7. Desktop notification — system alert when Claude needs attention or finishes
 8. Sound alert — play a sound when Claude completes a long task
 9. Slack/webhook — POST to a URL when Claude finishes

CONTEXT (inject info automatically)
10. Auto-inject context — load a checklist or project state at session start
11. Prompt validator — check prompts against rules before Claude processes them
12. Git status injection — prepend git branch/status to every prompt

LOGGING (track what Claude does)
13. Command logger — log every Bash command with timestamps
14. Change tracker — log every file Write/Edit with paths

ADVANCED
15. MCP tool guardrails — validate inputs to MCP server tools
16. Subagent monitor — log subagent spawn/complete with duration
17. Pre-compact snapshot — save context before compaction
18. HTTP validation service — send tool calls to remote endpoint for policy
19. Custom — describe what you want
```

Ask the user which hooks they want. For hooks that need customization, ask follow-up questions:
- Hook 2: which paths to protect?
- Hook 3: which commands to allow?
- Hook 4/5: which formatter/linter? (prettier, biome, eslint, ruff, black, rustfmt, etc.)
- Hook 6: how are test files named relative to source? (e.g., `foo.ts` → `foo.test.ts`)
- Hook 9: what webhook URL?
- Hook 10: what file or command to inject?
- Hook 11: what rules to enforce?
- Hook 15: which MCP server and what validations?
- Hook 18: what endpoint URL?
- Hook 19: full description of desired behavior

## Step 2: Read Existing Configuration

Before generating anything, check what already exists:

1. Read `.claude/settings.json` in the project root (if it exists)
2. Read `~/.claude/settings.json` (global settings)
3. Check for `.claude/hooks/` directory and any existing scripts

If hooks already exist, show them to the user and confirm the merge strategy: add to existing hooks, or replace specific ones.

## Step 3: Generate Hooks

For each selected hook, determine the correct configuration using this reference:

### Event and Matcher Reference

| Event | Matcher field | Can block? | Common matchers |
|-------|--------------|------------|-----------------|
| PreToolUse | tool name | Yes (deny) | Bash, Write, Edit, Read, mcp__server__tool |
| PostToolUse | tool name | No | Write\|Edit, Bash |
| PostToolUseFailure | tool name | No | any tool name |
| PermissionRequest | tool name | Yes (deny) | any tool name |
| SessionStart | start type | No | startup, resume, clear, compact |
| SessionEnd | end reason | No | clear, logout, prompt_input_exit |
| UserPromptSubmit | none | Yes (reject) | always fires |
| Stop | none | No | always fires |
| Notification | notification type | No | permission_prompt, idle_prompt |
| SubagentStart | agent type | No | Bash, Explore, Plan |
| SubagentStop | agent type | No | same as SubagentStart |
| PreCompact | trigger type | No | manual, auto |
| TeammateIdle | none | No | always fires |
| TaskCompleted | none | No | always fires |
| InstructionsLoaded | none | No | always fires |
| ConfigChange | config source | No | user_settings, project_settings |
| WorktreeCreate | none | No | always fires |
| WorktreeRemove | none | No | always fires |

### Handler Types

- `command`: runs shell script. Script receives JSON on stdin. Exit 0 = allow, exit 2 = block. Any other exit = non-blocking error.
- `http`: POST to URL. Request body is the same JSON. Response body uses same output format. Use for remote/team-wide policies.
- `prompt`: sends a prompt to Claude for single-turn yes/no evaluation. Use `$ARGUMENTS` placeholder for hook input.
- `agent`: spawns a subagent with Read, Grep, Glob tools for deep verification.

### JSON Structure

```json
{
  "hooks": {
    "EVENT_NAME": [
      {
        "matcher": "regex_pattern",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/script-name.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Helper Script Template

All helper scripts that parse JSON input must follow this pattern:

```bash
#!/bin/bash
# Check for jq
if ! command -v jq &> /dev/null; then
  echo "hook-factory: jq is required but not installed. Install with: brew install jq (macOS) or apt install jq (Linux)" >&2
  exit 1
fi

# Read JSON input from stdin
INPUT=$(cat)

# Extract fields (adjust per event type)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')
# ... event-specific extraction ...

# Your logic here

# To allow: exit 0
# To block (PreToolUse only): print reason to stderr and exit 2
# echo "Blocked: reason here" >&2
# exit 2
```

### Critical Rules When Generating Hooks

- Always use `"$CLAUDE_PROJECT_DIR"` (with quotes) for script paths in the command field. This handles paths with spaces.
- Default scope is project: `.claude/settings.json`. Only use `~/.claude/settings.json` for hooks the user explicitly wants across all projects.
- If a hook involves secrets (API keys, webhook tokens), use `.claude/settings.local.json` instead and warn the user not to commit it.
- For PostToolUse auto-formatting hooks, extract the specific file path from `tool_input` and only format that file — never the entire project. This also prevents infinite loops: the formatter runs on the file but does not trigger another Write event because it runs outside Claude Code.
- For async operations (logging, notifications), set `"async": true` on the handler. Never use async for safety/blocking hooks.
- PreToolUse is the ONLY event that can deny tool calls. Do not attempt to block actions via PostToolUse.
- Matchers are regex strings. Use `|` for multiple tools: `"Write|Edit"`.

### Hook Implementation Details Per Menu Item

**1. Block dangerous commands**: PreToolUse, matcher "Bash", command hook. Script extracts `.tool_input.command`, checks against patterns (rm -rf, DROP, DELETE FROM, git push --force, git reset --hard, chmod -R 777). Returns deny decision via JSON output on stdout.

**2. Protect paths**: PreToolUse, matcher "Write|Edit", command hook. Script extracts `.tool_input.file_path`, checks against user-specified protected paths. Denies if match.

**3. Command allowlist**: PreToolUse, matcher "Bash", command hook. Script extracts `.tool_input.command`, checks first word against allowed commands list. Denies if not in list.

**4. Auto-format**: PostToolUse, matcher "Write|Edit", command hook, async false. Script extracts `.tool_input.file_path`, runs formatter on that specific file.

**5. Auto-lint**: PostToolUse, matcher "Write|Edit", command hook. Script extracts file path, runs linter, outputs lint errors to stderr on exit 2 so Claude sees them and can fix.

**6. Auto-test**: PostToolUse, matcher "Write|Edit", command hook. Script extracts file path, derives test file path using project convention, runs test if test file exists.

**7. Desktop notification**: Notification event (for attention) + Stop event (for completion). On macOS: `osascript -e 'display notification'`. On Linux: `notify-send`.

**8. Sound alert**: Stop event, async true. On macOS: `afplay /System/Library/Sounds/Glass.aiff`. On Linux: `paplay` or `aplay`.

**9. Slack/webhook**: Stop event, async true. Script POSTs a JSON payload to the webhook URL via curl.

**10. Auto-inject context**: SessionStart event, command hook. Script cats a file or runs a command, outputs to stdout. SessionStart stdout is added as context Claude can see.

**11. Prompt validator**: UserPromptSubmit event, command hook. Script extracts `.user_prompt`, checks against rules. Exit 2 to reject with reason.

**12. Git status injection**: UserPromptSubmit event, command hook. Script runs `git branch --show-current` and `git status --short`, outputs to stdout. UserPromptSubmit stdout is added as context.

**13. Command logger**: PostToolUse, matcher "Bash", async true. Script extracts `.tool_input.command`, appends to log file with timestamp.

**14. Change tracker**: PostToolUse, matcher "Write|Edit", async true. Script extracts `.tool_input.file_path`, appends to log file with timestamp.

**15-18**: Build from the reference above based on user specifications.

**19. Custom**: Map the user's description to the correct event, matcher, and handler type using the reference table.

## Step 4: Write Files

1. Create `.claude/hooks/` directory if it doesn't exist
2. Write each helper script to `.claude/hooks/[name].sh`
3. Run `chmod +x` on each script
4. Merge the generated hook entries into the appropriate settings.json (project or global), preserving any existing hooks
5. If `.claude/settings.local.json` is needed (secrets), create it and remind the user to add it to `.gitignore`

## Step 5: Verify and Report

After writing all files:

1. List every hook installed with its event, matcher, and what it does
2. Show the complete settings.json that was written
3. Remind the user: "Restart Claude Code or start a new session for hooks to take effect. Hooks are snapshotted at startup."
4. If any hooks use jq, verify it's installed: `command -v jq`
5. If jq is missing, tell the user how to install it

## Important: Avoid These Mistakes

- Do not generate a PostToolUse hook on Write|Edit that itself writes files — this creates an infinite loop. Formatters and linters run as external processes and their file modifications don't trigger Claude Code hooks, so they're safe.
- Do not use exit code 2 for PostToolUse hooks expecting to "undo" an action — PostToolUse cannot block, the action already happened.
- Do not put secrets in `.claude/settings.json` — use `.claude/settings.local.json` for anything with API keys or tokens.
- Do not forget to quote `$CLAUDE_PROJECT_DIR` in command strings — paths may contain spaces.
