# 777 Hot Reels Megacharged: art report

octoplay · run `2026-11-26-2217-octoplay-777-hot-reels-megacharged` · captured 2026-11-26

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/777-hot-reels-megacharged

**Extracted:** 603 named components from 37 textures in 37 atlases; 46 Spine skeletons; 22 frame sequences (398 frames); 3 fonts. Grouped into 26 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A classic fruit-and-sevens machine staged as a neon cabinet flying through giant 3D 777 signs: the whole game is three colours of one flaming seven, each tied to a jackpot of its colour, on a backdrop that flips from purple night to orange blaze.

**Style.** Glossy sticker-like symbols with gold keylines, Western slab-serif lettering, and neon line work, on an abstract backdrop of light rays. The only solid scenery is a set of pre-rendered 777 blocks in steep perspective. Nothing is a character and nothing is a place.

**Rendering.** Smooth airbrushed enamel with one hard glint on symbols; flat neon outlines with glow for plaques, frames and jackpot wins; flat two-tone cartoon fire and white lightning for effects; soft gradient rays for the ground. Every symbol carries its own keyline and halo.

**Colour.** Measured over the game's art: near-black purple #1f0a2c 27%, red #9d2117 14%, orange #e96d0f 13%, gold #f9c013 11%, light golds #fdfbf3 and #fbed86 9% together, hot red #f11f07 3%, dark blue #0c0872 1%. The code is three hues: blue for the single seven and MINI, purple for the double seven and MINOR, red for the triple seven and MAJOR, repeated on symbol, plaque, jackpot win, gem and particle. Gold is the Wild, the frame, the logo and every amount. Cyan appears only as electricity.

**Lighting.** Almost everything is self-lit: neon, lamps behind plates, fire. Symbols have a conventional upper-left light and a warm halo. The backdrop's light comes from one vanishing point behind the cabinet.

**Ambience.** A machine in a dark club, humming with neon, that catches fire when a feature starts. The base game is cool and purple, Free Spins and the intro are orange and red; the cabinet itself does not change.

**Shape language.** The seven above all: as symbol, jackpot plaque silhouette, win plate, 3D block and logo. Around it a pinched cabinet outline, chevrons, diamonds on the win lines, thin dotted bulb lines, fat slab letters.

**Materials.** Enamel, polished gold, neon tube, back-lit glass, fruit skin, cut gems, fire, electric arc.

**Typography and lettering.** One voice: fat Western slab serifs. Drawn words for the logo, WILD, FREE SPINS, the jackpot names and the win tiers (gold to orange with a dark blue shadow); three bitmap numeral fonts from the provider's shared font store (UltraGold large, UltraActive and UltraInactive small). The help, the buttons and the balance line are the shell's Poppins.

**Motion.** All motion is Spine: 46 skeletons in two bundle files (44 in 4.2.43, two particle layers in 4.1.24), most of them scene layers and effects moving still pictures, with 22 hand-drawn frame sequences (398 frames: outline traces, fire, lightning, tumbling gems, a turning coin, the logo burning). Seen in play: the logo breaking up among coins after START, neon frames breathing, 777 blocks drifting behind the cabinet, cyan arcs on the frame and bolts at the jackpots, a gold seven flying from a Wild to the plaques, a lightning column on the last reel before a trigger, three sevens turning red on the splash, fire across the screen into Free Spins, Wilds locking, a BIG WIN and a MINOR jackpot win with gold rays and coins. No skeleton frame is shown in this report, because the project's renderer is written for Spine 3.7; assembled and motion pictures are absent for that reason only.

**Variants and themes.** Two backdrop states (Normal, Special) for the ground and for each of eight 777 block views; one seven in four colourings (blue, purple, red, gold) and three counts; three jackpot plaques and three jackpot win plates from one idea; three win tiers and a total from one layout; lit and unlit paytable plates and numerals.

**How it is built.** Three 4096 px atlas pages hold 518 sprites, with two of the pages roughly half empty; the ground is a mirrored half; words are separate from what they label, and six lettering files are localised (en-GB). The paytable pictures, the help logo, the buy card, the numeral fonts, the Double Chance card, the controls and Poppins come from the provider's shared services. Compared with Fire Rail Express (run 2026-11-26-1556) from the files: the shell, Poppins and the Double Chance card are the same; 40 sprites are pixel for pixel the same (36 white flame frames, the white starburst, a glow, a glow square, a white box); 23 of the 46 skeleton names are the same (Backgrounds, Logo, SlotFrame, Jackpot, WinBig, WinTotal, TileWild and others), which points to one scene template; the pictures under shared names such as bgNormal, bgSpecial and jackpotFrame are different. Everything that carries the theme is this game's own.

**Consistency.** Very high, by economy: one seven, one letter style, three hues and gold. The one piece outside the system is the painted buy card, and it shows the same cast.

**What to take from it.** (1) One drawing can be a whole high-symbol set: a single flaming seven, recoloured three times and repeated one, two or three times, gives the ranks, and the same seven in gold is the Wild and the logo. (2) Tie each top symbol to a prize by colour and by shape: blue 7 to the blue one-seven MINI plaque, purple 77 to MINOR, red 777 to MAJOR. The rule is readable without a word. (3) Put the paytable on the machine. The cabinet shows every pay above the reels and lights the winning row, so a small 5x3 area sits inside a rich, always-informative object. (4) A sequel or a 'charged' version can be made with little new art: two extra words on the logo, 25 white lightning frames tinted cyan and a jackpot row carry the difference. (5) Build the environment from light instead of scenery: two mirrored ray pictures, a few white line pieces tinted in the game and eight pre-rendered views of one 3D sign give depth and constant movement with almost no painting. (6) Change one thing for the feature and change it completely: the ground flips from purple to orange and the blocks from purple to gold, while the cabinet stays, so the player never loses the board. (7) Keep an effect library in white and tint it per game: the flame frames here are the same files as in Fire Rail Express. Bake colour only where tint would flatten form (the gems). (8) For AI art work: the painted content is tiny (four fruits, one seven, one crown, one key-art card). The value is in the system around it, so the brief should fix the three hues and gold (#0b37b7 blue, #c366f7 purple, #c50b05 red, #f9c013 gold), the keyline-and-halo treatment and the slab lettering before any picture is made.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast · brightness 37% · saturation 77% · contrast 44% · warm 62% / cool 26% · brighter towards: top (67), top-right (28), top-left (23)

Palette: #200b2b black 30%, #ec750f orange 19%, #9d1f18 red 15%, #fbcc16 gold 6%, #fefdf8 light gold 5%, #f11f07 red 4%, #fbee86 light gold 3%, #c64c13 orange 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 2 | 27% | 83% | 29% | 62% / 28% | #210b2e black 40%, #e8730e orange 24%, #9e1e19 red 23% |
| Reel board | 1 | 27% | 70% | 55% | 51% / 36% | #190a1c black 49%, #4e1016 dark red 13%, #fbd552 gold 7% |
| Symbols | 5 | 44% | 70% | 86% | 63% / 30% | #f0ae1c orange 11%, #190956 dark blue 10%, #0e0514 black 10% |
| Logo and title | 3 | 55% | 76% | 79% | 93% / 6% | #f6bc0f orange 22%, #170e0a black 13%, #faee1b gold 12% |
| Win celebrations and banners | 3 | 51% | 74% | 76% | 52% / 45% | #fcc315 gold 17%, #1b0736 black 10%, #c366f7 purple 10% |
| Effects | 5 | 64% | 52% | 44% | 60% / 9% | #fefdf9 light orange 23%, #fe1901 red 17%, #fc6a05 orange 14% |
| Game interface | 3 | 43% | 74% | 54% | 60% / 35% | #1b1935 dark blue 18%, #fbd02b gold 12%, #3c0d16 dark red 11% |
| Typography | 3 | 49% | 79% | 92% | 77% / 22% | #fbc511 gold 22%, #080359 dark blue 14%, #ce4614 orange 12% |
| Provider interface (shared) | 1 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### The flying 777 blocks behind the cabinet

`background-sevens` · atlas · 38 parts · largest 551×1577 · sheet `sheets/background-sevens.webp`

- **Role:** Giant extruded "777" signs that drift in from the edges of the screen behind the reels; the only solid objects in the environment.
- **Subject:** Eight views of a triple-seven block seen in steep perspective, named by where they sit (UR, UMR, UML, ML, DL, DM, DMR, DR), each in a Normal and a Special colouring, plus 21 white halftone highlight pieces and one white outline of a seven.
- **Style:** 3D sign lettering, like a casino roof sign rendered from below and from the side.
- **Rendering:** Rendered-look volumes: flat glossy red faces with a thin inset neon line, long extruded sides fading to nothing at the far end. Highlights are separate pieces of white dots and stripes (a halftone pattern).
- **Colour:** Measured: red #b7170b 25%, near-black #25062e 24%, orange #d9670c 18%, dark magenta #6a143c 18%, gold #f6ba14 7%. Normal: red-magenta faces on purple-black sides. Special: red faces on gold and orange sides.
- **Lighting:** Faces lit flat from the front; the sides carry a gradient that dies away with depth. The halftone pieces sweep light across a face (inference from their names Light3 to Light6 and their shapes).
- **Ambience:** Scale and speed: the blocks are far larger than the cabinet and are seen cropped, so the game feels as if it flies through its own logo.
- **Materials:** Lacquered sign faces, neon tube inlay, smooth plastic sides.
- **Variants:** Eight positions times two colourings (16 pictures). Normal is seen in the base game, Special in Free Spins.
- **Motion:** Not drawn here (Spine 4.2). BackgroundEffects has one animation per block, seven1 to seven8, 5 s each, with 75 bones and 136 slots. On the screens a block slides in at a corner, crosses behind the cabinet and leaves; several screens have none.
- **Construction:** Pre-rendered perspective views, not a 3D model in the game: the largest is 551x1577. The light pieces are separate so they can be animated over the still block.
- **Notes:** Depth without a 3D engine: eight fixed views of one object, moved slowly, are enough to make the flat ray backdrop feel like a space.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 28% · saturation 87% · contrast 37% · warm 74% / cool 13% · brighter towards: bottom-left (4), top-left (4), top-right (3)
- **Palette (measured):** #b7170b red 25%, #25062e black 24%, #d9670c orange 18%, #6a143c dark magenta 18%, #f6ba14 orange 7%, #ffffff white 3%

### Backdrops: purple night and orange blaze, with neon frame lines

`backgrounds` · atlas · 8 parts · largest 1376×2513 · sheet `sheets/backgrounds.webp`

- **Role:** The full-screen ground behind the cabinet in two states, and the white line pieces that draw the neon frames and lasers over it.
- **Subject:** Two tall pictures of light rays fanning from one point (bgNormal 1376x2513, bgSpecial 1375x2510), three thin outline pieces with a dotted inner line (side, top, bottom), a white starburst and two thin rays.
- **Style:** Abstract stage light: no place and no objects, only beams. It reads as a casino floor at night reduced to colour.
- **Rendering:** Soft airbrushed gradients with long straight streaks; the unit measures hard-edged (soft edge 0.014) because the pictures fill their rectangles. The line pieces are crisp white strokes with a row of dots.
- **Colour:** Measured: near-black purple #200c2f 49%, orange #ed730f 28%, red #9d2917 17%. The normal state is the purple one, the special state the orange and red one. The line pieces ship white; on the screens they are tinted red and pink in the base game and yellow in Free Spins (the tint is set by the game: inference from white art and coloured screens).
- **Lighting:** Light comes from the vanishing point of the rays, which sits at the middle of one long edge of each picture; nothing is lit by an outside source.
- **Ambience:** Base game: cool, dark, a club at night. Free Spins and the intro: hot and loud, the whole screen on fire. The change of backdrop is the main signal that a feature is on.
- **Materials:** Light only: beams, neon tube, bulb dots.
- **Variants:** Two states of the same composition (Normal, Special). The names bgNormal and bgSpecial are also used in Fire Rail Express, with other pictures.
- **Motion:** Not drawn here (Spine 4.2). The files give BackgroundEffects a "lasers" animation of 20.67 s; on the screens the neon frames at the sides and behind the cabinet sit at a different width in almost every frame, so they breathe in and out all the time.
- **Construction:** Each backdrop is one half of the scene, mirrored around the vanishing point to make a ground of about 2750x2510 (inference from the rays meeting on one edge and the symmetric screens). Frames are assembled from side, top and bottom pieces.
- **Notes:** A whole environment from two gradient pictures and three line pieces: almost no painting, all of the life comes from movement and tint.
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 26% · saturation 81% · contrast 24% · warm 55% / cool 37% · brighter towards: left (1)
- **Palette (measured):** #200c2f black 49%, #ed730f orange 28%, #9d2917 red 17%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### The cabinet: reel board, frame and neon outline

`reel-board` · atlas · 17 parts · largest 556×1053 · sheet `sheets/reel-board.webp`

- **Role:** The slot-machine body that holds everything: jackpot plaques at its head, the paytable in its middle and the 5x3 reels at its foot.
- **Subject:** A tall dark panel with a gold edge and three vertical dividers (slotBg 556x1053), a pinched cabinet outline in thin yellow neon with a dotted bulb line (slotFrameOutsideNeon), thin gold frame bars and corners, a blue-violet anticipation column, win line pieces with a gold diamond end, and guide squares.
- **Style:** An arcade or fruit-machine cabinet drawn as a flat front, with Art Deco gold lines.
- **Rendering:** Flat dark panels with fine gradients and a faint scanline texture; gold bars are small glossy strips with a red core. Measured contrast 0.548, hard-edged.
- **Colour:** Measured: near-black #190a1c 49%, dark red #4e1016 13%, gold #fbd552 7%, blue #2744b2 and #4c27d2 10% together (the anticipation column). The pure green #17ff01 4% is the layout guide square, not art.
- **Lighting:** The panel is unlit; the gold edge and the neon outline are self-lit and glow outward.
- **Ambience:** A lit machine in a dark room. The reel area is the darkest thing on screen, so the saturated symbols carry.
- **Materials:** Smoked glass, gold trim, neon tube, bulbs.
- **Variants:** One board for both states; on the screens its outer glow is gold in the base game and brighter yellow in Free Spins. frameGlowSpecial is a white glow piece for the special state.
- **Motion:** Not drawn here (Spine 4.2). Files: SlotFrame and SlotBackgrounds are still; SlotBackgroundsEffects has activate 1.35 s, loop 5.5 s, upgrade 0.67 s; ReelAnticipationBack and Front loop 0.8 and 0.67 s. On the screens of a Free Spins trigger the last reel turns into a blue-violet column with white lightning while two scatters wait.
- **Construction:** The panel is one half, mirrored (inference from the edge on one side only). Frame bars are 463x16 and 20x548 strips with 25 px corners. tileGuide is a 182 px cell, larger than the 150 to 190 px symbols drawn in it.
- **Notes:** The paytable is on the machine, above the reels, at all times: the board is two thirds information and one third play, and still reads as one object.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 27% · saturation 70% · contrast 55% · warm 51% / cool 36% · brighter towards: top (3), left (1), bottom-left (1)
- **Palette (measured):** #190a1c black 49%, #4e1016 dark red 13%, #fbd552 gold 7%, #fffffe light gold 6%, #2744b2 blue 6%, #17ff01 green 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Paytable pictures of the eleven symbols

`help-symbol-pictures` · atlas · 11 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The symbols as the help page shows them.
- **Subject:** Eleven 225x225 pictures: grapes, plum, lemon, cherries, a cluster of blue, purple and red sevens (tile5, the "any sevens" win), the blue seven, the purple double seven, the red triple seven, the crown, the gold seven with WILD, and FREE SPINS on its plate.
- **Style:** The same art, composed as it stands on the reels.
- **Rendering:** As the symbols; measured contrast 0.842.
- **Colour:** Measured: dark blue #18084d 15%, orange #eea81f 10%, gold #f3e478 8%, red #f25b2c 4%.
- **Lighting:** As the symbols.
- **Ambience:** A tidy catalogue of the set.
- **Materials:** As the symbols.
- **Variants:** One per symbol. tile5 exists only here: mixed sevens are a win rule, not a reel symbol.
- **Motion:** None.
- **Construction:** Served by the provider's shared asset service (assets/games/<game>/tiles/tileN.webp), composed pictures of the doubled and tripled sevens that the game itself builds from one seven.
- **Notes:** The numbering tile1 to tile11 is the game's own order of the symbols and is the key to every other file name (tile6Effect, tile10Txt, tile11Frame).
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 42% · saturation 71% · contrast 84% · warm 60% / cool 32% · brighter towards: top-left (4), top (3), top-right (1)
- **Palette (measured):** #18084d dark blue 15%, #eea81f orange 10%, #f3e478 gold 8%, #f25b2c red 4%, #f7f3e4 light gold 3%, #1c0b8e blue 3%

### Wild: the gold seven

`symbol-wild` · atlas · 2 parts · largest 402×428 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol, which also grows all three jackpots; the same seven is the 777 of the logo.
- **Subject:** A gold seven with a flame inside (402x428, the largest symbol picture) and the word WILD (206x96).
- **Style:** The same hot-rod seven, in gold, with slab-serif WILD across it.
- **Rendering:** Polished gold with a broad white glint, a dark double keyline and a yellow-green outer glow. Measured contrast 0.934, bright (0.612).
- **Colour:** Measured: gold #fedb15 34%, yellow #f7f266 11%, near-black #0f0b25 13%. WILD is yellow with a red shadow.
- **Lighting:** Lit from the upper left; it is the brightest symbol on the reels.
- **Ambience:** The prize piece: everything else is coloured enamel, this is metal.
- **Materials:** Gold.
- **Variants:** One picture, shown at about 100 px on the reels and large in the logo.
- **Motion:** Not drawn here (Spine 4.2). TileWild: onLand 0.42 s, win 0.6 s, lock 0.58 s (Wilds lock in Free Spins), a fire loop of 0.6 s. TileWildPiece has pieceLoop and startTrail: on the win screens a small gold seven is seen leaving a winning Wild toward the jackpots, as the help text describes ("shoots at its respective jackpot").
- **Construction:** The word is a separate piece over the seven. The seven ships at more than twice its on-reel size because the logo needs it large.
- **Notes:** One gold seven does three jobs: Wild, logo and flying jackpot token.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 61% · saturation 74% · contrast 93% · warm 82% / cool 15% · brighter towards: top (1)
- **Palette (measured):** #fedb15 gold 34%, #0f0b25 black 13%, #f7f266 gold 11%

### Scatter: FREE SPINS

`symbol-free-spins` · atlas · 5 parts · largest 227×148 · sheet `sheets/symbol-free-spins.webp`

- **Role:** The Free Spins symbol; 3, 4 or 5 of them start 10, 15 or 20 free spins (help text).
- **Subject:** A black plate with a gold and blue edge (tile11Frame 227x148), the words FREE and SPINS as separate pieces, and a white dotted highlight copy of each word.
- **Style:** A sign, not an object: two stacked words in the logo's slab serif.
- **Rendering:** Hard-edged letters with a red-to-yellow gradient and a dark blue shadow; measured dark (0.264) because of the plate.
- **Colour:** Measured: black #050106 48%, dark purple #210652 8%, gold #f8c10b 7%, orange #f64904 6%, yellow #fbe775 5%.
- **Lighting:** Letters lit from above; the halftone copies are for a light sweep (inference from the name Highlight).
- **Ambience:** Plain and loud among the pictures: it cannot be mistaken for a paying symbol.
- **Materials:** Enamel letters on a black plate.
- **Variants:** One. The help page shows the two words stacked on the plate.
- **Motion:** Not drawn here (Spine 4.2). TileFreeSpins: onLand 0.42 s, activate 1.1 s, loop 1.67 s, a fire loop 0.48 s; two fire sequences belong to it (fireTileFreeSpins 24 frames, tileFreeSpinsFire 18 frames). On the trigger screens the three symbols flare.
- **Construction:** Words apart from the plate, so the text can be localised without redrawing the symbol.
- **Notes:** A text-only scatter is honest and cheap; the art budget went to the sevens.
- **Measured:** dark, saturated, warm and cool mixed, high contrast, hard-edged · brightness 26% · saturation 49% · contrast 72% · warm 55% / cool 37% · brighter towards: top (2)
- **Palette (measured):** #050106 black 48%, #210652 dark purple 8%, #f8c10b gold 7%, #f64904 orange 6%, #fbe775 gold 5%, #fcfbf0 light gold 5%

### High symbols: blue, purple and red sevens, and the crown

`symbols-sevens-and-crown` · atlas · 4 parts · largest 228×225 · sheet `sheets/symbols-sevens-and-crown.webp`

- **Role:** The four top-paying symbols. On the reels the blue seven stands alone, the purple one is doubled and the red one tripled; each is tied to a jackpot of its colour.
- **Subject:** A seven in three colourings (tile6 blue, tile7 purple, tile8 red, each 176x189) with a flame painted inside the lower stroke, and a red and gold crown on a white fur band (tile9, 228x225).
- **Style:** Hot-rod flame lettering for the sevens; a storybook crown.
- **Rendering:** Glossy enamel volumes with a hard white glint, a gold bevel and keyline, and an outer halo. Measured contrast 0.909, strong highlights.
- **Colour:** Measured: dark blue #14074e 14%, orange #ed4f11 6%, red #c50b05 4%, blue #0b37b7 4%, golds #f6e966 and #f3e8a9. The three sevens differ in hue only.
- **Lighting:** Top-left light; each seven glows in its own colour.
- **Ambience:** The sevens are the game: loud, sharp-cornered, fast.
- **Materials:** Enamel, gold, velvet, fur, cut stones on the crown.
- **Variants:** One seven drawn once and recoloured three times; the count of sevens (1, 2, 3) is made in the game by repeating the picture (seen on the reels and in the help pictures).
- **Motion:** Not drawn here (Spine 4.2). TileContainerSeniors: onLand 0.42 s, win 0.67 s, a fire loop of 0.58 s, and transform6to7, transform6to8, transform7to8 of 1.17 s each, which is the Free Spins upgrade of sevens to the strongest one on the reels, as the help text describes. TileCrown: onLand 0.42 s, win 0.58 s. The upgrade was not caught on a screen.
- **Construction:** Three 176 px pictures make six symbols' worth of content (single, double, triple; three colours) plus their upgrade.
- **Notes:** Rank by repetition and colour, not by new drawings: blue 7, purple 77, red 777 is readable in a glance and maps straight onto MINI, MINOR and MAJOR.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 43% · saturation 70% · contrast 91% · warm 54% / cool 41% · brighter towards: top-left (3), left (1)
- **Palette (measured):** #14074e dark blue 14%, #f7f5e7 light gold 6%, #f6e966 gold 6%, #ed4f11 orange 6%, #f3e8a9 light gold 5%, #c50b05 red 4%

### Low symbols: grapes, plum, lemon, cherries

`symbols-fruit` · atlas · 4 parts · largest 163×162 · sheet `sheets/symbols-fruit.webp`

- **Role:** The four low-paying symbols; the on-reel paytable shows them together at 5x, 1x and 0.5x.
- **Subject:** A bunch of purple grapes (tile1), a dark blue plum with a leaf (tile2), a lemon (tile3) and a pair of cherries with a leaf (tile4), each about 160 px.
- **Style:** Classic fruit-machine fruit as glossy stickers.
- **Rendering:** Smooth airbrushed volumes with one soft highlight each, a gold keyline and a red-orange halo painted around the shape. Measured contrast 0.799.
- **Colour:** Measured over the four: dark blue #1c0958 17% (plum and outlines), orange #e9a126 15% (lemon), dark magenta #651857 and magenta #ba0762 (grapes, cherries), gold #f7e674 7% (keylines), red #f35f39 7% (halo).
- **Lighting:** One light from the upper left; the halo acts as a warm rim on every side.
- **Ambience:** Sweet and bright against the near-black reels.
- **Materials:** Fruit skin, leaf, a gold wire outline.
- **Variants:** One picture each. The larger pictures on the help page are a separate set.
- **Motion:** No frames of their own. TileContainerJuniors has onLand 0.42 s and win 0.6 s; each fruit has an 18-frame outline trace in the effects unit, seen on a win as a glowing line around the fruit.
- **Construction:** Single sprites of about 160 px in a 182 px cell, so they sit with air around them.
- **Notes:** Every symbol carries its own gold keyline and halo, so it reads on the dark reel and on fire alike without a tile behind it.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 39% · saturation 74% · contrast 80% · warm 64% / cool 26% · brighter towards: top (2), top-left (1), top-right (1)
- **Palette (measured):** #1c0958 dark blue 17%, #e9a126 orange 15%, #651857 dark magenta 9%, #523b26 brown 8%, #f7e674 gold 7%, #f35f39 red 7%


## Logo and title

The game's own wordmark.

### Help-page logo (horizontal)

`help-logo` · atlas · 1 parts · largest 612×160 · sheet `sheets/help-logo.webp`

- **Role:** The title at the top of the shell's help page.
- **Subject:** HOT REELS with MEGA CHARGED set to its right on one line, inside a yellow neon rectangle crossed by small lightning (612x160).
- **Style:** The same slab lettering as the game logo, flattened into a banner.
- **Rendering:** One flat picture with the glow painted in; measured bright (0.625) and warm (0.939).
- **Colour:** Measured: yellows #fce21d and #f8e357 38% together, light gold #fcf5b7 8%, dark magenta #35173a 8%, orange #eaa10e, red #f92b06.
- **Lighting:** Self-lit neon and lightning.
- **Ambience:** The game's heat on a quiet grey page.
- **Materials:** Enamel letters, neon, electricity.
- **Variants:** One.
- **Motion:** None: a still picture.
- **Construction:** Served by the provider's shared asset service (assets/games/<game>/logo/default.webp), not from the game's atlas. Fire Rail Express has a file of the same name in the same place with its own logo.
- **Notes:** The lightning that the title promises ("charged") is painted here, while in the game it is a white frame sequence tinted cyan.
- **Measured:** bright, vivid, warm, high contrast, strong highlights · brightness 62% · saturation 69% · contrast 81% · warm 94% / cool 5%
- **Palette (measured):** #fce21d gold 23%, #f8e357 gold 15%, #fcf5b7 light gold 8%, #35173a dark magenta 8%, #eaa10e orange 6%, #f92b06 red 5%

### The logo burning away

`logo-burn` · atlas · 21 parts · largest 350×297 · sheet `sheets/logo-burn.webp`

- **Role:** A frame sequence that destroys the logo: the transition from the intro into the game.
- **Subject:** 21 frames (logoBurn_00 to _20, about 350x293) of the stacked 777 HOT REELS MEGA CHARGED logo, whole in the first frame, eaten by black charred holes in the middle frames and reduced to a few dark flakes in the last.
- **Style:** A baked effect: the still logo run through a burn or dissolve.
- **Rendering:** The logo is shown small and all in gold tones; the holes have soft charred edges (soft edge 0.603).
- **Colour:** Measured: gold #f8e219 22%, near-black #170e08 17%, browns #562b0d and #934e12 21% together.
- **Lighting:** None of its own.
- **Ambience:** A fuse going off: the game starts by setting fire to its own name.
- **Materials:** Gold leaf turning to ash.
- **Variants:** One sequence.
- **Motion:** Seen on the sheet as three frames (first, middle, last). On the screens after START the logo breaks up among falling coins before the cabinet appears; the GameIntro skeleton's "show" lasts 3.42 s.
- **Construction:** Baked at reduced size and in gold only, so it is a different picture from the coloured logo it replaces; burnGradient (a 128 px gold-to-black ramp in the effects unit) may colour the same kind of burn elsewhere (inference).
- **Notes:** A destructive transition baked into 21 small frames instead of a shader: cheap to run and identical on every device.
- **Measured:** mid-tone, vivid, warm, high contrast, glow or soft effect, strong highlights · brightness 52% · saturation 74% · contrast 86% · warm 95% / cool 4% · brighter towards: bottom-left (11), top-left (3), left (1)
- **Palette (measured):** #f8e219 gold 22%, #170e08 black 17%, #562b0d brown 12%, #f7ed70 gold 11%, #934e12 brown 9%, #ecae16 orange 8%

### Logo: HOT REELS MEGA CHARGED

`logo` · atlas · 5 parts · largest 692×312 · sheet `sheets/logo.webp`

- **Role:** The title, on the intro and at the top centre of the cabinet between the paytable rows.
- **Subject:** Three separate words (HOT REELS 579x109, MEGA 388x137, CHARGED 420x129), a gold chevron backplate and its yellow neon outline. The "777" above the words on the intro is the gold seven of the Wild symbol, used three times.
- **Style:** Western slab-serif poster lettering, slanted and stacked off-axis.
- **Rendering:** Hard outlines, a two-step gradient inside each letter, a solid drop shadow. Measured contrast 0.557, soft edge 0.434 from the glow piece.
- **Colour:** Measured: orange #fdb203 36%, yellow #fdec18 15%, dark purple #20083b 13%, red #921008 and #fa2401. HOT REELS runs red to yellow on a dark outline; MEGA and CHARGED are yellow with a red shadow.
- **Lighting:** Lit from above inside the letters; the chevron outline is neon.
- **Ambience:** Hot, loud, classic. The slant of MEGA CHARGED against the level HOT REELS gives it a jolt.
- **Materials:** Enamel sign letters, gold plate, neon.
- **Variants:** A stacked version with 777 for the intro and a small version on the cabinet; a horizontal one for the help page (its own unit).
- **Motion:** Not drawn here (Spine 4.2). The Logo skeleton has loop 1.83 s and loopGs 2.02 s with 30 bones. On the screens after START the words swell and tip while coins and gems fall around them.
- **Construction:** Words are separate pieces so they can move one by one; the seven is shared with the Wild symbol (one 402x428 picture).
- **Notes:** The title names a version ("Megacharged") of an existing game by adding two words in a second colour, without touching the first.
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 61% · saturation 82% · contrast 56% · warm 88% / cool 12% · brighter towards: top-left (2), top-right (1)
- **Palette (measured):** #fdb203 orange 36%, #fdec18 gold 15%, #20083b dark purple 13%, #fefbd8 light gold 6%, #921008 red 5%, #fbf190 light gold 5%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature labels: FREE SPINS and BONUS SPINS

`feature-labels` · atlas · 2 parts · largest 926×167 · sheet `sheets/feature-labels.webp`

- **Role:** The words of the feature splash.
- **Subject:** FREE SPINS (926x167) and BONUS SPINS (924x165) on one line each.
- **Style:** The logo's slab serif, slanted.
- **Rendering:** Bevelled letters, gold to orange with a dark blue shadow. Measured contrast 0.872.
- **Colour:** Measured: gold #fac012 28%, orange #c64213 13%, yellow #fae55a 10%, dark blue #0c076c 9%.
- **Lighting:** Top light.
- **Ambience:** A shout.
- **Materials:** Gold letters.
- **Variants:** Two labels in one style. BONUS SPINS was not seen in play; it has its own splash skeleton (BonusSpinsSplash), so it is probably for spins granted by an operator (inference).
- **Motion:** Not drawn here (Spine 4.2). FreeSpinsSplash: show 1 s, hide 0.67 s; FreeSpinsSplashScenario: show 3.25 s. On the splash screen the label sits between flames under a gold "10", above three sevens that keep changing colour from blue, red and purple to all red.
- **Construction:** Localised files (en-GB) outside the atlas; the number is the UltraGold font.
- **Notes:** The splash teaches the feature without a sentence: three different sevens turn into three red ones.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 50% · saturation 76% · contrast 87% · warm 78% / cool 20% · brighter towards: top (2)
- **Palette (measured):** #fac012 gold 28%, #c64213 orange 13%, #290c27 black 13%, #fae55a gold 10%, #0c076c dark blue 9%, #f8e99f light gold 6%

### Win words, win-line plate and rays

`win-tiers` · atlas · 9 parts · largest 926×469 · sheet `sheets/win-tiers.webp`

- **Role:** The big-win tiers, the total at the end of a feature and the small plate that shows a line win.
- **Subject:** The words BIG WIN, SUPER WIN, MEGA WIN and TOTAL WIN (about 928 px wide), a gold diamond plate and chevron frame for the line sum, an orange plate frame and its white trail (the plate the win words sit on), and a white starburst.
- **Style:** The logo's slab serif, stacked in two lines.
- **Rendering:** Bevelled letters with a gold-to-orange gradient and a dark blue shadow. Measured contrast 0.787.
- **Colour:** Measured: gold #fcc613 24%, orange #ca4214 11%, dark red #611c12 9%, yellow #fce65b 8%, dark blue #0f0571 4%. All four words share one colouring.
- **Lighting:** Top light on the letters; rays are white, for tinting.
- **Ambience:** Warm and simple; the tiers differ by word only.
- **Materials:** Gold letters.
- **Variants:** Three tiers and a total from one layout.
- **Motion:** Not drawn here (Spine 4.2). WinBig: labelShow 1 s, sumShow 0.42 s, hide 0.67 s; WinBigEffects: fire 0.58 s, lasersLoop 8.33 s, raysLoop 1.5 s; WinTotal: show 1 s, loop 1 s. On the screens a line win shows gold lines with diamond ends across the reels and the amount counting up in the gold numerals. A BIG WIN came in Free Spins: the words sit on a blue neon plate (the frame piece, tinted) over gold rays and flying coins, with the amount below. SUPER WIN, MEGA WIN and TOTAL WIN were not seen.
- **Construction:** The four words are localised files (en-GB) outside the atlas; the starburst is pixel for pixel the one in Fire Rail Express (circularWhiteRays2).
- **Notes:** Unlike the jackpots, the win tiers are not colour-coded: the game keeps its colour code for the sevens alone.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 55% · saturation 72% · contrast 79% · warm 74% / cool 15% · brighter towards: top (4)
- **Palette (measured):** #fcc613 gold 24%, #ca4214 orange 11%, #611c12 dark red 9%, #fce65b gold 8%, #fffffd light gold 8%, #130827 black 7%

### Jackpot win plates and words

`jackpot-win` · atlas · 6 parts · largest 543×670 · sheet `sheets/jackpot-win.webp`

- **Role:** The celebration shown when a jackpot is claimed.
- **Subject:** Three tall neon sevens built of stacked outlines (blue 543x670, purple 526x615, red-orange 532x599) and the words MINI JACKPOT, MINOR JACKPOT and MAJOR JACKPOT (about 900x325 each).
- **Style:** Neon tube signs: the seven is drawn as layers of light, not as an object.
- **Rendering:** Concentric outlines with gradient fills and glow; words bevelled with a dark outline. Measured contrast 0.742.
- **Colour:** Measured: purple #c366f7 15%, gold #fcc514 12%, light blue #6ac9fa 11%, blue #1073c6 8%, red #ec3b06 7%, orange #f38522 7%. Each jackpot keeps its colour from symbol to plaque to win.
- **Lighting:** Self-lit.
- **Ambience:** A sign lighting up in the dark.
- **Materials:** Neon, enamel letters.
- **Variants:** Three colours of one layout.
- **Motion:** Not drawn here (Spine 4.2). WinJackpot: labelShow 1 s, hide 0.67 s; BackgroundReactions has jackpotWin 1.33 s. On the screen of a MINOR jackpot won in Free Spins the purple double seven stands large behind the words, with the amount under it, gold rays from the centre and 777 coins flying over the darkened cabinet. The MINI and MAJOR wins were not seen.
- **Construction:** The largest single pieces after the backdrops; word and seven are separate.
- **Notes:** The win screen is the plaque enlarged: nothing new is introduced at the moment of the win.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 50% · saturation 76% · contrast 74% · warm 37% / cool 62%
- **Palette (measured):** #c366f7 purple 15%, #fcc514 gold 12%, #6ac9fa blue 11%, #e2a5fe light purple 9%, #1d0537 black 9%, #1073c6 blue 8%


## Effects

Frame sequences, glows, particles and transitions.

### Fire: transition, white flames, feature loops

`fire` · atlas · 80 parts · largest 278×500 · sheet `sheets/fire.webp`

- **Role:** The fire used between states and around the reels.
- **Subject:** A 16-frame column of cartoon fire (fireTransition), two 18-frame white flame sets (flamesFill, flamesLighting, 310x150), a 10-frame standing flame (freeSpinsFireLoop), 13 frames of a thin horizontal streak (reelAnticipationFire) and 5 frames of a red zigzag bolt (fireLightning).
- **Style:** Flat cartoon fire in two or three tones.
- **Rendering:** Hard shapes with a soft outer glow (soft edge 0.647); the white sets are shape only.
- **Colour:** Measured: white #ffffff 41% (the tintable flames), orange #fd6a03 28%, light yellow #fffa87 12%, red #fe1300 9%.
- **Lighting:** Self-lit.
- **Ambience:** Heat on demand: the base game is cool, and fire arrives only with wins and features.
- **Materials:** Fire.
- **Variants:** Coloured fire for fixed uses, white fire to be tinted.
- **Motion:** Seen on the sheet as three frames per sequence. On the screens fire fills the frame for a moment when Free Spins begin, and flames stand on the sevens of the splash.
- **Construction:** The 36 white flame frames are pixel for pixel the ones in Fire Rail Express; fireTransition has the same name and frame count there but is cut to other sizes, so the two were not compared.
- **Notes:** The provider reuses a white flame set across games and tints it: an effect library, not per-game fire.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 76% · saturation 47% · contrast 31% · warm 56% / cool 0% · brighter towards: bottom (6), top-right (2), bottom-right (1)
- **Palette (measured):** #ffffff white 41%, #fd6a03 orange 28%, #fffa87 light gold 12%, #fe1300 red 9%, #fcc149 orange 3%, #bebebe grey 3%

### Symbol win traces and symbol fire

`symbol-win-effects` · atlas · 167 parts · largest 392×287 · sheet `sheets/symbol-win-effects.webp`

- **Role:** What plays on a symbol when it wins or lands: a glowing line that runs round its outline, and fire for the sevens and the scatter.
- **Subject:** Six 18-frame traces (tile1, 2, 3, 4, 6 and 9: an orange-white line following the shape of the grapes, plum, lemon, cherries, seven and crown, with a puff of grey smoke), an 18-frame trace of the scatter's rectangle, 17 frames of flame for the sevens (fireSeniors) and a 24-frame fire burst for the scatter (fireTileFreeSpins).
- **Style:** Hand-drawn cartoon effects: a sparkler line and flat two-tone flames.
- **Rendering:** Soft glowing strokes (soft edge 0.696); flames are flat shapes with a hot core and a red glow.
- **Colour:** Measured: red #fe1901 42%, oranges #fc8e41 18% and #fc5903 10%, cream #fff5d0 15%.
- **Lighting:** Self-lit.
- **Ambience:** A fuse running round the winning symbol.
- **Materials:** Fire, spark, smoke.
- **Variants:** One trace per symbol shape; the three sevens share one (tile6Effect) because they are one drawing (inference from there being no tile7Effect or tile8Effect).
- **Motion:** Seen on the sheet as three frames per sequence. On a win screen the winning grapes carry a bright red-white outline.
- **Construction:** 167 frames, the largest group in the atlas, most of them under 130 px.
- **Notes:** An outline trace is drawn per shape, so it costs frames for every new symbol; the saving is that the symbol itself never has to be redrawn or rigged for a win.
- **Measured:** mid-tone, vivid, warm, high contrast, glow or soft effect, strong highlights · brightness 55% · saturation 76% · contrast 63% · warm 100% / cool 0% · brighter towards: bottom-right (5), bottom (3), top (3)
- **Palette (measured):** #fe1901 red 42%, #fc8e41 orange 18%, #fff5d0 light gold 15%, #fed886 light orange 10%, #fc5903 orange 10%, #fdbd61 orange 3%

### Electricity

`electricity` · atlas · 25 parts · largest 193×75 · sheet `sheets/electricity.webp`

- **Role:** The "charged" of the title: small lightning that crawls along the cabinet's edge.
- **Subject:** Two white lightning sequences, 15 and 10 frames, the largest 193x75.
- **Style:** Hand-drawn forked sparks.
- **Rendering:** Pure white with a soft glow (soft edge 0.929), made to be tinted.
- **Colour:** Measured: white only. On the screens it is cyan against the gold frame.
- **Lighting:** Self-lit.
- **Ambience:** A short crackle now and then; the one cold colour among the warm ones.
- **Materials:** Electric arc.
- **Variants:** Two shapes.
- **Motion:** Seen on the sheet as three frames per sequence. On the screens a cyan arc sits at a different place on the cabinet's outline from frame to frame, and after a sevens win cyan bolts strike the MINI plaque.
- **Construction:** Small white frames, tinted and placed by the game.
- **Notes:** The version's whole theme ("Megacharged") is carried by 25 tiny white frames and a cyan tint.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff light yellow 100%

### Gems and 777 coins

`gems-and-coins` · atlas · 105 parts · largest 94×90 · sheet `sheets/gems-and-coins.webp`

- **Role:** The shower pieces: thrown on the intro, on wins and around the jackpots.
- **Subject:** A cut gem tumbling through 30 frames in blue, purple and red (about 88x72) and a gold coin stamped 777 turning through 15 frames (82x82 face on, 16 px wide edge on).
- **Style:** Rendered-look small objects.
- **Rendering:** Faceted with sharp white glints; the coin is polished gold with a darker rim. Measured contrast 0.564.
- **Colour:** Measured: red #c34019 15%, blue #1f7ec9 13%, purple #881ec8 13%, with light tints of each. The three gem colours are the three sevens' colours again.
- **Lighting:** Lit from above; glints move with the turn.
- **Ambience:** Treasure in the air.
- **Materials:** Cut glass or gemstone, gold.
- **Variants:** Three colours of one gem animation; one coin.
- **Motion:** Seen on the sheet as three frames per sequence. ParticleDiamond1 to 3 and ParticleCoin loop 1 s and 0.48 s. On the screens coins pour around the logo after START and gems fall at the top of the frame.
- **Construction:** 105 small frames; each colour of gem is baked as its own 30 frames rather than tinted.
- **Notes:** Gems are baked per colour because a tint would flatten the facets; coins and flames, which are one hue, are not.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 54% · saturation 66% · contrast 56% · warm 45% / cool 54% · brighter towards: top (28), top-right (19), right (5)
- **Palette (measured):** #c34019 red 15%, #1f7ec9 blue 13%, #881ec8 purple 13%, #f4c597 light orange 10%, #93c2f5 light blue 9%, #c763f2 purple 7%

### Light, lens flares and particle dots

`light-and-particles` · atlas · 17 parts · largest 512×512 · sheet `sheets/light-and-particles.webp`

- **Role:** The helper pictures effects are built from.
- **Subject:** A 512 px cloud noise (displacement), a white glow, two lens flares, three soft discs, a four-point glint, sparkle dots, 23 px glow dots in blue, purple, red and yellow, a white square, a gold-to-black ramp (burnGradient) and a green guide square.
- **Style:** Generic effect textures.
- **Rendering:** Soft greys and whites; measured muted (saturation 0.139).
- **Colour:** Measured: greys #a5a4a4 46% and #727171 11%, white 15%. The green #17ff00 8% is the guide, not art.
- **Lighting:** They are the light.
- **Ambience:** None alone.
- **Materials:** Light.
- **Variants:** Four colours of glow dot, matching the sevens and the Wild.
- **Motion:** No frames. The noise picture is the kind used to distort or dissolve another picture, and the ramp to colour a burn (inference from their names and look).
- **Construction:** Small textures outside the main style; the white glow and white square are pixel for pixel the ones in Fire Rail Express.
- **Notes:** Nothing here is specific to this game except the four dot colours.
- **Measured:** mid-tone, muted, warm and cool mixed, medium contrast, strong highlights · brightness 60% · saturation 14% · contrast 31% · warm 14% / cool 6% · brighter towards: left (1)
- **Palette (measured):** #a5a4a4 grey 46%, #fdfdfd white 15%, #1a1c19 black 15%, #727171 grey 11%, #17ff00 green 8%, #d7d7d6 grey 3%


## Game interface

Buttons, counters and panels drawn for this game.

### Buy Feature card: Free Spins

`buy-feature-card` · atlas · 1 parts · largest 490×190 · sheet `sheets/buy-feature-card.webp`

- **Role:** The picture on the Free Spins card of the shell's Buy Feature window.
- **Subject:** A 490x190 painting: a blue, a red and a purple seven fanned out in flames, cyan gems flying, red 777 blocks at both sides, on an orange blaze.
- **Style:** Key art in the game's own style; the only painted composition in the game.
- **Rendering:** Fully painted and opaque (soft edge 0.0), high contrast 0.714.
- **Colour:** Measured: oranges #efa118 24% and #d95010 20%, dark red #8c1105 18%, gold #f5d04d 3%.
- **Lighting:** Lit from the centre by the fire behind the sevens.
- **Ambience:** The feature as a poster.
- **Materials:** Enamel sevens, fire, cut gems.
- **Variants:** One. The second card in the window ("2x", Double Chance) is the provider's shared picture.
- **Motion:** None: a still picture.
- **Construction:** Served by the provider's shared asset service (assets/games/<game>/features/featurebuy.webp).
- **Notes:** It shows all three sevens together with the 777 blocks: the game's whole cast in one small picture.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 47% · saturation 78% · contrast 71% · warm 84% / cool 14%
- **Palette (measured):** #efa118 orange 24%, #d95010 orange 20%, #8c1105 dark red 18%, #b22f12 red 3%, #f5d04d gold 3%, #ea9cf5 light magenta 2%

### Jackpot plaques: MINI, MAJOR, MINOR

`jackpot-panel` · atlas · 10 parts · largest 516×265 · sheet `sheets/jackpot-panel.webp`

- **Role:** The three growing jackpots that stand behind the head of the cabinet, each with its value in the gold numerals.
- **Subject:** Three plaques cut to the silhouette of sevens: one blue seven (MINI, 315x223), two purple sevens (MINOR, 339x264) and three red sevens (MAJOR, 381x264), a yellow neon outline of each, the three words, and a dark striped plate with a gold edge.
- **Style:** Neon sign shapes with slab-serif labels; the plaque shape is the symbol it belongs to.
- **Rendering:** Flat colour fields with a soft inner gradient and a thin orange rim; words are bevelled with a dark outline. Measured contrast 0.508.
- **Colour:** Measured: dark blue #1b1935 24%, dark red #3b0e18 14%, orange-red #ef4004 12%, purple #c85ff7 11%, blue #127ccb 7%, gold #fbd534 6%. Blue, purple and red are the same three hues as the sevens.
- **Lighting:** Self-lit; the outline pieces glow when a plaque is live.
- **Ambience:** A row of signs over the machine, always counting.
- **Materials:** Back-lit acrylic, neon.
- **Variants:** Three colours, three silhouettes (1, 2, 3 sevens).
- **Motion:** Not drawn here (Spine 4.2). Jackpot: update 0.58 s, win 0.67 s, loop 2 s, five fire loops and five light loops of rising speed (0.5 s down to 0.25 s), progressShow and progressHide. On the screens the values rise during play (MAJOR from 777x to 783x over 60 spins) and count up from low numbers when the game opens.
- **Construction:** Shape, outline and word are separate pieces; the values are the UltraGold font. The plate name jackpotFrame is also used in Fire Rail Express, for another picture.
- **Notes:** The jackpot a symbol feeds has that symbol's colour and its number of sevens as its shape: the rule needs no text.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 38% · saturation 73% · contrast 51% · warm 49% / cool 45% · brighter towards: top-left (1)
- **Palette (measured):** #1b1935 dark blue 24%, #3b0e18 dark red 14%, #ef4004 orange 12%, #c85ff7 purple 11%, #127ccb blue 7%, #fbd534 gold 6%

### On-reel paytable plates

`paytable-panel` · atlas · 4 parts · largest 287×150 · sheet `sheets/paytable-panel.webp`

- **Role:** The frames of the always-visible paytable between the logo and the reels; a row lights when its symbol wins.
- **Subject:** A dark glass plate with a gold and red rim (payoutM 260x125), its lit gold version (payoutMWon 287x150), and two bracket frames for the Wild's value, plain and lit.
- **Style:** Small Art Deco plates in the cabinet's trim.
- **Rendering:** Soft gradients inside a crisp double rim; the lit versions carry a wide glow (soft edge 0.44).
- **Colour:** Measured: golds #feca1b 38% and #fdeb52 24%, light gold #fef6a2 15%, dull red #a42d4e 7%.
- **Lighting:** The lit plate is evenly self-lit, like a lamp behind glass.
- **Ambience:** An old machine's award glass.
- **Materials:** Glass, gold rim.
- **Variants:** Off and won states.
- **Motion:** Not drawn here (Spine 4.2). Payout: activate, deactivate and loop of 0.5 s and three activateMultiplier tracks of 0.77 s; PayoutFireEffect loops 1.2 s. On a win screen the winning row's plate turns gold and glows while the others stay dark.
- **Construction:** Plates only; the symbol pictures on them are the reel symbols and the values are small bitmap numerals (the UltraInactive and UltraActive fonts, by their names the resting and the lit state: inference).
- **Notes:** Showing the pays on the machine removes a trip to the help page and gives every win a second place to celebrate.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 75% · saturation 71% · contrast 41% · warm 100% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #feca1b gold 38%, #fdeb52 gold 24%, #fef6a2 light gold 15%, #a42d4e red 7%, #290302 black 6%, #fefbe1 light gold 4%


## Typography

Embedded fonts and lettering.

### Numerals: gold italic slab (UltraGold)

`UltraGold` · atlas · 20 parts · largest 240×494 · sheet `sheets/UltraGold.webp`

- **Role:** The large bitmap font: jackpot values, win amounts, the free spins count.
- **Subject:** Digits 0 to 9, x, +, -, *, /, ?, comma and full stop about 205 px high, with a euro sign and a capital X loaded as files of their own.
- **Style:** A very fat italic slab serif, the same family feeling as the logo.
- **Rendering:** Hard-edged (0.04), contrast 0.919: a gold fill with a horizontal shine and an orange foot, on a dark blue extrusion.
- **Colour:** Measured: gold #fbc511 24%, dark blue #080359 15%, orange #cf4614 12%, yellow #fbe756 11%, dark red #5e1a11 10%.
- **Lighting:** Top light with a band of shine across the middle.
- **Ambience:** Money: heavy, shiny, leaning forward.
- **Materials:** Polished gold on blue enamel.
- **Variants:** One style. It is one of many fonts in the provider's shared font store (fonts-v2); Fire Rail Express uses another of them (UltraPurpleGold).
- **Motion:** None of its own; on the screens the amounts count up.
- **Construction:** 18 glyphs on one 2048x512 WebP with a JSON of positions; other characters are single files fetched when a text needs them (the euro sign here).
- **Notes:** Blue under the gold keeps amounts readable on the orange Free Spins backdrop, where gold alone would vanish.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 49% · saturation 80% · contrast 92% · warm 76% / cool 23% · brighter towards: top (16), top-left (4)
- **Palette (measured):** #fbc511 gold 24%, #080359 dark blue 15%, #cf4614 orange 12%, #fbe756 gold 11%, #5e1a11 dark red 10%, #fbefb0 light gold 10%

### Small numerals, lit (UltraActive)

`UltraActive` · atlas · 20 parts · largest 40×93 · sheet `sheets/UltraActive.webp`

- **Role:** By its name, the lit state of the small paytable values on the cabinet (inference; which rows use it was not settled from the screens).
- **Subject:** The same character set at about 36 px: cream figures with a red outline.
- **Style:** The same fat slab serif, upright.
- **Rendering:** Soft outer edge (0.294), contrast 0.907.
- **Colour:** Measured: cream #feeac8 41%, reds #87161c 20% and #49070d 19%.
- **Lighting:** Flat and self-lit.
- **Ambience:** A lamp switched on.
- **Materials:** Lit glass.
- **Variants:** The lit one of a pair with UltraInactive.
- **Motion:** None of its own.
- **Construction:** 18 glyphs on a 1024x64 WebP from the shared font store.
- **Notes:** A state change done as two fonts rather than a tint: the lit and unlit values can differ in outline as well as colour.
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 54% · saturation 52% · contrast 91% · warm 100% / cool 0%
- **Palette (measured):** #feeac8 light orange 41%, #87161c red 20%, #49070d dark red 19%, #f3b7a0 light orange 7%, #99433b red 6%, #cf887a red 6%

### Small numerals, unlit (UltraInactive)

`UltraInactive` · atlas · 20 parts · largest 40×93 · sheet `sheets/UltraInactive.webp`

- **Role:** The resting state of the small paytable values on the cabinet: dark red figures with a light edge, as the rows look on the screens.
- **Subject:** The same character set at about 36 px: dark red figures with a tan outline.
- **Style:** The same fat slab serif, upright.
- **Rendering:** Hard-edged (0.127), contrast 0.832.
- **Colour:** Measured: dark red #3a0610 58%, tans #d9a768 18% and #f9dec3 10%.
- **Lighting:** Unlit.
- **Ambience:** A lamp switched off: readable but quiet.
- **Materials:** Dark glass with a metal edge.
- **Variants:** The unlit one of the pair.
- **Motion:** None.
- **Construction:** 18 glyphs on a 1024x64 WebP from the shared font store.
- **Notes:** Keeping the resting paytable dark red on near-black lets ten rows of numbers sit above the reels without competing with them.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 33% · saturation 72% · contrast 83% · warm 93% / cool 0%
- **Palette (measured):** #3a0610 dark red 58%, #d9a768 orange 18%, #f9dec3 light orange 10%, #e5be9c light orange 6%, #926145 orange 5%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 603 components cut from 37 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
