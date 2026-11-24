# Double Project repo: Claude Code pointer

Before any work here, read Dropbox `AI Agents/README.md` and check its version line, then `README.md` in this folder, then `MAINTENANCE.md`.

This folder is its own git repository (nested inside the Ken HQ media-system checkout, which ignores it). It codifies the Double Project trading system. It never trades, never touches the live account, and never edits the Dropbox state or status files.

To update it: follow `MAINTENANCE.md`. Short version: run `python3 scripts/sync_from_dropbox.py`, read what it reports as new, fold rule changes into `rules/RULEBOOK.md` and `history/DECISIONS.md`, update `history/OPEN-ITEMS.md` and the status block in `README.md`, add a `CHANGELOG.md` entry, commit with explicit paths.
