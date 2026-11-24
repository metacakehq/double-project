---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# How the Double Project works

## 1. The idea
One AI operator, one small cash account, a written rulebook, and a human who sets the objective and approves rule changes but does not approve trades. The design question the project answers is not "can an AI pick stocks" but "can a rule-bound agent run money unattended, protect it, record what it did, and improve its own rules without drifting." Every piece below exists to make that safe and auditable.

## 2. The pieces

| Piece | Where it lives | Role |
|---|---|---|
| The skill `double-project-trading` | Claude skill, synced to claude.ai and Cowork | The rulebook. Loaded first by every run. Only Ken saves changes to it |
| Daily Run task | claude.ai scheduled task, weekdays 9:00am CT, model claude-opus-5-5 | The run order for the trading day. Chains midday, afternoon and close checks into the same session with send_later |
| Weekly Scout task | claude.ai scheduled task, Sunday about 11:00am CT | Research and planning only. Regime read, earnings screen, position review, rule proposals |
| State file | Dropbox `Claude/Storage/Ken HQ/Double Project/`, one new dated file per run | The memory bridge between runs. Full state, not a diff: control numbers, positions, stops, flags, watchlist, rejects, rule changes with reasoning, open items, what tomorrow should do |
| Status file | Dropbox `Claude/Log/`, one per run, under 15 lines, no figures | What ran and what it needs, readable by anyone, picked up by Ethan's scan into Notion |
| Robinhood MCP | connector on the claude.ai account | Portfolio, positions, orders, quotes, indicators, earnings, order placement and cancellation |
| Dropbox MCP | connector | Read the latest state file, create the new one. Create-only, never update |
| Push notification | per run | Ken gets the report. Only this routine messages Ken about itself |
| Notion | Global Operating Picture, Recent | Pointer lines only. Never positions or balances |
| Ken | chat replies, usually in the run's own session | Clears flags, rules on proposals, approves loosening of survivability rules |

## 3. The day
All times Eastern. The task fires pre-open and the first run is at the open.
1. 10:00 Morning run. Control numbers, halt check, verify every stop, manage positions, evaluate the five flags, regime, discovery, enter or not, report. Then schedule the next three checks.
2. 12:45 Midday check. Stops live, trend breaks, one line.
3. 15:30 Afternoon review. Defense pass: stops verified and raised, broken trends exited before the close, earnings trims, leveraged decay check.
4. 16:05 Close report. Daily P&L; Friday adds the weekly recap. Write the new state file and the status file.
Sunday: the scout. No orders. Writes a state file and a status file too.

## 4. The control loop
Every run computes the same two numbers before anything else.
- V, the account value.
- F, the floor: max($500, HWM minus $500), where HWM is $1,000 plus peak cumulative realized P&L. The floor only ratchets up.
If V is at or below F: cancel everything, no trades, report HALT, wait for Ken. That is the only full stop in the system.

Four survivability rules bind every action and can only be loosened by Ken: the floor, 6% of V max loss per trade, 12% of V total open risk, a live GTC stop-market order on every position at all times (fill-then-stop is atomic).

Everything else is a dial, not a stop: regime (OFFENSE, NORMAL, DEFENSE from SPY and QQQ against their 50-day EMAs), the concentration band (30 to 50% of V per core position under $2,000), discovery screens, the six-step universal entry test, the stop ladder, the stall exit, the rotation rule, and the five diagnostic flags.

## 5. What halts trading (set 2026-11-19, Ken)
Only three things: the floor, Flag D Tier 2 (a serious stop-system failure, which halts new entries only), and a closed market. Items open with Ken never block trading. This was the outcome of the project's biggest lesson: before 11/19, a minor flag could park the account in cash for days waiting for a reply.

## 6. How rules change (set 2026-09-28, Ken)
Ken's words: "you set the rules not me... your job is the objective of doubling... if a rule is not serving us then we need to reassess it" and "you have authority to adjust rules, but i do want opportunity for input." So the operator makes the call, records the reasoning in the state file, and reports it as a change in that run. A change stands until Ken reverses it. Tightening needs no approval. Loosening any of the four survivability rules needs Ken first. The Sunday scout proposes only.

Rule text has three homes, and the ordering matters:
1. The skill is the authority on trading rules.
2. The task prompts are the authority on paths and file rules (they override the skill's older state-file procedure).
3. The state file carries any rule the skill does not yet have, with a line saying so.
When a rule is approved in chat, the run writes it into the state file and shows Ken a skill update card. Until Ken saves it, the state file carries it. See section 9 for the current gap.

## 7. Memory and provenance
No run remembers the last one. The state file is the only memory, so it is written as a complete document every time: a fresh session can read the latest file and run. Dropbox is write-once, so every run creates a new dated file and nothing is ever deleted or overwritten. This replaced a delete-and-recreate procedure that on 2026-09-28 left the system with no state file at all for a period. If the state is genuinely missing, the rule is: read the live account, protect every position, take no new entries, tell Ken, rebuild state from the account, never from memory.

## 8. Who does what
- Claude (the runs): everything in the loop, including rule tightening.
- Ken: objective, floor, loosening, clearing a Tier 2 flag whose cause is unknown, saving the skill, the open questions in `history/OPEN-ITEMS.md`.
- Ethan (Grok Bot chief of staff): reads the status files on his scan and carries pointers into Notion. Never positions or balances.
- Nobody else trades in the account. One recorded event (2026-11-02) had a stop cancelled by an actor other than the run; cause never identified.

## 9. Known drift and gaps (as of 2026-11-24; items 2 and 4 have a fix waiting in `runs/SKILL-UPDATE-PROMPT-2026-11-24.md`)
1. The skill still says "NEVER use create_trigger/cron scheduled tasks" because scheduled sessions could not attach Robinhood in July. Since October the runs are scheduled tasks and Robinhood attaches. The architecture section of the skill is out of date; the task prompts are what actually runs.
2. The skill does not contain P3 (gap-open exclusion and minimum trail distance), P4 (50d EMA direction definition), P5 (bear-fund extension cap), the swing-low definition, the half-size working definition, the initial-stop minimum, the P5 stretch trial or test 4b. The state file carries them. `rules/RULEBOOK.md` merges them.
3. The skill's state-file procedure section was updated to write-once, but the task prompts still say they override it. Harmless duplication.
4. The Claude session's "real-world transactions" permission check blocked order placement on 2026-10-28 and 11/09 to 11/12. Ken's "try again" clears it per event. Ken's position (2026-11-24): the system is authorized and autonomous, so a block should only happen on a real threat; a rule-compliant order inside the four survivability rules is not one. What this repo can and cannot do about it: the check is claude.ai's own safeguard on scheduled sessions, not a rule in the skill or the prompt, so no text here switches it off. The levers are (a) the task's tool permissions on claude.ai: "Always allow" for place_equity_order and cancel_equity_order, which the skill's bootstrap step already asks for and which the update prompt tells the run to remind Ken about; and (b) the operating rule in `runs/SKILL-UPDATE-PROMPT-2026-11-24.md` item 8: verify no order was created, retry once with a fresh ref_id, then report the exact order and treat it as Flag D Tier 2 only when a fill could be left unprotected.
5. The long-call allowance (rule 7) has never been used. It is the only lever with doubling-scale convexity and is gated on the floor question, open with Ken since September.

## 10. Shared learning across operators (Ken, 2026-11-24)
The learning loop (§4 of the control loop, `rules/LEARNING-LOOP.md`) runs inside one account. Ken wants it to run across every account that installs the system: each operator's runs suggest learnings automatically, and the operator pushes them back into this repo. The design keeps the run and the repo apart. The Sunday scout prints a `LEARNING PROPOSAL (for the shared repo)` block in portable form (ratios, no dollars, no identifiers) whenever its pattern read clears the threshold; the run never sends anything. The operator turns the block into a file under `learnings/proposed/` and a pull request with `scripts/learnings.py propose --pr`. The maintainer reviews it on the pull request and records the decision with `scripts/learnings.py review`: accepted learnings are folded into `rules/RULEBOOK.md` tagged `[community]` with the learning's id and author, and into the next `runs/SKILL-UPDATE-PROMPT-<date>.md`; each operator applies that prompt to their own copy or does not. The same authority rule as §6 applies: tightening can be accepted on the evidence, loosening needs the maintainer's yes. `INSTALL.md` is the install guide; `CONTRIBUTING.md` is the flow and the review checklist; `learnings/INDEX.md` is the generated table of everything proposed so far.

Data, not only learnings (Ken, same day): "amounts, wins and losses are all data that people using this are committing to put back into the community." Every run writes repo records (status rows per run, trade rows per closed trade) as dated CSV files in a `repo-records/` folder next to its state files; the operator publishes them to `data/<handle>/` with `scripts/publish_data.py publish --pr`, and `data/SCOREBOARD.md` aggregates every operator. This reversed the first-pass decision to keep trade figures out of the repo; the account identifier remains the one thing never published. Schema: `data/README.md`. This account's history is in `data/ken-hq/`.

