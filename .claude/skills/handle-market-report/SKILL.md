---
name: handle-market-report
description: Take a market report PDF (top slot games, by any publisher) through the whole handler — read which slot games it ranks, join them to the studio's one ledger of games, fix the report's 20 leading slot games, run the Games AI art analysis on each leader not analysed yet (once per game, ever), update the one-file summary report after each, and when all are done write the full art report of the leading games and the recommendation for Intelligate's next steps in art. Use when Roei attaches or names a market report PDF, asks to continue the market reports work, or asks where a leading game's analysis stands.
---

# Handle a market report

Read `CLAUDE.md` and `README.md` first. Every step leaves its state in the repository, so a later call continues where this one stops.

0. **See where things stand.** `python3 -I tools/ledger.py status` and `python3 -I tools/ledger.py queue`. An earlier call may have left leaders waiting or a run marked `running`: those are finished first (step 5), before a new report's.

1. **Record first.** `records/<YYYY-MM-DD>-<report slug>.md`: what was asked in Roei's words, the file's name, and later what you decided, how it was checked and what stays open.

2. **Take the PDF.** `python3 -I tools/ingest.py <file.pdf> --slug "<publisher period>"`. It says so when the same file was taken before; then go to step 5 with that report's leaders.

3. **Read the rankings** and write `reports/<id>/rankings.json` (schema in `README.md`).
   - Read every page's text; open the page picture (`pages/NNN.png`) wherever a ranking is a chart or a table the text scrambles. `tables/NNN.json` helps with real tables.
   - One entry in `lists` per ranked list the report prints, with its own title, metric, market and page. Keep the report's order and its words; `value` is the figure as printed, or null.
   - Give `type` on an entry that is not a slot (`crash`, `live`, `instant`, `table`): it is recorded and never a leader.
   - A list that ranks something else (providers, operators) is left out and named in `notes`.
   - Never fill a rank the report does not give. A list without ranks has `"rank": null` entries and earns no points.
   - `weight` stays 1 unless the report itself says one list matters more; write the reason in the record.

4. **Unify.** `python3 -I tools/ledger.py unify <id> --dry-run`, then without it.
   - A name it cannot place stops the run. Decide each from the report and the provider's catalogue: `"is": "<game id>"` for the same game under another spelling, `"new": true` for a different game (a sequel, a version, a clone by another provider).
   - A provider it does not know: add the spelling to `registry/providers.json` and run again.
   - Build and publish the summary (step 6) now, so Roei sees the leaders and what is waiting.

5. **Analyse each waiting leader, best position first** (`ledger.py queue`).
   - **Demo link.** The ledger may hold it (`demo`). Otherwise find the provider's own public free-play demo from its product page; for Pragmatic Play it is `https://demogamesfree.pragmaticplay.net/gs2c/openGame.do?gameSymbol=<symbol>&websiteUrl=https%3A%2F%2Fdemogamesfree.pragmaticplay.net&jurisdiction=99&lobby_url=https%3A%2F%2Fwww.pragmaticplay.com%2Fen%2F&lang=en&cur=USD`. Public pages only: no login, no account, no wagering. `ledger.py set <game id> demo=<link>` refuses a link with a session key.
   - `ledger.py start <game id>`.
   - Run the `extract-game-art` skill of `../Games-AI-art` on the link, whole: capture, extraction, screens, sorting, reading, report, its own artifact, its README row, commit and push on that repository's branch. One sub-agent per game works well; at most three games at a time, and give each the skill's path, the link, the game's and provider's names as the ledger has them, and Roei's request to quote. Drive and Miro uploads there are part of that skill; they need the connectors and are skipped, and said to be skipped, when one is missing.
   - `ledger.py complete <game id> --run ../Games-AI-art/runs/<run id> --report <its artifact address> [--drive …] [--miro …] [--commit <sha>]`. It keeps the run's digest in `analyses/<game id>/art/`.
   - A game that cannot be analysed: `ledger.py block <game id> --reason "<what was tried and what failed>"`, and go on. Never fake an analysis and never mark one complete without a published report.
   - After each game: step 6. The summary table changes game by game.

6. **Build, publish, keep.** `python3 -I tools/build_site.py`, look at `site/index.html` once after a change to the builder, then publish it with the Artifact tool at the address in `README.md` (`url` set, so the link stays). Commit and push both repositories.

7. **When the queue is empty** (every leader complete or blocked), write the two documents from the digests in `analyses/` and the full reports:
   - `documents/art-report.md`: the art of the leading games read across them: what they share, where they split, by art component (backgrounds, reel board, symbols, characters, logo, celebrations, effects, interface, typography), with the games named for every statement. The builder puts the measured comparison under it by itself, so do not retype the figures.
   - `documents/next-steps.md`: what Intelligate should do next in art. Each recommendation names the games it rests on, what to do, and how to tell it worked. Mark inference as inference; say what the set of games cannot show (blocked games, providers missing).
   - With a later report, both are revised, not started again: say at the top which reports and how many games they rest on.
   Then step 6 once more.

8. **Report to Roei** in the chat: the summary's link, the report's leaders, which were new and which were known, each new art report's link, what is blocked and why, and the two documents' main points.
