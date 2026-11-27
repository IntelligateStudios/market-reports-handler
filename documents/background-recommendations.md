Written 27 Nov 2026 for Roei, who asked: "send another agent to create recommendations section, focusing on "Game background , slot background , amount of elements of the background , contrast , saturation." To rank it, sorted by theo ranking where applicable." (Roei, 27 Nov 2026)

This section covers five things for every game: the **game background** (the scene or field behind and around the reels), the **slot background** (the reel window: what sits behind the symbols), **how many elements** the background holds, **contrast** and **saturation**.

**What it rests on.** The 16 of 57 leading slot games whose art analysis is finished: IGT 5, Octoplay 6, Light & Wonder 3, AGS 1 and Inspired 1. Games Global, Aristocrat and White Hat Studios are absent because their demos could not be opened. So this says what the leaders we could open do, not what the market does.

**The sort rule (ours).** Every table and list of games is in this order: each game stands at its rank in the most recent edition of the Eilers-Fantini report that ranks it in "Top Game Ranks – Slots" (by Theo Win Index). Games ranked in a newer edition come first; inside an edition, by that rank. The rank and the index are copied as the report states them. Six games are in the November 2026 edition; the other ten are not, and stand at their last ranked edition (September, August or July). One limit: the handler took ranks 1 to 50 of the July and August editions but only ranks 1 to 25 of September, October and November, so a game missing from a later edition is outside its first 25, not necessarily off the list.

**Measured and read.** *Measured* figures come from pixels: one real screenshot of each base game at rest, cropped into game background, reel window and symbols (the Method part gives the formulas; the crop boxes are in `documents/background-data.json`). *Read* statements are written from the pictures by looking at them, and mark inference as inference. Report figures are as stated.

## Recommendations

These are our inference from 16 games, not findings about the market. Each names the games and the figures it rests on.

1. **Reel window:** make it the darkest, quietest part of the screen: brightness 0.18 or less, contrast 0.17 or less.
2. **Symbols against the window:** about 4:1 in luminance on a dark window, or a cool window under warm symbols.
3. **Game background:** keep it darker than the symbols (0.10 to 0.40); under a bright scene, darken the window hard.
4. **Elements:** five groups at most, at the sides and the top; nothing that matters behind the reels.
5. **Saturation:** one hue can go to 0.9 and above if it stays dark; a painted scene of several hues stays at 0.45 to 0.75.
6. **Feature mode:** keep the composition and change the colour; paint a new scene only for the main bonus.
7. **See-through window:** only to show a feature object behind the reels, and tinted to 0.15 or darker.

### 1. Make the reel window the darkest, quietest part of the screen

- **Do:** put a plain dark panel behind the symbols. No picture in it; a faint pattern at most.
- **Target:** window brightness 0.18 or less, contrast inside the window 0.17 or less, and darker than the game background around it.
- **Measured:** 13 of 16 windows have a brightness of 0.18 or less (0.00 to 0.17). The three others are the teal cells of [Cash Eruption](#game-igt-cash-eruption) (0.24) and [Triple Cash Eruption](#game-igt-triple-cash-eruption) (0.20) and the cream window of [Cleopatra](#game-igt-cleopatra) (0.84). 12 of 16 have a contrast of 0.17 or less. In 14 of 16 the window is darker than the game background, and in 14 of 16 it has less contrast than the game background; the exceptions to both are [Cleopatra](#game-igt-cleopatra) and [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) (a window of 0.15 on a backdrop of 0.09).
- **Read:** where the window has a pattern it is faint and in the window's own colour: a fret ([Cash Eruption](#game-igt-cash-eruption), [Triple Cash Eruption](#game-igt-triple-cash-eruption)), a weave ([Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win)), a chevron ([Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win)), damask ([Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar)), a carved relief ([Serpent Gold](#game-octoplay-serpent-gold-hold-and-win)), a snout emblem ([Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus)), wood grain ([The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win)).

### 2. Separate the symbols from the window by about 4:1, or by opposite hue

- **Do:** check every symbol against the bare window. On a near-black window, rely on brightness. On a coloured window, rely on hue: a cool window under warm symbols.
- **Target:** a symbols-to-window luminance ratio of about 4:1 or more on a dark window. On a coloured window 2.7:1 can work if the hues are opposite.
- **Measured:** the ratio runs from 1.77 to 7.79, median 4.47; 10 of 16 games measure 3.99 or more. The game ranked first, [Cash Eruption](#game-igt-cash-eruption), measures only 2.67, and [Triple Cash Eruption](#game-igt-triple-cash-eruption) 3.72: both put red, orange and gold symbols (read) on a teal window (mean colour measured `#054c43` and `#063f37`). The lowest are [Cleopatra](#game-igt-cleopatra) (1.77), [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) (2.62) and [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) (2.89).
- **Read:** a symbol that must stand out brings its own tile: black behind the fireballs ([Cash Eruption](#game-igt-cash-eruption), [Triple Cash Eruption](#game-igt-triple-cash-eruption)), a coloured cloth behind each picture symbol ([Cleopatra](#game-igt-cleopatra)), a coloured square behind the high symbols ([Capital Gains](#game-ags-capital-gains)).

### 3. Keep the game background darker than the symbols

- **Do:** let the symbols be the brightest large thing on the screen. If the theme needs a bright scene, put a heavy dark tint between it and the symbols.
- **Target:** game background brightness 0.10 to 0.40, against symbols at 0.34 to 0.56. Under a brighter scene, a window at least 5:1 darker than the background.
- **Measured:** the symbols are brighter than the game background in 14 of 16 games; in those the background measures 0.09 to 0.40. The two bright scenes are [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) (0.69) and [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) (0.60); both tint the window down to 0.12 and 0.13, which gives the two largest window-to-background ratios among the games with a darker window (8.84 and 4.95).
- **Measured, contrast inside the background:** the nine painted scenes run from 0.32 to 0.86; the seven fields and light-only backdrops from 0.10 to 0.39. Both kinds are among the six games of the November edition, so we set no target for it.

### 4. Five groups of elements at most, at the sides and the top

- **Do:** plan the background as a frame around the reels. Count its groups of elements; stop at five. Put nothing that matters in the middle.
- **Read:** counted on the base-game screenshots, the backgrounds hold 1 to 5 groups of elements: 3 to 5 in the nine painted scenes, 1 to 3 in the seven fields and light-only backdrops. Nine games paint a place; five use a flat, graded or patterned field ([Cleopatra](#game-igt-cleopatra), [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win), [Capital Gains](#game-ags-capital-gains), [Money Gong Emperor](#game-igt-money-gong-emperor) and [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win)); two use light alone ([777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) and [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win)).
- **Read:** the reels and the prize plaques cover the middle of the picture. The mansion at the end of the avenue is hidden behind the wheel ([Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand)); the building site painted into the meadow is hidden behind the reels ([Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus)); the reels cover the middle of the mansion front ([Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion)).
- **Read, from the runs' own readings of frames and files:** in the fourteen games with a background picture, the picture itself stays still; what moves sits over it (torch flames, sparks, light shafts, swaying leaves). The two light-only backdrops move all the time. This section looked at stills, so it did not check motion itself.

### 5. One hue can be saturated to the top; several hues cannot

- **Do:** choose one of two patterns. A single-hue field or scene, saturated and dark. Or a painted scene of several hues, moderately saturated.
- **Target:** single hue: saturation 0.9 and above with brightness 0.30 or less. Several hues: saturation 0.45 to 0.75.
- **Measured:** six game backgrounds measure a saturation of 0.88 or more (0.89 to 0.97), and all six are dark (0.11 to 0.30): [Cash Eruption](#game-igt-cash-eruption) 0.93, [Cleopatra](#game-igt-cleopatra) 0.89, [Capital Gains](#game-ags-capital-gains) 0.97, [Money Gong Emperor](#game-igt-money-gong-emperor) 0.96, [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) 0.94 and [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) 0.96. The other ten measure 0.47 to 0.80; the eight painted scenes among them 0.47 to 0.73.
- **Read:** each of the six is one family of hue: orange-red stone, a violet to magenta sky, banknote green, red, red, clover green. The moderate ones mix hues: blue sky with green trees, red brick with blue sky, green pitch with a pink crowd.
- **Measured:** the symbols' saturation runs from 0.45 to 0.85. A window's saturation figure means little when the window is near black, so we set no target for it.

### 6. For a feature mode, keep the composition and change the colour

- **Do:** make the free spins or Hold and Win background from the base background: recolour it or regrade it to another time of day. Keep a new painting for the one bonus that carries the game.
- **Read:** 10 of 16 games keep the composition and change its colour or light: [Cash Eruption](#game-igt-cash-eruption), [Cleopatra](#game-igt-cleopatra), [Capital Gains](#game-ags-capital-gains), [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged), [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion), [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals), [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win), [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win), [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) and [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus). Five paint a new scene for a bonus: [Cash Eruption](#game-igt-cash-eruption), [Triple Cash Eruption](#game-igt-triple-cash-eruption), [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win), [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) and [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) ([Cash Eruption](#game-igt-cash-eruption) does both: a regrade for free spins, a new scene for the bonus). For [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) and [Money Gong Emperor](#game-igt-money-gong-emperor) no feature background was seen or could be placed. Of the ten recolours, six were seen in play and four are read from the files; the notes below say which.
- **Read:** seven of the ten recolours turn towards red, orange or gold ([Cash Eruption](#game-igt-cash-eruption), [Cleopatra](#game-igt-cleopatra), [Capital Gains](#game-ags-capital-gains), [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged), [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win), [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) and [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus)); three turn to night or purple ([Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion), [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) and [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win); the mansion also has a red and yellow evening).
- **Measured, on the background art files (figures from each run's `art.json`):** the brightness does not move one way. Base to feature: [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) 0.07 to 0.43, [Cash Eruption](#game-igt-cash-eruption) 0.17 to 0.26 (free spins), [Capital Gains](#game-ags-capital-gains) 0.37 to 0.26, [Cleopatra](#game-igt-cleopatra) 0.20 to 0.15, [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) 0.58 to 0.50. So the signal of a feature is the hue, not more light.
- **Read:** the window follows the background. Cream turns tan ([Cleopatra](#game-igt-cleopatra), seen), the wooden board turns purple ([The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win), seen), the red neon frame turns gold ([Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win), seen), the dark red backing turns gold ([Money Gong Emperor](#game-igt-money-gong-emperor), from the file).

### 7. Use a see-through window only to show a feature object, and tint it dark

- **Do:** keep the window opaque unless something behind the reels is part of the game. If it is, lay a dark tint over it.
- **Target:** a tint that brings the window to a brightness of 0.15 or less.
- **Read:** 4 of 16 games have a see-through window, and each shows a feature object through it: a prize wheel ([Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand), [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals), [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel)) or the prize plates on a mansion ([Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion)). The other twelve windows are opaque.
- **Measured:** the four tinted windows measure 0.07 to 0.15. The cost shows in [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion): its window contrast is 0.36, the highest of the thirteen dark windows, because the plates behind stay readable.

### What the rank order shows, and what it does not

The six games of the November edition and the ten ranked only in earlier editions overlap on every measure. Game background brightness: 0.16 to 0.40 against 0.09 to 0.69. Game background saturation: 0.68 to 0.97 against 0.47 to 0.96. Symbols to window: 1.77 to 7.79 against 2.62 to 5.44. Elements: 1 to 5 against 2 to 5.

The two highest-ranked games here do opposite things: [Cash Eruption](#game-igt-cash-eruption) has an opaque teal window in an orange-red hall, [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) a see-through tint over a wheel in a blue and green garden. One difference is in the figures: the only three windows brighter than 0.18 ([Cash Eruption](#game-igt-cash-eruption), [Triple Cash Eruption](#game-igt-triple-cash-eruption), [Cleopatra](#game-igt-cleopatra)) are all in the November edition, and all three are IGT games. That is a provider's habit as much as a ranking effect. Sixteen games are too few to claim a trend, and a rank reflects the game's maths, features, brand, age and distribution as well as its art.

## The tables

All in the sort order stated above. "Rank" is the edition and the rank the game is sorted on.

### Theo rank

| Game | Provider | Sorted on | Rank | Theo Win Index |
| --- | --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | IGT | November 2026 edition | 1 | 48.53x |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | Light & Wonder | November 2026 edition | 4 | 36.65x |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | IGT | November 2026 edition | 11 | 18.24x |
| [Cleopatra](#game-igt-cleopatra) | IGT | November 2026 edition | 13 | 17.07x |
| [Fire Rail Express Hold And Win](#game-octoplay-fire-rail-express-hold-and-win) | Octoplay | November 2026 edition | 17 | 15.29x |
| [Capital Gains](#game-ags-capital-gains) | AGS | November 2026 edition | 18 | 15.02x |
| [777 Hot Reels Megacharged](#game-octoplay-777-hot-reels-megacharged) | Octoplay | September 2026 edition | 18 | 14.06x |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | IGT | September 2026 edition | 19 | 13.39x |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | Light & Wonder | September 2026 edition | 24 | 12.12x |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | Light & Wonder | August 2026 edition | 22 | 13.72x |
| [Mystery Of The Lamp Secret Bazaar](#game-igt-mystery-of-the-lamp-secret-bazaar) | IGT | August 2026 edition | 26 | 12.30x |
| [Mega Cash Boost Hold And Win](#game-octoplay-mega-cash-boost-hold-and-win) | Octoplay | August 2026 edition | 32 | 11.15x |
| [Bigger Piggy Bank Superwheel](#game-inspired-bigger-piggy-bank-superwheel) | Inspired | July 2026 edition | 10 | 17.63x |
| [The Lucky Fella Hold And Win](#game-octoplay-the-lucky-fella-hold-and-win) | Octoplay | July 2026 edition | 16 | 15.79x |
| [Serpent Gold Hold And Win](#game-octoplay-serpent-gold-hold-and-win) | Octoplay | July 2026 edition | 17 | 14.55x |
| [Super Cash Boost Big Bad Bonus](#game-octoplay-super-cash-boost-big-bad-bonus) | Octoplay | July 2026 edition | 19 | 14.30x |

Rank and Theo Win Index in each edition, as the reports state them (list "Top Game Ranks – Slots"; pages are in the data file). A dash means the game is not among the ranks taken from that edition: 1 to 50 for July and August, 1 to 25 for September to November.

| Game | Jul | Aug | Sep | Oct | Nov |
| --- | --- | --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | 1 · 43.30x | 1 · 47.65x | 2 · 46.69x | 1 · 47.49x | 1 · 48.53x |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | 2 · 43.12x | 2 · 41.28x | 3 · 39.84x | 4 · 37.92x | 4 · 36.65x |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | 9 · 17.66x | 10 · 20.20x | 10 · 18.45x | 10 · 17.73x | 11 · 18.24x |
| [Cleopatra](#game-igt-cleopatra) | 14 · 16.33x | 17 · 15.21x | 15 · 15.22x | 18 · 14.48x | 13 · 17.07x |
| [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) | 3 · 27.51x | 7 · 22.78x | 9 · 18.53x | 12 · 16.59x | 17 · 15.29x |
| [Capital Gains](#game-ags-capital-gains) | 18 · 14.35x | 14 · 16.35x | 14 · 16.23x | 13 · 16.13x | 18 · 15.02x |
| [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) | – | 12 · 17.70x | 18 · 14.06x | – | – |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | – | 19 · 14.12x | 19 · 13.39x | – | – |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | 21 · 13.98x | 18 · 14.58x | 24 · 12.12x | – | – |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | 6 · 21.36x | 22 · 13.72x | – | – | – |
| [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) | 15 · 15.91x | 26 · 12.30x | – | – | – |
| [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) | 5 · 21.41x | 32 · 11.15x | – | – | – |
| [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) | 10 · 17.63x | – | – | – | – |
| [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) | 16 · 15.79x | – | – | – | – |
| [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) | 17 · 14.55x | – | – | – | – |
| [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus) | 19 · 14.30x | – | – | – | – |

### What the backgrounds are (read)

| Game | Rank | Game background | Elements | Reel window |
| --- | --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | Nov 1 | Scene: temple hall | 4 | Opaque teal cells |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | Nov 4 | Scene: garden avenue at night | 5 | See-through dark tint |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | Nov 11 | Scene: ruined temple | 3 | Opaque teal cells |
| [Cleopatra](#game-igt-cleopatra) | Nov 13 | Graded field with ruins | 2 | Opaque cream window |
| [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) | Nov 17 | Split field: fire and postcards | 2 | Opaque near-black |
| [Capital Gains](#game-ags-capital-gains) | Nov 18 | Flat field | 1 | Opaque black |
| [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) | Sep 18 | Light only: rays and neon lines | 2 | Opaque dark red-black |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | Sep 19 | Pattern field | 2 | Opaque dark red columns |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | Sep 24 | Scene: mansion front by day | 5 | See-through dark tint |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | Aug 22 | Scene: football stadium by day | 4 | See-through dark tint |
| [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) | Aug 26 | Scene: bazaar street at dusk | 4 | Opaque dark red damask |
| [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) | Aug 32 | Light only: beams | 2 | Opaque near-black |
| [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) | Jul 10 | Scene: bank hall | 4 | See-through dark tint |
| [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) | Jul 16 | Pattern field with leaves | 3 | Opaque wooden board |
| [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) | Jul 17 | Scene: misty rainforest | 3 | Opaque dark stone |
| [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus) | Jul 19 | Scene: meadow and mountains | 5 | Opaque dark brown |

How each is built and what moves. The motion column repeats each run's own reading of its frames and files; this section looked at stills.

| Game | Rank | Built as | Motion |
| --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | Nov 1 | One picture, torches over it | Torch flames only |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | Nov 4 | One picture, wheel in front | Still |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | Nov 11 | One picture | Still |
| [Cleopatra](#game-igt-cleopatra) | Nov 13 | One picture | Still |
| [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) | Nov 17 | Two pictures, sparks over them | Sparks drift |
| [Capital Gains](#game-ags-capital-gains) | Nov 18 | One picture | Still |
| [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) | Sep 18 | Ray picture and line pieces | Neon lines breathe, blocks pass |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | Sep 19 | One picture | Still in the file |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | Sep 24 | Layers: sky, clouds, mansion | Day seen; day to night in the files |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | Aug 22 | Picture and grass layers | Still |
| [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) | Aug 26 | One picture | Still |
| [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) | Aug 32 | Light shapes, no picture | Beams sweep all the time |
| [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) | Jul 10 | Layers: walls, door, light | Slow light shafts |
| [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) | Jul 16 | Layers: field, leaves, twigs | Leaves sway |
| [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) | Jul 17 | Layers: picture, branches, birds | Leaves sway |
| [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus) | Jul 19 | One picture, rays over it | Rays and butterflies |

### Game background (measured)

Measured on the background around the reels in the base-game screenshot. The last column is the base background art file's own brightness, contrast and saturation from the run's `art.json`.

| Game | Rank | Brightness | Contrast | Saturation | Art file |
| --- | --- | --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | Nov 1 | 0.23 | 0.50 | 0.93 | 0.17 · 0.34 · 0.95 |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | Nov 4 | 0.40 | 0.72 | 0.68 | 0.29 · 0.53 · 0.63 |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | Nov 11 | 0.22 | 0.79 | 0.69 | 0.42 · 0.59 · 0.53 |
| [Cleopatra](#game-igt-cleopatra) | Nov 13 | 0.16 | 0.19 | 0.89 | 0.20 · 0.17 · 0.88 |
| [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) | Nov 17 | 0.19 | 0.39 | 0.80 | 0.20 · 0.69 · 0.95; 0.20 · 0.35 · 0.65 |
| [Capital Gains](#game-ags-capital-gains) | Nov 18 | 0.30 | 0.18 | 0.97 | 0.37 · 0.30 · 0.97 |
| [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) | Sep 18 | 0.09 | 0.10 | 0.74 | 0.07 · 0.04 · 0.74 |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | Sep 19 | 0.13 | 0.20 | 0.96 | 0.10 · 0.14 · 0.97 |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | Sep 24 | 0.60 | 0.59 | 0.59 | 0.43 · 0.84 · 0.74; 0.86 · 0.38 · 0.36 |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | Aug 22 | 0.69 | 0.73 | 0.47 | 0.58 · 0.73 · 0.67 |
| [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) | Aug 26 | 0.21 | 0.32 | 0.56 | 0.26 · 0.45 · 0.56 |
| [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) | Aug 32 | 0.11 | 0.14 | 0.94 | no picture |
| [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) | Jul 10 | 0.27 | 0.86 | 0.73 | 0.48 · 0.85 · 0.50 |
| [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) | Jul 16 | 0.22 | 0.33 | 0.96 | 0.16 · 0.23 · 0.95 |
| [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) | Jul 17 | 0.32 | 0.58 | 0.47 | 0.31 · 0.60 · 0.38 |
| [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus) | Jul 19 | 0.30 | 0.49 | 0.57 | 0.45 · 0.81 · 0.49 |

[Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) and [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) build the base background from two files (fire and postcards; mansion and sky), given in that order.

### Reel window and symbols (measured)

| Game | Rank | Window brightness | Window contrast | Window saturation | Symbols brightness | Symbols saturation |
| --- | --- | --- | --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | Nov 1 | 0.24 | 0.27 | 0.94 | 0.41 | 0.78 |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | Nov 4 | 0.15 | 0.17 | 0.67 | 0.49 | 0.57 |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | Nov 11 | 0.20 | 0.14 | 0.93 | 0.46 | 0.74 |
| [Cleopatra](#game-igt-cleopatra) | Nov 13 | 0.84 | 0.50 | 0.28 | 0.56 | 0.61 |
| [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) | Nov 17 | 0.09 | 0.11 | 0.62 | 0.47 | 0.84 |
| [Capital Gains](#game-ags-capital-gains) | Nov 18 | 0.00 | 0.00 | 0.11 | 0.47 | 0.80 |
| [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) | Sep 18 | 0.15 | 0.26 | 0.73 | 0.40 | 0.70 |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | Sep 19 | 0.05 | 0.03 | 0.99 | 0.37 | 0.85 |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | Sep 24 | 0.13 | 0.36 | 0.58 | 0.51 | 0.54 |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | Aug 22 | 0.12 | 0.09 | 0.61 | 0.49 | 0.45 |
| [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) | Aug 26 | 0.06 | 0.03 | 0.98 | 0.37 | 0.76 |
| [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) | Aug 32 | 0.05 | 0.07 | 0.95 | 0.41 | 0.79 |
| [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) | Jul 10 | 0.07 | 0.12 | 0.53 | 0.40 | 0.74 |
| [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) | Jul 16 | 0.17 | 0.07 | 0.83 | 0.34 | 0.75 |
| [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) | Jul 17 | 0.11 | 0.13 | 0.69 | 0.38 | 0.68 |
| [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus) | Jul 19 | 0.17 | 0.16 | 0.49 | 0.53 | 0.57 |

### Contrast between regions (measured)

Luminance ratio of the brighter region to the darker one; 1.00 is no difference.

| Game | Rank | Symbols to window | Window to game background | Darker of the two |
| --- | --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | Nov 1 | 2.67 | 1.22 | window |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | Nov 4 | 4.65 | 3.45 | window |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | Nov 11 | 3.72 | 1.71 | window |
| [Cleopatra](#game-igt-cleopatra) | Nov 13 | 1.77 | 7.02 | background |
| [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) | Nov 17 | 5.53 | 1.78 | window |
| [Capital Gains](#game-ags-capital-gains) | Nov 18 | 7.79 | 3.04 | window |
| [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) | Sep 18 | 2.89 | 1.41 | background |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | Sep 19 | 5.11 | 1.70 | window |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | Sep 24 | 3.99 | 4.95 | window |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | Aug 22 | 5.44 | 8.84 | window |
| [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) | Aug 26 | 4.29 | 1.81 | window |
| [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) | Aug 32 | 4.67 | 1.48 | window |
| [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) | Jul 10 | 4.80 | 3.33 | window |
| [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) | Jul 16 | 2.62 | 1.45 | window |
| [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) | Jul 17 | 3.63 | 2.57 | window |
| [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus) | Jul 19 | 5.07 | 1.94 | window |

### Feature mode (read, with the art files' measured brightness)

| Game | Rank | Change | Seen | Base file brightness | Feature file brightness |
| --- | --- | --- | --- | --- | --- |
| [Cash Eruption](#game-igt-cash-eruption) | Nov 1 | Regrade and new scene | in play | 0.17 | free spins 0.26; bonus 0.11 |
| [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) | Nov 4 | Unknown | not seen | 0.29 | – |
| [Triple Cash Eruption](#game-igt-triple-cash-eruption) | Nov 11 | New scene | in play | 0.42 | bonus 0.16 |
| [Cleopatra](#game-igt-cleopatra) | Nov 13 | Recolour | in play | 0.20 | free spins 0.15 |
| [Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win) | Nov 17 | New scene | in play | 0.20; 0.20 | hold and win 0.20; jackpot hold and win 0.43 |
| [Capital Gains](#game-ags-capital-gains) | Nov 18 | Recolour | in play and files | 0.37 | free spins 0.26 |
| [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) | Sep 18 | Recolour | in play | 0.07 | free spins 0.43 |
| [Money Gong Emperor](#game-igt-money-gong-emperor) | Sep 19 | Unknown | files | 0.10 | features 0.08 |
| [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion) | Sep 24 | Regrade | files | 0.43; 0.86 | evening 0.35; night 0.16 |
| [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals) | Aug 22 | Regrade | files | 0.58 | free games 0.50 |
| [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) | Aug 26 | New scene | files | 0.26 | bonus 0.28 |
| [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win) | Aug 32 | Recolour | in play | no picture | – |
| [Bigger Piggy Bank](#game-inspired-bigger-piggy-bank-superwheel) | Jul 10 | New scene | in play | 0.48 | free spins 0.55 |
| [The Lucky Fella](#game-octoplay-the-lucky-fella-hold-and-win) | Jul 16 | Recolour | in play | 0.16 | free spins 0.11 |
| [Serpent Gold](#game-octoplay-serpent-gold-hold-and-win) | Jul 17 | Regrade | in play | 0.31 | bonus 0.31 |
| [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus) | Jul 19 | Regrade | files | 0.45 | bonus 0.49 |

## The games, one by one

In the same order. Descriptions are read from the pictures named in the data file; the screenshot each measure used is named at the end of each note. How each background is built and what moves is in the table above.

- **[Cash Eruption](#game-igt-cash-eruption)** (IGT; November edition, rank 1). The inside of a stone temple in orange-red light, seen straight on, with a live torch at each side. 4 groups: back wall of stone blocks, stepped piers left and right, stair across the bottom, two torches. **Reel window:** Opaque teal cells with a faint fret pattern, gold dividers, a thin patterned frame. The fireball symbols bring their own black tile. **Feature mode:** Free spins: the same hall pushed brighter and redder (seen in play, `fs-01-start`). Bonus: a new scene, a volcano crater under a red spiral sky, with the cells dimmed to dark teal (seen in play, `bonus-02-early`). Measured on `01-main.webp`.
- **[Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand)** (Light & Wonder; November edition, rank 4). A night garden: rounded topiary trees, clipped hedges and lit street lamps under a blue sky. The feature wheel stands behind the reels and hides the mansion at the end of the avenue. 5 groups: night sky, topiary trees, hedges and lawn, street lamps, the feature wheel behind the reels. **Reel window:** No panel: a dark olive tint over the wheel, which shows faintly between the symbols. No frame and no dividers. **Feature mode:** No second background is among the captured files and no feature was seen in play. That free spins keep this scene is inference from the files (a hedge overlay strip). Measured on `01-base-at-rest.png`.
- **[Triple Cash Eruption](#game-igt-triple-cash-eruption)** (IGT; November edition, rank 11). A ruined temple in violet shadow with a white-hot break of lava light in the wall behind the reels. 3 groups: carved pillars left and right, broken wall with lava light, cobbled floor. **Reel window:** Opaque teal cells with a faint fret pattern in a thin red patterned frame. The fireball symbols bring their own black tile. **Feature mode:** Bonus: a new scene, the volcano crater under a red sky, with two boards of dimmed dark teal cells (seen in play, `bonus-03-values-land`). Measured on `main-01-base-at-rest.webp`.
- **[Cleopatra](#game-igt-cleopatra)** (IGT; November edition, rank 13). An empty sky graded from violet to magenta, with a dim colonnade in the two bottom corners. 2 groups: graded sky, colonnade ruins, mirrored left and right. **Reel window:** A cream window in a heavy gold cabinet, with bead dividers. Each picture symbol sits on its own coloured cloth tile; the letters sit on the cream. **Feature mode:** Free spins: the same picture recoloured from purple to red, and the window from cream to tan (seen in play, `09-free-spins`). Measured on `01-main.webp`.
- **[Fire Rail Express Hold And Win](#game-octoplay-fire-rail-express-hold-and-win)** (Octoplay; November edition, rank 17). No place: a dark red fire field with sparks on the left and torn purple postcards with line drawings of locomotives on the right. 2 groups: fire field with sparks, purple postcard collage. **Reel window:** A near-black panel with a faint weave in a thin gold frame, with dark dividers. **Feature mode:** Hold and Win: a new picture from the same motifs, the postcards spread across the whole screen in purple and gold (seen in play, `14-hold-04-bonus-start`). Jackpot Hold and Win: fire across the whole screen (seen in play, `19-jackpot-03-bonus`). Measured on `02-main.webp`.
- **[Capital Gains](#game-ags-capital-gains)** (AGS; November edition, rank 18). A flat banknote-green field with soft lighter pools behind the logo and the reels. 1 group: green field with light pools. **Reel window:** Black cells with thin dividers inside a green edge. The high symbols bring their own coloured tile; the letters sit on the black. **Feature mode:** Free spins: the same field recoloured red with the top edge left green (read from the file `fs_background_ls`; not seen in play). The Money Charge bonus keeps the green field and slides a vault panel in at the left (seen in play, `08-bonus-nine`). Measured on `01-main.webp`.
- **[777 Hot Reels Megacharged](#game-octoplay-777-hot-reels-megacharged)** (Octoplay; September edition, rank 18). No place: a near-black purple field of faint rays with thin red neon frame lines at both sides. The cabinet glows gold in front of it. 2 groups: purple ray field, red neon frame lines. **Reel window:** A dark red-black panel with gold dividers inside the gold cabinet frame. The symbols nearly fill their cells. **Feature mode:** Free spins: the same composition turned from purple to orange and red rays, with red 777 blocks on gold at the sides (seen in play, `16-free-spins-01`). Measured on `02-main-01.webp`.
- **[Money Gong Emperor](#game-igt-money-gong-emperor)** (IGT; September edition, rank 19). A flat red ground covered with a small wave-scale pattern, with one round ring at the left that holds the gong. 2 groups: red wave-scale pattern, round ring for the gong. **Reel window:** Five dark red columns, each lit down its middle, between gold dividers in a gold scroll frame. **Feature mode:** No feature was seen in play. Read from the files: a separate dark red curtain scene with firecrackers (`FeaturesBG`), and a gold wave-scale reel backing for the bonus spins (`Reel--FS--Background`). Where the curtain scene is used is not known from this run. Measured on `02-main.webp`.
- **[Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion)** (Light & Wonder; September edition, rank 24). The front of a red-brick mansion with a gold roof under a blue sky; its roof holds the prize plates and the reels cover its middle. 5 groups: sky with clouds, mansion front and roof, cypress trees, round bushes, steps and drive. **Reel window:** A dark tint over the mansion: its wall and prize plates stay readable between the symbols. Thin gold frame and dividers. **Feature mode:** Read from the files, not seen in play: the same mansion in an evening version (red and yellow) and a night version (violet and deep blue), each with its own sky. Measured on `03-base-at-rest.png`.
- **[Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals)** (Light & Wonder; August edition, rank 22). A football stadium seen from the pitch: bright striped grass, a pale touchline wall and two tiers of crowd in red and pink. Two goals and the feature wheel sit above the reels. 4 groups: striped pitch, touchline wall, crowd stands, roof and sky. **Reel window:** A dark green tint with a grass top edge and no frame; the wheel shows faintly at its top. A reel that holds a feature symbol stack turns red or blue. **Feature mode:** Read from the file `bg_freegame`, not seen in play: the same stadium at night under a starry sky with floodlight beams and a cooler pitch. Measured on `01-base-at-rest.png`. Read from the UK build of the game; that its art matches the US game is inference.
- **[Mystery Of The Lamp Secret Bazaar](#game-igt-mystery-of-the-lamp-secret-bazaar)** (IGT; August edition, rank 26). A covered bazaar street at dusk in warm brown and red, with stalls of fruit at both sides. 4 groups: stalls with fruit and vegetables, baskets, sacks and jars, arches and awnings, wall lanterns. **Reel window:** Dark crimson damask panels between gold dividers in a thin gold frame with curled finials. **Feature mode:** Read from the file `bonusBg`, not seen in play: a new scene, a treasure cave in blue and violet light. Measured on `01-main.webp`.
- **[Mega Cash Boost Hold And Win](#game-octoplay-mega-cash-boost-hold-and-win)** (Octoplay; August edition, rank 32). No picture: a dark red space crossed by red and white light beams. 2 groups: dark red field, red and white beams. **Reel window:** A near-black panel with a faint chevron in a thin red neon frame, with hairline dividers. **Feature mode:** Hold and Win: the same field turned orange-gold with yellow beams, and the frame turned gold (seen in play, `18-hold-04-board`). Measured on `06-main.webp`.
- **[Bigger Piggy Bank Superwheel](#game-inspired-bigger-piggy-bank-superwheel)** (Inspired; July edition, rank 10). A navy bank hall with tall pale windows at both sides and a round vault door behind the reels; a band of starry sky with the Super Wheel runs across the top. 4 groups: navy walls, tall windows left and right, round vault door, starry band with the Super Wheel. **Reel window:** A near-black navy tint in a thin gold frame; the wheel behind shows faintly. The fifth reel has a green backing on the measured screenshot. **Feature mode:** Free spins: a new scene, the inside of the vault in bright gold; the board stays dark (seen in play, `11-freespins-scene`). Measured on `01-base-rest.webp`.
- **[The Lucky Fella Hold And Win](#game-octoplay-the-lucky-fella-hold-and-win)** (Octoplay; July edition, rank 16). A dark green field with a faint diamond lattice, ringed by large clover leaves and twigs. 3 groups: green lattice field, large clover leaves, twigs. **Reel window:** A red-brown wooden board in a thin wavy gold frame, with hairline dividers. **Feature mode:** Free spins: the same composition turned purple with a rainbow ribbon and clovers in pink, blue and yellow; the board turns purple too (seen in play, `16-fs-05-wild-reels`). Measured on `03-main.webp`.
- **[Serpent Gold Hold And Win](#game-octoplay-serpent-gold-hold-and-win)** (Octoplay; July edition, rank 17). A misty green rainforest with large leaves framing the corners and a bird at each side; a stone serpent head sits on the reel frame. 3 groups: misty forest, foreground leaves, two birds. **Reel window:** A dark brown carved stone panel with vines as dividers in a carved stone frame. **Feature mode:** Bonus: the same forest at dusk in orange and violet, with carved temple walls brought in at the sides around a larger board (seen in play, `14-bonus-02`). Measured on `03-main-01.webp`.
- **[Super Cash Boost Big Bad Bonus](#game-octoplay-super-cash-boost-big-bad-bonus)** (Octoplay; July edition, rank 19). A storybook valley: fir woods and blue mountains under white clouds, with a dirt path through a meadow. The prize plates and the reels cover its middle. 5 groups: sky with clouds, mountains, fir woods, meadow and bushes, dirt path. **Reel window:** A dark brown panel with a faint snout emblem in a thin gold frame, with gold dividers. **Feature mode:** Read from the file `bgSpecial`, not seen in play: the same valley at sunset with the three houses built. Measured on `03-main-01.webp`.

## Method and limits

**Method, the same for all sixteen.**

- **The picture.** One real screenshot of the base game at rest, from the run's `game-screens/`. We looked at it first and drew the crop boxes by eye; every box is in `documents/background-data.json`.
- **Game background.** Boxes on the background outside the reel board, clear of the logo, the prize plaques and the buttons.
- **Reel window.** Small boxes on bare window between the symbols.
- **Symbols.** The centre half of every cell of the reel grid.
- **Brightness.** Mean luma (0.2126 R + 0.7152 G + 0.0722 B on the stored values), from 0 to 1.
- **Contrast.** The 95th minus the 5th percentile of that luma inside the region, from 0 to 1. The data file also holds the RMS contrast.
- **Saturation.** Mean HSV saturation, (max − min) / max, from 0 to 1.
- **Between two regions.** A WCAG-style ratio, (L1 + 0.05) / (L2 + 0.05), of the regions' mean relative luminance, the brighter over the darker.
- **Consistency with the art project.** Brightness, contrast and saturation use the formulas of Games-AI-art `tools/measure.py`. The difference: that tool measures a whole art file reduced to 160 px and weighted by its transparency; here every pixel of a crop of a screenshot counts. The "art file" figures are copied from each run's `art.json`.
- **Elements.** A group is one kind of thing a viewer would name (sky, trees, lamps). Counted on the base-game screenshot; logo, prize plaques, buttons and characters on the reel frame are not counted.

**Limits.**

- **Sixteen games, five providers.** 41 leaders are not here, among them every game of Games Global, Aristocrat and White Hat Studios.
- **One frame.** A screenshot is one moment. Backgrounds that move ([Fire Rail Express](#game-octoplay-fire-rail-express-hold-and-win), [777 Hot Reels](#game-octoplay-777-hot-reels-megacharged) and [Mega Cash Boost](#game-octoplay-mega-cash-boost-hold-and-win)) measure differently from frame to frame. Screens are desktop landscape captures; portrait layouts were not measured.
- **Boxes by eye.** Another choice of boxes moves the figures a little. A symbol core holds some window where the symbol is thin, which lowers the symbols-to-window ratio; a window patch can touch a symbol's glow.
- **Few real screens.** [Huff N Even More Puff Grand](#game-lnw-huff-n-even-more-puff-grand) and [Money Gong Emperor](#game-igt-money-gong-emperor) have six real screens each and no feature in play. Features not seen in play, and read from the files instead: the free spins of [Capital Gains](#game-ags-capital-gains), and the feature backgrounds of [Huff N Puff Money Mansion](#game-lnw-huff-n-puff-money-mansion), [Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals), [Mystery Of The Lamp](#game-igt-mystery-of-the-lamp-secret-bazaar) and [Super Cash Boost](#game-octoplay-super-cash-boost-big-bad-bonus).
- **[Huff N Lots Of Goals](#game-lnw-huff-n-lots-of-goals)** was read from the UK build of the game. That its art is the same as the US game the report ranks is inference.
- **Motion** was not checked here; the motion lines repeat each run's own reading.
- **Ranks.** For September to November only ranks 1 to 25 were taken from the reports, so ten games are sorted on an older edition. The report's publisher says its data is a sample. A rank is not a measure of the art.
