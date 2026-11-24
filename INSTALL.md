---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Installing the system on your own account

This is what it takes to run the Double Project rules on a brokerage account of your own, with Claude as the operator, and to feed what your runs learn back into this repo. Read all of it before the first run. It trades real money without per-trade approval. You are the operator: every "Ken" in the skill and the prompts is a placeholder for you, and the authorizations in the text are yours to give or not give. Nothing here is investment advice; it is a rule set and the machinery to run it.

## What you need
- A claude.ai plan with scheduled tasks, the Robinhood connector and a file-storage connector (Dropbox is what the prompts assume; another store works if the two prompts are edited to match).
- A Robinhood cash account enabled for agentic trading, funded with what you are prepared to run the rules on. The rules were written for about $1,000 and whole shares; the concentration band and the floor assume that scale (SYSTEM.md §4).
- A GitHub account with access to this repo, and `git` plus the `gh` CLI if you want the two-minute learning flow in `CONTRIBUTING.md`.

## 1. The skill
1. Take `skill/double-project-trading/SKILL.md`. Replace every `<ACCOUNT>` with your own Robinhood account identifier, exactly as `get_accounts` reports it.
2. Read the "Campaign started" line and the control numbers: set your own start date, start value and goal. The floor F and the HWM formula derive from the start value, so change them together.
3. Read `rules/RULEBOOK.md` in full. It is the complete current rule set, including rules the skill text may not yet carry (tags `[state]`, `[practice]`, `[trial]`). The latest `runs/SKILL-UPDATE-PROMPT-<date>.md` tells a session how to fold those into the skill; run it on your copy after installing, or edit the text in first.
4. Create the skill in claude.ai (Settings, Skills, upload or paste), named `double-project-trading`.

## 2. Storage
Create a folder for state files and a folder for status files in your store. The prompts use Dropbox namespace paths (`ns:<number>//...`); replace them with your own, display path included. Keep the write-once rule: one new dated state file per run, never overwrite. State files are sensitive (positions, balances); status files carry no figures.

## 3. The two scheduled tasks
Create them from `runs/daily-run.md` (weekdays, your market-open hour in UTC) and `runs/weekly-scout.md` (Sunday). Replace the storage paths and the operator name, keep everything else. Model: the strongest available; these runs decide trades. Attach the Robinhood and storage connectors to each task.

On the first run of each task, when the session asks for tool permissions, choose "Always allow" for the Robinhood order tools (place and cancel) and for the scheduling tool. Without this the daily run will stall on the permission check at the exact moment it needs to place a stop (SYSTEM.md §9 item 4, `ops/OPERATING-NOTES.md`).

## 4. First week
Expect the first scout to backfill nothing (no trades yet) and the first daily runs to sit in cash unless a setup qualifies; cash is the position when nothing qualifies. Read every report. If a report ever implies the goal is near, that is a reporting failure and the skill's honesty rule has been dropped somewhere.

## 5. Learnings
Nothing to set up. Once the skill carries the learning loop, your Sunday scout prints a `LEARNING PROPOSAL (for the shared repo)` block whenever your trades show a pattern that clears the threshold. `CONTRIBUTING.md` says how to push it back here in two minutes, and what the review checks. Accepted learnings reach you as the next skill-update prompt; whether to apply them to your copy is your call.

## What stays with the original operator
`scripts/sync_from_dropbox.py`, the `history/` generated files and the status block in `README.md` read Ken's Dropbox and describe his account. They are not needed to run the system. If you keep your own fork current from your own store, write your own sync for your paths and keep your figures out of commits the same way (`.gitignore`, redaction).
