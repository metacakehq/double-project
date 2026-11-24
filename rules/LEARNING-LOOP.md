---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# The learning loop: how the system learns from wins and losses

Ken, 2026-11-24: the system should learn from its wins and failures on its own and suggest improvements. Today it does this informally: the state file records "practice notes" and "evidence" lines, and the Sunday scout proposes rule changes when the week produced evidence. This document makes that a procedure with a fixed record, so patterns are found by looking at data, not by whoever remembers. It is written to be pasted into the skill (see `runs/SKILL-UPDATE-PROMPT-2026-11-24.md`).

## 1. One record per closed trade (close report, same day)
When a position closes, the close report appends one TRADE REVIEW block to the state file's TRADE REVIEWS section. Fields, every one filled, "n/a" allowed:
```
TRADE REVIEW <ticker> <entry date> -> <exit date>
  Result: <+/- $ and %> | Hold: <sessions> | Vehicle: long | bear fund | option
  Setup: momentum scan | PEAD day 1-2 | bear pullback | bear breakdown | rotation | other
  Regime at entry: OFFENSE | NORMAL | DEFENSE | Flags live at entry: <list or none>
  Entry test at entry: ADX <v>, EMA distance <x ATR>, bar quality <note>
  Initial stop: <x ATR below entry>; risk <$ and % of V>
  Exit type: stop (gap) | stop (intraday) | raised stop | profit zone | trend break | stall | rotation | earnings trim
  Max favorable excursion: <+% peak vs entry> | Max adverse: <-% trough vs entry>
  Rule that decided the exit: <rule name and section>
  What worked: <one line> | What did not: <one line>
  Candidate lesson: <one line, or "none">  Tags: <free tags, e.g. tight-stop, gap, ecommerce, 3x>
```
Max favorable and adverse excursion come from 30minute bars over the hold. These two numbers are what make "would a wider stop have paid" answerable instead of argued.

## 2. Weekly pattern read (Sunday scout, new section 6)
The scout reads every TRADE REVIEW block (all time, not just the week) and answers these with counts, not impressions:
1. By exit type: how many stop-outs were later recovered (price back above entry within 5 sessions)? That is the shake-out rate; it tests the stop ladder and the initial-stop minimum.
2. By setup: win rate and average result for each setup type. Any setup with 4 or more trades and a negative average is named.
3. By stop distance: average result for initial stops under 0.5x ATR, 0.5 to 1.0x, over 1.0x.
4. Max favorable excursion versus realized: how much of the average winner's peak was kept? Under 50% for 5 or more winners is evidence the trailing is too tight.
5. By regime and vehicle: longs in DEFENSE versus bear funds in DEFENSE.
6. Repeat lessons: the same "candidate lesson" tag appearing 3 or more times.

## 3. From pattern to proposal
A pattern becomes a PROPOSAL only when: it rests on 4 or more trades (3 for bear funds while the sample is small), the mechanism is named (which rule produced the outcome), and the change is specific (a number, a threshold, a step). The proposal states the evidence counts, the expected cost, and how it will be judged (which field in future TRADE REVIEW blocks). Proposals that tighten may be adopted as practice by the daily run; proposals that loosen go to Ken. One rule change at a time per area; a change gets a review date and a tag in the RULE CHANGES LOG, like the stretch trial.

## 4. Scoreboard the scout keeps
A short table in the state file, refreshed every Sunday: trades, wins, losses, win rate, average win, average loss, payoff ratio, shake-out rate, kept-excursion ratio, trades per week, realized pace per week against the pace the goal needs. The honesty note about the objective cites this table.

## 5. Backfill
The first scout after this is adopted writes TRADE REVIEW blocks for the 17 closed trades to date from the state files' run logs (excursions from historicals), so the pattern read starts with a sample instead of waiting months.
