# Fire Rail Express: Hold & Win: art report

octoplay · run `2026-11-26-1556-octoplay-fire-rail-express-hold-win` · captured 2026-11-26

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/fire-rail-express-hold-and-win

**Extracted:** 578 named components from 36 textures in 36 atlases; 41 Spine skeletons; 25 frame sequences (445 frames); 3 fonts. Grouped into 21 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A classic 3x3 fruit machine dressed as a gold steam train: one glossy purple-and-gold locomotive, a screen split between fire and purple postcards, and gold coins whose centre colour names the jackpot.

**Style.** Glossy casino illustration with a 3D-rendered look for the train, coins and symbols, set against graphic paper ephemera (postcards and tickets printed with engravings) and Wild West poster lettering. The reel board itself is restrained Art Deco.

**Rendering.** Smooth airbrushed volumes, pinpoint highlights and hard outer edges on every object; soft additive glows and cartoon fire for effects. Symbols carry a warm rim light so they sit in the fire's glow.

**Colour.** Gold and fire against purple. Measured over the game's art: near-black #240d0f 26%, orange #e9800f 13%, dark purple #431a56 11%, brown #804309 11%, gold #f6c723 6%, light gold #fdfcf7 4%, dark red #740505 3%. The four jackpots own purple (MINI), blue (MINOR), green (MAJOR) and red (GRAND), repeated on coin, plaque and win word; the three win tiers are purple, blue and red. The amounts are purple numerals with a gold rim. Steel grey appears once, on the horseshoe.

**Lighting.** Objects are lit from the upper left or front with a red-orange rim from below right; the backdrop's fire lights from the bottom of the screen. Lamps, coins' flames and all effects are self-lit.

**Ambience.** A furnace and a ticket office: hot, rich, a little nostalgic. The base game is half fire and half cool purple; the cash bonus turns the backdrop to gold and purple postcards, the jackpot bonus to fire across the whole screen.

**Shape language.** Circles (coins, wheel, boiler door, fire rings), the perforated ticket rectangle, rounded plaques with one cut corner, a thin square frame, fat slab-serif letters.

**Materials.** Polished gold, lacquered purple steel, enamel, copper, steel, fruit skin, worn printed card, fire, steam.

**Typography and lettering.** Drawn lettering in one family of Western slab serifs: black on gold for the logo, fire-filled for WILD, coloured enamel for the jackpot words, purple, blue and red with gold outlines for the win tiers, cream with a red edge for the splash sentences. One bitmap numeral font, purple with a gold rim. Everything else is the provider shell's Poppins (Regular, SemiBold, Bold).

**Motion.** All motion is Spine 4.2.43: 41 skeletons in one file, most of them scene layers and effects, moving still pictures and 25 hand-drawn frame sequences (445 frames: fire, glints, a turning coin and ticket). The train is one picture with animated wheel, rods, highlights and sparks. Seen in play: a fire sweep after START, coins thrown on the pile, the train driving across the reels into the bonus, coin and ticket showers, fire inside the live jackpot frame. No skeleton frame is shown in this report, because the project's renderer is written for Spine 3.7.

**Variants and themes.** Three backdrop states (base, cash bonus, jackpot bonus), two reel boards, six coin faces from one blank, two collectors from one train, two splash cards, three win tiers from one layout, fruit symbols from one fruit each with darker side copies.

**How it is built.** Three 4096 px atlas pages hold 532 sprites; backdrops are tall columns, the board and frames are mirrored halves, flames ship white to be tinted, words are separate from the coins and plaques they sit on. Five localised lettering files (en-GB). Paytable and buy-card pictures, the numeral font and the interface come from the provider's shared services.

**Consistency.** High. Gold, the flame emblem and the slab serif recur on every piece, and the ticket shape returns as logo, particle and backdrop. The one seam is between the rendered-look objects and the flat engraved postcards, and it is used on purpose as foreground against background.

**What to take from it.** (1) One hero object can carry a game: the train is a single picture, and highlights, sparks, a blurred wheel and a coin pile make it feel alive. Budget the render, not the rig. (2) Colour-code the prizes end to end: each jackpot keeps its colour on the coin, the plaque and the win word, so a 3x3 board reads at a glance. (3) A classic fruit set is made new by context, not by redrawing fruit: rim light from the fire, three-of-a-kind clusters built from one painted fruit and a darker copy. (4) Split the backdrop into two contrasting halves (hot painted fire, cool printed paper) and swap them per feature: three moods from four narrow pictures. (5) Ship fire and light in white and tint in the game: one flame sequence serves every jackpot colour. Useful for AI-made effects too, where consistent colour across frames is hard. (6) Keep words apart from the objects they label (coins, plaques, splashes): localisation touches five files only. (7) For AI art work: the painted pieces are few and still; the craft is in consistency of gold, rim light and lettering, which is where a style reference and a fixed palette (#f6c723 gold, #431a56 purple, #e9800f fire) should be set.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm, medium contrast, hard-edged · brightness 36% · saturation 77% · contrast 57% · warm 72% / cool 20% · brighter towards: top (46), top-right (22), left (17)

Palette: #240d0f black 27%, #e9800f orange 14%, #431a56 dark purple 12%, #804309 brown 12%, #f6c723 gold 7%, #fdfcf7 light gold 5%, #bc7716 orange 4%, #740505 dark red 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 25% | 84% | 56% | 73% / 23% | #250c0c black 35%, #804408 brown 17%, #461c54 dark purple 15% |
| Reel board | 1 | 24% | 56% | 47% | 90% / 3% | #1e1010 black 71%, #f37b15 orange 10%, #28fe0a green 7% |
| Symbols | 5 | 55% | 73% | 62% | 78% / 13% | #f6861c orange 30%, #fefcee light gold 10%, #fac92a gold 10% |
| Characters | 1 | 55% | 59% | 69% | 80% / 7% | #f0af2a orange 19%, #f3f1eb light orange 17%, #6b3f0f brown 16% |
| Logo and title | 2 | 56% | 67% | 85% | 97% / 0% | #f7dc4c gold 29%, #0a0402 black 18%, #d1aa2f gold 15% |
| Win celebrations and banners | 3 | 42% | 71% | 64% | 55% / 37% | #4f1a6a dark purple 19%, #210e30 dark purple 16%, #f1b832 orange 15% |
| Effects | 3 | 77% | 53% | 31% | 67% / 0% | #fefdfc light orange 37%, #f37303 orange 23%, #f5c607 gold 15% |
| Game interface | 3 | 47% | 73% | 64% | 88% / 7% | #f37b11 orange 26%, #251516 black 13%, #f2b43a orange 13% |
| Typography | 1 | 42% | 76% | 83% | 81% / 0% | #600753 dark magenta 22%, #efbe3f orange 17%, #932589 magenta 16% |
| Provider interface (shared) | 1 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backdrops: fire field and train postcards

`backgrounds` · atlas · 4 parts · largest 2750×2510 · sheet `sheets/backgrounds.webp`

- **Role:** The full-screen pictures behind the reels: two for the base game and two for the bonus games.
- **Subject:** bgNormal is a tall column of dark red with yellow fire at its foot and sparks rising; bgNormalCards is a stack of torn purple postcards printed with pale line drawings of locomotives, wheels and the word POSTCARD. bgSpecial is a full spread of the same postcards in purple and gold; bgSpecial1 is a column of orange and yellow flame.
- **Style:** Two manners side by side: a soft painted fire and a graphic print, blueprint-like engravings in one pale ink on tinted, worn card. On the screens the fire fills the left of the base game and the cards the right, cut on a diagonal.
- **Rendering:** Dark and saturated (brightness 0.25, saturation 0.845). The cards have scuffed edges, creases and specks; the fire is smooth gradients with small hard sparks. Measured soft edge is near 0 because the pictures are opaque rectangles.
- **Colour:** bgNormal #290202 and #750903 dark reds with #ae1f07 and gold #f3c818 at the foot; bgNormalCards #361343, #603173 and #8150a7 purples; bgSpecial adds gold-brown #ab670b and #6c3e07 to purple #431a4f; bgSpecial1 is orange #e17d0d (40%) with yellow #f5c01b.
- **Lighting:** The fire lights from below: measured light sits at the bottom of the pictures. The cards are evenly lit with a faint sheen and no cast shadow except where one overlaps another.
- **Ambience:** Heat on one side, old paper and travel on the other: a furnace and a collector's album. It tells the theme (steam train, fire, tickets) without a landscape.
- **Materials:** Flame, embers, worn printed card.
- **Variants:** Base game: fire left, purple cards right. Cash Hold & Win: the gold and purple spread (bgSpecial). Jackpot Hold & Win: fire across the whole screen (seen in play; bgSpecial1 is the flame column it is made with, inference).
- **Motion:** The pictures are still. On the screens sparks, light streaks and a four-point glint drift over the fire; these come from the BackgroundEffects and ForegroundEffects skeletons (loop 6.63 s, the last key time in the file) and from particle textures, not from the backdrop itself.
- **Construction:** Four opaque pictures, each 2510 px high: columns 866, 785 and 1100 px wide and one spread 2750 px wide. The columns are placed, stretched or mirrored by the Backgrounds skeleton (2 bones, 2 slots); how exactly is not read from the file.
- **Notes:** Shipping narrow columns instead of full screens keeps four backdrops on one 4096 px page. The postcard motif is reused by the feature splash and the buy cards.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 25% · saturation 84% · contrast 56% · warm 73% / cool 23% · brighter towards: bottom (3), bottom-left (1)
- **Palette (measured):** #250c0c black 35%, #804408 brown 17%, #461c54 dark purple 15%, #ca750e orange 12%, #703b80 purple 6%, #f4c21a gold 5%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board: gold frame, dark backing, lock bars and markers

`reel-board` · atlas · 38 parts · largest 589×715 · sheet `sheets/reel-board.webp`

- **Role:** The frame and backing of the 3x3 reels, with what marks a cell in the bonus games.
- **Subject:** slotBgNormal and slotBgSpecial are the left half of a board: near-black panels with a faint chevron weave inside a thin gold frame with a small scroll at mid-height; the special one adds the horizontal divisions of nine cells. tileLockBg is an orange Art Deco fan pattern, tile17 a small red faceted triangle, line and lineEnd the gold pieces of a win line, tileLockEffect a horizontal bar of fire in 29 frames; tileGuide and tileGuide2 are flat green layout guides and glowSquare a soft white square.
- **Style:** Restrained Art Deco: thin bevelled gold lines on black, one scroll as ornament. It is the quietest piece of the game.
- **Rendering:** Dark and hard-edged (brightness 0.239; slotBgNormal is 88% #1d1010). The gold line is a smooth gradient with a red inner edge.
- **Colour:** Near-black brown #1e1010, gold #f4cd49 and #c67824, orange #f37b15 for the lock bar. The pure green #28fe0a in the measured palette is the two layout guides, not art.
- **Lighting:** The gold frame carries a top-left highlight; the lock bar and the red triangle are self-lit.
- **Ambience:** A dark stage for bright symbols: everything on it reads at once.
- **Materials:** Polished gold, black woven lacquer or leather (inference from the chevron weave), fire.
- **Variants:** Normal board (three undivided reels) and special board (nine cells) for the Hold & Win games. In the bonus an empty cell shows the red triangle and a held reel is edged by the fire bars.
- **Motion:** The board is still; SlotFrame has an idle of 1.67 s that runs glints along the frame (whiteGlow and blinkRealistic parts in its skin). tileLockEffect is a 29-frame fire bar; three of its frames were seen on the sheet. Reel effects (ReelEffectNormal 0.67 s, ReelAnticipationBack 1.07 s) use the soft square.
- **Construction:** Half a board, 589x715, mirrored to make the whole; a win line is a 16x25 tile stretched with an end cap. Guides ship with the art.
- **Notes:** A mirrored half and a stretched line tile are the cheap parts; the fire bar sequence is the expensive one.
- **Measured:** dark, saturated, warm, medium contrast, hard-edged · brightness 24% · saturation 56% · contrast 47% · warm 90% / cool 3% · brighter towards: top-left (2)
- **Palette (measured):** #1e1010 black 71%, #f37b15 orange 10%, #28fe0a green 7%, #ffffff light gold 3%, #f4cd49 gold 3%, #bd7323 orange 2%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Paytable pictures of every symbol

`help-symbol-pictures` · atlas · 17 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The symbol pictures the shell's help panel shows beside the pays.
- **Subject:** Seventeen 225x225 pictures: each symbol as it appears in a cell (three cherries, three lemons and so on, the WILD word, the coins and collectors) and the small red triangle.
- **Style:** The game's symbols, composed.
- **Rendering:** As the symbols: glossy and vivid (saturation 0.785).
- **Colour:** Orange #f6ad23 (27%), reds #d9390c and #a1130a, green #31550b.
- **Lighting:** As the symbols: top light, warm rim.
- **Ambience:** A catalogue.
- **Materials:** As the symbols.
- **Variants:** One per symbol id, tile1 to tile17.
- **Motion:** None: stills.
- **Construction:** WebP files served by the provider's shared asset service. They show how the game composes the three-fruit clusters from the single fruit parts.
- **Notes:** The quickest reference for what a finished cell looks like.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 50% · saturation 78% · contrast 74% · warm 79% / cool 15% · brighter towards: top (3)
- **Palette (measured):** #f6ad23 orange 27%, #d9390c red 10%, #97520f brown 6%, #641905 dark red 6%, #19130d black 5%, #a1130a red 5%

### Feature symbols: coins, jackpot coins and collector trains

`symbols-coins` · atlas · 98 parts · largest 306×320 · sheet `sheets/symbols-coins.webp`

- **Role:** What drives the Hold & Win games: cash coins, the four jackpot coins and the two collector trains.
- **Subject:** Gold coins with a flame emblem: a plain one and one embossed (cash), and four with a coloured centre and coloured flame for MINI (purple), MINOR (blue), MAJOR (green) and GRAND (red); a red ring of fire (the Jackpot Collector's disc); a small copy of the locomotive; the words CASH, COLLECTOR, JACKPOT, MINI, MINOR, MAJOR and GRAND; a white coin edge for spinning; and highlight sequences.
- **Style:** Glossy casino tokens with fat Western lettering; the jackpot words are tilted across the coin on the screens.
- **Rendering:** Smooth gold gradients with a brushed streak, hard edges on the coins (soft edge 0.02 each) and soft glows in the highlights.
- **Colour:** Coin gold #f9b81f to #f8ba21 with rim brown #7c3007. Centres: MINI #800e9e and #c124f3, MINOR #08b3f4 and #0c8ba9, MAJOR #30ab0a, GRAND #b81005; the collector disc is fire #f34003 and #fc9403.
- **Lighting:** A diagonal sheen across each coin from the top; the fire disc is self-lit.
- **Ambience:** Tokens to collect: colour says the prize before the word is read.
- **Materials:** Gold, coloured enamel, fire.
- **Variants:** Six coin faces, two collectors (Cash Collector on gold, Jackpot Collector on the fire ring) made from the same small train, and the value shown in the purple-and-gold numerals.
- **Motion:** coinHighlight is a 28-frame ring of fire closing round a coin; the three coin and collector highlights are 18-frame white sweeps (three frames of each seen). TileCash: onLand 0.42 s, loop 2 s, collect 0.5 s; TileCollector: onLand 0.42 s, loop 1 s, win 0.5 s. On the screens a landing coin flashes yellow.
- **Construction:** Coin faces about 287x295, words as separate pictures laid over them, one 278x331 train, and four frame sequences.
- **Notes:** Six coins from one gold blank and a centre colour; the words are separate, so a coin can be relabelled.
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 59% · saturation 73% · contrast 58% · warm 80% / cool 12% · brighter towards: top (8), top-right (1)
- **Palette (measured):** #f88e1b orange 35%, #fac92c gold 13%, #fffded light gold 12%, #77250a dark red 7%, #dc280a red 5%, #211a46 dark blue 4%

### Low symbols: cherry, lemon, orange, watermelon

`symbols-fruit` · atlas · 16 parts · largest 193×229 · sheet `sheets/symbols-fruit.webp`

- **Role:** The four low-paying symbols, each built as a cluster of three fruits.
- **Subject:** A single cherry on a stem with a leaf, a lemon, an orange and a striped watermelon, each with a second, darker copy (L or Left) and white silhouettes named Outline.
- **Style:** Classic fruit-machine subjects painted as glossy, slightly stylised still life.
- **Rendering:** Smooth airbrushed volumes with pinpoint highlights and a thin warm rim; hard outer edge (soft edge 0.102).
- **Colour:** Cherry red #cd0e0d, lemon #e4a806, orange #f68005, watermelon greens #2b5307 and #5a8010; leaves #385a04 to #85ad12. Every fruit has an orange-red rim (#e43b04 measured on the watermelon). The 23% near-white in the unit's palette is the outline masks.
- **Lighting:** Lit from the upper left, with a warm red-orange rim on the lower right as if from the fire.
- **Ambience:** Juicy and familiar; the rim light ties them to the fire field.
- **Materials:** Fruit skin, leaf.
- **Variants:** Per fruit: a front copy, a side copy shaded darker for depth, and outline masks for each. On the reels each symbol shows three fruits, the side ones behind the front one.
- **Motion:** No frame sequence of their own. TileContainer has a win of 0.58 s; the outline masks are there to flash or glow the silhouette (inference from their names and shape).
- **Construction:** One fruit picture reused three times per symbol (front plus darker side copies), about 135 to 193 px wide, with white masks.
- **Notes:** Three-of-a-kind in a cell from one painted fruit: cheap, and it makes a 3x3 board look full.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 54% · saturation 72% · contrast 48% · warm 49% / cool 14% · brighter towards: top-left (3), left (2), bottom-left (2)
- **Palette (measured):** #fffffe light gold 23%, #3f6608 dark green 12%, #d93a06 red 12%, #192903 black 12%, #ec9307 orange 11%, #a02e05 brown 7%

### High symbols: horseshoe, star, bell, seven

`symbols-premium` · atlas · 77 parts · largest 277×270 · sheet `sheets/symbols-premium.webp`

- **Role:** The four higher-paying symbols with their win highlights.
- **Subject:** A silver horseshoe, a faceted blue star, a copper bell and a red seven with a flame painted inside it and a gold edge; each with darker side copies (the seven has left and right ones) and a 17-frame highlight in which a line of fire traces the symbol's outline.
- **Style:** The same glossy still life as the fruit, with harder, more metallic surfaces.
- **Rendering:** Polished metal gradients with sharp speculars; the star is cut in flat facets. Strong highlights measured, contrast 0.703.
- **Colour:** Horseshoe steel #7b9095 and #eff7f9 (saturation 0.225, the one grey thing in the game); star blues #043266, #165fab and #9ac8f5; bell copper #bd3b07 and #f08638; seven reds #e03d0f and #be0908 with cream #fcf0a4. All carry the orange rim.
- **Lighting:** Upper-left key light and the warm rim; the outline fire is self-lit.
- **Ambience:** Lucky charms polished for a jackpot hall.
- **Materials:** Steel, cut glass or enamel (the star), copper, lacquer and gold (the seven).
- **Variants:** Front and side copies as for the fruit; one highlight sequence per symbol.
- **Motion:** tile5 to tile8 Highlight, 17 frames each: a flame runs round the outline and dies out (three frames of each seen on the sheet). On the screens winning symbols also pulse.
- **Construction:** Still pictures 170 to 277 px, plus four 17-frame sequences of thin fire lines up to 162 px.
- **Notes:** An outline traced in fire is a win effect that needs no change to the symbol itself.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 50% · saturation 67% · contrast 70% · warm 85% / cool 15% · brighter towards: top-left (3), top (2), bottom-left (1)
- **Palette (measured):** #f55721 orange 30%, #faab68 orange 14%, #fcf0ce light orange 13%, #11080c black 7%, #680e04 dark red 5%, #b11b09 red 5%

### Wild: the word WILD in fire

`symbol-wild` · atlas · 4 parts · largest 149×130 · sheet `sheets/symbol-wild.webp`

- **Role:** The wild symbol.
- **Subject:** Four separate letters W, I, L, D in a Western slab serif, filled with a flame texture inside a dark red bevel.
- **Style:** Saloon-poster lettering turned into burning metal.
- **Rendering:** Very saturated (0.951); a mottled fire fill with a bright core and a dark extruded edge.
- **Colour:** Orange #f99e08 (35%), #dd4605, dark red #861802, gold #fed926.
- **Lighting:** The letters glow from inside; the bevel takes a top-left light.
- **Ambience:** Hot and loud: the brightest thing on the reels.
- **Materials:** Fire held in a red metal frame.
- **Variants:** One design. On the reels it stacks: a reel of three WILD words was seen.
- **Motion:** TileWild: onLand 0.33 s, loop 1 s, win 0.58 s. Shipping the letters apart lets each move by itself (inference; the letters were not seen moving apart on the screens).
- **Construction:** Four letter pictures 130 px high on a 10-bone rig.
- **Notes:** A word as a symbol, split into letters for animation.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 49% · saturation 95% · contrast 72% · warm 100% / cool 0% · brighter towards: top-left (1)
- **Palette (measured):** #f99e08 orange 35%, #dd4605 orange 26%, #861802 dark red 20%, #fed926 gold 11%, #3e0301 dark red 2%, #b85725 orange 2%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The locomotive: mascot, collector and scene

`train` · atlas · 35 parts · largest 694×709 · sheet `sheets/train.webp`

- **Role:** The game's one figure: the steam locomotive above the reels, on the intro, and in the transition into the bonus games.
- **Subject:** A three-quarter front view of a steam locomotive: gold boiler front with a flame emblem on a riveted round door, two lit lamps, gold cowcatcher, deep purple boiler and cab, a tender behind. With it: three piles of gold coins, a wheel shown blurred by speed in two frames, connecting-rod pieces, a white highlight pass in 19 frames and spark bursts in 8.
- **Style:** Glossy 3D-look illustration, rendered or painted to look rendered (inference): clean forms, exaggerated shine, toy-like proportions with an oversized boiler front.
- **Rendering:** Smooth gradients, crisp edges, strong white highlights on the gold (contrast 0.69, strong highlights measured). The purple is nearly black in shadow.
- **Colour:** Gold #e2a329 and #f3ce7c, browns #693d10 and #b07419 in the gold's shadow, near-black #190f10; the purple boiler is too dark to enter the measured palette.
- **Lighting:** Lit from the upper front; the two lamps and the emblem glow on their own. On the screens steam behind it is white against the red field.
- **Ambience:** Wealth on rails: heavy, polished, about to move. It is the only object with weight in the scene.
- **Materials:** Polished gold, lacquered purple steel, glass lamps, gold coins.
- **Variants:** One picture (694x709) used at several sizes: large on the intro, medium above the reels, enlarged and glowing as it crosses the reels into the bonus. The same train, smaller, is the collector symbol (see the coin symbols).
- **Motion:** SceneCollector (64 bones, 78 slots) holds it: activate 0.67 s, a loop of the train of 1.42 s, collect 0.33 s, upgrade 0.58 s. On the screens the coin pile grows and glows when a coin lands, and the train drives over the reels at the bonus transition. The wheel is two blurred frames and the rods are separate parts, so the running gear is animated by parts while the body is one picture (inference from the part list).
- **Construction:** One body picture with separate wheel-blur, rod, coin-pile, highlight and spark parts on a 4.2.43 Spine rig. No skeleton frame is shown here: the renderer of this project is written for Spine 3.7.
- **Notes:** A single hero render carried by highlights and sparks is enough for a mascot that never turns. The body is not cut into parts.
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 55% · saturation 59% · contrast 69% · warm 80% / cool 7% · brighter towards: top-right (1), top-left (1)
- **Palette (measured):** #f0af2a orange 19%, #f3f1eb light orange 17%, #6b3f0f brown 16%, #b37417 orange 16%, #190f10 black 13%, #fbdea0 light orange 5%


## Logo and title

The game's own wordmark.

### Help logo: the full ticket with HOLD & WIN

`help-logo` · atlas · 1 parts · largest 394×137 · sheet `sheets/help-logo.webp`

- **Role:** The logo at the top of the shell's help panel.
- **Subject:** The gold ticket with FIRE RAIL EXPRESS, a black HOLD & WIN tab under it and the gold locomotive embossed on the right half.
- **Style:** The same poster lettering and foil ticket as the in-game logo.
- **Rendering:** Hard-edged (soft edge 0.094), high contrast 0.955.
- **Colour:** Gold #f7dc4b (32%), black #0a0302 (26%), brown #96721f, light gold #f8f59c.
- **Lighting:** Foil sheen; light measured at the right, where the embossed train is.
- **Ambience:** A printed ticket.
- **Materials:** Gold foil card, black ink.
- **Variants:** The only place the sub-title HOLD & WIN appears as art; in the game the logo has no sub-title.
- **Motion:** None: a still in the help panel.
- **Construction:** One 394x137 WebP served by the provider's shared asset service, not from the game's atlas.
- **Notes:** A ready composition of logo and stub: a good reference for how the two in-game parts sit together.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 52% · saturation 70% · contrast 96% · warm 100% / cool 0% · brighter towards: right (1)
- **Palette (measured):** #f7dc4b gold 32%, #0a0302 black 26%, #96721f brown 15%, #ceae35 gold 11%, #f8f59c light gold 6%, #423514 brown 3%

### Logo: FIRE RAIL EXPRESS on a gold ticket

`logo` · atlas · 21 parts · largest 753×264 · sheet `sheets/logo.webp`

- **Role:** The game's wordmark as it sits at the top left of the reels and on the intro.
- **Subject:** A gold train ticket with perforated ends, FIRE RAIL EXPRESS in black slab-serif capitals with a yellow outline and small flames along the top edge; a second part (defaultBack) is the ticket's stub with the locomotive embossed in gold. Also a motion-blurred copy and an 18-frame highlight.
- **Style:** Wild West poster lettering on a printed ticket: flat, graphic, with a metallic sheen.
- **Rendering:** High contrast (0.825) with strong highlights: black letters on gold #f7dc4d, the gold banded light and dark like foil.
- **Colour:** Gold #f7dc4d (28%), #d1aa2e and #f7f095, black #0a0402, brown #8b5b12. Hues are yellow 65% and orange 35%: no other colour.
- **Lighting:** A foil sheen from the upper right; the highlight frames sweep a white glint across the letters.
- **Ambience:** A ticket to ride: the logo is an object from the theme, not a floating title.
- **Materials:** Gold foil card, black ink.
- **Variants:** Sharp and blurred copies (the blur for its entry), and the stub with the embossed train behind it. The help panel uses a fuller version with HOLD & WIN (the help logo).
- **Motion:** Logo skeleton: show 0.43 s, idle 0.75 s, hide 0.33 s, with "Gs" twins for another state (which state is not known from the files). logoHighlight is an 18-frame glint; three frames seen on the sheet.
- **Construction:** A 753x264 picture, a 280x208 stub, a blurred copy and a frame sequence, on a 10-bone rig.
- **Notes:** Only two hues, so it stays readable over fire or purple.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 57% · saturation 66% · contrast 82% · warm 97% / cool 0% · brighter towards: top-right (2), top (1)
- **Palette (measured):** #f7dc4d gold 28%, #0a0402 black 17%, #d1aa2e gold 16%, #8b5b12 brown 15%, #f7f095 light gold 7%, #fdf9dc light gold 6%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Bonus Game splashes

`feature-splashes` · atlas · 7 parts · largest 1114×357 · sheet `sheets/feature-splashes.webp`

- **Role:** The screens that announce the two Hold & Win games.
- **Subject:** A torn purple postcard with a faint map and locomotive drawing, an orange card with a gold frame (half of it), and four lettering pictures: BONUS GAME in purple and in orange-red, CASH TRAINS COLLECT CASH PRIZES and JACKPOT TRAINS COLLECT JACKPOT PRIZES in cream with a red edge.
- **Style:** Postcard as a stage, poster capitals on top.
- **Rendering:** Mid-tone and vivid (saturation 0.747), medium contrast; the card is textured, the lettering flat and outlined.
- **Colour:** Purple card #5c1c75 and #8c51a2; orange card #ef840e and #ba450b; cream lettering #fbdb9d.
- **Lighting:** A sunburst of rays behind the title on the screens; the cards are evenly lit.
- **Ambience:** An announcement pinned over the game: the reels stay visible underneath.
- **Materials:** Worn card, printed ink.
- **Variants:** Two versions: purple for the cash game, orange for the jackpot game, each with its own two lettering files.
- **Motion:** FreeSpinsSplash and FreeSpinsSplashSpecial1: show 1 s, hide 0.5 s. Both seen in play, each waiting for the shell's START button.
- **Construction:** A 558x639 card and half a 563x684 card, a 50 px black square for the dimming, and four localised lettering files 1114 px wide (en-GB).
- **Notes:** The lettering is the only localised art in the game: four splash files and TOTAL WIN.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 44% · saturation 75% · contrast 52% · warm 60% / cool 38% · brighter towards: bottom-left (2)
- **Palette (measured):** #581c70 dark purple 31%, #ef840e orange 26%, #fbdb9d light orange 12%, #bb3e10 orange 8%, #8d529f purple 6%, #2c0b3b dark purple 3%

### Win tiers: BIG WIN, SUPER WIN, MEGA WIN, TOTAL WIN

`win-tiers` · atlas · 14 parts · largest 1114×555 · sheet `sheets/win-tiers.webp`

- **Role:** The banners for large wins and for a bonus game's total.
- **Subject:** Three two-line titles in fat Western capitals with a gold outline: BIG WIN (purple fill), SUPER WIN (blue), MEGA WIN (red); TOTAL WIN in purple; a gold spoked train wheel with a white rim mask; a gold frame; three chevron-patterned panels in purple, blue and red; a fan of gold rays; white ray and shine bursts.
- **Style:** Circus and saloon poster type with a train wheel as the turning ornament.
- **Rendering:** Dark fills with bright double outlines (gold, then a coloured glow); high contrast with strong highlights.
- **Colour:** BIG #350e4f and #651985, SUPER #1f104e and #22267e, MEGA #320d37 with red #700c10; outlines gold #f1bf3b and #f1ee8a. Panels: #34083a, #072258, #6b0808. Wheel gold #edb526.
- **Lighting:** Letters carry a top highlight; rays and shines are white and meant to be tinted or added as light (inference).
- **Ambience:** A show poster: each tier is the same layout in a hotter colour.
- **Materials:** Enamelled sign letters, gold.
- **Variants:** Three tiers by colour (purple, blue, red), each with its own panel; TOTAL WIN for the bonus end.
- **Motion:** WinBig: labelShow 0.92 s, sumShow 0.42 s, hide 0.5 s; WinBigEffects loops 3 s; WinTotal show 0.92 s. Not seen in play: no win reached a tier and no bonus was played to its total.
- **Construction:** Title pictures up to 772x451 (TOTAL WIN 1114x555 as a localised file), a 557x560 wheel, half a frame, three 331x278 panels and white light parts.
- **Notes:** One layout recoloured three times. Read from the sheet only.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 41% · saturation 70% · contrast 64% · warm 46% / cool 39% · brighter towards: top-right (3)
- **Palette (measured):** #290e43 dark purple 35%, #f0b92f orange 15%, #fffefe light gold 9%, #f1ed86 gold 8%, #700a0a dark red 8%, #561d7c dark purple 6%

### Jackpot win: the plaque enlarged

`jackpot-win` · atlas · 5 parts · largest 498×472 · sheet `sheets/jackpot-win.webp`

- **Role:** What shows when a jackpot is collected.
- **Subject:** A large copy of the jackpot plaque frame (a rounded panel with one cut corner, gold and red rim, dark chevron inside) and large MINI, MINOR, MAJOR and GRAND words.
- **Style:** The jackpot panel's own design at celebration size.
- **Rendering:** Hard-edged (0.054), high contrast 0.805.
- **Colour:** Frame black #1e1714 with gold #f0bd39; words in red #c61a1c, blue #046ccd, green #1f810d and purple #9054cd.
- **Lighting:** Top light on the letters. On the screen the frame fills with fire and a violet glow sits behind it.
- **Ambience:** The prize named in its own colour, as big as the screen allows.
- **Materials:** Gold, enamel letters.
- **Variants:** Four words, one frame.
- **Motion:** WinJackpot: show 0.92 s, hide 0.5 s. Seen once in play (MINI): the plaque with fire inside, the amount 15 below, coins and tickets flying.
- **Construction:** A 498x472 frame and four word pictures up to 885x238.
- **Notes:** It reuses the panel art, so a jackpot win is recognised from the panel the player has been watching.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 40% · saturation 68% · contrast 80% · warm 63% / cool 30% · brighter towards: top (5)
- **Palette (measured):** #1e1714 black 23%, #f0bd39 orange 17%, #efea93 light gold 9%, #c61a1c red 7%, #046ccd blue 6%, #083279 dark blue 6%


## Effects

Frame sequences, glows, particles and transitions.

### Flying coins and tickets

`coins-and-tickets` · atlas · 71 parts · largest 156×156 · sheet `sheets/coins-and-tickets.webp`

- **Role:** The particles of a win.
- **Subject:** A gold flame coin turning through 32 frames and a gold ticket tumbling through 39.
- **Style:** The same gold as the symbols, simplified for small size.
- **Rendering:** Bright and hard-edged (brightness 0.681, saturation 0.897).
- **Colour:** Gold #f5c606 (45%), orange #e18a05 (33%), light gold #fceba8: two hues only.
- **Lighting:** A highlight that moves with the turn.
- **Ambience:** Money and tickets in the air: the theme's confetti.
- **Materials:** Gold.
- **Variants:** One coin, one ticket.
- **Motion:** Full turn cycles (ParticleCoin loop 1 s, ParticleTicket loop 1.3 s). On the screens coins shower at the bonus start and at the jackpot win, and tickets fly off a counting win.
- **Construction:** 71 frames up to 156 px.
- **Notes:** The ticket as a particle repeats the logo's shape.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged · brightness 68% · saturation 90% · contrast 45% · warm 100% / cool 0% · brighter towards: top-right (11), top (9), right (6)
- **Palette (measured):** #f5c606 gold 45%, #e18a05 orange 33%, #fceba8 light gold 9%, #e4b758 orange 5%, #cf4b02 orange 4%, #b10601 red 3%

### Fire effects

`fire` · atlas · 85 parts · largest 282×500 · sheet `sheets/fire.webp`

- **Role:** The game's fire: transition flames, rings, sparks and the flames inside frames.
- **Subject:** Five frame sequences: fireTransition (16 frames of a rising flame, 282x500), fireCircle (13, a ring of fire about 190 px), fireSparkle (19, a small fireball with a tail, 201x31), flamesFill and flamesLighting (18 each, a white flame shape and its inner detail, 310x150), and a single fire particle.
- **Style:** Cartoon fire: flat tongues in three tones with a soft glow, not photographic flame.
- **Rendering:** Bright and soft (brightness 0.782, soft edge 0.613). The two flames sequences are white, made to be coloured in the game.
- **Colour:** White #fffffe (43%, the white flame masks), orange #fd6903, light yellow #fef782, red #fe1200.
- **Lighting:** Self-lit.
- **Ambience:** Heat as decoration: fire outlines, fills and announces things all through the game.
- **Materials:** Flame.
- **Variants:** One ring, one flying spark, one rising flame, one flame bed in two layers.
- **Motion:** Hand-drawn frame animation, 13 to 19 frames each (three frames of each seen on the sheet). JackpotEffects loops the flame bed in 0.57 s; SlotTransition shows in 2 s. On the screens flame shapes sweep the screen after START and fire burns inside the active jackpot frame.
- **Construction:** 85 small frames; the flame bed is shipped as white fill and white detail so one sequence can burn in any colour.
- **Notes:** A white fire that is tinted in the game is worth copying: one sequence, many colours.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 78% · saturation 47% · contrast 30% · warm 58% / cool 0% · brighter towards: left (12), top-right (2), top-left (2)
- **Palette (measured):** #fffffe light gold 43%, #fd6903 orange 27%, #fef782 light gold 15%, #fe1200 red 8%, #fdbf4d orange 4%, #fca91a orange 2%

### Light, glints and smoke

`light-and-smoke` · atlas · 19 parts · largest 582×578 · sheet `sheets/light-and-smoke.webp`

- **Role:** The shared light shapes and the steam.
- **Subject:** White halos and rings, a soft glow, a four-point glint, a light cone, two puffs of smoke, speck fields, small orange and yellow light dots, tiny particle dots, white squares for flashes and a noise texture.
- **Style:** Stock effect shapes; the smoke is soft and painterly.
- **Rendering:** Almost all white and soft (brightness 0.885, saturation 0.017, soft edge 0.887).
- **Colour:** White #fcfaf9 (85%); the only colour is the two small light dots.
- **Lighting:** They are the light.
- **Ambience:** Steam and sparkle around metal.
- **Materials:** Light, steam.
- **Variants:** One of each.
- **Motion:** Moved, scaled and faded by the skeletons that use them: whiteGlow alone is in 17 of the 41. The steam cloud behind the train on the screens is built from the smoke puffs (inference).
- **Construction:** 19 white textures from 10 px to 582 px, tinted and blended in the game.
- **Notes:** A small white kit used everywhere.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 88% · saturation 2% · contrast 9% · warm 31% / cool 0%
- **Palette (measured):** #fcfaf9 light orange 85%, #0f0f0f black 7%, #dad6d0 light orange 3%, #434343 grey 2%, #717171 grey 2%


## Game interface

Buttons, counters and panels drawn for this game.

### Buy Feature cards

`buy-feature-cards` · atlas · 2 parts · largest 575×225 · sheet `sheets/buy-feature-cards.webp`

- **Role:** The two pictures on the shell's Buy Feature panel.
- **Subject:** Hold & Win: the locomotive and multiplier coins (10x, 8x, 7x) over purple cards and fire. Jackpot Hold & Win: the Jackpot Collector among the four jackpot plaques on fire.
- **Style:** Key-art collages of the game's own parts.
- **Rendering:** Vivid and busy (saturation 0.73); opaque pictures.
- **Colour:** Orange #ed942e (35%), #db4511, dark magenta #672066.
- **Lighting:** Fire glow from below.
- **Ambience:** An advertisement for each feature.
- **Materials:** As the game's art.
- **Variants:** Two cards; a third 2X card on the panel is the provider's shared picture.
- **Motion:** None: stills.
- **Construction:** Two 575x225 WebP files from the provider's shared asset service.
- **Notes:** They show the intended composition of each feature in one picture.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 49% · saturation 73% · contrast 68% · warm 91% / cool 4% · brighter towards: bottom (1)
- **Palette (measured):** #ed942e orange 35%, #db4511 orange 10%, #b36a26 orange 10%, #672066 dark magenta 8%, #924a51 red 8%, #f1c96a orange 7%

### Spin counter of the bonus games

`spin-counter` · atlas · 4 parts · largest 270×130 · sheet `sheets/spin-counter.webp`

- **Role:** The 1 2 3 counter above the reels in Hold & Win.
- **Subject:** A small gold plate with two rivets and a dark red window, and the digits 1, 2 and 3 in cream.
- **Style:** A locomotive's number plate.
- **Rendering:** Hard-edged, high contrast 0.852.
- **Colour:** Dark red #38111c, gold #efb328, cream #fef9d6.
- **Lighting:** Top light on the plate.
- **Ambience:** Machine hardware.
- **Materials:** Riveted gold plate.
- **Variants:** Three digits lit or removed as spins are used (seen as 1 2 3, then 1 2).
- **Motion:** SpinCounter: activate 0.42 s, loop 0.83 s; SpinCounterPositions show 0.45 s.
- **Construction:** A 270x130 plate and three digit pictures 56 px high.
- **Notes:** Small, and in the theme.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 46% · saturation 72% · contrast 85% · warm 92% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #38111c dark red 35%, #efb328 orange 20%, #8e2c0a brown 11%, #fef9d6 light gold 9%, #c87e14 orange 9%, #fefa3f gold 5%

### Jackpot panel: four plaques

`jackpot-panel` · atlas · 45 parts · largest 243×229 · sheet `sheets/jackpot-panel.webp`

- **Role:** The GRAND, MAJOR, MINOR and MINI plaques above the reels.
- **Subject:** A rounded dark panel with one cut corner in a gold rim, an active version with a red and gold rim, the four words in fat Western capitals each in its own colour, a thin gradient line, an 18-frame corner glint and a 20-frame burst of flame.
- **Style:** Art Deco plaque with saloon lettering.
- **Rendering:** Mid-tone and vivid; hard frames, soft effects (soft edge 0.269 over the unit).
- **Colour:** Frame #1e1313 with gold #f3b62d; active rim #ea3b0e and #fbdb3f; words red (GRAND), green (MAJOR), blue (MINOR), purple (MINI).
- **Lighting:** Top light on the rim and the letters.
- **Ambience:** A scoreboard that heats up: fire is what marks a plaque as live.
- **Materials:** Gold, enamel, fire.
- **Variants:** Idle and active frame; two sizes on the screens (GRAND and MAJOR larger than MINOR and MINI). The values 500x, 100x, 30x and 15x are the numeral font.
- **Motion:** Jackpot: idle 0.83 s, activate 0.33 s, activeLoop 0.67 s, collect 0.5 s, upgrade 0.58 s. jackptCollectEffect is 20 frames of flame, jackpotFrameHighlight 18 frames of a glint (three frames of each seen).
- **Construction:** One 243x229 frame (and its active twin) reused for all four, words as separate pictures.
- **Notes:** One frame, four words, four colours.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 44% · saturation 73% · contrast 55% · warm 82% / cool 12% · brighter towards: top (4), top-right (1)
- **Palette (measured):** #fc7c04 orange 34%, #1f1613 black 23%, #f1be3b orange 8%, #821213 dark red 6%, #fefcf6 light orange 5%, #0b4381 dark blue 2%


## Typography

Embedded fonts and lettering.

### Numerals: purple with a gold rim

`UltraPurpleGold` · atlas · 14 parts · largest 210×229 · sheet `sheets/UltraPurpleGold.webp`

- **Role:** The bitmap font for jackpot values, coin values and win amounts.
- **Subject:** Digits 0 to 9, x, +, comma and full stop in a fat Western face with curled terminals.
- **Style:** Saloon numerals, glossy.
- **Rendering:** Hard-edged (0.025), high contrast 0.834: a two-tone purple fill split by a horizontal shine, a gold rim, a dark red drop edge.
- **Colour:** Purple #600753 and #932589, gold #efbe3f and #f7ed8b, dark red #600d0c.
- **Lighting:** Top light on the rim; a band of shine across the middle.
- **Ambience:** Rich and loud; it is the counter-colour to all the gold.
- **Materials:** Enamel in a gold rim.
- **Variants:** One style. It comes from the provider's shared font store (fonts-v2), so other games may use it (inference).
- **Motion:** None of its own; on the screens the amounts count up.
- **Construction:** 14 glyphs about 229 px high on one WebP with a JSON of positions.
- **Notes:** Purple numerals on a gold game: amounts never get lost among the coins.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 42% · saturation 76% · contrast 83% · warm 81% / cool 0% · brighter towards: top (13), top-left (1)
- **Palette (measured):** #600753 dark magenta 22%, #efbe3f orange 17%, #932589 magenta 16%, #f7ed8b light gold 14%, #600d0c dark red 13%, #b0451e orange 8%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 578 components cut from 36 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
