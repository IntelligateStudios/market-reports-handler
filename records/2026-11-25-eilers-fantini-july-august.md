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

## The analyses (25 to 27 Nov 2026)

One analyst sub-agent per leader, each following `analyst-brief.md`; the main session found the hard demos, ran the Light & Wonder captures, closed each game (secrets check, README row in Games-AI-art, `ledger.py complete`, summary rebuilt and republished) and committed both repositories.

- **16 analysed**: Cash Eruption, Triple Cash Eruption, Cleopatra, Mystery Of The Lamp Secret Bazaar, Money Gong Emperor (IGT); Capital Gains (AGS); Fire Rail Express Hold And Win, 777 Hot Reels Megacharged, Mega Cash Boost Hold And Win, Super Cash Boost Big Bad Bonus, Serpent Gold Hold And Win, The Lucky Fella Hold And Win (Octoplay); Huff N Even More Puff Grand, Huff N Puff Money Mansion, Huff N Lots Of Goals (Light & Wonder); Bigger Piggy Bank Superwheel (Inspired). Each run, its report address and its commit are on the ledger.
- **14 blocked**, reasons on the ledger: eight Games Global titles (demos refused for the United States), 7s Fire Blitz Power Force 5 and Hotstepper 2 (White Hat Studios, no public demo), Lightning Link High Stakes (account only), Divine Fortune Gold (access denied, age gate), Hypernova Megaways (server unreachable), Cash Eruption High Stakes (not yet on the demo host).
- Roei, 26 Nov 2026: "yes it may identify itself as it needs to make it work" (the capture names itself desktop Chrome). Nothing else was changed about how a demo is reached: no proxy, no account, no gate.
- Games-AI-art pull request #18 (merged 27 Nov, on Roei's "go-ahead") holds the first eleven runs and the tool changes; the last five runs are on the branch `claude/market-research-slot-games-yh6cnm`.

## The two documents (27 Nov 2026)

`documents/art-report.md` and `documents/next-steps.md` were written by the main session from the sixteen digests in `analyses/` (each game's `direction` fields and measured figures).

- **Decided without asking**: to write them with 14 leaders blocked, saying so at the top of both, since no blocked game can be opened from here; to group the games into three families of look (our reading); to phrase the second document as recommendations marked as inference.
- **How it was checked**: every count in them was taken from the ledger or the digests (leaders per provider, 12 of 16 games on Spine 4.x, brightness under 0.5 in 12, warmer than cool in 13, a very dark largest palette colour in 11, by script); every game-specific statement was taken from that game's own takeaways or direction text; both pages were opened at desktop and phone width with no overflow and no dead link.

## What stays open

- The 14 blocked leaders, and the bonus rounds not seen in play (listed at the end of the art report).
- No Drive folder or Miro board was made for the sixteen runs.
- The licensed PDFs stay in the repository and the summary stays a private artifact; nothing was shared or posted.
- Tool gaps, in Games-AI-art `.claude/skills/extract-game-art/providers.md`: a Spine 4.x renderer first.
- The handler's default branch: the repository has only the working branch; `main` is for Roei to create on GitHub (a push to `main` from the session was refused).
