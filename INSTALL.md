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

Budget about two hours for setup, plus a day for brokerage funds to settle. Do the steps in order; each one is checked in the final checklist.

## 0. Accounts and connections
Everything below is done once, before the skill or the tasks exist.

1. **Robinhood account for the agent.** The system runs on a Robinhood cash account enabled for agentic trading (Robinhood calls it an Agentic account), separate from any account you trade by hand. Open it in the Robinhood app, cash account not margin: the rules assume settled funds and T+1 settlement, and the "settled funds only" rule in the skill depends on it. Fund it with what you are prepared to run the rules on and wait for the deposit to settle. The rules were written for about $1,000 and whole shares; the concentration band, the floor and the share-granularity notes assume that scale (SYSTEM.md §4). If you plan to use the long-call allowance (skill rule 7), the account needs options approval at Level 2; if not, leave options off and the rule simply never fires.
2. **Robinhood connector in claude.ai.** In claude.ai, Settings, Connectors, add the Robinhood connector and sign in with the Robinhood login that owns the agentic account. Then, in any chat, ask Claude to run `get_accounts` and note the identifier of the agentic account exactly as it is returned. That string replaces `<ACCOUNT>` everywhere. Confirm it is the agentic cash account and not another one on the login; the skill names one account and trades only in it.
3. **Storage connector.** Add the Dropbox connector (or another file store; the two prompts assume Dropbox). Create two folders: one for state files (positions and balances, sensitive) and one for status files (no figures). In a chat, ask Claude to list the state folder through the connector and note the path it uses to reach it. Dropbox team accounts expose a namespace path of the form `ns:<number>//...` and the team root is not writable, which is why the prompts carry both the namespace path and the display path. Replace both with yours.
4. **Scheduled tasks.** Confirm your claude.ai plan offers scheduled tasks and that a scheduled task can be given connectors. The runs are two tasks; a plan without them cannot run the system unattended.
5. **GitHub.** Access to this repo (ask the maintainer), plus `git` and the `gh` CLI if you want the two-minute learning flow in `CONTRIBUTING.md`. Not needed to trade.

## 1. The skill
1. Take `skill/double-project-trading/SKILL.md`. Replace every `<ACCOUNT>` with the identifier from step 0.2.
2. Read the "Campaign started" line and the control numbers: set your own start date, start value and goal. The floor F and the HWM formula derive from the start value, so change them together.
3. Read `rules/RULEBOOK.md` in full. It is the complete current rule set, including rules the skill text may not yet carry (tags `[state]`, `[practice]`, `[trial]`). The latest `runs/SKILL-UPDATE-PROMPT-<date>.md` tells a session how to fold those into the skill; run it on your copy after installing, or edit the text in first.
4. Create the skill in claude.ai (Settings, Skills, upload or paste), named `double-project-trading`.

## 2. The two scheduled tasks
Create them from `runs/daily-run.md` (weekdays, your market-open hour in UTC; the prompt chains 12:45, 15:30 and 16:05 ET into the same session) and `runs/weekly-scout.md` (Sunday, no orders). In each prompt replace: the storage namespace and display paths from step 0.3, the account identifier, and the operator name. Keep everything else. Model: the strongest available; these runs decide trades. Attach the Robinhood and storage connectors to each task.

## 3. First run, by hand
Before the schedule fires, start the daily task yourself on a weekday morning (or run its prompt in a chat with the same connectors) and watch it:
- It must read your account with `get_portfolio` and quote V, HWM and F correctly for your start value.
- When the session asks for tool permissions, choose "Always allow" for the Robinhood order tools (place and cancel), the storage connector and the scheduling tool. Without this the run stalls on the permission check at the exact moment it needs to place a stop (SYSTEM.md §9 item 4, `ops/OPERATING-NOTES.md`). If a rule-compliant order is still blocked later, the skill's order-block rule says what the run does and reminds you of this setting.
- It must create a new dated state file and a status file in your folders, and schedule the midday wake-up quoting a trigger id. Check the files exist and that the state file names your account correctly.
Expect it to sit in cash unless a setup qualifies; cash is the position when nothing qualifies. Then let the schedule take over.

## 4. First week
Read every report. The first scout will find no closed trades and backfill nothing; that is correct. If a report ever implies the goal is near, that is a reporting failure and the skill's honesty rule has been dropped somewhere. If the daily chain misses a wake-up, `ops/OPERATING-NOTES.md` has the send_later notes (absolute UTC times, never a computed delay).

## 5. Learnings
Nothing to set up. Once the skill carries the learning loop, your Sunday scout prints a `LEARNING PROPOSAL (for the shared repo)` block whenever your trades show a pattern that clears the threshold. `CONTRIBUTING.md` says how to push it back here in two minutes, and what the review checks. Accepted learnings reach you as the next skill-update prompt; whether to apply them to your copy is your call.

## Checklist
- [ ] Agentic cash account open, funded, deposit settled; options level set only if long calls will be used
- [ ] Robinhood connector added; account identifier copied from `get_accounts`
- [ ] Storage connector added; state and status folders created; namespace and display paths noted
- [ ] Plan has scheduled tasks with connectors
- [ ] Skill created with `<ACCOUNT>`, start date, start value and goal replaced
- [ ] Rulebook read; skill-update prompt applied or rules edited in
- [ ] Two tasks created with paths, account and operator name replaced; connectors attached; strongest model
- [ ] First run watched: V, HWM, F correct; "Always allow" granted on order, storage and scheduling tools; state and status files written; next wake-up scheduled
- [ ] Repo access and `gh` set up, if you will contribute learnings

## What stays with the original operator
`scripts/sync_from_dropbox.py`, the `history/` generated files and the status block in `README.md` read Ken's Dropbox and describe his account. They are not needed to run the system. If you keep your own fork current from your own store, write your own sync for your paths and keep your figures out of commits the same way (`.gitignore`, redaction).

## What this guide cannot tell you
Robinhood's and claude.ai's screens change. This guide names what each step must end with (an agentic cash account identifier, a connector that answers `get_accounts`, a writable storage path, a task with connectors attached), not which buttons to press. If a step's outcome differs from what is described here, stop before the first run and sort it out; the system assumes every outcome above.
