How a market report becomes this ledger. Every step is a tool in the repository `IntelligateStudios/market-reports-handler`; the procedure is its skill `handle-market-report`.

### 1. The report is taken

The PDF is copied in unchanged, with each page's text, a picture of each page and the tables found on it. A PDF taken before is recognised by its fingerprint and is not taken twice.

### 2. Its rankings are read

Every ranked list in the report is written down as the report prints it: the list's title, what it measures, the market, the page, and each game's rank, provider and value. Nothing is added to a list, and a value appears only as the report states it.

### 3. The games are joined to the record

Each ranked name is matched to the one ledger of games: the same title from the same provider is the same game, whatever the spelling, capitals or marks. A sequel or a version ("1000", "Megaways", "Xmas") is a game of its own. A name that could be two games is never guessed: the run stops until someone decides.

The ledger started from what the studio already had: the games with a PRD and GDD in Intelligate HQ, the games of our web research of 21 Nov 2026, and the art runs in Games AI art.

### 4. The report's 20 leaders are fixed

Only slot games count. With one list, the leaders are its first 20. With several lists, a game earns 21 − rank points in each list that ranks it in the first 20 (times the list's weight, 1 unless the run's record says why not), and the 20 highest totals lead. This rule is ours, a way to join a report's lists into one order. It is not a figure of the report, and each report's page shows its lists unchanged beside it.

### 5. Each leader is analysed once

A leader with no art analysis gets one: a run of Games AI art on the provider's public free-play demo, which extracts every texture, sprite and skeleton, measures every image and reads every art component. Its full report is published as its own page and linked here. A game analysed for an earlier report is not analysed again; its page simply gains the new report's rank. A game that cannot be analysed (no public demo, a client the tools cannot read) is marked Blocked with the reason.

### 6. The two documents are written

When every leader is analysed or blocked, two documents are written from the finished analyses: **Art of the leaders**, the games' art side by side, and **Next steps in art**, what Intelligate should do next, each recommendation resting on named games.

### Measured or read

| Label | What it means |
| --- | --- |
| Measured | Computed from the game's own pixels by fixed rules, the same for every game, so two games can be compared: palette and shares, brightness, saturation, contrast, warm and cool share, soft edges. |
| Read | Written by Claude from looking at the game's sheets and screens: style, rendering, lighting, ambience, materials. Inference is marked as inference. |
| As stated | Copied from a market report, with its page. |

### Limits

- A report's ranking is that publisher's view of its own markets and period; two reports can disagree, and both are kept.
- An art analysis covers the layout and the features the demo showed during the capture, at the size the game ships its art.
- Competitors' art is kept for study inside the studio and is not shared outside it.
