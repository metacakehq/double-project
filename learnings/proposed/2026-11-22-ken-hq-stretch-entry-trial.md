---
id: 2026-11-22-ken-hq-stretch-entry-trial
date: 2026-11-22
author: ken-hq
area: entry
direction: loosening
status: trial
trades: 0
review_by: 2026-12-20
rule_touched: Universal entry test, test 3 (P5 bear-fund extension cap), new 3b
title: Stretch entry for bear funds between 1.5x and 2.0x ATR below the falling 20d EMA
---
# Stretch entry for bear funds between 1.5x and 2.0x ATR below the falling 20d EMA

## Pattern
In a strongly trending down tape the P5 cap (underlying no more than 1.5x ATR14 below its falling 20d EMA) blocks the continuation day, which in a 3x fund is the biggest day of the move.

## Evidence
One day. 2026-11-20: the cap kept the account out of SOXS (+32.1% on the day) and SQQQ (+16.5%) for the whole session while both qualified on every other test. The 2026-11-22 scout kept the base cap and proposed a bounded trial instead of removing it. Below threshold; approved by the operator as a trial.

## Mechanism
The cap exists to avoid buying the underlying's exhaustion low, where a bear fund gets stopped on the snap-back. But distance from the EMA alone does not distinguish exhaustion from acceleration. Trend strength does: a rising ADX14 over 25 on the underlying says the move is accelerating, not exhausting.

## Proposed change
Test 3b: underlying between 1.5x and 2.0x ATR14 below its falling 20d EMA is enterable only if the underlying's ADX14 is above 25 and has risen 3 consecutive sessions. Size 7.5 to 12.5% of V; if no integer share count fits, no entry. Initial stop at least 1.0x the fund's ATR14 beyond a structure level. Exits unchanged. No pyramiding while the underlying is beyond 1.5x. Max one stretch position. Tag STRETCH in the state file. Beyond 2.0x stays blocked.

## Expected cost
A stretch entry on the day the move exhausts is stopped on the snap-back, at up to 12.5% of V sized, so the loss per event is bounded by the smaller size.

## How to judge
After 3 STRETCH-tagged trades or on 2026-12-20, whichever first: win rate and average result of STRETCH trades against ordinary bear entries, and their max adverse excursion.

## Source
Status at source: trial approved by the operator 2026-11-22 11:24 CT. Loosening, so it needed an explicit yes. Account band under $2,000, whole shares.

## Decision
2026-11-24, maintainer (ken-hq): trial. Stays in `proposed/` with status `trial` until the review date; in `rules/RULEBOOK.md` as [trial] and queued for the skill in `runs/SKILL-UPDATE-PROMPT-2026-11-24.md` item 2.
