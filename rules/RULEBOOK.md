---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# The Double Project rulebook, consolidated

This is every rule in force on 2026-11-24, in one document. Each rule carries a tag:
- **[skill]** the text is in the live skill `double-project-trading` (see `skill/` for the verbatim copy).
- **[state]** the rule is in force but only the state file carries it; the skill has not been updated. These are the ones a skill save should pick up.
- **[prompt]** the rule lives in the scheduled-task prompt, which overrides the skill on that point.
- **[practice]** an operating practice the runs adopted and recorded; Ken may reverse it.
- **[trial]** a Ken-approved trial with a review date.
Dates are when the rule took effect. Ken's words are quoted where the record has them.

## 0. The campaign
Robinhood "Agentic" cash account (number redacted; Level 2 options, T+1 settlement). Started 2026-07-24 with $1,000. Goal $2,000. Ken authorized execution without per-trade approval, strictly within these rules. [skill]

## 1. Control numbers, computed first on every run [skill]
- V = account value from get_portfolio. Outside regular hours, compute V from regular-session closes, not after-hours marks. [practice, 2026-11-15]
- HWM = $1,000 + peak-to-date cumulative realized P&L since 2026-07-24 (minimum 0).
- Floor F = max($500, HWM minus $500). Ratchets up only, on realized gains.
- If V is at or below F: cancel all open orders, take no trades, report HALT, await Ken.
- Settled cash is read from get_accounts (unsettled_funds), not the cash figure. [prompt]

## 2. The four survivability rules (tightening is free; loosening needs Ken first) [skill]
1. Floor F, above.
2. Max loss per trade 6% of V at entry (shares times stop distance).
3. Total open risk across all positions at most 12% of V.
4. Every stock or ETF position has a live GTC stop-market sell at all times. Fill-then-stop is atomic.
   - Fill-then-stop procedure [practice, 2026-10-19]: after any buy, check order status and get_equity_positions every 1 to 2 minutes for 10 or more minutes; place the GTC stop the moment shares appear. If unfilled after 10 minutes, send_later checks no more than 5 minutes apart. Never cancel a working buy just for convenience; never leave a fill unprotected.
   - The close report checks the order STATE of every stop (confirmed or queued), not just its presence. [practice, 2026-11-02]
   - A stop placed after the close reads "queued" until the next open; the next morning run confirms it reads "confirmed" and re-places it if rejected. [practice, 2026-10-25]

## 3. Other hard rules [skill]
1. Concentration dial: each core position 30 to 50% of V at entry while V < $2,000 (band widened from 40 to 50% on 2026-08-30 because share granularity, not setup quality, was rejecting candidates); 25 to 50% once V is at or above $2,000. Up to 3 core positions below $2,000; hard ops cap of 4 open positions. Earnings-trim stubs under 20% of V do not count.
2. Deployment dial: governed by regime and the 12% budget, never a fixed cap. Full deployment always available, never mandatory. Cash is a position.
3. Settled funds only.
4. Never average down. No shorting; bear or inverse ETFs are the only bearish vehicle. No VIX or volatility products.
5. Earnings blackout: no new entry within 5 trading days before a name reports; a holding reporting within 2 trading days sells at least half (all if at a loss). Single-stock leveraged ETFs inherit their underlying's earnings. Index and commodity ETFs exempt.
6. Options: long calls (long puts only as an exit hedge). ITM, 30 to 60 DTE, close at 21 DTE or at minus 50%. Total premium at risk at most 15% of V. Prefer post-earnings entries after IV crush. No options on leveraged ETFs. No call buying in DEFENSE. Never used to date; gated on the open floor question. [skill; practice: do not place one until the floor question is settled, 2026-10-06]
7. Half size [state, working definition since 2026-11-01, open item 7]: 15 to 25% of V. Binding whenever DEFENSE makes long entries half size and for the first bear-fund entry.

## 4. Regime filter, daily [skill]
SPY and QQQ against their 50-day EMAs.
- Both above rising 50d = OFFENSE.
- Mixed = NORMAL.
- Both below falling 50d = DEFENSE.
- "Rising" or "falling" for the 50d EMA = today's posted value against the value 3 sessions earlier (P4). [state, 2026-10-18, Ken approved]
- DEFENSE consequences: bear funds become the primary vehicle and may be sized as core positions, only on confirmed downtrends (underlying below a falling 20d EMA with ADX14 > 25); first bear entry half size, may pyramid to full core on confirmation; bear profit-taking at +10 to 15%; long entries disfavored and half size; no call buying; if nothing qualifies either way, cash. DEFENSE does not force exits of existing longs; their stops manage them.

## 5. Discovery (only when the concentration dial has room and settled cash is over $300) [skill]
- Stock scan "Momentum swing candidates" (ADX14 > 25, RSI14 55 to 75, average volume > 2M, cap > $2B, price 10 to 250). Scan IDs are in the skill.
- Leveraged ETF scan (RSI 60 to 85, ADX > 30, volume > 1M). Identify leveraged funds by name, map each to its underlying, qualify on the underlying. Max 1 leveraged position. Exit if the underlying flattens or after about 2 weeks of no progress (decay guard). Recent-IPO underlyings: borderline is NO, half size only.
- Sizing feasibility check [skill, 2026-08-30]: before rejecting a setup, compute which whole-share counts land inside the band; report the workable price ranges so granularity rejections are visible, never silent.
- PEAD module: names that beat and gapped up, gap held through day 1, are candidates from day 2. Never enter before a report. PEAD candidates pass the same universal entry test; there is no PEAD bypass. [skill, 2026-09-28]
- Sunday PEAD pre-positioning screen: reporters in the next about 14 days with 4 or more consecutive EPS beats, rising estimates, sector momentum, filtered by the sizing check; carried as post-print candidates only. Name the rejects so the next run does not re-screen them. [skill, 2026-08-06; prompt]
- Category rejects (standing): MSTR, COIN, BMNR, ASST, GME and spot crypto ETFs; names with pinned prices (TECH) or deal-pinned patterns (RXO, 2026-10-30); data-integrity names (TEVA, DV, BOXX). [state]

## 6. The universal entry test (every entry, every vehicle; cite the number that failed) [skill unless tagged]
1. ADX14 > 25. While Flag C is live, also rising for 3 consecutive sessions.
2. Price above a RISING 20d EMA (up over the prior 3 sessions). Bear funds: underlying below a FALLING 20d EMA.
3. Extension cap: price no more than 1.5 x ATR14 above its 20d EMA. Over the cap is a WATCH with a recorded re-qualifying price, not a reject.
   - P5, bear funds [state, 2026-10-18, Ken approved]: the underlying must be no more than 1.5 x ATR14 BELOW its falling 20d EMA. Over is a WATCH.
   - 3b, bear-fund STRETCH entry [trial, Ken approved 2026-11-22 11:24 CT]: underlying between 1.5x and 2.0x ATR14 below its falling 20d EMA is enterable only if the underlying's ADX14 is > 25 and rising 3 consecutive sessions. Size 7.5 to 12.5% of V (half of a normal first bear entry); if no integer share count fits, no entry. Initial stop at least 1.0x the fund's ATR14 beyond a structure level. Exits unchanged. No pyramiding while the underlying is beyond 1.5x. Max one stretch position. Tag "STRETCH" in the state file. Beyond 2.0x stays blocked. Review after 3 stretch trades or on 2026-12-20, whichever first: keep, widen or drop.
4. Reversal-bar deferral: no entry within 1 session of a bar whose range exceeds 2 x ATR14 and closes in the bottom third of that range. Defers one session; does not reject.
   - 4b, bear funds [state, tightening made by Claude 2026-11-23, stands unless Ken reverses]: no bear-fund entry within 1 session of an UNDERLYING up bar whose true range (including the gap) exceeds 2 x ATR14, unless that bar closes in the bottom third of its true range. If such a bar is still forming, enter late in the session only if it is closing in the bottom third.
5. Earnings blackout clear, and no live diagnostic flag blocks it.
6. An integer share count lands inside the concentration band, funded from SETTLED cash.
Indicator procedure [practice, 2026-10-04]: pull ADX14, ATR14 and the 20d EMA with a fixed start of 2026-07-01T00:00:00Z, interval day, last 4; pull the 50d EMA with start 2026-04-01. Fixed starts make smoothed indicators reproducible between runs.

## 7. Entries and initial stops
- Entries: pullback toward support or clean breakout in a confirmed trend; limit orders near the ask; GFD. [skill]
- Initial stop minimum distance [practice since 2026-11-10, proposed to Ken 2026-11-22 as item 9]: the initial stop sits at least 1.0 x ATR14 below entry and beyond a structure level; reduce the share count if needed so dollar risk stays within 6% of V. Evidence: EBAY 11/09 (stop 0.21x ATR under entry, shaken out on an intraday dip), KR 11/06, WEC 11/18.
- Blocked orders [practice, 2026-11-12]: if the Claude session's permission check blocks an order, do not retry or work around it; report to Ken. While orders are being blocked, do stop swaps in the morning run, never late in the day for a small gain.

## 8. Trade management [skill unless tagged]
- Core longs: sell half at about +20%, then trail the remainder below successive swing lows until trend break. Stubs, positions under 20% of V, and a 1-share core may take a full exit in the +15 to 25% zone. Bear funds: full exit at +10 to 15%; the zone counts as reached when touched intraday. [practice, 2026-11-16]
- Trend break exit: a close below the trend-break line (the rising 20d EMA), RSI collapse, or reversal.
- Stop ladder: at +5% versus entry raise the stop to entry-adjacent (just below entry, under the nearest intraday support); the level counts when reached intraday. [practice, 2026-11-05] At +10% raise to breakeven; pyramiding up to half the original size is permitted (combined at most 60% of V, risk within 6% and 12%). Then trail below swing lows.
- Swing low [state, in use since 2026-10-12, written into the 10/18 skill proposal]: a daily low with a higher low on the session before AND after, confirmed at that later close. The stop goes just under it and only ever moves up. Raises may be made at the 15:30 review once the pattern is clear. [practice, 2026-11-11]
- Minimum trail distance (P3 part 2) [state, 2026-10-18, Ken approved]: a raise may not put the stop closer than 0.5 x ATR14 below the prior close. Never lowers a stop. Does not apply to initial stops.
- Rotation rule [skill, 2026-08-10]: a new candidate may displace an existing core position only if all hold: fresh catalyst-grade signal (day 1 or 2 post-earnings beat with gap held, or a new qualifying breakout with rising ADX); the displaced position is objectively the weakest (lowest gain and below +5%, or about 2 weeks no progress); a working position (up 10%+ or making new highs above a rising 20d EMA) is never displaced; max one rotation per week; the swap is a normal exit then a normal entry under every rule. T+1: sell day 0, buy day 1.
- Stall exit [skill, 2026-09-11]: exit a core position, replacement or not, when all hold: held 15+ trading days; below +5% versus entry; ADX14 under 20; 20d EMA flat (under 0.5% movement over 5 sessions). Cancel the GTC stop first, then sell. A stall-exited name returns to normal discovery at once. A pending catalyst does not defer a stall exit.
- Stop swaps are cancel-then-place with a fresh uuid4 ref_id; confirm the replacement is live immediately. [practice, 2026-10-13]
- Cash-secured puts (narrow): only when capital would sit idle a week or more waiting for a pullback; strike at the desired entry, 2 to 3 weeks out. [skill]

## 9. Diagnostic review flags (replaced the consecutive-loss pause on 2026-09-28) [skill]
Governing principle: a flag must name a specific failing mechanism and cite evidence. Never raise a flag on trade count, win rate or a losing streak alone. Evaluate all five every morning run; report every live flag with evidence and response.
- **A, same-theme repeat failure.** Two or more losing exits in the last 10 trading days from the same sector or theme. Response: that theme blocked for new entries for 10 trading days from the latest exit. Everything else continues at full size.
- **B, entry-timing failure.** Two or more of the last three closed trades exited within 3 trading days of entry and never traded 3% above entry. Response: next entry half size and a pullback-toward-support entry. Clears on the first entry that trades +3%.
- **C, regime-filter mismatch.** A losing exit while the regime reads OFFENSE and both index ADX14 readings are under 20. Response: every new entry needs ADX14 > 25 AND rising 3 consecutive sessions. Clears when either index ADX14 closes above 20.
- **D, stop-system failure, tiered** [skill, amended 2026-11-19 per Ken]. Tier 1 MINOR, never halts, log and fix in the same run: stop fill up to 3% worse than the stop on a non-gap fill (1 to 3% recorded as a WATCH); any gap-open fill below the stop (P3 exclusion, Ken approved 2026-10-18); realized loss above risk by no more than that slippage; a missing stop of known cause replaced in the same run. Tier 2 SERIOUS, halts NEW entries only: non-gap fill more than 3% worse; realized loss over 1.5x risk not explained by a gap; missing stop of unknown cause, or a second one within 10 trading days, or one that cannot be re-protected in the same run; orders cannot be placed or confirmed (permission block, API failure); two WATCH events within 10 trading days. Tier 2 clears itself when the cause is identified and fixed and the next 2 sessions show every stop live with no new event; an order-placement failure clears when a test confirms orders place again; unknown cause goes to Ken. (This superseded the 2026-10-28 auto-clear rule, which required 3 clean days with positions open.)
- **E, drawdown by magnitude.** Cumulative realized P&L more than $75 below its high-water mark. Response: written diagnosis to Ken; new entries at half size until a winning closed trade.

## 10. What halts trading, complete list [skill, 2026-11-19, Ken]
1. The floor (V at or below F): cancel all, no trades, HALT, await Ken.
2. Flag D Tier 2: new entries only; existing positions keep full management and protection.
3. US market closed.
Nothing else halts. Flags A, B, C and E narrow theme, size or the entry bar. Items open with Ken never block trading. Ken: "the only thing that should halt trading should be something serious."

## 11. How rules change [skill, 2026-09-28]
Make the call, record the reasoning in the state file, report it to Ken in that run. A change stands until Ken reverses it. Tightening is free. Loosening any of the four survivability rules needs Ken first. The Sunday scout proposes only; it changes no rule. Never sit on a rule question waiting for a ruling.

## 12. Scheduling and files [prompt overrides skill]
- The weekday Daily Run task (claude.ai, 9:00am CT) runs the morning run and chains 12:45, 15:30 and 16:05 ET with send_later into the same session, each wake-up scheduling the next. Pass absolute UTC times; cross-check against a Robinhood quote timestamp. Never schedule tomorrow's morning run; the recurring task does that. The Sunday scout schedules nothing.
- Half days (for example the Friday after Thanksgiving, 1:00 pm ET close) compress the chain. [state]
- State: one new dated file per run in `Claude/Storage/Ken HQ/Double Project/`, full content, six-line header, sensitive: yes. Never delete, overwrite, rename or move. Latest date is current; a later -HHMM wins on the same date.
- Status: one file per run in `Claude/Log/`, under 15 lines, no positions, tickers held, balances or dollar figures.
- Missing state: read the live account, protect every position, no new entries, report, rebuild from the account, never from memory.

## 12b. Learning loop [proposed 2026-11-24, Ken asked; adopted into the skill via the update prompt]
Every closed trade gets a fixed TRADE REVIEW record at the close report (setup, regime, stop distance, exit type, max favorable and adverse excursion, lesson). The Sunday scout reads all reviews and reports counts by exit type, setup, stop distance, kept excursion and regime, keeps a scoreboard, and turns a pattern into a proposal only with 4 or more trades, a named mechanism and a specific change. Full text in `rules/LEARNING-LOOP.md`.

Shared learnings [Ken, 2026-11-24]: every operator's scout prints its proposals in a portable block; operators push them to `learnings/proposed/` by pull request; accepted ones enter this rulebook with a `[community]` tag and the learning id and author, and reach every operator as the next skill-update prompt. Three learnings from this account seed the folder: `2026-11-10-ken-hq-initial-stop-minimum` (accepted, §8 initial stop), `2026-11-23-ken-hq-bear-reversal-bar-deferral` (accepted, test 4b), `2026-11-22-ken-hq-stretch-entry-trial` (trial, test 3b). Flow and review checklist: `CONTRIBUTING.md`.

## 13. Reporting [skill, prompt]
Brief. One line per position (entry, current, stop). V against $1,000 and against F. What was done and why. Quiet days two or three lines. Trades, rule triggers and live flags always reported. No em dashes, no preamble, no escalating language. State negatives plainly and name the positives. Never imply the target is near; state the gap.

## 14. The honest standing note on the objective [skill, 2026-09-28, refreshed in every state file]
$2,000 from $1,000. With one or two core positions at about 35% of V, a +20% move adds about 7% to V and the scale-out books half of that, so doubling needs on the order of 9 to 14 net winning trades at current sizes: months to years, not weeks. Levers in descending order of evidence: trend quality at entry (Flag C and the entry test); the never-used long-call allowance; letting winners run past +20% (the scale-out has never fired, so there is no evidence it is the constraint).
