---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Keeping this repo current

Anyone with this Mac's Dropbox can update it: Claude Code opened at this folder, a Cowork session with the Dropbox folder selected, or Ken by hand. The procedure is the same.

## When
- After Ken saves a skill update, or changes a task prompt.
- After a rule change or Ken decision shows up in a state file.
- Otherwise about monthly, to refresh the generated history and the status block.

## Steps
1. Read Dropbox `AI Agents/README.md` version line first (shared-memory rule). Then this file.
2. Run the sync:
   ```bash
   python3 scripts/sync_from_dropbox.py
   ```
   It reads the Dropbox folders and the synced skill, regenerates `history/RUN-LOG.md` and `history/STATUS-LOG.md`, refreshes the redacted copies under `skill/` and `runs/`, writes `history/OPEN-ITEMS.generated.md` from the latest state file, and prints: the latest state file name, any skill or prompt text that changed since the last commit, and RULE CHANGES LOG lines dated after the last sync date in `CHANGELOG.md`.
   Without this Mac (Cowork with only the Dropbox connector): read the files it would read, listed in `README.md` under "Where the live pieces are", and do steps 3 to 6 by hand.
3. For each new rule change or Ken decision: add a dated entry to `history/DECISIONS.md` with the reasoning as the state file gives it, and fold the rule into `rules/RULEBOOK.md` in the right section with its date tag. If the skill now contains a rule the RULEBOOK marked "state-carried", change the tag.
4. Rewrite `history/OPEN-ITEMS.md` from the generated file, keeping the numbering the state file uses.
5. Update the status block at the top of `README.md` (date, trade count, realized, last V, regime) from the latest state file.
6. If the architecture changed (new task, new connector, new file rule), update `SYSTEM.md` and `ops/RUN-ORDER.md`.
7. Append a `CHANGELOG.md` entry: date, what changed, which Dropbox files it came from.
8. Learnings (`CONTRIBUTING.md`): review any open pull request under `learnings/proposed/`. Decide with `python3 scripts/learnings.py review <id> --accept|--decline|--trial --note "..."`, merge, then fold an accepted learning into `rules/RULEBOOK.md` with a `[community]` tag and the learning id, and add it to the current `runs/SKILL-UPDATE-PROMPT-<date>.md`. Name it in `CHANGELOG.md` with its author. When a Sunday scout of this account printed a LEARNING PROPOSAL block, file it the same way (`propose`, author `ken-hq`).
9. Data: publish this account's run records (the runs write them to `Claude/Storage/Ken HQ/Double Project/repo-records/` once the skill update is saved):
   ```bash
   python3 scripts/publish_data.py publish --handle ken-hq --source "<Dropbox>/AI Agents/Claude/Storage/Ken HQ/Double Project/repo-records"
   ```
   then review any open `Data:` pull request from another operator (no account identifiers, headers match `data/README.md`) and merge it; the scoreboard regenerates on each publish.
10. Commit with explicit paths, never `git add -A`. The git folder is in Dropbox: commit from one Mac at a time and push after each commit if a remote exists.
   ```bash
   git add README.md CHANGELOG.md rules/RULEBOOK.md history/
   git commit -m "Sync YYYY-MM-DD: <what changed>"
   ```
11. Shared-memory close: write a `Claude/Log/` file for the session, and if Ken decided something, a Decisions Log row in Notion.

## What not to do
- Do not write to the Dropbox state or status folders from here.
- Do not change the live skill from here. A rule change goes to Ken as a skill update; this repo records it.
- Do not add the account number anywhere. The sync script redacts it; keep it that way.
- Do not "clean up" the history files. They are the record; append, do not rewrite.

## Giving this to another AI or person
Hand over the folder or the repo URL. `README.md` then `SYSTEM.md` then `rules/RULEBOOK.md` is the reading order. `analysis/` holds the assessments; add a new dated one rather than editing an old one.
