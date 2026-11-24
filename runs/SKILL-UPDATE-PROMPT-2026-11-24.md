---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Prompt for the active session: save the missing rules into the skill

Paste everything below the line into the active Double Project session (the Daily Run session is fine, after the close report, or the Sunday scout). It asks the session to produce the full updated skill text and show the save card. Ken taps save. Then run `scripts/sync_from_dropbox.py` here and the `[state]` tags in `rules/RULEBOOK.md` become `[skill]`.

---

Skill maintenance, no trading in this step. Invoke the double-project-trading skill, then read the latest state file in ns:1074522407//AI Agents/Claude/Storage/Ken HQ/Double Project (list without a trailing slash, newest date wins). Produce the complete updated SKILL.md text and show me the skill save card. Keep every existing rule and the amendment log intact; add the following, each as a dated amendment-log line as well as rule text in the right section. Where the state file's wording and mine differ, use the state file's. Keep the account number exactly as the skill has it.

1. REGIME. P4 (Ken approved 2026-10-18): the 50d EMA is "rising" or "falling" when today's posted value is above or below the value 3 sessions earlier, the same test the 20d EMA uses.

2. UNIVERSAL ENTRY TEST, test 3. Add P5 (Ken approved 2026-10-18): for bear funds the underlying must be no more than 1.5 x ATR14 BELOW its falling 20d EMA; over is a WATCH with a recorded re-qualifying price. Add 3b, the STRETCH ENTRY TRIAL (Ken approved 2026-11-22 11:24 CT): underlying between 1.5x and 2.0x ATR14 below its falling 20d EMA is enterable only if the underlying's ADX14 is above 25 and rising 3 consecutive sessions; size 7.5 to 12.5% of V; if no integer share count fits, no entry; initial stop at least 1.0x the fund's ATR14 beyond a structure level; exits unchanged; no pyramiding while the underlying is beyond 1.5x; max one stretch position; tag STRETCH in the state file; beyond 2.0x stays blocked; review after 3 stretch trades or on 2026-12-20, whichever first.

3. UNIVERSAL ENTRY TEST, test 4. Add 4b (tightening, 2026-11-23, stands unless Ken reverses): no bear-fund entry within 1 session of an UNDERLYING up bar whose true range (including the gap from the prior close) exceeds 2 x ATR14, unless that bar closes in the bottom third of its true range; if such a bar is still forming, the entry may be taken late in the session only if it is closing in the bottom third.

4. TRADE MANAGEMENT. Swing low (in use since 2026-10-12): a daily low with a higher low on the session before AND after, confirmed at that later close; the stop goes just under it and only ever moves up. Minimum trail distance, P3 part 2 (Ken approved 2026-10-18): a raise may not put the stop closer than 0.5 x ATR14 below the prior close; never lowers a stop; not for initial stops. Ladder and profit-zone levels count when reached intraday (practice 2026-11-05 and 2026-11-16). Initial stop minimum (practice since 2026-11-10, item 9): the initial stop sits at least 1.0 x ATR14 below entry and beyond a structure level; reduce the share count if needed so dollar risk stays within 6% of V.

5. HALF SIZE (working definition since 2026-11-01, item 7): 15 to 25% of V, used for first bear entries and for long entries in DEFENSE, until Ken defines it otherwise.

6. FLAG D. Confirm the tiered text of 2026-11-19 is present. Add that a gap-open fill below the stop is the P3 exclusion (Ken, 2026-10-18) and that the 2026-10-28 auto-clear rule is superseded by the Tier 2 self-clearing text.

7. SCHEDULING ARCHITECTURE. Replace the paragraph that forbids scheduled tasks. The runs are two claude.ai scheduled tasks since 2026-10-06: the weekday Daily Run (about 9:00am Central) which chains 12:45, 15:30 and 16:05 ET into the same session with send_later using absolute UTC times, and the Sunday Weekly Scout which schedules nothing. Never schedule tomorrow's morning run from a wake-up. Note that the July 2026 Robinhood-attach failure no longer applies. Keep the bootstrap guidance about tapping "Always allow" on the Robinhood and scheduling tools.

8. ORDER PLACEMENT BLOCKS (Ken, 2026-11-24: the system runs autonomously; a permission block on a rule-compliant order is not a threat). Add an operating rule: if the session's permission check blocks a rule-compliant order, first verify with get_equity_orders that no order was created, then retry once with a fresh ref_id; if still blocked, record it, report it to Ken in that run's report with the exact order it wanted to place, and treat it as Flag D Tier 2 only if a fill could be left unprotected (a stop after a buy, or the place step of a stop swap). Never start a stop swap while blocks are occurring that day. Remind Ken in the report that the fix is on his side: in the scheduled task's settings and the first run of a new session, "Always allow" the Robinhood place_equity_order and cancel_equity_order tools.

9. LEARNING LOOP (Ken, 2026-11-24). Add a new section with this text, then a matching step in the close report and a new section 6 in the Sunday scout:
   - Every closed trade gets a TRADE REVIEW block in the state file at the close report with these fields: result in dollars and percent, hold in sessions, vehicle, setup type (momentum scan, PEAD day 1-2, bear pullback, bear breakdown, rotation, other), regime and flags at entry, ADX and EMA distance at entry, initial stop distance in ATR and risk in dollars and percent of V, exit type (stop gap, stop intraday, raised stop, profit zone, trend break, stall, rotation, earnings trim), maximum favorable and adverse excursion from 30minute bars, the rule that decided the exit, what worked, what did not, one candidate lesson or "none", tags.
   - The Sunday scout reads all TRADE REVIEW blocks and reports counts: shake-out rate (stop-outs recovered above entry within 5 sessions), win rate and average result by setup type, average result by initial stop distance (under 0.5x ATR, 0.5 to 1.0x, over 1.0x), share of the average winner's peak excursion that was kept, longs versus bear funds by regime, and any candidate lesson tag seen 3 or more times. It keeps a scoreboard table: trades, wins, losses, win rate, average win and loss, payoff ratio, shake-out rate, kept-excursion ratio, trades per week, realized pace per week against the pace the goal needs.
   - A pattern becomes a proposal only with 4 or more trades (3 for bear funds while the sample is small), a named mechanism, and a specific change with an expected cost and a review field. Tightening proposals may be adopted as practice by the daily run; loosening goes to Ken. One change at a time per area, each with a review date, like the stretch trial.
   - The first scout after this is saved backfills TRADE REVIEW blocks for every closed trade since 2026-07-24 from the state files' run logs, with excursions from historicals.

10. In the amendment log, add one line dated 2026-11-24 listing items 1 to 9 as "skill brought level with the state file and the learning loop added, per Ken." Then show the save card. After I save, say in one line what the next run will do differently.
