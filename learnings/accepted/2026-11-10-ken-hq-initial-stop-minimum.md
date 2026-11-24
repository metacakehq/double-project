---
id: 2026-11-10-ken-hq-initial-stop-minimum
date: 2026-11-10
author: ken-hq
area: exit
direction: tightening
status: accepted
trades: 1
review_by: 2026-12-20
rule_touched: Trade management, initial stop
title: Initial stop at least 1.0x ATR14 below entry, beyond a structure level
---
# Initial stop at least 1.0x ATR14 below entry, beyond a structure level

## Pattern
Stops placed inside normal daily range get hit by noise and the trade recovers without the account. The 2026-11-09 EBAY stop sat 0.21x ATR14 below entry; it filled intraday and price was back above entry the next session. The re-entry on 11/10 with the stop about 1.1x ATR below held.

## Evidence
One named shake-out (EBAY, 11/09, stop 0.21x ATR14, recovered within 1 session) and the earlier TEAM stop of 2026-09-26, a 6.4% gap that the stop could not have avoided at any distance, which is why gaps are excluded from the test. Below the 4-trade threshold; adopted as practice on 11/10 and proposed to the operator by the 2026-11-22 scout (open item 9). The backfill of TRADE REVIEW blocks will give the shake-out rate across all 17 closed trades.

## Mechanism
The 6% per-trade cap sizes the position from the stop distance, so a tight stop buys a bigger position. Nothing in the rules set a minimum distance for the initial stop, only for raises (P3 part 2, 0.5x ATR below the prior close). A stop inside 0.5x ATR is inside the day's expected movement.

## Proposed change
Initial stop at least 1.0x ATR14 below entry and beyond a structure level (swing low or the breakdown bar's high for bear funds). If that distance puts dollar risk over 6% of V, reduce the share count; if no integer share count fits, no entry.

## Expected cost
Smaller positions at the same risk, so each winner contributes less. More entries blocked on share granularity at small V.

## How to judge
Shake-out rate in the Sunday pattern read (stop-outs recovered above entry within 5 sessions) for trades entered after 2026-11-10 against those before. Review at the 2026-12-20 scout or after 4 stops under the new rule, whichever first.

## Source
Status at source: adopted as practice 2026-11-10, proposed to operator 2026-11-22. Account band: under $2,000, whole shares only, which is what makes the granularity cost real.

## Decision
2026-11-24, maintainer (ken-hq): accepted as practice, carried in `rules/RULEBOOK.md` trade management [practice] and queued for the skill in `runs/SKILL-UPDATE-PROMPT-2026-11-24.md` item 4. Evidence remains thin; the shake-out rate from the backfill is what confirms or reverses it.
