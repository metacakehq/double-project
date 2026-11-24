---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Contributing a learning

This repo takes one kind of contribution from operators: a learning, which is a pattern your installed copy found in its own closed trades, with the mechanism named and a specific change proposed. Rule edits, prompt edits and new features go through the maintainer; open an issue to discuss them.

Maintainer: Ken Ott (`metacakehq`). The maintainer accepts, declines or trials learnings and folds accepted ones into `rules/RULEBOOK.md` and the next skill update.

## The automatic part
Once the skill in `skill/double-project-trading/SKILL.md` is installed per `INSTALL.md`, your Sunday scout already does the work. When its pattern read (rules/LEARNING-LOOP.md §2) finds something that clears the proposal threshold (§3), it prints a `LEARNING PROPOSAL (for the shared repo)` block at the end of its report, in the portable form of §6: counts, percent of V and ATR multiples, no account identifiers, no dollar figures. If it finds a pattern that does not yet clear the threshold, it prints the same block marked `status at source: idea`.

## The part you do (two minutes)
1. Copy the block from the scout's report into a file, or straight to stdin.
2. From a clone of this repo on the main branch:
   ```bash
   python3 scripts/learnings.py propose block.txt --pr
   ```
   The script checks the required fields, refuses any 9-digit number and any `$` amount, writes `learnings/proposed/<date>-<your handle>-<slug>.md`, rebuilds `learnings/INDEX.md`, creates a branch `learning/<id>`, commits, pushes and opens the pull request with `gh`. Without `--pr` it only writes the file; commit and open the pull request by hand.
3. If you do not have write access, fork once with `gh repo fork --remote`, then push the branch to your fork and run `gh pr create`. The script prints these steps if its push is refused.
4. No git on your machine: open an issue with the "Learning proposal" template and paste the block. The maintainer files it for you.

Your handle goes into the file as `author`. Use your GitHub login or any stable name; it is how repeat lessons from the same account are told apart from the same lesson seen by many accounts, which is the signal this folder exists to find.

## What the review checks
- Threshold: 4 or more trades (3 for bear funds), or honestly marked `idea`.
- Mechanism named: which rule produced the outcome.
- One specific change, one area, with an expected cost and a way to judge it.
- Privacy: no account identifiers, no dollar figures, nothing that identifies a person. Tickers and dates are fine.
- Not already covered: the maintainer checks `learnings/INDEX.md` and `rules/RULEBOOK.md`. A duplicate is still useful; it is merged as a second author on the existing learning's evidence rather than declined.

Review happens on the pull request. The maintainer records the decision with
```bash
python3 scripts/learnings.py review <id> --accept --note "why" --trades 7
```
(or `--decline`, or `--trial --review-by 2026-12-31`), which moves the file and writes the Decision section, then merges. Tightening learnings can be accepted on the evidence. Loosening learnings need the maintainer's explicit yes, the same rule the live system applies to itself.

## After acceptance
The maintainer adds the rule to `rules/RULEBOOK.md` with a `[community]` tag and the learning id, and to the next `runs/SKILL-UPDATE-PROMPT-<date>.md`. Each operator decides whether to paste that prompt into their own run session; this repo recommends rules, it never pushes them into anyone's account. The changelog names every accepted learning and its author.

## What never goes in a pull request
Account numbers, balances, order IDs, per-trade dollar results, state files, status files, screenshots of the brokerage. The sync script and the `.gitignore` keep Ken's own figures out; the same standard applies to everyone.
