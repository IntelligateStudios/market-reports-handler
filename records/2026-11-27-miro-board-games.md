# Games from the Miro board

27 Nov 2026.

## What was asked

Roei, 27 Nov 2026: "also go the miro board https://miro.com/app/board/uXjVEJ-AMw8=/ and add the games from there (also add column 'source' to our records and report)"

## What the board holds

Read with the Miro connector, read-only: 98 items. Eleven headings each name a game or a series with its provider in red; a yellow sticky beside each gives the market ("US", "EU", "US/EU"); 72 screenshots sit under them (not opened). One heading is a series with three linked games, so the board names 13 games:

| Game | Provider as the board writes it | Market note |
| --- | --- | --- |
| Coin Strike, Coin Strike 2, Coin Strike XXL (the "Coin Strike series", each linked to its page on playson.com) | Playson | US/EU |
| King of the sky | Playson | US |
| 4 Pots Riches | Playson | US/EU |
| Sugar Teddy | Playson | US |
| 4 Gold Cards | Kendoo | US/EU |
| Locomoto | Kendoo | US/EU |
| Zeus Power | Kendoo | US/EU |
| Lucky penny 3 pots | 3oaks | US/EU |
| Lucky Penny 2 | none written | US/EU, "Most GGR comes from Turkey" |
| More magic Apples | 3oaks | EU |
| Voltage Blitz | Koala | none |

## Decided without asking

- "Add the games" is taken as: put them on the ledger and analyse each once, like a report's leaders. They are not leaders of any report; they wait in the queue after the leaders as board picks.
- A board is a new kind of input beside a report: `boards/<date>-<slug>/board.json`, joined with `ledger.py board <id>`. The same matching rules apply (never guess; a version is its own game).
- "Source" is a column in the ledger's status, in the summary's tables and on each game's page: Market report, Miro board, Intelligate HQ, Web research, Games AI art, as many as apply.
- Lucky Penny 2 is entered with no provider, as the board has none; its analyst establishes it. That it is 3 Oaks Gaming's, like Lucky Penny 3 Pots, is inference.
- Titles are written with capitals; the board's own spelling is kept as an alias. The market notes are copied as written, and are the board's statements, not a report's.
- Kendoo and Koala are new providers.
- Nothing was written to Miro.

## After

- `tools/ledger.py` gained `board` and `sources_of`; `queue` lists board picks after the leaders; `tools/build_site.py` shows Source in the summary's leader table, the games table and each game's page, and a section "From the Miro board of reference games" with the market as the board notes it. Two tests cover it (16 pass).
- The ledger holds 159 games; 13 are board picks, none of them named by any of the five reports. "Coin Strike 2" and "Coin Strike XXL" were entered as games of their own beside "Coin Strike".
- **Open**: the 13 picks wait for analysis behind the report leaders; the board's 72 screenshots were not opened; the Backgrounds, Art of the leaders and Next steps texts name only report leaders so far.
