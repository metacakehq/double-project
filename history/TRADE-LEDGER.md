---
updated: 2026-11-24
owner: Claude
brand: Ken HQ
scope: on-demand
status: current
sensitive: yes
---
# Trade ledger, 2026-07-24 to 2026-11-23

Every closed trade since the campaign started. Reconstructed from the state files' run logs and records, the skill's amendment log, and the September handoff documents. Two August wins (08-03 and 08-06) are known only by date and P&L; the September handoff did not name them. Figures are realized P&L in dollars. These are brokerage figures: see the sensitivity note in `README.md`.

| # | Entry | Exit | Ticker | Shares | Entry px | Exit px | P&L | Exit type | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Jul/Aug | 2026-08-03 | (not named) | | | | +10.35 | | first closed win |
| 2 | Jul/Aug | 2026-08-06 | (not named) | | | | +26.30 | | |
| 3 | by 2026-09-07 | 2026-09-08 | ELF | 5 | 96.00 | about 103.3 | +36.42 | stop (raised) | largest win of the long book |
| 4 | 2026-07-27 | 2026-09-11 | BAC | 8 | 62.45 | 62.6801 | +1.84 | stall exit | the trade that created the stall-exit rule (skill log says +1.82) |
| 5 | about 2026-09-20 | 2026-09-21 | CVX | | | | -25.39 | stop | energy; rolling-over crude |
| 6 | 2026-09-22 | 2026-09-23 | DINO | | | | -17.84 | stop | bought the day after an outside reversal; source of the reversal-bar deferral |
| 7 | 2026-09-09 | 2026-09-28 | TEAM | 2 | | | -1.56 | stop (gap) | stopped 0.43% below entry on a 6.4% gap-down; the stop worked |
| 8 | 2026-09-28 | 2026-10-14 | FTNT | 2 | 176.2743 | 186.15 | +19.75 | stop at open (gap) | stop had been raised to 189.60 on the ladder |
| 9 | 2026-09-29 | 2026-10-15 | PLTR | 2 | 186.1099 | 196.44 | +20.66 | stop at open (gap) | stop 197.90 |
| 10 | 2026-10-19 | 2026-10-27 | DOCU | 6 | 74.92 | about 82.95 | +47.67 | stop (raised) | best long; 16-minute unprotected window at entry raised Flag D |
| 11 | 2026-10-29 | 2026-11-06 | KR | 7 | 65.43 | 66.80 | +9.59 | stop at open (gap) | P3 exclusion applied |
| 12 | 2026-10-30 | 2026-11-09 | EBAY | 4 | 121.48 | 120.6514 | -3.31 | stop | entry-adjacent stop (0.21x ATR) shaken out intraday |
| 13 | 2026-11-09 | 2026-11-18 | KR | 4 | 67.62 | 69.15 | +6.12 | stop (raised) | re-entry after the 11/06 stop-out |
| 14 | 2026-11-11 | 2026-11-17 | EBAY | 2 | 122.7341 | 117.844 | -9.78 | stop | second ecommerce loss; Flag A live through 12/02 |
| 15 | 2026-11-13 | 2026-11-16 | SOXS | 5 | 53.39 | 58.3301 | +24.70 | bear profit zone | breakdown-style entry; first bear-fund trade |
| 16 | 2026-11-16 | 2026-11-18 | WEC | 2 | 117.44 | 115.00 | -4.88 | stop at open (gap) | tight initial stop; P3 exclusion |
| 17 | 2026-11-19 | 2026-11-19 | SOXS | 5 | 50.93 | 60.955 | +50.13 | bear profit zone | pullback-style entry; same-day exit; new realized peak |

## Totals
- 17 closed trades: 11 wins, 6 losses. Win rate 65%.
- Gross wins +$253.53, gross losses -$62.76, net realized **+$190.77** (the 2026-11-23 state file's figure).
- Average win $23.05; average loss $10.46; payoff ratio 2.2.
- Largest win +$50.13 (SOXS, one session). Largest loss -$25.39 (CVX).
- Every loss died within the 0 to minus 6% band; no loss came from a winner given back.
- The +20% scale-out has never fired on a long. Longs have exited by stop (gaps or raised stops) every time.
- Bear funds: 2 trades, 2 wins, +$74.83, both in November's DEFENSE tape. That is 39% of all realized P&L from the last two weeks.
- Options: never used.

## Account value checkpoints (regular-session closes)
| Date | V | Note |
|---|---|---|
| 2026-07-24 | 1,000.00 | start |
| 2026-09-07 | 1,105.04 | probe; BAC and ELF held |
| 2026-09-28 | 1,032.66 | after the CVX, DINO, TEAM losses |
| 2026-10-06 | 1,074.63 | FTNT, PLTR |
| 2026-10-16 | 1,073.07 | all cash, Flag D |
| 2026-10-23 | 1,135.17 | DOCU |
| 2026-11-04 | 1,158.64 | peak close to date; KR, EBAY |
| 2026-11-13 | 1,123.24 | |
| 2026-11-19 | about 1,195 | after the second SOXS trade |
| 2026-11-23 | 1,194.87 | all cash; HWM 1,190.77; floor 690.77 |

## Blocked or missed entries (for the record, not P&L)
- 2026-10-28 KR 7 sh: permission block. Entered the next day instead.
- 2026-11-10 EBAY 2 sh re-entry: permission block, no reply, missed.
- 2026-11-12 SOXS 5 sh at 47.90: permission block, no reply, missed (would have been about minus 4.5% at that close).
- 2026-11-20 SOXS and SQQQ: failed the P5 cap all day while they rose 32% and 16.5%. Led to the stretch trial.
- 2026-11-23 SOXS and SQQQ: deferred by the new test 4b.
