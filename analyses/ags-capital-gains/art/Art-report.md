# Capital Gains: art report

ags · run `2026-11-26-1037-ags-capital-gains` · captured 2026-11-26

Source: the provider's free-play demo, https://eu-rgs.gameiom.com/games/launch?operatorId=41&gameCode=capital_gains&partnerid=63&moneymode=fun&channel=desktop&language=en_US

**Extracted:** 1188 named components from 29 textures in 29 atlases; 0 Spine skeletons; 45 frame sequences (854 frames); 25 fonts. Grouped into 29 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A money-themed slot with no character and no place: glossy gold, cash and gem icons on a black reel window over a flat banknote-green field, with one loud counter-colour, the electric blue lightning of its Money Charge Jackpots feature.

**Style.** Casino-floor object illustration, carried over from a land-based cabinet (inference from the cabinet-style signage, credit-based pays and bet-level buttons). Everything is a thing of wealth shown as an icon: vault door, diamond, gold bars, banknotes, coins, money bag, currency signs, card letters. The setting is an abstract banknote pattern, not a scene; the only place the game ever shows is the gold-ringed vault chamber of the bonus.

**Rendering.** Smooth airbrushed gradients, hard silhouettes and bright specular streaks; 12% of edges measure soft over the whole game. High symbols sit on a rounded tile of their own colour; low symbols are bevelled letters with a white edge and a black outline. Titles are extruded, bevelled display lettering. Lightning is the one soft, glowing family (77% soft edges).

**Colour.** Green, gold and black, with blue as the charge. Measured over the game's own art: black #060f09 33%, black-teal #0e3e2f 10%, orange-gold #e79510 10%, white #f3f9f8 5%, dark green #0d6d06 4%, blue #0366f6 3%, green #06a04b 2%; saturation 0.67, warm 39% against cool 41%; hues green 31%, orange 22%, blue 13%, yellow 12%. The base background is two greens only (#046c31, #04af53). Each high symbol owns a tile colour (diamond red, gold bars blue, notes purple, coins dark green) and each letter one flat colour (A red, K blue, Q yellow, J green). The free spins swap the field to red (#ce110a). Jackpot tiers: Grand red, Major green, Minor blue, Mini purple. Lightning is #0269f7 with a white core.

**Lighting.** A plain light from above on nearly everything (top on 354 parts measured, top-right 81, top-left 55), with white streak highlights on gold. No scene lighting, no cast light between objects. Lightning and the vault symbol's landing flash are self-lit.

**Ambience.** Bright, clean and blunt: the promise is money itself. Calm in the base game, hotter by colour alone in the free spins, and charged when the lightning locks the green discs in the bonus.

**Shape language.** Round and heavy: discs, coins, the vault wheel, the sack, the ring of the vault chamber. Rounded square tiles for high symbols. Slab-serif letters. The background's only ornament is banknote engraving: guilloche curves and scrollwork.

**Materials.** Polished gold above all; cut diamond; printed paper money; enamel-coloured letters; black glass panels with hairline rainbow edges and gold corner beads; a dark neutral plastic for the console.

**Typography and lettering.** The logo is gold slab-serif capitals on two arches with a red-brown extrusion and a laurel; MONEY CHARGE is white-violet italic capitals over yellow JACKPOTS on a purple extrusion; WILD is cream western slab lettering; the disc values are cream slab numerals baked into each picture. Help pages set live text in red-orange outlined serif small capitals. 25 font files are embedded (among them Cinzel, Alfa Slab One, Bodoni, Trajan Pro, Bebas Neue, Roboto, Myriad Pro, Dollar Bill); which of them this game draws with was not traced, and a list this long reads as a provider's shared set (inference).

**Motion.** Frame sequences only: no skeleton and no Spine file is shipped, so the empty assembled folder says nothing more than that. 45 sequences hold 854 frames: every symbol has a pre-rendered win animation (14 frames for the diamond, 24 for the other high symbols, 38 for each low symbol), the wild and the vault also a landing animation, the vault door swings open in 50 frames, lightning runs in 14 looping sets (276 frames, the largest), and coins and gems tumble in 24 frames each for the big win. Symbols mostly stay in place while a highlight crosses them; the energy comes from flashes and lightning, not from deforming art.

**Variants and themes.** Every symbol in three states: still, dimmed copy (drawn, about a quarter as bright) and animation. The Money Charge disc in 29 baked values, lit and dimmed. Reel window with a green or a red edge; background in green, red, paytable and loading versions. Titles with and without the word JACKPOTS, for markets without the jackpot. Only the desktop landscape layout was captured; the files name portrait cuts as well.

**How it is built.** 29 texture pages, 1,188 named sprites in TexturePacker atlases, one atlas per symbol animation and one per screen (base game, preloader, paytable, vault gateway, Money Charge, menus, autoplay). Backgrounds are four JPEGs at 1440x810. Everything is a bitmap or a frame sequence; values and pay rows are baked pictures; labels and meters are live text. The console and the autoplay panel are a neutral dark kit that is not themed to the game.

**Consistency.** Very consistent and very narrow: one rendering manner for every object, one green for the world, gold for value, blue lightning for the feature. The console is the one foreign body, grey-violet and unthemed. The feature's brand (Money Charge Jackpots, violet and yellow) deliberately does not match the game's green and gold, so it reads as a badge shared across games (inference).

**What to take from it.** (1) A leading US online slot can carry no character, no world and no story: this one ranks on thirteen clear money icons, a jackpot panel and one feature effect. Clarity of symbols on black beats scenery here. (2) The black reel window with a coloured tile behind each high symbol is a cheap, strong recipe for legibility: every symbol is identifiable by colour alone at thumbnail size. (3) One effect family, used everywhere, gives the feature its identity: blue lightning frames the meters, the title, each locked symbol and the total. It is the only cold colour in the game, so it never competes with the art. (4) Production is frame sequences and stills only, with no rigging: 854 frames, most of them a highlight crossing a still picture. This is art an image pipeline can produce directly: a still per symbol, a dimmed copy, and a short shine or flash sequence. (5) Feature variants are done by recolour, not new art: the free spins are the same background in red and the same reel window with a red edge. (6) Values baked into pictures (29 discs, twice) cost sprites but guarantee the look of the numerals; live text is kept for meters and rules. (7) The loading screen sells the three features as three captioned cards before play; it is the clearest statement of what the game wants the player to hope for.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 34% · saturation 67% · contrast 56% · warm 39% / cool 40% · brighter towards: top (354), top-right (81), top-left (55)

Palette: #060f09 black 33%, #0e3e2f dark cyan 10%, #e79510 orange 10%, #f3f9f8 light cyan 5%, #0d6d06 dark green 4%, #514e49 grey 4%, #0366f6 blue 3%, #06a04b green 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 5 | 31% | 88% | 55% | 28% / 40% | #042310 black 38%, #0a7123 dark green 21%, #d98d09 orange 13% |
| Reel board | 1 | 4% | 12% | 31% | 50% / 25% | #000000 black 87%, #8c0e0a dark red 5%, #35391c brown 3% |
| Symbols | 13 | 40% | 70% | 71% | 59% / 26% | #151d0e black 30%, #a30c03 red 8%, #f4fbf7 light green 8% |
| Logo and title | 1 | 34% | 54% | 80% | 47% / 46% | #040408 black 33%, #4c1e6c dark purple 11%, #fce615 gold 6% |
| Win celebrations and banners | 2 | 53% | 72% | 71% | 74% / 17% | #ef9819 orange 29%, #092707 black 18%, #f9e648 gold 11% |
| Effects | 1 | 59% | 71% | 65% | 0% / 100% | #0269f7 blue 52%, #f4fdff light cyan 22%, #0db4ff cyan 10% |
| Game interface | 4 | 15% | 45% | 27% | 10% / 61% | #030707 black 59%, #0e353c dark cyan 24% |
| Provider interface (shared) | 2 | 73% | 0% | 74% | 0% / 0% | #fcfcfc white 46%, #ababab grey 21%, #767676 grey 11% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Base game background

`base_background_ls-2.25x` · atlas · 1 parts · largest 1440×810 · sheet `sheets/base_background_ls-2.25x.webp`

- **Role:** The full-screen ground behind the base game, landscape layout.
- **Subject:** A flat banknote-green field with two soft lighter pools, one behind the jackpot panel and a larger one behind the reels, a faint guilloche line pattern like the engraving on paper money, and a pale scrollwork ornament along the bottom right.
- **Style:** Abstract print design, taken from the look of a banknote; no place and no depth.
- **Rendering:** Smooth gradients with hairline engraved curves at low contrast.
- **Colour:** Green only, measured: dark green #046c31 73%, green #04af53 27%; saturation 0.97, hue 100% green.
- **Lighting:** No light source; the two glows act as spotlights that lift the panel and the reels.
- **Ambience:** Calm, clean and bright: money as a colour.
- **Materials:** Printed paper (inference from the guilloche and scrollwork).
- **Variants:** One picture, 1440x810, for the landscape layout; the portrait layout was not captured.
- **Motion:** Still.
- **Construction:** One JPEG; the file name says 2.25x of a 640x360 design.
- **Notes:** The quietest background in the batch of leaders: all attention goes to the symbols and the jackpot meters.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 37% · saturation 97% · contrast 30% · warm 0% / cool 50% · brighter towards: bottom-right (1)
- **Palette (measured):** #046c31 dark green 73%, #04af53 green 27%

### Free spins background

`fs_background_ls-2.25x` · atlas · 1 parts · largest 1440×812 · sheet `sheets/fs_background_ls-2.25x.webp`

- **Role:** The full-screen ground behind the free spins.
- **Subject:** The base background recoloured: the two pools and most of the field turn red, with the top edge left green and the same scrollwork at the bottom right.
- **Style:** The same banknote design, colour-swapped.
- **Rendering:** Smooth gradients, hairline pattern.
- **Colour:** Red over green, measured: red #ce110a 49% and #930d07 13%, dark green #145a26 22%; hues red 71%, green 29%.
- **Lighting:** None; red glows where the green ones were.
- **Ambience:** Hotter and more urgent than the base game, by colour alone.
- **Materials:** Printed paper (inference).
- **Variants:** One picture, 1440x812.
- **Motion:** Still.
- **Construction:** One JPEG.
- **Notes:** The free spins were not reached in play, so this background is read from the file only.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 26% · saturation 87% · contrast 33% · warm 74% / cool 13% · brighter towards: top-right (1)
- **Palette (measured):** #ce110a red 49%, #145a26 dark green 22%, #930d07 red 13%, #595d2c brown 7%, #cc562a orange 5%, #719045 green 2%

### Paytable background

`landscape_paytable_background-2.25x` · atlas · 1 parts · largest 1440×810 · sheet `sheets/landscape_paytable_background-2.25x.webp`

- **Role:** The ground of every help and paytable page.
- **Subject:** A near-black teal panel with a faint ring pattern, framed by a green banknote band at the top, where a small Capital Gains logo sits, and a green band with white scrollwork at the bottom; thin gold rules divide them.
- **Style:** Banknote ornament as page furniture.
- **Rendering:** Flat bands, hairline gold rules, engraved scroll ornament.
- **Colour:** Measured: black-teal #001516 71%, green #0a8f3c 23%, brown-gold #755b1d 2%.
- **Lighting:** None.
- **Ambience:** Formal, like a certificate.
- **Materials:** Printed paper, gold rule.
- **Variants:** One picture, 1440x810.
- **Motion:** Still.
- **Construction:** One JPEG with the logo baked in.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 18% · saturation 86% · contrast 53% · warm 8% / cool 52%
- **Palette (measured):** #001516 black 71%, #0a8f3c green 23%, #755b1d brown 2%

### Loading screen background

`preloader_background_ls-2.25x` · atlas · 1 parts · largest 1440×810 · sheet `sheets/preloader_background_ls-2.25x.webp`

- **Role:** The ground of the loading screen, behind the three feature cards.
- **Subject:** Green at the top fading down into black-teal, fine radiating engraved lines, and two pale scrollwork ornaments at the bottom corners.
- **Style:** The banknote design in a darker key.
- **Rendering:** Gradient with hairline rays.
- **Colour:** Measured: black-teal #02211e 80%, dark green #028e48 18%; brightness 0.16.
- **Lighting:** A glow from the top edge (measured: top).
- **Ambience:** A dim stage before the bright game.
- **Materials:** Printed paper (inference).
- **Variants:** One picture, 1440x810.
- **Motion:** Still.
- **Construction:** One JPEG.
- **Measured:** dark, vivid, cool, medium contrast, hard-edged · brightness 16% · saturation 91% · contrast 43% · warm 0% / cool 72% · brighter towards: top (1)
- **Palette (measured):** #02211e black 80%, #028e48 dark green 18%, #025734 dark green 2%

### Money Charge bonus scene and the J symbol

`money-charge_L6-raw_0-1x` · atlas · 50 parts · largest 1080×1142 · sheet `sheets/money-charge_L6-raw_0-1x.webp`

- **Role:** The side panel, cash piles and WINNER title of the Money Charge bonus, with the green J symbol's win animation packed on the same page.
- **Subject:** A round green vault chamber in a thick riveted gold ring on an orange-gold field, heaps of green banknote bundles along its floor; two separate cash piles for the screen's top corners; a WINNER title in white-violet capitals; black meter panels with a rainbow hairline and gold corner beads; a red-boxed green disc reading 75000; the green J.
- **Style:** Rendered gold and money, the same glossy manner as the symbols, at scene size.
- **Rendering:** Hard gold bevels with rivets, soft green glow inside the ring, detailed banknote bundles.
- **Colour:** Green and orange-gold, measured: black-green #082a04 38%, orange #d98d09 25%, dark green #157b02 15%, green #3fb708 5%.
- **Lighting:** From above (43 parts measured); the chamber glows from inside.
- **Ambience:** A vault full of cash: the one moment the game shows a place.
- **Materials:** Polished gold with rivets, paper money, black glass meters.
- **Variants:** The vault panel in a landscape cut (719x1082, three copies) and a portrait cut (1080x1142); cash left and right; WINNER; three meter backgrounds.
- **Motion:** L6_win, 38 frames: the J with a light moving on it, like the other low symbols. The scene parts are stills; in play the panel slides in from the left over the logo and blue lightning frames the locked discs (seen in the bonus screens).
- **Construction:** 50 sprites on one page; the J is here only because of how the pages were packed.
- **Notes:** In play the jackpot meters sit inside the gold ring, so the panel is built as a frame for them.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 38% · saturation 87% · contrast 71% · warm 36% / cool 33% · brighter towards: top (43), bottom (1)
- **Palette (measured):** #082a04 black 38%, #d98d09 orange 25%, #157b02 dark green 15%, #3fb708 green 5%, #effbf9 light cyan 3%, #aa6505 brown 2%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board

`matrix_0-1x` · atlas · 2 parts · largest 1235×678 · sheet `sheets/matrix_0-1x.webp`

- **Role:** The backing and frame of the 5x3 reel window.
- **Subject:** A black rectangle divided by four thin grey vertical lines, with a soft glowing edge: green for the base game, red for the free spins.
- **Style:** Minimal; the board is a black window, not an object.
- **Rendering:** Flat black with a blurred coloured edge and hairline dividers.
- **Colour:** Black #000000 87%, with the edge in dark red #8c0e0a or green #299c38 (measured).
- **Lighting:** None.
- **Ambience:** Neutral: it exists to make the symbols' colours as strong as possible.
- **Materials:** None drawn.
- **Variants:** Two: green edge (1235x678) and red edge (1265x658).
- **Motion:** Still.
- **Construction:** Two sprites.
- **Notes:** A black board on a flat field is the plainest reel treatment among the games read so far; it is also why each high symbol carries its own coloured tile.
- **Measured:** dark, muted, warm and cool mixed, medium contrast · brightness 4% · saturation 12% · contrast 31% · warm 50% / cool 25% · brighter towards: top (1)
- **Palette (measured):** #000000 black 87%, #8c0e0a dark red 5%, #35391c brown 3%, #5f8451 green 2%, #299c38 green 2%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### VAULT bonus symbol: landing and win animations

`BN_0-1x` · atlas · 21 parts · largest 231×227 · sheet `sheets/BN_0-1x.webp`

- **Role:** The vault symbol's two animations; three or more vaults award the Cash Vault feature (as the paytable screen states).
- **Subject:** A round gold vault door with a spoked wheel handle and a ring of rivets, on a red tile with a gold frame; the landing frames begin as a white flash.
- **Style:** Rendered gold object, the same glossy manner as the other high symbols.
- **Rendering:** Hard-edged gold with radial highlights; the first landing frame is almost wholly white bloom.
- **Colour:** The brightest unit in the game, measured: light gold #fef885 28% and #fefdf0 20%, gold #feeb30 16%, orange #f7b214 7%, red #963115 5%; brightness 0.80.
- **Lighting:** Self-lit in the flash; otherwise a light from the front on the door's centre.
- **Ambience:** A jolt of anticipation: the flash marks it as the trigger symbol.
- **Materials:** Polished gold, red enamel tile.
- **Variants:** Two sequences: BN_land 7 frames, BN_win 14 frames.
- **Motion:** BN_land, 7 frames: a white flash that clears to show the door. BN_win, 14 frames: the door pulses brighter and the wheel appears to turn slightly between frames (inference from six frames).
- **Construction:** 21 trimmed frames; frame sequences.
- **Notes:** The same vault door, larger, is the hero of the Cash Vault pick screen.
- **Measured:** bright, saturated, warm, high contrast, hard-edged, strong highlights · brightness 80% · saturation 52% · contrast 68% · warm 88% / cool 11%
- **Palette (measured):** #fef885 light gold 28%, #fefdf0 light gold 20%, #feeb30 gold 16%, #f7b214 orange 7%, #963115 red 5%, #eb7d12 orange 4%

### Diamond: win animation

`H1_0-1x` · atlas · 14 parts · largest 219×214 · sheet `sheets/H1_0-1x.webp`

- **Role:** The frame-by-frame animation the diamond symbol plays when it is part of a win.
- **Subject:** A brilliant-cut diamond, blue-white with dark blue facets, on a red rounded tile with a gold hairline edge.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Red and ice blue, measured: light cyan #edfbfd 27%, red #a40205 27%, dark red #470303 14%, blue #191eec 2%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 14 frames.
- **Motion:** H1_win, 14 frames: the stone flares white and its facets shift between frames; one frame grows larger than the tile (219x214 against 181x161).
- **Construction:** One atlas page per symbol, 14 trimmed frames; a frame sequence, not a skeleton.
- **Notes:** The highest paying picture (100 for five in the paytable screen).
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 48% · saturation 62% · contrast 92% · warm 68% / cool 31% · brighter towards: top (1), top-right (1)
- **Palette (measured):** #edfbfd light cyan 27%, #a40205 red 27%, #470303 dark red 14%, #a5e7f9 light cyan 5%, #6fd2f7 cyan 3%, #191eec blue 2%

### Gold bars: win animation

`H2_0-1x` · atlas · 24 parts · largest 175×151 · sheet `sheets/H2_0-1x.webp`

- **Role:** The frame-by-frame animation the gold bars symbol plays when it is part of a win.
- **Subject:** Three gold bars, one leaning upright and stamped FINE GOLD, on a deep blue tile.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Blue against gold, measured: dark blue #04064b 29%, gold #fef401 18%, orange #f79f01 14%, blue #0d3abc 12%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 24 frames.
- **Motion:** H2_win, 24 frames: the three frames on the sheet differ only by a highlight moving over the upright bar (inference: a shine sweep).
- **Construction:** One atlas page per symbol, 24 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 38% · saturation 97% · contrast 91% · warm 53% / cool 47% · brighter towards: bottom-right (24)
- **Palette (measured):** #04064b dark blue 29%, #fef401 gold 18%, #f79f01 orange 14%, #0d3abc blue 12%, #d05e01 orange 11%, #973002 brown 6%

### Banknote bundles: win animation

`H3_0-1x` · atlas · 24 parts · largest 161×139 · sheet `sheets/H3_0-1x.webp`

- **Role:** The frame-by-frame animation the banknote bundles symbol plays when it is part of a win.
- **Subject:** Three bundles of green banknotes with a red and gold band, fanned over each other on a purple tile.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Green on purple, measured: black-violet #14062e 36%, dark green #0b5f06 15%, purple #44037d 15%, light greens #bdf781 and #72d241 10% each.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 24 frames.
- **Motion:** H3_win, 24 frames: near-identical frames with a light passing over the notes (inference: a shine sweep).
- **Construction:** One atlas page per symbol, 24 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 29% · saturation 87% · contrast 88% · warm 7% / cool 69% · brighter towards: top-right (24)
- **Palette (measured):** #14062e black 36%, #0b5f06 dark green 15%, #44037d dark purple 15%, #bdf781 green 10%, #72d241 green 10%, #30991d green 8%

### Dollar coins: win animation

`H4_0-1x` · atlas · 24 parts · largest 156×136 · sheet `sheets/H4_0-1x.webp`

- **Role:** The frame-by-frame animation the dollar coins symbol plays when it is part of a win.
- **Subject:** A stack of copper-gold coins with one large coin standing in front, a dollar sign embossed on it, on a dark green tile.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Gold on dark green, measured: black-green #021f01 30%, gold #fdd70d 27%, orange #ef860b 17%, brown #9e380c 13%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 24 frames.
- **Motion:** H4_win, 24 frames: the frames on the sheet are almost the same picture, so the movement is small, a glint on the coin (inference).
- **Construction:** One atlas page per symbol, 24 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 45% · saturation 93% · contrast 86% · warm 86% / cool 7% · brighter towards: right (24)
- **Palette (measured):** #021f01 black 30%, #fdd70d gold 27%, #ef860b orange 17%, #9e380c brown 13%, #d55c0c orange 3%, #fff589 light gold 3%

### Money bag: win animation

`H5_0-1x` · atlas · 24 parts · largest 130×156 · sheet `sheets/H5_0-1x.webp`

- **Role:** The frame-by-frame animation the money bag symbol plays when it is part of a win.
- **Subject:** A round gold sack tied with a red cord, a red dollar sign on its belly, green notes bursting from its mouth. No tile behind it.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Orange-gold with green, measured: orange #e4970a 42%, dark red #760d01 14%, green #8adc46 9%, gold #fadc31 7%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 24 frames.
- **Motion:** H5_win, 24 frames: the bag stays in place while a highlight moves on it (inference from three frames).
- **Construction:** One atlas page per symbol, 24 trimmed frames; a frame sequence, not a skeleton.
- **Notes:** The only high symbol without a coloured tile, so it reads lighter on the black reel.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 53% · saturation 88% · contrast 82% · warm 80% / cool 10% · brighter towards: top-right (24)
- **Palette (measured):** #e4970a orange 42%, #760d01 dark red 14%, #8adc46 green 9%, #b54e06 brown 9%, #fadc31 gold 7%, #f3f290 light gold 5%

### Dollar sign: win animation

`L1_0-1x` · atlas · 38 parts · largest 115×131 · sheet `sheets/L1_0-1x.webp`

- **Role:** The frame-by-frame animation the dollar sign symbol plays when it is part of a win.
- **Subject:** A fat gold dollar sign with a yellow-to-orange gradient, a dark red rim and a hot white core.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** All warm, measured: orange #f9a304 37%, dark red #8f1000 18%, gold #ffe865 17% and #ffda1e 11%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 38 frames.
- **Motion:** L1_win, 38 frames: the three frames on the sheet are the same shape with the lighting shifting slightly; the longest symbol animations in the game are these low symbols.
- **Construction:** One atlas page per symbol, 38 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 55% · saturation 91% · contrast 91% · warm 100% / cool 0% · brighter towards: top (38)
- **Palette (measured):** #f9a304 orange 37%, #8f1000 dark red 18%, #ffe865 gold 17%, #ffda1e gold 11%, #0b0100 black 8%, #c74200 orange 8%

### Cent sign: win animation

`L2_0-1x` · atlas · 38 parts · largest 161×196 · sheet `sheets/L2_0-1x.webp`

- **Role:** The frame-by-frame animation the cent sign symbol plays when it is part of a win.
- **Subject:** A copper cent sign, pink-orange on its face with a dark red bevel.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Copper, measured: dark red #670604 26%, orange #f29e5a 20%, red #af2208 16%, light orange #fccc9b 13%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 38 frames.
- **Motion:** L2_win, 38 frames: the three frames on the sheet are the same shape with the lighting shifting slightly; the longest symbol animations in the game are these low symbols.
- **Construction:** One atlas page per symbol, 38 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 38% · saturation 81% · contrast 84% · warm 100% / cool 0% · brighter towards: top-left (38)
- **Palette (measured):** #670604 dark red 26%, #f29e5a orange 20%, #af2208 red 16%, #da5518 orange 13%, #fccc9b light orange 13%, #040000 black 8%

### A: win animation

`L3_0-1x` · atlas · 38 parts · largest 212×195 · sheet `sheets/L3_0-1x.webp`

- **Role:** The frame-by-frame animation the a symbol plays when it is part of a win.
- **Subject:** A red slab-serif capital A with a white edge, a black outline and a faint diamond-shaped facet inside the letter.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Red, measured: #e50000 31%, #9e0101 21%, near-black #1c0505 18%, white edge #f0f8f8 12%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 38 frames.
- **Motion:** L3_win, 38 frames: the three frames on the sheet are the same shape with the lighting shifting slightly; the longest symbol animations in the game are these low symbols.
- **Construction:** One atlas page per symbol, 38 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 29% · saturation 76% · contrast 97% · warm 90% / cool 10%
- **Palette (measured):** #e50000 red 31%, #9e0101 red 21%, #1c0505 black 18%, #f0f8f8 light cyan 12%, #5e0404 dark red 4%, #9fdbde cyan 3%

### K: win animation

`L4_0-1x` · atlas · 38 parts · largest 150×127 · sheet `sheets/L4_0-1x.webp`

- **Role:** The frame-by-frame animation the k symbol plays when it is part of a win.
- **Subject:** A blue slab-serif capital K with a white edge and black outline.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Blue, measured: #0031b2 36%, #014af4 16%, black #110408 15%, white edge #ebf9fa 12%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 38 frames.
- **Motion:** L4_win, 38 frames: the three frames on the sheet are the same shape with the lighting shifting slightly; the longest symbol animations in the game are these low symbols.
- **Construction:** One atlas page per symbol, 38 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** mid-tone, vivid, cool, high contrast, hard-edged · brightness 32% · saturation 78% · contrast 96% · warm 0% / cool 100% · brighter towards: top (38)
- **Palette (measured):** #0031b2 blue 36%, #014af4 blue 16%, #110408 black 15%, #ebf9fa light cyan 12%, #061757 dark blue 6%

### Q: win animation

`L5_0-1x` · atlas · 38 parts · largest 143×143 · sheet `sheets/L5_0-1x.webp`

- **Role:** The frame-by-frame animation the q symbol plays when it is part of a win.
- **Subject:** A yellow-gold capital Q with a white edge and black outline.
- **Style:** The same glossy illustration as the still, redrawn frame by frame.
- **Rendering:** Pre-rendered frames with a bright sweep or flare added; hard silhouette, smooth gradients.
- **Colour:** Gold, measured: #fcd100 44%, black #140504 14%, white edge #eefbf8 12%, brown #9f7303 7%.
- **Lighting:** Light from above, with a travelling highlight in the animation (seen across the three frames on the sheet).
- **Ambience:** A short flash of reward; the picture itself never changes character.
- **Materials:** As the still symbol.
- **Variants:** One sequence of 38 frames.
- **Motion:** L5_win, 38 frames: the three frames on the sheet are the same shape with the lighting shifting slightly; the longest symbol animations in the game are these low symbols.
- **Construction:** One atlas page per symbol, 38 trimmed frames; a frame sequence, not a skeleton.
- **Measured:** bright, vivid, warm, high contrast, hard-edged, strong highlights · brightness 63% · saturation 78% · contrast 97% · warm 93% / cool 7% · brighter towards: top (38)
- **Palette (measured):** #fcd100 gold 44%, #140504 black 14%, #eefbf8 light cyan 12%, #9f7303 brown 7%, #e49401 orange 6%, #51380b brown 5%

### WILD: landing and win animations

`WW_0-1x` · atlas · 29 parts · largest 231×224 · sheet `sheets/WW_0-1x.webp`

- **Role:** The wild symbol's two animations: landing on the reel and taking part in a win.
- **Subject:** The word WILD in cream-to-gold western slab capitals with a dark red shadow, on a red tile with a gold frame; in the win frames the tile glows and a white light runs through the letters.
- **Style:** Lettering as a symbol, in the manner of a saloon sign.
- **Rendering:** Bevelled letters with a hard shadow; the tile has a soft darker pattern; glow frames add a white bloom.
- **Colour:** Red and cream-gold, measured: red #a40704 34%, light gold #fffef0 21%, dark red #530703 16%, gold #ffee26 4%.
- **Lighting:** From above (22 parts measured); in the win frames the light comes from the letters themselves.
- **Ambience:** Loud and simple.
- **Materials:** Painted sign lettering, enamel red.
- **Variants:** Two sequences: WW_land 10 frames, WW_win 19 frames.
- **Motion:** WW_land, 10 frames: the letters arrive tilted and larger than the tile, then settle (the frames on the sheet show the word skewed, then square). WW_win, 19 frames: the tile and letters brighten to a glow and back.
- **Construction:** 29 trimmed frames on one page; frame sequences.
- **Notes:** The paytable screen says the wild appears on reels 2, 3, 4 and 5 only.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 47% · saturation 70% · contrast 92% · warm 100% / cool 0% · brighter towards: top (22)
- **Palette (measured):** #a40704 red 34%, #fffef0 light gold 21%, #530703 dark red 16%, #fdf4a5 light gold 5%, #ffee26 gold 4%, #f29717 orange 4%

### Reel symbols at rest, dimmed copies and Money Charge values

`symbols-raw_0-1x` · atlas · 88 parts · largest 361×379 · sheet `sheets/symbols-raw_0-1x.webp`

- **Role:** The still picture of every reel symbol, a darkened copy of each for reels that are dimmed during a feature, and the green Money Charge disc with every credit value it can carry.
- **Subject:** Thirteen symbols: a gold vault door on a red tile (BN, the VAULT bonus), WILD lettering on a red tile (WW), a cut diamond on a red tile (H1), gold bars on blue (H2), banded banknote bundles on purple (H3), stacked dollar coins on green (H4), a gold money bag stuffed with notes (H5), a gold dollar sign (L1), a copper cent sign (L2), red A, blue K, yellow Q, green J; and a green disc in a gold ring (TT) alone and with values from 50 to 75000.
- **Style:** Glossy casino-floor illustration: rendered 3D-looking objects for the money symbols, bevelled serif letters for the royals. No character and no scene, only objects of wealth.
- **Rendering:** Smooth airbrushed gradients, hard silhouettes, bright specular streaks on gold; the high symbols sit on a rounded square tile with a darker vignette, the low ones stand free with a thin white edge and a black outline. The value digits are cream slab numerals with a dark bevel.
- **Colour:** Each symbol owns one colour pair, measured on the sheet: black #17200f leads at 47% (the dimmed copies), then green #16be14 and #066c0c (the discs), orange #f1950a and gold #fee115. Hues: green 52%, yellow 20%, orange 19%, red 5%.
- **Lighting:** A light from above on almost every part (top on 67 of the parts measured); gold carries white streak highlights, the diamond a blue-white flare.
- **Ambience:** Bright, plain and money-minded: a bank counter's contents laid out as icons.
- **Materials:** Polished gold, cut diamond, printed paper notes with a red-gold band, sack cloth drawn as gold, enamelled letters, a green dimpled disc that reads as a casino chip or a button (inference).
- **Variants:** 13 symbols, each with a `_b` copy darkened to about a quarter of its brightness; the disc blank, and with 29 lit values (50 to 75000) and 29 dimmed ones. No blurred spin copies were seen in the files.
- **Motion:** None in this atlas: these are the stills. The tool's lines 'H x5, L x6, TT x29' are not frame sequences, they are the numbered symbol names (H1 to H5, L1 to L6, the values). Each symbol's animation is its own atlas (see the win-animation units).
- **Construction:** 88 sprites on one page; values are baked into the disc picture, one sprite per value, not live text. Two small streak sprites (HardRain, Sparks) are particle pictures.
- **Notes:** The dimmed copies are drawn, not tinted at run time, which doubles the still set. The largest still is 361x379, so symbols ship larger than the 130-pixel cell of the desktop layout.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 34% · saturation 64% · contrast 55% · warm 44% / cool 31% · brighter towards: top (67), top-left (5), top-right (3)
- **Palette (measured):** #17200f black 47%, #494841 grey 11%, #16be14 green 8%, #f1fafa light cyan 6%, #066c0c dark green 6%, #f1950a orange 4%


## Logo and title

The game's own wordmark.

### Logo, feature titles and jackpot panel

`base_game-raw_0-1x` · atlas · 19 parts · largest 775×335 · sheet `sheets/base_game-raw_0-1x.webp`

- **Role:** The Capital Gains logo, the Money Charge Jackpots and Money Charge Bonus titles, the jackpot meter panel and the reel frame.
- **Subject:** CAPITAL GAINS in gold slab-serif capitals on two arched lines with a red-brown extrusion and a gold laurel under it; MONEY CHARGE in white-violet italic capitals over JACKPOTS or BONUS in yellow, on a purple extrusion; a black four-meter panel (Grand, Major, Minor, Mini) with rainbow hairlines and gold corner beads; a blue panel in a gold frame.
- **Style:** Casino cabinet signage: bevelled, extruded display lettering.
- **Rendering:** Gradient-filled letters with a light top bevel, a dark extruded side and a thin outline; panels are flat black with hairline colour.
- **Colour:** Measured: black #040408 33%, dark purple #4c1e6c 11%, gold #fce615 6%, pale blue #e9ebf2 5%, dark blue #130a4a 5%. The logo is gold on red-brown; the feature title is violet and yellow, set apart from the green game on purpose (inference).
- **Lighting:** From above (10 parts measured): light bevels on the top of each letter.
- **Ambience:** Confident and old-school, like a sign above a bank of machines.
- **Materials:** Polished gold lettering, chrome-white letters, black glass.
- **Variants:** The logo at two sizes (549x318 and 192x110, the small one three times); each title with and without the word JACKPOTS (the files call it 'no jackpot'), several copies; the meter panel whole and the Grand meter alone.
- **Motion:** Stills; blue lightning sequences play around the title and the meters (see the lightning unit).
- **Construction:** 19 sprites; repeated copies of one sprite are separate entries of the same picture.
- **Notes:** The feature brand, Money Charge Jackpots, is given as much room on screen as the game's own logo.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 34% · saturation 54% · contrast 80% · warm 47% / cool 46% · brighter towards: top (10)
- **Palette (measured):** #040408 black 33%, #4c1e6c dark purple 11%, #fce615 gold 6%, #e9ebf2 light blue 5%, #130a4a dark blue 5%, #b4bfe4 light blue 3%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Big win particles

`bigwin-particles_0-1x` · atlas · 50 parts · largest 330×313 · sheet `sheets/bigwin-particles_0-1x.webp`

- **Role:** The pieces thrown during a big win: spinning gems and coins over a ray burst.
- **Subject:** A teal-cyan cut gem in 24 frames of a tumble, a gold coin in 24 frames of a flip from face to edge, a blue-white starburst of rays, and a small white sparkle.
- **Style:** Small rendered 3D objects.
- **Rendering:** Sharp, glossy, with motion-ready silhouettes; the ray burst is fully soft.
- **Colour:** Measured: orange #f3a806 26%, cyan #74d9fb 13%, pale green-white #f8fef6 13%, brown-gold #b98603 9%, dark cyan #0c7c7e 6%.
- **Lighting:** Top and top-right (measured).
- **Ambience:** Shower of riches.
- **Materials:** Gold; cut gem.
- **Variants:** Two sequences of 24 frames, one ray burst (330x313), one sparkle.
- **Motion:** coin, 24 frames: a full flip. gem, 24 frames: a full tumble. Seen in play: under a HUGE WIN label the coins and gems fall over the whole screen from above, with the ray burst behind the win box.
- **Construction:** 50 sprites; particle sprites for an emitter (inference).
- **Notes:** The gem here is teal, not the blue-white diamond of the H1 symbol: a separate asset.
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 65% · saturation 69% · contrast 58% · warm 47% / cool 53% · brighter towards: top (11), top-right (9), right (2)
- **Palette (measured):** #f3a806 orange 26%, #f8fef6 light green 13%, #74d9fb cyan 13%, #b98603 brown 9%, #0c7c7e dark cyan 6%, #040f10 black 6%

### Cash Vault feature: the vault pick

`gateway-vault-raw_0-1x` · atlas · 87 parts · largest 994×565 · sheet `sheets/gateway-vault-raw_0-1x.webp`

- **Role:** The second screen of the Cash Vault feature, where one of two vaults is chosen and opens to the Money Charge bonus or free spins.
- **Subject:** Two large gold vault doors side by side in dark green recesses, closed and with one open to a dark red-brown interior; a vault door in 50 frames of swinging open; a gold slot-reel window with two dark bars (the spinner that shows the number of spins and wilds, as on the loading card '15 / 200'); the MONEY CHARGE BONUS title growing in; a white-violet lightning flash; a green panel in a gold frame for the prompt.
- **Style:** Rendered gold hardware, the game's richest pictures.
- **Rendering:** Detailed radial highlights on the door, rivets, a hard gold bevel on the spinner; the intro flash is soft white and violet.
- **Colour:** Measured: orange #ef981a 29%, black-green #092707 18%, gold #f9e549 11%, light gold #fcfa97 8%, dark red #461a12 5%.
- **Lighting:** From above and from the front on the doors (top on 13 parts); the flash lights the whole frame.
- **Ambience:** The reveal: heavy doors, a choice, a flash.
- **Materials:** Polished gold, steel rivets, dark vault interior.
- **Variants:** Vaults closed and one open (994x565 each); four sequences.
- **Motion:** vault_spin_door, 50 frames: the door turns from face-on to edge-on as it swings open (frame 49 is a thin sliver). vault_spinner, 13 frames: the reel window appears and its bars change. vault_mc, 13 frames: the Money Charge Bonus title scales up. vault_intro, 6 frames: a lightning flash across the screen.
- **Construction:** 87 sprites on the largest page of the game (1988x2982 as shipped); two 3x3 sprites are invisible hit areas for the left and right vault.
- **Notes:** Not reached in play: read from the files and from the paytable's description ('a 2nd screen will appear displaying two vault options').
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 52% · saturation 72% · contrast 72% · warm 74% / cool 16% · brighter towards: top (13), right (5), bottom-left (2)
- **Palette (measured):** #ef981a orange 29%, #092707 black 18%, #f9e549 gold 11%, #fcfa97 light gold 8%, #b8520f orange 6%, #6b4a44 red 6%


## Effects

Frame sequences, glows, particles and transitions.

### Lightning

`lightning_0-1x` · atlas · 276 parts · largest 513×122 · sheet `sheets/lightning_0-1x.webp`

- **Role:** Blue electric arcs that frame the jackpot meters, the feature title, locked Money Charge symbols, the win box and the bonus summary.
- **Subject:** Branching bolts in three lengths, horizontal arcs, and closed frames of lightning: rectangles for a reel cell and for meters, a ring, and one thin gold rectangle (win_over).
- **Style:** Stylised electricity, drawn rather than photographic.
- **Rendering:** White-hot core, saturated blue body and a soft blue halo; 77% of edges measured soft, the softest unit in the game.
- **Colour:** Blue only, measured: #0269f7 52%, light cyan #f4fdff 22%, cyan #0db4ff 10%; cool 99.7%.
- **Lighting:** Self-lit.
- **Ambience:** Energy and charge, the only cold colour in a green and gold game, which is why it reads at once.
- **Materials:** Light.
- **Variants:** 14 sequences: frame_base 40 frames, frame_bonus 23, jackpot_grand, jackpot_major, jackpot_mini_minor, count_up, logo and three summary rows 20 each, border_end 11, and bolts large, medium and small 7 each.
- **Motion:** Each sequence is a loop of a crackling arc that changes shape every frame; the cell frames run around a symbol's square (seen locked on each disc in the bonus screens), the bolts strike downward (seen behind WINNER).
- **Construction:** 276 trimmed frames on one page, the largest sequence set in the game; frame sequences drawn additively over the scene (inference from the black-free, glow-only pictures).
- **Notes:** The feature's name is Money Charge, and lightning is its whole visual identity: no other effect family exists in the files.
- **Measured:** mid-tone, vivid, cool, high contrast, glow or soft effect, strong highlights · brightness 59% · saturation 71% · contrast 65% · warm 0% / cool 100% · brighter towards: right (6), top-right (5), bottom (4)
- **Palette (measured):** #0269f7 blue 52%, #f4fdff light cyan 22%, #0db4ff cyan 10%, #a7ecff light cyan 5%, #68daff cyan 5%, #11f4ff cyan 3%


## Game interface

Buttons, counters and panels drawn for this game.

### Autoplay panel

`autoplays_0-1x` · atlas · 30 parts · largest 1789×998 · sheet `sheets/autoplays_0-1x.webp`

- **Role:** The autoplay settings screen: number of spins, stop conditions and loss and win limits.
- **Subject:** A black full-screen panel, rounded square choice buttons in dark and in green, toggles, slider tracks with a round knob that has a green centre, a red flash box and a close button with a white cross.
- **Style:** The same neutral interface as the console.
- **Rendering:** Dark gradients, thin light rims; the selected state is a flat yellow-green gradient.
- **Colour:** Measured: black #010102 83%, dark blue-grey #2b2937 8%, green #8bad37 4% and #537e2e 2%.
- **Lighting:** Top and bottom rims.
- **Ambience:** Functional.
- **Materials:** Dark plastic; green lit state.
- **Variants:** 30 sprites: five spin-count buttons in two states, two toggles in two states, three sliders.
- **Motion:** State changes only.
- **Construction:** One atlas; text is live.
- **Notes:** Named 'ukgc' in two files: a regulatory panel (UK rules), shared across the provider's games by inference.
- **Measured:** dark, muted, warm and cool mixed, low contrast, hard-edged · brightness 6% · saturation 9% · contrast 12% · warm 0% / cool 14% · brighter towards: bottom (15), top (7), top-left (3)
- **Palette (measured):** #010102 black 83%, #2b2937 dark blue 8%, #8bad37 green 4%, #537e2e green 2%

### Console and menus

`menus-raw_0-1x` · atlas · 142 parts · largest 692×404 · sheet `sheets/menus-raw_0-1x.webp`

- **Role:** The bottom control bar and the menu: spin, max bet, bet levels, multiplier, sound, menu, help, and the bet, win and balance boxes.
- **Subject:** A round spin button with a grey circular arrow, D-shaped side buttons, rounded square and pill buttons, a speaker icon in three states, a black modal panel, and small dark boxes with a blue hairline for bet, win and balance.
- **Style:** Neutral dark interface, not themed to the game.
- **Rendering:** Dark violet-grey gradients with a thin light rim and a soft drop shadow; icons are flat pale grey.
- **Colour:** Measured: black #09090e 70%, dark blue-grey #2c283b 19%, grey #5b5b6e 3%; saturation 0.29. The selected bet level is the one green button (seen in play).
- **Lighting:** A top light on each button (top on 45 parts).
- **Ambience:** Quiet and functional; it steps back from the game.
- **Materials:** Dark glass or plastic.
- **Variants:** 142 sprites: each button in up, over, down and disabled states; 82 smaller parts not shown on the sheet.
- **Motion:** State changes only.
- **Construction:** One atlas of states; labels are live text.
- **Notes:** Inference: this console is AGS's own shared interface dressed for no game in particular (the file names say 'ags_accounts', 'ags_deposit', 'ags_home'). It is read here because that was not checked against a second AGS game.
- **Measured:** dark, saturated, cool, medium contrast · brightness 12% · saturation 28% · contrast 26% · warm 0% / cool 78% · brighter towards: top (45), bottom (17), top-right (10)
- **Palette (measured):** #09090e black 70%, #2c283b dark blue 19%, #5b5b6e grey 3%

### Paytable parts

`paytable_0-1x` · atlas · 69 parts · largest 655×278 · sheet `sheets/paytable_0-1x.webp`

- **Role:** The pictures the eleven help pages are built from.
- **Subject:** Teal pay boxes with a gold hairline; rows of small symbols (five, four and three of a kind); the vault pays (5 = 1000, 4 = 250, 3 = 100) in orange numerals; the Money Charge Bonus title; the two vaults; the PowerXStream logo in chrome and red; WILD, vault and green disc at several sizes; four jackpot name plates (red Grand, green Major, blue Minor, purple Mini); page dots and round arrow buttons.
- **Style:** The game's symbols reused small, on certificate-like panels.
- **Rendering:** Flat panels with hairlines; text set over them live in red-orange outlined serif capitals (seen on the help screens).
- **Colour:** Measured: black-teal #023636 64%, black #041007 13%, orange #c76e09 4%, gold #facd12 3%.
- **Lighting:** Top (measured).
- **Ambience:** Formal and dense.
- **Materials:** Printed panel.
- **Variants:** 69 sprites; pay rows are pre-composed pictures, one per symbol.
- **Motion:** None.
- **Construction:** Page pictures plus live text.
- **Notes:** The pay rows are baked as pictures while the figures beside them are live text. The jackpot plates fix the tier colours: Grand red, Major green, Minor blue, Mini purple.
- **Measured:** dark, vivid, cool, medium contrast, hard-edged · brightness 23% · saturation 89% · contrast 34% · warm 18% / cool 78% · brighter towards: top (9), top-left (3), top-right (1)
- **Palette (measured):** #023636 black 64%, #041007 black 13%, #c76e09 orange 4%, #facd12 gold 3%

### Loading screen parts

`preloader_0-1x` · atlas · 19 parts · largest 922×539 · sheet `sheets/preloader_0-1x.webp`

- **Role:** The loading screen: three feature cards, the logos and the progress bar.
- **Subject:** A card of the Money Charge grid (green discs with values and MINI plates in lightning-blue cells), a card of the vault spinner showing 15 and 200, a card of the two closed vaults, the Money Charge Jackpots and Bonus titles, the PowerXStream logo, the small Capital Gains logo, a gold progress bar in a dark capsule, Continue and No buttons and the AGS mark.
- **Style:** A sales poster: each feature shown as a picture with a caption.
- **Rendering:** Small composed screenshots of the features with a soft drop shadow.
- **Colour:** Mostly black (#020302 71%) around small bright pictures; hues split blue, green, yellow and orange about evenly (measured).
- **Lighting:** Top (measured).
- **Ambience:** A pitch before play: it names the three things to hope for.
- **Materials:** As the game's own art.
- **Variants:** 19 sprites.
- **Motion:** The bar fills (loader_bar under a mask).
- **Construction:** One atlas.
- **Notes:** The three cards are the fastest summary of the game's features: Cash Vault pick, Money Charge Jackpots, Free Spins with added wilds.
- **Measured:** dark, saturated, cool, medium contrast · brightness 15% · saturation 32% · contrast 33% · warm 16% / cool 70% · brighter towards: top (6), bottom (2), top-right (1)
- **Palette (measured):** #020302 black 71%, #2e2d41 dark blue 6%, #6a627f purple 2%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `ios_scroll`: 1 parts
- `preloadSpinner`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Alfa Slab One (Regular); AvantGarde Bk BT (Book); Bebas Neue (Regular); Bodoni MT (Bold); Cinzel (Bold); Cinzel (Regular); Dollar Bill (Regular); Gentium Basic (Regular); Gentium Book Basic (Bold); Guardi 55 Roman (Roman); Helvetica (Bold); Helvetica (Regular); Hiroshige Std (Bold); Myriad Pro (Bold); Myriad Pro (Regular); Myriad Pro (Semibold); Noto Serif (Bold); Nunito Sans (Regular); Roboto (Bold); Roboto (Medium); Roboto (Regular); Saddlebag (Regular); Trajan Pro (Regular); Universal Serif (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1188 components cut from 29 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
