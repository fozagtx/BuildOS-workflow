---
name: bounty-workflow
description: "Authorized bug-bounty loop: pick a program, lock scope, recon, proof, report. Use when hunting bounties, triaging a program, or writing a submission."
version: 1.0.0
author: zanbuilds
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Security, BugBounty, Pentest, Report]
    related_skills: [web-pentest, dogfood, oss-forensics, github, domain-intel]
---

# Authorized bug-bounty workflow

Use this as the outer loop. Delegate live web testing to `web-pentest`. Delegate product-click QA to `dogfood`. Never skip the authorization gate.

## When to use

The operator says hunt, bounty, HackerOne, Bugcrowd, Immunefi, "find vulns", or names a program/asset.

## Inputs

1. Program URL or name
2. In-scope assets (hosts, apps, repos)
3. Out-of-scope list
4. Authorization basis (program terms + operator `authorized`)
5. Time box

## Procedure

1. Create `workspace/engagements/engagement-YYYYMMDD-HHMMSS/{evidence,findings,reports}`.
2. Quote the program scope into `scope.txt`. Refuse anything not listed.
3. Ask verbatim: "Confirm: (a) target is [X], (b) you have written authorization via [program], (c) window is [N] hours. Reply `authorized` to proceed."
4. Stop unless the reply is exactly that acknowledgement. Write `authorization.md`.
5. Recon, read-only first (headers, tech, repos, public advisories). Then `web-pentest` for live apps.
6. Verify with a non-destructive witness. No exploit, no report.
7. Write `reports/submission.md` using the pentest-report template: title, severity, CWE, asset, proof, impact, fix. L3/L4 only in the submit pile.
8. Do not file on any platform until the operator says to send.

## Output

A folder with scope, authorization, evidence, and a submission-ready report. Chat stays redacted.
