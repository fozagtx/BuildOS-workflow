---
name: glaze-context-gather
description: Gather context from project memory, guides, and codebase before implementation. Use when starting new features, complex changes, or when you need to understand existing patterns. Triggers on "gather context", "check what exists", "explore the codebase", or any task that needs codebase understanding before coding.
context: fork
model: haiku
agent: Explore
allowed-tools: Read Grep Glob
argument-hint: '"<glaze-app-guide-path>" "<task description>"'
arguments:
  - guide_path
  - task
---

Gather context for this task: $task

Glaze App Guide path: `$guide_path`

Raw invocation arguments: $ARGUMENTS

## Scope And Search

- Work only from the provided paths and context.
- Keep searches and reads inside `.glaze-sources/`, `$guide_path`, and other explicit `<runtime_context>` paths such as provided log paths.
- Never search home directories, iCloud, OneDrive, or paths outside those explicit scopes.
- Never run broad `find` commands such as `find /`, `find ~`, `find /Users`, or similar full-home/full-disk scans; they can trigger macOS privacy permission prompts.
- Use only `Grep`, `Glob`, and `Read` for searches and reads.
- If required information is missing, report it instead of widening the search.
- Batch independent reads and searches in one turn; sequence only when a call depends on a prior result.

## Sources (in priority order)

### 1. Project Memory

Read `.glaze_memory/PROJECT-CONTEXT.md` only when it is already known to exist, and extract only task-relevant current state and recent history. If it is absent or unknown, report "No project memory yet" and continue with the guide and code.

### 2. App Guide

Read the Glaze App Guide at `$guide_path`. Use `Read` with `offset` and `limit` to read only relevant sections — never read the full guide. If `$guide_path` is missing or equals `(not found)`, report "Glaze App Guide path unavailable" and continue with project memory and code only; do not search for the guide.

**Guide section index (line numbers → use as offset):** | Section | Lines | When to read | | Critical Rules | 52-72 | Always | | Decision Trees | 73-105 | Always | | Overview / Architecture | 106-129 | Often | | Backend (handlers, services) | 130-519 | Backend tasks | | Window Management | 147-302 | Window tasks | | Adding Backend Handlers | 303-336 | New IPC handlers | | Global Shortcuts | 337-374 | Hotkey tasks | | System Notifications | 375-408 | Notification tasks | | System Tray | 409-498 | Menu bar tasks | | Frontend (components, routing) | 520-582 | UI tasks | | Configuration | 583-616 | Config tasks | | Bundling & Publishing | 617-787 | Native modules | | Static Assets | 788-1039 | Images/fonts | | App Updates | 1040-1074 | Update/auto-update tasks | | Quick Reference / Patterns | 1075-1198 | Always | | File Modification Guide | 1199-1227 | What to edit/avoid | | Settings Convention & Cross-Window Sync | 1228-1237 | Settings/cross-window tasks | | Debugging Runtime Errors | 1238-1247 | Runtime bug tasks | | WKWebView Rendering Caveat | 1248+ | Rendering bug tasks |

If a section is not at the listed offset (guide edits shift line numbers), locate its heading with Grep instead of scanning the file.

### 3. Existing Codebase

- Check existing implementations for patterns
- Look for related code that new features should integrate with

## Output Format

```
## Context for: [Task Description]

### From Project Memory
[Relevant entries, or "No relevant history"]

### From GLAZE-APP-GUIDE.md
- Section: [name] — [relevant info]

### From Existing Code
- [file path]: [what it contains/does]

### Notable Constraints
[NEVER/ALWAYS rules, forbidden patterns found]
```

## Rules

1. Report, don't decide — no architectural recommendations or package dependecies
2. Be concise — summarize, don't dump file contents
3. Only include relevant info — skip unrelated sections
4. Do NOT read `@glaze/core` component files — component usage is out of scope here
5. Output must be under 400 words
