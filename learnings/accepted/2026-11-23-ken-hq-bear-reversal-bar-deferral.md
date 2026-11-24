---
id: 2026-11-23-ken-hq-bear-reversal-bar-deferral
date: 2026-11-23
author: ken-hq
area: entry
direction: tightening
status: accepted
trades: 2
review_by: 2026-12-20
rule_touched: Universal entry test, test 4 (reversal-bar deferral), new 4b
title: No bear-fund entry within one session of an outsized up bar on the underlying
---
# No bear-fund entry within one session of an outsized up bar on the underlying

## Pattern
The entry tests for bear funds measure distance below the falling 20d EMA. A violent one-day rebound in the underlying pulls it back inside the cap and turns the tests green at the exact moment the short-term direction has reversed against the trade. The long side already had this rule (test 4, adopted 2026-09-28 after DINO); the bear side did not.

## Evidence
Two events, one per side. DINO (long, 2026-09): bought the day after a wide outside reversal on heavy volume, stopped out on day two; that produced test 4. SOXX +13.6% and QQQ +7.0% on 2026-11-23, both closing near their highs: the bear-fund tests turned green only because of the rebound. Counted as events, not trades, because the rule exists to prevent the trade. Below the 4-trade threshold; adopted as a tightening on 11/23.

## Mechanism
Test 3 and P5 read a level (distance from the EMA) and not the bar that produced it. A rebound bar with true range over 2x ATR14 that closes in its top two-thirds is the strongest short-term up signal the data has, and the level tests cannot see it.

## Proposed change
Test 4b: no bear-fund entry within 1 session of an underlying up bar whose true range, including the gap from the prior close, exceeds 2x ATR14, unless that bar closes in the bottom third of its true range. If such a bar is still forming, the entry may be taken late in the session only if it is closing in the bottom third.

## Expected cost
If the rebound fails the next day, the rule cost that entry. On a trend that resumes immediately, one session of continuation is missed.

## How to judge
For deferred entries, record what the fund did over the next 2 sessions in the state file. Review at the 2026-12-20 scout: deferrals that avoided a loss against deferrals that cost a winner.

## Source
Status at source: adopted as tightening 2026-11-23, stands unless the operator reverses (open item 11).

## Decision
2026-11-24, maintainer (ken-hq): accepted. In `rules/RULEBOOK.md` universal entry test [practice], queued for the skill in `runs/SKILL-UPDATE-PROMPT-2026-11-24.md` item 3.
