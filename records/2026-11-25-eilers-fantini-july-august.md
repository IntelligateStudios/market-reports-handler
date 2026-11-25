# Eilers-Fantini U.S. Online Game Performance Report, July and August 2026 editions (handled 25 Nov 2026)

## What was asked

Roei, 25 Nov 2026: attached two PDFs to the chat with no words, after the request recorded in `2026-11-25-origin.md` ("Given a PDF … understand which slot games are top ranked, take the 20 leading games …").

- `EILERS-FANTINI_U.S._Online_Game_Performance_Report_-_July_2_2.pdf`: July 2026 edition, published 21 Jul 2026, data through June 2026, 80 pages.
- `EILERS-FANTINI_U.S._Online_Game_Performance_Report_-_August_.pdf`: August 2026 edition, published 25 Aug 2026, data through July 2026, 80 pages.

Both carry on their cover a line naming the subscriber they were issued to and "Unauthorized distribution prohibited", and the notice that no part may be copied or disseminated without the publisher's consent. They are kept here for the studio's own use; Roei is told.

## What was read

The ranking tables are pictures, not text, so each was read from the page picture (`pages/045.png` and so on) and typed into `rankings.json`. Per report, three lists:

| List | Page | Counts towards the leaders |
| --- | --- | --- |
| Top Game Ranks – Slots, ranks 1 to 50, by Theo Win Index | 45, 46 | Yes (weight 1) |
| Top Games by GGR – Overall, 25 games of every type | 43 | No (weight 0): the same games by another measure, with live and table games |
| NEW Top Game Ranks – Slots, 25 games under 191 days in the database | 57 | No (weight 0): a subset of the slot ranking |

So each report's 20 leaders are simply the first 20 of its own slot ranking. Left out: the overall rank (page 42), every non-slot ranking (pages 47 to 54), the other new-game rankings and the supplier and game-type summaries.

## Decided without asking

- **Every version is its own game**: Cash Eruption, Triple Cash Eruption, Cash Eruption High Stakes, Megajackpots Cash Eruption and Cash Eruption Slingo are five games; so are the 7s Fire Blitz and Huff N Puff titles.
- **"Crazy Time Live"** (Evolution) is the "Crazy Time" already on record from the web research of 21 Nov.
- **Truncated titles**: "The Goonies Megaways Quest For Treasure Jack.." is kept as printed (July, rank 44). "Big Catch Even Bigger Bass 3 Megaways Jackpot .." (August, rank 48) is completed from the same page's Key Observations, which print it whole.
- **Suppliers as the report groups them**: Divine Fortune Gold is listed under Evolution (the parent of NetEnt).
- Page pictures are kept only for pages 42 to 60, the rankings; `source.pdf` holds the rest.
- The two reports together name 30 different leaders (20 in August, 10 more in July). The queue takes them by best position.

## How it was checked

Each typed list was read back against its page picture row by row (rank, title, supplier, index). `ledger.py unify --dry-run` placed every name with no doubt left; 93 games are now on the ledger.
