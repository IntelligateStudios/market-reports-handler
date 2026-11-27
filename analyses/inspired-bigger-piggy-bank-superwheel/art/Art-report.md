# Bigger Piggy Bank Superwheel: art report

inspired · run `2026-11-27-0438-inspired-bigger-piggy-bank-superwheel` · captured 2026-11-27

Source: the provider's free-play demo, https://marketingdemo.stg-uk.inspiredvirgo.com/tpi-game/marketing?parentredirect=false&rgsId=virgo&igpId=demo&brandId=marketing&skinId=default&gameId=IGG_biggerpiggybanksuperwheel94&channelType=desktop&presentType=HTML5&secureToken=sampleToken&playerId=*&accountId=*&localeCode=en-GB&currencyCode=XXX&IGG_currency=XXX&IGG_language=en-GB&IGG_channel=desktop&IGG_jurisdiction=GB&IGG_homeUrl=https://inseinc.com

**Extracted:** 895 named components from 37 textures in 37 atlases; 64 Spine skeletons; 31 frame sequences (363 frames); 13 fonts. Grouped into 39 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A toy-shop bank heist: glossy pink and gold piggy banks, candy bubble lettering and a steel vault with a pig's snout for a lock, set in a navy and gold bank hall, with a red-and-rainbow game-show wheel bolted on top as a shared feature.

**Style.** Glossy cartoon with a soft 3D-look: fat, rounded, toy-like objects with no outlines, and thick outlined balloon lettering for every word. The pig is the only character and appears as symbol, mascot, lock, clasp, coin stamp and win-line head. The Super Wheel and the gamble wheel are flatter and more graphic, in a television game-show manner.

**Rendering.** Smooth airbrushed gradients, a broad soft highlight and small hard white glints on every round form; gold is painted yellow-to-brown, not rendered. Backgrounds are clean stylised interiors in one-point perspective with detail kept at the vault door. Only the vault door's opening (31 frames) and the big-win gems read as true 3D renders.

**Colour.** Measured over the game's own art: mid-tone, saturated (59%), warm 52% against cool 40%, high contrast; the largest measured areas are the dark navy and plum grounds (#131025, #372e63, #683a50). On them sit three candy families: pig pink and magenta (#f676b7, #fe30a2), gold (#f4d020, #bc7d0b) and money green (#63b53e), with cyan (#08f9f1) behind pink pigs and feature tiles. Four prize colours are fixed everywhere: red Grand, purple Major, blue Minor, green Mini. The shared wheel adds its own red (#c90402).

**Lighting.** Top and top-left light on every object (measured: top 91, top-left 53, top-right 41 of the parts with a readable light side). Each symbol ships a 'Light' and a 'Light Hit' copy of itself as an additive layer for its flash, plus thin light sweeps. The hall is lit warm from windows and a ceiling lightbox against cool walls; the bonus room is lit by its own gold.

**Ambience.** Friendly greed: money as sweets and toys, nothing sinister about the bank. The base game is a calm night hall with a mascot watching from the top of the reels; the bonus is the inside of the vault, all gold. The shared Super Wheel brings a louder, studio-lights mood from outside the theme.

**Shape language.** Circles and fat rounded squares: the pig is nearly a sphere, coins and wheels repeat it, tiles and panels have wide radii, letters are inflated. The snout (an oval with two holes) is the game's mark and is stamped on coins, bars, the case, the hammer, the vault and the carpet.

**Materials.** Glazed ceramic, polished gold, paper banknotes, glossy plastic lettering, brushed steel for the vault, enamel wheels, cut gems.

**Typography and lettering.** All display words are painted lettering (logo, WILD, COLLECT, BONUS, the win tiers, prize names). Running text and numbers are set by the client: 53 of its 82 text styles lead with Borsok and Alegreya Sans Black, in cream (#fffef0) with a navy stroke (#140d49) for the big-win title, as its text-style file states. Thirteen font files ship; the Helvetica, Tahoma, Roboto, Barlow and Arial Black ones serve the provider's interface (inference from the style lists).

**Motion.** Skeletal: 64 Spine 3.8.99 skeletons, most of them short (0.83 s) bounce, win and collect moves on symbols built from a handful of parts, with longer idles for the mascot (4.17 s) and the scene (4.67 s). The signature move is the smash: a pig cracks, flies apart in 14 pre-cut shards and leaves a money heap. Frame sequences are kept for what a rig cannot do: the vault door (31 frames), spinning coins (18 a colour), gems (12 each), sparkles. The five intro pages are video clips. Curves in this Spine version are not read by the drawing tool, so the frames here show poses with linear easing.

**Variants and themes.** Pink to gold is the upgrade rule for every pig (symbol, pot pig, wheel pig). The cash pig exists at 1x1, 2x2, 3x3 and 4x3. Scenes, panels and logos ship in landscape and portrait versions inside one pack; base and bonus versions of the board, wheel and prize panels differ by backing and glow. Win words ship in six languages. The client serves the same art at 0.5 and 0.75 of the studio's size; this run holds the 0.75 pack.

**How it is built.** PixiJS client on Inspired's Virgo platform. 30 WebP atlas pages loaded of the 36 its manifest lists (the rest are other languages' win words and a US-CT wheel), up to 4096 px, packed by load order, not by subject, with trimmed and rotated frames listed in a packed manifest (base64 of LZ-UTF8 JSON), and all skeletons as JSON inside one data file. Symbols are small rigs of 4 to 30 parts with separate light layers; lettering is split into one sprite a letter where it must animate. Five of the pages are spent on the vault-door transition.

**Consistency.** The pig-and-money art is tight: one light, one finish, one lettering hand, one mark. The Super Wheel, its red interface and the gamble wheel are visibly a second system (flat fills, block capitals, red glow buttons), dressed with the logo and a snout coin but not redrawn in the toy style.

**What to take from it.** (1) One mark carries a whole game: the snout is on at least nine different pieces, so plain objects (bars, a case, a coin) need no character art to belong. (2) Upgrade by material, not by new design: the same pig in pink then gold, at four sizes, gives the feature ladder with one character painted twice (small and large). (3) A breakable symbol is cheap when planned: paint the object once, cut 14 shards, add two crack overlays and a 'what is inside' picture. (4) Ship a 'Light' and a 'Light Hit' copy of each symbol as additive layers: win flashes then cost no new painting. (5) Fix a colour per prize (red, purple, blue, green) and repeat it on coins, panels, wheel wedges and flying tokens. (6) Keep the board near black and the scene dark navy so saturated symbols read; put scene detail where the reels do not cover it. (7) Budget texture memory for transitions: this game spends five 4096 px pages on one door opening. For AI art work, that sequence is a 3D render job, not an image-model job. (8) A shared platform feature (the Super Wheel) will look bolted on unless it is redrawn in the game's finish; here it was not, and it shows.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 44% · saturation 59% · contrast 62% · warm 52% / cool 40% · brighter towards: top (91), top-left (53), top-right (41)

Palette: #131025 black 14%, #372e63 dark blue 10%, #683a50 magenta 10%, #f7f2e6 light orange 3%, #6509a3 purple 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 4 | 46% | 47% | 72% | 52% / 47% | #261f33 dark purple 24%, #474569 blue 13%, #e9c441 gold 12% |
| Reel board | 4 | 44% | 74% | 58% | 54% / 32% | #020b0d black 23%, #e7841a orange 10%, #f8e75b gold 7% |
| Symbols | 11 | 54% | 70% | 54% | 68% / 10% | #f661b1 magenta 21%, #b62d61 red 15%, #bd7c0d orange 12% |
| Characters | 3 | 66% | 60% | 43% | 72% / 7% | #fbef66 gold 18%, #fce3e8 light red 18%, #f874b7 magenta 12% |
| Logo and title | 2 | 44% | 52% | 66% | 50% / 36% | #6b3151 magenta 23%, #17153d dark blue 12%, #72708c grey 9% |
| Win celebrations and banners | 5 | 25% | 84% | 44% | 34% / 63% | #4a0379 dark purple 32%, #0b0722 black 26%, #7a13bb purple 7% |
| Effects | 4 | 64% | 67% | 47% | 59% / 25% | #5a9d29 green 16%, #f5de5b gold 13%, #f6b80e orange 11% |
| Game interface | 5 | 38% | 79% | 50% | 68% / 22% | #c80403 red 24%, #090f19 black 17%, #f8c011 gold 8% |
| Provider interface (shared) | 1 | 23% | 52% | 58% | 58% / 9% | #181010 black 47%, #e90101 red 13%, #940401 dark red 13% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backgrounds (bank vault hall; inside the vault)

`backgrounds` · atlas · 2 parts · largest 1920×1920 · sheet `sheets/backgrounds.webp`

- **Role:** The base-game scene and the bonus scene, each one square painting.
- **Subject:** Base: a navy bank hall with tall paper-screen windows, a checkered gold floor, an orange carpet with snout medallions, and a round steel vault door with a gold pig snout at its centre. Bonus: inside the vault, gold walls of deposit boxes and a floor heaped with coins, with a snout plaque glowing at the back.
- **Style:** Stylised painted interior in one-point perspective, simplified shapes.
- **Rendering:** Clean gradients, hard edges, patterned wallpaper kept faint; detail gathers at the vault door.
- **Colour:** Base navy and violet (#2c1c35, #46446a) against gold light (#eec647, #f9ec81); bonus almost all gold and orange (#a57546, #d36f08).
- **Lighting:** Warm light from the windows and a ceiling lightbox on cool walls; in the bonus the light comes from the back wall.
- **Ambience:** A cartoon bank after hours; the bonus is the inside of the treasure.
- **Materials:** Steel, brass, lacquered wood, carpet, gold.
- **Variants:** Two scenes; both 1920x1920 at this pack, cropped by the layout for landscape and portrait.
- **Motion:** Stills; the moving copy is the BonusTransition rig.
- **Construction:** One picture each; square so that one file serves both orientations.
- **Notes:** The reels cover the centre, so the vault door is mostly hidden in play: the painting is made to read at its edges. In the free spins the gold room is shown brighter and paler than the file, with the reels over its centre (game screens 11 to 18).
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged · brightness 52% · saturation 54% · contrast 84% · warm 72% / cool 25% · brighter towards: bottom (1)
- **Palette (measured):** #eec647 gold 21%, #2c1c35 dark purple 20%, #a57546 orange 16%, #f9ec81 gold 8%, #46446a blue 7%, #71442c brown 5%

### Vault scene rig and door opening

`BonusTransition` · skeleton · 58 parts · largest 1920×1920 · sheet `sheets/BonusTransition.webp`

- **Role:** The base scene as layers, and the move into the bonus: the vault door unlocks, opens and the camera goes in.
- **Subject:** Walls, the flattened hall, the steel door with its four pistons and gold snout, rings of bolts, light shafts, three depths of coin heaps and the gold room behind.
- **Style:** As the backgrounds.
- **Rendering:** The door's opening is a pre-rendered sequence of 31 frames at 1500x1500 (source size), the only part of the game that reads as true 3D render.
- **Colour:** Navy and grey steel (#251f33, #484466, #76718e, #c6c3c4) with gold (#e4c446).
- **Lighting:** Window light shafts as additive sprites; the snout and bolts light up before the door moves.
- **Ambience:** A heist moment, held for five seconds.
- **Materials:** Brushed steel, brass, gold.
- **Variants:** Base idle, bonus intro, bonus outro, bonus idle.
- **Motion:** Seen in the frames: baseIdle 4.67 s (shafts and glints), bonusIntro 5 s (pistons draw back, the door swings, the gold room fills the view), bonusOutro the reverse, bonusidle 4.67 s.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 40 bones, 48 slots, 10 additive; 58 parts, among them the 31-frame door sequence spread over five 4096 px pages.
- **Notes:** The costliest piece of the game in texture memory: five pages for one transition.
- **Skeleton (from the file):** Spine 3.8.99 · 40 bones · 48 slots · 15 mesh, 61 region, 1 clipping · animations: baseIdle (4.67 s), bonusIntro (5.0 s), bonusOutro (5.0 s), bonusidle (4.67 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 46% · saturation 40% · contrast 72% · warm 45% / cool 53% · brighter towards: top (3), bottom-left (3), top-left (2)
- **Palette (measured):** #251f33 dark purple 20%, #484466 blue 18%, #76718e grey 14%, #c6c3c4 grey 12%, #e4c446 gold 12%, #a0979b grey 4%

### Super Wheel (the shared wheel)

`super-wheel` · atlas · 16 parts · largest 660×960 · sheet `sheets/super-wheel.webp`

- **Role:** The second, community wheel: a 'Player Link' feature that players on the same stake share (as the intro pages say).
- **Subject:** A wheel-of-fortune disc of thin rainbow wedges with a ring of bulbs, a red and gold rim reading SUPER WHEEL, a gold hub, a question-mark pointer, white tapered segment cards with red multipliers, on a starry blue backdrop.
- **Style:** TV game-show wheel, flatter and more graphic than the pigs.
- **Rendering:** Flat colour wedges, simple bevels, outlined red numerals.
- **Colour:** Navy (#011b45, #02388e) behind a full rainbow, red (#cd230f) and gold (#f8bf1a).
- **Lighting:** Lit bulbs and a glowing rim; no cast light.
- **Ambience:** Showtime, a studio at night.
- **Materials:** Enamel, bulbs, gold.
- **Variants:** Landscape and portrait backdrops; segment values 8x to 50x and BONUS as separate cards.
- **Motion:** None in these pictures; the wheel is turned by code.
- **Construction:** Separate base, pins, centre, blank centre, hub and clacker so the disc can spin under a fixed rim.
- **Notes:** Its look (red buttons, Arial-like numerals) differs from the pig art: it reads as a shared Inspired feature dressed for this game (inference).
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 23% · saturation 93% · contrast 34% · warm 42% / cool 56% · brighter towards: bottom (3), top-left (1)
- **Palette (measured):** #011b45 dark blue 30%, #2d0e07 black 27%, #02388e dark blue 11%, #f8bf1a orange 5%, #cd230f red 5%, #8d0e07 dark red 5%

### Super Wheel aura

`SuperWheel_Background_Base` · skeleton · 31 parts · largest 836×844 · sheet `sheets/SuperWheel_Background_Base.webp`

- **Role:** The glow behind the Super Wheel, which grows over five levels.
- **Subject:** A gold ring with blue, violet and iridescent bursts behind it, a field of small stars and streaking sparks.
- **Style:** Pure effect art.
- **Rendering:** Soft blurred shapes, additive.
- **Colour:** White-gold core (#fdf9ec, #fdc906) with blue, cyan and violet halos (#025be4, #047096, #7a39fe).
- **Lighting:** Emissive throughout.
- **Ambience:** Cosmic, rising excitement.
- **Materials:** Light only.
- **Variants:** Base and Super Bonus colourings; five idle levels each.
- **Motion:** Seen in the frames: long loops (9 to 14 s) in which the halo breathes and sparks cross; level 5 cycles through rainbow tints.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 39 bones, 36 slots of which 29 additive; a 19-frame spark streak sequence.
- **Notes:** Intensity is done with more layers and faster loops, not new art.
- **Skeleton (from the file):** Spine 3.8.99 · 39 bones · 36 slots · 306 region · animations: Background_Idle_Lvl1 (14.1 s), Background_Idle_Lvl2 (11.03 s), Background_Idle_Lvl3 (9.07 s), Background_Idle_Lvl4 (9.2 s), Background_Idle_Lvl5 (9.2 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, strong highlights · brightness 55% · saturation 49% · contrast 49% · warm 74% / cool 26% · brighter towards: bottom (2), top-left (1)
- **Palette (measured):** #fdf9ec light gold 18%, #4e3a30 brown 9%, #1a120e black 8%, #047096 cyan 6%, #420065 dark purple 5%, #025be4 blue 4%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board

`reel-board` · atlas · 5 parts · largest 838×518 · sheet `sheets/reel-board.webp`

- **Role:** The 5x3 window the symbols sit in.
- **Subject:** A thin gold rounded frame, a near-black backing with faint blue column lines, a green-edged backing for the Super Bonus, a small snout coin, and a help picture of lit reels.
- **Style:** Minimal.
- **Rendering:** Flat dark panel with a slight inner glow; the frame is a thin bevelled line.
- **Colour:** Near black (#010b0c 69%) with green (#1e601a) and navy (#132651) edges.
- **Lighting:** None of its own; a green glow marks active reels.
- **Ambience:** A dark stage so the candy colours of the symbols carry.
- **Materials:** Glass or lacquer (inference), gold trim.
- **Variants:** Base and Super Bonus backings.
- **Motion:** None.
- **Construction:** Single pictures about 815x515 at this pack.
- **Notes:** The board is the quietest thing on screen by design.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 16% · saturation 89% · contrast 41% · warm 22% / cool 50% · brighter towards: right (1)
- **Palette (measured):** #010b0c black 69%, #1e601a dark green 7%, #132651 dark blue 4%

### Bonus wheel behind the reels

`Wheel` · skeleton · 13 parts · largest 768×765 · sheet `sheets/Wheel.webp`

- **Role:** The six-wedge wheel that turns behind and beside the board and awards prizes or free spins.
- **Subject:** A gold-rimmed wheel of six bright wedges (Grand red, Major purple, Minor blue, Mini green, Free Spins, Golden Free Spins) with a snout coin as its pin, plus cash piles for its foot.
- **Style:** Game-show wheel in the pigs' candy style.
- **Rendering:** Flat wedges with a soft gradient, gold bevelled dividers, bubble lettering along each wedge.
- **Colour:** Gold and orange (#eb811a, #f9e85a) with the four prize colours.
- **Lighting:** A light sweep and a divider glow mark the winning wedge.
- **Ambience:** Carnival.
- **Materials:** Enamel and gold.
- **Variants:** Base and bonus contents; a US-CT variant page exists in the manifest and was not loaded.
- **Motion:** Activate (0.83 s): the wedge's edges glow and a light arc sweeps across it.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 7 bones, 5 slots; the wheel face is one 660 px picture turned by code.
- **Notes:** Only the wedge highlight is rigged.
- **Skeleton (from the file):** Spine 3.8.99 · 7 bones · 5 slots · 3 region, 2 clipping · animations: Activate (0.83 s)
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 58% · saturation 68% · contrast 65% · warm 75% / cool 18% · brighter towards: bottom-left (1)
- **Palette (measured):** #eb811a orange 15%, #f9e85a gold 11%, #ab6816 brown 8%, #c3a842 gold 7%, #f4cd1f gold 6%, #68432b brown 5%

### Win lines and win bar

`Winlines` · skeleton · 13 parts · largest 419×92 · sheet `sheets/Winlines.webp`

- **Role:** Marks a winning line and shows the ten line shapes.
- **Subject:** A yellow comet trail led by a small gold pig head, a white bar sweep, and ten small grid diagrams of the lines.
- **Style:** Effect and diagram.
- **Rendering:** Soft yellow streak; flat diagrams.
- **Colour:** Yellow (#fbda05) on navy diagrams (#031747).
- **Lighting:** Emissive.
- **Ambience:** Quick and light.
- **Materials:** Light.
- **Variants:** Ten lines.
- **Motion:** Each Winline animation (0.67 s) runs the pig along its path with the trail behind.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 42 bones carry the ten paths; two sprites.
- **Notes:** A pig as the head of the win line keeps even this small effect on theme.
- **Skeleton (from the file):** Spine 3.8.99 · 42 bones · 4 slots · 1 clipping, 10 path, 1 region, 1 mesh · animations: Winline01 (0.67 s), Winline02 (0.67 s), Winline03 (0.67 s), Winline04 (0.67 s), Winline05 (0.67 s), Winline06 (0.67 s), Winline07 (0.67 s), Winline08 (0.67 s), Winline09 (0.67 s), Winline10 (0.67 s)
- **Measured:** mid-tone, vivid, cool, high contrast, hard-edged, strong highlights · brightness 51% · saturation 63% · contrast 84% · warm 23% / cool 72% · brighter towards: bottom (2), top (1)
- **Palette (measured):** #031747 dark blue 38%, #fafcfb light green 21%, #fbda05 gold 6%, #fcf7ab light gold 6%, #b2b2ba grey 4%, #f88e04 orange 2%

### Side meter (pigs and safe)

`MatrixPig` · skeleton · 45 parts · largest 638×683 · sheet `sheets/MatrixPig.webp`

- **Role:** The column beside the reels that fills with small pigs toward a safe (its role in play is read from the screens).
- **Subject:** A narrow navy column of five pig-shaped slots, small pink pig and gold safe tokens, a glow, and sweeping light bars.
- **Style:** Small icons of the main art.
- **Rendering:** Reduced copies of the pig and safe paintings.
- **Colour:** Orange-gold and pale light (#dc992a, #fefee4) on navy (#151c67).
- **Lighting:** Additive light bars.
- **Ambience:** A progress tease.
- **Materials:** As the pig and safe.
- **Variants:** Landscape and portrait panels.
- **Motion:** The pig token hops (1 s); a 17-frame light sequence circles the meter.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 3 bones; two 17-frame sequences.
- **Notes:** Nothing further.
- **Skeleton (from the file):** Spine 3.8.99 · 3 bones · 2 slots · 2 region · animations: animation (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 60% · saturation 63% · contrast 49% · warm 72% / cool 20% · brighter towards: top (3), top-left (2), top-right (1)
- **Palette (measured):** #dc992a orange 24%, #fefee4 light gold 15%, #f7e665 gold 12%, #151c67 dark blue 10%, #090c29 black 5%, #fcf60c gold 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Reel symbols, still and spinning copies

`symbol-stills` · atlas · 35 parts · largest 651×600 · sheet `sheets/symbol-stills.webp`

- **Role:** The flat picture of every symbol the reels draw while they turn or rest; the rigs take over on landing and on a win.
- **Subject:** Pink and gold piggy banks in framed tiles, four prize coins (Grand, Major, Minor, Mini), a pink mallet tile reading COLLECT, a gold safe reading BONUS, an EXTRA +1 SPIN tile, a WILD tile of coin stacks, four money pictures (a cluster of gold dollar signs, a blue pig-nosed briefcase, gold bars, a wad of green notes) and five royals (A, K, Q, J, 10).
- **Style:** Glossy cartoon with a soft 3D-look: fat rounded forms, no outlines on the objects, thick outlined bubble lettering on the words.
- **Rendering:** Smooth airbrushed gradients with small hard white glints; the royals are inflated letters with a darker extruded side and one cut gem each.
- **Colour:** Gold leads (#f4d020, #bc7d0b, measured 36% yellow and 32% orange hue), with magenta (#f63e9f, #e81971) for pig tiles and wild, cyan behind the pink pig and the feature tiles; each royal has its own colour: purple A, red K, blue Q, green J, pink 10.
- **Lighting:** Top and top-left light (measured), a broad soft highlight on every round form and a rim of bounce light underneath.
- **Ambience:** Toy-shop bright and friendly; money shown as sweets rather than as wealth.
- **Materials:** Polished gold, glazed ceramic (the pink pig), paper notes, cut gems, enamel-like tile backs with a sunburst.
- **Variants:** Dim copies (B1_Normal_Dim, L2_Dim, L3_Dim, H1 and B4 Inactive) for losing positions; gold pig tiles at 1x1, 2x2, 3x3 and 4x3 cells; small 'Simple' copies of four feature symbols; glow columns for the hammer and the safe.
- **Motion:** None in these pictures: they are the stills the reel strip uses.
- **Construction:** Single sprites on the page the client calls 'nocrush' (not recompressed), about 165 px a cell at this pack; the larger gold pigs are single pictures up to 651x600.
- **Notes:** The symbol ids are the game's: B1 cash pig, B2 prize coins, B3 collect hammer, B4 bonus safe, B6 extra spin, WI wild, H1 to H4 high, L1 to L5 royals. What each does is read from the paytable pages, not from these files.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 60% · saturation 74% · contrast 64% · warm 77% / cool 14% · brighter towards: top (7), top-left (4), top-right (2)
- **Palette (measured):** #bc7d0b orange 18%, #f4d020 gold 18%, #fcf7c4 light gold 10%, #f63e9f magenta 8%, #f9e86c gold 7%, #7b4b0f brown 6%

### Bonus safe

`B4` · skeleton · 21 parts · largest 854×900 · sheet `sheets/B4.webp`

- **Role:** The symbol that starts the wheel bonus.
- **Subject:** A gold cube safe with a purple ship's-wheel handle and a small pink snout on the door, on a pink sunburst tile, the word BONUS below; it opens to a heap of notes and coins.
- **Style:** Chunky toy cartoon.
- **Rendering:** Flat bevelled gold faces with soft gradients; the door has closed, partly open, open and motion-smear pictures.
- **Colour:** Gold and brown (#dba318, #a86415), green money (#66b63f, #217748), magenta tile (#fc3dab).
- **Lighting:** Top light; a body-light overlay and a small starburst.
- **Ambience:** A cartoon heist prize.
- **Materials:** Brushed gold, purple enamel handle, paper money.
- **Variants:** A dim 'Inactive' still; a glow column.
- **Motion:** Seen in the frames: bounce; intro and outro fade the word; collect_intro swings the door open through its drawn stages to show the money; win holds the open safe while notes flutter (7 note sprites).
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 24 bones, 23 slots, 21 parts including four door states.
- **Notes:** The door opening is drawn stages swapped in order, not a 3D turn.
- **Skeleton (from the file):** Spine 3.8.99 · 24 bones · 23 slots · 27 region, 2 clipping · animations: bounce (0.83 s), collect_intro (0.83 s), collect_outro (0.83 s), intro (0.0 s), outro (0.5 s), win (0.83 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 56% · saturation 74% · contrast 58% · warm 68% / cool 17% · brighter towards: top (3), top-right (1), top-left (1)
- **Palette (measured):** #a86415 brown 22%, #dba318 orange 21%, #f7e25d gold 11%, #66b63f green 9%, #217748 dark green 9%, #fc3dab magenta 6%

### Prize coins (Grand, Major, Minor, Mini)

`B2_Grand` · skeleton · 28 parts · largest 533×246 · sheet `sheets/B2_Grand.webp`

- **Role:** The four fixed prizes as coin symbols that land on the reels and fly to the prize panels.
- **Subject:** A gold coin stamped with a pig's snout, ringed in the prize's colour, with the prize name in bubble letters across it.
- **Style:** Flat-fronted cartoon coin with thick candy lettering.
- **Rendering:** Soft bevel on the coin, each letter a separate sprite with a white outline and darker drop edge.
- **Colour:** One colour a prize: red Grand (#ea3048), purple Major (#9419d7), blue Minor (#2d8df6), green Mini (#42ba26), all on gold (#fcee7a).
- **Lighting:** Even front light; the colour ring is a blurred glow sprite behind the coin; a diagonal light sweep passes over.
- **Ambience:** Arcade prize tokens.
- **Materials:** Stamped gold.
- **Variants:** Four prizes from one coin, four glow discs and 18 letter sprites.
- **Motion:** Bounce: the coin and its letters hop one after another (letters are on their own bones).
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. The Grand rig has 10 bones and 9 slots; the unit also holds the Major, Minor and Mini rigs' parts, which are not drawn here.
- **Notes:** The same four colours code the prize panels, the wheel wedges and the collection coins everywhere in the game.
- **Skeleton (from the file):** Spine 3.8.99 · 10 bones · 9 slots · 8 region, 1 clipping · animations: bounce (0.83 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 61% · saturation 68% · contrast 37% · warm 60% / cool 32%
- **Palette (measured):** #fcee7a gold 22%, #42ba26 green 11%, #2d8df6 blue 11%, #9419d7 purple 11%, #ecbf3a orange 11%, #ea3048 red 10%

### Gold piggy bank, giant (2x2, 3x3, 4x3)

`B1_Enhanced3x3` · skeleton · 31 parts · largest 1200×1200 · sheet `sheets/B1_Enhanced3x3.webp`

- **Role:** The 'Bigger Pigs' of the title: the gold pig as one symbol over several cells.
- **Subject:** The gold pig at large size with the same notes and dollar sign, in pink sunburst frames made for 2x2, 3x3 and 4x3 cells.
- **Style:** As the small gold pig, with more room for reflections.
- **Rendering:** A separately painted large pig (711x647 at this pack) rather than the small one scaled: finer glints, softer brown reflections on the belly.
- **Colour:** Magenta leads because of the frames (#ff5bc6 21%, #fc299c 14%), then gold (#f4d21c, #bf7e09).
- **Lighting:** Top-left key (measured), white sparkle on the snout rim.
- **Ambience:** The showpiece of the reels; a big friendly object that fills the board.
- **Materials:** Polished gold, paper notes, a large mixed heap of coins, notes and gold bars.
- **Variants:** Three frame sizes on one pig; three skeletons (2x2, 3x3, 4x3) share every part but the frame.
- **Motion:** Bounce, idle, collect; the collect frames show a yellow flash, cracks, the shell flying apart and the money heap left in the frame.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 33 bones, 30 slots; frames are separate sprites up to 712x544, the pig is one picture.
- **Notes:** Giant symbols are done by drawing one large pig and three frames, not by tiling.
- **Skeleton (from the file):** Spine 3.8.99 · 33 bones · 30 slots · 28 region, 2 clipping · animations: bounce (0.83 s), collect (0.83 s), idle (0.83 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 57% · saturation 74% · contrast 56% · warm 76% / cool 2% · brighter towards: top-left (5), top (3), top-right (2)
- **Palette (measured):** #ff5bc6 magenta 21%, #bf7e09 orange 18%, #fc299c magenta 14%, #f4d21c gold 13%, #fefad9 light gold 7%, #fceb73 gold 7%

### Gold piggy bank, one cell (rig)

`B1_Enhanced` · skeleton · 27 parts · largest 375×412 · sheet `sheets/B1_Enhanced.webp`

- **Role:** The upgraded cash pig at one cell: the gold form the pink pig becomes.
- **Subject:** The same pig in polished gold with green notes sticking out of the slot and a brown-gold dollar sign, on a hot pink sunburst tile in a gold frame.
- **Style:** Same toy cartoon; the metal is drawn, not rendered.
- **Rendering:** Yellow-to-brown gradients with sharp white glints on snout, ear and back; closed smiling eyes.
- **Colour:** Gold (#f4d420, #bc8209, #fcec73) on magenta (#fe30a2, #fe64d3); green only on the notes. Measured warm 83%.
- **Lighting:** Top light with a strong specular streak; a separate additive light and a starburst 'Shine'.
- **Ambience:** Richer and louder than the pink pig: the same character having won.
- **Materials:** Polished gold, paper money, a heap of coins, notes and bars inside.
- **Variants:** B1_Enhanced-2 is a second skeleton on the same parts (mirrored, by its bone scale: inference from the file).
- **Motion:** Bounce, idle and collect as on the pink pig; collect shatters the gold shell into shards and shows the money heap.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 31 bones, 30 slots, 14 shard sprites.
- **Notes:** Pink tile behind gold, cyan tile behind pink: the tile colour always opposes the pig.
- **Skeleton (from the file):** Spine 3.8.99 · 31 bones · 30 slots · 2 clipping, 28 region · animations: bounce (0.83 s), collect (0.83 s), idle (0.83 s)
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 63% · saturation 73% · contrast 56% · warm 83% / cool 3% · brighter towards: top (2), top-left (2), top-right (2)
- **Palette (measured):** #bc8209 orange 21%, #f4d420 gold 17%, #fcec73 gold 10%, #fe30a2 magenta 10%, #fefad8 light gold 10%, #fe64d3 magenta 9%

### Wild

`WI` · skeleton · 9 parts · largest 282×246 · sheet `sheets/WI.webp`

- **Role:** Substitutes for other symbols (as its word says).
- **Subject:** Stacks of gold coins filling a pink-framed tile with WILD in fat pink letters across them.
- **Style:** Toy cartoon with candy lettering.
- **Rendering:** Coins drawn with a snout stamp on each top, warm brown shadows between stacks; letters with white rim and darker pink edge.
- **Colour:** Gold (#fada42, #e6a019) and brown (#b16a09) under pink (#c22563, #f33a8d); measured warm 94%.
- **Lighting:** Top-left key; a second, brighter coin layer and white star glints flash on.
- **Ambience:** Abundance: the tile is full to the edge.
- **Materials:** Stamped gold, glossy pink plastic letters.
- **Variants:** None.
- **Motion:** Bounce lifts the tile; win pushes the four letters out one by one toward the viewer while the coins brighten.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 12 bones, 11 slots; each letter its own sprite.
- **Notes:** The pink frame instead of gold marks the wild apart from the pig tiles.
- **Skeleton (from the file):** Spine 3.8.99 · 12 bones · 11 slots · 9 region, 2 clipping · animations: bounce (0.83 s), win (0.83 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 56% · saturation 78% · contrast 67% · warm 94% / cool 0% · brighter towards: top-left (3), top (1)
- **Palette (measured):** #fada42 gold 21%, #b16a09 brown 20%, #c22563 red 16%, #e6a019 orange 12%, #fbeb8f light gold 7%, #bf2e02 red 4%

### Extra spin tile

`B6` · skeleton · 4 parts · largest 205×197 · sheet `sheets/B6.webp`

- **Role:** The symbol that adds a spin in the free spins (read from the words on it).
- **Subject:** The words EXTRA +1 SPIN in pink and gold bubble letters on a cyan sunburst tile in a gold frame.
- **Style:** Lettering tile.
- **Rendering:** Outlined candy letters with a light inner bevel.
- **Colour:** Cyan (#09f6e4 25%) with red-pink (#e93d74) and gold lettering.
- **Lighting:** Flat front light.
- **Ambience:** Cheerful, loud.
- **Materials:** Enamel tile, glossy letters.
- **Variants:** The frame sprite is named B5_Frame, so a symbol B5 existed or shares it (inference).
- **Motion:** Bounce hops the words; win fades the tile, then brings EXTRA, +1 and SPIN in one after another.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 7 bones, 4 slots, 4 parts.
- **Notes:** Words are separate sprites so each can pop on its own.
- **Skeleton (from the file):** Spine 3.8.99 · 7 bones · 4 slots · 4 region · animations: bounce (0.83 s), win (1.07 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 57% · saturation 78% · contrast 64% · warm 54% / cool 40% · brighter towards: top (3)
- **Palette (measured):** #09f6e4 cyan 25%, #e93d74 red 13%, #4c1a22 dark red 11%, #01bab5 cyan 10%, #ab630d brown 7%, #d99f1d orange 6%

### High symbols (dollar cluster, briefcase, gold bars, notes)

`H1` · skeleton · 26 parts · largest 392×353 · sheet `sheets/H1.webp`

- **Role:** The four paying picture symbols.
- **Subject:** H1 three gold dollar signs on a spray of notes with a green glow; H2 a blue ribbed briefcase with a pig's snout as its clasp and notes spilling; H3 three gold bars stamped with a snout; H4 a banded wad of green notes.
- **Style:** Toy cartoon; objects float without a tile.
- **Rendering:** Soft 3D-look shading, hard glints, warm bounce under the gold.
- **Colour:** Green and cyan lead this group (#a9f96d, #63b53e, #22607c, #45aec7) with gold (#e1a117, #fae25b); measured cool 46% against warm 36%.
- **Lighting:** Top light (measured); each object has a matching 'Light' overlay sprite for its win flash.
- **Ambience:** Clean, bright money still lifes.
- **Materials:** Gold, moulded plastic case, paper.
- **Variants:** Four rigs; only H1 is drawn here, the other three are on the sheet as parts.
- **Motion:** H1 bounce and win: the dollar signs spread and swell while the green glow pulses; H2 has four fluttering-note pictures and H3 three star glints.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. H1 has 8 bones and 7 slots; H2 12 bones, H3 11, H4 4.
- **Notes:** The pig's snout is stamped on the case and the bars, so even plain objects belong to this game.
- **Skeleton (from the file):** Spine 3.8.99 · 8 bones · 7 slots · 7 region · animations: bounce (0.83 s), win (0.83 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 56% · saturation 70% · contrast 48% · warm 36% / cool 46% · brighter towards: top (8), top-right (3), top-left (1)
- **Palette (measured):** #22607c cyan 16%, #a9f96d green 13%, #e1a117 orange 12%, #45aec7 cyan 10%, #63b53e green 10%, #2d7020 dark green 8%

### Royals (A, K, Q, J, 10)

`L1` · skeleton · 14 parts · largest 282×286 · sheet `sheets/L1.webp`

- **Role:** The five low symbols.
- **Subject:** Inflated letters and a 10, each one colour, four of them holding a cut gem (purple diamond on A, red on K, blue on Q, green on J).
- **Style:** Balloon lettering.
- **Rendering:** Glossy top highlight, a darker extruded side, a soft inner glow; gems faceted with a gold setting.
- **Colour:** Purple A, red K (#bc183b), blue Q (#0d46b7), green J, pink 10 (#dd3485); dark purple shade (#261035).
- **Lighting:** Top and top-left (measured); a thin coloured light sweep per letter.
- **Ambience:** Sweet-shop letters, in key with the pigs.
- **Materials:** Glossy plastic, cut gems.
- **Variants:** Five rigs; A is drawn here. Dim stills for K and Q.
- **Motion:** Bounce stretches and tilts the letter; win swells it while the sweep crosses and the gem pops.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 4 to 6 bones each: letter, gem, light sweep.
- **Notes:** The 10 has no gem.
- **Skeleton (from the file):** Spine 3.8.99 · 5 bones · 5 slots · 4 region, 1 clipping · animations: bounce (0.83 s), win (0.8 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 43% · saturation 72% · contrast 70% · warm 30% / cool 50% · brighter towards: top (4), top-left (3)
- **Palette (measured):** #261035 dark purple 12%, #dd3485 magenta 10%, #bc183b red 9%, #0d46b7 blue 9%, #6e18c0 purple 8%, #f8eef9 light magenta 7%

### Collect hammer

`B3` · skeleton · 8 parts · largest 481×114 · sheet `sheets/B3.webp`

- **Role:** The symbol that collects the values of the pigs in view.
- **Subject:** A fat pink mallet whose head ends in a pig's snout, with a wooden handle and gold ferrule, on a cyan sunburst tile, the word COLLECT below.
- **Style:** Toy cartoon, same family as the pigs.
- **Rendering:** Smooth pink gradients with a pale top highlight; pink outlined bubble lettering.
- **Colour:** Pink (#c61b73 and lighter) on cyan (#08f9f1 29%, #03c3bc); gold frame.
- **Lighting:** Top light; an edge-light sprite on the head and a smear sprite for the swing.
- **Ambience:** Playful threat: a toy hammer for breaking piggy banks.
- **Materials:** Rubber or painted wood (inference from the soft highlights), wood, gold.
- **Variants:** B3_Reversed is the same rig facing the other way.
- **Motion:** Bounce tilts the hammer; collect lifts it out of the tile, swings it up to the corner and brings it down; the word fades out for the swing and back in after.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 8 bones, 8 slots: whole hammer, separate head and handle for the swing, smear and edge light.
- **Notes:** The snout on the hammer head ties the tool to the pig theme without drawing a second character.
- **Skeleton (from the file):** Spine 3.8.99 · 8 bones · 8 slots · 8 region · animations: bounce (0.83 s), collect (0.83 s), collect_intro (0.5 s), collect_outro (0.5 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 58% · saturation 78% · contrast 55% · warm 46% / cool 40% · brighter towards: right (1), top-left (1), bottom (1)
- **Palette (measured):** #08f9f1 cyan 29%, #4a1111 dark red 8%, #c61b73 magenta 8%, #03c3bc cyan 7%

### Pink piggy bank (cash symbol), rig

`B1_Normal` · skeleton · 26 parts · largest 1641×1804 · sheet `sheets/B1_Normal.webp`

- **Role:** The cash symbol in its ordinary form: a pink pig on a cyan tile that carries a money value and is smashed when collected.
- **Subject:** A round pink ceramic pig in three-quarter view with a big snout, a purple dollar sign on its flank, a coin in its slot, a red curly tail, on a gold-framed cyan sunburst tile.
- **Style:** Rounded toy cartoon, soft 3D-look, no outline.
- **Rendering:** Airbrushed volume with a glossy top highlight and a darker magenta underside; sleepy half-closed purple eyes drawn as a separate layer.
- **Colour:** Pink body (#f676b7 37%, #b12f62 39% in shade), cyan tile, gold frame; measured 70% magenta hue.
- **Lighting:** Top-left key (measured), white gloss on the back, separate additive 'Light' and 'Light Hit' overlays for the flash.
- **Ambience:** Cute and calm; the pig looks pleased rather than excited.
- **Materials:** Glazed ceramic, gold coin, a pile of gold coins inside.
- **Variants:** The gold pigs (B1_Enhanced, the XL rig) are the upgraded forms; a dim still exists.
- **Motion:** Seen in the frames: bounce squashes and lifts the pig out of the tile; idle is a slow breathing bob; collect cracks the body, breaks it into 14 shards and leaves a heap of gold coins on the tile.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 30 bones, 28 slots; the break is 14 separate shard sprites plus two crack overlays, a bottom half and a coin heap.
- **Notes:** The shards are cut from the same painting as the whole pig, so the break needs the pig drawn once and sliced. The game screens 08 to 10 show the collect in play: pigs turn to coins and leave broken shells with coin heaps.
- **Skeleton (from the file):** Spine 3.8.99 · 30 bones · 28 slots · 2 clipping, 26 region · animations: bounce (0.83 s), collect (0.83 s), idle (0.83 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 45% · saturation 63% · contrast 44% · warm 64% / cool 2% · brighter towards: top-left (7), top-right (4), right (2)
- **Palette (measured):** #b12f62 red 39%, #f676b7 magenta 37%, #dc4a89 magenta 10%, #691b53 dark magenta 4%, #fdb6db light magenta 4%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Pot pig above the reels (five growth stages)

`Pots` · skeleton · 47 parts · largest 900×900 · sheet `sheets/Pots.webp`

- **Role:** The character over the board that fattens as cash symbols land and bursts into the feature (read from its animation names PotLvl0 to PotLvl4 and Activate).
- **Subject:** A pink piggy bank in four sizes, each fatter, with coins and then notes sticking out, and a fifth, gold, cracked pig with money bursting from it.
- **Style:** The game's toy cartoon; this is its mascot.
- **Rendering:** Airbrushed ceramic with pale gloss; sleepy purple eyes on their own layer; the gold stage has cracks and a starburst.
- **Colour:** Pink (#f775b7, #b63065) through to gold (#f4d323, #b7800b); a pale pink flash layer makes up 30% of the measured area (#fbe3ea).
- **Lighting:** Top light; every stage has a 'Light' and a 'LightHit' flash copy.
- **Ambience:** Anticipation told by a body: the fuller the pig, the nearer the feature.
- **Materials:** Glazed ceramic, gold, paper notes, coins.
- **Variants:** Five stages; a second rig (PotsOverReels) plays the last stage's burst in front of the reels.
- **Motion:** Seen in the frames: each level has a still, a jump, a hit and a four-second idle (a slow bob and blink); level 4 turns gold and Activate breaks it into shards.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 50 bones, 44 slots, 20 animations; the gold stage has 14 shard sprites.
- **Notes:** The frame shown is the level 4 idle; 12 parts of it belong to the wheel pig's rig and are missing from the drawing, so the game screens are the reference.
- **Skeleton (from the file):** Spine 3.8.99 · 50 bones · 44 slots · 3 clipping, 65 region, 5 mesh · animations: PotLvl1 (0.83 s), PotLvl1Jump (0.83 s), PotLvl1Static (0.0 s), PotLvl1_Idle (4.17 s), PotLvl2 (0.83 s), PotLvl2Jump (0.83 s), PotLvl2Static (0.0 s), PotLvl2_Idle (4.17 s), PotLvl3 (0.83 s), PotLvl3Jump (0.83 s), PotLvl3Static (0.0 s), PotLvl3_Idle (4.17 s), PotLvl4 (0.83 s), PotLvl4Jump (0.83 s), PotLvl4Static (0.0 s), PotLvl4_Activate (0.83 s), PotLvl4_Idle (0.83 s), PotLvl0Jump (0.83 s), PotLvl0Static (0.0 s), PotLvl0_Idle (4.17 s)
- **Measured:** bright, saturated, warm, medium contrast, strong highlights · brightness 66% · saturation 53% · contrast 42% · warm 75% / cool 2% · brighter towards: top-left (7), top (2), top-right (1)
- **Palette (measured):** #fbe3ea light red 30%, #f775b7 magenta 16%, #b63065 red 12%, #b7800b orange 10%, #f4d323 gold 8%, #794f09 brown 4%

### Wheel pig (bonus, gold)

`WheelCharacterBonus` · skeleton · 8 parts · largest 686×632 · sheet `sheets/WheelCharacterBonus.webp`

- **Role:** The same mascot in the bonus, turned gold.
- **Subject:** A gold pig seen from the front with a gold snout, a yellow starburst behind and notes around.
- **Style:** Toy cartoon.
- **Rendering:** Yellow-to-brown gold gradients with white glints.
- **Colour:** Gold (#fbf266 51%, #f2cd12, #835208) with green notes.
- **Lighting:** Top light and a large additive glow behind.
- **Ambience:** Jackpot mood.
- **Materials:** Polished gold.
- **Variants:** Gold twin of the pink wheel pig; shares its coin and cash sprites.
- **Motion:** Not drawn here (incomplete without the shared parts). By the file: the pink pig's animations plus Intro2 and Outro2.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 22 bones, 18 slots.
- **Notes:** Pink in the base game and gold in the bonus is the game's one rule for every pig.
- **Skeleton (from the file):** Spine 3.8.99 · 22 bones · 18 slots · 14 region, 3 mesh · animations: IdleLoop (3.0 s), Intro (0.93 s), Intro2 (0.93 s), Outro (0.83 s), Outro2 (0.83 s), SpinAward (1.17 s), SpinIdle (1.67 s), SpinIntroClockwise (1.17 s), Static (0.0 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 76% · saturation 69% · contrast 38% · warm 88% / cool 6% · brighter towards: top (2), top-right (1)
- **Palette (measured):** #fbf266 gold 51%, #f2cd12 gold 11%, #835208 brown 9%, #c89305 orange 7%, #fff8c3 light gold 6%, #377d22 green 6%

### Wheel pig (base game)

`WheelCharacter` · skeleton · 10 parts · largest 296×311 · sheet `sheets/WheelCharacter.webp`

- **Role:** The pig that sits on top of the reel frame in front of the vault and looks down at the board.
- **Subject:** A round pink pig seen from the front, snout forward, on a pile of notes, coins and gold bars, with a red curly tail.
- **Style:** Toy cartoon, front view.
- **Rendering:** Smooth pink sphere shading, a separate glossy snout and eyes.
- **Colour:** Pink (#f367ac, #a0264a) with green money (#69bc41, #2c6f1d).
- **Lighting:** Top light, soft.
- **Ambience:** A watching mascot.
- **Materials:** Ceramic, paper, gold.
- **Variants:** A gold version exists for the bonus (WheelCharacterBonus).
- **Motion:** Not drawn here (the frame came out without the snout, which is its own rig laid in front of the reel frame). By the file: IdleLoop 3 s, Intro, Outro, SpinIntroClockwise, SpinIdle 1.67 s, SpinAward.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 17 bones, 14 slots; the snout is a second skeleton (WheelCharacterInFront) so that it can overlap the reel frame.
- **Notes:** See the base-game screens for how it looks whole.
- **Skeleton (from the file):** Spine 3.8.99 · 17 bones · 14 slots · 3 mesh, 10 region · animations: IdleLoop (3.0 s), Intro (0.83 s), Outro (0.83 s), SpinAward (1.17 s), SpinIdle (1.67 s), SpinIntroClockwise (1.17 s), Static (0.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 50% · saturation 67% · contrast 51% · warm 41% / cool 24% · brighter towards: top (4), top-right (1)
- **Palette (measured):** #f367ac magenta 22%, #69bc41 green 21%, #2c6f1d dark green 17%, #a0264a red 10%, #c93a73 red 7%, #b86d20 orange 6%


## Logo and title

The game's own wordmark.

### Loading screen, intro pages and static logo

`loading-and-intro` · atlas · 11 parts · largest 1080×1920 · sheet `sheets/loading-and-intro.webp`

- **Role:** What the player sees before the reels.
- **Subject:** The vault hall with the logo across the top, a navy panel for the feature pages, heart-shaped navy arrows with gold rims, and small copies of three feature symbols.
- **Style:** As the backgrounds and logo.
- **Rendering:** As the backgrounds.
- **Colour:** Navy and violet (#454362, #17153d) with gold.
- **Lighting:** As the backgrounds.
- **Ambience:** An invitation; the feature pages are videos.
- **Materials:** Not applicable to this piece.
- **Variants:** Landscape and portrait.
- **Motion:** None in these pictures; the five intro pages play video clips (960x504 at the 0.5 pack, 15 fps by the manifest), which this capture's browser showed as black boxes.
- **Construction:** Single pictures.
- **Notes:** The full logo with SUPERWHEEL in gold is here as one picture (GameIntro_GameLogo).
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 47% · saturation 49% · contrast 78% · warm 52% / cool 44% · brighter towards: bottom (2), top-right (2), top (1)
- **Palette (measured):** #454362 blue 17%, #17153d dark blue 15%, #72708b grey 11%, #b8b4b5 grey 10%, #f2e9af light gold 7%, #ecd369 gold 6%

### Logo

`LogoHorizontal` · skeleton · 13 parts · largest 2400×479 · sheet `sheets/LogoHorizontal.webp`

- **Role:** The game's wordmark.
- **Subject:** BIGGER PIGGY in fat pink balloon letters, a gold pig between the words, BANK in green letters made of banknotes with a snout in the A, notes fanning behind.
- **Style:** Balloon lettering with objects set into it.
- **Rendering:** Each word a glossy, thickly outlined shape with a dark plum shadow plate behind.
- **Colour:** Pink (#f868ce), green (#64c639, #38801c), gold, on a plum plate (#742851).
- **Lighting:** Top gloss on each letter; star glints and a light sweep.
- **Ambience:** Loud, sweet, instantly readable.
- **Materials:** Glossy plastic letters, paper-money letters, gold.
- **Variants:** Horizontal and stacked ('semi-horizontal') builds; the SUPERWHEEL line in gold is only in the static intro logo.
- **Motion:** Idle (1 s): the gold pig bobs, a sweep crosses the words and stars twinkle.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 16 bones, 14 slots.
- **Notes:** Three words, three materials: the logo states the palette of the whole game.
- **Skeleton (from the file):** Spine 3.8.99 · 16 bones · 14 slots · 13 region, 1 clipping · animations: Idle (1.0 s), Static (0.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 34% · saturation 65% · contrast 25% · warm 43% / cool 9% · brighter towards: top (2), top-left (1)
- **Palette (measured):** #742851 magenta 68%, #64c639 green 7%, #38801c green 7%, #f868ce magenta 5%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature panels

`modals` · atlas · 9 parts · largest 1320×1920 · sheet `sheets/modals.webp`

- **Role:** Backings for the bonus entry, free spins and Fortune Bet messages.
- **Subject:** Purple radial backdrops, a navy panel with gold rim, a gold-studded panel patterned with snouts, a panel with a rainbow wheel rising from its base, and the Fortune Bet toggle.
- **Style:** Panels in the game's navy and gold.
- **Rendering:** Flat dark fields with soft radial light.
- **Colour:** Deep purple (#4a0379 43%, #7912b9) and near black (#0b0623).
- **Lighting:** Centre glow.
- **Ambience:** A hush before a prize.
- **Materials:** Not applicable to this piece.
- **Variants:** Landscape and portrait.
- **Motion:** None.
- **Construction:** Single pictures up to 1920x1080 at this pack.
- **Notes:** Text is set by the client in the Borsok font.
- **Measured:** dark, vivid, cool, medium contrast, hard-edged · brightness 14% · saturation 91% · contrast 32% · warm 22% / cool 78% · brighter towards: bottom (3), top (2)
- **Palette (measured):** #4a0379 dark purple 43%, #0b0623 black 34%, #7912b9 purple 10%, #e6830a orange 2%

### Win titles and counter digits

`big-win` · atlas · 22 parts · largest 789×216 · sheet `sheets/big-win.webp`

- **Role:** The celebration words and the digits of the counting win.
- **Subject:** NICE WIN, BIG WIN, HUGE WIN, MEGA WIN and EPIC WIN, the four prize names and BONUS COMPLETE as lettering; fat yellow digits with a magenta drop edge.
- **Style:** Bubble lettering.
- **Rendering:** Each tier more dressed: white for Nice and Big, pink for Huge, pink with coins for Mega, green with notes for Epic.
- **Colour:** White (#fcf9ee), pink, green (#4bb831), purple (#9b27df), blue (#3899f9) on plum outlines (#311c44).
- **Lighting:** Top gloss.
- **Ambience:** Escalating sweetness.
- **Materials:** Glossy plastic.
- **Variants:** Five tiers; six languages in the manifest (English loaded).
- **Motion:** None in the pictures; placed and scaled by the client.
- **Construction:** One sprite a word, ten digits and two separators.
- **Notes:** Tier is told by colour and by what is stuck on the letters.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 50% · saturation 59% · contrast 78% · warm 44% / cool 39% · brighter towards: top (16), top-left (1)
- **Palette (measured):** #311c44 dark purple 16%, #fcf9ee light gold 11%, #792753 magenta 6%, #530d1d dark red 5%, #4bb831 green 5%, #9b27df purple 4%

### Feature explainer panel

`ModelPanels` · skeleton · 5 parts · largest 765×765 · sheet `sheets/ModelPanels.webp`

- **Role:** The animated panel that shows how pigs, hammer and pots work.
- **Subject:** Its own parts are a small wheel face, a prize panel and three value labels; the rest it borrows from the symbol rigs.
- **Style:** As the symbols.
- **Rendering:** As the symbols.
- **Colour:** Gold, red, green, blue.
- **Lighting:** Not applicable to this piece.
- **Ambience:** Tutorial.
- **Materials:** Not applicable to this piece.
- **Variants:** Landscape, portrait and golden free spins versions.
- **Motion:** Not drawn here: 47 of its parts belong to other rigs. By the file: four 4.2 s animations.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 95 bones, 87 slots.
- **Notes:** It reuses the symbol art rather than shipping a video.
- **Skeleton (from the file):** Spine 3.8.99 · 95 bones · 87 slots · 6 clipping, 120 region, 1 path · animations: Landscape (4.2 s), LandscapeGoldenFS (4.2 s), Portrait (4.2 s), PortraitGoldenFS (4.27 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 52% · saturation 70% · contrast 73% · warm 69% / cool 23% · brighter towards: bottom-left (1)
- **Palette (measured):** #c9ac3f gold 12%, #af6111 brown 10%, #cc0c0a red 8%, #17e018 green 5%, #fcf9ec light gold 5%, #0e54e4 blue 4%

### Bring Home The Bacon burst

`BringHomeTheBacon` · skeleton · 27 parts · largest 1700×995 · sheet `sheets/BringHomeTheBacon.webp`

- **Role:** A celebration burst (when it plays was not seen).
- **Subject:** The words BRING HOME THE BACON stacked in pink and green with two gold pigs, a gold starburst, and rashers of bacon, notes and coins flying out.
- **Style:** The game's lettering and toy objects.
- **Rendering:** Motion-blurred copies of coins, notes and bacon; a large soft glow.
- **Colour:** Gold and brown glow (#f4d360, #875028) with pink (#f3529c).
- **Lighting:** A central burst lights everything.
- **Ambience:** A joke told loudly.
- **Materials:** Bacon, paper, gold.
- **Variants:** None.
- **Motion:** 2.13 s: the title pops, the burst throws the pieces outward, the title fades.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 65 bones, 53 slots; three short frame sequences.
- **Notes:** Bacon as confetti is the game's one plain joke on its own theme.
- **Skeleton (from the file):** Spine 3.8.99 · 65 bones · 53 slots · 53 region · animations: animation (2.13 s)
- **Measured:** mid-tone, vivid, warm, high contrast, glow or soft effect, strong highlights · brightness 56% · saturation 64% · contrast 66% · warm 84% / cool 5% · brighter towards: top (3), top-left (1)
- **Palette (measured):** #875028 brown 29%, #f4d360 gold 16%, #bb8623 orange 13%, #fff9ee light orange 8%, #f3529c magenta 5%, #f3a306 orange 4%

### Super Bonus and Super Wheel titles

`GoodFortune` · skeleton · 5 parts · largest 707×207 · sheet `sheets/GoodFortune.webp`

- **Role:** The pop-up when the shared wheel awards.
- **Subject:** SUPER BONUS and SUPER WHEEL in gold block capitals with a red extruded side, over yellow bokeh spots.
- **Style:** Game-show block lettering.
- **Rendering:** Bevelled gold with a hot white face.
- **Colour:** Gold (#faeb1d, #d79711) with brown and red edges.
- **Lighting:** Emissive, sparkles.
- **Ambience:** Jackpot television.
- **Materials:** Gold.
- **Variants:** Two titles.
- **Motion:** 3 s: the word drops in small, swells, holds and fades among drifting light spots.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 44 bones, 41 slots, 38 additive.
- **Notes:** Block capitals, not bubble letters: the shared wheel keeps its own type.
- **Skeleton (from the file):** Spine 3.8.99 · 44 bones · 41 slots · 41 region · animations: SuperBonusWon_PopUp (3.0 s), SuperWheelWon_PopUp (3.0 s)
- **Measured:** bright, vivid, warm, high contrast, strong highlights · brightness 63% · saturation 78% · contrast 86% · warm 100% / cool 0%
- **Palette (measured):** #faeb1d gold 27%, #673408 brown 21%, #d79711 orange 19%, #fffdc8 light gold 12%, #fdf780 gold 6%, #130402 black 5%


## Effects

Frame sequences, glows, particles and transitions.

### Collection coins

`PotCollection` · skeleton · 90 parts · largest 90×90 · sheet `sheets/PotCollection.webp`

- **Role:** The coin that flies from a symbol to a prize panel.
- **Subject:** A snout coin spinning on its vertical axis, in gold and in the four prize colours.
- **Style:** Small 3D-look coin.
- **Rendering:** Pre-rendered turn, 18 frames a colour.
- **Colour:** Gold, red, purple, green, blue.
- **Lighting:** Glossy.
- **Ambience:** Quick reward.
- **Materials:** Metal.
- **Variants:** Five colours.
- **Motion:** 0.7 s: the coin turns once while it grows and shrinks.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 90 frames of 90x90.
- **Notes:** Nothing further.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 5 slots · 86 region · animations: PotCollection (0.7 s), PotCollectionGrand (0.7 s), PotCollectionMajor (0.7 s), PotCollectionMini (0.7 s), PotCollectionMinor (0.7 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 71% · saturation 59% · contrast 52% · warm 44% / cool 43% · brighter towards: right (1), bottom (1)
- **Palette (measured):** #fae465 gold 12%, #f9cbfc light magenta 11%, #b1e8fd light cyan 9%, #c2fe95 light green 8%, #e54d29 red 7%, #fdc292 light orange 7%

### Anticipation flames

`SuperWheel_Trigger_Anticipation` · skeleton · 4 parts · largest 180×560 · sheet `sheets/SuperWheel_Trigger_Anticipation.webp`

- **Role:** Heats a reel when the shared wheel may trigger.
- **Subject:** A column of orange and red flame, a gold reel overlay, a red burst and thin frame glows.
- **Style:** Soft effect art.
- **Rendering:** Blurred additive shapes.
- **Colour:** Orange (#fda502 53%), gold, red (#d81003).
- **Lighting:** Emissive.
- **Ambience:** Tension.
- **Materials:** Fire, light.
- **Variants:** Not applicable to this piece.
- **Motion:** 2.07 s loop of rising flame.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 13 bones, 8 additive slots.
- **Notes:** Nothing further.
- **Skeleton (from the file):** Spine 3.8.99 · 13 bones · 9 slots · 44 region, 1 clipping · animations: SW_Trigger_Anticipation (2.07 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 68% · saturation 88% · contrast 35% · warm 100% / cool 0%
- **Palette (measured):** #fda502 orange 53%, #feec45 gold 15%, #d81003 red 13%, #fedc0f gold 9%, #fffff1 light gold 5%, #fdf39c light gold 2%

### Reel edge sparkle

`reel-anim` · atlas · 17 parts · largest 234×567 · sheet `sheets/reel-anim.webp`

- **Role:** A sparkling outline that runs round a reel.
- **Subject:** A tall rectangle traced in green and gold sparks with small coins.
- **Style:** Particle effect.
- **Rendering:** Soft.
- **Colour:** Green (#5a992c) and gold (#f0de54).
- **Lighting:** Emissive.
- **Ambience:** Not applicable to this piece.
- **Materials:** Not applicable to this piece.
- **Variants:** Not applicable to this piece.
- **Motion:** 17 frames.
- **Construction:** Frame sequence, 234x567.
- **Notes:** Nothing further.
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, glow or soft effect · brightness 63% · saturation 71% · contrast 55% · warm 49% / cool 26%
- **Palette (measured):** #5a992c green 42%, #f0de54 gold 23%, #b89218 gold 12%, #397219 dark green 6%, #ebce19 gold 5%, #aabd42 yellow 5%

### Big-win gems

`win-gems` · atlas · 37 parts · largest 150×147 · sheet `sheets/win-gems.webp`

- **Role:** Gems that fall during big wins.
- **Subject:** A diamond, a ruby and an emerald tumbling, and a snout coin.
- **Style:** 3D-look render, more realistic than the rest.
- **Rendering:** Faceted, pre-rendered turns of 12 frames.
- **Colour:** White, red (#e80806), green (#32db0a).
- **Lighting:** Sharp speculars.
- **Ambience:** Luxury confetti.
- **Materials:** Cut stone.
- **Variants:** Three gems.
- **Motion:** 12 frames each.
- **Construction:** Frame sequences about 150 px.
- **Notes:** The gems are the one place the game leaves its toy look.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 57% · saturation 61% · contrast 37% · warm 68% / cool 17% · brighter towards: top (4), top-right (3), top-left (3)
- **Palette (measured):** #e8efe6 light green 21%, #e80806 red 15%, #ced0ba light yellow 12%, #3a970c green 10%, #a40203 red 10%, #32db0a green 8%


## Game interface

Buttons, counters and panels drawn for this game.

### Super Wheel interface

`super-wheel-interface` · atlas · 27 parts · largest 638×666 · sheet `sheets/super-wheel-interface.webp`

- **Role:** Buttons and panels of the shared wheel: open, back, players, stake tabs, help pictures.
- **Subject:** Red glowing rounded buttons with gold icons (wheel, arrow, players, X), red tabs and bars, the PLAYER LINK badge, two help pictures.
- **Style:** Flat arcade interface.
- **Rendering:** Flat red with an outer glow, gold pictograms.
- **Colour:** Red (#c90402 37%) and gold (#f8c010).
- **Lighting:** Self-lit glow.
- **Ambience:** Urgent, casino-floor red.
- **Materials:** Lit plastic.
- **Variants:** Active and idle states.
- **Motion:** None.
- **Construction:** Single sprites.
- **Notes:** Red here against the navy and pink of the game marks the wheel as a separate, shared feature (inference).
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 43% · saturation 82% · contrast 48% · warm 87% / cool 6% · brighter towards: top (7), left (2), top-left (1)
- **Palette (measured):** #c90402 red 37%, #f8c010 gold 14%, #fefbed light gold 8%, #300100 black 6%, #780804 dark red 4%, #db8310 orange 4%

### Meters and bars

`meters-and-bars` · atlas · 6 parts · largest 528×102 · sheet `sheets/meters-and-bars.webp`

- **Role:** Win, total win and spins-left bars.
- **Subject:** Dark rounded bars with thin gold edges.
- **Style:** Minimal.
- **Rendering:** Flat.
- **Colour:** Near black (#04131b) with gold hairlines.
- **Lighting:** None.
- **Ambience:** Out of the way.
- **Materials:** Not applicable to this piece.
- **Variants:** Landscape and portrait.
- **Motion:** None.
- **Construction:** Single sprites.
- **Notes:** Nothing further.
- **Measured:** dark, vivid, warm and cool mixed, high contrast, hard-edged · brightness 19% · saturation 85% · contrast 63% · warm 58% / cool 39% · brighter towards: top (2), top-right (2)
- **Palette (measured):** #04131b black 73%, #9b5b15 brown 9%, #c59d5c orange 6%, #408120 green 2%

### Prize panels

`GrandPot` · skeleton · 40 parts · largest 533×246 · sheet `sheets/GrandPot.webp`

- **Role:** The four fixed prize boxes over the reels.
- **Subject:** Glossy rounded rectangles in red, purple, blue and green with the prize name in outlined letters on top, small coin slots and snout coins that fill them, and small pigs for pot levels.
- **Style:** Candy panels.
- **Rendering:** Glass-like gradient with a light upper edge and gold hairline.
- **Colour:** Red (#bb0505), purple (#510297, #7a07ce), green (#03ad0b), blue.
- **Lighting:** A light sweep on change.
- **Ambience:** Arcade scoreboard.
- **Materials:** Glossy plastic.
- **Variants:** Base and bonus backings, landscape and portrait.
- **Motion:** Each panel flashes pale gold and settles (0.83 s).
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 4 bones each.
- **Notes:** The multiplier text (1000X and so on) is drawn by the client's font, not painted.
- **Skeleton (from the file):** Spine 3.8.99 · 4 bones · 3 slots · 1 clipping, 5 region · animations: Base_L (0.83 s), Base_P (0.83 s), Bonus_L (0.83 s), Bonus_P (0.83 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 41% · saturation 77% · contrast 57% · warm 46% / cool 40% · brighter towards: top-right (15), top-left (4), right (4)
- **Palette (measured):** #bb0505 red 13%, #510297 purple 9%, #03ad0b green 6%, #fae58e light gold 5%, #7a07ce purple 5%, #03e018 green 4%

### Super Wheel segment cards and spin button

`SuperWheel_Segment` · skeleton · 12 parts · largest 406×220 · sheet `sheets/SuperWheel_Segment.webp`

- **Role:** The value cards of the Super Wheel and its red spin button.
- **Subject:** Tall white tapered cards with red stacked numerals (20x to 50x), a BONUS card with a gold S, a blue diamond backing and a round red spin button.
- **Style:** Graphic, game-show.
- **Rendering:** Flat white card, outlined red numerals with a light bevel.
- **Colour:** White-gold (#fefde8, #fede65) and red (#d91506).
- **Lighting:** Additive glow copies of the text.
- **Ambience:** Bright and blunt.
- **Materials:** Card, enamel.
- **Variants:** Four values and the bonus.
- **Motion:** Upgrade animations (1.87 s) swap a card's value with a flash.
- **Construction:** Spine 3.8.99 skeleton as JSON inside the client's data manifest; parts are trimmed sprites on shared atlas pages at 0.75 of the studio's size. 19 bones, 27 slots, 10 additive.
- **Notes:** Nothing further.
- **Skeleton (from the file):** Spine 3.8.99 · 19 bones · 27 slots · 19 region, 8 clipping · animations: SB_Upgrade (1.87 s), SV1-SB_Upgrade (1.87 s), SV1_Segment_Upgrade (1.87 s), SV2-SB_Upgrade (1.87 s), SV2_Segment_Upgrade (1.87 s), SV3-SB_Upgrade (1.87 s), SV3_Segment_Upgrade (1.87 s), SV4-SB_Upgrade (1.87 s), SV4_Segment_Upgrade (1.87 s)
- **Measured:** bright, saturated, warm, medium contrast, strong highlights · brightness 68% · saturation 55% · contrast 41% · warm 88% / cool 3% · brighter towards: top-left (1)
- **Palette (measured):** #fefde8 light gold 29%, #d91506 red 22%, #fede65 gold 19%, #fef5aa light gold 9%, #f93538 red 6%, #fa8205 orange 2%

### Gamble wheel

`gamble-wheel` · atlas · 24 parts · largest 424×425 · sheet `sheets/gamble-wheel.webp`

- **Role:** The optional gamble after a win: a red and green wheel with adjustable odds.
- **Subject:** A dark disc with gold and silver rims, red and green halves, a gold pointer, plus-minus arrows in navy with gold rims, round GAMBLE ON, OFF and 5X+ buttons.
- **Style:** Flat interface with gold trim.
- **Rendering:** Flat fills, thin bevels.
- **Colour:** Near black (#071120 51%) with red (#e70814) and green (#0c9a07).
- **Lighting:** None.
- **Ambience:** Plain, functional.
- **Materials:** Not applicable to this piece.
- **Variants:** On, off and 5x states; a portrait logo.
- **Motion:** None in these pictures.
- **Construction:** Single sprites.
- **Notes:** Named DualWheelGamble and unthemed apart from a snout coin and the logo: probably Inspired's shared gamble dressed for this game (inference; not checked against a second Inspired game).
- **Measured:** dark, vivid, warm and cool mixed, medium contrast · brightness 24% · saturation 74% · contrast 48% · warm 38% / cool 41% · brighter towards: top (5), bottom (2), left (2)
- **Palette (measured):** #071120 black 51%, #0a5f04 dark green 6%, #aa6310 brown 6%, #e70814 red 6%, #a00511 red 5%, #610710 dark red 4%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `inspired-shared-interface`: 69 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Alegreya Sans (Black); Arial Black (Regular); Barlow Semi Condensed (Bold); Borsok (Regular); Helvetica Neue Condensed (Condensed Bold); Helvetica Neue Condensed Black (Condensed Black); ITC Eras (Bold); Paddy Mischief (Bold); Roboto (Bold); Rockwell Extra Bold (Regular); Tahoma (Bold); Unna (Bold); Unna (Bold Italic).

## How this was made, and its limits

- The demo was opened in a browser at 1920×1080 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 895 components cut from 37 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
