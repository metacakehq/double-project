---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Assessment of the Double Project system, 2026-11-24

Written at the first codification, from the complete Dropbox record (47 state files, 46 status files, the skill, both task prompts, the September handoff documents). The scheduled runs' chat transcripts are not on disk; where the record is thin it says so. Written for Ken and for anyone he shares the repo with.

## 1. The short version
The system works as a safety system and as a record. It has not yet worked as a doubling machine, and its own documents say so honestly. In four months it has never lost more than 6% on a trade, never left a position unprotected for more than 16 minutes, never lost its memory for more than one day, and has written down every rule change with its reasoning. Realized return is +19% on the starting capital, with 39% of that coming from two bear-fund trades in the last two weeks. The doubling goal is, by the system's own arithmetic, more than a year away at the observed pace.

## 2. What is working
1. **The protection layer.** Every loss is in the 0 to minus 6% band. The floor has never been approached (V has stayed $500 above it). The 6% and 12% caps have never been breached. Stops exist on every position at every check, and the one time one disappeared (11-02, unknown actor) the close check caught it within 20 minutes.
2. **Memory without memory.** Fresh sessions with no recollection run the account every day from one document. The write-once state file plus "what tomorrow should do" is the right design; it survived the September loss and has been clean since.
3. **Rules that cite evidence.** Each change names the trade that caused it (BAC for the stall exit, DINO for the reversal bar, TEAM and CVX for the diagnostic flags, EBAY for the tiered Flag D, SOXX for the stretch trial). The amendment logs read like a lab notebook. That is rare and worth keeping.
4. **Honesty about the objective.** The standing note refuses to let any run imply the goal is near. It has been refreshed every day.
5. **Autonomy fixed on 11-19.** Before that, a minor flag could park the account for days waiting on Ken (10-14 to 10-18, 10-19 to 10-28, 11-02 to 11-04, 11-17 to 11-19: about 19 trading sessions of halted entries in six weeks). Ken's 11-19 decision removed the whole class.
6. **The bear-fund playbook.** Two for two in a DEFENSE tape, both exits at the profit zone, both inside the rules. This is the first part of the system to show convexity.

## 3. What is not working, or not yet
1. **Throughput.** Seventeen trades in seventeen weeks. The documented constraint since August is too few qualifying entries, not too many: share granularity in a $1,100 account, the extension cap, earnings blackouts, flag halts, and three permission blocks. The band widening (08-30), the flag redesign (09-28), the tiered Flag D (11-19) and the stretch trial (11-22) are all attempts to widen the funnel without loosening protection. The record shows the funnel is still the problem.
2. **Long winners are small.** Average long win about $20; no long has ever reached the +20% scale-out. Longs have exited by raised stops or gap-downs every time. The stop ladder locks in gains early, which is why losses are tiny, but it also caps upside. Whether tighter trailing costs more than it saves is untested; the 11-18 practice note (tight initial stops shaken out) is the first evidence pointing one way.
3. **Skill drift.** Eight rules in force are not in the skill (see `history/OPEN-ITEMS.md` item 1). The state file carries them, so nothing is lost, but a fresh run reading the skill alone would run old rules for bear funds, trailing and Flag D clearing. This is the one maintenance item that creates real operating risk.
4. **The permission block.** The Claude session blocked order placement five times in two weeks; three entries were missed. The runs handle it correctly (report, do not retry) but the fix is outside the system. Until it is structural, "autonomous" has an asterisk.
5. **Scout coverage.** The Sunday IPO and new-instrument search has returned "no readable results" most weeks. Estimate-revision trends cannot be verified with the tools available. The PEAD screen does what it can; two of its qualifiers have been entered since October (none the record attributes to a scout pick, actually: KR and EBAY came from the momentum scan). The scout's main value has been rule proposals and the position review.
6. **Operating cost.** Four Opus sessions a weekday plus Sunday, each loading a 30 KB skill and a 19 KB state file. The record does not carry token or dollar cost. Worth measuring once before deciding the system should run for another year.

## 4. Risks to name
1. A real stop-layer failure that looks like slippage can now run two more events before anything halts (accepted on 11-19; the 6% and 12% caps bound it).
2. Two sessions trading the same account. The prompts guard against it (never schedule tomorrow's run), and it has not happened, but it is the failure mode that would hurt most.
3. Leveraged 3x funds as core positions in DEFENSE. The rules handle decay and mean reversion with the +10 to 15% exit and the stretch cap; a gap against a 3x fund is still the largest single-day risk the account takes.
4. Account number in two Dropbox files and the skill. Redacted here. Keep it that way if the repo is shared.
5. Dependence on one operator's honesty in evaluating the flags (the 09-28 amendment says this itself).

## 5. Recommendations, in order
1. **Save the skill.** Merge `rules/RULEBOOK.md` into the live skill so the skill and the state file say the same thing. Twenty minutes, removes the only drift that could misdirect a run.
2. **Fix the permission block structurally** or, if it cannot be allowed for scheduled runs, make the Daily Run treat a block as a known condition with a defined fallback (for example, hold the entry plan in the state file and let the next run retry once at the open).
3. **Decide the floor question.** It has been open since September and it gates the one lever (long calls, premium at most 15% of V) with doubling-scale upside. A decision either way is better than the current state, where the lever exists on paper and never fires.
4. **Measure the cost of a trading week** and write it into the state file once. The honesty note about the objective should include what the system costs to run.
5. **Run the stretch trial to its review date** (3 trades or 2026-12-20) before any other bear-fund change. One rule change at a time is how the record stays readable.
6. **Give the long side one controlled experiment**: wider initial stops (the item 9 practice) for the next five long entries, judged on exits, before touching the scale-out.

## 6. What this repo adds
Before today the system was explained in five places (skill, two prompts, the latest state file, the canon pointers) and understood fully by nobody who had not read all 47 state files. This repo puts the rules in one document with provenance tags, the decisions in order with reasoning, the ledger in one table, and a script that keeps it current. It is also the first place the drift between the skill and the state file is written down as a list.
