# Money Gong Empress: art report

igt · run `2026-11-27-0950-igt-money-gong-empress` · captured 2026-11-27

Source: the provider's free-play demo, https://stage-game-launcher-lux.isoftbet.com/1015/201473?mode=0&cur=USD&lang=en

**Extracted:** 1191 named components from 55 textures in 55 atlases; 31 Spine skeletons; 46 frame sequences (530 frames); 8 fonts. Grouped into 52 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

The purple sister of Money Gong Emperor: the same gold gong with its red fret knot, the same firecrackers, pots and jackpot balls, moved onto a purple wave-scale wall with purple royals, four gold objects on coloured plates and one painted character, a smiling empress in purple brocade, as the top symbol and the host of the pop-ups.

**Style.** Two manners side by side. Symbols, pots, gong and firecrackers are glossy, toy-like stylised objects. The empress is a realistic painted figure. The setting is not a place but ornament: a purple ground pressed with a wave-scale pattern, cloud scrolls and Greek-key bands. The interface buttons are a neutral charcoal set outside the theme, except the game's own red and green Bonus Buy buttons.

**Rendering.** Smooth airbrushed gradients with hard silhouettes, a gold or light rim and white star glints on every object; lettering with a white outline and a dark extrusion; effects as soft light on black, many of them greyscale. Nothing has a drawn black outline. Measured hard-edged overall (soft edge 0.075).

**Colour.** Purple ground, gold objects. Measured over all of the game's art: near-black #180c0c at 17% and dark purple #450657 at 13% lead; hues are orange 40%, yellow 21%, purple 17%, red 10%; warm 64% against cool 16%, saturation 0.63, brightness 0.39. The backgrounds and the reel backing are purple only (#39034d, #3d0156; hues 100% purple). The other colours are a code kept from the sister game: green #04ed61 is the money ball, the gong's features each have a colour, and each jackpot tier has its own (Grand red, Major green, Maxi purple, Minor blue, Mini orange). Red survives only on the gong's emblem, the firecrackers, the logo's extrusion and the multipliers.

**Lighting.** One top light on everything (measured from the top on 189 parts, top-right on 29, top-left on 19) with specular glints on the gold; the grounds are dark (brightness 0.07 to 0.09) with a low magenta glow, so the gold objects are the light of the screen.

**Ambience.** Festive, lucky and rich, and softer than the sister game: the same New Year firecrackers, coins and pots of gold, in a night-purple room with lotus, fan and koi and a smiling empress. Calm in the base game; the bonus spins turn the board itself gold.

**Shape language.** Circles everywhere: gong, coins, money balls, jackpot discs, round buttons, the ring in the background, the bonus wheel. Around them, cloud scrolls and a Greek-key band as the two ornaments, and pill-shaped plaques for every figure. The lettering is the one angular element.

**Materials.** Polished gold above all; purple silk or lacquer for the grounds; jade or glass balls; enamel plates; brocade and gold jewellery on the empress; paper firecrackers; smoked glass for the buttons.

**Typography and lettering.** The logo is heavy angular faux-brush capitals in bevelled yellow gold with a deep red extrusion, with EMPRESS in smaller gold capitals. Jackpot names, BONUS BUY and MONEY GONG BONUS are drawn in the same faux-brush manner; two such faces are embedded (Gang of Three and Nuku Nuku), which is probably where they come from (inference). The three feature words are rounded poster capitals, one colour each. Running text is live Noto Sans (Black, Condensed Black, Condensed Bold, Regular, Display Condensed Bold) with Passion One. Figures are bitmap sets drawn per place: white for the bonus spins, gold for the Bonus Buy price, magenta and gold-edged for values, brown lacquer and yellow for the Money Gong Bonus.

**Motion.** Spine skeletons carry all of it: 17 skeletons in Spine 4.0 or 4.1 (the report header counts 31 because 14 layout entries of the client are counted with them). By their animation names: every symbol has a win and the empress an expanded appear and win, the money ball four landings, the gong turns like a coin to a feature face and is struck, pots grow and are hit by coins, firecrackers are lit and go off, four win tiers come in, loop and leave, and the empress pops up with a scroll. Around them, 46 frame sequences (530 frames) of sparks, sweeps, trails and bursts, and nine particle files. No skeleton frame is shown: the project's drawing tool is written for Spine 3.7 and drew none of these. The four real screens show only the intro, the base game and a spin, so movement is read from names and parts and is inference throughout.

**Variants and themes.** One base ground, one dim stage for the intro, and a board that changes backing from dark purple to gold for the bonus spins; a Hold & Win grid, a round Money Gong Bonus wheel and a Bonus Buy panel as further scenes (parts only, not seen in play). Every reel symbol ships sharp and motion-blurred. The money ball comes green and gold, plain and with four jackpot names. The gong has six faces. The top symbol comes one cell and three cells tall. Landscape only was captured; portrait animations are named in the files.

**How it is built.** 1,191 named sprites on 55 textures in 52 units, 50 of them the game's own art. Solid art is PNG in TexturePacker sheets or Spine atlases; effects are JPEG on black on separate pages of the same atlas; backgrounds are single JPEGs with no layers (1584x720). A reel symbol is about 233x227 on a plate, or 291x272 for a royal, for a cell of about 299x303; the empress of the pop-up is the largest art (body 847x629). Half of the reel frame is shipped and probably mirrored (inference). Three skeletons (the two ambients and the transition) ship only a placeholder. Against Money Gong Emperor's 51 units, what is new is the Bonus Buy (three units), the empress and the vortex effects; file names such as emperor_Blick and a REPEAT PAYS gong face show the package was built from the sister game's (inference).

**Consistency.** Very tight, and tight across two games. One emblem at four sizes, two ornaments, one top light and a ground of a single hue hold every screen together. The gong, pots, firecrackers and meters are kept exactly, in red and gold, so the family is recognised at once; the ground, the royals and the character carry the difference. The loose ends are the neutral grey buttons and the plain sans win titles, which belong to the provider's kit more than to the game.

**What to take from it.** (1) A second game from one art package. Gong, pots, firecrackers, jackpot balls, meters, frame and every effect are reused; the new work is one ground colour, five recoloured royals, four object symbols and one character. For a studio this is the cheapest route to a second leading title. (2) What changes is what the player sees most: the hue of the ground (red to purple, measured 100% purple on backgrounds and reel backing) and the face of the top symbol. What carries the brand stays untouched: the gold gong with its red knot. (3) The royals are dyed in the ground's own colour (purple on purple here, red on red in the sister game) and held off it by a gold edge and a glow. Gold is kept for the symbols that pay. (4) Colour as a code survives the reskin: green money ball, one colour per gong feature, one per jackpot tier, taught on the intro panel and repeated on gong, balls and meters. A code that is independent of the theme can move between games. (5) No scenery at all: a patterned wall with a seat for the gong, and a board that turns from dark purple to gold for the bonus spins. (6) One painted character, saved for the top symbol and the pop-up, cut into a few large parts (head, body, hair, sleeves, beads, eyes) and able to stand three cells tall. Everything else that moves is an object. (7) Effects are greyscale or gold light on black, shipped apart from the solid art and cut to their object (a sweep per wordmark, a shine per part of the empress, a full-figure mask). An AI art pipeline can follow that split: make the solid piece, derive masks and glows from its outline. (8) Pre-rendered blur: every reel symbol has a second, motion-blurred picture. Plan two outputs per symbol. (9) Several drawn number sets, each tied to one place and prize, instead of one font: figures are treated as art.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 39% · saturation 63% · contrast 49% · warm 64% / cool 16% · brighter towards: top (189), top-right (29), top-left (19)

Palette: #180c0c black 17%, #450657 dark purple 13%, #521e09 brown 7%, #8c887f grey 7%, #fafaf7 light yellow 5%, #3d3b31 grey 5%, #675a47 brown 4%, #c9c5c0 grey 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 5 | 12% | 94% | 31% | 10% / 88% | #3b034e dark purple 80%, #710691 dark purple 12% |
| Reel board | 9 | 38% | 88% | 55% | 70% / 27% | #3d0255 dark purple 20%, #4e0d02 dark red 17%, #f2b80f orange 17% |
| Symbols | 6 | 51% | 78% | 63% | 73% / 15% | #e4a626 orange 19%, #fae44f gold 14%, #a45812 brown 11% |
| Characters | 1 | 24% | 84% | 66% | 62% / 27% | #27080e black 26%, #8a04a6 purple 20%, #630867 dark magenta 17% |
| Logo and title | 3 | 55% | 63% | 66% | 89% / 0% | #fbe95b gold 22%, #7b110a dark red 14%, #eba736 orange 13% |
| Win celebrations and banners | 5 | 38% | 58% | 44% | 97% / 2% | #56553a brown 24%, #1c140b black 20%, #612807 brown 14% |
| Effects | 14 | 42% | 48% | 43% | 63% / 4% | #130d08 black 19%, #3f3126 brown 14%, #878178 grey 10% |
| Game interface | 6 | 36% | 63% | 55% | 56% / 23% | #331126 dark magenta 35%, #fdfdfb light yellow 6%, #f0b818 orange 6% |
| Typography | 1 | 39% | 81% | 43% | 100% / 0% | #1f0704 black 45%, #fce12a gold 28%, #632d14 brown 11% |
| Provider interface (shared) | 2 | 18% | 38% | 7% | 1% / 41% | #120c1d black 80%, #ffffff white 11%, #2e263d dark purple 8% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Base game background

`40332634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Main--Landscape-jpg` · atlas · 1 parts · largest 1584×720 · sheet `sheets/40332634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Main--Landscape-jpg.webp`

- **Role:** The ground behind the whole base game.
- **Subject:** A purple wall pressed with a wave-scale (seigaiha) pattern, with one large round frame of cloud-scroll ornaments embossed at the left, the seat of the gong. No place, no horizon, no object.
- **Style:** Ornament as setting: a patterned surface, not a scene.
- **Rendering:** Smooth gradient with a fine embossed pattern and soft raised ornament in the same colour.
- **Colour:** One hue only: dark purple #39034d at 90% and magenta-purple #78058d at 10%; hues 100% purple, brightness 0.085, saturation 0.96, contrast 0.09.
- **Lighting:** A magenta glow rises from the bottom left (measured: light from bottom-left); the top right falls to near black.
- **Ambience:** Rich, quiet and nocturnal; it gives the screen its colour and then stays out of the way.
- **Materials:** Embossed lacquer or silk (inference from the sheen).
- **Variants:** One landscape picture; the files name a portrait layout that was not captured.
- **Motion:** None in the picture itself.
- **Construction:** A single 1584x720 JPEG, no layers.
- **Notes:** The sister game Money Gong Emperor uses the same wall and ring in red: here the whole ground is turned to purple.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 8% · saturation 96% · contrast 9% · warm 3% / cool 94% · brighter towards: bottom-left (1)
- **Palette (measured):** #39034d dark purple 90%, #78058d dark magenta 10%

### Preloader background with the logo

`40332634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Preloader--Landscape-jpg` · atlas · 1 parts · largest 1584×720 · sheet `sheets/40332634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Preloader--Landscape-jpg.webp`

- **Role:** The loading screen.
- **Subject:** The logo MONEY GONG EMPRESS in bevelled gold with a red extrusion, on a gold coin with gold cloud scrolls, in the middle of a purple wave-scale ground ringed with purple cloud ornaments.
- **Style:** Glossy 3D title art on a flat ornamental ground.
- **Rendering:** Hard bevels with white star glints on the letters; soft embossing on the ground.
- **Colour:** Purple with a gold and red centre: #3e074f 62%, #6f0893 19%, gold #f5e169 5%, dark red #7e1510 4%; contrast 0.74.
- **Lighting:** Lit from the top (measured); the logo is the only bright thing and a dark vignette closes the bottom.
- **Ambience:** A rich, festive opening.
- **Materials:** Polished gold lettering, red lacquer sides, embossed purple ground.
- **Variants:** One landscape picture.
- **Motion:** None; the logo is baked into the picture.
- **Construction:** A single 1584x720 JPEG with the logo painted in.
- **Notes:** The only place where the red of the sister game survives at size: the logo's extrusion.
- **Measured:** dark, vivid, cool, high contrast, hard-edged · brightness 18% · saturation 88% · contrast 74% · warm 19% / cool 79% · brighter towards: top (1)
- **Palette (measured):** #3e074f dark purple 62%, #6f0893 purple 19%, #f5e169 gold 5%, #7e1510 dark red 4%, #a009bd magenta 2%

### Intro and feature background

`40332634ad5e24bd264ae5a7d48701fc30b342c33ba3FeaturesBG-jpg` · atlas · 1 parts · largest 1584×720 · sheet `sheets/40332634ad5e24bd264ae5a7d48701fc30b342c33ba3FeaturesBG-jpg.webp`

- **Role:** The ground behind the intro panel that explains the features.
- **Subject:** A dark purple stage with a soft light from above, two thin vertical light seams in the middle and rows of red firecrackers with gold characters along the bottom corners.
- **Style:** A staged backdrop: dim, with the props pushed to the edges.
- **Rendering:** Soft gradients; the firecrackers are small glossy 3D-looking objects, darkened.
- **Colour:** Dark purple #410159 at 82%, near-black #240322 11%, dark red #6a0f1a 3% for the firecrackers; brightness 0.083.
- **Lighting:** A purple wash from the top centre; everything else is in shade.
- **Ambience:** Expectant, like a curtain before a show.
- **Materials:** Paper firecrackers with gold print; the rest is light.
- **Variants:** One landscape picture.
- **Motion:** None in the picture.
- **Construction:** A single 1584x720 JPEG.
- **Notes:** The firecrackers are the only red objects the game keeps from its sister.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 8% · saturation 98% · contrast 10% · warm 6% / cool 92%
- **Palette (measured):** #410159 dark purple 82%, #240322 black 11%, #74019e purple 3%, #6a0f1a dark red 3%

### Bonus spins ambient layer (placeholder only)

`FreeSpinsAmbient` · atlas · 1 parts · largest 16×16 · sheet `sheets/FreeSpinsAmbient.webp`

- **Role:** A skeleton meant to play an ambient loop over the bonus spins.
- **Subject:** No picture: the atlas holds one placeholder on a 16x16 texture.
- **Style:** Nothing to read.
- **Rendering:** Nothing to read.
- **Colour:** Nothing measured: the unit has no art.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** Six animations by name: in, loop and out, each for landscape and portrait.
- **Motion:** A Spine 4.0 skeleton of 2 bones and 1 slot; what it shows is not in the files read (inference: particles).
- **Construction:** A 16x16 PNG and a skeleton file.
- **Notes:** Listed so that the package is whole; it carries no art.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 2 bones · 1 slots · animations: FreeSpinsLandscapeIdleIn (0 s), FreeSpinsLandscapeIdleLoop (0 s), FreeSpinsLandscapeIdleOut (0 s), FreeSpinsPortraitIdleIn (0 s), FreeSpinsPortraitIdleLoop (0 s), FreeSpinsPortraitIdleOut (0 s)

### Base game ambient layer (placeholder only)

`MainAmbient` · atlas · 1 parts · largest 16×16 · sheet `sheets/MainAmbient.webp`

- **Role:** A skeleton meant to play an ambient loop over the base game.
- **Subject:** No picture: the atlas holds one placeholder on a 16x16 texture.
- **Style:** Nothing to read.
- **Rendering:** Nothing to read.
- **Colour:** Nothing measured: the unit has no art.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** Two animations by name, MainAmbientLandscape and MainAmbientPortrait.
- **Motion:** A Spine 4.0 skeleton of 2 bones and 1 slot. What it shows in the game, if anything, is drawn elsewhere, probably by the particle files (inference).
- **Construction:** A 16x16 PNG and a skeleton file.
- **Notes:** Listed so that the package is whole; it carries no art.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 2 bones · 1 slots · animations: MainAmbientLandscape (0 s), MainAmbientPortrait (0 s)


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Bonus spins frame and counter figures

`FreeSpins.desktop` · atlas · 17 parts · largest 918×1189 · sheet `sheets/FreeSpins.desktop.webp`

- **Role:** The reel frame of the bonus spins, a gold plaque and the white figures of its counters.
- **Subject:** Half a gold reel frame with a round side medallion and a red tassel, a gold plaque with cut corners, and a set of fat white figures with a dark red outline (0 to 9, currency signs, comma, point).
- **Style:** Gold furniture and poster figures.
- **Rendering:** The frame is airbrushed gold with a light rim; the figures are flat white with a dark outline.
- **Colour:** Brown-gold #984f06 33%, white #fefefd 18%, near-black #340802 17%, gold #ecb31e 16%; warm 1.0.
- **Lighting:** Top-lit (measured).
- **Ambience:** Rich and plain.
- **Materials:** Gold metal and a red silk tassel.
- **Variants:** One frame; the base game's frame in Main.desktop is the same build in gold with purple.
- **Motion:** None in the sheet.
- **Construction:** 17 sprites; the frame half is 918x1189 and is probably mirrored for the other side (inference).
- **Notes:** White figures on gold are the most legible numbers in the package.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 50% · saturation 75% · contrast 76% · warm 100% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #984f06 brown 33%, #fefefd light orange 18%, #340802 black 17%, #ecb31e orange 16%, #c6810f orange 9%, #631f05 brown 2%

### Hold & Win grid parts

`HoldAndWin.desktop` · atlas · 5 parts · largest 1073×134 · sheet `sheets/HoldAndWin.desktop.webp`

- **Role:** The furniture of the Hold & Win grid: a top bar, cell dividers and two round sockets.
- **Subject:** A long dark red bar with gold scroll ends, two thin purple divider lines, a gold-rimmed dark socket and the same socket filled with green.
- **Style:** Flat interface furniture with gold trim.
- **Rendering:** Clean vector-like shapes with a bevelled gold rim.
- **Colour:** Near-black red #340811 at 70% with gold #d0a621 and #fefd67; the filled socket is bright green.
- **Lighting:** Top-lit gold rims (measured: top).
- **Ambience:** Sober; it frames the balls and adds nothing itself.
- **Materials:** Gold metal, dark lacquer, green glass.
- **Variants:** The socket comes empty and filled: a counter of collected money balls (inference from the pair).
- **Motion:** None in the sheet.
- **Construction:** 5 sprites in a TexturePacker sheet; the dividers are 1571x15 and 21x943.
- **Notes:** Not seen in play.
- **Measured:** dark, vivid, warm, high contrast · brightness 22% · saturation 93% · contrast 72% · warm 76% / cool 22% · brighter towards: top (3)
- **Palette (measured):** #340811 black 70%, #93510a brown 10%, #d0a621 gold 10%, #fefd67 gold 4%

### Bonus spins reel backing

`403363884f0202977094baecccc2c8b15bbe14a502e2Reel--FS--Background-jpg` · atlas · 1 parts · largest 1567×907 · sheet `sheets/403363884f0202977094baecccc2c8b15bbe14a502e2Reel--FS--Background-jpg.webp`

- **Role:** The surface behind the reels during the bonus spins.
- **Subject:** The same five columns in gold, pressed with the wave-scale pattern, shading to brown at each column's edges.
- **Style:** Patterned graded surface.
- **Rendering:** Gradient with an embossed pattern.
- **Colour:** Brown #983c05 43%, gold-orange #f1b108 33%, orange #d17807 22%; warm 1.0, brightness 0.475.
- **Lighting:** Each column lit along its centre.
- **Ambience:** Rich: the board itself turns to gold for the feature.
- **Materials:** Embossed gold leaf (inference).
- **Variants:** The feature counterpart of the purple backing.
- **Motion:** None.
- **Construction:** A single 1567x907 JPEG.
- **Notes:** The feature is told by swapping one surface from the game's darkest colour to its brightest.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 48% · saturation 97% · contrast 56% · warm 100% / cool 0%
- **Palette (measured):** #983c05 brown 43%, #f1b108 orange 33%, #d17807 orange 22%, #4e0f02 dark red 2%

### Hold & Win blank cell

`403366a53f7fbab67db96b9a95b64e9b329c19e95d57HW--Reel--Blank--Image-jpg` · atlas · 1 parts · largest 299×303 · sheet `sheets/403366a53f7fbab67db96b9a95b64e9b329c19e95d57HW--Reel--Blank--Image-jpg.webp`

- **Role:** A blank picture for an empty cell of the Hold & Win grid.
- **Subject:** A flat grey square.
- **Style:** No art: a technical blank.
- **Rendering:** Flat fill.
- **Colour:** One grey, #8b8b8b at 100%.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** One.
- **Motion:** None.
- **Construction:** A 299x303 JPEG, the size of one cell.
- **Notes:** It gives the cell size: about 299x303 at this pack's scale. How the game tints or hides it was not seen.
- **Measured:** mid-tone, muted, neutral, low contrast, hard-edged · brightness 55% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #8b8b8b grey 100%

### Base game reel backing

`4033aa50488a2fbfdaa32554c05b121b5004969e1662Reel--Main--Background-jpg` · atlas · 1 parts · largest 1567×907 · sheet `sheets/4033aa50488a2fbfdaa32554c05b121b5004969e1662Reel--Main--Background-jpg.webp`

- **Role:** The surface behind the five reels in the base game.
- **Subject:** Five vertical purple columns, each lighter in its middle and near black at its edges, like five rounded drums or hanging silk panels.
- **Style:** Plain graded surface.
- **Rendering:** Smooth gradient with a faint brushed grain.
- **Colour:** Dark purple #3d0156 at 88% and near-black #1c0127 at 12%; brightness 0.074, contrast 0.07, cool 1.0.
- **Lighting:** Each column lit along its centre line.
- **Ambience:** Dark and deep, so that gold symbols stand out.
- **Materials:** Silk or brushed lacquer (inference).
- **Variants:** One picture; the bonus spins use the gold backing instead.
- **Motion:** None.
- **Construction:** A single 1567x907 JPEG covering 5 columns.
- **Notes:** The darkest surface of the game: the purple royals read on it only because each letter carries a gold edge and a magenta glow.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 7% · saturation 98% · contrast 7% · warm 0% / cool 100%
- **Palette (measured):** #3d0156 dark purple 88%, #1c0127 black 12%

### Money Gong Bonus wheel parts

`BonusRespinWheel1` · atlas · 16 parts · largest 1274×995 · sheet `sheets/BonusRespinWheel1.webp`

- **Role:** The round scene of the Money Gong Bonus.
- **Subject:** A dark red disc wreathed in gold cloud scrolls, a filler disc with a gold glow, the gold fret coin as centre, a gold Greek-key ring, a glossy orange panel pill, a round purple reel backing and eight gold scroll ornaments for the eight directions.
- **Style:** Glossy ornament, the same manner as the gong.
- **Rendering:** Airbrushed gold with soft drop shadows.
- **Colour:** Dark red #490a01 at 46% with gold #efb910 17% and brown-gold #9f5b0a 16%; a little purple (3%) from the reel backing.
- **Lighting:** Top-lit (measured on 7 parts).
- **Ambience:** Ceremonial; a feast of gold cloud.
- **Materials:** Gold, red lacquer.
- **Variants:** Eight ornaments, one per position; one round purple cell backing (228x228).
- **Motion:** Moved by the BonusRespinWheel skeleton: WheelAppear, WheelIdle, PanelIn, PanelCollide, GongAppear by name.
- **Construction:** 16 sprites; the cloud ground is the largest at 1274x995.
- **Notes:** Not seen in play. The cell backing is purple here, where the rest of the wheel keeps the sister game's red.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 32% · saturation 92% · contrast 68% · warm 97% / cool 3% · brighter towards: top (7), top-left (2), top-right (1)
- **Palette (measured):** #490a01 dark red 46%, #efb910 gold 17%, #9f5b0a brown 16%, #cc8f14 orange 6%, #090103 black 5%

### Firecrackers around the gong

`FireCracker` · atlas · 4 parts · largest 100×149 · sheet `sheets/FireCracker.webp`

- **Role:** The meter of the Hold & Win trigger: firecrackers that are lit one by one.
- **Subject:** A fat red firecracker with a gold character on a gold diamond label and gold coin marks, a small wick, a puff of smoke and a ground shadow.
- **Style:** Toy-like glossy object.
- **Rendering:** Smooth gradients, a gold printed label, a soft grey smoke puff.
- **Colour:** Red #f61124 at 49% with gold #fade80 13%; the rest is the grey of the smoke.
- **Lighting:** Soft light from the upper left on the cylinder (read from the sheet).
- **Ambience:** Festive: New Year.
- **Materials:** Printed paper and a twisted wick.
- **Variants:** By the animation names three small crackers and a big one, each with Static, Idle, IdleStart, WinActivate and Win.
- **Motion:** 24 animations: a cracker stands, is lit, smokes and goes off (inference from the names); the fireworks themselves are in FireCracker1.
- **Construction:** A Spine 4.0 skeleton of 53 bones and 45 slots over only 4 pictures (the cracker is 100x149).
- **Notes:** One small picture reused many times makes the whole ring.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 53 bones · 45 slots · animations: Idle1 (0 s), Idle2 (0 s), Idle3 (0 s), IdleBig (0 s), IdleStart1 (0 s), IdleStart2 (0 s), IdleStart3 (0 s), IdleStartBig (0 s), IdleStartBigSmoke (0 s), IdleStartSmoke1 (0 s), IdleStartSmoke2 (0 s), IdleStartSmoke3 (0 s), Static1 (0 s), Static2 (0 s), Static3 (0 s), StaticBig (0 s), Win1 (0 s), Win2 (0 s), Win3 (0 s), WinActivate1 (0 s), WinActivate2 (0 s), WinActivate3 (0 s), WinActivateBig (0 s), WinBig (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 39% · saturation 71% · contrast 63% · warm 99% / cool 1% · brighter towards: bottom-right (1)
- **Palette (measured):** #f61124 red 49%, #fade80 gold 13%, #8c8a87 grey 6%, #0f0604 black 6%, #524d46 grey 4%

### The Money Gong and its feature faces

`Gong` · atlas · 20 parts · largest 905×907 · sheet `sheets/Gong.webp`

- **Role:** The feature device at the left of the board: the gong that awards a feature.
- **Subject:** A large round gold gong with a red openwork emblem (a symmetric fret knot); a gold ring with a Greek-key band; four coloured outline rings; and feature faces of the same disc: green REPEAT PAYS, blue PRIZE BOOST, purple MULTIPLIER, red VORTEX PAYS and red-gold MONEY GONG BONUS, plus a small blue gong, a PRIZE BOOST wordmark and a dark red YOU WIN bar with gold scroll ends.
- **Style:** Glossy 3D-looking emblem art: a coin or medal, not an instrument on a stand.
- **Rendering:** Smooth airbrushed bevels, a bright top highlight on the gold, lettering with a white outline and a dark extrusion.
- **Colour:** Gold and red with one colour per feature: #fdf641, #f6a511, dark red #610e07, and blue #052c67 among the leading colours; brightness 0.54, contrast 0.81.
- **Lighting:** Lit from the top (measured on 8 parts) with a hot upper rim.
- **Ambience:** Ceremonial; the biggest gold object of the screen.
- **Materials:** Polished gold, red enamel, coloured enamel for the feature faces.
- **Variants:** Six faces of one disc and four outline rings: the feature is told by colour first and by the word second. The intro panel names Multiplier, Vortex Pays, Prize Boost and Money Gong Bonus, so the green REPEAT PAYS face is probably left from the sister game (inference).
- **Motion:** 35 animations by name, among them Idle1, Idle2, AnticipationIn/Loop/Out, FeatureRotate, RotationStop, Collide, TriggerSplash and YouWinIn/Loop: the gong turns like a coin to a feature face (SideRound and SideStraight are its edge) and is struck (inference from the names; no frame was drawn).
- **Construction:** A Spine 4.0 skeleton of 44 bones and 46 slots; the plain gong is 905x907, the feature faces about 343x343.
- **Notes:** Unchanged from Money Gong Emperor in shape and colour: the gong stays red and gold on the purple game.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 44 bones · 46 slots · animations: AnticipationIn (0 s), AnticipationLoop (0 s), AnticipationOut (0 s), Appear (0 s), Collide (0 s), FakeWinRotate (0 s), FeatureDimIn (0 s), FeatureDimOut (0 s), FeatureOut (0 s), FeatureParticleBack (0 s), FeatureRotate (0 s), FrameFeatureAppear (0 s), FrameFeatureDisappear (0 s), FrameFeatureRotate (0 s), FrameIdle1 (0 s), FrameIdle2 (0 s), FrameReleaseRotation (0 s), FrameRepeatPaysRotation (0 s), GongFeatureTriggerLandscape (0 s), GongFeatureTriggerPortrait (0 s), Idle1 (0 s), Idle2 (0 s), RaysIdle (0 s), ReleaseRotation (0 s), RespinsTransition (0 s), RotationStop (0 s), ScaleIn (0 s), ScaleLoop (0 s), ScaleOut (0 s), TriggerSplash (0 s), YouWinCollide (0 s), YouWinIn (0 s), YouWinLoop (0 s), YouWinOutLandscape (0 s), YouWinOutPortrait (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 54% · saturation 78% · contrast 81% · warm 74% / cool 21% · brighter towards: top (8)
- **Palette (measured):** #610e07 dark red 15%, #fdf641 gold 14%, #f6a511 orange 13%, #fbf9b2 light gold 7%, #e24f15 orange 5%, #052c67 dark blue 3%

### Gold pots of the bonus spins

`Pot` · atlas · 29 parts · largest 417×316 · sheet `sheets/Pot.webp`

- **Role:** The two pots under the board that hold the bonus spins awards (6 and 12).
- **Subject:** A round gold pot heaped with coins and ingots, loose heaps of coins, two oval brown plaques with gold scroll rims reading 6 and 12, a BONUS SPINS strip in white on dark red, a square-holed coin turning, and a small ingot.
- **Style:** Glossy stylised objects.
- **Rendering:** Airbrushed gold with strong highlights and engraved texture on the pot's collar.
- **Colour:** Gold and brown: #f4c513 36%, #892d04 20%, #e07a0a 12%; warm 1.0, brightness 0.60.
- **Lighting:** Top-lit (measured), with hot highlights on the rim.
- **Ambience:** Abundant, lucky.
- **Materials:** Polished and hammered gold, brown lacquer plaques.
- **Variants:** Two plaques (6, 12), three sizes of coin heap (Coins x4), a 20-frame turning coin.
- **Motion:** 10 animations by name: Idle1 to 3, Grow1, Grow2, Collide1 to 3, Win, WinIdle: the pot grows as coins hit it (inference from the names).
- **Construction:** A Spine 4.0 skeleton of 111 bones and 125 slots over 29 sprites; the pot is 417x316.
- **Notes:** The same pot appears again in the Bonus Buy panel.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 111 bones · 125 slots · animations: Collide1 (0 s), Collide2 (0 s), Collide3 (0 s), Grow1 (0 s), Grow2 (0 s), Idle1 (0 s), Idle2 (0 s), Idle3 (0 s), Win (0 s), WinIdle (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 60% · saturation 85% · contrast 67% · warm 100% / cool 0% · brighter towards: top (3)
- **Palette (measured):** #f4c513 gold 36%, #892d04 brown 20%, #e07a0a orange 12%, #f9df5b gold 9%, #be5908 orange 6%, #fbe998 light gold 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Reel symbols, sharp and blurred (sheet 1)

`Main.desktop1` · atlas · 40 parts · largest 440×394 · sheet `sheets/Main.desktop1.webp`

- **Role:** The still pictures the reels show while turning and stopping.
- **Subject:** The empress in a gold square frame, sharp and motion-blurred; BONUS SPINS, WILD, the money ball and the four jackpot balls, each sharp or blurred; purple royals 10, J, Q, K and A; the koi; square-holed gold coins at several turns; the multipliers x2, x5 and x8 in red with white outline; a magenta dollar sign; the figures 2, 4, 3 of 243.
- **Style:** Glossy stylised symbols; one painted portrait.
- **Rendering:** Hard silhouettes with gold rims; the blurred copies are smeared vertically.
- **Colour:** Gold-orange #e39f2b 19%, gold #fbe350 10%, magenta #950aa8 9%, green #0ce260 5%; saturation 0.77.
- **Lighting:** From the top (measured on 20 parts).
- **Ambience:** Bright and legible.
- **Materials:** Gold, glass, lacquer.
- **Variants:** Every reel symbol ships twice: sharp and pre-blurred.
- **Motion:** None in the sheet; the blur is drawn, not computed.
- **Construction:** 40 sprites in a TexturePacker sheet with hashed names; the empress is 440x394, a royal about 334x290.
- **Notes:** The empress in her square frame is the only reel symbol that is a picture of a person.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 50% · saturation 77% · contrast 57% · warm 72% / cool 14% · brighter towards: top (20), top-left (5), top-right (4)
- **Palette (measured):** #e39f2b orange 19%, #7b4314 brown 11%, #fbe350 gold 10%, #950aa8 magenta 9%, #0ce260 green 5%, #d915e2 magenta 4%

### Reel symbols, balls, coins and value figures (sheet 2)

`Main.desktop2` · atlas · 95 parts · largest 314×332 · sheet `sheets/Main.desktop2.webp`

- **Role:** More reel stills and the figures written on the balls.
- **Subject:** WILD, MONEY GONG BONUS, a gold ball, and the four jackpot balls in a gold and in a green version (MAJOR, MAXI, MINI, MINOR); the fan, the lotus blurred, the koi blurred, the turtle; a gold square-holed coin in about twenty turns; faint purple fret watermarks; magenta figures 0 to 9 with currency signs, a gold-edged set, and x3.
- **Style:** Glossy stylised objects.
- **Rendering:** Airbrushed, hard-edged (soft edge 0.11), strong highlights.
- **Colour:** Gold #f6d836 30%, orange #d99c23 13%, green #06e85c 6%, magenta #b00a98 3%; brightness 0.60.
- **Lighting:** Top (45 parts) and top-right (17), measured.
- **Ambience:** Rich; a table of treasure.
- **Materials:** Gold, jade, glass.
- **Variants:** Each jackpot ball comes on gold and on green; the coin spin is drawn frame by frame.
- **Motion:** The coin turn is a frame sequence in pictures.
- **Construction:** 95 sprites.
- **Notes:** In the base game screen the balls carry the gold-edged figures and the Money Gong Prize meter the magenta ones.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 60% · saturation 77% · contrast 69% · warm 77% / cool 12% · brighter towards: top (45), top-right (17), left (2)
- **Palette (measured):** #f6d836 gold 30%, #d99c23 orange 13%, #3e0708 dark red 7%, #faea88 light gold 7%, #06e85c green 6%, #f5f8f4 light green 4%

### Blue page: Prize Boost coin, koi symbol, Minor ball

`AllSymbols1` · atlas · 6 parts · largest 290×302 · sheet `sheets/AllSymbols1.webp`

- **Role:** Symbol parts that share blue.
- **Subject:** A blue fret coin in a blue glowing ring, the koi symbol (a gold carp leaping on a royal blue plate with scalloped corners), the pale blue-white Minor ball with the fret emblem pressed in, the MINOR wordmark, and two shadows.
- **Style:** Glossy stylised objects on coloured plates.
- **Rendering:** Airbrushed gold with white glints on the koi; the ball is frosted glass with an embossed emblem.
- **Colour:** Blue: light #cceafc 18%, dark #07278b 16%, #1c84c4 13%; the gold of the koi is the only warm part.
- **Lighting:** From the top left (measured).
- **Ambience:** Cool and precious.
- **Materials:** Gold, blue enamel, frosted glass.
- **Variants:** The koi is symbol s8.
- **Motion:** Moved by the AllSymbols skeleton (Symbol8Win; PrizeBoostApply for the coin, by name).
- **Construction:** 6 sprites; the symbol is 233x227, the coin 290x302.
- **Notes:** A page per colour is how this atlas is packed; the tags are not the game's logic.
- **Measured:** mid-tone, vivid, cool, high contrast, strong highlights · brightness 48% · saturation 68% · contrast 60% · warm 19% / cool 76% · brighter towards: top-left (1)
- **Palette (measured):** #cceafc light blue 18%, #07278b dark blue 16%, #0d021a black 15%, #1c84c4 blue 13%, #31b4e6 cyan 7%, #76d4f5 cyan 5%

### Green page: money ball, Major ball, fan symbol, green coin

`AllSymbols2` · atlas · 6 parts · largest 290×302 · sheet `sheets/AllSymbols2.webp`

- **Role:** The money ball and the parts that share green.
- **Subject:** The green money ball (a glossy jade ball with the fret emblem pressed in and a white highlight) in two near-identical versions, a green fret coin in a ring, the fan symbol (a gold folding fan with a small gold lamp on a teal disc), a darker green Major ball and the MAJOR wordmark.
- **Style:** Glossy stylised objects.
- **Rendering:** A glass ball with a sharp specular window and an embossed emblem; the fan is airbrushed gold with printed pattern.
- **Colour:** Green: #04ed61 31%, dark #128b07 18%; the fan brings gold and teal.
- **Lighting:** Top and top-left (measured).
- **Ambience:** Lucky; jade.
- **Materials:** Jade or glass, gold paper, enamel.
- **Variants:** bonus_moneyball and moneyball green; the fan is symbol s6.
- **Motion:** Moved by the AllSymbols skeleton (MoneyBallLand1 to 4, MoneyBallWin, Symbol6Win by name).
- **Construction:** 6 sprites; the ball is 242x250.
- **Notes:** The green ball is the one saturated cool colour that recurs on every screen: it is the thing to collect.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 60% · saturation 85% · contrast 56% · warm 14% / cool 47% · brighter towards: top (2), top-left (1)
- **Palette (measured):** #04ed61 green 31%, #128b07 dark green 18%, #41d417 green 6%, #0c1607 black 5%, #1ef5a2 green 4%, #0b4c18 dark green 4%

### Gold and red page: wild, bonus spins, turtle, gold ball, Mini ball, empress parts

`AllSymbols3` · atlas · 26 parts · largest 319×923 · sheet `sheets/AllSymbols3.webp`

- **Role:** The warm-coloured symbol parts and several parts of the expanding empress.
- **Subject:** The wild's base (a pink-red fret medallion in a gold scalloped frame) and its WILD wordmark; the bonus spins plate (an orange disc in a gold scalloped ring) and its BONUS SPINS wordmark; the turtle symbol (a gold dragon turtle on a red plate); a gold money ball; the orange Mini ball and MINI wordmark; the MONEY GONG BONUS wordmark; a red fret coin; and of the empress: two gold frames (319x923 and 516x516), her hair, a hand holding a gold ornament with bead chains, and a fan.
- **Style:** Glossy stylised objects; the empress parts are painted realistically.
- **Rendering:** Airbrushed gold with glints; the hair and hand are painted with soft brushwork.
- **Colour:** Gold #f4c51b 20%, brown-gold #a9530e 20%, dark red #711408 8%, red #be1707 4%; warm 1.0.
- **Lighting:** Top-lit (measured on 9 parts).
- **Ambience:** Rich and warm.
- **Materials:** Gold, red enamel, hair, beads.
- **Variants:** The turtle is symbol s9. The empress frame comes 1x1 and three cells tall: the top symbol can cover a reel (Symbol10ExpandedAppear by name).
- **Motion:** Empress-Gold is a 4-frame sequence of the swinging bead chains; the rest is moved by the AllSymbols skeleton.
- **Construction:** 26 sprites.
- **Notes:** The wordmarks are separate sprites over their plates, so the plate can spin or glow under a still word.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 50% · saturation 81% · contrast 65% · warm 100% / cool 0% · brighter towards: top (9), bottom-right (1), bottom-left (1)
- **Palette (measured):** #f4c51b gold 20%, #a9530e brown 20%, #2a0804 black 13%, #fbeb5d gold 9%, #711408 dark red 8%, #e67f15 orange 7%

### Purple page: empress body and head, royals, lotus, Maxi ball, purple coin

`AllSymbols4` · atlas · 13 parts · largest 516×661 · sheet `sheets/AllSymbols4.webp`

- **Role:** The top symbol's main parts and the parts that share purple.
- **Subject:** The empress: a smiling young woman with an elaborate black updo, gold phoenix hairpins and red flowers (head 485x447), a body in a purple brocade robe with gold-edged black collar (516x661), a wide sleeve and a fan shadow. Also the royals 10 and K as fat glossy purple letters with a gold edge and a magenta glow, the lotus symbol (a gold lotus on a purple plate), a purple Maxi ball, the MAXI wordmark and a purple fret coin.
- **Style:** Two manners: the empress is a realistic painted figure, everything else is glossy and toy-like.
- **Rendering:** The figure is painted with soft skin and sharp jewellery; the letters are smooth 3D-looking shapes with a top highlight.
- **Colour:** Magenta and purple: #36092d 37%, #980ba9 11%, #e611ea 4%; skin and red flowers bring #af3a54.
- **Lighting:** Top-lit (measured on 6 parts).
- **Ambience:** Elegant and warm; the face looks at the player.
- **Materials:** Brocade, gold jewellery, skin, lacquered letters.
- **Variants:** s1 (10) and s4 (K) are here with 6-frame sequences; the lotus is s7. The other royals are in the sheets Main.desktop1 and 2.
- **Motion:** By name: Symbol1Win to Symbol10Win, Symbol10ExpandedAppear and Symbol10ExpandedWin; the empress is rigged from head, body, sleeve, hair, hand, fan and bead chains.
- **Construction:** 13 sprites; the empress is built for a frame three cells tall.
- **Notes:** The royals are purple on a purple board: the sister game's are red on red. Each game dyes its cheapest symbols in its own ground colour and keeps gold for the paying ones.
- **Measured:** dark, vivid, warm and cool mixed, high contrast · brightness 26% · saturation 80% · contrast 68% · warm 61% / cool 15% · brighter towards: top (6), top-right (1), bottom (1)
- **Palette (measured):** #36092d dark magenta 37%, #980ba9 magenta 11%, #af3a54 red 10%, #090303 black 5%, #e611ea magenta 4%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The empress of the pop-ups

`PopUps` · atlas · 15 parts · largest 847×629 · sheet `sheets/PopUps.webp`

- **Role:** The host who appears with a scroll to announce a feature or a result.
- **Subject:** A smiling young woman seen from the chest up: a black updo with gold phoenix pins, red flowers and tassels, a jewel on her forehead; a purple brocade robe with a black and gold collar; long hair flying behind; two wide sleeves seen from the front; four strands of gold beads; and a purple scroll with gold rollers held open in front of her.
- **Style:** A realistic painted figure, the one character of the game.
- **Rendering:** Soft painted skin, sharp gold jewellery, patterned cloth; hard-edged overall (soft edge 0.05).
- **Colour:** Purple and magenta with skin and gold: #8a04a6 20%, #630867 17%, skin #dc8451 and #f8c48f, gold #f4d32c 3%, on near-black #27080e.
- **Lighting:** From the top right (measured on 3 parts), warm on the face.
- **Ambience:** Warm, welcoming, a little theatrical.
- **Materials:** Brocade silk, gold metalwork, beads, paper scroll.
- **Variants:** One pose; landscape and portrait placements by name.
- **Motion:** Six animations by name (PopUp in, loop and out for landscape and portrait). The eyes are separate (two scleras, two irises), so she blinks or looks (inference); the bead strands and the back hair are separate, so they swing (inference).
- **Construction:** A Spine 4.0 skeleton of 38 bones and 37 slots over 15 pictures; the body is 847x629, the head 572x457, the scroll 985x510.
- **Notes:** The largest art of the game. Not seen in play.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 38 bones · 37 slots · animations: PopUpLandscapeIn (0 s), PopUpLandscapeLoop (0 s), PopUpLandscapeOut (0 s), PopUpPortraitIn (0 s), PopUpPortraitLoop (0 s), PopUpPortraitOut (0 s)
- **Measured:** dark, vivid, warm and cool mixed, high contrast, hard-edged · brightness 24% · saturation 84% · contrast 66% · warm 62% / cool 27% · brighter towards: top-right (3), bottom-right (1), bottom-left (1)
- **Palette (measured):** #27080e black 26%, #8a04a6 purple 20%, #630867 dark magenta 17%, #994519 brown 8%, #dc8451 orange 6%, #53122e dark magenta 6%


## Logo and title

The game's own wordmark.

### Animated logo of the intro

`Intro` · atlas · 11 parts · largest 742×743 · sheet `sheets/Intro.webp`

- **Role:** The title as it assembles on the intro and preloader.
- **Subject:** A gold coin with the red fret emblem, the words MONEY and GONG as separate bevelled gold pieces, a red backing of both words, EMPRESS in smaller gold capitals, gold cloud scrolls behind and in front, and a small coin turning.
- **Style:** Heavy angular faux-brush capitals, glossy 3D-looking.
- **Rendering:** Bevelled gold with white glints and a deep red extrusion.
- **Colour:** Gold and red: #fbe95c 25%, dark red #7b110a 16%, #eba636 15%; warm 1.0.
- **Lighting:** Top-lit (measured on 4 parts).
- **Ambience:** Festive and rich.
- **Materials:** Polished gold, red lacquer.
- **Variants:** The words are separate, so the logo can build word by word.
- **Motion:** Two animations by name, IntroLandscape and IntroPortrait; a 4-frame coin.
- **Construction:** A Spine 4.0 skeleton of 57 bones and 54 slots over 11 pictures; the coin is 742x743.
- **Notes:** The logo is the sister game's with one word changed: the family is the brand, the last word the game.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 57 bones · 54 slots · animations: IntroLandscape (0 s), IntroPortrait (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 58% · saturation 70% · contrast 71% · warm 100% / cool 0% · brighter towards: top (4), bottom-left (1)
- **Palette (measured):** #fbe95c gold 25%, #7b110a dark red 16%, #eba636 orange 15%, #fdf9b6 light gold 12%, #bf772c orange 11%, #93481e brown 8%

### In-game logo skeleton (base picture)

`Logo` · atlas · 1 parts · largest 337×58 · sheet `sheets/Logo.webp`

- **Role:** The small logo at the top left of the base game.
- **Subject:** The words MONEY GONG as a dark red and grey mask: the under-layer of the logo, not the finished lettering.
- **Style:** Faux-brush capitals.
- **Rendering:** A flat mask with a red inner glow.
- **Colour:** Dark red #570c03 50%, #941204 21%.
- **Lighting:** None of its own.
- **Ambience:** None alone.
- **Materials:** None.
- **Variants:** One.
- **Motion:** One animation by name, Win: the logo reacts to a win.
- **Construction:** A Spine 4.0 skeleton of 29 bones and 29 slots; this page holds one 337x58 picture, the finished logo is in FeatureScreen.desktop (540x171).
- **Notes:** Read with Logo1, which holds its lights.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 29 bones · 29 slots · animations: Win (0 s)
- **Measured:** dark, vivid, warm, medium contrast · brightness 20% · saturation 91% · contrast 43% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #570c03 dark red 50%, #941204 dark red 21%, #cd6c25 orange 9%, #7c4d2a brown 8%, #cc1b06 red 7%, #c44112 orange 2%

### Logo lights

`Logo1` · atlas · 5 parts · largest 352×221 · sheet `sheets/Logo1.webp`

- **Role:** The effects of the in-game logo.
- **Subject:** A field of white sparks, a yellow glow in the shape of the logo, a cone of rays, a gold four-point star and a white wipe bar.
- **Style:** Light on black.
- **Rendering:** Soft additive shapes.
- **Colour:** Greys with gold #f9f372 and #f7e724.
- **Lighting:** They are the light.
- **Ambience:** Sparkle.
- **Materials:** Light.
- **Variants:** Five parts.
- **Motion:** Played by the Logo skeleton's Win (inference).
- **Construction:** 5 sprites on a JPEG page.
- **Notes:** The glow is cut to the logo's own outline.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 43% · saturation 29% · contrast 44% · warm 40% / cool 0%
- **Palette (measured):** #494542 grey 22%, #191614 black 21%, #767574 grey 16%, #a5a3a0 grey 7%, #f9f372 gold 6%, #f7e724 gold 6%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Intro panel pictures

`FeatureScreen` · atlas · 15 parts · largest 664×646 · sheet `sheets/FeatureScreen.webp`

- **Role:** The pictures of the intro panel that explains the three ways into the features.
- **Subject:** The gold gong with its red-gold emblem, the MONEY GONG BONUS wordmark alone and on a green ball, the green money ball, three firecrackers at different angles, and the three feature words MULTIPLIER (pink-violet), VORTEX PAYS (red) and PRIZE BOOST (blue) in rounded poster capitals, with two red shadows.
- **Style:** Glossy objects and poster wordmarks.
- **Rendering:** Airbrushed, with white outlines and dark extrusions on the words.
- **Colour:** Dark red #661004 21%, gold #ecd231 15%, green #08ec63 6%, red #e60608 4%.
- **Lighting:** Top (3 parts) and left (measured).
- **Ambience:** Explanatory but festive.
- **Materials:** Gold, glass, paper.
- **Variants:** Three panels by the animation names Feature1, Feature2, Feature3.
- **Motion:** Firecracker is a 6-frame sequence; the skeleton is large (98 bones, 120 slots).
- **Construction:** 15 pictures; the gong is 664x646.
- **Notes:** VORTEX PAYS is this game's own feature word; the sister game's panel reads REPEAT PAYS.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 98 bones · 120 slots · animations: Feature1 (0 s), Feature2 (0 s), Feature3 (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 49% · saturation 80% · contrast 76% · warm 84% / cool 12% · brighter towards: top (3), bottom-left (2), left (2)
- **Palette (measured):** #661004 dark red 21%, #ecd231 gold 15%, #f1e58c gold 9%, #d3620e orange 9%, #97430e brown 8%, #08ec63 green 6%

### Jackpot meter sparkle trails (uncut page)

`JackpotPanel` · atlas · 1 parts · largest 1709×1020 · sheet `sheets/JackpotPanel.webp`

- **Role:** The sparkle that runs round a jackpot meter when it is idle or won.
- **Subject:** A page of about twenty frames of a pill-shaped ring of pale gold sparks, with one grey gradient bar and a small gold star.
- **Style:** Light on black.
- **Rendering:** Fine sparks.
- **Colour:** Pale yellow-grey on black: #55563d 51%, #1a1a12 26%; hues 100% yellow.
- **Lighting:** They are the light.
- **Ambience:** A quiet shimmer.
- **Materials:** Light.
- **Variants:** One trail, many frames.
- **Motion:** 28 animations by name: Idle, TrailPath, WinIn, WinLoop and WinOut for Grand, Major, Maxi, Mini and Minor, and three for the Money Gong prize.
- **Construction:** A Spine 4.0 skeleton of 18 bones and 35 slots. The atlas is in the newer Spine text format, which the reader does not cut: the unit is one whole 1709x1020 page.
- **Notes:** The frames are not cut apart, so their count is read from the page, not measured.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 18 bones · 35 slots · animations: GrandIdle (0 s), GrandTrailPath (0 s), GrandWinIn (0 s), GrandWinLoop (0 s), GrandWinOut (0 s), MajorIdle (0 s), MajorTrailPath (0 s), MajorWinIn (0 s), MajorWinLoop (0 s), MajorWinOut (0 s), MaxiIdle (0 s), MaxiTrailPath (0 s), MaxiWinIn (0 s), MaxiWinLoop (0 s), MaxiWinOut (0 s), MiniIdle (0 s), MiniTrailPath (0 s), MiniWinIn (0 s), MiniWinLoop (0 s), MiniWinOut (0 s), MinorIdle (0 s), MinorTrailPath (0 s), MinorWinIn (0 s), MinorWinLoop (0 s), MinorWinOut (0 s), MoneyGongIdle (0 s), MoneyGongWinIn (0 s), MoneyGongWinLoop (0 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 32% · saturation 27% · contrast 27% · warm 100% / cool 0%
- **Palette (measured):** #55563d brown 51%, #1a1a12 black 26%, #95967e grey 18%, #85865a yellow 5%

### Multiplier values

`Multiplier` · atlas · 4 parts · largest 145×100 · sheet `sheets/Multiplier.webp`

- **Role:** The multiplier shown when the gong awards one.
- **Subject:** x2, x5 and x8 in fat rounded red figures with a thick white outline and a dark red drop.
- **Style:** Comic poster figures.
- **Rendering:** Flat red with a white keyline.
- **Colour:** Red #f01e0c 55%, white 26%, dark red #450202 15%; contrast 0.94.
- **Lighting:** Top-lit by a faint highlight (measured: top).
- **Ambience:** Punchy.
- **Materials:** None.
- **Variants:** Three values here; the paytable sheet also holds x3, x4, x10 and x25.
- **Motion:** Two animations by name, Appear and Static; each value is a 4-frame sequence.
- **Construction:** A Spine 4.0 skeleton of 3 bones and 2 slots.
- **Notes:** Red on white is the highest contrast in the package: it must read over anything.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 3 bones · 2 slots · animations: Appear (0 s), Static (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 45% · saturation 68% · contrast 94% · warm 100% / cool 0% · brighter towards: top (4)
- **Palette (measured):** #f01e0c red 55%, #fffdfd light red 26%, #450202 dark red 15%

### Win tier titles

`SpecialMessages` · atlas · 8 parts · largest 901×119 · sheet `sheets/SpecialMessages.webp`

- **Role:** The titles of the four win tiers.
- **Subject:** BIG WIN, HUGE WIN, MASSIVE WIN and SPECTACULAR in plain condensed sans capitals, yellow gold with a darker edge, each also in a blurred half-size copy.
- **Style:** Plain poster lettering, outside the faux-brush manner of the game's own words.
- **Rendering:** Flat yellow with a soft dark edge.
- **Colour:** Yellow gold only: #c8ad0b 40%, #f4e47f 17%; hues 98% yellow.
- **Lighting:** None of its own; the glows are in SpecialMessages1.
- **Ambience:** Loud by size and motion rather than by drawing.
- **Materials:** None.
- **Variants:** Four titles, sharp and blurred.
- **Motion:** 21 animations by name: each tier comes in, loops and leaves, with two ambient layers and a reel ambient.
- **Construction:** A Spine 4.0 skeleton of 209 bones and 130 slots, the heaviest rig of the game, over 8 pictures of 901x119.
- **Notes:** The titles are the provider's kit rather than this game's art (inference: the sister game ships the same).
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 209 bones · 130 slots · animations: BigWinIn (0 s), BigWinLoop (0 s), BigWinOut (0 s), HugeWinIn (0 s), HugeWinLoop (0 s), HugeWinOut (0 s), MassiveWinIn (0 s), MassiveWinLoop (0 s), MassiveWinOut (0 s), ReelsAmbientIn (0 s), ReelsAmbientLoop (0 s), ReelsAmbientOut (0 s), SpecialMessagesAmbient1In (0 s), SpecialMessagesAmbient1Loop (0 s), SpecialMessagesAmbient1Out (0 s), SpecialMessagesAmbient2In (0 s), SpecialMessagesAmbient2Loop (0 s), SpecialMessagesAmbient2Out (0 s), SpectacularIn (0 s), SpectacularLoop (0 s), SpectacularOut (0 s)
- **Measured:** bright, vivid, warm, high contrast, strong highlights · brightness 66% · saturation 76% · contrast 65% · warm 100% / cool 0%
- **Palette (measured):** #c8ad0b gold 40%, #f4e47f gold 17%, #d7be54 gold 12%, #7d6e16 brown 10%, #f3d718 gold 8%, #fefae0 light gold 4%

### Win tier lights

`SpecialMessages1` · atlas · 38 parts · largest 819×819 · sheet `sheets/SpecialMessages1.webp`

- **Role:** The lights of the win titles.
- **Subject:** A round field of orange sparks, a cone of yellow rays, a rising orange glow, a dark glow cut to each title, and a 30-frame strip of sparks.
- **Style:** Light on black.
- **Rendering:** Soft additive shapes.
- **Colour:** Brown to gold: #5f3109 32%, #d98e25 12%, #f8db78 11%.
- **Lighting:** They are the light.
- **Ambience:** Warm, fiery.
- **Materials:** Light.
- **Variants:** One glow per title.
- **Motion:** TopParticles is a 30-frame sequence; the rest is moved by the SpecialMessages skeleton.
- **Construction:** 38 sprites on a JPEG page; the spark field is 819x819.
- **Notes:** Each title has its own glow mask: effects are fitted to shapes.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 36% · saturation 80% · contrast 46% · warm 99% / cool 0%
- **Palette (measured):** #5f3109 brown 32%, #1f1105 black 23%, #a8570b brown 13%, #d98e25 orange 12%, #f8db78 gold 11%, #dcb350 orange 4%


## Effects

Frame sequences, glows, particles and transitions.

### Symbol effects, page 1

`AllSymbols-0` · atlas · 133 parts · largest 206×626 · sheet `sheets/AllSymbols-0.webp`

- **Role:** Lights of the symbols and of the empress.
- **Subject:** Gold particle fields, star flares, two red vortex swirls, sparkle bursts, glows for the green, blue and yellow money balls, a ring of fire for the ball, gold trails along a circle, near-miss spark bands, light sweeps cut to the wordmarks, and for the empress a back shine, a head glow, a fan shine and a magenta cloud-pattern strip (Empress-BG, 206x626).
- **Style:** Light on black.
- **Rendering:** Soft additive shapes and frame sequences.
- **Colour:** Black and gold: #120904 30%, #4b2c14 16%, #ebaf18 8%; hues 71% orange, 6% magenta.
- **Lighting:** They are the light.
- **Ambience:** Sparkling, warm.
- **Materials:** Light, fire.
- **Variants:** One glow per ball colour; sweeps per wordmark.
- **Motion:** Frame sequences by name: NearMiss x15, Trail x13, particleBurst x13, particles_antic x17, MoneyBallFireEffect x10, Vortex-Sparkle x11 and x8, Bonus_Spins_Lsweep x20.
- **Construction:** 133 sprites on a JPEG page.
- **Notes:** The vortex swirls are new against the sister game: they belong to Vortex Pays (inference from the name).
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 33% · saturation 61% · contrast 42% · warm 90% / cool 2% · brighter towards: top-left (1)
- **Palette (measured):** #120904 black 30%, #4b2c14 brown 16%, #ebaf18 orange 8%

### Symbol effects, page 2

`AllSymbols-1` · atlas · 128 parts · largest 258×331 · sheet `sheets/AllSymbols-1.webp`

- **Role:** More lights of the symbols and of the empress.
- **Subject:** A greyscale shine of the empress's robe and of her head, a pink glow of her hair, gold rays for the wild, a purple ball shine, a white firework burst, a fireball, spark rings and bursts, gold trails, near-miss bands and light sweeps for the ball and the Money Gong Bonus word.
- **Style:** Light on black; the shines are greyscale copies of the art they light.
- **Rendering:** Soft additive shapes.
- **Colour:** Black, brown and gold: #120906 26%, #513a28 22%, #ebad13 9%.
- **Lighting:** They are the light.
- **Ambience:** Sparkling.
- **Materials:** Light.
- **Variants:** A shine per empress part.
- **Motion:** Frame sequences by name: Trail x17, particleBurst x18, Vortex-Sparkle-1 x20, NearMiss x15, moneyballLSweep x7; three frames are still named emperor_Blick.
- **Construction:** 128 sprites on a JPEG page.
- **Notes:** The name emperor_Blick shows the files were built from the sister game's.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 34% · saturation 59% · contrast 38% · warm 91% / cool 1% · brighter towards: bottom-left (1)
- **Palette (measured):** #120906 black 26%, #513a28 brown 22%, #877260 orange 10%, #ae7811 brown 9%, #ebad13 orange 9%, #76440b brown 7%

### Bonus Buy lights

`BonusBuy1` · atlas · 20 parts · largest 480×654 · sheet `sheets/BonusBuy1.webp`

- **Role:** The lights of the Bonus Buy panel and its button.
- **Subject:** A gold glow in the panel's outline, a button glow in white and in pink, a pot glow, greyscale shines of the pot, red and green scroll ornaments that light up, and glints on the coins.
- **Style:** Light on black; shines cut to their object.
- **Rendering:** Soft additive shapes.
- **Colour:** Orange #eaa201 34% with greys; a little green (7%) and red from the ornaments.
- **Lighting:** They are the light.
- **Ambience:** Tempting.
- **Materials:** Light.
- **Variants:** Ornaments in red and in green, matching the red and green buttons.
- **Motion:** Frame sequences of 3 by name: ButtonOrnament, OrnamentPopup, Pot, Coins.
- **Construction:** 20 sprites on a JPEG page.
- **Notes:** The sister game ships no Bonus Buy.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 54% · saturation 64% · contrast 34% · warm 84% / cool 3%
- **Palette (measured):** #eaa201 orange 34%, #c2bfa9 yellow 15%, #5e573c brown 10%, #141207 black 9%, #948d69 yellow 6%, #57310d brown 4%

### Money Gong Bonus wheel lights

`BonusRespinWheel` · atlas · 44 parts · largest 701×701 · sheet `sheets/BonusRespinWheel.webp`

- **Role:** The lights of the bonus wheel.
- **Subject:** A large star of rays, a ring of yellow-green rays, an orange glow, a ring of gold sparks, an orange panel glow, a bright shine and a yellow ring.
- **Style:** Light on black.
- **Rendering:** Soft additive shapes.
- **Colour:** Black to gold: #140e04 23%, #4f3a0c 21%, #fae811 12%.
- **Lighting:** They are the light.
- **Ambience:** Radiant.
- **Materials:** Light.
- **Variants:** One 38-frame particle ring.
- **Motion:** 10 animations by name on a Spine 4.1.24 skeleton of 100 bones and 117 slots: WheelAppear, WheelIdle, RaysAppear, GongAppear, PanelIn, PanelCollide, CellCollectEffect.
- **Construction:** 44 sprites; the ray star is 701x701.
- **Notes:** Not seen in play.
- **Skeleton (from the file):** Spine 4.1.24 · 100 bones · 117 slots · animations: CellCollectEffect (0 s), GongAppear (0 s), GongIdle (0 s), PanelCollide (0 s), PanelIdle (0 s), PanelIn (0 s), RaysAppear (0 s), RaysIdle (0 s), WheelAppear (0 s), WheelIdle (0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 40% · saturation 78% · contrast 45% · warm 97% / cool 0%
- **Palette (measured):** #140e04 black 23%, #4f3a0c brown 21%, #8b6712 brown 16%, #fae811 gold 12%, #e19c0f orange 8%

### Intro panel lights

`FeatureScreen1` · atlas · 19 parts · largest 177×242 · sheet `sheets/FeatureScreen1.webp`

- **Role:** The lights of the intro panel.
- **Subject:** Greyscale shines of the gong at three turns, white glows and light sweeps cut to the wordmarks, firecracker flames, a spark and a soft glow.
- **Style:** Light on black; masks of the art.
- **Rendering:** Soft additive shapes.
- **Colour:** Greys with a little gold #f6e411 (4%); saturation 0.17.
- **Lighting:** They are the light.
- **Ambience:** Glinting.
- **Materials:** Light, flame.
- **Variants:** A shadow and a sweep per feature word.
- **Motion:** Sequences by name: FirecrackerFlame x5, Gong x3, MoneyGongBonusBlick x3.
- **Construction:** 19 sprites on a JPEG page.
- **Notes:** Greyscale shines are tinted in the engine (inference).
- **Measured:** mid-tone, muted, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 62% · saturation 17% · contrast 37% · warm 62% / cool 0%
- **Palette (measured):** #a1a09c grey 34%, #fcfafa light red 22%, #6e6b66 grey 12%, #413e39 grey 9%, #d7cfcb light orange 6%, #18110c black 5%

### Firecracker smoke and fireworks

`FireCracker1` · atlas · 23 parts · largest 219×240 · sheet `sheets/FireCracker1.webp`

- **Role:** What a firecracker gives off when it is lit and goes off.
- **Subject:** Grey smoke and fog puffs, a white glow in the cracker's shape, a 16-frame firework burst of violet-white streaks with gold tips, a spark and a fuse light.
- **Style:** Light and smoke on black.
- **Rendering:** Soft shapes; fine streaks in the burst.
- **Colour:** Greys with violet: #a09297 19%, #5d4954 15%, #362130 6%; hues 42% magenta.
- **Lighting:** They are the light.
- **Ambience:** A small celebration each time.
- **Materials:** Smoke, sparks.
- **Variants:** One burst sequence.
- **Motion:** fireworks2 is a 16-frame sequence.
- **Construction:** 23 sprites on a JPEG page.
- **Notes:** The burst is tinted violet, toward the game's ground colour.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 38% · saturation 28% · contrast 42% · warm 31% / cool 10%
- **Palette (measured):** #0b070c black 34%, #a09297 grey 19%, #5d4954 grey 15%, #f6edee light red 13%, #362130 dark magenta 6%, #debbbf light red 5%

### Gong effects, page 1

`Gong1-0` · atlas · 64 parts · largest 420×336 · sheet `sheets/Gong1-0.webp`

- **Role:** Bursts and splashes of the gong.
- **Subject:** White blob bursts, rings of white splash, small gold particle fields, flat star streaks for YOU WIN, a ring of dots and an orange fireball.
- **Style:** Greyscale light on black.
- **Rendering:** Soft blobs and sparks.
- **Colour:** Grey: #201f1e 30%, #faf9fa 21%; saturation 0.05.
- **Lighting:** They are the light.
- **Ambience:** Impact.
- **Materials:** Light.
- **Variants:** Greyscale, so that one set can be tinted for each feature colour (inference).
- **Motion:** Sequences by name: Burst x17, YouWinFX x30, FeatureFX x6, Particles x6, Splash x3.
- **Construction:** 64 sprites on a JPEG page.
- **Notes:** The same construction as the sister game's gong effects.
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 50% · saturation 4% · contrast 52% · warm 10% / cool 0%
- **Palette (measured):** #201f1e grey 30%, #faf9fa white 21%, #585653 grey 18%, #bfbfbe grey 14%, #888682 grey 14%

### Gong effects, page 2

`Gong1-1` · atlas · 64 parts · largest 266×279 · sheet `sheets/Gong1-1.webp`

- **Role:** More bursts and splashes of the gong.
- **Subject:** More white bursts and splash rings, gold particle fields, a star of rays and a white mask of the fret emblem.
- **Style:** Greyscale light on black.
- **Rendering:** Soft blobs and sparks.
- **Colour:** Grey with a little warm: #c0bfbe 20%, #171511 19%, #d1af7a 5%.
- **Lighting:** They are the light.
- **Ambience:** Impact.
- **Materials:** Light.
- **Variants:** The emblem mask is named Green: a flash laid on the gong's face.
- **Motion:** Sequences by name: Particles x23, FeatureFX x18, Splash x15, Burst x6.
- **Construction:** 64 sprites on a JPEG page.
- **Notes:** Read with page 1.
- **Measured:** mid-tone, muted, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 51% · saturation 17% · contrast 52% · warm 39% / cool 0%
- **Palette (measured):** #c0bfbe grey 20%, #171511 black 19%, #695f4f brown 16%, #f8f8f8 white 14%, #928c82 grey 13%, #433828 brown 11%

### Intro logo lights and ground

`Intro1` · atlas · 9 parts · largest 1092×726 · sheet `sheets/Intro1.webp`

- **Role:** The lights of the animated logo, with the purple ground of the intro.
- **Subject:** A gold glow cut to the whole logo, the purple ring ground in a landscape and a portrait crop, a star field, a burst of yellow rays, a ring that runs from orange through pink to violet, a glow, a star and a flare bar.
- **Style:** Light on black, and two pieces of background.
- **Rendering:** Soft additive shapes.
- **Colour:** Purple #4f0561 36% with gold #dabb49 and #f8eb3f.
- **Lighting:** They are the light.
- **Ambience:** A fanfare.
- **Materials:** Light.
- **Variants:** Landscape and portrait grounds.
- **Motion:** Moved by the Intro skeleton.
- **Construction:** 9 sprites; the logo glow is 1092x726.
- **Notes:** The orange-to-violet ring is the one place where the sister game's warm colours and this game's purple are blended in one object.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 31% · saturation 82% · contrast 31% · warm 66% / cool 24% · brighter towards: bottom (1)
- **Palette (measured):** #4f0561 dark purple 36%, #8d7928 brown 18%, #1c1305 black 9%, #50360f brown 8%, #dabb49 gold 5%, #f8eb3f gold 5%

### Multiplier sparks

`Multiplier1` · atlas · 17 parts · largest 272×275 · sheet `sheets/Multiplier1.webp`

- **Role:** The burst behind a multiplier value.
- **Subject:** A 17-frame burst of gold and orange sparks.
- **Style:** Light on black.
- **Rendering:** Soft round sparks.
- **Colour:** Black to gold: #6a3d0d 19%, #d3a119 8%, #fae968 7%.
- **Lighting:** They are the light.
- **Ambience:** A pop.
- **Materials:** Light.
- **Variants:** One sequence.
- **Motion:** Particles x17.
- **Construction:** 17 sprites on a JPEG page.
- **Notes:** The same burst is shipped again in ValueUpdate.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged, strong highlights · brightness 45% · saturation 55% · contrast 45% · warm 84% / cool 0%
- **Palette (measured):** #0a0704 black 29%, #6a3d0d brown 19%, #af6d10 brown 10%, #d3a119 orange 8%, #fae968 gold 7%, #fefce1 light gold 7%

### Pop-up lights

`PopUps1` · atlas · 9 parts · largest 726×429 · sheet `sheets/PopUps1.webp`

- **Role:** The lights of the empress pop-up.
- **Subject:** A greyscale shine of her head ornaments, a white mask of her whole figure (named PrincessGlow), a shine and a shadow of the scroll, gold sparks, a glow, a violet head shadow, a star and a shine bar.
- **Style:** Masks of the art, light on black.
- **Rendering:** Soft shapes.
- **Colour:** Greys: #8a8a8a 33%, white 32%; saturation 0.08.
- **Lighting:** They are the light.
- **Ambience:** A soft halo.
- **Materials:** Light.
- **Variants:** One mask per part.
- **Motion:** Moved by the PopUps skeleton.
- **Construction:** 9 sprites on a JPEG page; the head shine is 726x429.
- **Notes:** A full-figure mask means the character can be lit, flashed or revealed as a silhouette.
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 61% · saturation 8% · contrast 44% · warm 9% / cool 2%
- **Palette (measured):** #8a8a8a grey 33%, #fdfdfd white 32%, #17160f black 14%, #48474b grey 10%, #bfbfbf grey 8%

### Pot lights

`Pot1` · atlas · 10 parts · largest 139×136 · sheet `sheets/Pot1.webp`

- **Role:** The lights of the gold pots.
- **Subject:** Round flares, glows, a white mask of the pot, a blink, a ray cone, a star and small particles.
- **Style:** Light on black.
- **Rendering:** Soft additive shapes.
- **Colour:** Greys with gold #f9ec4f (6%).
- **Lighting:** They are the light.
- **Ambience:** Glint of treasure.
- **Materials:** Light.
- **Variants:** One pot mask.
- **Motion:** Moved by the Pot skeleton.
- **Construction:** 10 sprites on a JPEG page.
- **Notes:** Small: the largest is 139x136.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 52% · saturation 35% · contrast 63% · warm 59% / cool 0%
- **Palette (measured):** #ada89f grey 16%, #140e06 black 15%, #f9f8f5 light orange 15%, #4e422f brown 14%, #7c7260 orange 13%, #483007 brown 6%

### Transition (placeholder only)

`Transition` · atlas · 1 parts · largest 16×16 · sheet `sheets/Transition.webp`

- **Role:** A skeleton meant to play between scenes.
- **Subject:** No picture: one placeholder on a 16x16 texture.
- **Style:** Nothing to read.
- **Rendering:** Nothing to read.
- **Colour:** Nothing measured: the unit has no art.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** Two animations by name, TransitionLandscape and TransitionPortrait.
- **Motion:** A Spine 4.0 skeleton of 2 bones and 1 slot; what it shows is not in the files read.
- **Construction:** A 16x16 PNG and a skeleton file.
- **Notes:** Listed so that the package is whole.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 2 bones · 1 slots · animations: TransitionLandscape (0 s), TransitionPortrait (0 s)

### Value update effect

`ValueUpdate` · atlas · 19 parts · largest 334×152 · sheet `sheets/ValueUpdate.webp`

- **Role:** The effect when a ball's value changes.
- **Subject:** Two dark strips of a geometric pattern (landscape and portrait) and a 17-frame burst of gold sparks.
- **Style:** Light on black.
- **Rendering:** Soft sparks; a faint pattern.
- **Colour:** Black with pale gold #fcea87 (11%).
- **Lighting:** They are the light.
- **Ambience:** A flash of change.
- **Materials:** Light.
- **Variants:** Landscape and portrait strips.
- **Motion:** One animation by name, ValueUpdate; Particles x17.
- **Construction:** A Spine 4.0 skeleton of 4 bones and 2 slots over 19 sprites.
- **Notes:** Probably used by Prize Boost (inference).
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 4 bones · 2 slots · animations: ValueUpdate (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 30% · saturation 39% · contrast 34% · warm 49% / cool 0%
- **Palette (measured):** #0f0c0a black 38%, #332c25 brown 24%, #fcea87 light gold 11%, #794a11 brown 6%


## Game interface

Buttons, counters and panels drawn for this game.

### Intro panel interface

`FeatureScreen.desktop` · atlas · 12 parts · largest 1201×232 · sheet `sheets/FeatureScreen.desktop.webp`

- **Role:** The controls and titles of the intro panel.
- **Subject:** The HOLD & WIN wordmark in gold on a red bar, the finished small logo MONEY GONG EMPRESS, a white play arrow on a charcoal disc, page arrows in four states and a page dot.
- **Style:** Wordmarks in the game's manner; neutral controls.
- **Rendering:** Bevelled gold lettering; flat controls.
- **Colour:** Near-black #191115 34%, gold-brown #b47a15 20%, dark red #700f03 13%, gold #fae824 11%.
- **Lighting:** Top-lit.
- **Ambience:** Plain.
- **Materials:** Gold, lacquer.
- **Variants:** Arrow states: off, hover, on, pressed (inference from the four tints).
- **Motion:** None.
- **Construction:** 12 sprites; HOLD & WIN is 1201x232.
- **Notes:** HOLD & WIN is drawn in a western slab face, unlike the faux-brush title.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 38% · saturation 60% · contrast 63% · warm 69% / cool 12% · brighter towards: top (1)
- **Palette (measured):** #191115 black 34%, #b47a15 orange 20%, #700f03 dark red 13%, #fae824 gold 11%, #deb225 gold 8%, #9b1b04 red 4%

### Base game interface and board furniture

`Main.desktop` · atlas · 82 parts · largest 1736×704 · sheet `sheets/Main.desktop.webp`

- **Role:** The buttons, meters and frame of the base game.
- **Subject:** Half of the gold reel frame with a purple inlay and a tassel (purple in the base game screen); jackpot plaques as glossy pills in red, gold, blue, orange, purple and green with gold scroll ends; the words GRAND, MAJOR, MINOR, MAXI, MINI and MONEY GONG PRIZE; round charcoal buttons with white icons (spin, stop, auto, bet, sound, settings, home, turbo, trophy, plus, minus, close, tick); gold coins; and small copies of the symbols.
- **Style:** Two manners: themed gold furniture, and a neutral charcoal button set.
- **Rendering:** Furniture is airbrushed with bevelled gold; buttons are flat discs with a thin light rim.
- **Colour:** Near-black #1d0b0d 38%, white 11%, gold #e8a928 10%, grey-violet #53495a 8% for the buttons.
- **Lighting:** Top-lit (measured on 26 parts).
- **Ambience:** Orderly; the gold belongs to the game, the buttons to the provider.
- **Materials:** Gold, enamel, smoked glass.
- **Variants:** Six plaque colours, one per meter. The button discs are tinted slightly violet here.
- **Motion:** None in the sheet.
- **Construction:** 82 sprites; the frame half is 918x1106.
- **Notes:** Jackpot tier colours are the same code as on the balls: Grand red, Major green, Maxi purple, Minor blue, Mini orange.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 36% · saturation 52% · contrast 48% · warm 52% / cool 29% · brighter towards: top (26), top-right (3), left (2)
- **Palette (measured):** #1d0b0d black 38%, #fefdfd white 11%, #954d0f brown 10%, #e8a928 orange 10%, #53495a grey 8%, #9990a2 grey 4%

### Paytable pictures

`Paytable.desktop` · atlas · 43 parts · largest 739×1020 · sheet `sheets/Paytable.desktop.webp`

- **Role:** The pictures of the paytable and rules pages.
- **Subject:** A tall purple panel with a gold frame and a pot on top, the empress full length in a gold frame three cells tall, green buttons, small copies of every symbol and ball, the feature words MULTIPLIER, VORTEX PAYS and PRIZE BOOST, FIRECRACKERS, gold figures, red multipliers x2 to x25, and two small diagrams of valid and invalid ways.
- **Style:** The game's own art at small size, with plain diagrams.
- **Rendering:** As the originals; hard-edged (soft edge 0.11).
- **Colour:** Dark magenta #371429 38%, #77215c 8%, with green #36862a and #6fd859 for the buttons.
- **Lighting:** Top-lit (measured on 20 parts).
- **Ambience:** Informative.
- **Materials:** As the originals.
- **Variants:** Multipliers x2, x3, x4, x5, x8, x10 and x25.
- **Motion:** None.
- **Construction:** 43 sprites; the full-length empress is 264x537.
- **Notes:** The only place the whole standing empress is shipped as one picture: she holds a fan and wears a floor-length purple robe.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 41% · saturation 64% · contrast 65% · warm 58% / cool 12% · brighter towards: top (20), top-left (3), bottom (1)
- **Palette (measured):** #371429 dark magenta 38%, #fdfcfa light orange 9%, #77215c dark magenta 8%, #36862a green 4%, #6fd859 green 4%

### Bonus Buy buttons and price figures

`BonusBuy.desktop` · atlas · 24 parts · largest 614×211 · sheet `sheets/BonusBuy.desktop.webp`

- **Role:** The buttons and figures of the Bonus Buy panel.
- **Subject:** Wide glossy buttons in green and in red, each in several states (disabled, normal, hover, pressed), a round red close button with a gold cross and gold rim in four states, and a set of tall gold figures with a brown edge (0 to 9, currency signs, comma, point).
- **Style:** Glossy themed buttons, unlike the charcoal provider set.
- **Rendering:** Glass-like gradient with a top highlight and a gold rim.
- **Colour:** Green #569d4a 15% and #2a6120, gold #f5b50d and #f9de4b, red #e5060a 6%.
- **Lighting:** Top-lit (measured on 18 parts).
- **Ambience:** Inviting; green to buy, red to leave.
- **Materials:** Glass, gold.
- **Variants:** Two button colours by four states.
- **Motion:** None in the sheet.
- **Construction:** 24 sprites; a button is 614x211.
- **Notes:** A feature the sister game does not have.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 51% · saturation 65% · contrast 66% · warm 76% / cool 12% · brighter towards: top (18)
- **Palette (measured):** #569d4a green 15%, #afc19c green 9%, #f5b50d orange 9%, #f9de4b gold 8%, #2a6120 dark green 7%, #e5060a red 6%

### Intro panel as one picture

`4033027e388672692afe19dc03fc34f88b87aea5f19aPT_Preview_1-jpg` · atlas · 1 parts · largest 1163×585 · sheet `sheets/4033027e388672692afe19dc03fc34f88b87aea5f19aPT_Preview_1-jpg.webp`

- **Role:** A flat preview of the intro panel, used in the paytable.
- **Subject:** On purple in a gold frame, under the logo, three columns: IGNITE ALL FIRECRACKERS OR COLLECT 6 OR MORE (green ball) TO TRIGGER HOLD & WIN; the gong MAY AWARD MULTIPLIER, VORTEX PAYS, PRIZE BOOST OR MONEY GONG BONUS DURING HOLD & WIN; EACH MONEY GONG BONUS DURING HOLD & WIN AWARDS THE MONEY GONG BONUS.
- **Style:** The game's art composed with gold poster captions.
- **Rendering:** Flat composite.
- **Colour:** Dark purple #47025d 70% with gold #b17528 and #dcc14c.
- **Lighting:** Top-lit.
- **Ambience:** Clear and festive.
- **Materials:** As the parts.
- **Variants:** One.
- **Motion:** None.
- **Construction:** A single 1163x585 JPEG.
- **Notes:** It shows the layout of the intro in one frame: three columns, picture then words.
- **Measured:** dark, vivid, warm and cool mixed, high contrast, hard-edged · brightness 20% · saturation 91% · contrast 64% · warm 28% / cool 68% · brighter towards: top (1)
- **Palette (measured):** #47025d dark purple 70%, #b17528 orange 10%, #dcc14c gold 5%, #6f2214 dark red 4%, #72029a purple 3%, #86325b magenta 3%

### Bonus Buy panel

`BonusBuy` · atlas · 4 parts · largest 741×962 · sheet `sheets/BonusBuy.webp`

- **Role:** The panel that offers the feature for a price.
- **Subject:** A tall dark magenta panel with a gold frame, a separate gold top bar with red ends, a row of gold ingots, and the gold pot heaped with coins.
- **Style:** Themed panel with glossy objects.
- **Rendering:** Airbrushed gold; the panel is a soft gradient.
- **Colour:** Dark magenta #39132b 63%, #76215e 12%, brown-gold #984f0b 11%.
- **Lighting:** Top-lit (measured).
- **Ambience:** Rich; a shop window.
- **Materials:** Gold, lacquer.
- **Variants:** One panel.
- **Motion:** Five animations by name: ButtonIdle, ButtonHover, ButtonPress, BuyPopUpIdle, BuyPopUpPress.
- **Construction:** A Spine 4.0 skeleton of 48 bones and 67 slots over 4 pictures; the panel is 741x962.
- **Notes:** Not seen in play.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 48 bones · 67 slots · animations: ButtonHover (0 s), ButtonIdle (0 s), ButtonPress (0 s), BuyPopUpIdle (0 s), BuyPopUpPress (0 s)
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 23% · saturation 72% · contrast 41% · warm 64% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #39132b dark magenta 63%, #76215e dark magenta 12%, #984f0b brown 11%


## Typography

Embedded fonts and lettering.

### Money Gong Bonus figures

`MoneyGong.desktop` · atlas · 34 parts · largest 276×276 · sheet `sheets/MoneyGong.desktop.webp`

- **Role:** The numbers of the Money Gong Bonus.
- **Subject:** Two sets of figures with currency signs: one in brown lacquer with a cream and orange double outline, one in flat yellow; plus a dark disc and a yellow square.
- **Style:** Fat rounded poster figures.
- **Rendering:** The lacquer set has a gloss band across the middle and a glowing outline; the yellow set is flat.
- **Colour:** Near-black #1f0704 45%, yellow #fce12a 28%, brown #632d14 11%, orange #f45b05 4%.
- **Lighting:** A gloss from the top left on the lacquer set (measured).
- **Ambience:** Heavy and precious.
- **Materials:** Lacquer; flat ink.
- **Variants:** Two sets for two places.
- **Motion:** None.
- **Construction:** 34 sprites; a lacquer figure is about 93x140.
- **Notes:** With the white, magenta and gold sets elsewhere the game draws at least five number sets.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 39% · saturation 81% · contrast 43% · warm 100% / cool 0% · brighter towards: top-left (2), top (2)
- **Palette (measured):** #1f0704 black 45%, #fce12a gold 28%, #632d14 brown 11%, #f9d893 light orange 8%, #f45b05 orange 4%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `Preloader.desktop`: 5 parts
- `CheatTool`: 43 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Gang of Three (Regular); Noto Sans (Black); Noto Sans (Condensed Black); Noto Sans (Condensed Bold); Noto Sans (Regular); Noto Sans Display (Condensed Bold); Nuku Nuku (Regular); Passion One (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1191 components cut from 55 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
