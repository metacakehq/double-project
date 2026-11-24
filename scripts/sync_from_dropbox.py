#!/usr/bin/env python3
"""Sync the Double Project repo from the Dropbox record on this Mac.

Reads (never writes) the Dropbox AI Agents folder and the Claude desktop app's synced skill, then
regenerates the generated files in this repo and reports what is new since the last CHANGELOG entry.

Run from anywhere:  python3 scripts/sync_from_dropbox.py [--dry-run]

Generated:
  skill/double-project-trading/SKILL.md   verbatim live skill, account number redacted
  runs/daily-run.md, runs/weekly-scout.md verbatim newest ROLE prompts, redacted
  history/RUN-LOG.md                      every RUN LOG line across all state files (latest wording wins)
  history/STATUS-LOG.md                   every status file body, in order
  history/OPEN-ITEMS.generated.md         the OPEN WITH KEN section of the latest state file
Printed: latest state file, rule-change lines newer than the last sync, text diffs in skill and prompts.
"""
import glob, os, re, sys, subprocess, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AI = os.path.abspath(os.path.join(REPO, "..", "..", "..", ".."))  # .../AI Agents
STATE_DIR = os.path.join(AI, "Claude", "Storage", "Ken HQ", "Double Project")
LOG_DIR = os.path.join(AI, "Claude", "Log")
ROLE_GLOB_DAILY = os.path.join(AI, "Claude", "ROLE-double-project-daily-run-*.md")
ROLE_GLOB_SCOUT = os.path.join(AI, "Claude", "ROLE-double-project-weekly-scout-*.md")
SKILL_GLOB = os.path.expanduser(
    "~/Library/Application Support/Claude/local-agent-mode-sessions/*/*/rpm/plugin_*/skills/double-project-trading/SKILL.md")
ACCOUNT_RE = re.compile(r"\b\d{9}\b")  # the brokerage account number is a bare 9-digit number; nothing else in these files is
HEADER = "---\nupdated: {d}\nowner: Claude\nbrand: Ken HQ\nscope: on-demand\nstatus: current\nsensitive: {s}\n---\n"
DRY = "--dry-run" in sys.argv
TODAY = datetime.date.today().isoformat()


def redact(t):
    return ACCOUNT_RE.sub("<ACCOUNT>", t)


def read(p):
    return open(p, encoding="utf-8", errors="replace").read()


def write(rel, text):
    p = os.path.join(REPO, rel)
    old = read(p) if os.path.exists(p) else None
    if old == text:
        return False
    if DRY:
        print(f"  would write {rel}")
        return True
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text)
    print(f"  wrote {rel}")
    return True


def newest(paths):
    return sorted(paths)[-1] if paths else None


def strip_header(t):
    m = re.match(r"---\n.*?\n---\n", t, re.S)
    return t[m.end():] if m else t


def last_sync_date():
    p = os.path.join(REPO, "CHANGELOG.md")
    if not os.path.exists(p):
        return "2026-01-01"
    ds = re.findall(r"^## (\d{4}-\d{2}-\d{2})", read(p), re.M)
    return max(ds) if ds else "2026-01-01"


def main():
    print(f"Repo {REPO}\nDropbox AI Agents {AI}")
    if not os.path.isdir(STATE_DIR):
        sys.exit(f"State folder not found: {STATE_DIR}")
    states = sorted(glob.glob(os.path.join(STATE_DIR, "Ken-HQ-double-project-state-*.md")))
    latest = states[-1]
    print(f"Latest state file: {os.path.basename(latest)}  ({len(states)} state files)")
    since = last_sync_date()
    print(f"Last sync per CHANGELOG: {since}")

    # 1. skill
    sk = newest(glob.glob(SKILL_GLOB))
    if sk:
        write("skill/double-project-trading/SKILL.md", redact(read(sk)))
    else:
        print("  skill not found on this Mac; skill/ left as is")

    # 2. prompts
    for g, rel, title in ((ROLE_GLOB_DAILY, "runs/daily-run.md", "Daily Run"),
                          (ROLE_GLOB_SCOUT, "runs/weekly-scout.md", "Weekly Scout")):
        src = newest(glob.glob(g))
        if not src:
            print(f"  no ROLE file for {title}")
            continue
        body = strip_header(read(src))
        text = (HEADER.format(d=TODAY, s="no") + f"# {title} prompt (verbatim copy, account number redacted)\n\n"
                f"Source: Dropbox `Claude/{os.path.basename(src)}`. Copied by scripts/sync_from_dropbox.py.\n\n" + redact(body))
        write(rel, text)

    # 3. run log across all states, latest wording wins per date
    best = {}
    for f in states:
        m = re.search(r"## RUN LOG(.*?)(\n## |\Z)", read(f), re.S)
        if not m:
            continue
        for line in re.findall(r"^- (2026-\d\d-\d\d[^\n]*(?:\n  [^\n]*)*)", m.group(1), re.M):
            best[line[:10]] = line.replace("\n  ", " ")
    runlog = (HEADER.format(d=TODAY, s="yes") + "# Run log (generated)\n\nOne line per run date, taken from the RUN LOG section "
              "of every state file; where several files describe the same date the newest wording wins. Carries account values "
              "and trade figures. Regenerate with scripts/sync_from_dropbox.py; do not edit.\n\n")
    runlog += "\n".join(f"- {redact(best[d])}" for d in sorted(best)) + "\n"
    write("history/RUN-LOG.md", runlog)

    # 4. status log
    status_files = sorted(glob.glob(os.path.join(LOG_DIR, "*-double-project.md"))
                          + glob.glob(os.path.join(LOG_DIR, "*-double-project-weekly-scout.md")))  # run status files only, not session logs
    out = [HEADER.format(d=TODAY, s="no") + "# Status log (generated)\n\nEvery status file the runs wrote to `Claude/Log/`, "
           "oldest first. No figures by design. Regenerate with scripts/sync_from_dropbox.py; do not edit.\n"]
    for f in status_files:
        body = strip_header(read(f)).strip()
        out.append(f"\n## {os.path.basename(f)}\n{redact(body)}\n")
    write("history/STATUS-LOG.md", "".join(out))

    # 5. open items from the latest state
    lt = read(latest)
    m = re.search(r"## OPEN WITH KEN[^\n]*\n(.*?)(\n## |\Z)", lt, re.S)
    if m:
        write("history/OPEN-ITEMS.generated.md",
              HEADER.format(d=TODAY, s="no") + f"# Open with Ken, as the latest state file lists it (generated)\n\n"
              f"Source: `{os.path.basename(latest)}`. Fold changes into history/OPEN-ITEMS.md by hand.\n\n" + redact(m.group(1).strip()) + "\n")

    # 6. report: rule changes newer than the last sync
    m = re.search(r"## RULE CHANGES LOG(.*?)(\n## |\Z)", lt, re.S)
    print("\nRULE CHANGES LOG lines dated after the last sync:")
    n = 0
    if m:
        for line in re.findall(r"^- (2026-\d\d-\d\d[^\n]*(?:\n  [^\n]*)*)", m.group(1), re.M):
            if line[:10] > since:
                n += 1
                print("  -", redact(line.replace("\n  ", " "))[:300])
    print("  (none)" if n == 0 else f"  {n} line(s): fold into rules/RULEBOOK.md and history/DECISIONS.md")

    # 7. git diff of the copied files
    if not DRY and os.path.isdir(os.path.join(REPO, ".git")):
        r = subprocess.run(["git", "-C", REPO, "status", "--short", "--", "skill", "runs", "history"],
                           capture_output=True, text=True)
        print("\ngit status of generated and copied files:\n" + (r.stdout or "  clean\n"))
    print("Next: MAINTENANCE.md steps 3 to 8.")


if __name__ == "__main__":
    main()
