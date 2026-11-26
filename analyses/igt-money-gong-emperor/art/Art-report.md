# Money Gong Emperor: art report

igt · run `2026-11-26-1846-igt-money-gong-emperor` · captured 2026-11-26

Source: the provider's free-play demo, https://stage-game-launcher-lux.isoftbet.com/1015/201371?mode=0&cur=USD&lang=en

**Extracted:** 1127 named components from 54 textures in 54 atlases; 30 Spine skeletons; 42 frame sequences (494 frames); 8 fonts. Grouped into 51 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A red and gold Chinese good-fortune game built around one emblem: a gold gong with a red fret knot that reappears as the title's coin, the money balls and the coins, with fat red brush-stroke royals, four glossy gold objects on coloured plates and one painted character, a laughing emperor, as the top symbol and the host of the pop-ups.

**Style.** Two manners side by side. Symbols, pots, gong and firecrackers are glossy, toy-like stylised objects. The emperor is a realistic painted figure. The setting is not a place but ornament: a red ground pressed with a wave-scale pattern, cloud scrolls and Greek-key bands. The interface buttons are a neutral charcoal set outside the theme.

**Rendering.** Smooth airbrushed gradients with hard silhouettes, a gold or light rim and white star glints on every object; lettering with a white outline and a dark extrusion; effects as soft light on black. Nothing has a drawn black outline. Measured hard-edged overall (soft edge 0.07).

**Colour.** Red and gold with almost no cool colour: measured over the game's own art, dark red #600d04 at 20% and near-black #1d0d08 at 18% lead, then gold-orange #edb517 at 8%; warm 74% against cool 4%, saturation 0.62, brightness 0.39. Hues are orange 43%, red 33%, yellow 19%, green 3%. Colour outside red and gold is rationed and always means something: green #06ed61 is the money ball, green, blue, purple and red-gold are the gong's four features, and each jackpot tier has a colour of its own (Grand red, Major green, Maxi purple, Minor blue, Mini orange); magenta is the top prize's figure; the multiplier is red with a white outline.

**Lighting.** One top light on everything (measured from the top on 174 parts, top-right on 32, top-left on 19) with specular glints on the gold; the backgrounds are dark with a low glow, so the gold objects are the light of the screen. The base reel backing is the darkest surface (#550202, brightness 0.07).

**Ambience.** Festive, lucky and rich: New Year firecrackers, coins, pots of gold and a laughing emperor. Calm in the base game, where the screen is a dark red wall with gold furniture; the bonus spins turn the board itself gold.

**Shape language.** Circles everywhere: gong, coins, money balls, jackpot discs, round buttons, the ring in the background, the bonus wheel. Around them, cloud scrolls and a Greek-key band as the two ornaments, and pill-shaped plaques for every figure. The lettering is the one angular element.

**Materials.** Polished gold above all; red lacquer and enamel; glass or jade balls; brocade and gold metalwork on the emperor; paper firecrackers; smoked glass for the buttons.

**Typography and lettering.** The logo is heavy angular faux-brush capitals in bevelled yellow gold with a deep red extrusion. Jackpot names and MONEY GONG BONUS are drawn in the same faux-brush manner; two such faces are embedded (Gang of Three and Nuku Nuku), which is probably where they come from (inference). The three feature words are rounded poster capitals, one colour each. Running text is live Noto Sans (Black, Condensed Black, Condensed Bold, Regular) with Passion One. Figures are bitmap sets drawn per place: white for the bonus spins, magenta and gold for ball values, brown-lacquer and yellow for the Money Gong Bonus.

**Motion.** Spine skeletons carry all of it: 16 skeletons in Spine 4.0 or 4.1 (the report header counts 30 files because 14 layout files of the client are counted with them). By their animation names: every symbol has a win, the money ball four landings, the gong turns like a coin to a feature face and is struck, pots grow and are hit by coins, firecrackers are lit and go off, four win tiers come in, loop and leave, and the emperor pops up with a scroll. Around them, 42 frame sequences (494 frames) of sparks, sweeps, trails and bursts, and nine particle files. No skeleton frame is shown: the project's drawing tool is written for Spine 3.7 and drew none of these; the six real screens show only the base game, the intro and a spin, so movement is read from names and parts and is inference throughout.

**Variants and themes.** One base ground, one curtain scene for the intro, and a board that changes backing from dark red to gold for the bonus spins; a Hold & Win grid and a round Money Gong Bonus wheel as feature scenes (parts only, not seen in play). Every reel symbol ships sharp and motion-blurred. The money ball comes green and gold, plain and with four jackpot names. The gong has five faces. Landscape only was captured; portrait animations are named in the files.

**How it is built.** 1,127 named sprites on 54 textures in 51 units, 49 of them the game's own art. Solid art is PNG in TexturePacker sheets or Spine atlases; effects are JPEG on black on separate pages of the same atlas; backgrounds are single JPEGs with no layers (1584x720, the curtain 3168x1440). A reel symbol is about 300x270 for a cell of about 313x302; the emperor of the pop-up is the largest art (head 899x801). Half of the reel frame is shipped and mirrored (inference). Three skeletons (the two ambients and the transition) ship only a placeholder.

**Consistency.** Very tight. One emblem at four sizes, two ornaments, one top light and a two-colour palette hold every screen together, and the few other colours are a code the player learns on the intro panel and meets again on the gong, the balls and the meters. The loose ends are the neutral grey buttons and the plain sans win titles, which belong to the provider's kit more than to the game.

**What to take from it.** (1) A feature can be the art direction. The gong is a symbol, the title's coin, the trigger device and the bonus wheel's centre: one well-made emblem reused at four sizes does the work of several separate illustrations. (2) Colour is used as a code, not as decoration. On an almost entirely red and gold screen, green means money ball, four colours mean the four features and each jackpot tier has its own, taught once on the intro panel and repeated on gong, balls and meters. (3) No scenery at all. The background is a patterned wall with a seat for the gong; the board changes from dark red to gold for the bonus spins. A leading game here spends nothing on a landscape. (4) Royals are cheap and still on theme: five letters in one red brush stroke with a gold edge, no ornament each, readable on a near-black reel backing. (5) The only painted character is saved for the top symbol and the pop-up host, cut into a few large parts. Everything else that moves is an object. (6) Effects are greyscale or gold light on black, shipped apart from the solid art and shaped to their object (a light sweep per wordmark, a glow per silhouette). That split is a production pattern an AI art pipeline can follow: generate solid pieces, derive masks and glows from their outlines. (7) Pre-rendered blur: every reel symbol has a second, motion-blurred picture. Plan two outputs per symbol. (8) Several drawn number sets, each tied to one place and prize, instead of one font: figures are treated as art.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm, medium contrast, hard-edged · brightness 39% · saturation 62% · contrast 47% · warm 74% / cool 4% · brighter towards: top (174), top-right (32), top-left (19)

Palette: #600d04 dark red 20%, #1d0d08 black 18%, #edb517 orange 8%, #3c372d brown 7%, #88837a grey 7%, #f9f9f7 light yellow 6%, #c1bfbd grey 5%, #665a46 brown 4%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 5 | 10% | 97% | 21% | 100% / 0% | #5f0302 dark red 88%, #270202 black 6%, #a80b04 red 4% |
| Reel board | 10 | 37% | 89% | 55% | 92% / 6% | #4f0702 dark red 39%, #f2b80f orange 17%, #9d4207 brown 16% |
| Symbols | 3 | 54% | 78% | 63% | 78% / 14% | #e4a626 orange 21%, #f9e450 gold 15%, #08e75e green 6% |
| Characters | 2 | 31% | 90% | 57% | 98% / 1% | #670d05 dark red 36%, #c80906 red 21%, #f7c10e gold 11% |
| Logo and title | 3 | 55% | 70% | 70% | 92% / 0% | #fdf44e gold 17%, #f9bd18 orange 16%, #6b1109 dark red 12% |
| Win celebrations and banners | 6 | 38% | 59% | 46% | 94% / 4% | #4c3c21 brown 23%, #1c130b black 20%, #74724f yellow 11% |
| Effects | 15 | 43% | 42% | 46% | 59% / 0% | #1b130c black 24%, #4c3f2a brown 19%, #7c7368 grey 10% |
| Game interface | 4 | 34% | 62% | 55% | 64% / 21% | #250f10 black 34%, #680a03 dark red 15%, #fdfdfc light orange 9% |
| Typography | 1 | 39% | 81% | 43% | 100% / 0% | #1f0704 black 45%, #fce12a gold 28%, #632d14 brown 11% |
| Provider interface (shared) | 2 | 18% | 38% | 7% | 1% / 41% | #120c1d black 80%, #ffffff white 11%, #2e263d dark purple 8% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Red wave-scale ground, base game background

`76512634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Main--Landscape-jpg` · atlas · 1 parts · largest 1584×720 · sheet `sheets/76512634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Main--Landscape-jpg.webp`

- **Role:** The backdrop of the base game, behind the reel board, the gong and the meters.
- **Subject:** A flat red ground covered with a small wave-scale pattern (overlapping arcs), with one raised round frame at the left: a ring with cloud-scroll ornaments at four points and a recessed disc in its middle. The right two thirds are empty.
- **Style:** Ornamental and graphic, not a place: Chinese festive paper or lacquer rather than a landscape.
- **Rendering:** Smooth digital relief: the ring is embossed with a soft inner shadow and a thin lit rim; the pattern is tone on tone and fades into a dark vignette at the top right.
- **Colour:** One hue. Measured #570403 at 90% and #a51609 at 10%, brightness 0.10, saturation 0.97, fully warm, contrast 0.14.
- **Lighting:** A soft glow rises from the bottom left corner (measured light from the bottom left); the ring is lit along its lower inner edge. Everything else falls to dark.
- **Ambience:** Warm, dark and quiet: a red wall that leaves all brightness to the gold laid over it.
- **Materials:** Embossed lacquer or card with a pressed pattern (as it reads; inference).
- **Variants:** The preloader ground is the same pattern with the logo painted in; FeaturesBG is a separate curtain scene. A portrait version exists by the animation names (MainAmbientPortrait) but was not captured.
- **Motion:** None in the file. The skeleton MainAmbient that would animate over it ships only a placeholder.
- **Construction:** One JPEG of 1584x720, no layers.
- **Notes:** The recessed ring is the seat of the gong: the background is built around the feature device, and the reel area is left plain because the reel backing covers it.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 10% · saturation 97% · contrast 14% · warm 100% / cool 0% · brighter towards: bottom-left (1)
- **Palette (measured):** #570403 dark red 90%, #a51609 red 10%

### Preloader picture with the logo

`76512634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Preloader--Landscape-jpg` · atlas · 1 parts · largest 1584×720 · sheet `sheets/76512634ad5e24bd264ae5a7d48701fc30b342c33ba3Background--Preloader--Landscape-jpg.webp`

- **Role:** The loading screen.
- **Subject:** The logo MONEY GONG EMPEROR on a gold coin with gold cloud scrolls, centred on the red wave-scale ground inside two concentric rings with cloud-scroll ornaments.
- **Style:** The same ornamental graphic manner as the base ground, with the logo as a glossy bevelled object on top.
- **Rendering:** Flattened into one picture: bevelled gold letters with white glints and a dark red extrusion, a soft dark vignette to the corners.
- **Colour:** Red with a gold centre: #5e0b08 at 82%, then #c2891f, #f8f08b and #f9e73d for the logo; brightness 0.18, contrast 0.71.
- **Lighting:** The logo is lit from above with star glints on letter corners; the ground glows a little behind it.
- **Ambience:** Festive and rich: gold on red, symmetric, like a seal.
- **Materials:** Polished gold, red enamel edges, embossed red ground.
- **Variants:** Only the landscape picture was captured (the file name says Landscape).
- **Motion:** None in the file; the loading bar and marks are drawn over it by the launcher.
- **Construction:** One JPEG of 1584x720 with the logo baked in.
- **Notes:** It is the only place where the logo is a finished flat picture; in the game the logo is assembled from parts (unit Intro).
- **Measured:** dark, vivid, warm, high contrast, hard-edged · brightness 18% · saturation 88% · contrast 71% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #5e0b08 dark red 82%, #280807 black 4%, #c2891f orange 4%, #f8f08b light gold 2%, #b21709 red 2%, #f9e73d gold 2%

### Red curtain scene with firecrackers

`76512634ad5e24bd264ae5a7d48701fc30b342c33ba3FeaturesBG-jpg` · atlas · 1 parts · largest 3168×1440 · sheet `sheets/76512634ad5e24bd264ae5a7d48701fc30b342c33ba3FeaturesBG-jpg.webp`

- **Role:** The backdrop of the intro panel (seen in the real screens); by its name, of the feature screens too (inference).
- **Subject:** A dark red stage: curtain folds at both sides, a brighter band of light across the top, two thin vertical light lines framing the middle, and rows of round red firecrackers with striped fuses along the bottom corners, soft and out of focus.
- **Style:** Theatrical and 3D-rendered where the base ground is flat ornament.
- **Rendering:** Soft, low-contrast render; the firecrackers are blurred as a foreground would be; faint large cloud-scroll shapes sit in the curtain.
- **Colour:** Almost one colour: #600101 at 89%, #270101, #a40201; brightness 0.08, saturation 0.99, contrast 0.10.
- **Lighting:** A top light washes the upper middle; the two vertical lines glow; edges go to black.
- **Ambience:** A stage before the show: dark, expectant, festive through the firecrackers alone.
- **Materials:** Cloth, paper firecrackers with gold bands.
- **Variants:** None captured.
- **Motion:** None in the file.
- **Construction:** One JPEG of 3168x1440, twice the size of the base ground.
- **Notes:** It is the darkest and plainest picture of the game, made to sit behind bright text and tokens.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 8% · saturation 99% · contrast 10% · warm 100% / cool 0%
- **Palette (measured):** #600101 dark red 89%, #270101 black 7%, #a40201 red 4%

### Bonus spins ambient layer (placeholder only)

`FreeSpinsAmbient` · atlas · 1 parts · largest 16×16 · sheet `sheets/FreeSpinsAmbient.webp`

- **Role:** A skeleton meant to play an ambient loop over the bonus spins.
- **Subject:** No picture: one 1x1 placeholder on a 16x16 texture.
- **Style:** Nothing to read.
- **Rendering:** Nothing to read.
- **Colour:** Nothing measured: the unit has no art.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** Six animations by name: FreeSpins Landscape and Portrait, each with IdleIn, IdleLoop and IdleOut.
- **Motion:** A Spine 4.0 skeleton of 2 bones and 1 slot; the particle files FreeGameTrailTop and FreeGameTrailBottom suggest the ambience is particles (inference).
- **Construction:** A 16x16 PNG and a skeleton file.
- **Notes:** Listed so that the package is whole; it carries no art.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 2 bones · 1 slots · animations: FreeSpinsLandscapeIdleIn (0 s), FreeSpinsLandscapeIdleLoop (0 s), FreeSpinsLandscapeIdleOut (0 s), FreeSpinsPortraitIdleIn (0 s), FreeSpinsPortraitIdleLoop (0 s), FreeSpinsPortraitIdleOut (0 s)

### Base game ambient layer (placeholder only)

`MainAmbient` · atlas · 1 parts · largest 16×16 · sheet `sheets/MainAmbient.webp`

- **Role:** A skeleton meant to play an ambient loop over the base game.
- **Subject:** No picture: the atlas holds one 1x1 placeholder on a 16x16 texture.
- **Style:** Nothing to read.
- **Rendering:** Nothing to read.
- **Colour:** Nothing measured: the unit has no art.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** Two animations by name, MainAmbientLandscape and MainAmbientPortrait.
- **Motion:** A Spine 4.0 skeleton of 2 bones and 1 slot. What it moves in the game, if anything, is drawn elsewhere, probably by the particle emitters (inference).
- **Construction:** A 16x16 PNG and a skeleton file.
- **Notes:** Listed so that the package is whole; it carries no art.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 2 bones · 1 slots · animations: MainAmbientLandscape (0 s), MainAmbientPortrait (0 s)


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Bonus spins frame and counter digits

`FreeSpins.desktop` · atlas · 17 parts · largest 918×1189 · sheet `sheets/FreeSpins.desktop.webp`

- **Role:** The reel frame variant and the number font of the bonus spins.
- **Subject:** One half of the gold scroll frame (a top rod with a side plaque and red tassel), a gold plaque with notched ends, and a set of heavy white digits with currency signs, comma and point.
- **Style:** The frame is the game's gold ornament; the digits are a plain condensed poster face.
- **Rendering:** Frame: bevelled gold with soft highlights. Digits: flat white with a dark brown outline and no gradient.
- **Colour:** #984f06, #ecb31e and #c6810f for the gold, #fefefd for the digits, #340802 for outlines.
- **Lighting:** Frame lit from the top.
- **Ambience:** Clear and loud: white numbers on gold are the most readable figures in the game.
- **Materials:** Polished gold, silk tassel.
- **Variants:** The base game frame is the same drawing in Main.desktop; the digits come with pound, dollar and euro signs.
- **Motion:** None in the files.
- **Construction:** 17 sprites; the frame half is 918x1189 and is mirrored for the other side (inference from one half being shipped).
- **Notes:** Shipping half a frame and mirroring it halves the texture cost of the largest ornament.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 50% · saturation 75% · contrast 76% · warm 100% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #984f06 brown 33%, #fefefd light orange 18%, #340802 black 17%, #ecb31e orange 16%, #c6810f orange 9%, #631f05 brown 2%

### Hold & Win board parts

`HoldAndWin.desktop` · atlas · 5 parts · largest 1073×134 · sheet `sheets/HoldAndWin.desktop.webp`

- **Role:** The pieces that turn the reel board into the Hold & Win grid.
- **Subject:** A long dark red bar with gold scroll ends, a thin horizontal and a thin vertical divider line, and two round cell tokens with a gold rim: one dark and empty, one bright green.
- **Style:** The game's gold-rimmed ornament, kept very plain.
- **Rendering:** Clean vector-like shapes with a soft gold bevel; the green token has a brushed radial sheen.
- **Colour:** #390a02 at 71%, gold #c79f26 and #fdfa5a, and the one green #0ee813.
- **Lighting:** Gold rims lit from the top.
- **Ambience:** Sober: the grid is furniture, and the money balls bring the colour.
- **Materials:** Gold, dark lacquer, green glass or jade.
- **Variants:** Empty and filled cell token.
- **Motion:** None in the files.
- **Construction:** 5 sprites in a TexturePacker sheet; the dividers are 1571x15 and 21x943, the bar 1073x134, the tokens 112x107.
- **Notes:** The filled token is the same green as the money ball, so a held position and a collected ball read as one thing.
- **Measured:** dark, vivid, warm, high contrast · brightness 22% · saturation 92% · contrast 71% · warm 97% / cool 1% · brighter towards: top (3)
- **Palette (measured):** #390a02 black 71%, #c79f26 gold 10%, #8e4d0b brown 10%, #fdfa5a gold 5%, #e9c44e gold 2%, #0ee813 green 2%

### Reel backing, bonus spins

`765163884f0202977094baecccc2c8b15bbe14a502e2Reel--FS--Background-jpg` · atlas · 1 parts · largest 1567×907 · sheet `sheets/765163884f0202977094baecccc2c8b15bbe14a502e2Reel--FS--Background-jpg.webp`

- **Role:** The ground behind the symbols during the bonus spins (the file name says FS).
- **Subject:** The same five lit columns, now gold and covered with the wave-scale pattern.
- **Style:** Ornamental; the pattern of the base background brought onto the board.
- **Rendering:** Embossed tone-on-tone pattern over a column gradient.
- **Colour:** Orange and gold: #983c05 at 43%, #f1b108 at 33%, #d17807 at 22%; brightness 0.48 against 0.07 for the base backing.
- **Lighting:** Each column is lit down its centre.
- **Ambience:** A switch from night to gold: the feature is told by the board changing colour, not by a new scene.
- **Materials:** Pressed gold foil (as it reads).
- **Variants:** The gold counterpart of the base backing.
- **Motion:** None.
- **Construction:** One JPEG of 1567x907.
- **Notes:** The red royals will sit on gold here, the reverse of the base game; no real screen of the bonus spins was reached to confirm how it looks in play.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 48% · saturation 97% · contrast 56% · warm 100% / cool 0%
- **Palette (measured):** #983c05 brown 43%, #f1b108 orange 33%, #d17807 orange 22%, #4e0f02 dark red 2%

### Blank cell, Hold & Win

`765166a53f7fbab67db96b9a95b64e9b329c19e95d57HW--Reel--Blank--Image-jpg` · atlas · 1 parts · largest 299×303 · sheet `sheets/765166a53f7fbab67db96b9a95b64e9b329c19e95d57HW--Reel--Blank--Image-jpg.webp`

- **Role:** A blank picture for a Hold & Win cell (by its name).
- **Subject:** A flat grey square.
- **Style:** None.
- **Rendering:** Flat fill.
- **Colour:** #8b8b8b at 100%.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** None.
- **Motion:** None.
- **Construction:** One JPEG of 299x303: the size of one cell.
- **Notes:** A neutral picture, probably tinted or used as a mask by the client (inference). It gives the cell size.
- **Measured:** mid-tone, muted, neutral, low contrast, hard-edged · brightness 55% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #8b8b8b grey 100%

### Reel backing, base game

`7651aa50488a2fbfdaa32554c05b121b5004969e1662Reel--Main--Background-jpg` · atlas · 1 parts · largest 1567×907 · sheet `sheets/7651aa50488a2fbfdaa32554c05b121b5004969e1662Reel--Main--Background-jpg.webp`

- **Role:** The ground behind the symbols on the five reels of the base game.
- **Subject:** Five vertical columns of dark red, each brightest down its middle and black at its edges, like five lit cylinders or cloth panels.
- **Style:** Plain and abstract.
- **Rendering:** A smooth gradient with a faint grain; no pattern, no ornament.
- **Colour:** #550202 at 88% and #270101 at 12%; brightness 0.07, contrast 0.06: the darkest surface in the game.
- **Lighting:** Each column is lit down its centre, which rounds the reels.
- **Ambience:** Deep and recessive: the board reads as a dark window in which red and gold symbols float.
- **Materials:** Reads as satin or lacquer (inference).
- **Variants:** The bonus spins backing is gold (next unit); the Hold & Win board uses its own cells.
- **Motion:** None.
- **Construction:** One JPEG of 1567x907 for the whole board: about 313 wide per reel and 302 high per row.
- **Notes:** Red royals on a red board work only because the board is this dark and the letters carry a bright rim.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 7% · saturation 98% · contrast 6% · warm 100% / cool 0%
- **Palette (measured):** #550202 dark red 88%, #270101 black 12%

### Money Gong Bonus wheel parts

`BonusRespinWheel1` · atlas · 16 parts · largest 1274×995 · sheet `sheets/BonusRespinWheel1.webp`

- **Role:** The scene of the Money Gong Bonus: a round wheel of cells around a large coin (by the names; the bonus was not reached in play).
- **Subject:** A dark red round ground wreathed in gold clouds, a dark disc with a gold glow, the large gold coin with the red fret emblem, a gold ring with a Greek-key band, a shadow ring, an orange-gold panel pill, a purple disc and eight gold cloud-scroll ornaments for the eight directions.
- **Style:** The game's gold and red ornament at its most elaborate.
- **Rendering:** Airbrushed bevels on the gold; the cloud wreath is drawn with outlined scrolls and a soft shadow.
- **Colour:** #490a01 at 46%, gold #efb910 and #cc8f14, brown #9f5b0a, with a small purple.
- **Lighting:** Top-lit gold; the centre disc glows at its rim.
- **Ambience:** Ceremonial, a seal or a compass of fortune.
- **Materials:** Gold, lacquer, a purple enamel disc.
- **Variants:** Eight ornaments for eight positions; one purple cell ground (reelBG_purple), other colours not in the files.
- **Motion:** Driven by the BonusRespinWheel skeleton: WheelAppear, WheelIdle, GongAppear, GongIdle, PanelIn, PanelIdle, PanelCollide, CellCollectEffect.
- **Construction:** 16 sprites on the second page of the BonusRespinWheel atlas; the cloud ground is 1274x995.
- **Notes:** No real screen of this bonus was reached, so how the parts sit together is read from names only.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 32% · saturation 92% · contrast 68% · warm 97% / cool 3% · brighter towards: top (7), top-left (2), top-right (1)
- **Palette (measured):** #490a01 dark red 46%, #efb910 gold 17%, #9f5b0a brown 16%, #cc8f14 orange 6%, #090103 black 5%

### Firecracker

`FireCracker` · atlas · 4 parts · largest 100×149 · sheet `sheets/FireCracker.webp`

- **Role:** The firecrackers around the gong; igniting all of them triggers Hold & Win (the intro panel says so).
- **Subject:** A short red paper cylinder with gold bands, a gold character on a red diamond label, a striped wick, a small smoke puff and a shadow.
- **Style:** Stylised 3D-looking object, bright and simple.
- **Rendering:** Smooth shading with a gold rim; tiny at the size shipped.
- **Colour:** Red #f61124 at 49% with gold #fade80.
- **Lighting:** Lit from the front; a soft drop shadow.
- **Ambience:** Festive, New Year.
- **Materials:** Paper, gold foil.
- **Variants:** Three small sizes and one big, by the animation names (Idle1 to 3, IdleBig).
- **Motion:** 20 animations by name: Static, IdleStart, Idle, WinActivate and Win, each for sizes 1 to 3 and Big: a cracker is lit, burns and goes off (inference from the names).
- **Construction:** A Spine 4.0 skeleton of 46 bones and 40 slots over 4 pictures; the cracker is only 100x149.
- **Notes:** A whole trigger mechanic rests on one 100-pixel sprite repeated in a ring.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 46 bones · 40 slots · animations: Idle1 (0 s), Idle2 (0 s), Idle3 (0 s), IdleBig (0 s), IdleStart1 (0 s), IdleStart2 (0 s), IdleStart3 (0 s), IdleStartBig (0 s), Static1 (0 s), Static2 (0 s), Static3 (0 s), StaticBig (0 s), Win1 (0 s), Win2 (0 s), Win3 (0 s), WinActivate1 (0 s), WinActivate2 (0 s), WinActivate3 (0 s), WinActivateBig (0 s), WinBig (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 39% · saturation 71% · contrast 63% · warm 99% / cool 1% · brighter towards: bottom-right (1)
- **Palette (measured):** #f61124 red 49%, #fade80 gold 13%, #8c8a87 grey 6%, #0f0604 black 6%, #524d46 grey 4%

### The Money Gong and its feature faces

`Gong` · atlas · 15 parts · largest 905×907 · sheet `sheets/Gong.webp`

- **Role:** The feature device at the left of the board: the gong that awards a feature during Hold & Win.
- **Subject:** A large round gold gong with a red openwork emblem (a symmetric fret knot) in its middle; a gold ring with a Greek-key band; four coloured outline rings; and four feature faces of the same disc: green REPEAT PAYS, blue PRIZE BOOST, purple MULTIPLIER and red-gold MONEY GONG BONUS, plus a small blue gong, a PRIZE BOOST wordmark and a dark red YOU WIN bar with gold scroll ends.
- **Style:** Glossy 3D-looking emblem art: a coin or medal, not an instrument with a stand.
- **Rendering:** Smooth airbrushed bevels, a bright top highlight on the gold, a clean inner shadow in the cut-outs, lettering with white outline and a dark extrusion.
- **Colour:** Gold and red with one colour per feature: #fdf22f, #f6a612, #630e07, and blue #052c69 among the leading colours; brightness 0.55, contrast 0.82.
- **Lighting:** Lit from the top with a hot upper rim; the feature faces glow from within.
- **Ambience:** Rich and ceremonial; the single biggest gold object on the screen.
- **Materials:** Polished gold, red enamel, coloured enamel or glass for the feature faces.
- **Variants:** Five faces of one disc (plain, green, blue, purple, red) and four outline rings in the same colours: the feature is told by colour first, by the word second.
- **Motion:** 34 animations by name, among them Idle1, Idle2, AnticipationIn/Loop/Out, FeatureRotate, RotationStop, Collide, TriggerSplash, YouWinIn/Loop and RespinsTransition: the gong turns like a coin to show a feature face (the side strips in Gong1 are its edge) and is struck (inference from the names; no frame was drawn or seen).
- **Construction:** A Spine 4.0 skeleton of 44 bones and 46 slots over 15 pictures; the plain gong is 905x907, the feature faces 343x343.
- **Notes:** The gong carries the same fret emblem as the money balls and the coins: one motif at three sizes ties the feature together.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 44 bones · 46 slots · animations: AnticipationIn (0 s), AnticipationLoop (0 s), AnticipationOut (0 s), Appear (0 s), Collide (0 s), FeatureDimIn (0 s), FeatureDimOut (0 s), FeatureOut (0 s), FeatureParticleBack (0 s), FeatureRotate (0 s), FrameFeatureAppear (0 s), FrameFeatureDisappear (0 s), FrameFeatureRotate (0 s), FrameIdle1 (0 s), FrameIdle2 (0 s), FrameReleaseRotation (0 s), FrameRepeatPaysRotation (0 s), GongFeatureTriggerLandscape (0 s), GongFeatureTriggerPortrait (0 s), Idle1 (0 s), Idle2 (0 s), RaysIdle (0 s), ReleaseRotation (0 s), RespinsTransition (0 s), RotationStop (0 s), ScaleIn (0 s), ScaleLoop (0 s), ScaleOut (0 s), TriggerSplash (0 s), YouWinCollide (0 s), YouWinIn (0 s), YouWinLoop (0 s), YouWinOutLandscape (0 s), YouWinOutPortrait (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 55% · saturation 78% · contrast 82% · warm 71% / cool 24% · brighter towards: top (4)
- **Palette (measured):** #fdf22f gold 16%, #630e07 dark red 14%, #f6a612 orange 13%, #fcfcb0 light gold 7%, #e04e17 orange 5%, #052c69 dark blue 4%

### Gong edge and ring shadow

`Gong1` · atlas · 3 parts · largest 440×451 · sheet `sheets/Gong1.webp`

- **Role:** The side of the gong for its turn, and a shadow ring.
- **Subject:** A thin ring shadow, a half-round orange strip and a straight orange strip with horizontal bands.
- **Style:** Functional parts.
- **Rendering:** Banded gradient strips; soft shadow.
- **Colour:** Orange-brown: #9d4304 at 81%, #f66f04.
- **Lighting:** Banding suggests a lit metal edge.
- **Ambience:** None on their own.
- **Materials:** Metal edge.
- **Variants:** Round and straight edge.
- **Motion:** Used in the gong's rotation (inference from the names SideRound and SideStraight).
- **Construction:** 3 sprites on a second page of the Gong atlas.
- **Notes:** A flat disc is given thickness with two strips instead of a 3D model.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 32% · saturation 98% · contrast 29% · warm 100% / cool 0% · brighter towards: top (3)
- **Palette (measured):** #9d4304 brown 81%, #f66f04 orange 10%, #250901 black 6%, #5f2e04 brown 4%

### Gold pots with bonus spins plaques

`Pot` · atlas · 29 parts · largest 417×316 · sheet `sheets/Pot.webp`

- **Role:** The two pots above the board that hold the 6 and 12 bonus spins awards.
- **Subject:** A round-bellied gold pot with ring handles and a hammered band, heaps of gold coins and ingots for its top at three sizes, an oval red-brown plaque with a gold rim reading 12 and one reading 6, a BONUS SPINS ribbon in white on dark red, a square-holed coin turning in 20 frames and a small ingot.
- **Style:** Glossy stylised treasure, the same toy-like gold as the symbols.
- **Rendering:** Airbrushed gold with strong specular highlights and a deep orange shadow side; white-rimmed lettering.
- **Colour:** Gold and orange: #f4c513 at 36%, #892d04, #e07a0a, #f9df5b; brightness 0.60, saturation 0.85.
- **Lighting:** Lit from the top; the coin heap is the brightest part.
- **Ambience:** Abundance: a pot that visibly fills.
- **Materials:** Polished and hammered gold, coins, ingots.
- **Variants:** Two plaques (6 and 12); three coin heaps (Coins 2, 4 and 5 of a 4-frame set) for the pot filling.
- **Motion:** 10 animations by name: Idle1 to 3, Grow1 and Grow2, Collide1 to 3, Win and WinIdle: the pot grows as it collects and is hit by arriving coins (inference from the names); the coin spins in a 20-frame sequence.
- **Construction:** A Spine 4.0 skeleton of 111 bones and 125 slots over 29 pictures; the pot is 417x316.
- **Notes:** The pots are the progress meters of the bonus spins trigger, drawn as objects instead of bars.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 111 bones · 125 slots · animations: Collide1 (0 s), Collide2 (0 s), Collide3 (0 s), Grow1 (0 s), Grow2 (0 s), Idle1 (0 s), Idle2 (0 s), Idle3 (0 s), Win (0 s), WinIdle (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 60% · saturation 85% · contrast 67% · warm 100% / cool 0% · brighter towards: top (3)
- **Palette (measured):** #f4c513 gold 36%, #892d04 brown 20%, #e07a0a orange 12%, #f9df5b gold 9%, #be5908 orange 6%, #fbe998 light gold 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Static symbols, coins and tokens (sheet 1)

`Main.desktop1` · atlas · 55 parts · largest 410×397 · sheet `sheets/Main.desktop1.webp`

- **Role:** Flat copies of symbols for the spinning reels and the board, the flying coins, the jackpot balls and small paytable copies.
- **Subject:** The emperor blurred, BONUS SPINS and WILD sharp and blurred, the green and gold money balls with MAJOR, MAXI, MINI and MINOR in sharp and blurred forms, MONEY GONG BONUS, a red openwork fret medallion, square-holed gold coins seen flat, tilted and edge-on, magenta and gold digits, white dot sparks, the 243 stack of digits, and thumbnail symbols of about 80 pixels.
- **Style:** The same glossy manner, flattened to single sprites.
- **Rendering:** Blurred copies are vertical motion smears of the sharp ones, drawn into the sheet.
- **Colour:** #e8ad2c at 26%, #7b4311, green #09e55e at 10%, #fbed56; saturation 0.76.
- **Lighting:** Top-lit (measured from the top on 32 of the parts).
- **Ambience:** The same lucky cheer.
- **Materials:** Gold, glass balls, enamel.
- **Variants:** Every reel symbol exists sharp and blurred; the money ball in green (base) and gold; coins at six turning angles.
- **Motion:** No sequence is declared, but the coin angles and the blurred copies are motion stills: the reels spin by swapping to the blurred picture (seen in the real screen of the turning reels).
- **Construction:** 55 sprites in a TexturePacker sheet whose names carry a hash prefix; symbols about 300x310, thumbnails 72 to 80.
- **Notes:** Blur is pre-rendered per symbol, not done by the client: a spinning reel costs a second picture of each symbol.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 57% · saturation 76% · contrast 66% · warm 73% / cool 16% · brighter towards: top (32), top-right (4), top-left (2)
- **Palette (measured):** #e8ad2c orange 26%, #7b4311 brown 10%, #09e55e green 10%, #b66415 orange 9%, #fbed56 gold 8%, #190904 black 5%

### Static symbols, coins and value digits (sheet 2)

`Main.desktop2` · atlas · 87 parts · largest 300×310 · sheet `sheets/Main.desktop2.webp`

- **Role:** The second sheet of flat reel pictures: royals and objects sharp and blurred, coin turn frames, emblem watermarks and the value digits of the money balls.
- **Subject:** A, 10, K, Q, J in red with a gold edge, each also blurred; the money tree on blue, the lion on red, the drums on purple and the lantern on teal; gold coins with four characters around a square hole at many angles and plain coin rings; four faint purple round emblems; fat magenta digits and currency signs, and the same in gold with a pink core and a dark outline.
- **Style:** Glossy stylised objects; the digits are a rounded heavy poster face.
- **Rendering:** Airbrushed, hard-edged, with blur copies; the magenta digits are flat with a soft lower shade.
- **Colour:** Gold leads: #f6d83c at 28%, #da9b25, #fbeb8a, with #470806 and #a9140a for the reds; saturation 0.80.
- **Lighting:** Top and top-right light (measured on 41 and 19 of the parts).
- **Ambience:** Bright and rich.
- **Materials:** Gold coin metal, enamel plates.
- **Variants:** Two digit sets for values (magenta, and gold with pink core), each with pound, dollar and euro; coins in about twenty angles.
- **Motion:** The coin angles make a turning coin when played in order (inference); the blurred symbols are the spin state.
- **Construction:** 87 sprites; a reel symbol is about 300x270 for a cell of about 313x302.
- **Notes:** The magenta digits match the yellow Money Gong Prize meter's figure seen in the real screens: one loud counter-colour reserved for the top prize.
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 55% · saturation 80% · contrast 59% · warm 89% / cool 5% · brighter towards: top (41), top-right (19), top-left (3)
- **Palette (measured):** #f6d83c gold 28%, #da9b25 orange 17%, #fbeb8a light gold 8%, #470806 dark red 7%, #a9140a red 7%

### All reel symbols, layered for animation

`AllSymbols` · atlas · 64 parts · largest 340×318 · sheet `sheets/AllSymbols.webp`

- **Role:** The symbol set of the game as one skeleton: ten paying symbols, the wild, the bonus spins symbol, the money balls and the Money Gong Bonus symbol.
- **Subject:** Royals 10, J, Q, K and A as fat red brush-stroke letters; four gold objects on coloured shaped plates: a lantern on teal, a pair of drums on purple, a money tree on blue, a guardian lion on red; a smiling bearded emperor in a red and gold hat, in a gold frame, built from separate head, hat, crown wings, beard, hair, mouth, teeth and eyelid; a WILD on a pink-red medallion with a gold cloud rim; BONUS SPINS on a bronze plate; money balls in green and gold with a faint fret emblem; jackpot discs MINI, MINOR, MAXI and MAJOR; feature coins in blue, green, purple and red; MONEY GONG BONUS as stacked gold letters.
- **Style:** Glossy, toy-like, stylised objects with a realistic painted face for the emperor: two manners side by side.
- **Rendering:** Airbrushed gradients, hard silhouettes, a thin gold or light rim, white star glints; the royals have a darker red inner stroke and a gold edge; the emperor's face is painted with skin texture and soft shadows.
- **Colour:** Gold and red lead: #f3c423 at 14%, #7b1707, #a94e0f, red #d61810, with green #06ed61 for the money ball; saturation 0.81, contrast 0.64. Each high symbol owns one plate colour (teal, purple, blue, red).
- **Lighting:** Top light on almost every part (measured from the top on 21 of the parts), with specular glints on the gold.
- **Ambience:** Cheerful, lucky, rich: every picture is a wish for wealth.
- **Materials:** Polished gold throughout, coloured enamel plates, glass or jade for the balls, silk and brocade on the emperor.
- **Variants:** Royals share one colour and differ by letter only; the four objects differ by plate colour and silhouette; the money ball comes plain green, gold, and with each of the four jackpot names; the four feature coins repeat the gong's four colours.
- **Motion:** 39 animations by name: Symbol1Win to Symbol10Win, WildAppear and WildWin, BonusSpinsLand and Win, MoneyBallLand1 to 4 and MoneyBallWin, MoneyGongBonusLand, Idle, Trigger and Win, NearMiss, WheelAnticipation, MultiplierApply, PrizeBoostApply, RepeatPaysApply and CollectEffect. The emperor is the only symbol cut into moving parts (eyelids, mouth, beard, hair: inference that he blinks and laughs). No frame was drawn here: the skeletons are Spine 4.0 and the project's drawing tool is written for 3.7.
- **Construction:** A Spine 4.0 skeleton of 198 bones and 208 slots over 64 pictures; a royal is about 241x203, an object about 229x220, the money ball 242x250.
- **Notes:** The highest symbol is a person and the only one with a face; everything else is an object or a letter. Effects for these symbols are in the units AllSymbols1-0 and AllSymbols1-1.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 198 bones · 208 slots · animations: BonusSpinsLand (0 s), BonusSpinsWin (0 s), CollectEffect (0 s), MoneyBallLand1In (0 s), MoneyBallLand1Loop (0 s), MoneyBallLand1Out (0 s), MoneyBallLand2 (0 s), MoneyBallLand3 (0 s), MoneyBallLand4 (0 s), MoneyBallWin (0 s), MoneyGongBonusIdle1 (0 s), MoneyGongBonusIdle2 (0 s), MoneyGongBonusIdle2In (0 s), MoneyGongBonusLand (0 s), MoneyGongBonusTrigger (0 s), MoneyGongBonusWin (0 s), MultiplierApply (0 s), MultiplierStateIn (0 s), MultiplierStateLoop (0 s), NearMiss (0 s), PrizeBoostApply (0 s), PrizeBoostStateIn (0 s), PrizeBoostStateLoop (0 s), RepeatPaysApplyIn (0 s), RepeatPaysApplyLoop (0 s), RepeatPaysApplyOut (0 s), Symbol1Win (0 s), Symbol2Win (0 s), Symbol3Win (0 s), Symbol4Win (0 s), Symbol5Win (0 s), Symbol6Win (0 s), Symbol7Win (0 s), Symbol8Win (0 s), Symbol9Win (0 s), Symbol10Win (0 s), WheelAnticipation (0 s), WildAppear (0 s), WildWin (0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 47% · saturation 81% · contrast 64% · warm 69% / cool 22% · brighter towards: top (21), top-left (3), right (2)
- **Palette (measured):** #f3c423 gold 14%, #7b1707 dark red 11%, #150407 black 9%, #a94e0f brown 9%, #06ed61 green 6%, #d61810 red 5%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The emperor with a scroll (pop-up figure)

`PopUps` · atlas · 15 parts · largest 899×801 · sheet `sheets/PopUps.webp`

- **Role:** The game's one full character: he holds the scroll on which feature messages are written (by the names PopUp, Scroll and TextPlaceholder).
- **Subject:** A laughing man with a long dark red-brown beard and moustache, in a red and gold court hat with a green jewel and two long gold wings, a red robe with a green and gold collar and gold shoulder guards; two red rolled scroll ends with gold caps, a curved red scroll sheet with a gold border, two wide gold-lined sleeves and two hands gripping the scroll.
- **Style:** Realistic painted figure, close to the Chinese god of wealth as slot games draw him (inference as to who he is; the game calls him the emperor).
- **Rendering:** Painterly digital portrait: skin texture, soft modelled shadows, embroidery detail on the robe; the scroll and sleeves are smoother and more graphic.
- **Colour:** Red: #430d05 at 28%, #c60806 at 23%, #8b1208, with orange #da7b21 and gold #f4d42e; brightness 0.28, saturation 0.89.
- **Lighting:** Lit from above and both sides (measured top-right, top-left and top), warm, with rim light on the hat.
- **Ambience:** Jovial and generous: he presents the win.
- **Materials:** Brocade, gold metalwork, a jade or emerald jewel, lacquered scroll rods.
- **Variants:** One figure; landscape and portrait layouts by the animation names.
- **Motion:** Six animations by name: PopUp In, Loop and Out for landscape and portrait. The figure is cut into head, body, sleeves, hands and scroll, so he can unroll and hold the scroll (inference). No frame was drawn or seen in play.
- **Construction:** A Spine 4.0.64 skeleton of 57 bones and 73 slots over 15 pictures; the head is 899x801 and the body 725x653, the largest character art in the game.
- **Notes:** He is cut into far fewer parts than a Pragmatic Play character: a few large pieces moved whole, not a deforming rig (inference from 15 pictures on 57 bones).
- **Skeleton (from the file):** Spine 4.0.64 · 57 bones · 73 slots · animations: PopUpLandscapeIn (0 s), PopUpLandscapeLoop (0 s), PopUpLandscapeOut (0 s), PopUpPortraitIn (0 s), PopUpPortraitLoop (0 s), PopUpPortraitOut (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 28% · saturation 89% · contrast 65% · warm 98% / cool 1% · brighter towards: top-right (4), top-left (3), top (2)
- **Palette (measured):** #430d05 dark red 28%, #c60806 red 23%, #8b1208 dark red 17%, #da7b21 orange 8%, #ad5213 brown 7%, #f4d42e gold 6%

### Emperor glows and shadows

`PopUps2` · atlas · 5 parts · largest 515×473 · sheet `sheets/PopUps2.webp`

- **Role:** The soft layers behind and over the pop-up figure.
- **Subject:** A gold outline glow following the hat and shoulders, two red-orange flame-like glows, a dark red soft shadow of the head, a flat yellow silhouette of the head and hat, and a round white soft glow.
- **Style:** Effect layers shaped to the figure.
- **Rendering:** All soft-edged (measured soft edge 0.72).
- **Colour:** #fcc001 at 45%, #680c00 at 37%, #ef1c02.
- **Lighting:** They are the figure's rim light and halo.
- **Ambience:** Radiant.
- **Materials:** Light.
- **Variants:** None.
- **Motion:** Faded in and out with the figure (inference).
- **Construction:** 5 sprites on a third page of the PopUps atlas, up to 642x343.
- **Notes:** The glow is drawn to the silhouette rather than made by a shader.
- **Measured:** mid-tone, vivid, warm, low contrast, glow or soft effect · brightness 45% · saturation 98% · contrast 8% · warm 99% / cool 0%
- **Palette (measured):** #fcc001 gold 45%, #680c00 dark red 37%, #ef1c02 red 9%


## Logo and title

The game's own wordmark.

### Logo in parts, and intro pieces

`Intro` · atlas · 10 parts · largest 1030×1032 · sheet `sheets/Intro.webp`

- **Role:** The logo as it is assembled in the game and on the intro, with the intro's own firecracker and cloud.
- **Subject:** MONEY and GONG as two rows of heavy angular capitals in bevelled yellow gold, EMPEROR as a smaller row in the same letters, a dark red base shape of the two big words, an arc of small gold clouds, a large gold coin with the red fret emblem, a big gold cloud scroll, a large red firecracker with a gold label and a field of white sparkles.
- **Style:** Faux-brush display lettering with cut, wedge-shaped strokes, made into a glossy gold object: the common look of an Asian-themed slot title.
- **Rendering:** Each letter has a pale yellow face with a white top highlight, a darker gold bevel and a deep red extrusion; clouds are outlined gold scrolls with soft shading.
- **Colour:** Yellow and gold over red: #fdf44e at 18%, #f9bd18 at 18%, #fdfaab, with #6b110a and #a21108; brightness 0.57, contrast 0.73.
- **Lighting:** Lit from the top, with glints added as separate sparkles.
- **Ambience:** Loud, rich and lucky; the brightest thing on any screen it is on.
- **Materials:** Polished gold, red lacquer.
- **Variants:** Landscape and portrait intro animations by name; the small in-game logo and the preloader logo are the same design at other sizes.
- **Motion:** Two animations, IntroLandscape and IntroPortrait, on a skeleton of 135 bones: the words, coin and clouds arrive separately (inference from the parts being separate).
- **Construction:** A Spine 4.0 skeleton with 10 pictures; MONEY is 1096x306, the coin 1030x1032: the logo is kept at about three times the size it has in the base game.
- **Notes:** The coin behind the title is the gong itself: title, feature device and money ball all share the fret emblem.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 135 bones · 121 slots · animations: IntroLandscape (0 s), IntroPortrait (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 57% · saturation 76% · contrast 73% · warm 100% / cool 0% · brighter towards: top (3), bottom-right (1), bottom-left (1)
- **Palette (measured):** #fdf44e gold 18%, #f9bd18 orange 18%, #6b110a dark red 13%, #fdfaab light gold 12%, #2c0403 black 8%, #a21108 red 6%

### Logo mask

`Logo` · atlas · 1 parts · largest 421×72 · sheet `sheets/Logo.webp`

- **Role:** A mask of the words MONEY GONG for the logo's win shine.
- **Subject:** The two words on one line in dark red with a thin orange edge.
- **Style:** The logo lettering, flat.
- **Rendering:** Flat fill with a soft edge (soft edge 0.49).
- **Colour:** #4d0a04 and #8a0e08.
- **Lighting:** None.
- **Ambience:** None on its own.
- **Materials:** None.
- **Variants:** None.
- **Motion:** One animation, Win, on a skeleton of 29 bones: a light wipe runs across the logo inside this mask (inference from the names LogoMask and Wipe).
- **Construction:** One picture of 421x72 and a Spine 4.0 skeleton.
- **Notes:** The in-game logo is 421 pixels wide here against 1096 for the intro's MONEY alone.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 29 bones · 27 slots · animations: Win (0 s)
- **Measured:** dark, vivid, warm, medium contrast · brightness 17% · saturation 90% · contrast 38% · warm 100% / cool 0%
- **Palette (measured):** #4d0a04 dark red 46%, #8a0e08 dark red 36%, #855735 brown 8%, #bb1e16 red 4%, #bd522a orange 2%

### Logo shine layers

`Logo1` · atlas · 5 parts · largest 354×323 · sheet `sheets/Logo1.webp`

- **Role:** The light effects of the logo's Win animation.
- **Subject:** A field of white sparkles, a fan of soft rays, a four-point yellow star, a glow copy of EMPEROR and a white wipe bar.
- **Style:** Effect textures.
- **Rendering:** Soft shapes on black for adding over the logo.
- **Colour:** Greys with a little gold (#f9ef70).
- **Lighting:** Self-lit.
- **Ambience:** A quick sparkle.
- **Materials:** Light.
- **Variants:** None.
- **Motion:** Played by the Logo skeleton's Win animation.
- **Construction:** 5 sprites on a 512x512 JPEG.
- **Notes:** Effects are shipped as JPEG on black, the solid art as PNG: the same split holds across the game.
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged · brightness 34% · saturation 8% · contrast 36% · warm 11% / cool 0%
- **Palette (measured):** #4f4f4f grey 38%, #171715 black 29%, #858584 grey 18%, #b0b0b0 grey 6%, #74570b brown 2%, #e9e6d3 light yellow 2%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Intro panel pieces

`FeatureScreen` · atlas · 13 parts · largest 607×495 · sheet `sheets/FeatureScreen.webp`

- **Role:** The pictures of the three-part intro panel that explains the features.
- **Subject:** MONEY GONG BONUS as stacked gold letters, alone and on a green ball; a large green money ball; MULTIPLIER in purple-pink, REPEAT PAYS in green and PRIZE BOOST in blue, each with a white outline and dark extrusion; three red firecrackers at different angles.
- **Style:** The symbol manner at large size; the feature words are heavy poster capitals in one colour each.
- **Rendering:** Glossy gradients inside the letters, white outline, dark drop; the firecrackers are smooth 3D-looking objects.
- **Colour:** #7d0d04, green #07ec62 at 11%, gold #f8d029 and #fbf27e, red #e60709; contrast 0.85.
- **Lighting:** Top-lit letters; the ball glows from inside.
- **Ambience:** A bright, simple poster of the rules.
- **Materials:** Gold, glass ball, paper firecrackers.
- **Variants:** One colour per feature, the same colours as the gong's faces and outline rings.
- **Motion:** Three animations, Feature1 to Feature3, one per column of the panel (inference); the firecracker has a 6-frame sequence.
- **Construction:** A Spine 4.0 skeleton of 97 bones and 118 slots over 13 pictures; the largest wordmark is 607x495.
- **Notes:** The intro teaches by colour: green ball, then the three coloured feature words, exactly as they will appear on the gong.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 97 bones · 118 slots · animations: Feature1 (0 s), Feature2 (0 s), Feature3 (0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 48% · saturation 76% · contrast 85% · warm 65% / cool 24% · brighter towards: bottom-left (2), left (2), top (2)
- **Palette (measured):** #7d0d04 dark red 15%, #170a06 black 14%, #07ec62 green 11%, #f8d029 gold 10%, #fbf27e gold 9%, #e60709 red 7%

### Intro panel gong, glows and shadows

`FeatureScreen1` · atlas · 11 parts · largest 664×646 · sheet `sheets/FeatureScreen1.webp`

- **Role:** The gong of the intro panel and the soft layers under its pieces.
- **Subject:** The gold gong with a red-gold emblem at 664x646, red outline glows shaped to the Money Gong Bonus mark and the ball, grey drop shadows shaped to each feature word, two dark red smoke-like shadows and a yellow dot particle.
- **Style:** Support layers.
- **Rendering:** Soft-edged glows and shadows; the gong is the glossy emblem again.
- **Colour:** #dbb91f at 27%, #d4670a, #671a03, with pure red #ff0100 for the glows.
- **Lighting:** The gong is top-lit; the glows are red light around objects.
- **Ambience:** Depth and warmth under the poster.
- **Materials:** Gold; light.
- **Variants:** A shadow per word.
- **Motion:** Used by the FeatureScreen skeleton.
- **Construction:** 11 sprites on a second page.
- **Notes:** Every word has its own drawn shadow, so nothing depends on a runtime shadow.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 48% · saturation 86% · contrast 62% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #dbb91f gold 27%, #d4670a orange 17%, #671a03 dark red 16%, #94480c brown 13%, #e4de83 gold 8%, #ff0100 red 6%

### Jackpot meter sparkle trails

`JackpotPanel` · atlas · 1 parts · largest 1709×1020 · sheet `sheets/JackpotPanel.webp`

- **Role:** The sparkle that runs around a prize meter when it is idle or won.
- **Subject:** Twenty-one frames of a long rounded outline made of small pale yellow sparkles, a soft grey vertical gradient bar and a small orange star.
- **Style:** Effect texture.
- **Rendering:** Fine sparkles on black.
- **Colour:** Pale yellow-green greys: #55563d, #95967e, #85865a on #1a1a12.
- **Lighting:** Self-lit.
- **Ambience:** A gentle glitter around the meters.
- **Materials:** Sparkles.
- **Variants:** One trail reused for Grand, Major, Maxi, Minor, Mini and the Money Gong Prize (by the animation names).
- **Motion:** 28 animations by name: Idle, TrailPath, WinIn, WinLoop and WinOut for each of the five jackpots, and Idle, WinIn and WinLoop for the Money Gong Prize.
- **Construction:** A Spine 4.0 skeleton of 18 bones and 35 slots. Its atlas is in the newer Spine text format with rotated frames, which the reader did not cut: the unit is shown as one whole 1709x1020 page.
- **Notes:** The frames lie on their side on the page (the atlas says rotate 90). The meter plaques themselves are in the interface sheet Main.desktop.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 18 bones · 35 slots · animations: GrandIdle (0 s), GrandTrailPath (0 s), GrandWinIn (0 s), GrandWinLoop (0 s), GrandWinOut (0 s), MajorIdle (0 s), MajorTrailPath (0 s), MajorWinIn (0 s), MajorWinLoop (0 s), MajorWinOut (0 s), MaxiIdle (0 s), MaxiTrailPath (0 s), MaxiWinIn (0 s), MaxiWinLoop (0 s), MaxiWinOut (0 s), MiniIdle (0 s), MiniTrailPath (0 s), MiniWinIn (0 s), MiniWinLoop (0 s), MiniWinOut (0 s), MinorIdle (0 s), MinorTrailPath (0 s), MinorWinIn (0 s), MinorWinLoop (0 s), MinorWinOut (0 s), MoneyGongIdle (0 s), MoneyGongWinIn (0 s), MoneyGongWinLoop (0 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 32% · saturation 27% · contrast 27% · warm 100% / cool 0%
- **Palette (measured):** #55563d brown 51%, #1a1a12 black 26%, #95967e grey 18%, #85865a yellow 5%

### Multiplier tags x2, x5, x8

`Multiplier` · atlas · 4 parts · largest 145×100 · sheet `sheets/Multiplier.webp`

- **Role:** The multiplier shown when the gong awards the Multiplier feature.
- **Subject:** x8, x2 and x5 in fat rounded red characters with a white outline and a dark red drop.
- **Style:** Comic, sticker-like lettering.
- **Rendering:** Flat red with a slight top highlight, a thick white outline and a hard dark shadow below.
- **Colour:** #f01e0c at 55%, #fffdfd at 26%, #450202 at 15%; contrast 0.94, the highest of any unit.
- **Lighting:** Top highlight only.
- **Ambience:** Punchy; made to be read in a glance on top of gold.
- **Materials:** Flat enamel or sticker.
- **Variants:** Three values in this unit; the paytable sheet also has x3, x4, x10 and x25 small.
- **Motion:** Two animations, Appear and Static; each value is listed as a 4-frame sequence by the reader, but the sheet shows one drawing per value.
- **Construction:** A Spine 4.0 skeleton of 3 bones over 4 pictures of about 140x100.
- **Notes:** Red with a white outline is used nowhere else: the multiplier is the only art that leaves the gold palette on purpose.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 3 bones · 2 slots · animations: Appear (0 s), Static (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 45% · saturation 68% · contrast 94% · warm 100% / cool 0% · brighter towards: top (4)
- **Palette (measured):** #f01e0c red 55%, #fffdfd light red 26%, #450202 dark red 15%

### Win tier titles

`SpecialMessages` · atlas · 8 parts · largest 901×119 · sheet `sheets/SpecialMessages.webp`

- **Role:** The titles of the four big-win tiers.
- **Subject:** BIG WIN, HUGE WIN, MASSIVE WIN and SPECTACULAR in condensed capitals, each also as a blurred copy at half size.
- **Style:** Plain bold sans capitals in gold, far simpler than the logo.
- **Rendering:** A yellow face with a darker gold lower edge; little bevel.
- **Colour:** All gold: #c8ad0b at 40%, #f4e47f, #d7be54, #f3d718; brightness 0.67.
- **Lighting:** Flat, with a light upper half.
- **Ambience:** Clear announcement rather than spectacle.
- **Materials:** Gold foil.
- **Variants:** Four tiers in one design, told apart only by the word; a blurred copy of each for the entrance.
- **Motion:** 21 animations by name: In, Loop and Out for each tier, plus ReelsAmbient and two SpecialMessagesAmbient loops. The skeleton has 209 bones for 8 pictures, so the letters or particles ride many bones (inference). No big win was reached in play.
- **Construction:** A Spine 4.0 skeleton; each title is one picture of 901x119.
- **Notes:** A title is a single strip of text, not letter-by-letter art: the celebration is carried by particles and rays (next unit).
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 209 bones · 130 slots · animations: BigWinIn (0 s), BigWinLoop (0 s), BigWinOut (0 s), HugeWinIn (0 s), HugeWinLoop (0 s), HugeWinOut (0 s), MassiveWinIn (0 s), MassiveWinLoop (0 s), MassiveWinOut (0 s), ReelsAmbientIn (0 s), ReelsAmbientLoop (0 s), ReelsAmbientOut (0 s), SpecialMessagesAmbient1In (0 s), SpecialMessagesAmbient1Loop (0 s), SpecialMessagesAmbient1Out (0 s), SpecialMessagesAmbient2In (0 s), SpecialMessagesAmbient2Loop (0 s), SpecialMessagesAmbient2Out (0 s), SpectacularIn (0 s), SpectacularLoop (0 s), SpectacularOut (0 s)
- **Measured:** bright, vivid, warm, high contrast, strong highlights · brightness 66% · saturation 76% · contrast 65% · warm 100% / cool 0%
- **Palette (measured):** #c8ad0b gold 40%, #f4e47f gold 17%, #d7be54 gold 12%, #7d6e16 brown 10%, #f3d718 gold 8%, #fefae0 light gold 4%

### Win celebration lights

`SpecialMessages1` · atlas · 38 parts · largest 819×819 · sheet `sheets/SpecialMessages1.webp`

- **Role:** The light and particle layers of the big-win titles.
- **Subject:** A large disc of orange sparks, a tall yellow ray, a half-round orange glow, a glow copy of each title, a 30-frame strip of small orange sparks and a cluster of sparks for a path.
- **Style:** Effect textures.
- **Rendering:** Soft and additive on black.
- **Colour:** Orange and brown on black: #5f3109, #a8570b, #d98e25, #f8db78.
- **Lighting:** Self-lit; the glow rises from below the title.
- **Ambience:** Warm fireworks.
- **Materials:** Sparks.
- **Variants:** One set for all four tiers.
- **Motion:** TopParticles is a 30-frame sequence; the rest are moved by the SpecialMessages skeleton.
- **Construction:** 38 sprites on a JPEG page; the spark disc is 819x819.
- **Notes:** The same lights serve every tier, so tiers differ by the word and, probably, by duration (inference).
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 36% · saturation 80% · contrast 46% · warm 99% / cool 0%
- **Palette (measured):** #5f3109 brown 32%, #1f1105 black 23%, #a8570b brown 13%, #d98e25 orange 12%, #f8db78 gold 11%, #dcb350 orange 4%


## Effects

Frame sequences, glows, particles and transitions.

### Symbol effects (sheet 1)

`AllSymbols1-0` · atlas · 137 parts · largest 490×490 · sheet `sheets/AllSymbols1-0.webp`

- **Role:** The light effects of the symbols' landing, win, near-miss and anticipation.
- **Subject:** A star flare, gold dust, WILD rays, a sunburst, grey sparkle fields, a glowing fret disc, a BONUS SPINS glow, coloured ball shines in purple, green, blue and yellow, near-miss spark strips, rings of gold dust, an orange emperor silhouette glow and outline, curved gold trails, a pink disc, a fire-like explosion, white light sweeps shaped to BONUS SPINS, the ball and MONEY GONG BONUS, and small blinks.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Gold on black: #6d400d, #e9ad16, #b07815, with single purple, green, blue, yellow and pink pieces.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** Ball shine in four colours, matching the jackpot tiers.
- **Motion:** Frame sequences: NearMiss 30 frames, particles_antic 18, Trail 18, Bonus_Spins_Lsweep 17, moneyballLSweep 9, emperor_Blick 9, moneyGongBonus_lSweep 8.
- **Construction:** 137 sprites on a JPEG page of the AllSymbols atlas, up to 490x490.
- **Notes:** A light sweep is drawn per symbol shape (the sweep frames carry the lettering's outline), so the shine follows the letters exactly.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 42% · saturation 69% · contrast 46% · warm 85% / cool 2% · brighter towards: bottom-left (1)
- **Palette (measured):** #6d400d brown 25%, #1d1106 black 17%, #e9ad16 orange 14%, #b07815 orange 11%, #6e6656 orange 6%, #3a362d brown 5%

### Symbol effects (sheet 2)

`AllSymbols1-1` · atlas · 86 parts · largest 184×184 · sheet `sheets/AllSymbols1-1.webp`

- **Role:** More symbol effects: fireworks, rings and bursts.
- **Subject:** A white firework burst, gold dust rings, three frames of a copper Greek-key fire ring, dotted gold rings, curved gold trails, particle bursts, a white radial gradient, a thin ring and more light sweeps.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Orange-gold on black: #9f7142, #d5a872, #ecae10.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Frame sequences: particleBurst 30 frames, MoneyBallFireEffect 20, particles_antic 13, Trail 12.
- **Construction:** 86 sprites on a second JPEG page, up to 184x184.
- **Notes:** The fire ring around a money ball is itself made of the Greek-key band: even the effects carry the ornament.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 40% · saturation 65% · contrast 41% · warm 94% / cool 0%
- **Palette (measured):** #9f7142 orange 28%, #553614 brown 20%, #1f1205 black 17%, #d5a872 orange 10%, #ecae10 orange 8%, #7c551b brown 8%

### Money Gong Bonus wheel effects

`BonusRespinWheel` · atlas · 44 parts · largest 701×701 · sheet `sheets/BonusRespinWheel.webp`

- **Role:** The rays and particles of the bonus wheel.
- **Subject:** A fine star of rays, a green-yellow ring of rays, a soft yellow blob, a gold dust ring, an orange panel glow, a sunburst, a radial gradient and a yellow ring.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Yellow and orange on black: #fae811, #e19c0f, #8b6712.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** A 38-frame particle sequence; the skeleton's animations are RaysAppear, RaysIdle, CellCollectEffect and the wheel and panel moves.
- **Construction:** A Spine 4.1.24 skeleton of 100 bones and 117 slots; 44 sprites on this page, the rays 701x701.
- **Notes:** The one skeleton exported as Spine 4.1; the others say 4.0 exported from 4.1.24.
- **Skeleton (from the file):** Spine 4.1.24 · 100 bones · 117 slots · animations: CellCollectEffect (0 s), GongAppear (0 s), GongIdle (0 s), PanelCollide (0 s), PanelIdle (0 s), PanelIn (0 s), RaysAppear (0 s), RaysIdle (0 s), WheelAppear (0 s), WheelIdle (0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 40% · saturation 78% · contrast 45% · warm 97% / cool 0%
- **Palette (measured):** #140e04 black 23%, #4f3a0c brown 21%, #8b6712 brown 16%, #fae811 gold 12%, #e19c0f orange 8%

### Intro panel effects

`FeatureScreen2` · atlas · 13 parts · largest 295×404 · sheet `sheets/FeatureScreen2.webp`

- **Role:** The moving bits of the intro panel.
- **Subject:** Three frames of a silver gong disc turning edge-on, three white light sweeps shaped to the Money Gong Bonus mark, three frames of orange firecracker flame with sparks, a grey glow and a white four-point spark.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Greys with orange-yellow flame: #a19f9b, #f6e80e, #732f03.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Sequences: FirecrackerFlame 5 frames, Gong 3, MoneyGongBonusBlick 3.
- **Construction:** 13 sprites on a JPEG page.
- **Notes:** The grey gong frames are tinted in the client (inference): only brightness is stored.
- **Measured:** mid-tone, muted, warm and cool mixed, medium contrast, hard-edged · brightness 51% · saturation 22% · contrast 41% · warm 67% / cool 0%
- **Palette (measured):** #a19f9b grey 44%, #6e6b66 grey 16%, #403d39 grey 12%, #18110c black 6%, #d5d3cc grey 6%, #f6e80e gold 5%

### Firecracker effects

`FireCracker1` · atlas · 22 parts · largest 154×154 · sheet `sheets/FireCracker1.webp`

- **Role:** Smoke, flash and firework of a firecracker going off.
- **Subject:** A white smoke cloud, a 16-frame firework that opens into purple and pink streaks with orange tips, a white glow in the shape of the cracker, a small cloud, a sparkle, a short line and a fuse dot.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Greys with magenta and pink: #f7edef, #6c505e, #9f808d, #cfaeb5.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** fireworks2 is a 16-frame sequence; the particle file Fuse.json drives the burning fuse (inference from its name).
- **Construction:** 22 sprites on a JPEG page, up to 154x154.
- **Notes:** The firework is the one purple-pink effect in a gold game.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 37% · saturation 33% · contrast 42% · warm 38% / cool 9%
- **Palette (measured):** #0a060c black 39%, #f7edef light red 15%, #3f2938 dark magenta 10%, #6c505e magenta 10%, #9f808d magenta 9%, #cfaeb5 red 8%

### Gong effects (sheet 1)

`Gong2-0` · atlas · 26 parts · largest 531×427 · sheet `sheets/Gong2-0.webp`

- **Role:** Bursts and sparkles of the gong being struck and awarding.
- **Subject:** White blob bursts, rings of white sparkles, small orange sparks, flat white streak fans and a yellow fireball cloud.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Neutral greys and white (saturation 0.02), with one yellow piece.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Sequences: Burst 16 frames, FeatureFX 4, YouWinFX 4.
- **Construction:** 26 sprites on a JPEG page, up to 531x427.
- **Notes:** Stored colourless and tinted per feature colour in the client (inference from four coloured features sharing one grey set).
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 60% · saturation 2% · contrast 58% · warm 3% / cool 0%
- **Palette (measured):** #fafafa white 30%, #20201f grey 21%, #bfbfbf grey 19%, #585756 grey 15%, #888887 grey 14%

### Gong effects (sheet 2)

`Gong2-1` · atlas · 38 parts · largest 351×358 · sheet `sheets/Gong2-1.webp`

- **Role:** More gong bursts, splashes and particles.
- **Subject:** White bursts, sparkle rings, round splash rings, orange spark fields, a fine star of rays and a streak fan.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Greys with some orange: #c0bfbf, #f6f6f6, #e9c386.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Sequences: Particles 14 frames, FeatureFX 10, Splash 9, Burst 3.
- **Construction:** 38 sprites on a JPEG page.
- **Notes:** Splash rings suit a struck metal disc: the hit is shown as a ring of light, not as a mallet.
- **Measured:** mid-tone, muted, warm and cool mixed, medium contrast, hard-edged · brightness 49% · saturation 18% · contrast 52% · warm 40% / cool 0%
- **Palette (measured):** #5c5347 brown 21%, #c0bfbf grey 20%, #181611 black 20%, #918c83 grey 13%, #f6f6f6 white 11%, #3e311e brown 5%

### Gong effects (sheet 3)

`Gong2-2` · atlas · 50 parts · largest 305×302 · sheet `sheets/Gong2-2.webp`

- **Role:** Further gong effects and the emblem as a white mask.
- **Subject:** Orange spark fields, sparkle rings, white bursts and splashes, streak fans, a ring of dots and the fret emblem as a white shape on black (named Green).
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Greys with some orange: #c1c0c0, #f8f8f8, #e9c186.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Sequences: Particles 14 frames, YouWinFX 11, FeatureFX 10, Splash 9, Burst 4.
- **Construction:** 50 sprites on a JPEG page.
- **Notes:** The white emblem is a tint mask: one drawing gives the emblem in any feature colour.
- **Measured:** mid-tone, muted, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 48% · saturation 15% · contrast 48% · warm 32% / cool 0%
- **Palette (measured):** #181613 black 23%, #494239 brown 21%, #c1c0c0 grey 15%, #f8f8f8 white 15%, #7b7368 grey 14%, #a39886 orange 5%

### Gong effects (sheet 4)

`Gong2-3` · atlas · 14 parts · largest 414×142 · sheet `sheets/Gong2-3.webp`

- **Role:** The streak fan of the You Win moment.
- **Subject:** Three of fourteen frames of a flat fan of white streaks spreading sideways.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Greys only.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** YouWinFX, 14 frames.
- **Construction:** 14 sprites on a JPEG page, about 400x140.
- **Notes:** A wide, low burst made to sit behind the You Win bar.
- **Measured:** dark, muted, neutral, medium contrast, hard-edged · brightness 27% · saturation 0% · contrast 37% · warm 0% / cool 0%
- **Palette (measured):** #202020 grey 52%, #555555 grey 28%, #848484 grey 14%, #b3b3b3 grey 5%

### Intro effects and pattern

`Intro1` · atlas · 8 parts · largest 1628×784 · sheet `sheets/Intro1.webp`

- **Role:** The light layers of the logo intro and its pattern strip.
- **Subject:** A dark red-brown strip of the wave-scale pattern, a soft olive ellipse glow, white sparkles, a white ray burst, a flat lens flare, a yellow four-point star and a white bar gradient.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** #2c180b at 66%, #5b4d1e, greys.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Moved by the Intro skeleton.
- **Construction:** 8 sprites on a JPEG page; the pattern strip is 1628x784.
- **Notes:** The pattern strip is the only tiling ornament shipped as its own texture.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 21% · saturation 62% · contrast 27% · warm 80% / cool 0%
- **Palette (measured):** #2c180b black 66%, #5b4d1e brown 22%, #9c9c9c grey 5%, #676767 grey 4%, #dedede white 2%

### Multiplier particles

`Multiplier1` · atlas · 17 parts · largest 272×275 · sheet `sheets/Multiplier1.webp`

- **Role:** The burst behind a multiplier tag.
- **Subject:** Orange and yellow soft dots clustered, fading to nothing across the sequence.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** #6a3d0d, #af6d10, #d3a119, #fae968.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Particles, 17 frames.
- **Construction:** 17 sprites, up to 272x275.
- **Notes:** The same 17-frame burst is in ValueUpdate at a smaller size.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged, strong highlights · brightness 45% · saturation 55% · contrast 45% · warm 84% / cool 0%
- **Palette (measured):** #0a0704 black 29%, #6a3d0d brown 19%, #af6d10 brown 10%, #d3a119 orange 8%, #fae968 gold 7%, #fefce1 light gold 7%

### Pop-up scroll effects

`PopUps1` · atlas · 17 parts · largest 880×801 · sheet `sheets/PopUps1.webp`

- **Role:** Rays behind the emperor and shines on the scroll.
- **Subject:** A ring of orange-gold rays at 880x801, pale pink light sweeps shaped to the scroll rods, flat orange lens blinks and stars, and a white vertical sweep.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** #634509, #ac8112, with pale pink #e8c6b9.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Sequences: Star 8 frames, Blick 5, ScrollBlick 3.
- **Construction:** 17 sprites on a JPEG page.
- **Notes:** The rays are as large as the figure's head: the pop-up is staged as a sunburst behind him.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 31% · saturation 81% · contrast 38% · warm 98% / cool 0%
- **Palette (measured):** #634509 brown 41%, #201504 black 32%, #ac8112 brown 12%, #e8c6b9 light orange 5%

### Pot effects

`Pot1` · atlas · 10 parts · largest 139×136 · sheet `sheets/Pot1.webp`

- **Role:** Glows and sparkles of the gold pots.
- **Subject:** Round flares, a particle mask, a flat orange glow, a white glow, a white pot-shaped glow, a blink, a ray, a star sparkle and a few orange sparks.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** Greys with gold #f9ec4f.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** Moved by the Pot skeleton; the particle files PotCoinSplash and PotCoinsFall add coins (inference from their names).
- **Construction:** 10 sprites, the largest 139x136.
- **Notes:** Like the cracker, the pot has a white glow cut to its own outline.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 52% · saturation 35% · contrast 63% · warm 59% / cool 0%
- **Palette (measured):** #ada89f grey 16%, #140e06 black 15%, #f9f8f5 light orange 15%, #4e422f brown 14%, #7c7260 orange 13%, #483007 brown 6%

### Transition (placeholder only)

`Transition` · atlas · 1 parts · largest 16×16 · sheet `sheets/Transition.webp`

- **Role:** A skeleton for the transition between base game and feature.
- **Subject:** No picture: one 1x1 placeholder on a 16x16 texture.
- **Style:** Nothing to read.
- **Rendering:** Nothing to read.
- **Colour:** Nothing measured: the unit has no art.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** TransitionLandscape and TransitionPortrait by name.
- **Motion:** A Spine 4.0 skeleton of 2 bones and 1 slot; the transition's picture is drawn by something else in the client (inference).
- **Construction:** A 16x16 PNG and a skeleton file.
- **Notes:** Listed so that the package is whole; it carries no art.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 2 bones · 1 slots · animations: TransitionLandscape (0 s), TransitionPortrait (0 s)

### Value update effect

`ValueUpdate` · atlas · 19 parts · largest 334×152 · sheet `sheets/ValueUpdate.webp`

- **Role:** The effect when a money ball's value changes (by the name).
- **Subject:** Two dark strips of a hexagonal pattern for landscape and portrait, and the 17-frame orange dot burst.
- **Style:** Effect texture.
- **Rendering:** Soft light shapes on black, meant to be added over the picture (the black is the blend ground: inference from the format).
- **Colour:** #0f0c0a, #332c25, with gold #fcea87.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and heat.
- **Materials:** Light, sparks.
- **Variants:** None.
- **Motion:** One animation, ValueUpdate, and a 17-frame particle sequence.
- **Construction:** A Spine 4.0 skeleton of 4 bones; 19 sprites.
- **Notes:** The pattern strips are named PatternPortrait and PatternLandscape but look swapped by shape (the wide one is called Portrait); their use was not seen.
- **Skeleton (from the file):** Spine 4.0-from-4.1.24 · 4 bones · 2 slots · animations: ValueUpdate (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 30% · saturation 39% · contrast 34% · warm 49% / cool 0%
- **Palette (measured):** #0f0c0a black 38%, #332c25 brown 24%, #fcea87 light gold 11%, #794a11 brown 6%


## Game interface

Buttons, counters and panels drawn for this game.

### Intro panel interface

`FeatureScreen.desktop` · atlas · 11 parts · largest 386×386 · sheet `sheets/FeatureScreen.desktop.webp`

- **Role:** The controls of the intro panel.
- **Subject:** A large charcoal disc, the small logo, a dark gradient bar, a white play triangle, left arrows in four states and a page dot.
- **Style:** The neutral launcher button manner.
- **Rendering:** Flat white and grey shapes with thin dark outlines.
- **Colour:** #171216 at 66%, #fffffc, with the logo's gold.
- **Lighting:** None.
- **Ambience:** Neutral.
- **Materials:** Smoked glass.
- **Variants:** Arrow states for normal, hover, pressed and disabled (inference from four tints).
- **Motion:** None.
- **Construction:** 11 sprites; the disc is 386x386, the logo 541x157.
- **Notes:** The play arrow seen on the real intro screen is this disc and triangle.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, glow or soft effect · brightness 28% · saturation 27% · contrast 38% · warm 35% / cool 25% · brighter towards: top (1)
- **Palette (measured):** #171216 black 66%, #fffffc light gold 8%, #711807 dark red 4%, #f8ec73 gold 4%, #eecb2a gold 3%, #978f9c grey 3%

### Main interface sheet

`Main.desktop` · atlas · 75 parts · largest 1736×704 · sheet `sheets/Main.desktop.webp`

- **Role:** The controls, meter plaques and board furniture of the base game.
- **Subject:** Round dark glass buttons with white icons (trophy, sound on and off, gear, auto spin, bet coins, clock, home, spin arrow, stop square, lightning, fast-forward, tick, minus, plus, close); pill plaques with a gold rim in red, yellow, blue, orange, purple and green for the prize meters; the meter names GRAND, MAJOR, MAXI, MINOR, MINI and MONEY GONG PRIZE; half of the gold scroll frame; gold rods; x2, x5 and x8 tags; and stray symbol copies (emperor, coin, lantern, small royals).
- **Style:** Two layers that do not mix: themed gold ornament for the game's own furniture, and a neutral dark set of round buttons shared with other games of the launcher (inference from their neutral look).
- **Rendering:** Plaques: glossy enamel with a bevelled gold rim and a top highlight. Buttons: flat white icons on translucent charcoal discs with a thin light rim.
- **Colour:** #1e0b0c at 39%, #964a0d, #fefdfd, greys #53495a and #9990a2 from the buttons, orange #e38f13, red #e90e07.
- **Lighting:** Plaques lit from the top (measured on 22 parts).
- **Ambience:** Orderly: colour belongs to the prizes, the controls stay grey.
- **Materials:** Enamel, gold, smoked glass.
- **Variants:** Six plaque colours, one per prize: Grand red, Major green, Maxi purple, Minor blue, Mini orange and the Money Gong Prize yellow (matched to the real screen).
- **Motion:** None in the sheet.
- **Construction:** 75 sprites in a TexturePacker sheet, the largest a 1736x704 soft shadow.
- **Notes:** The prize meters use the same five colours as the jackpot money balls, so a ball's label and its meter match by colour.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 35% · saturation 53% · contrast 49% · warm 54% / cool 28% · brighter towards: top (22), top-right (3), top-left (1)
- **Palette (measured):** #1e0b0c black 39%, #964a0d brown 12%, #fefdfd light orange 11%, #53495a grey 8%, #e38f13 orange 5%, #9990a2 grey 4%

### Paytable sheet

`Paytable.desktop` · atlas · 42 parts · largest 739×1020 · sheet `sheets/Paytable.desktop.webp`

- **Role:** The pictures of the payouts pages.
- **Subject:** A tall red banner with a gold top, a green button plaque, a ways diagram with question marks and a pay example (5 - 100, 4 - 25, 3 - 5), green and grey highlight bars, the word FIRECRACKERS, big gold digits 0, 3, 5 and X, small copies of the gong, the emperor, the jackpot balls in gold and green, BONUS SPINS, WILD, MONEY GONG BONUS, the three feature words and small red multiplier tags x2 to x25.
- **Style:** The game's symbols reduced, with plain diagram graphics beside them.
- **Rendering:** Small glossy copies; the diagrams are flat black, white, red and green.
- **Colour:** #430e07 at 38%, #901d05, #fdfcfb, greens #36892a and #6fd859; contrast 0.64.
- **Lighting:** Top-lit copies (measured on 20 parts).
- **Ambience:** Informative; the red and gold stay, the page is otherwise plain.
- **Materials:** As the symbols.
- **Variants:** Jackpot balls in gold and in green, as on the reels.
- **Motion:** None.
- **Construction:** 42 sprites; the banner is 739x1020, the small symbols about 110x110.
- **Notes:** The paytable pages were not reached in play, so their layout and text are not described; only the pictures are read. Multiplier values up to x25 appear here.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 40% · saturation 73% · contrast 64% · warm 74% / cool 14% · brighter towards: top (20), top-left (3)
- **Palette (measured):** #430e07 dark red 38%, #901d05 dark red 12%, #fdfcfb light yellow 10%, #36892a green 4%, #6fd859 green 4%, #3e453b grey 3%

### Feature preview picture

`7651027e388672692afe19dc03fc34f88b87aea5f19aPT_Preview_1-jpg` · atlas · 1 parts · largest 1163×585 · sheet `sheets/7651027e388672692afe19dc03fc34f88b87aea5f19aPT_Preview_1-jpg.webp`

- **Role:** A flattened picture of the intro panel inside a gold border, used in the paytable (by its name PT_Preview; inference).
- **Subject:** The three columns of the intro: firecrackers and the green ball trigger Hold & Win; the gong may award Multiplier, Repeat Pays, Prize Boost or the Money Gong Bonus; each Money Gong Bonus ball awards the Money Gong Bonus.
- **Style:** The intro panel as one image.
- **Rendering:** Flattened; slightly soft from JPEG.
- **Colour:** #640302 at 67%, #b47b28, #981809, #e0c456.
- **Lighting:** As the intro.
- **Ambience:** A summary card.
- **Materials:** None.
- **Variants:** One picture.
- **Motion:** None.
- **Construction:** One JPEG of 1163x585.
- **Notes:** Label text here is yellow and white bold sans capitals, the same as on the live intro screen.
- **Measured:** dark, vivid, warm, high contrast, hard-edged · brightness 23% · saturation 89% · contrast 70% · warm 98% / cool 1%
- **Palette (measured):** #640302 dark red 67%, #b47b28 orange 8%, #981809 red 8%, #e0c456 gold 6%, #8b411f brown 3%, #caa8a7 red 2%


## Typography

Embedded fonts and lettering.

### Money Gong Bonus digits

`MoneyGong.desktop` · atlas · 34 parts · largest 276×276 · sheet `sheets/MoneyGong.desktop.webp`

- **Role:** Two bitmap number fonts for the Money Gong Bonus, with a dark disc and a yellow square.
- **Subject:** A heavy rounded digit set in dark brown with a banded sheen, a cream inner line and an orange outer glow line, with pound, dollar, euro, x, comma and point; and a plain flat yellow set of the same characters.
- **Style:** Poster numerals; the brown set is styled like lacquered wood or bronze.
- **Rendering:** Layered outlines (dark, cream, orange) with a horizontal highlight band; the yellow set is flat.
- **Colour:** #1f0704 at 45%, yellow #fce12a at 28%, #632d14, cream #f9d893, orange #f45b05.
- **Lighting:** A band of light across the middle of each brown digit.
- **Ambience:** Weighty; prize figures that look like objects.
- **Materials:** Lacquer or bronze with a gilt edge.
- **Variants:** Two sets: decorated brown and flat yellow.
- **Motion:** None.
- **Construction:** 34 sprites, digits about 93x140 and 64x98.
- **Notes:** With the white digits of the bonus spins and the magenta and gold digits of the money balls, the game ships five drawn number sets, each for one place.
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
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1127 components cut from 54 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
