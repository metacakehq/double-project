---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: no
---
# Community data: every operator's runs and trades

Ken, 2026-11-24: "amounts, wins and losses are all data that people using this are committing to put back into the community." Running this system means publishing its results here. One folder per operator, named by handle, two CSV files each, plus a generated scoreboard across everyone. The account identifier is the one thing that never appears; everything else about what the system did is data.

```
data/
  README.md                 this file: the schema and the rules
  SCOREBOARD.md             generated across all operators by scripts/publish_data.py scoreboard
  <handle>/
    status.csv              one row per run (morning, midday, afternoon, close, scout)
    trades.csv              one row per closed trade
    README.md               optional: the operator's start date, start value, goal, notes
```

## status.csv
| Column | Meaning |
|---|---|
| operator | your handle, same as the folder |
| date | session date, YYYY-MM-DD |
| run | morning, midday, afternoon, close, scout, or other |
| v | account value at the run, dollars |
| hwm | high-water mark used for the floor |
| floor | floor F at the run |
| regime | OFFENSE, NORMAL or DEFENSE |
| cash | settled cash, dollars (blank if not recorded) |
| open_positions | tickers held, separated by spaces, with shares if known (`KR:7 EBAY:4`) |
| actions | what the run did: buys, sells, stop moves, in a short phrase; "none" when nothing |
| flags | live diagnostic flags (`A`, `D1`, `D2`) or "none" |
| notes | anything else, one line |

## trades.csv
| Column | Meaning |
|---|---|
| operator | your handle |
| trade_id | `<entry_date>-<ticker>`, with a suffix if the same name was entered twice that day |
| entry_date, exit_date | YYYY-MM-DD |
| ticker | the instrument traded (the fund, for bear funds) |
| vehicle | long, bear_fund, option |
| side | long always (the system never shorts); kept for completeness |
| shares | integer |
| entry_price, exit_price | average fill prices |
| pnl_usd | realized, after the brokerage's own accounting |
| pnl_pct | pnl_usd over the position's entry cost |
| hold_sessions | trading sessions held |
| setup | momentum_scan, pead, bear_pullback, bear_breakdown, rotation, other |
| regime_entry | regime at entry |
| stop_atr | initial stop distance in ATR14 multiples (blank if unknown) |
| risk_pct_v | initial dollar risk as percent of V at entry |
| exit_type | stop_gap, stop_intraday, raised_stop, profit_zone, trend_break, stall, rotation, earnings_trim, other |
| notes | one line |

Blank cells are allowed where the record does not have the value. Never guess a figure; leave it blank. Dates in ISO form, prices and dollars as plain numbers with no currency sign or thousands separator.

## How rows get here
The runs write the rows. Once the skill carries the repo-record step (`runs/SKILL-UPDATE-PROMPT-2026-11-24.md` item 11), the close report writes one status row for each run of the day and one trade row for each trade closed that day to a `repo-records/` folder in the operator's store, as small dated CSV files (`YYYY-MM-DD-status.csv`, `YYYY-MM-DD-trades.csv`, same headers as here). The operator then runs

```bash
python3 scripts/publish_data.py publish --handle <handle> --source <path to repo-records> --pr
```

which merges every record into `data/<handle>/status.csv` and `trades.csv` (deduplicating on date+run and trade_id), regenerates `SCOREBOARD.md`, commits, pushes and opens the pull request. Weekly is enough; the merge is idempotent. Operators whose claude.ai has the GitHub connector can have the close report commit the rows straight to their fork's `data/<handle>/` instead, and skip the script.

## What this is for
The learning loop reads TRADE REVIEW blocks inside one account. This folder is the same evidence across accounts, in a shape a script can read. Every operator's pattern read gets stronger as the folder grows, and `SCOREBOARD.md` shows plainly how the system is doing for everyone, not only for its author.
