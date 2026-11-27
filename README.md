# Market reports handler

A market report PDF in; out, the studio's one ledger of leading slot games, an art analysis of every leader (run once per game, ever), and one summary report that holds it all.

Roei asked for it on 25 Nov 2026 (`records/2026-11-25-origin.md`). It is called again and again, each time with another report, so every step keeps its state here.

**The summary report:** https://claude.ai/artifact/LmgXcz5py18WGQnzQZipts (private; one HTML file with every page inside, built into `site/index.html`).

## What happens to a report

1. **Taken.** `tools/ingest.py` copies the PDF in with each page's text, picture and tables. The same file is never taken twice.
2. **Read.** Its ranked lists are written, as printed, to `reports/<id>/rankings.json`.
3. **Unified.** `tools/ledger.py unify` matches every ranked name to `registry/games.json`, adds the new games, and fixes the report's 20 leading slot games.
4. **Analysed.** Each leader with no art analysis gets a run of Games AI art (`IntelligateStudios/Games-AI-art`, skill `extract-game-art`). `ledger.py complete` records where it is and keeps its digest in `analyses/`.
5. **Summarised.** `tools/build_site.py` rebuilds the summary after each game; it is republished at the address above.
6. **Concluded.** When every leader is analysed or blocked: `documents/art-report.md` (the art of the leading games) and `documents/next-steps.md` (Intelligate's next steps in art).

The skill `.claude/skills/handle-market-report/SKILL.md` is the procedure. `documents/method.md` says the same for a reader of the summary, and is its Method page.

## What is where

| Path | What it is |
| --- | --- |
| `registry/games.json` | The ledger: one entry per game. Its names and spellings, provider, type, demo link, every report and list that ranks it, what the studio already had on it, and its art analysis (`none`, `running`, `complete` with the run, the published report, Drive and Miro, or `blocked` with the reason). Written only by `ledger.py`. |
| `registry/providers.json` | Each provider's key and the ways reports write its name. |
| `reports/<YYYY-MM-DD>-<slug>/` | One report: `source.pdf`, `pages/NNN.txt` and `.png`, `tables/`, `report.json` (header and, once unified, its leaders), `rankings.json` (its lists as printed), `unify.json` (what each name was taken as). |
| `analyses/<game id>/art/` | The digest of a finished art run: `digest.json` (counts, measured palette and tone, the art direction as read, takeaways), `Art-report.md` (the full report as text) and up to four small game screens. The run itself, with all its art, stays in Games-AI-art. |
| `documents/` | `method.md`, and when written `art-report.md` and `next-steps.md`. |
| `site/index.html` | The summary report, generated. Pages: Summary, Reports (one per report), Games (one per game), Art of the leaders, Next steps in art, Method. |
| `records/` | Dated records: what was asked, what was decided, how it was checked. |
| `tools/`, `tests/` | The tools below and their tests. |

A game's id is `<provider key>-<name>`, for example `pragmatic-gates-of-olympus`: the same as its art run's folder in Games-AI-art without the date.

## Tools

Python 3 with pdfplumber and Pillow; `pdftotext` and `pdftoppm` (poppler) when present. Run them with `python3 -I` from the repository's root.

| Command | What it does |
| --- | --- |
| `tools/ingest.py <file.pdf> [--slug …] [--date …]` | Takes a PDF into `reports/`. |
| `tools/ledger.py status` | The whole ledger in one table. |
| `tools/ledger.py unify <report id> [--dry-run] [--top 20]` | Joins the report's games to the ledger and fixes its leaders. Stops, writing nothing, on a name that could be two games. |
| `tools/ledger.py queue [--json]` | Leaders of any report still without a complete art analysis, best first. |
| `tools/ledger.py set <game id> demo=<link> …` | Sets a game's demo link, name, provider, type, family or notes; `alias+=<spelling>` adds a spelling. A link with a session key is refused. |
| `tools/ledger.py start <game id>` | An art run has begun. A complete game is refused: a game is analysed once. |
| `tools/ledger.py complete <game id> --run <run folder> --report <artifact address> [--drive …] [--miro …] [--commit …]` | The run is finished and published; keeps its digest here. |
| `tools/ledger.py block <game id> --reason "…"` | The game cannot be analysed, and why. |
| `tools/ledger.py seed` | Takes in what the sibling repositories hold (run once, on 25 Nov 2026; safe to run again). |
| `tools/build_site.py` | Writes `site/index.html` from all of the above. |
| `python3 -I -m unittest discover tests` | The tests. |

## `rankings.json`

```jsonc
{
  "title": "Top Performing Online Slots, Q3 2026",   // as on the cover
  "publisher": "…",
  "period": "Jul–Sep 2026",                           // what the rankings cover
  "published": "2026-10",
  "markets": ["US iGaming"],
  "notes": "What was left out and why (a provider ranking on page 9, …).",
  "lists": [
    {
      "id": "us-ggr",                                 // short, unique in the report
      "title": "Top 25 games by GGR, US",             // the list's own heading
      "metric": "Share of GGR",
      "market": "US",
      "page": 4,
      "weight": 1,                                    // leave out unless the record says why not
      "entries": [
        { "rank": 1, "game": "Cash Eruption", "provider": "IGT", "value": "1.9%" },
        { "rank": 2, "game": "Aviator", "provider": "Spribe", "type": "crash" },
        { "rank": 3, "game": "Gates of Olympus 1000", "provider": "Pragmatic Play", "new": true },
        { "rank": 4, "game": "Huff N More Puff", "provider": "L&W", "is": "lnw-huff-n-more-puff" }
      ]
    }
  ]
}
```

`rank` and `value` are as the report prints them (`null` when it gives none). `type` marks a game that is not a slot. `is` and `new` answer a name `unify` could not place.

## The leaders rule

Only slot games. A game earns `weight × (21 − rank)` points in each list that ranks it 1 to 20, and the 20 highest totals are the report's leaders (ties: the better best rank, then the name). With one list this is its first 20. The rule is the handler's way to join a report's lists; it is said to be so wherever the order is shown, and each report's lists are shown unchanged beside it.

## Boards

A Miro board on which the studio collects reference games is a second kind of input beside a report. Its games are typed into `boards/<YYYY-MM-DD>-<slug>/board.json` (`id`, `title`, `url`, `read`, `about`, and `games`: each with `game`, `provider`, and where the board gives them `market`, `note`, `link`; `"is": "<game id>"` or `"new": true` answers a name the ledger asks about) and joined with `python3 -I tools/ledger.py board <board id>`. A board's games are picks: they are analysed once like leaders, and wait in the queue after them (position 99). A market written on a board is the board's note, not a report's figure.

Every game has a **source**, shown by `ledger.py status` and in the summary's tables: Market report, Miro board, Intelligate HQ, Web research, Games AI art, as many as apply (`sources_of` in `tools/ledger.py`).

## Where things stand

27 Nov 2026: two reports are handled (Eilers-Fantini, U.S. Online Game Performance, July and August 2026 editions). They name 30 leading slot games between them; the ledger holds 93 games.

- **16 leaders are analysed**, each with a published art report: IGT (5), Octoplay (6), Light & Wonder (3), AGS (1), Inspired (1).
- **14 leaders are blocked**, each with its reason on the ledger (`ledger.py status`): Games Global (8, public demos refused for visitors from the United States), White Hat Studios (2), Aristocrat, Evolution, ReelPlay and IGT's Cash Eruption High Stakes (no public demo that opens). A blocked game is taken up again when a link or another machine is available: `ledger.py start <id>`.
- **Both documents are written** from the sixteen: `documents/art-report.md` and `documents/next-steps.md`. They are written again when a blocked leader is analysed or a new report adds leaders.
- The record of the run is `records/2026-11-25-eilers-fantini-july-august.md`.

