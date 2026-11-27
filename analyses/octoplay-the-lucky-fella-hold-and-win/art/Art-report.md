# The Lucky Fella Hold And Win: art report

octoplay · run `2026-11-27-0430-octoplay-the-lucky-fella-hold-and-win` · captured 2026-11-27

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/the-lucky-fella-hold-and-win

**Extracted:** 533 named components from 49 textures in 49 atlases; 64 Spine skeletons; 15 frame sequences (290 frames); 3 fonts. Grouped into 27 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

An Irish-luck slot built as a small stage set: one laughing leprechaun, a wooden signboard of reels in a wobbly gold frame, five pots waiting under it and five jackpot banners above, on a dark clover field that turns purple under a rainbow for the features.

**Style.** Chunky 3D-look casino illustration with storybook proportions: rounded props (mug, pipe, barrel, boot, mushroom, pots), a big-headed family-animation character, and fairground lettering. The backdrop is a flat pattern, not a landscape. Nothing is straight: the frame, the board's outline and the banners all wobble or curl.

**Rendering.** Smooth airbrushed volumes with hard outer edges for every object (soft edge 0.05 to 0.2: character 0.059, pipe 0.051, jackpot banners 0.114, high symbols 0.197), a green rim light under most props, and soft light for everything magical (rainbow effects 0.941, sparkles 0.825, bursts 0.827). Lettering has a two-tone face with a hard horizon, a thick rim and an extruded side.

**Colour.** Dark green and dark purple fields under gold and a full rainbow. Measured over the art files: near-black green #0b290b 17%, near-white #fcfbf7 11% (white effect sprites the game tints), dark magenta #36082e 10%, gold-orange #f2bb19 7%, wood brown #682b16 6%, purple #550867 3%, green #0c750e 2%. Gold marks what pays (coins, pots, WILD, frame, jackpot names); the rainbow marks what is magic (ribbon, progress meter, Collector panel, Jackpot Coin, transitions); and a five-step rainbow scale ranks things: purple, blue, green, red and gold for the royals and for the jackpot banners.

**Lighting.** Objects are lit from the top or top-right with a green bounce from below, as if standing in the clover field. The backdrop is darkest in the middle so the board glows against it. In the feature scene the light source is the rainbow ribbon itself.

**Ambience.** Cosy, lucky and good-humoured: a pub sign in a clover patch at night. The feature scene is the same place enchanted, not a different world.

**Shape language.** The heart-shaped clover leaf is the module: backdrop leaves, the coin's stamp, the Scatter, the pipe's badge, the hat, the particles. Round bellies (pots, mug, barrel, coins, the character) against a thin wavy frame line; the curled scroll for jackpots; the arc for rainbows. The only sharp shape is the Booster arrow.

**Materials.** Polished gold, cast iron, varnished wood, leather, felt, enamel and coloured glass, foam and beer, waxy leaves, light.

**Typography and lettering.** Four voices. The logo and jackpot names: gold serif capitals with a brown side. WILD, SCATTER, BOOST, FREE SPINS and the other headlines: a curly western poster face in yellow and orange with a red rim; captions in the same face in white with a wine outline, written as rhymes. Win tiers: tall flared capitals, dark with a neon outline. Numbers: the provider's bitmap fonts, Ultra in cream and gold (jackpot values, win amounts) and in purple and gold, and Ravie in yellow with a rainbow side (the Spin Progress counter). The low symbols 10 to A are fat slab serifs in single colours. Small interface text is the shell's Poppins (Regular, SemiBold, Bold).

**Motion.** All motion is Spine 4.2.43: 64 skeletons in one bundle file, plus 15 hand-drawn frame sequences (290 frames): five of white sparkle and smoke (112 frames), two of rainbow (45), two of white bursts (33), two of the pots (34), three coin and coin-shine sequences (45) and the GRAND highlight (21). The leprechaun is a 55-bone rig with separate eyes, brows, moustache, coat halves and limbs; the mug's effect has 51 bones; the big-win banner 92. Seen in play: the leprechaun standing large in front of the board as the game opens; a full mug over a reel and beer running down whole reels as stacked WILDs with foam on top; coins dropping from Golden Coins towards the pots; a thin line across a winning row with the amount in cream and gold numerals; FEATURE UNLOCKED over a small copy of the board when the Spin Progress counter reaches zero; the 10 FREE SPINS splash over a white burst; a rainbow wash across the whole screen into the purple scene; a large mug with WILD over the board before Wild Reels; +5 FREE SPINS on a retrigger; BIG WIN on its wooden plaque over a violet haze with Golden Coins tumbling across the screen. No skeleton frame is shown in this report, because the project's renderer is written for Spine 3.7.

**Variants and themes.** Two states of the whole stage from two backdrops and one tinted board (skins normal and special; holdAndWin for the board): green for the base game, purple with coloured clovers and a rainbow ribbon for Free Spins (seen) and, by the skin names, the Hold & Win. Frame in two states (gold; white with rainbow glow). Pots in two states with a 14-frame change. One character at two crops (1x2 symbol and full reel). Five jackpot banners as two mirrored shapes in four colours plus the Grand. Splashes in a normal and an upgraded skin.

**How it is built.** Two 4096 px atlas pages hold 442 sprites, 290 of them animation frames, with 18 localised lettering files (en-GB), six loose textures and one skeleton bundle. The two backdrops are 1375x1255 pictures; the reel board ships in grey and is tinted. Symbols are layered where they move (mug in ten parts, Booster in four, coins with turn and shine frames) and single pictures where they do not (royals, the four props). Paytable pictures, the flattened logo, the numeral fonts and the interface come from the provider's shared services.

**Consistency.** High. One clover module, one gold, one rainbow and one wobbling line run through backdrop, frame, symbols, interface and effects, and the green rim light ties the painted props to the green field. Seams: the win-tier lettering (dark with a neon outline) and the flat cartoon smoke are drawn in other hands than the gold-and-enamel world around them, and the white bursts are generic.

**What to take from it.** (1) One character, used twice. The leprechaun is a single 55-bone rig of 20 small parts that serves as the intro figure, the 1x2 Collector and the full-reel Collector; there is no separate mascot beside the reels. For our packages: design the character as a symbol first and reuse the rig. (2) A theme can stand on a pattern instead of a painted scene. The backdrop is a dark lattice of shamrocks with a dozen loose leaves on bones; the second scene is the same layout in purple with a rainbow ribbon. Two 1375 px pictures and 11 leaf sprites make both stages, which is well within what image generation and a rig can deliver. (3) Ship neutral, tint in the game: the reel board is a grey wood picture coloured per state, and every sparkle and burst is white. One picture then serves the base game, Free Spins and the Hold & Win. (4) Let one cheap motif carry the brand: the heart-leaf clover is on the coin, the pipe, the hat, the Scatter, the backdrop and the confetti. A module like this keeps generated pieces looking like one game. (5) Use colour as a scale as well as a theme: the same five rainbow steps rank the royals and the jackpots, gold means payment and the rainbow means magic. (6) The persistent unlock meter costs little art: five flat pictograms, a watch, a ribbon and six caption files give the game its long-term structure (five features unlocked over 10, 25, 50, 75 and 100 spins, the game's rules). (7) Anticipation art without mechanics: the pots fill with gold and grow rainbows in 14 and 20 drawn frames although, as the rules say, this has no influence on the trigger. It is a place where animation budget buys excitement directly. (8) Spend drawn frames on reusable white effects: 145 of the 290 frames are white sparkle, smoke and bursts that rigs tint and place on symbols, pots, jackpots and the backdrop. (9) From the same provider and framework as Fire Rail Express, 777 Hot Reels, Mega Cash Boost and Super Cash Boost (same shell, Poppins, Double Chance card, one skeleton bundle in Spine 4.2.43, packed 4096 px pages): of the five, this is the one with a character and a painted prop set, which shows the framework carries an illustrated theme as easily as a neon one.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 44% · saturation 68% · contrast 53% · warm 49% / cool 22% · brighter towards: top (46), top-right (27), bottom-right (18)

Palette: #0b290b black 18%, #fcfbf7 light yellow 12%, #36082e dark magenta 10%, #f2bb19 orange 8%, #6c6567 grey 7%, #682b16 brown 6%, #550867 dark purple 3%, #0c750e dark green 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 15% | 93% | 32% | 20% / 46% | #072a0b black 50%, #310436 black 25%, #4a0570 dark purple 6% |
| Reel board | 1 | 67% | 8% | 49% | 4% / 3% | #686868 grey 44%, #fffffe light orange 42%, #00ff25 green 3% |
| Symbols | 8 | 56% | 73% | 62% | 72% / 14% | #f2bc15 gold 19%, #391a06 brown 13%, #fbf8ef light orange 11% |
| Characters | 1 | 43% | 81% | 50% | 35% / 44% | #183307 black 28%, #a14bfc purple 14%, #2f720a dark green 8% |
| Logo and title | 2 | 48% | 82% | 69% | 56% / 27% | #03341f black 36%, #f3d660 gold 15%, #d9a40c orange 13% |
| Win celebrations and banners | 2 | 46% | 60% | 74% | 82% / 15% | #581d1b dark red 25%, #f9f5f6 light red 11%, #976a79 red 9% |
| Effects | 5 | 71% | 42% | 30% | 43% / 27% | #f8fcfa light cyan 28%, #a4e5fb light cyan 10%, #d07450 orange 9% |
| Game interface | 3 | 48% | 86% | 61% | 81% / 11% | #df8e10 orange 29%, #8e4a05 brown 24%, #f4d032 gold 9% |
| Typography | 2 | 59% | 66% | 81% | 91% / 1% | #f8eed4 light orange 15%, #f8ee84 gold 14%, #d98011 orange 12% |
| Provider interface (shared) | 2 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backdrops: green clover field and purple rainbow night

`backgrounds` · atlas · 13 parts · largest 1375×1255 · sheet `sheets/backgrounds.webp`

- **Role:** The two full-screen backdrops (bgNormal for the base game, bgSpecial for the intro and, by its skin name and the frame's FS parts, the features) and the loose leaves and branches that move over them.
- **Subject:** A dark green field quilted with a faint diamond lattice of shamrocks, ringed by large clover leaves and twigs; and a dark purple field with the same lattice, crossed by a glowing rainbow ribbon and ringed by blue, purple, pink and yellow clovers.
- **Style:** Flat decorative pattern in the middle, soft 3D-look foliage at the edges: a stage curtain rather than a landscape. There is no horizon, sky or ground.
- **Rendering:** The leaves are smooth gradient shapes with one sharp crease and hard edges (soft edge 0.007 for the unit); each leaf lobe is a separate heart shape. The rainbow ribbon is a blurred light trail.
- **Colour:** Two near-black fields: green #072a0b 50% and purple #310436 25%, with #037910 and #4a0570 as the lit leaf colours. Brightness 0.153, saturation 0.931: very dark and very saturated.
- **Lighting:** The centre is darker and plainer so the board stands out; the leaves glow as if lit from the screen itself.
- **Ambience:** A clover patch at night, calm and lush; the purple version is the same place under a spell.
- **Materials:** Waxy leaves, thin brown twigs, light.
- **Variants:** Two backdrops of 1375x1255 (normal, special), three- and four-leaf lobes in green, blue-violet, yellow-orange, pink and purple, three green branches and two bare ones. The skeletons carry the same two skins, normal and special.
- **Motion:** BackgroundEffects (44 bones, 50 slots; skins normal and special) moves the leaves and branches: branches 4.5 s, clovers 3.17 s, glow 3.33 s. BackgroundsReactions has a level0 to level5 loop (4 s down to 2 s) and a levelUp of 1.17 s, so the backdrop reacts faster as the Spin Progress level rises (inference from the names and lengths).
- **Construction:** One 1375x1255 picture per state, stretched to the screen, plus 11 loose leaf and branch sprites animated by bones. The purple scene's rainbow is painted into bgSpecial.
- **Notes:** The backdrop is the cheapest large piece of the game: a pattern, a vignette and a dozen leaves.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 15% · saturation 93% · contrast 32% · warm 20% / cool 46% · brighter towards: top-left (3), bottom-left (3), bottom-right (3)
- **Palette (measured):** #072a0b black 50%, #310436 black 25%, #4a0570 dark purple 6%, #037910 dark green 6%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board: wooden panel in a wavy gold frame

`reel-board` · atlas · 22 parts · largest 1173×730 · sheet `sheets/reel-board.webp`

- **Role:** The 5x3 reel area: its backing, mask, frame in two states, dividers, the empty cell of the Hold & Win and the win line.
- **Subject:** A board of wood grain with an irregular, hand-cut outline; a thin gold frame line that bulges at the middle of each side, with a sprig of clover at each top corner; hairline dividers; a small wooden diamond tile for an empty cell.
- **Style:** Storybook signboard: nothing is straight, every edge wobbles a little.
- **Rendering:** The backing (slotBg, 1173x730) ships as a grey wood-grain picture, so the game colours it (on screen it is red-brown, and purple-brown on the first spins); the frame is a hard-edged gold line with a white core. The unit measures grey #686868 44% and white 42% because of the grey backing, the white mask and the guides.
- **Colour:** In the files: grey wood, gold line, and for the feature frame a white-pink-orange line with a magenta glow (slotFrameFSGlow). On screen: red-brown wood inside gold on the green field.
- **Lighting:** Flat; the frame has its own thin highlight. The FS glow pieces are soft white strips meant to be tinted and added.
- **Ambience:** Hand-made and warm; a pub sign among the leaves.
- **Materials:** Carved wood, a gold wire frame, living clover on the corners.
- **Variants:** Frame in two states, Normal (gold with a green underside) and FS (white and rainbow-tinted, with glow strips); four slightly different dividers; SlotBackgrounds has three skins: normal, special and holdAndWin.
- **Motion:** SlotFrame (15 bones) idles in 2.25 s; SlotTransition plays 3.33 s with a rainbow strip, coins, fireworks and the pots; LevelUpReelSplash sweeps a rainbow strip over a reel in 0.75 s; SpinEffect 0.67 s; ReelAnticipation loops clovers over a reel in 1 s; WinLine (39 bones) bends winLine1, a 1920x100 strip, along the paying line in 1 s. In play a win showed thin lines across the paying symbols with the amount in cream and gold numerals; the help page shows the line as a rainbow stripe (the line and lineEnd textures are 16x14 rainbow pieces).
- **Construction:** The frame is built from one side piece, one top and one bottom piece, mirrored; the backing is one grey picture tinted per state; reelsMask is a white picture of the board's outline. tileGuide (a pure green 218x218 square), whiteBox and glowSquare are helpers.
- **Notes:** Shipping the wood in grey and tinting it is how one picture serves the base game, the features and the Hold & Win.
- **Measured:** bright, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 67% · saturation 8% · contrast 49% · warm 4% / cool 3% · brighter towards: top (4), bottom-right (2), top-right (2)
- **Palette (measured):** #686868 grey 44%, #fffffe light orange 42%, #00ff25 green 3%, #060706 black 2%, #383e34 grey 2%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Paytable pictures of the 17 symbols

`help-symbol-pictures` · atlas · 17 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The 225x225 pictures the provider's shell shows in HELP, one per symbol id (tile1 to tile17), served from the shared asset service and not from the game's atlas.
- **Subject:** 10, J, Q, K, A; a barrel, a buckled boot, a red mushroom, a horseshoe; the beer-mug WILD; the gold clover coin; the leprechaun's head in a gold frame (tile12) and his whole figure (tile17); the rainbow JACKPOT coin; the empty wooden diamond (tile14); the clover SCATTER; the red BOOST arrow.
- **Style:** Glossy casino illustration with a 3D look: rounded volumes, gold trims, heavy lettering with an extruded side.
- **Rendering:** Each symbol is flattened to one picture, composed as it lands on the reel (mug with foam and the word, coin with its rim glow). Measured soft edge 0.201, contrast 0.699.
- **Colour:** Gold and orange lead (#f1b81b 12%, #bb420d 8%) over dark brown (#321f07, #732e12) with clover green (#3f8318). Each royal has its own colour: purple 10, blue J, green Q, orange-red K, yellow A.
- **Lighting:** Lit from the top and top-right (8 of 10 measured parts), with a coloured rim on the shadow side of the objects.
- **Ambience:** A lucky-charm drawer: Irish folk objects made shiny.
- **Materials:** Polished gold, glazed coloured lettering, varnished wood, leather, glass-like clover leaves, a soft mushroom cap.
- **Variants:** 17 stills, one per symbol id; tile12 and tile17 are the same character at two crops.
- **Motion:** None: stills for the help pages.
- **Construction:** 17 separate WebP files of 225x225, flattened copies of the layered symbols in the atlas.
- **Notes:** They give the symbol ids their meaning: the atlas names the symbols only as tile1 to tile16.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 46% · saturation 77% · contrast 70% · warm 66% / cool 22% · brighter towards: top-right (4), top (4), right (2)
- **Palette (measured):** #321f07 black 17%, #f1b81b orange 12%, #3f8318 green 8%, #bb420d orange 8%, #732e12 brown 8%, #f3f1e5 light yellow 4%

### Wild: the beer mug

`symbol-wild` · atlas · 13 parts · largest 349×412 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol (tile10). With Wild Reels unlocked it fills whole reels (the game's rules); it is also the picture of the first unlock splash.
- **Subject:** A wooden tankard with gold hoops and a carved handle, overflowing with cream foam, and the word WILD in yellow capitals with a red outline; a clover hangs on the word.
- **Style:** The same chunky 3D-look props as the high symbols, with comic foam.
- **Rendering:** Airbrushed wood and gold with hard edges; the foam is a cluster of soft bubbles with a yellow-green rim; the beer itself is a flat yellow strip with fine bubbles (tile10BeerLenght, 210x361) made to be stretched. Measured soft edge 0.164.
- **Colour:** Beer yellow #f6c10f 26%, wood brown #4b1908 24%, foam cream #f5ecd4 20%; warm 0.918. WILD is yellow with a red rim.
- **Lighting:** Top light on the mug and foam; the word has a light upper half and an orange lower half.
- **Ambience:** Pub cheer; the most generous-looking object on the reels.
- **Materials:** Wood, brass, liquid, foam, a glass bubble (beerBubble).
- **Variants:** Mug body, handle, foam cap, beer column with foam top, beer strip, three foam blobs, a drop streak, a bubble, the word and its clover; TileWild has three skins (skin0 to skin2).
- **Motion:** TileWild (6 bones): show 0.5 s, loop 1 s, win 0.58 s, using the word and three foam blobs. TileWildEffect (51 bones, 54 slots) is the mug itself: activate 0.5 s, activateSplash 1.67 s, levelUpSplash 3.33 s, loop 1.67 s, hide 0.67 s. In play, a full mug stood over reel 5 on the first spins and, on the unlock splash, beer filled a 3x3 block of WILD cells. That the many bones pour the beer down a reel is inference from the stretchable strip and the bone count.
- **Construction:** 13 sprites: the mug is 349x412, larger than a cell, in separate body, handle, foam and liquid layers so it can tip and pour; foamTrail is a separate 87x99 texture for a trail.
- **Notes:** The strip is spelt tile10BeerLenght in the game's files.
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 58% · saturation 70% · contrast 52% · warm 92% / cool 3% · brighter towards: top (2), bottom-right (1), right (1)
- **Palette (measured):** #f6c10f gold 26%, #4b1908 brown 24%, #f5ecd4 light orange 20%, #844c19 brown 6%, #dbc49b orange 6%, #df790d orange 4%

### Jackpot Coin

`symbol-jackpot-coin` · atlas · 15 parts · largest 350×357 · sheet `sheets/symbol-jackpot-coin.webp`

- **Role:** The jackpot symbol of the Hold & Win (tile13): it lands as a coin and reveals a jackpot's name (the game's rules).
- **Subject:** The clover coin again, with its four heart leaves enamelled green, red, blue and purple inside a gold rim, on a rainbow disc, with the word JACKPOT across it.
- **Style:** The Golden Coin's design recoloured as cloisonne enamel.
- **Rendering:** Hard-edged (soft edge 0.102): a bevelled gold rim, flat glossy enamel leaves with a highlight each, a full-spectrum gradient disc behind (tile13Plate, 350x357) with a soft orange edge.
- **Colour:** Gold #f1ae1d 18% with pure spectrum accents: yellow #f8e60d, cyan #06b4dc, red #f61825. Saturation 0.791.
- **Lighting:** Highlights on the lower right of the rim (4 of 6 measured parts), as on the Golden Coin.
- **Ambience:** The rare, magic version of the everyday coin.
- **Materials:** Gold and coloured enamel or glass.
- **Variants:** Still coin (tile13Coin), rainbow plate, the word, and a 12-frame turning coin; TileJackpot has four skins that swap the word for MINI, MINOR, MAJOR or MAXI lettering from the jackpot panel.
- **Motion:** One frame sequence, jackpotCoin (12 frames, a full turn; ParticleCoinJackpot loops it in 0.4 s). TileJackpot: onLand 0.5 s, loop 1 s, activate 2.17 s, collect 0.83 s. Not seen in play: the jackpots stayed locked.
- **Construction:** 15 sprites; coin, plate and word are separate so the word can be swapped by skin.
- **Notes:** It uses the five jackpot colours on one coin, which ties it to the banners above the reels.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 60% · saturation 79% · contrast 63% · warm 66% / cool 25% · brighter towards: bottom-right (4), top (1), right (1)
- **Palette (measured):** #f1ae1d orange 18%, #f8e60d gold 7%, #06b4dc cyan 7%, #f8db6f gold 7%, #dc730a orange 6%, #4f1404 dark red 4%

### Bonus Booster arrow

`symbol-booster` · atlas · 4 parts · largest 291×356 · sheet `sheets/symbol-booster.webp`

- **Role:** The Booster (tile16): once unlocked at level 5 it raises the multiplier of the Hold & Win or the Free Spins by x0.5 (the game's rules).
- **Subject:** A red arrow with a gold rim bending upwards like a ribbon, a gold clover on its head, and the word BOOST.
- **Style:** A sign-painter's arrow given thickness, folded in two planes.
- **Rendering:** Hard-edged (soft edge 0.119): flat red planes with a soft gradient, a bevelled gold border, a green rim at the foot; the back fold and a soft grey shadow are separate sprites.
- **Colour:** Red #ee0c01 and dark red #900f04 with gold #d78509, #fad31a; saturation 0.932, warm 0.946.
- **Lighting:** Lit from the top-left (2 of 2 measured parts).
- **Ambience:** Urgent and upward: the one aggressive shape in a soft game.
- **Materials:** Enamelled metal with a gold edge.
- **Variants:** Front fold, back fold, shadow, word.
- **Motion:** TileBooster (8 bones): onLand 0.5 s, loop 1 s, loopLevelUp 1 s, activate 0.92 s. Not seen in play (level 5 was not reached).
- **Construction:** Four sprites; the same arrow is a small yellow icon on the Spin Progress meter (featureIconArrow).
- **Notes:** Red is otherwise rare on the reels (the mushroom, the K), so the arrow reads at once.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 46% · saturation 93% · contrast 71% · warm 95% / cool 2% · brighter towards: top-left (2)
- **Palette (measured):** #d78509 orange 24%, #900f04 dark red 14%, #fad31a gold 14%, #ee0c01 red 12%, #391004 black 9%, #fce94e gold 8%

### Golden Coin (Cash Prize)

`symbol-golden-coin` · atlas · 34 parts · largest 272×288 · sheet `sheets/symbol-golden-coin.webp`

- **Role:** The cash symbol (tile11): it carries a prize of 1x to 10x and throws a coin towards the pot under its reel (the game's rules).
- **Subject:** A gold coin stamped with a four-leaf clover made of four hearts, seen face-on, and the same coin turning in the air.
- **Style:** Polished 3D coin, simple and heraldic.
- **Rendering:** A lathe-turned look: a raised rim, a brushed face with diagonal light bands, an embossed clover. The glow frames are grey-white copies of the face meant to be added over it. Measured soft edge 0.318, strong highlights.
- **Colour:** Gold only: #d89a0e 35%, #f6cd3c 12%, #fade7c, with brown shadow #532102; hues orange 0.677 and yellow 0.323, cool 0.002.
- **Lighting:** A light band crosses the face from the top-left to the bottom-right; the glow sequence moves that band.
- **Ambience:** Treasure: the object the whole game is about collecting.
- **Materials:** Polished and brushed gold.
- **Variants:** The reel coin (tile11, 272x288, with a green foot shadow), a 13-frame turning coin (coin_00 to coin_12, 166 px), a 20-frame shine (tile11Glow).
- **Motion:** Two frame sequences: coin (13 frames, a full turn; ParticleCoin loops it in 0.4 s) and tile11Glow (20 frames, a light sweep; TileCashGlow loops in 1.32 s). TileCash: onLand 0.5 s, loop 1 s, upgrade 0.5 s, collect 0.83 s. In play the landed coins showed their value on the face and small coins fell to the pots.
- **Construction:** 34 sprites, 33 of them animation frames. The value is drawn by a bitmap font over the coin.
- **Notes:** The heart-leaf clover stamp is the game's mark: it is on the coins, the pipe, the hat and the jackpot coin.
- **Measured:** bright, saturated, warm, medium contrast, strong highlights · brightness 72% · saturation 60% · contrast 51% · warm 72% / cool 0% · brighter towards: bottom-right (4), top-left (1), top-right (1)
- **Palette (measured):** #d89a0e orange 35%, #fffefb light orange 32%, #f6cd3c gold 12%, #532102 brown 7%, #995507 brown 7%, #fade7c gold 4%

### Low symbols: 10, J, Q, K, A

`symbols-royals` · atlas · 5 parts · largest 184×172 · sheet `sheets/symbols-royals.webp`

- **Role:** The five low-paying symbols (tile1 to tile5).
- **Subject:** Five fat serif characters, each tilted back as if standing on the reel, with a contrasting coloured side.
- **Style:** Circus-poster slab serif turned into moulded 3D letters; no ornament, no clover on them.
- **Rendering:** A smooth face with a soft inner bevel and a thin lighter outline, then an extruded side in a second colour (purple under the yellow A, green under the purple 10 and the blue J, blue-green under the Q, purple under the K). Measured soft edge 0.301.
- **Colour:** One colour per letter: purple 10 (#9231b8), blue J (#256aa3), green Q (#438e19), orange-red K (#c23b07), yellow A (#f5b610). Warm 0.405 against cool 0.462, the only symbol unit that is balanced.
- **Lighting:** Lit from the top (3 of 4 measured parts); the face is lighter towards its upper edge.
- **Ambience:** Friendly and toy-like; they recede behind the picture symbols because they carry no gold.
- **Materials:** Matt moulded plastic or painted wood; no metal.
- **Variants:** Five letters, one piece each.
- **Motion:** One skeleton holds all five (TileContainerJuniors, skins tile1 to tile5: onLand 0.42 s, win 0.58 s, transformStart 0.5 s and transformStop 0.42 s for the Pipe Swap). It uses coloredSmoke and a white glow besides the letter. No frame sequence.
- **Construction:** One sprite per letter, 119 to 184 px wide and 163 to 178 px high.
- **Notes:** The two-colour extrusion repeats the rainbow idea in the cheapest symbols: every letter shows two rainbow colours.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 37% · saturation 85% · contrast 52% · warm 40% / cool 46% · brighter towards: top (3), top-right (1)
- **Palette (measured):** #261c06 black 16%, #9231b8 purple 13%, #438e19 green 12%, #f5b610 orange 10%, #c23b07 orange 9%, #256aa3 blue 6%

### Scatter: the gold-rimmed clover

`symbol-scatter` · atlas · 2 parts · largest 308×264 · sheet `sheets/symbol-scatter.webp`

- **Role:** The Scatter (tile15): three on reels 1, 3 and 5 start 10 Free Spins (the game's rules).
- **Subject:** A four-leaf clover of dark green glass leaves set in a thick gold rim, lying at a three-quarter angle, with the word SCATTER in yellow capitals with a red outline.
- **Style:** Jewellery: the clover as a brooch.
- **Rendering:** Faceted glossy leaves with white speculars inside a bevelled gold setting. Contrast 0.819, the highest of the symbols.
- **Colour:** Gold #f2ca1d 17% around greens #0d4806, #237e14 and a bright #15ce0f; the word is yellow on dark red #461204.
- **Lighting:** Lit from the top, with light passing through the leaves near the centre.
- **Ambience:** Precious and lucky.
- **Materials:** Green glass or emerald, polished gold.
- **Variants:** Clover (308x264) and word (255x71).
- **Motion:** TileFreeSpins (18 bones, 14 slots): onLand 0.5 s, loop 1 s, show 0.67 s, activate 1.33 s, with circularRainbowRays, magicSparks and a blink star. In play the landed Scatter glowed green with the word under it.
- **Construction:** Two sprites; the word is separate.
- **Notes:** WILD, SCATTER and BOOST share one lettering: yellow face, orange lower half, red rim.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 51% · saturation 82% · contrast 82% · warm 48% / cool 26% · brighter towards: top (1)
- **Palette (measured):** #f2ca1d gold 17%, #0d4806 dark green 14%, #237e14 dark green 12%, #461204 dark red 10%, #15ce0f green 8%, #a95b09 brown 7%

### High symbols: barrel, boot, mushroom, horseshoe

`symbols-premium` · atlas · 4 parts · largest 247×254 · sheet `sheets/symbols-premium.webp`

- **Role:** The four higher-paying picture symbols (tile6 to tile9).
- **Subject:** A wooden barrel with gold hoops lying on its side, a leprechaun's plum-coloured boot with a gold buckle, a red-capped mushroom seen from below, a silver horseshoe.
- **Style:** Stylised 3D-look props, chunky and rounded, seen from a three-quarter angle.
- **Rendering:** Smooth airbrushed volumes with hard outer edges (soft edge 0.197), strong speculars and a green rim light on the lower edge of every object.
- **Colour:** Each object its own hue: wood brown (#361c0b, #bf855d), plum (#6c3026), red cap (#f3302a) with a cream stem (#eff2ef), pale cyan steel (#add5ce, #6fa399). Contrast 0.796, the highest among the reel symbols with the Scatter.
- **Lighting:** Lit from the top-right (2 of 3 measured parts) and rimmed in green from below, as if the green backdrop reflected on them.
- **Ambience:** Storybook Irish props; cosy and a little comic.
- **Materials:** Varnished staves and brass hoops, soft leather, a wet glossy cap with gills, brushed steel.
- **Variants:** Four objects, one piece each.
- **Motion:** One skeleton holds all four (TileContainerSeniors, skins tile6 to tile9: onLand 0.42 s, win 0.58 s, transformStart 0.5 s, transformStop 0.42 s). It adds circularWhiteRays2, coloredSmoke and a white glow. No frame sequence.
- **Construction:** One sprite per object, 213 to 247 px wide: larger than the letters, so they overlap the cell edges on screen (seen in play).
- **Notes:** No high symbol is gold: gold is kept for the coins, the Wild's word and the frame.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 44% · saturation 60% · contrast 80% · warm 66% / cool 20% · brighter towards: top-right (2), right (1)
- **Palette (measured):** #361c0b brown 25%, #6c3026 dark red 14%, #eff2ef light green 10%, #bf855d orange 10%, #add5ce light cyan 4%, #6fa399 cyan 3%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The Lucky Fella: the leprechaun (Collector)

`leprechaun-collector` · atlas · 27 parts · largest 226×649 · sheet `sheets/leprechaun-collector.webp`

- **Role:** The game's one character. He is the Collector symbol: 1x2 in the base game (tile12) and a whole reel above an active pot in the Hold & Win (tile17), collecting every prize on the reels (the game's rules). He also stands on the intro screen and, large, in front of the board during the opening sequence (real screens).
- **Subject:** A stout, laughing leprechaun with an orange beard and moustache, big ears and green eyes, in a tall green top hat with a gold buckle and a clover, a green tailcoat with white cuffs over a dark waistcoat with a buckled belt, striped green stockings and brown buckled shoes. He stands on a rainbow panel inside a thin gold frame.
- **Style:** Family-animation character design with a 3D look: a large head, a small body, round forms, a friendly open smile.
- **Rendering:** Smooth airbrushed volumes with hard outer edges (soft edge 0.059), fine strokes only in the beard and brows, glossy highlights on hat, buckle and shoes. His backing (tile12PlateBg, 226x649) is a vertical rainbow gradient with sparkles.
- **Colour:** Greens #183307 28% and #2f720a 8% with the rainbow panel's purple #a14bfc 14% and leather brown #582b0a; the beard is orange. Hues: green 0.486, orange 0.264, purple 0.159.
- **Lighting:** Lit from the top-right (5 of 10 measured parts), with a yellow-green rim on hat and coat.
- **Ambience:** Jolly, harmless, generous: a host rather than a trickster.
- **Materials:** Felt hat and coat, leather belt and shoes, gold buckles, knitted stockings, hair.
- **Variants:** One figure in 20 body parts; a green ghost of the whole figure for a glow (tile12Glow); the same parts are used by two rigs, TileCollector12 (the 1x2 symbol) and TileCollector17 (the full-reel Collector).
- **Motion:** Two Spine 4.2.43 rigs of 55 bones each: TileCollector12 (onLand 0.75 s, loop 1 s, loopLevelUp 1 s, collect 1 s, win 0.75 s) and TileCollector17 (show 1.17 s, showLabel 1 s, loop 1 s, loopEmpty 2 s, loopSplash 1 s, collect 1 s, win 0.75 s, winJackpot 1.75 s). Eyes, irises, brows, moustache, nose, hat front and back, coat halves, arms, hand and legs are separate, so the face can blink, look and laugh and the body can bounce. No frame of the rig is drawn here: the project's renderer does not read Spine 4.x; the real screens show him whole.
- **Construction:** 27 sprites: 20 body parts (the face 321x267 is the largest), the rainbow panel, four gold frame strips and the glow. The parts are small: the whole figure is about 360 px high in the atlas.
- **Notes:** The only character art in the game is one rig used at two crops, on the intro and as a symbol; there is no separate mascot beside the reels.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 43% · saturation 81% · contrast 50% · warm 35% / cool 44% · brighter towards: top-right (5), bottom-right (3), top-left (2)
- **Palette (measured):** #183307 black 28%, #a14bfc purple 14%, #2f720a dark green 8%, #582b0a brown 4%


## Logo and title

The game's own wordmark.

### Logo, flattened for HELP

`help-logo` · atlas · 1 parts · largest 371×127 · sheet `sheets/help-logo.webp`

- **Role:** The 371x127 copy of the logo the provider's shell shows at the top of the help pages.
- **Subject:** The whole logo as one picture: gold words on the green arch, the gold ribbon and two clovers.
- **Style:** As the logo.
- **Rendering:** A reduced, flattened copy; hard-edged (soft edge 0.122).
- **Colour:** Dark green #102e13 28%, golds #d19f10 16%, #ddc152 12%, #f0e68b 11%.
- **Lighting:** As the logo.
- **Ambience:** As the logo.
- **Materials:** As the logo.
- **Variants:** One picture.
- **Motion:** None.
- **Construction:** One WebP from the provider's shared asset service, not from the game's atlas.
- **Notes:** It shows the logo complete, which the atlas only holds in parts.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 52% · saturation 74% · contrast 82% · warm 63% / cool 19%
- **Palette (measured):** #102e13 dark green 28%, #d19f10 orange 16%, #ddc152 gold 12%, #f0e68b gold 11%, #efe41d gold 7%, #4ea10d green 6%

### Logo: THE LUCKY FELLA, HOLD & WIN

`logo` · atlas · 7 parts · largest 654×356 · sheet `sheets/logo.webp`

- **Role:** The wordmark on the top edge of the reel frame, on the intro screen and (flattened) in HELP.
- **Subject:** THE LUCKY FELLA in gold serif capitals on a curved dark green plate with a gold edge, HOLD & WIN in dark green capitals on a gold ribbon below, a clover at each end of the ribbon.
- **Style:** A pub sign or a label: an arched nameplate over a ribbon.
- **Rendering:** The gold letters have a light-to-dark vertical gradient, a brown extruded side and a dark outline; the plate is a flat dark green with a double gold and green border; the ribbon is a simple folded band with a soft glow.
- **Colour:** Dark green #02341f 36%, golds #f4d760 15%, #daa40b 13% and #f6e606 7%, brown #4d1904, clover green #47a605.
- **Lighting:** Top-lit letters; a small star glint travels over them (blinkRealistic12 in the Logo skeleton).
- **Ambience:** Traditional and reassuring: the game's most sober piece.
- **Materials:** Enamel plate, gold lettering, satin ribbon.
- **Variants:** Seven parts: plate, ribbon plate, THE, LUCKY, FELLA, HOLD & WIN, a clover.
- **Motion:** Logo (15 bones, 19 slots): show 0.67 s, idle 1.83 s, splashLoop 2 s, hide 0.77 s. In the real screens the logo sits above the rainbow ribbon with the Spin Progress counter under it.
- **Construction:** Each word is its own sprite (THE 271x127, LUCKY 470x146, FELLA 427x139), so the words can arrive one by one; the plate is 654x356.
- **Notes:** Green and gold only: the rainbow is kept out of the logo and carried by the ribbon behind it.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 47% · saturation 83% · contrast 68% · warm 56% / cool 28% · brighter towards: bottom (1), top-left (1), top (1)
- **Palette (measured):** #02341f black 36%, #f4d760 gold 15%, #daa40b orange 13%, #4d1904 brown 7%, #f6e606 gold 7%, #47a605 green 4%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature lettering (en-GB)

`feature-lettering` · atlas · 17 parts · largest 1114×237 · sheet `sheets/feature-lettering.webp`

- **Role:** The localised words of the splashes and labels: FEATURE UNLOCKED and its five captions, FREE SPINS, BONUS GAME, MORE FOR THE GRAND JACKPOT, HOLD & WIN and FREE SPINS for the multiplier badge, UNLOCK.
- **Subject:** Two kinds of lettering in one curly western face: headline words in yellow with an orange lower half and a red-pink rim, and caption lines in white with a dark wine outline, such as FROM MUG TO REEL, WILD WINS REVEAL! and PUFF O' SMOKE, SYMBOLS TRANSFORMED - LUCK AWOKE!
- **Style:** Fairground poster capitals with forked serifs; rhymed two-line captions.
- **Rendering:** Headlines: a two-tone face with a hard horizon, a thick rim and a dark drop side. Captions: flat white with a thick dark outline and a soft shadow (the unit's soft edge 0.308 comes from these shadows).
- **Colour:** White #f9f5f6 20% and wine #5b0d1d 16% for captions; gold #f6c516 and orange #d28c31 for headlines. Warm 0.988.
- **Lighting:** Headlines top-lit; captions unlit.
- **Ambience:** A barker's patter: cheerful, rhyming, a little old-fashioned.
- **Materials:** Painted sign lettering.
- **Variants:** 17 files: five unlock captions, two feature captions, three headline labels, one anticipation label, UNLOCK, and five single words (HOLD, &, WIN, FREE, SPINS) at 287x104 for the multiplier badge.
- **Motion:** LevelUpSplash (54 bones; skins level0 to level4): show 4.33 s, addTiles 2 s. FreeSpinsSplash show 1.67 s, HoldAndWinSplash show 2.33 s, each with skins normal and upgraded. In play: FEATURE UNLOCKED with the mug and its caption over a small copy of the board, and 10 FREE SPINS with the pipe, the mug and WILDS & PUFFS INCREASED WHEN UNLOCKED! over the dimmed game and a white burst.
- **Construction:** One WebP per phrase, most on a 1114 px wide canvas, in a localised folder (only en-GB was loaded), so a language is 17 small files.
- **Notes:** The splash skeletons come in a normal and an upgraded skin, for the Bonus Booster's multiplier (inference from the skin names and the rules).
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 56% · saturation 52% · contrast 85% · warm 99% / cool 0% · brighter towards: top (2), top-left (1)
- **Palette (measured):** #f9f5f6 light red 20%, #5b0d1d dark red 16%, #986a78 red 13%, #d28c31 orange 10%, #f6c516 gold 9%, #c2a7af red 8%

### Win tiers: BIG WIN, SUPER WIN, MEGA WIN, TOTAL WIN

`win-tiers` · atlas · 7 parts · largest 1114×507 · sheet `sheets/win-tiers.webp`

- **Role:** The big-win banner in three tiers and the total-win word, with the wooden plate the amount stands on.
- **Subject:** Two-line words in tall, flared serif capitals with a dark face and a glowing coloured outline; a wide wooden plaque with slanted ends and a thin gold frame.
- **Style:** Neon-outlined saloon lettering: the game's one use of dark letters with a light rim, the opposite of the gold words elsewhere.
- **Rendering:** A dark purple face with a faint inner gradient, a gold inner line and a soft outer glow in the tier colour; the plaque is brown wood grain with hard edges. Measured brightness 0.333, the darkest lettering unit.
- **Colour:** Dark purple faces #290f47 20%, wood #562519 33%, gold lines #efbe46 and #ece189; the glow is purple for BIG, blue #353cf3 for SUPER, orange #f46f09 for MEGA and magenta-pink #d3077f for TOTAL WIN.
- **Lighting:** Self-lit outlines; no top light.
- **Ambience:** Night-fair signage; it suits the purple feature scene.
- **Materials:** Neon tube around painted letters, a wooden plaque with a gold wire frame.
- **Variants:** Three tier words (452 to 718 px wide, 496 high) and TOTAL WIN (1114x507, localised); WinBig has skins label0 to label2.
- **Motion:** WinBig (92 bones, 59 slots): labelShow 1 s, sumShow 0.5 s, sumUpgrade 0.33 s, bangupEnd 1.33 s, hide 1 s, with clovers, explosion frames, a radial blur and white particles. WinTotal (24 bones): show 0.67 s, bangupEnd 0.67 s, hide 0.5 s, with rainbow rays. WinNormal and WinSmall only place the amount. In play, BIG WIN came once in Free Spins: the word with a purple glow on the wooden plaque, sprigs of clover on the plaque's top corners, the amount in cream and gold numerals under it, the game dimmed to a violet haze and Golden Coins tumbling across the screen. SUPER WIN and MEGA WIN were not reached.
- **Construction:** Seven sprites: three words, the localised total word, the plaque, half of its frame (mirrored) and a black square for the dimming.
- **Notes:** 92 bones for one banner: most of them carry clovers and particles, so the celebration is built from the game's small shared sprites, not from new art.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 33% · saturation 70% · contrast 62% · warm 62% / cool 33% · brighter towards: bottom-right (1), bottom (1)
- **Palette (measured):** #562519 dark red 33%, #290f47 dark purple 20%, #efbe46 orange 9%, #ece189 gold 8%, #522273 dark purple 5%, #353cf3 blue 4%


## Effects

Frame sequences, glows, particles and transitions.

### Magic sparkle and smoke

`magic-effects` · atlas · 113 parts · largest 298×297 · sheet `sheets/magic-effects.webp`

- **Role:** The sparkle trails, twinkle fields, halo and puffs of smoke used on symbols, pots, the backdrop and the Pipe Swap.
- **Subject:** Trails and clouds of tiny four-point sparkles; a white ring with a fine fringed corona; a cartoon puff of cream and yellow smoke with blobby lobes that breaks into wisps.
- **Style:** Classic fairy-dust effects; the smoke is drawn as flat cartoon blobs, unlike the painted props.
- **Rendering:** Soft and pale (soft edge 0.825, saturation 0.2, contrast 0.098): white and pale cyan dots made to be added and tinted. The smoke has clean flat shapes with a light rim.
- **Colour:** Near-white #eef5ed 43%, pale cyan #a5e5fb 31%, pale gold #f3e6b3 9%.
- **Lighting:** Self-lit.
- **Ambience:** Twinkling and gentle.
- **Materials:** Light, dust, smoke.
- **Variants:** Five frame sequences: bgMagicEffect1 (42 frames), magicSparks (32), coloredSmoke (14), effectMagic (12), effectMagic2 (12), and the still magicHalo (288x290).
- **Motion:** All hand-drawn frames, 112 of the 113 sprites. bgMagicEffect1 is the most reused: the backdrop's reactions, the jackpots, the Collector, the Scatter and the pots all play it. coloredSmoke is the Pipe Swap's puff and the symbols' transform (TileContainerJuniors and Seniors, transformStart 0.5 s).
- **Construction:** Small frames (the largest 298x297) packed on the two atlas pages; white so one sequence serves any colour.
- **Notes:** 42 frames for one sparkle trail is the game's largest single sequence.
- **Measured:** bright, muted, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 88% · saturation 20% · contrast 10% · warm 36% / cool 49%
- **Palette (measured):** #eef5ed light green 43%, #a5e5fb light cyan 31%, #c6c6b8 grey 13%, #f3e6b3 light gold 9%, #dfc764 gold 4%

### Bursts and fireworks

`bursts-and-fireworks` · atlas · 35 parts · largest 497×487 · sheet `sheets/bursts-and-fireworks.webp`

- **Role:** White flashes for landings, unlocks and wins.
- **Subject:** A round ray burst, a radial streak blur, a 10-frame pop that opens from a white blob into flying sparks, and a 23-frame scatter of twinkling stars.
- **Style:** Generic white effect sprites.
- **Rendering:** Pure white on clear (measured #ffffff 100%, saturation 0.0), soft (0.827), tinted and added by the game.
- **Colour:** White only in the files; the colour comes from the game's tint (inference from the pure white sprites).
- **Lighting:** Self-lit.
- **Ambience:** Punctuation: short, bright, neutral.
- **Materials:** Light.
- **Variants:** explosionEffect (10 frames), fireworkEffects (23 frames), circularWhiteRays2 (497x487), explosiveRadialBlur (390x378).
- **Motion:** Two frame sequences. Used by Jackpot (unlock), WinBig, WinJackpot, WinTotal, SwapSplash, SlotTransition and the Spin Progress meter. In play a white ray burst sat behind the logo on some spins and behind the number on the Free Spins splash.
- **Construction:** 35 sprites, 33 of them frames. The sprite circularWhiteRays2 has the same name as one in Mega Cash Boost: Hold & Win and Fire Rail Express: Hold & Win; whether it is the same picture was not compared.
- **Notes:** Nothing here is themed; the theme is carried by the rainbow and clover effects.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 1% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Rainbow effects

`rainbow-effects` · atlas · 47 parts · largest 332×397 · sheet `sheets/rainbow-effects.webp`

- **Role:** The rainbow as moving light: arcs that grow, ribbons that write themselves, a vertical rainbow strip for transitions, and rays.
- **Subject:** A rainbow arc appearing from one end; a looping ribbon of rainbow light drawing an S; a tall soft rainbow bar; a fan of blurred rays in the spectrum colours.
- **Style:** Soft light painting; no outline anywhere.
- **Rendering:** Entirely soft (soft edge 0.941, the softest unit): blurred bands with a white-hot core on the ribbons.
- **Colour:** Measured magentas #961770 14% and #ae53b8 12%, orange #f0a641 13%, red #c54057, yellow #f2e13c, cyan #62e0f5: the full spectrum, weighted to the warm and magenta side.
- **Lighting:** They are the light.
- **Ambience:** Magic made friendly: the rainbow replaces fire and lightning as the game's energy.
- **Materials:** Light.
- **Variants:** Two frame sequences (effectRainbowShow, 22 frames, an arc up to 132x135; rainbowSpecialShow, 23 frames, a ribbon up to 332x397), rainbowTransition (122x509) and circularRainbowRays (144x161).
- **Motion:** effectRainbowShow x22 and rainbowSpecialShow x23 are drawn frame by frame. The strip is used by SlotTransition (3.33 s), LevelUpReelSplash (0.75 s) and the Collector's effect; the ribbon by GlobalMultiplier and WinJackpot. In play, entering Free Spins washed the whole screen in a horizontal rainbow before the purple scene appeared, and the purple backdrop's rainbow ribbon loops behind the board during Free Spins.
- **Construction:** 47 small sprites, 45 of them frames; the effects are small and scaled up, which their softness allows.
- **Notes:** The rainbow appears at four scales with one look: backdrop ribbon, frame ribbon, pot rainbow, effect frames.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, glow or soft effect · brightness 53% · saturation 64% · contrast 50% · warm 61% / cool 23% · brighter towards: bottom-left (1)
- **Palette (measured):** #961770 magenta 14%, #f0a641 orange 13%, #ae53b8 magenta 12%, #c54057 red 10%, #f2e13c gold 8%, #62e0f5 cyan 3%

### Pipe Swap: the pipe and its clover

`pipe-swap` · atlas · 2 parts · largest 461×462 · sheet `sheets/pipe-swap.webp`

- **Role:** The picture of the Pipe Swap feature (level 2): on a no-win screen it turns paying symbols into one symbol (the game's rules). Also shown on the Free Spins splash.
- **Subject:** A large briar pipe with a dark stem, seen from the bowl side, with a glossy green clover badge on the bowl.
- **Style:** The props' 3D look at the largest size in the game.
- **Rendering:** Smooth airbrushed wood with a bright green rim light along the underside and stem; hard-edged (soft edge 0.051).
- **Colour:** Wood oranges and browns #c2754e 28%, #67301b 22%, #2f1209, with green #116109 and a bright #1cef2a.
- **Lighting:** Lit from the top-right, rimmed in green from below.
- **Ambience:** Cosy, grandfatherly; smoke as harmless magic.
- **Materials:** Polished briar wood, a dark mouthpiece, an enamel clover.
- **Variants:** Pipe (461x462) and clover badge (142x150); the same pipe is a small yellow icon on the Spin Progress meter.
- **Motion:** SwapSplash (10 bones): show and showSplash 1.33 s, with coloredSmoke and firework frames. TileTransformEffect: show 1.38 s. In the first spins of this run a yellow silhouette of the pipe stood over the reels with the mug; the swap itself was not caught in a frame.
- **Construction:** Two sprites; the 461 px pipe is the largest prop in the atlas after the jackpot banners.
- **Notes:** A smoking pipe as a feature picture is a choice to weigh for some markets (a remark, not something the files say).
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 38% · saturation 70% · contrast 67% · warm 82% / cool 9% · brighter towards: top-right (1)
- **Palette (measured):** #c2754e orange 28%, #67301b brown 22%, #2f1209 black 20%, #116109 dark green 6%, #eaad7e orange 6%, #905031 brown 5%

### Glows, particles and small clovers

`light-and-particles` · atlas · 10 parts · largest 494×494 · sheet `sheets/light-and-particles.webp`

- **Role:** Helpers: a soft white glow, a ring wave, a star glint, dust particles, two small glossy clovers thrown as particles, and the engine's emitter textures.
- **Subject:** A round glow (494 px), a bubble-like ring, a four-point glint, sparse yellow and white dots, two four-leaf clovers in yellow-green, and a pure green guide square.
- **Style:** Utility sprites; the clovers are in the props' glossy style.
- **Rendering:** Soft whites and two small hard-edged clovers. The unit's 35% pure green #17ff01 is the particle guide square, not art.
- **Colour:** White 57%; clover greens #74a20a and #add20b.
- **Lighting:** Self-lit; the clovers are top-lit.
- **Ambience:** Background shimmer.
- **Materials:** Light; waxy leaves.
- **Variants:** whiteGlow, whiteWave, blinkRealistic12, yellowParticles, whiteParticles, clover1, clover2, particleGuide, and the textures glow and emitter_particle.
- **Motion:** No frame sequence. Moved by skeletons: ReelAnticipation and TileFreeSpinsEffect throw the clovers, WinBig carries them on its many bones, TrailEffect and SpinCounterPiece use the ring; BackgroundParticles and ForegroundParticles place emitters (particleGuide).
- **Construction:** 10 sprites; clover1 is 103x85 and clover2 66x64.
- **Notes:** Clovers as decoration and confetti: in play BIG WIN carried clover sprigs on its plaque and a shower of Golden Coins, not generic confetti.
- **Measured:** bright, saturated, warm and cool mixed, low contrast, strong highlights · brightness 87% · saturation 42% · contrast 4% · warm 1% / cool 21% · brighter towards: left (1), right (1)
- **Palette (measured):** #ffffff white 57%, #17ff01 green 35%, #305f08 dark green 3%, #74a20a green 3%, #add20b green 2%


## Game interface

Buttons, counters and panels drawn for this game.

### Jackpot banners: MINI, MAJOR, GRAND, MAXI, MINOR

`jackpot-panel` · atlas · 35 parts · largest 932×727 · sheet `sheets/jackpot-panel.webp`

- **Role:** The five jackpots above the reels (15x, 25x, 50x, 150x and 2500x the stake, the game's rules), each locked by a padlock until Spin Progress level 4.
- **Subject:** Five curled parchment-like banners with gold borders, in purple (MINI), green (MAJOR), red (MAXI) and blue (MINOR), and a wider orange-gold GRAND banner with a clover crest and a rainbow lower edge; gold name lettering; a gold padlock; two glowing cyan butterflies.
- **Style:** Heraldic scroll banners drawn as bent metal sheets; the names in the logo's gold serif.
- **Rendering:** Hard-edged (soft edge 0.114): a satin gradient face inside a bevelled gold border that curls at the corners. The names have a light top, an orange lower half and a brown side. GRAND's highlight is a 21-frame grey-white sweep cut to the letters.
- **Colour:** Gold and orange lead (#de8c10 35%, #f3c737 10%, #963c05 20%) with one flat colour per banner: green #115f01, purple #5b046a, blue #163a88, red on MAXI. Warm 0.822.
- **Lighting:** Top-lit (5 of 7 measured parts); each banner is lighter down its middle, like a bent sheet catching light.
- **Ambience:** A row of prizes hung like pennants over a fairground stall.
- **Materials:** Enamelled or satin-covered metal with gold edging, gold lettering, a brass padlock with a steel shackle.
- **Variants:** Four small banners in two mirrored shapes (Mini and Minor 303x388, Major and Maxi about 405x431) and the Grand (932x727); five names; the lock in two parts; the Jackpot skeleton has skins jackpot0 to jackpot4.
- **Motion:** Jackpot (7 bones): idle 1.83 s, unlock 1 s, win 1 s, and lockGs and loopGs for the intro screen; it uses explosion and firework frames for the unlock. JackpotAnticipationSplash 4.33 s shows MORE FOR THE GRAND JACKPOT. One frame sequence: jackpotGrandHighlight, 21 frames. In play all five stayed locked, each with its padlock; on the intro they show their values.
- **Construction:** 35 sprites, 21 of them the GRAND highlight. Banner, name and lock are separate, so a banner can show a padlock or, on the intro, its value in the UltraWhiteGold numerals.
- **Notes:** The five banner colours are the same five as the enamel leaves and rim of the Jackpot Coin and as the royals' colours: one palette of rainbow steps is used for ranking everywhere.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 47% · saturation 88% · contrast 65% · warm 82% / cool 11% · brighter towards: top (5), right (1), left (1)
- **Palette (measured):** #de8c10 orange 35%, #963c05 brown 20%, #f3c737 gold 10%, #390f05 dark red 6%, #115f01 dark green 6%, #5b046a dark magenta 4%

### The five pots under the reels

`pots` · atlas · 42 parts · largest 296×301 · sheet `sheets/pots.webp`

- **Role:** The collectors of the base game: a Golden Coin throws a coin to the pot under its reel and may activate it; active pots start the Hold & Win and decide which reels get a Collector (the game's rules).
- **Subject:** A round-bellied cauldron with a rim and two small lugs, in dull dark iron when inactive and in polished gold when active, with coins inside, a rainbow rising from it, and a 14-frame change from iron to gold that fills from the bottom.
- **Style:** The classic pot of gold as a chunky 3D-look prop, matching the barrel and mug.
- **Rendering:** Smooth metal gradients with a green rim light underneath; front and back rim are separate so coins can sit inside. The rainbow is a soft arc (potProgressRainbowWave) and a blurred rainbow haze (potProgressRainbow). The glow frames are grey-white copies of the pot.
- **Colour:** Gold-brown #824d03 55%, #c38e03, #f3c112, #f8ef43, with dark iron #382b2c for the inactive pot. Warm 0.812.
- **Lighting:** Lit from the top-right and top-left (15 of 17 measured parts); a bright band across the belly.
- **Ambience:** The promise at the bottom of the screen: dull pots waiting to turn to gold.
- **Materials:** Cast iron, polished gold, light.
- **Variants:** Inactive and active pot (front 258x165, back rim 211x31), two coins, the rainbow in two forms, a 14-frame fill (potProgress) and a 20-frame shine (potGlow). SceneCollector has skins skin0 to skin4, one per pot.
- **Motion:** SceneCollector (57 bones, 72 slots): idle 0.42 s, collect 0.58 s, progress 1.67 s, preactivate 1.17 s, loopPreactive 2 s, activate 0.58 s, activateSplash 6.67 s, loopActive 2 s, loopMax 0.58 s, reset 1 s. Two frame sequences: potProgress (14 frames, iron turning to gold from the bottom up) and potGlow (20 frames, a shine). In play the five pots stayed dark under the reels while coins dropped towards them.
- **Construction:** 42 sprites, 34 of them animation frames. Front, back rim and coins are layered so the pot has an inside.
- **Notes:** The rules say the gold and rainbow on the pots are 'purely for visual entertainment': the fill animation is anticipation art, not a meter.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 46% · saturation 82% · contrast 50% · warm 81% / cool 8% · brighter towards: top-right (9), top-left (6), left (2)
- **Palette (measured):** #824d03 brown 55%, #c38e03 orange 8%, #382b2c dark red 6%, #f3c112 gold 6%, #fffeff light magenta 5%, #f8ef43 gold 4%

### Spin Progress meter and respin counter

`spin-progress` · atlas · 12 parts · largest 692×361 · sheet `sheets/spin-progress.webp`

- **Role:** The meter above the reels that counts base-game spins down to the next of five unlocks (Wild Reels, Pipe Swap, Normal Game Collector, Jackpots, Bonus Booster; the game's rules), and the 3-2-1 respin counter of the Hold & Win.
- **Subject:** A rainbow ribbon that waves across the top of the frame; a gold pocket watch with a rainbow rim; five flat yellow-green icons (mug, pipe, hat, key with a clover bow, arrow); a wooden plate with three cells and the numerals 1, 2, 3 in purple with gold edges.
- **Style:** The ribbon and watch are painted; the feature icons are flat one-colour pictograms with a glow, a different, lighter language for 'not yet yours'.
- **Rendering:** Ribbon: soft folded bands of the seven colours with a glow. Icons: flat #e7f71e silhouettes with cut-out details and a soft halo. Counter numerals: purple faces with a gold bevel.
- **Colour:** Icon yellow-green #e7f71e 17%, rainbow oranges #f8a71b and #f16827, wood #572617 22%, cyan #96f8f2 on the watch.
- **Lighting:** The icons are self-lit; the watch has a top highlight.
- **Ambience:** A countdown to a present: playful and light.
- **Materials:** Satin ribbon, a gold watch, neon-like signs, a wooden plate.
- **Variants:** Five feature icons; ProgressBar has skins feature0 to feature5; three numerals; the watch hand is its own 12x26 sprite.
- **Motion:** ProgressBar (32 bones): show 0.5 s, activate 1.83 s, regress 0.5 s, reset 0.67 s, loops of 3.17, 2 and 1 s, and a regressClockArrow of 1.67 s that turns the watch hand. ProgressBarEffect waves the ribbon in a 9.5 s loop. SpinCounter: show 0.58 s and a remove and reset animation per numeral. In play the meter read 10 then 25 UNLOCK in the yellow Ravie numerals, with the watch on its left and the next feature's icon on its right.
- **Construction:** 12 sprites. The ribbon (692x361) is one picture bent by bones; the word UNLOCK is a localised lettering file.
- **Notes:** A persistent unlock meter is the game's own structure; its art cost is small: five pictograms, a watch and a ribbon.
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 59% · saturation 75% · contrast 55% · warm 74% / cool 17% · brighter towards: top-right (1), bottom (1)
- **Palette (measured):** #572617 dark red 22%, #e7f71e gold 17%, #f8a71b orange 12%, #f16827 orange 8%, #c93f10 orange 6%, #96f8f2 light cyan 5%


## Typography

Embedded fonts and lettering.

### Numerals: RavieRegular (yellow with a rainbow side)

`font-ravie` · atlas · 18 parts · largest 143×237 · sheet `sheets/font-ravie.webp`

- **Role:** The bitmap numerals of the Spin Progress counter (seen in play as 10, 9 ... 25 above the reels).
- **Subject:** Swollen, curly display numerals 0 to 9 with x, +, *, ?, /, comma, minus and point.
- **Style:** A psychedelic poster face (the font service names it RavieRegular) dressed for the game.
- **Rendering:** Hard-edged (soft edge 0.044): a yellow face with a lighter centre, an orange outline, and a thin stacked rainbow extrusion at the lower left.
- **Colour:** Orange #e1860e 35%, yellows #fbdd17 28% and #fdfa78 11%, with magenta #de158e and red #dd2547 in the rainbow edge.
- **Lighting:** Top-lit faces.
- **Ambience:** Bouncy and loud.
- **Materials:** Glossy enamel.
- **Variants:** 18 glyphs on this page. The descriptor lists 110, among them many currency signs placed on other pages that this session did not load.
- **Motion:** None in the files.
- **Construction:** A page from the provider's shared font service (fonts-v2), 143 px wide digits; not in the game's atlas.
- **Notes:** 92 glyphs the reader cut wrongly from this page (they live on pages loaded on demand) were removed from the run.
- **Measured:** bright, vivid, warm, high contrast, hard-edged, strong highlights · brightness 67% · saturation 84% · contrast 66% · warm 93% / cool 4% · brighter towards: top (3)
- **Palette (measured):** #e1860e orange 35%, #fbdd17 gold 28%, #fdfa78 gold 11%, #fdf243 gold 4%, #de158e magenta 4%, #f29b37 orange 4%

### Numerals: UltraPurpleGold and UltraWhiteGold

`font-ultra` · atlas · 29 parts · largest 210×229 · sheet `sheets/font-ultra.webp`

- **Role:** Two bitmap numeral sets from the provider's font service: a cream set with a gold rim (seen on the intro as the jackpot values 15x to 2500x and in play as win amounts) and a purple set with a gold rim.
- **Subject:** Fat slab-serif numerals 0 to 9 with x, +, comma, point and minus, in two colourings.
- **Style:** Wood-type poster numerals (the service names the face Ultra), heavy and round.
- **Rendering:** Very hard-edged (soft edge 0.027): a flat face split by a horizon line, a bevelled gold border and a dark red side.
- **Colour:** Cream #f8eed4 20%, golds #eebe42 15% and #f8ec8a 13%, purple #600753 and #932589, dark red side #570d0a.
- **Lighting:** Top-lit (18 of 19 measured parts).
- **Ambience:** Showman's numbers: solid and rich.
- **Materials:** Enamel face in a gold setting.
- **Variants:** Two sets: UltraWhiteGold (15 glyphs) and UltraPurpleGold (14 glyphs).
- **Motion:** None in the files.
- **Construction:** Two pages from the shared font service; digits about 200 px wide. Fire Rail Express: Hold & Win used UltraPurpleGold too (the provider notes of this project).
- **Notes:** Where the purple set is used was not identified in the screens; the values on the Golden Coins are a candidate (inference).
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 56% · saturation 60% · contrast 86% · warm 90% / cool 0% · brighter towards: top (18), top-left (1)
- **Palette (measured):** #f8eed4 light orange 20%, #eebe42 orange 15%, #f8ec8a light gold 13%, #570d0a dark red 12%, #600753 dark magenta 12%, #932589 magenta 8%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts
- `shared-tile0`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 533 components cut from 49 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
