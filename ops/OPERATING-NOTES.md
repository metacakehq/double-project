---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Operating notes: what the tools actually do

Collected from the OPERATING NOTE sections of the state files, 2026-10-06 to 2026-11-23. Each line is something a run learned by hitting it.

## Robinhood MCP
- place_equity_order takes limit_price (not price) and stop_price; stops are type stop_market, time in force GTC.
- ref_id must be a fresh uuid4 every call. A reused key returns 409 "idempotency_key already in use" and creates no order (2026-10-28).
- Stop swaps are cancel-then-place: the shares are held against the old stop. Place the replacement immediately after its own cancel and confirm it is live. Do not start a swap late in the day while orders are being blocked.
- get_equity_orders takes state_group open or closed only; use updated_at_gte (ISO UTC) for today's activity.
- A stop placed after the close shows state "queued" until the next open. Confirm "confirmed" at the next morning run.
- get_portfolio outside regular hours marks leveraged ETFs at after-hours prints. Compute V from regular-session closes for the record (2026-11-15: $1,134.06 reported against $1,123.24 at the close).
- Daily indicator bars for the current session are not available at 16:05 ET. Intraday estimates: 20d EMA = EMA_prev + (2/21) x (price minus EMA_prev); ATR = (ATR_prev x 13 + today's true range) / 14. The indicator series ends at the prior session's bar during the day; use posted values.
- Pull ADX14, ATR14 and 20d EMA with start_time 2026-07-01T00:00:00Z fixed, interval day, last 4; 50d EMA with start 2026-04-01. Smoothed indicators change with the history window, so the fixed start is what makes values reproducible (verified identical across three runs, 2026-10-06).
- Hourly bars from get_equity_historicals skip the 9:30 to 10:00 slot; use 30minute bars for the true day low. A day-interval request with a start inside today's session returns "end must be after start".
- The momentum scan returns 150 to 175 rows; output lands inline or in a file and is very long. Parse with Python, do not read it raw.
- get_earnings_calendar with high_market_cap over 14 days returns 200 to 1,800 rows with no price or cap. Save to a file and intersect with the momentum scan, or shortlist known large caps, then quote and check beat streaks. get_earnings_results takes a single symbol. "Rising estimate trends" cannot be verified with these tools; only the beat streak and price structure can.
- The Agentic account is identified by number in the task prompts (redacted here).

## Dropbox MCP
- Create-only. No update, no append. Every write is a new file. This is why the state is one dated file per run.
- The team root is not writable. Use the ns: paths in the prompt. A path at the team root fails with TEAM_ROOT_NOT_WRITABLE.
- list_folder: path WITHOUT a trailing slash; a trailing slash returns INVALID_PATH.
- If a fetch fails, search for "double-project-state" before concluding the state is missing.
- 2026-09-28: the old delete-then-recreate procedure deleted the state file and the recreate was refused. Nothing is deleted any more.

## Scheduling (send_later and the task)
- The weekday task fires about 14:00Z, pre-open. The morning run itself happens at the open; if an open-print check is wanted, add a send_later at about 15:00Z.
- Pass absolute UTC times in `at`. Do not compute delay minutes from the container clock, which has drifted by hours. Cross-check against a Robinhood quote's venue_last_trade_time.
- Each wake-up schedules only the next one. Always confirm a trigger id. The chain has fired on time every day since 2026-11-04.
- Never schedule tomorrow's morning run from a wake-up and never from the Sunday scout: two sessions would trade the same account.
- EST slots from 2026-11-02: morning 15:00Z, midday 17:45Z, afternoon 20:30Z, close 21:05Z. Half days compress: 2026-11-27 midday about 16:15Z, afternoon 17:30Z, close 18:05Z.
- July 2026: fresh scheduled sessions could not attach the Robinhood connector, so runs lived in one chat via send_later. Since October the runs are scheduled tasks and Robinhood attaches; the skill's architecture note predates this.

## The permission check
- The Claude session's "Real-World Transactions" classifier blocked order placement on 2026-10-28 and 11/09, 11/10, 11/11 and 11/12. Robinhood itself requested nothing. Ken's "try again" cleared it the same morning on 11/09 and 11/11; on 10/28, 11/10 and 11/12 the entries were missed. Practice: do not retry or work around a block; report it. A block that could leave a fill unprotected is a Flag D Tier 2 condition.
- Ken, 2026-11-24: blocks should only happen on a real threat. New rule (in the skill once the update prompt is saved): verify no order was created, retry once with a fresh ref_id, then report the exact order; Tier 2 only when a fill could be left unprotected. The structural fix is on claude.ai: "Always allow" the Robinhood place and cancel tools for the scheduled task and at the first run of any new session.

## Ken-reply checks
- The runs look for Ken's answer in the session and, when needed, with a Gmail search (newer_than:1d, keywords "Double Project", "Flag D", the ticker). Gmail hit a quota error once at a close (2026-10-21).

## Reporting
- Status files carry no positions, tickers, balances or dollar figures, so Ethan's scan can carry them into Notion.
- The state file stays readable: about 16 to 19 KB, full content, "what tomorrow should do" near the end.
