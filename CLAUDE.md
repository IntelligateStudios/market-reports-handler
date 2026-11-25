# Market reports handler — working guide for Claude

A market report PDF in; the studio's ledger of leading slot games, one art analysis per leader and one summary report out. The project belongs to Roei Bar Aviv, VP of AI at Intelligate Studios (a slot game studio). `README.md` says what is where and how the tools work; the skill `.claude/skills/handle-market-report/` is the procedure. Read both before working.

## Rules

- **Start from the state.** You are called repeatedly. Run `python3 -I tools/ledger.py status` and `queue` first, and finish what an earlier call left before taking a new report.
- **A game is analysed once.** The ledger (`registry/games.json`) is the memory. A game whose art analysis is `complete` is never run again because another report names it; the report's rank is added to its entry. Only Roei asking for a repeat makes a second run, and that is a new run in Games-AI-art.
- **Never guess a match.** The same title from the same provider is the same game. A sequel or a version ("1000", "Megaways", "Xmas") is another game. When `unify` asks, decide from the report and the provider's catalogue and write the answer in `rankings.json`.
- **As the report states.** A rank or a figure from a report is copied with its page. Nothing is filled in, rounded or carried from one list to another. The leaders' order is the handler's rule (README) and is called that.
- **Measured, read, stated.** Measured figures come from Games-AI-art's pixels; readings mark inference as inference; report figures are "as stated". The two written documents name the games each statement rests on and never invent a figure.
- **Record first.** A dated file in `records/` before a report is handled: what was asked in Roei's words, the file. After: what was decided, how it was checked, what stays open.
- **Complete means published.** `ledger.py complete` only after the run's art is read and its report is published as its own private artifact. A game that cannot be analysed is `block`ed with what was tried.
- **Only `ledger.py` writes the ledger**, and only `build_site.py` writes `site/`. Fix the tool, not the output.
- **Secrets stay out.** No session key in a link (`mgckey=`, `token=`, `session=`), a record or a commit. Public pages only when looking for a demo: no login, no account, no wagering.
- **Reports and competitors' art are for use inside the studio.** A market report may be licensed; an art analysis is a competitor's work kept for study. The summary and the art reports are private artifacts. Posting, sending or sharing any of it, and creating or editing anything in the company's services (Drive, Miro, Confluence, Slack), needs Roei's approval, except the Drive folder and Miro board each art run makes, which he asked for (Games-AI-art `records/2026-11-25-drive-and-miro.md`).
- **After each analysed game**: build the summary, republish it at its address (README), commit and push here and in Games-AI-art. A container can end; nothing unpushed survives it.
- **Tools.** Python tools run with `python3 -I`. A tool opens with a comment saying what it reads and writes; keep it true. `python3 -I -m unittest discover tests` passes before every commit.

## Related repositories

- **Games AI art** (`IntelligateStudios/Games-AI-art`): the analysis each leader gets. Its skill `extract-game-art` is run from there, on that repository's branch.
- **Intelligate HQ** (`IntelligateStudios/intelligate-ai`): Roei's working app. Its competitor GDD runs and its web research of 21 Nov 2026 seeded the ledger. Nothing here writes to it.

Work happens on a branch and is merged with a pull request.
