---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Shared learnings: what every operator's runs teach the system

Ken, 2026-11-24: anyone who installs this system should have their runs suggest learnings automatically, and push those learnings back into the repo themselves, so the rules improve from everyone's trades, not just one account's.

This folder is where that happens. One file per learning. The Sunday scout of every installed copy emits a `LEARNING PROPOSAL` block whenever a pattern clears the threshold in `rules/LEARNING-LOOP.md` §3. The operator turns the block into a file here with `scripts/learnings.py propose` and opens a pull request. The maintainer reviews it, and an accepted learning goes into `rules/RULEBOOK.md` with a `[community]` tag and into the skill through the next skill update.

## The lifecycle
| Folder | Status in the file | Meaning |
|---|---|---|
| `proposed/` | `proposed` | Opened by a pull request, not yet reviewed |
| `proposed/` | `trial` | Adopted as a time-boxed trial with a review date; stays here until judged |
| `accepted/` | `accepted` | Judged true on the evidence; folded into the rulebook and queued for the skill |
| `declined/` | `declined` | Judged not supported, or already covered; kept with the reason so it is not re-proposed blind |

`INDEX.md` is generated from the files by `scripts/learnings.py index`. Do not edit it by hand.

## What a learning is
A learning is a pattern in closed trades that names its mechanism and proposes a specific change. It is not an opinion about the market and not a report of one trade. The threshold is the one the system already uses for itself: 4 or more trades (3 for bear funds while the sample is small), the rule that produced the outcome, a specific number or step, the expected cost, and the TRADE REVIEW field that will judge it. A block that falls short is still welcome as `status_at_source: idea`; the maintainer will hold it in `proposed/` until more evidence arrives from any operator.

## Privacy, one rule
No account identifiers, ever: the script refuses any 9-digit number. Everything else about what the system did is community data (Ken, 2026-11-24): dollar results, account values, tickers, dates, prices. Give percent of V and ATR multiples as well, so learnings compare across accounts of different size.

## Who decides
The maintainer of this repo (Ken, or whoever he names in `CONTRIBUTING.md`) accepts, declines or trials a learning. Tightening proposals can be accepted on the evidence alone. Loosening proposals need an explicit yes from the maintainer, the same rule the live system applies to itself (SYSTEM.md §6). Each operator still decides what goes into their own installed skill; this repo recommends, it does not push rules into anyone's account.

## Format
See `TEMPLATE.md` for the file, and `rules/LEARNING-LOOP.md` §6 for the block the scout emits. The two are the same fields; the script does the conversion.
