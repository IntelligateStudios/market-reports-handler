# Super Cash Boost Big Bad Bonus: art report

octoplay · run `2026-11-26-2343-octoplay-super-cash-boost-big-bad-bonus` · captured 2026-11-26

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/super-cash-boost-big-bad-bonus

**Extracted:** 518 named components from 37 textures in 37 atlases; 41 Spine skeletons; 20 frame sequences (283 frames); 3 fonts. Grouped into 24 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

The Three Little Pigs told through building materials: straw, wood and brick are at once the three Wild pigs, the three houses, the three prize ladders and the three win tiers, in a painted storybook valley with the wolf kept back for the bonus.

**Style.** Storybook cartoon in two registers: painted animation-background landscapes and feature-film style characters (the wolf, three pigs), against inflated glossy letters and toy tools with a pig's snout worked into each. Interface plates are the materials themselves, a straw bale, a plank, a brick panel.

**Rendering.** Backgrounds and props are painterly with visible brushwork; characters are smoothly blended with sharp speculars and a light rim; letters, tools, logo and numerals are flat gradients with gloss bands and thick dark outlines. Effects are flat white hand-drawn smoke, dust and wind, with soft white glows added on top.

**Colour.** Measured over the game's art: dark forest greens #192f29 19% and #375d56 10%, near-white #eef2f0 9% (smoke, numerals), brick brown #8d3d17 6%, warm yellow #f3d07a 6%, sky blues #6498bd 6% and #a7cfe1 4%, straw #efdaae 2%. The scene is green and blue, the interface warm brown, tan and gold, and the symbols take one saturated hue each. Jackpots are coded by colour: MINI magenta, MINOR blue, MAJOR green, MEGA red-orange, GRAND gold. Frame metal ranks the pigs: steel, copper, gold.

**Lighting.** Daylight from the upper right in the base scene and a low sunset behind the hills in the special scene; props and plates are lit from the upper left; characters have a warm key and a thin cool rim. Nothing glows by itself except a plate being boosted.

**Ambience.** Sunny, rustic and good-humoured. The base game is a building site in a meadow at midday; the intro shows the finished village at sunset with the wolf waiting. Threat is played as comedy.

**Shape language.** Round and soft everywhere: balloon letters, fat tools, plump pigs, puffed clouds and bushes. The pig's snout (an oval with two dots) is the repeated mark, on every letter, the tape measure, the hard hat, the toolbox, the coin and the reel panel's watermark. Square frames are kept for the Wilds and houses only.

**Materials.** Straw, rough timber, fired brick, glossy enamel and plastic, gold coin, denim, fur, skin; flat white smoke and dust.

**Typography and lettering.** Two voices. Drawn balloon capitals with uneven baselines for the logo, the jackpot names and the win tiers, each word in its own colour; a fat rounded numeral face from the provider's shared font store in white (MarvinRound, on the ladders) and gold (MarvinRoundYellow, for jackpots and wins). HOLD & WIN and its rule line use the rounded face. The help, buttons and balance line are the shell's Poppins.

**Motion.** All motion is Spine: 41 skeletons in one bundle file (38 in 4.2.43; BonusSpinsSplash, ForegroundEffects and Foregrounds in 4.1.24) moving still pictures and cut-up characters, with 20 hand-drawn frame sequences (283 frames: the piggy coin's turn, plate bursts and sweeps in three materials, dust, wind, the wolf's breath, air rings and swirls on the tools, a frame glint, butterflies). Seen in play: the logo's words dropping in, the Boost sign growing across bleached reels and its word flying to a plate that flares and rises, a reel flashing pink under a landing Wild, winning symbols growing with a gold line, an air ring round the tape measure, a BIG WIN presented by the Straw Farmer pig. Not seen: the bonus, in which by the files the wolf inhales and blows (3.23 s) and the houses burst open. No skeleton frame is shown in this report, because the project's renderer cannot draw Spine 4; assembled and motion pictures are absent for that reason only.

**Variants and themes.** Two scenes on one composition (day building site, sunset village). Three pigs on one portrait layout and, by their parts, one rig. Three houses, each whole and destroyed. Three prize plates and three plate effects on one timing. Five jackpot names and five sets of coloured brick strips. Three win tiers and a total on one lettering. One numeral face in two colourings.

**How it is built.** Two 4096 px atlas pages hold 453 sprites, each page carrying one 2750 px scene; four lettering files are localised (en-GB). Characters and houses are cut into parts for Spine (the wolf 43 sprites with breath, the pigs 32, the houses 33). The reel backing and its pig watermark are grey and tinted by the engine. The flat symbol pictures, the flat logo, the numeral fonts, the Extra Chance card, the controls and Poppins come from the provider's shared store, outside the game bundle.

**Consistency.** Very consistent: one idea (three materials in rising strength) orders the Wilds, houses, ladders, win tiers and effects, and one mark (the snout) themes every filler symbol. The joins that show are between the painted characters and the flat glossy letters, which are two different finishes on the same reel, and the plain gold reel frame, which belongs to neither. Shared with the other Octoplay runs (Fire Rail Express, 777 Hot Reels): the shell, Poppins, the Extra Chance card `buyChances2x` (the same file) and three light sprites (circularWhiteRays2, glowSquare, whiteGlow, pixel for pixel); 22 and 24 of the 41 skeleton names also appear in those runs, one scene template (inference). A sprite reading BOILERPLATE is left in the atlas.

**What to take from it.** (1) Pick one ordering idea from the theme and use it for everything that has ranks. Here straw, wood and brick rank the Wilds (x1, x2, x3), the houses, the prize ladders and the win tiers, so the player learns the scale once. (2) Theme the filler symbols with one small mark instead of new drawings: a snout on each letter and tool was enough to make 10 to A belong to the tale. (3) Make interface plates out of the theme's materials. The prize cells are a bale, a plank and a brick panel, each one sprite repeated five times, and they give the screen its character more than the reel frame does. (4) Hold the best character back. The wolf is the largest drawing in the game (740x1374 px body, three heads) and appears only on the intro and in the bonus. (5) Let a character present the win: the BIG WIN reuses the Wild pig's bust and the scene's props (hay bale, board, daisies) rather than a separate celebration set. (6) One effect language keeps a cartoon coherent: every effect here is flat white smoke, dust or wind, drawn by hand in 5 to 27 frames, with generic soft glows for light. (7) For AI art work: the scenes are two paintings on one composition (same path, same framing trees, different hour and state), a clear brief for a day and sunset pair; the three pigs are one portrait layout with costume, prop and frame metal changed, a clear brief for consistent character variants. (8) Cut characters and breakable props into parts from the start: each house exists whole and destroyed in loose pieces so one skeleton can stage the collapse on any cell. (9) Grey art tinted in the engine (the reel backing and watermark) is a cheap way to recolour a board per mode. (10) Draw words separately from what they label and keep them in localised files; the logo's four words and the BOOST word are separate sprites so they can animate and travel.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 51% · saturation 51% · contrast 67% · warm 42% / cool 44% · brighter towards: top-left (65), top (58), top-right (19)

Palette: #192f29 dark cyan 20%, #375d56 dark cyan 10%, #eef2f0 light green 10%, #8d3d17 brown 7%, #f3d07a orange 6%, #6498bd blue 6%, #a7cfe1 light cyan 5%, #efdaae light orange 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 47% | 51% | 76% | 34% / 54% | #19332c dark cyan 26%, #385e54 dark cyan 15%, #f0d183 orange 9% |
| Reel board | 2 | 52% | 43% | 29% | 46% / 4% | #7f7f7f grey 38%, #873e16 brown 18%, #e6b353 orange 14% |
| Symbols | 6 | 48% | 64% | 67% | 70% / 22% | #f8c191 light orange 13%, #32150d dark red 12%, #1b453b dark cyan 12% |
| Characters | 1 | 45% | 31% | 56% | 12% / 78% | #2d3646 dark blue 33%, #4b85a4 blue 24%, #f4f5f4 white 12% |
| Logo and title | 2 | 59% | 65% | 76% | 74% / 25% | #fde623 gold 15%, #fbecc4 light orange 13%, #ed0c04 red 9% |
| Win celebrations and banners | 3 | 46% | 72% | 56% | 70% / 23% | #8d3614 brown 26%, #d2954c orange 12%, #491108 dark red 8% |
| Effects | 5 | 80% | 32% | 27% | 40% / 6% | #fdfdfc light yellow 43%, #f7bb05 gold 19%, #a9a9a8 grey 13% |
| Game interface | 1 | 82% | 41% | 22% | 97% / 0% | #fdf6c1 light gold 55%, #fcfcfa light green 14%, #f6ba09 orange 14% |
| Typography | 2 | 59% | 23% | 83% | 18% / 82% | #e8e1da light orange 52%, #1a1717 black 35%, #f9d94c gold 8% |
| Provider interface (shared) | 1 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backgrounds: the meadow path and the village at sunset

`backgrounds` · atlas · 2 parts · largest 2750×2513 · sheet `sheets/backgrounds.webp`

- **Role:** The two full-screen scenes. bgNormal is behind the base game; bgSpecial is the intro screen and, by its name, the bonus scene (inference until seen in play).
- **Subject:** bgNormal: a dirt path through a flowered meadow into rounded bushes, fir woods and blue mountains under piled white clouds, with the pigs' building site in front: stacks of orange bricks, a sawhorse, a hay bale, crossed planks with nails and a blue trowel. bgSpecial: the same valley at sunset with the three houses built, a straw house with ears and round blue windows at the left, a plank house behind it, a tiled brick house at the right, and a village down the lane.
- **Style:** Storybook landscape painting in the manner of a hand-painted animation background: soft rounded masses, readable brush shapes, no outlines.
- **Rendering:** Painterly, with visible brush marks in foliage and clouds and crisp cut edges on the props; measured hard-edged (soft edge 0.004) and high contrast 0.756.
- **Colour:** Measured over both: dark cyan-green #19332c 26% and #385e54 15% (woods and shade), warm yellow #f0d183 9% (sunset light and path), blues #6899ba 8%, #9ac9df 4% and #3b7f9e 3% (sky and mountains), pale #d4eef4 6% (clouds). Normal is green and blue; Special swaps the sky to yellow, peach and violet.
- **Lighting:** Normal: a high midday sun from the upper right, short cool shadows across the path. Special: low warm light from behind the hills that rims the roofs and clouds, with the foreground trees in shadow as a dark frame.
- **Ambience:** A calm summer valley; the work in progress in the base scene and the finished houses in the special one tell the tale's before and after.
- **Materials:** Grass, leaves, packed earth, clouds, brick, straw, planks, roof tiles.
- **Variants:** Two scenes of 2750x2510 px on one composition: path in the middle, trees framing both top corners, mountains on the horizon.
- **Motion:** Still pictures. The Backgrounds skeleton only places them; BackgroundEffects adds white rays (idle 5 s, loopSpecial 6.67 s) and ParticleButterflyNormal sends small white butterflies across, seen in play as specks over the meadow.
- **Construction:** Each scene is one sprite of about 2750 px, larger than the 1280x720 view, so the same picture serves landscape and portrait (inference from SectorsPosition holding both layouts).
- **Notes:** The scene is where the theme lives: the reels carry only tools and letters, so the tale is told by what stands in the meadow behind them.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 47% · saturation 51% · contrast 76% · warm 34% / cool 54% · brighter towards: top (1), top-right (1)
- **Palette (measured):** #19332c dark cyan 26%, #385e54 dark cyan 15%, #f0d183 orange 9%, #6899ba blue 8%, #d4eef4 light cyan 6%, #9ac9df cyan 4%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board: a thin gold frame on a dark panel

`reel-board` · atlas · 42 parts · largest 529×315 · sheet `sheets/reel-board.webp`

- **Role:** Holds the 5x3 reels in the middle of the screen, between the two prize ladders.
- **Subject:** Four thin gold rails (up, down, left, right), a grey gradient backing, a 4 px divider, a grey pig-snout emblem that sits faintly behind the reels like a watermark, the gold win line piece and its end, an orange diamond outline (tile17, the empty cell), and layout guides (the green tileGuide square, whiteSquare) that are never shown.
- **Style:** Deliberately plain: a picture frame, not a machine.
- **Rendering:** Polished gold drawn with two or three flat tones and a light line; the backing is a neutral gradient that the game tints to dark maroon (seen in play; the tint is not in the file).
- **Colour:** Measured over the parts: grey #7f7f7f 56% (the untinted backing and emblem), gold #eaba4b 13% and #c56f22 7% (rails); the green #2afe01 12% is the layout guide, not art. On screen the panel is a dark plum-brown.
- **Lighting:** Flat; a light sweep travels the frame (slotFrameLightSweep, 30 frames of small white corner glints).
- **Ambience:** Stays out of the way so the coloured symbols and the textured ladders around it carry the picture.
- **Materials:** Gold rail, dark lacquer panel.
- **Variants:** One frame; no second state for the bonus was found among the sprites.
- **Motion:** SlotFrame idle 1.17 s with the 30-frame glint; ReelAnticipation loop 0.33 s and ReelEffect 0.67 s reuse the dust sequence of the prize plates. Seen in play: the reel under a landing Wild flashes pink-white, a win draws a thin gold line through the row with the winning symbols enlarged and the rest dimmed, and a landing Boost sign bleaches the whole panel to cream.
- **Construction:** Rails of 1028x23 and 29x651 px, so the reel window is about 1028x651 at source scale; the backing is a small 529x315 gradient stretched.
- **Notes:** The grey, tinted-in-engine backing and emblem are a cheap way to recolour the board without new art.
- **Measured:** mid-tone, saturated, warm and cool mixed, low contrast, hard-edged · brightness 59% · saturation 28% · contrast 18% · warm 21% / cool 6% · brighter towards: top (2), right (1), left (1)
- **Palette (measured):** #7f7f7f grey 56%, #eaba4b orange 13%, #2afe01 green 12%, #a7a7a7 grey 7%, #c56f22 orange 7%, #fefdfa light orange 3%

### Prize plates: hay, wood and brick

`sector-plates` · atlas · 3 parts · largest 344×182 · sheet `sheets/sector-plates.webp`

- **Role:** The cells of the three prize ladders around the reels: five hay cells at the left, five wood cells at the right and five brick cells across the top for MINI, MAJOR, GRAND, MEGA and MINOR. Each holds a cash multiplier or a jackpot that Boost symbols raise.
- **Subject:** A straw bale seen from the front, a rough-sawn plank with split ends, and a red brick panel with a pale mortar border.
- **Style:** The three little pigs' three building materials turned into interface: the same idea as the three Wild pigs and the three houses.
- **Rendering:** Painted texture with strong form shadow, each with its own edge: frayed straw, splintered wood, a clean rectangular border for brick.
- **Colour:** Measured: brown #843c16 55% and #521b07 12% (brick, wood shade), tans #c78b49 17%, #ecbc79 12% and #b36c34 4% (straw and wood light). Warm 1.0, cool 0.0.
- **Lighting:** From the upper left on all three (measured top-left 3 of 3).
- **Ambience:** Rustic and tactile next to the flat gold frame; the ladders look built rather than drawn.
- **Materials:** Straw, timber, fired brick and mortar.
- **Variants:** Three plates of about 320x170 px; the value on each is set in the white numeral font, and the jackpot names are separate drawn words.
- **Motion:** The Sectors skeleton has show 0.55 s, pick 0.33 s, swap 0.53 s, boost 1.33 s, win 0.67 s and four boost loops of 0.77 s. Seen in play: when a Boost symbol lands, a white BOOST word flies to a plate, the plate glows gold-white and its number rises (2x to 3x, 25x to 75x).
- **Construction:** One sprite per material, repeated five times; the top row repeats the brick plate at a larger size.
- **Notes:** Material carries rank: straw is the low ladder (1x to 5x at the start), wood the higher one (5x to 10x), brick the jackpots, which is the tale's own order of strength.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 38% · saturation 76% · contrast 54% · warm 100% / cool 0% · brighter towards: top-left (3)
- **Palette (measured):** #843c16 brown 55%, #c78b49 orange 17%, #ecbc79 orange 12%, #521b07 brown 12%, #b36c34 orange 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Symbol pictures for the help page

`help-symbol-pictures` · atlas · 18 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The flat pictures the provider's help window lists with their pays.
- **Subject:** All 17 symbols at 225x225 px: the five letters, the four tools (the toolbox with its tools standing in it), the three Wild pigs in their frames with WILD, the Boost signpost with its word, the three houses whole (straw and wood in frames, brick without), and the empty diamond; tile0 is a blank from the shared store.
- **Style:** The reel symbols as finished single pictures.
- **Rendering:** As on the reels; these show each animated symbol composed, which the atlas parts do not.
- **Colour:** Measured: skin and plaster #f8c68e 12%, dark red #53190b 12%, red #da382f 8%, blue #79b2e5 6%, gold #f4b718 6% and #f9cf55 4%, dark green #192c19 6%.
- **Lighting:** From above (measured top 8).
- **Ambience:** A tidy catalogue of the cast.
- **Materials:** As the symbols.
- **Variants:** One picture per symbol.
- **Motion:** None; stills.
- **Construction:** Separate files in the provider's shared asset store for this game (`assets/games/<slug>/tiles/tileN.webp`), outside the game bundle.
- **Notes:** These are the only place in the files where a Wild pig or a house can be seen assembled without a renderer for Spine 4.2.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 51% · saturation 63% · contrast 74% · warm 72% / cool 20% · brighter towards: top (8), top-left (2), bottom-left (1)
- **Palette (measured):** #f8c68e light orange 12%, #53190b dark red 12%, #da382f red 8%, #79b2e5 blue 6%, #f4b718 orange 6%, #192c19 dark green 6%

### The three Wild pigs

`symbols-wild-pigs` · atlas · 32 parts · largest 441×475 · sheet `sheets/symbols-wild-pigs.webp`

- **Role:** The three Wilds, one per pig: Straw Farmer (plain Wild), Woodworker (x2) and Builder (x3), as the help page names them. Each throws coins to the heap above the reels and, in the bonus, turns into its house.
- **Subject:** Bust portraits in square frames. The farmer pig wears a straw hat and chews a wheat ear, in a steel-blue frame. The woodworker has a ginger beard and a topknot and holds a hammer and a plank, in a copper frame. The builder wears a red hard hat with goggles, laughs with eyes shut and holds a gold trowel, in a gold frame. All three stand before the same forest view, with WILD in gold letters across the bottom.
- **Style:** Animated-feature character portraits, more rendered than anything else on the reels.
- **Rendering:** Painted with soft blended skin, sharp specular dots and a thin light rim; the frames are bevelled metal; measured high contrast 0.66 and hard-edged.
- **Colour:** Measured: skin pink #f8bb94 20% and #e0835d 7%, dark forest #1c423b 19% and #446c56 5%, browns #b75d25 13% and #6d2811 11%, steel blue #61919d 7%. The frame colour ranks the three: steel, copper, gold.
- **Lighting:** A warm key from the upper right on the faces (measured top-right 7, top 5).
- **Ambience:** Three good-natured workmen; the portraits put faces on the reels that otherwise show only objects.
- **Materials:** Skin, straw, cloth, hair, steel, wood, a metal frame.
- **Variants:** Three characters on one layout. Each is cut for animation: the bust, both ears, the snout, eyelids and blink pieces, hands or an arm, the held tool and the background square are separate sprites (32 in all).
- **Motion:** TileWild: onLand 0.58 s, loop 1.33 s, win 0.67 s, loopSplash and loopWinSplash 2 s, transformStart 0.5 s. Seen in play: a Wild lands with its reel flashing pink-white, the portrait breaks out of its frame at a larger size on a win, and the multiplier (x2, x3) sits at its corner. No skeleton frame is shown here; the rig is Spine 4.2.
- **Construction:** Busts of 405 to 441 px over background squares of about 290 px, so the character is drawn larger than its cell and can lean out of the frame.
- **Notes:** One rig, three skins is the economy to note: the pigs share construction, and only costume, prop and frame metal change.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 49% · saturation 59% · contrast 66% · warm 65% / cool 30% · brighter towards: top-right (7), top (5), bottom-left (2)
- **Palette (measured):** #f8bb94 light orange 20%, #1c423b dark cyan 19%, #b75d25 orange 13%, #6d2811 brown 11%, #e0835d orange 7%, #61919d cyan 7%

### Boost symbol: the signpost arrow

`symbol-boost` · atlas · 4 parts · largest 411×311 · sheet `sheets/symbol-boost.webp`

- **Role:** The Boost symbol: when it lands it raises the values on the prize plates.
- **Subject:** A fat yellow arrow with an orange edge on a yellow pole in a tuft of grass, with BOOST in white letters as a separate piece.
- **Style:** A cartoon road sign.
- **Rendering:** Flat yellow with one lighter band, a thick orange outline and a thin cyan-green contact edge below; the word has a dark outline.
- **Colour:** Measured: gold #fee030 46%, orange #d45704 22%, cream #fefef7 10%, brown #7a4d0a 7%.
- **Lighting:** Gloss from the upper left.
- **Ambience:** The loudest object on the reels; it reads as an instruction.
- **Materials:** Painted sheet metal or enamel, grass.
- **Variants:** One arrow, one word, one pole, one tuft.
- **Motion:** TileBooster: onLand 0.58 s, loop 2.67 s, boost 0.92 s. Seen in play: the sign grows to three cells wide across the middle of the reels while the other symbols bleach to cream, then white BOOST words fly to the plates, which light up and rise.
- **Construction:** Four sprites, the arrow 411x311 px: larger than a cell, for the grown state.
- **Notes:** The same word in the same letters travels from the symbol to the plate it boosts, so cause and effect are drawn as one object moving.
- **Measured:** bright, vivid, warm, high contrast, hard-edged, strong highlights · brightness 71% · saturation 75% · contrast 60% · warm 96% / cool 2% · brighter towards: top-left (1)
- **Palette (measured):** #fee030 gold 46%, #d45704 orange 22%, #fefef7 light gold 10%, #7a4d0a brown 7%, #f8a414 orange 5%, #fef68c light gold 2%

### High symbols: trowel, tape measure, hard hat, toolbox

`symbols-tools` · atlas · 41 parts · largest 383×354 · sheet `sheets/symbols-tools.webp`

- **Role:** The four high-paying symbols: the pigs' building tools.
- **Subject:** A blue-bladed trowel with a yellow handle (tile6), a pink and purple tape measure whose face is a snout (tile7, with its steel tape as a separate piece), a red hard hat with a gold snout badge (tile8) and a gold toolbox with a snout front, holding a saw, a spirit level, a wrench, a putty knife and a screwdriver as separate pieces (tile9).
- **Style:** Toy-like cartoon objects, rounded and thick, with the same snout mark as the letters.
- **Rendering:** Smooth gradients, a warm rim, a clear outline and hard gloss marks; steel is drawn in flat grey bands.
- **Colour:** Measured: red #d43232 20% (hat), gold #fbbf09 11% and #fde06e 8% (box, handles), orange #db830d 8% and brown #9b4b05 12%, with white #f8faf9 14% and grey #bbc5c5 10% from the swirl frames and steel. The trowel and tape add blue and pink in small amounts.
- **Lighting:** From the upper left (measured top-left 4), with a glossy highlight on each curved top.
- **Ambience:** A child's tool set: cheerful, harmless, clearly handled by small cartoon animals.
- **Materials:** Plastic, enamelled metal, steel, wood.
- **Variants:** The hat has two motion-blurred copies (tile8BlurS, tile8BlurF); the toolbox is built from a back, a front and five loose tools. Three white hand-drawn sequences belong to them: tile6Stroke (8 frames, a straight swipe), tile7AirSwirl (9 frames, a ring) and tile8Swirl (11 frames, a spinning wisp).
- **Motion:** TileContainerSeniors has win 0.67 s and showWinSplash 0.67 s. Seen in play: winning symbols grow past their cell and a winning tape measure sits inside the white air ring. By the parts and names the trowel swipes, the hat spins through its blurred copies and the toolbox's tools move on their own (inference; not caught in a frame).
- **Construction:** Sprites of 127 to 383 px; the toolbox alone is seven pieces so the tools can jump.
- **Notes:** Each high symbol gets one small physical gag instead of a glow, which costs a few loose parts and one short white sequence each.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 61% · saturation 61% · contrast 56% · warm 78% / cool 5% · brighter towards: top-left (4), left (1), right (1)
- **Palette (measured):** #d43232 red 20%, #f8faf9 light green 14%, #9b4b05 brown 12%, #fbbf09 gold 11%, #bbc5c5 grey 10%, #fde06e gold 8%

### The three houses, whole and blown down

`symbols-houses` · atlas · 33 parts · largest 290×292 · sheet `sheets/symbols-houses.webp`

- **Role:** The bonus symbols: a straw, a wood and a brick house, which the Wild pigs become when Hold & Win starts and which lock on the reels (the splash text reads HOUSES LOCK ON THE REELS). Each reveals a cash prize or a jackpot.
- **Subject:** The straw house is a round thatched hut with ears and a snout-shaped door; the wood house a leaning plank cabin with a horned plank roof; the brick house a neat cottage with orange roof tiles, a chimney and round windows. Each has a background square (steel frame with green hills for straw, a dark red square for wood, a gold frame with hills for brick) and broken versions of its parts: a splintered front, torn roof sides, loose planks.
- **Style:** The scene's storybook houses redrawn as small props with thick shapes.
- **Rendering:** Painted with clear planes of light and shade and a dark outline; tiles and planks are drawn one by one.
- **Colour:** Measured: dark red-brown #33130c 29% and #72260e 8%, orange #a94d26 15% and #f6bc63 7% (tiles, planks, straw), dark green #0e3f30 11% and #386450 7% (hills), cream #fad7b0 8% (plaster).
- **Lighting:** From the upper left (measured top-left 8, top 6).
- **Ambience:** Cosy when whole; the destroyed parts turn each into a comic wreck rather than a ruin.
- **Materials:** Thatch, planks, plaster, roof tile, brick.
- **Variants:** Three houses, each in parts (base or front, roof left and right, near and far roof sides, foliage) with a destroyed twin for the wood and brick houses; the straw house has loose roof tufts instead.
- **Motion:** TileHouse: show 0.57 s, onLand 0.58 s, loop 2 s, activate 0.33 s, activateLoop 1.67 s, burst 0.83 s, reveal0 to reveal2 0.58 s, revealSplash 1 s. By the parts and names the roof and front fly apart on burst and the prize shows behind (inference; the bonus was not reached in play, and the help picture shows the three houses whole above the prizes 4x, 10x and MAJOR 750x).
- **Construction:** 33 sprites; background squares of 290 px with house parts of 54 to 307 px laid over them.
- **Notes:** Drawing every house twice, whole and broken, in loose parts lets one skeleton stage the tale's central gag on any cell.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 35% · saturation 71% · contrast 66% · warm 72% / cool 22% · brighter towards: top-left (8), top (6), left (4)
- **Palette (measured):** #33130c dark red 29%, #a94d26 orange 15%, #0e3f30 dark cyan 11%, #72260e dark red 8%, #fad7b0 light orange 8%, #386450 green 7%

### Low symbols: 10, J, Q, K, A with pig snouts

`symbols-letters` · atlas · 5 parts · largest 176×133 · sheet `sheets/symbols-letters.webp`

- **Role:** The five low-paying symbols.
- **Subject:** A blue 10 whose zero is a snout, a purple J with a snout for its dot, a green Q with a snout as its tail, a red K with a snout at the top of the stem and a gold A with a snout at its foot.
- **Style:** Inflated cartoon letters, each with a pig's snout worked into the letterform so that even the fillers belong to the tale.
- **Rendering:** Smooth gradient fill, a darker inner edge, a thick dark outline and one curved white gloss; measured hard-edged and high contrast 0.755.
- **Colour:** One hue each. Measured over the five: blue #6eb1e5 19%, red #e43130 10%, greens #73d034 and #a5e972 14% together, gold #f5c523 6%, near-black #140e1c 13% (outlines), dark red #500804 7%.
- **Lighting:** Gloss from above (measured top 5 of 5); no cast shadow.
- **Ambience:** Candy-bright against the dark reel panel.
- **Materials:** Glossy plastic or balloon.
- **Variants:** One picture each, about 130 to 176 px. The help page shows a separate, larger set.
- **Motion:** No frames of their own. TileContainerJuniors has a win of 0.62 s and carries the 15-frame white puff (transformEffect) that is seen when symbols change.
- **Construction:** Single sprites with free air around them in the reel cell; no tile behind.
- **Notes:** The snout is the only device: five letters themed with one small shape.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 50% · saturation 68% · contrast 76% · warm 44% / cool 38% · brighter towards: top (5)
- **Palette (measured):** #6eb1e5 blue 19%, #140e1c black 13%, #e43130 red 10%, #73d034 green 7%, #500804 dark red 7%, #a5e972 green 7%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The wolf: a full-figure character in parts

`wolf` · atlas · 43 parts · largest 740×1374 · sheet `sheets/wolf.webp`

- **Role:** The game's villain and the actor of the bonus: he stands on the intro screen and, by the skeleton SectorsActivator (activate 3.23 s, loop 2.67 s), is the one who blows at the prize plates.
- **Subject:** A grey and white wolf standing upright with hands on hips, in blue denim dungarees over a grey checked shirt with rolled sleeves, black clawed feet, a dark bushy tail, red inner ears, and three heads: a sly grin (chrHead), eyes shut with cheeks drawn in (chrHeadInhale) and puffed with lips pursed (chrHeadBlowing).
- **Style:** Western animated-feature cartoon: big head with heavy brows, small waist, long legs, readable attitude from the silhouette alone.
- **Rendering:** Painted with soft gradients and a few hard accents; the fur is drawn as large pointed tufts with white rims, the denim with stitched seams and a pocket.
- **Colour:** Measured: dark blue-grey #2d3646 33% (fur and shade), denim blue #4b85a4 24% and #2c527b 4%, white #f4f5f4 12% (muzzle, chest, breath), greys #77787a 12% and #cbcdcb 7%. The only warm note is the red of the ears.
- **Lighting:** Light from the upper left on the body with a thin cyan rim along the arms and legs; the measure finds no single direction over the parts.
- **Ambience:** More smug than frightening: a foreman in work clothes who has come to inspect the building site.
- **Materials:** Fur, denim with brass buttons, woven shirt cloth, claws.
- **Variants:** One body, two arms (one resting on the hip), one tail, one ear and three swappable heads for the breath cycle; two breath sequences in flat white, characterInhaleEffect (10 frames of thin curved streaks) and characterExhaleEffectNew (25 frames of a rolling cloud).
- **Motion:** A Spine skeleton (SectorsActivator) that swaps heads through inhale and blow, with the two hand-drawn breath sequences. Seen in play only as the standing pose on the intro screen; the bonus was not reached, so the blow is read from the files and the help picture, where he blows a white cloud.
- **Construction:** A body of 740x1374 px with separate arms, tail, ear and heads on the main pages. No skeleton frame is shown: the file is Spine 4.2, which the project's renderer cannot draw.
- **Notes:** He is the largest single drawing in the game and is kept out of the base game, so the bonus has something the player has not been looking at all session (inference).
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged · brightness 45% · saturation 31% · contrast 56% · warm 12% / cool 78% · brighter towards: top-left (2), top-right (2), left (2)
- **Palette (measured):** #2d3646 dark blue 33%, #4b85a4 blue 24%, #f4f5f4 white 12%, #77787a grey 12%, #cbcdcb grey 7%, #2c527b blue 4%


## Logo and title

The game's own wordmark.

### Logo as one picture (help page)

`help-logo` · atlas · 1 parts · largest 710×199 · sheet `sheets/help-logo.webp`

- **Role:** The flattened logo the provider's help window shows at its top.
- **Subject:** All four words with the wolf head behind CASH, on a bed of straw with a green bush at the left end.
- **Style:** The same lettering as the in-game logo.
- **Rendering:** Flat fills, outlines and gloss; straw drawn as fine yellow strokes.
- **Colour:** Measured: cream #fbebb8 14%, red #ec0705 9%, yellow #fbf02c 4%; the rest is spread over outline tones.
- **Lighting:** Gloss from above.
- **Ambience:** A badge version, readable at small size on the dark help window.
- **Materials:** Enamel letters, straw.
- **Variants:** One picture, 710x199 px.
- **Motion:** None; a still.
- **Construction:** A single file from the provider's shared asset store for this game (`assets/games/<slug>/logo/default.webp`), not from the game's atlas.
- **Notes:** Octoplay keeps a flat logo and flat symbol pictures per game outside the game bundle, for its shell.
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 57% · saturation 59% · contrast 78% · warm 71% / cool 28% · brighter towards: right (1)
- **Palette (measured):** #fbebb8 light gold 14%, #ec0705 red 9%, #fbf02c gold 4%

### Logo: SUPER CASH BOOST over BIG BAD BONUS

`logo` · atlas · 7 parts · largest 587×91 · sheet `sheets/logo.webp`

- **Role:** The title, above the reels in the base game and on the intro screen.
- **Subject:** Three words in three treatments, SUPER in red with a yellow outline and mixed upper and lower case shapes, CASH in gold, BOOST in cream to peach with the T raised, then BIG BAD BONUS smaller in cyan with a dark blue outline; the wolf's head on a shield-shaped tuft of chest fur (logoHead) and a small green bush. A sprite named `default` reads BOILERPLATE in the same lettering as the provider's other games use for a placeholder (inference: a template leftover, not shown in play).
- **Style:** Bouncy cartoon lettering with uneven baselines, close to a comic title.
- **Rendering:** Flat fills with a gloss band, a thick outline and a dark drop shadow; the head is painted like the character.
- **Colour:** Measured: gold #fee523 22%, orange #f69615 11%, red #ee0f04 9%, peach #fbdca8 8%, cream #f8f6e0 6%, black #140609 5%.
- **Lighting:** A gloss from above on each letter; no cast light.
- **Ambience:** Loud and friendly; the wolf peering over the middle word is the one hint of the villain in the base game.
- **Materials:** Glossy enamel letters, fur.
- **Variants:** The words are separate sprites (logoLabel1 SUPER, logoLabel2 CASH, logoLabel3 BOOST, logoLabel4 BIG BAD BONUS), so they can move one by one. The help page uses a flattened copy on a straw nest (help-logo).
- **Motion:** Logo skeleton: show 1 s, idle 2.5 s, idleGameSplash 6.67 s, win 1.17 s, collect 0.5 s, hide 0.33 s. Seen after START: the words drop in one after another over the reels. A heap of gold coins lies behind the logo throughout play; the help says Wild pigs throw coins onto it.
- **Construction:** Word sprites of 246 to 431 px wide, a 120x172 head and a 38 px bush.
- **Notes:** The coin heap behind the logo belongs to the mechanic (coins thrown by Wilds collect there), so the logo doubles as the place the player watches for the bonus.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 61% · saturation 70% · contrast 74% · warm 77% / cool 23% · brighter towards: top (2), right (1)
- **Palette (measured):** #fee523 gold 22%, #f69615 orange 11%, #ee0f04 red 9%, #fbdca8 light orange 8%, #f8f6e0 light gold 6%, #140609 black 5%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Bonus labels: HOLD & WIN and its rule line

`feature-labels` · atlas · 4 parts · largest 1064×188 · sheet `sheets/feature-labels.webp`

- **Role:** The words of the bonus splash.
- **Subject:** HOLD & WIN in gold capitals with a dark outline (fsLabelTxt) and HOUSES LOCK ON THE REELS in small white capitals (fsSplashTxt), with two black 50 px squares used as screen fades.
- **Style:** The numeral fonts' round sans rather than the logo's balloon letters.
- **Rendering:** Flat gold with a lighter top half and a thick near-black outline and offset shadow.
- **Colour:** Measured: gold #f7cf3d 41%, near-black #111010 18%, cream #e1dad3 13%.
- **Lighting:** A flat top gloss.
- **Ambience:** Plain and instructive; the splash relies on the scene and the wolf for its drama (inference: the splash was not reached).
- **Materials:** Enamel lettering.
- **Variants:** Two localised word pictures (en-GB) and two fades.
- **Motion:** FreeSpinsSplash show 0.67 s, loop 6 s, hide 0.5 s; BonusSpinsSplash show 1 s. Not seen in play.
- **Construction:** Each label is its own 1064 px wide file under `imagesLocalized/…/en-GB`, so a language swaps without touching the atlas.
- **Notes:** The feature is named by its mechanic (Hold & Win), not by the tale; the tale is left to the pictures.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 57% · saturation 47% · contrast 82% · warm 67% / cool 29% · brighter towards: top (1)
- **Palette (measured):** #f7cf3d gold 41%, #111010 black 18%, #e1dad3 light orange 13%, #9c9a9a grey 8%, #48412f brown 8%, #7a692d brown 5%

### Win celebrations: BIG, SUPER, MEGA and TOTAL WIN on building materials

`win-tiers` · atlas · 20 parts · largest 1064×292 · sheet `sheets/win-tiers.webp`

- **Role:** The plates and words of the win tiers and the bonus total.
- **Subject:** Words: BIG WIN in pink-purple, SUPER WIN in blue, MEGA WIN in green and TOTAL WIN in blue-teal, in the logo's lettering. Plates and dressing: a straw sum plate and a wood sum plate (win1SumPlate, win2SumPlate), three brick blocks of different widths, a large hay bale, crossed planks with nails, one plank, a big and a small pile of orange bricks, two loose bricks, two strips of daisies and grass, two leaves.
- **Style:** The base scene's building site reused as a stage for the win.
- **Rendering:** The props are painted like the background's foreground props; the words are flat with gloss and outline.
- **Colour:** Measured: brown #8d3c15 30% and #451205 7%, straw #cd944d 18% and #f1ce84 6%, brick orange #f9782e 8%, blues #97c6e7 and #6ea7ea 6% together (the words).
- **Lighting:** From the upper left on the props (measured top-left 7, top 6).
- **Ambience:** A win is built, not exploded: straw, planks and bricks pile up around the amount and a pig looks over the top.
- **Materials:** Straw, timber, brick, flowers.
- **Variants:** Three tier words and a total on one lettering; two sum plates; bricks in five sizes. BIG WIN was seen with the straw plate, the hay bale and the Straw Farmer pig; by the parts, SUPER WIN and MEGA WIN use wood and brick with the other two pigs (inference).
- **Motion:** WinSmall and WinNormal sumShow 0.33 s; WinBig labelShow 0.83 s, sumShow 0.33 s; WinTotal show 0.75 s. Seen in play: ordinary wins show the amount in the gold numerals over the reels; a BIG WIN raises the Straw Farmer pig's bust above the reels beside a hay bale and a board with daisies, the pink words over the amount on its straw plate, piggy coins flying and the reels dimmed purple. SUPER WIN, MEGA WIN and TOTAL WIN did not come in the sessions.
- **Construction:** 20 sprites, the widest (TOTAL WIN) a localised file of 1064x292 px; props of 147 to 819 px.
- **Notes:** The ladder of materials (straw, wood, brick) is used again here, after the pigs, the houses and the prize plates, and the pig of the tier presents the win in person.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 46% · saturation 72% · contrast 54% · warm 77% / cool 17% · brighter towards: top-left (7), top (6), left (1)
- **Palette (measured):** #8d3c15 brown 30%, #cd944d orange 18%, #f9782e orange 8%, #451205 dark red 7%, #f1ce84 orange 6%, #97c6e7 blue 4%

### Jackpot names and the jackpot win plate

`jackpot-plates` · atlas · 16 parts · largest 769×371 · sheet `sheets/jackpot-plates.webp`

- **Role:** The five jackpot names (MINI, MINOR, MAJOR, MEGA, GRAND) shown on the brick row above the reels and on a ladder cell that holds a jackpot, and the parts of the plate shown when one is won.
- **Subject:** Five words in fat rounded capitals, each in its own colour with a darker outline of the same hue and a white inner line: MINI magenta-purple, MINOR light blue, MAJOR green, MEGA red-orange, GRAND gold. A large brick wall panel (jackpotSplashBg, 769x371) and, per jackpot, a top strip and a side strip of four glossy bricks in that jackpot's colour.
- **Style:** The same balloon lettering as the logo, colour-coded.
- **Rendering:** Vertical gradient fill, gloss band, double outline; the bricks are flat with a light top edge.
- **Colour:** Measured: brick red #8f3012 23% and #4e0b08 8%, gold #f2ca3d 12%, then small shares of each code colour: green #115703, blues #648ddf and #9dc5ea, purple #530767, dark blue #08346a.
- **Lighting:** Gloss from above (measured top 10).
- **Ambience:** Five prizes told apart at a glance by colour before the word is read.
- **Materials:** Enamel letters, glazed brick.
- **Variants:** Five words, five top strips, five side strips, one wall. The file name of one strip is misspelt as shipped (`jackpotSplashMiinorUp`).
- **Motion:** JackpotLabels show; WinJackpot show 1.17 s, loop 8.33 s, hide 0.5 s. In play the names sit still on the brick row and a boosted jackpot's plate glows gold-white while its number rises (GRAND from 1000x to 2500x in the opening sequence). No jackpot was won in the sessions, so the win plate is read from its parts: a brick wall framed by strips of the jackpot's colour (inference).
- **Construction:** Word sprites of 608 to 828 px wide, much larger than shown on the plates, so the same word serves the win plate.
- **Notes:** The jackpot win is a brick wall, the strongest material of the tale, bordered in the jackpot's own colour: theme and prize code in one plate.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 46% · saturation 74% · contrast 57% · warm 63% / cool 29% · brighter towards: top (10), top-left (5), bottom-right (1)
- **Palette (measured):** #8f3012 red 23%, #f2ca3d gold 12%, #4e0b08 dark red 8%, #115703 dark green 4%, #648ddf blue 4%, #9dc5ea light blue 4%


## Effects

Frame sequences, glows, particles and transitions.

### Prize plate effects: boost bursts, dust and the wind strike

`sector-effects` · atlas · 121 parts · largest 228×360 · sheet `sheets/sector-effects.webp`

- **Role:** Everything that happens to a prize plate: it lights when boosted, puffs dust when its value swaps and is struck by the wolf's wind when it pays.
- **Subject:** For each material (brick, hay, wood): a 4-frame burst that is the plate itself with a white-hot glowing edge, and a 23-frame light sweep that starts as the plate's lit top edge and thins to a faint streak. A 27-frame white dust burst rising in columns (sectorSwapEffect, 228x360) and a 13-frame horizontal white gust (sectorsWinWindStrike, up to 677x90).
- **Style:** Hand-drawn 2D effect animation in flat white, with the plate bursts painted from the plates.
- **Rendering:** Flat white shapes with ragged cartoon edges for dust and wind; soft additive glow on the plate bursts (measured soft edge 0.54).
- **Colour:** Measured: white #fefefd 67%, then the plates' own browns #883f1a 12%, #bf8455 8% and tans. No colour is added by the effects; they only whiten.
- **Lighting:** Self-lit; the bursts read as light coming off the plate.
- **Ambience:** Dry and physical: dust and wind rather than sparkle, which suits straw, wood and brick.
- **Materials:** Dust, air, glare.
- **Variants:** The burst and sweep are drawn three times, once per material, on the same timing; dust and wind are shared.
- **Motion:** Sectors boost 1.33 s with boost loops of 0.77 s, swap 0.53 s, win 0.67 s; BonusWind win 0.67 s. Seen in play: a boosted plate flares gold-white with its edge alight and its number replaced. The wind strike belongs to the bonus and was not seen.
- **Construction:** 121 sprites, the largest group in the game, most of them thin strips from 17 to 91 px high.
- **Notes:** The most frames in the game are spent on the prize plates, not on the reels: the plates are where the player's eye is meant to rest between spins (inference).
- **Measured:** bright, muted, warm and cool mixed, medium contrast, strong highlights · brightness 84% · saturation 19% · contrast 28% · warm 35% / cool 7% · brighter towards: bottom (3), top (3), left (3)
- **Palette (measured):** #fefefd light gold 67%, #883f1a brown 12%, #bf8455 orange 8%, #c4cac5 grey 5%, #f1cca3 light orange 4%, #daa77c orange 2%

### Light pieces and guides

`light-and-particles` · atlas · 10 parts · largest 512×512 · sheet `sheets/light-and-particles.webp`

- **Role:** The soft lights every glow in the game is made of, plus technical pieces.
- **Subject:** A round white glow in two files (glowCircle, whiteGlow, 494 px), a white star burst of rays (circularWhiteRays2), a fan of faint vertical rays (raysWhite4), a soft white square (glowSquare), a small four-point glint, a yellow dot, a tiny glow strip, a 512 px cloud noise used to distort (displacement) and a green guide square that is never shown.
- **Style:** Generic white light sprites.
- **Rendering:** Soft gradients, to be tinted and added.
- **Colour:** Measured greys and white; the green #18ff00 7% is the guide.
- **Lighting:** They are the light.
- **Ambience:** None of their own.
- **Materials:** Light.
- **Variants:** One of each.
- **Motion:** Used by most skeletons (SpinEffect 0.5 s, the splashes, the collector, the plates).
- **Construction:** Ten sprites. circularWhiteRays2, glowSquare and whiteGlow are the same pictures, pixel for pixel once alpha is applied, as in the Fire Rail Express and 777 Hot Reels runs: pieces of Octoplay's shared kit.
- **Notes:** Not this game's own art except the vertical ray fan, which the other two runs do not have under that name.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 77% · saturation 7% · contrast 23% · warm 0% / cool 4%
- **Palette (measured):** #a5a5a5 grey 41%, #fefefe white 39%, #717171 grey 10%, #18ff00 green 7%, #d7d7d7 grey 2%

### Smoke, puffs and dust

`smoke-and-dust` · atlas · 21 parts · largest 372×112 · sheet `sheets/smoke-and-dust.webp`

- **Role:** General-purpose puffs: where a symbol changes into another, where something lands, and the dust of the transition into the bonus.
- **Subject:** A 5-frame flat white cloud that spreads sideways (smokeBurst, up to 372x112), a 15-frame set of small white puffs that scatter outward and shrink (transformEffect) and one soft grey dust blot (particleDust).
- **Style:** Flat cartoon smoke with scalloped edges and a pale grey underside.
- **Rendering:** Two-tone flat shapes; only the dust blot is soft.
- **Colour:** Measured: white #f1f1f3 78%, greys #686868 13% and #b8b8b8 9%; saturation 0.006.
- **Lighting:** None; flat.
- **Ambience:** Light and comic.
- **Materials:** Smoke, dust.
- **Variants:** Two sequences and one blot.
- **Motion:** TransformEffect show 0.57 s, ParticleSpawn loop 0.5 s. SlotTransition (show 2.08 s) is built from brick-wall pieces, so the way into the bonus is by its names a wall rising or falling in dust (inference; not seen).
- **Construction:** 21 small sprites on the main pages.
- **Notes:** White flat smoke is the game's one effect language, shared by the wolf's breath, the plates and the symbols.
- **Measured:** bright, muted, neutral, medium contrast, strong highlights · brightness 86% · saturation 1% · contrast 28% · warm 0% / cool 30% · brighter towards: left (1)
- **Palette (measured):** #f1f1f3 white 78%, #686868 grey 13%, #b8b8b8 grey 9%

### The piggy coin

`coin` · atlas · 30 parts · largest 169×170 · sheet `sheets/coin.webp`

- **Role:** The coin a Wild pig throws to the heap above the reels and the coin of the win showers.
- **Subject:** A gold coin with a pig's face in relief, shown turning through a full flip.
- **Style:** Cartoon coin, thick-rimmed.
- **Rendering:** Flat gold with a darker relief line, a pale highlight arc and a thick edge when seen from the side.
- **Colour:** Measured: gold #f7bb05 72% and #feeb70 18%, brown #bd7c02 4%.
- **Lighting:** Gloss from the upper right.
- **Ambience:** Bright and toy-like.
- **Materials:** Gold.
- **Variants:** One 30-frame turn (coinPiggy_00 to _29) at about 170 px.
- **Motion:** ParticleCoin loop 1 s and TrailEffect collect 0.5 s use the turn; in play coins lie in a heap behind the logo and scatter over a win amount.
- **Construction:** 30 frames spread over both atlas pages.
- **Notes:** Even the coin carries the pig mark, so the currency belongs to this game and not to the provider's shell.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 76% · saturation 88% · contrast 31% · warm 100% / cool 0% · brighter towards: top-right (4), top (2)
- **Palette (measured):** #f7bb05 gold 72%, #feeb70 gold 18%, #bd7c02 brown 4%, #feed22 gold 2%, #efbc4b orange 2%

### Butterflies

`butterflies` · atlas · 6 parts · largest 49×39 · sheet `sheets/butterflies.webp`

- **Role:** Ambient life over the meadow in the base game.
- **Subject:** A white butterfly in six wing positions from open to edge-on, at most 49x39 px.
- **Style:** A silhouette, tinted by the game.
- **Rendering:** Flat white with a soft edge.
- **Colour:** Measured white #ffffff 100%; any colour comes from the engine.
- **Lighting:** None.
- **Ambience:** A small sign that the scene is alive.
- **Materials:** None to speak of.
- **Variants:** One 6-frame flap.
- **Motion:** ParticleButterflyNormal loop 0.2 s; in play small pale specks drift at the screen edges.
- **Construction:** Six tiny sprites.
- **Notes:** Six frames of 49 px are the whole cost of an animated background.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff light cyan 100%


## Game interface

Buttons, counters and panels drawn for this game.

### Coin heap, coin counters and the spin counter

`collector-and-counters` · atlas · 20 parts · largest 280×256 · sheet `sheets/collector-and-counters.webp`

- **Role:** The game's own small interface: the heap of coins that grows above the reels as Wild pigs land, and the counter of the bonus's three spins.
- **Subject:** A wide heap of gold coins (coinHeapBig), a short stack (coinStack), three views of a small coin lying flatter and flatter (progressCoin), a dark plate in a gold rim (counterPlate) with the white numerals 1, 2 and 3 as drawn pieces, and a ten-frame cream puff with white debris (sceneCollectorExplosion).
- **Style:** Cartoon treasure, in the same gold as the frame.
- **Rendering:** Flat gold with a darker edge and a light dot; the puff is a flat cream shape with a white core.
- **Colour:** Measured: pale gold #fdf6c1 55% (the puff), gold #f6ba09 14% and #eebd49 2%, dark red-brown #3d1005 10% (the plate).
- **Lighting:** Flat, with a top gloss on the coins.
- **Ambience:** A growing pile that promises the bonus; the help text says the pile is for show and does not change the odds.
- **Materials:** Coin gold, a lacquered plate.
- **Variants:** One heap, one stack, three coin views, three numerals. `fsCounter` is an empty 280x256 guide box.
- **Motion:** SceneCollector: progress 1.67 s, create 0.5 s, show 0.4 s, win 1.17 s, winLoop 1.33 s, idle 1.83 s; SpinCounter: show 0.88 s, progress 0.33 s, reset 0.45 to 0.58 s, anticipation 0.5 s. In play the heap sits behind the logo; a coin in flight to it was not caught in a frame. The spin counter was not seen in play; the help picture shows the plate with 1 2 3.
- **Construction:** Small sprites (the heap is 311x139 px) on the main pages.
- **Notes:** The counter plate takes the place of the usual free-spins panel: three lives shown as three numerals.
- **Measured:** bright, saturated, warm, low contrast, strong highlights · brightness 82% · saturation 41% · contrast 22% · warm 97% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #fdf6c1 light gold 55%, #fcfcfa light green 14%, #f6ba09 orange 14%, #3d1005 dark red 10%, #eebd49 orange 2%


## Typography

Embedded fonts and lettering.

### Numerals, white (MarvinRound)

`MarvinRound` · atlas · 24 parts · largest 332×475 · sheet `sheets/MarvinRound.webp`

- **Role:** The white numerals and signs on the hay and wood prize plates and for multipliers.
- **Subject:** Heavy rounded digits 0 to 9 with x, +, -, comma, full stop, slash, asterisk and question mark, and the letters X, C, p, t, i, l loaded as single files.
- **Style:** A fat rounded display face, soft as dough, close in spirit to the logo.
- **Rendering:** Off-white fill with a thick black outline and a black shadow offset down and to the right.
- **Colour:** Measured: off-white #e8e1da 61%, black #1a1819 36%.
- **Lighting:** Flat; the offset shadow suggests light from the upper left.
- **Ambience:** Chunky and friendly, readable on straw and wood texture alike.
- **Materials:** Flat print.
- **Variants:** 24 glyphs kept: 18 from the font page and six letters loaded as files of their own. The font lists 92 more such single-file glyphs that this session never loaded.
- **Motion:** None.
- **Construction:** A bitmap font from Octoplay's shared font store (`fonts-v2/MarvinRound`), glyphs about 340 px high on a 2048 px page.
- **Notes:** Fire Rail Express and 777 Hot Reels take other faces from the same store (UltraPurpleGold; UltraGold, UltraActive, UltraInactive), so the store is shared and the choice is the game's.
- **Measured:** mid-tone, muted, neutral, high contrast, hard-edged, strong highlights · brightness 59% · saturation 16% · contrast 82% · warm 3% / cool 96% · brighter towards: top-left (20), left (4)
- **Palette (measured):** #e8e1da light orange 61%, #1a1819 black 36%

### Numerals, yellow (MarvinRoundYellow)

`MarvinRoundYellow` · atlas · 14 parts · largest 150×196 · sheet `sheets/MarvinRoundYellow.webp`

- **Role:** The gold numerals of the jackpot values on the brick row and of win amounts.
- **Subject:** Digits 0 to 9 with x, +, comma and full stop.
- **Style:** The same fat rounded face.
- **Rendering:** Yellow fill with a darker orange lower half, black outline and offset shadow.
- **Colour:** Measured: gold #f9d94c 52%, orange #f3b821 16%, black #111009 21%.
- **Lighting:** A flat two-tone split, light above.
- **Ambience:** Coin-gold; it marks money wherever it appears.
- **Materials:** Flat print.
- **Variants:** 14 glyphs.
- **Motion:** None of its own; the game counts amounts up in it (WinNormal sumBangupEnd 0.5 s).
- **Construction:** A bitmap font from the shared store (`fonts-v2/MarvinRoundYellow`), glyphs about 185 px high on a 2048x256 page.
- **Notes:** White for multipliers that can change, gold for jackpots and wins: two colourings of one face do the work of a type system.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 60% · saturation 67% · contrast 89% · warm 99% / cool 0% · brighter towards: top-left (10), top (4)
- **Palette (measured):** #f9d94c gold 52%, #111009 black 21%, #f3b821 orange 16%, #302916 brown 7%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 518 components cut from 37 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
