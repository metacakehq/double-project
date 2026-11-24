---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Run order, as checklists

The prompts in `runs/` are the authority. This is the same thing laid out as the operator actually does it, with the practices the state files added. Times ET.

## Morning run (task fires about 9:00 CT; first market action at the open)
1. Load the skill. If it does not load by name, search skills for "double project".
2. Load tools in one batch each: Robinhood (portfolio, positions, orders, quotes, realized P&L, indicators, place and cancel order, earnings results) and Dropbox (list_folder, fetch, create_file, create_folder, search).
3. Market holiday check. Closed: say so in one line, stop.
4. Read state: list the state folder (no trailing slash), fetch the latest-dated file. Fallback chain if missing: old single file (stale), then Dropbox search, then the missing-state procedure.
5. Control numbers: V, realized P&L to date, HWM, F. Settled cash from get_accounts. V at or below F: cancel all, HALT, stop.
6. Verify every position has a live GTC stop and check its state (confirmed). Unprotected: place a stop now.
7. Manage positions: ladder levels reached intraday, swing-low raises (respect the minimum trail distance), trend-break lines, earnings proximity, leveraged decay.
8. Evaluate all five flags. Report any live one with evidence and response.
9. Regime: pull SPY and QQQ 50d EMAs with the fixed 2026-04-01 start; direction = today against 3 sessions earlier. ADX14 for both indices.
10. Discovery only if the concentration dial has room and settled cash is over $300. Run the scans (output is long; parse with Python). Qualify each candidate through the six tests and cite the failing number. Bear funds in DEFENSE: check zone (P5), stretch zone (3b), test 4b on the underlying.
11. Enter the best rule-compliant setup or nothing. Limit near ask, GFD. Then fill-then-stop: poll every 1 to 2 minutes for 10 minutes; place the GTC stop the moment shares appear. A blocked order: report to Ken, do not retry.
12. Report to Ken (brief). Then schedule 12:45, 15:30 and 16:05 with send_later using absolute UTC times, verified against a quote timestamp. Confirm a trigger id.

## Midday check (12:45)
Stops live? Trend breaks? Ladder levels reached? One-line status. Schedule 15:30.

## Afternoon review (15:30)
Defense pass: every stop verified and raised where a rule says so; broken trends exited before the close; earnings-proximity trims; leveraged decay check. Schedule 16:05.

## Close report (16:05)
1. Daily P&L. V from regular-session closes. Friday: weekly recap (week P&L, closed trades, pace against the goal).
2. Check order state of every stop (confirmed or queued).
3. Write the new state file: full content, header, "what tomorrow should do" section, run log line, rule changes with reasoning.
4. Write the status file (no figures).
5. Confirm both creates succeeded. If a create fails, retry once with -HHMM, then report.

## Sunday scout (about 11:00 CT)
1. Load skill and tools. No orders of any kind.
2. Read the latest state file.
3. Regime into the week from Friday's closes. Say whether either index is near flipping.
4. PEAD pre-positioning screen: earnings calendar (high market cap, about 14 days), shortlist, verify beat streaks one symbol at a time, apply the entry test and the sizing check at half band in DEFENSE. List qualifiers with day 1 and day 2 dates, and name every reject.
5. New instruments, funds, IPOs, regime shifts worth noting.
6. Position review: entry, Friday close, percent, stop, distance, what triggers Monday, stall watch.
7. Rule gaps: propose only where the week produced evidence. Say plainly when there is nothing.
8. Write state and status files. Schedule nothing.
