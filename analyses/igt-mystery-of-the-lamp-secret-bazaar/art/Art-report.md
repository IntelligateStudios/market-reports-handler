# Mystery Of The Lamp Secret Bazaar: art report

igt · run `2026-11-26-1602-igt-mystery-of-the-lamp-secret-bazaar` · captured 2026-11-26

Source: the provider's free-play demo, https://rgs-awsdemo01.lab.wagerworks.com/skb/gateway?channel=INT&countrycode=GB&currencycode=FPY&language=en&nscode=SKB&skincode=MKW&softwareid=200-1813-001&uniqueid=0&technology=HTML&presenttype=STD

**Extracted:** 1011 named components from 77 textures in 77 atlases; 10 Spine skeletons; 43 frame sequences (664 frames); 10 fonts. Grouped into 77 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

An Arabian-nights market at dusk in red, gold and violet: realistic still-life wares and three gold-mounted gems on a velvet-red board under three glowing bottle lamps, with one friendly 3D genie and coloured smoke as the thread that ties every part together.

**Style.** Painterly realism for the scene and the picture symbols (market goods drawn as still lifes), rendered 3D for everything that moves in space (the genie, lamps, coins, gems, tiles), and ornamental gold scrollwork on deep red for the frame and plaques. The lettering is a family of its own: storybook display scripts with 3D extrusion.

**Rendering.** No outlines anywhere. Objects are softly lit and detailed; each picture symbol sits in a halo of coloured smoke instead of a tile. Gold is thin, crisp and bright; glass buttons and lamps have a hard top highlight. Effects are photographic smoke, fire and lightning added over the art.

**Colour.** Measured over the game's own art, the palette is led by near-black #0a0509 (26%), dark red #501614 (8%) and dark blue-violet #2c2842 (8%), then near-white #f7f8f5 and golds #f6d117 and #f9f15c. On screen the board is deep red with gold, the street warm orange and rose with violet-blue shadow, and the controls violet and blue with yellow glyphs. Colour carries meaning: each picture symbol has one smoke colour (violet, yellow, orange-red, green), each lamp one glass colour (blue Collect, pearl Jackpot, orange Ignite), each of the five prizes one title colour (red Grand, green Major, magenta Maxi, cyan Minor, orange Mini), and magenta-pink is kept for money won (the win frame and the win digits). The bonus cave turns the whole palette cool: blue #474ebe leads it at 56%.

**Lighting.** Two lights in the base scene: warm lantern light from the stalls and the ground, cool dusk from above. Symbols are lit softly from the upper left with their smoke as a back light. Lamps glow from inside. The cave is lit by blue shafts from above.

**Ambience.** A warm, rich evening market with a secret in it; friendly rather than mysterious, because the genie smiles and the smoke is pink. The cave is the cold, magical counter-scene.

**Shape language.** Round and generous: bottle-bellied lamps, dome buttons, coins, cushion and heart-shaped gems, fat rounded royals. The frame answers with thin straight rails ending in curls. Smoke puffs and spirals soften every edge.

**Materials.** Polished and chased gold, red velvet or damask, blown glass, cut gemstones, brass, fruit, olive oil, woven carpet, stone and wood in the street, smoke, fire and lightning.

**Typography and lettering.** Four lettering families, all gold-based. The wordmarks: Mystery of the Lamp in a gold storybook serif with swashes, Secret Bazaar in red and gold slab capitals. The lamp words (Collect, Jackpot, Ignite) in a yellow decorative script with coloured 3D sides. The prize titles in a round seventies-style script, one colour each. Numerals in a tall fat Didone-like serif as bitmap fonts: gold chrome with a coloured edge for each prize, pink chrome for wins, ivory, yellow and orange for coin values. Big-win words are plain fat sans capitals in gold on a deep layered extrusion. Labels (TOTAL BET, WIN, BALANCE) are live text in Oswald; Yeseva One is embedded too.

**Motion.** Spine 4.0 skeletons throughout (18 binary skeleton files, each with an opaque and an alpha page), mixing rigged parts with short frame sequences. The tools here read only JSON skeletons of older versions, so none was drawn, and the 10 skeletons counted at the top of this report are JSON files of a promotional overlay loaded by the demo host (prize tickets, chests, cards), not this game's. What follows is from the frame sequences, the names in the files and the real screens. Reels use pre-blurred copies of every symbol. Gems land wrapped in white lightning and send small gems up to their lamp, whose gold pile grows in three steps. The wild is a rolled carpet that unrolls over 39 frames to show WILD or 2X. Wins darken the board, put a magenta neon frame with a running light on each winning cell and count the amount in pink digits. The genie is a rig with IK that sways over a billowing smoke column, her hands glowing. Smoke (two puffs, many tints) loops behind the logo, the lamp words and the prize plaques. The big-win words are built letter by letter in five tiers; a coin stream and a spinning lamp are the transitions (inference from their skeletons; not reached in play).

**Variants and themes.** Two scenes (bazaar, cave), each in landscape and portrait. Every symbol as a still and a blurred copy; picture symbols also as object and halo apart. One lamp design in three colours, one treasure pile in three sizes for each. One prize plaque in five titles, one numeral face in nine colourings. One button design in four states for every function. One bonus tile in blue and gold.

**How it is built.** 987 named sprites on 54 atlas pages (1,011 components and 77 textures with the fonts, loose pictures and the demo host's overlay), 43 frame sequences holding 664 frames, 4 embedded fonts of the game. The client served its sheets from a folder named mobile: symbol cells are 164x145 and buttons 200x200, close to what a 1280x720 screen shows, while backgrounds are 2040x1410. Whether a larger pack exists for other devices is not known from this capture. Art is split by blend, not by subject: each skeleton has a page of opaque plates for additive light and a page with alpha. Greyscale and white effect art is tinted in the engine. Much is pre-rendered from 3D (gem turns, tile tumbles, word swings, coin flips) rather than rigged.

**Consistency.** High. One palette rule (red and gold board, violet controls, magenta for wins), one material set and one binding motif, smoke, run from the loading picture to the smallest effect. The lettering is the loosest part: five display faces share only their gold. Two file names for symbols do not match their pictures, a trace of an earlier symbol set (inference).

**What to take from it.** (1) Smoke is the system: two white puffs and a spiral, tinted and looped, give the logo, the lamps, the prizes, the symbols' halos and the transitions one common atmosphere at almost no texture cost. (2) Picture symbols need no tile. A soft halo in the symbol's own colour separates it from the board and codes it at a glance; the royals are kept in one red so they recede. (3) Colour is assigned once and reused: one hue per lamp feature, per prize tier and per symbol, and one hue (magenta-pink) reserved for money won. A player can read the state of the game from colour alone. (4) The feature is always on screen: three lamps with growing gold piles sit on the reel frame from the first spin, so the promise of the bonus is part of the base composition, not a separate meter. (5) Split art by blend mode: an opaque page of light effects on black and an alpha page per animation. It keeps files small and is a pattern worth copying in our own pipeline. (6) Pre-rendered 3D in short sequences (11 to 39 frames) does the work of complex rigs for gems, coins, tiles and word turns; only the genie has a real character rig, and even she fakes her turn from rendered views (inference). (7) Build win words from letters with separate extruded backs: five tier titles fit on one small page and can animate letter by letter. (8) For AI-assisted art: the still-life symbols and the two matte-painting scenes are the kind of picture an image model makes well; the value this game adds is in the strict colour coding, the gold ornament drawn clean, and the motion design, which still need an artist's system.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 34% · saturation 55% · contrast 45% · warm 44% / cool 32% · brighter towards: top (81), top-left (66), top-right (41)

Palette: #0a0509 black 26%, #501614 dark red 8%, #2c2842 dark blue 8%, #f7f8f5 light yellow 6%, #f6d117 gold 4%, #f9f15c gold 4%, #7c777e grey 3%, #ecc7bf light red 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 4 | 29% | 62% | 28% | 42% / 54% | #45202c dark red 30%, #474cbc blue 26%, #6c3c4a red 9% |
| Reel board | 6 | 21% | 92% | 54% | 78% / 12% | #360106 black 57%, #6c080a dark red 9%, #e39814 orange 8% |
| Symbols | 10 | 50% | 71% | 61% | 53% / 41% | #2f4988 blue 17%, #faf54e gold 13%, #fac911 gold 10% |
| Characters | 2 | 66% | 18% | 34% | 12% / 34% | #fbf9fc light purple 44%, #29252b grey 20%, #b273f3 purple 14% |
| Logo and title | 2 | 57% | 52% | 54% | 61% / 16% | #fffcfe light magenta 22%, #58271d dark red 14%, #cd8b6a orange 11% |
| Win celebrations and banners | 5 | 63% | 40% | 40% | 56% / 0% | #f9f9f9 white 28%, #632f25 dark red 22%, #fbf061 gold 8% |
| Effects | 22 | 31% | 28% | 38% | 23% / 18% | #050403 black 49%, #f7f8f5 light green 9%, #342e2f grey 7% |
| Game interface | 1 | 15% | 82% | 38% | 20% / 79% | #071026 black 57%, #0a2f62 dark blue 16%, #104ea3 blue 4% |
| Typography | 13 | 50% | 66% | 84% | 91% / 5% | #070403 black 18%, #8c5921 brown 14%, #f7d710 gold 14% |
| Provider interface (shared) | 12 | 31% | 55% | 63% | 25% / 67% | #1b142b dark purple 53%, #fcfcfc white 8%, #f5c85f orange 7% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Base game background (landscape) and layout masks

`default_webp80_jpg-0.84264b` · atlas · 13 parts · largest 2040×1410 · sheet `sheets/default_webp80_jpg-0.84264b.webp`

- **Role:** The scene behind the reels in the base game, on a sheet that also carries the reel masks and the small meter plates.
- **Subject:** A covered bazaar street at dusk: fruit and vegetable stalls, baskets, sacks, clay jars and crates in the foreground, stone arches and awnings behind, lanterns on the walls. No people.
- **Style:** Painterly 3D-looking environment art, realistic in proportion and softened like a matte painting.
- **Rendering:** A single flat picture with soft detail and depth blur toward the back; no outlines. The masks beside it are flat pink, grey and green rectangles, technical pieces and not art.
- **Colour:** Measured over the sheet: dark red-brown #492631 leads (56%), with light red #febebd (the pink mask) second; warm 77% against cool 13%. On screen the street reads orange and rose in the lit foreground against violet-blue shadow.
- **Lighting:** Warm lantern and firelight from the stalls at the sides and the ground, cool blue dusk from the gaps in the awnings above.
- **Ambience:** Evening market after the crowd has gone: warm, rich, slightly secretive.
- **Materials:** Rough stone, wood crates, woven baskets, cloth awnings, clay, fruit.
- **Variants:** A landscape picture here (2040x1410) and a portrait one on its own sheet; the bonus has its own cave scene. The meter plates come as balance, total bet (disabled, enabled, over) and two win-meter backings.
- **Motion:** The picture itself is still. Inference: any movement over it comes from the smoke and star skeletons, not from layers of this picture.
- **Construction:** One 2040x1410 picture with no separate layers, larger than the 1280x720 view so the same file can be cropped for several aspect ratios (inference from its size). Masks: reelMask 852x435, symbol cell 164x145.
- **Notes:** The sheet mixes the background with layout masks; the sorting places it by its largest piece.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 33% · saturation 52% · contrast 38% · warm 77% / cool 13% · brighter towards: top (3), bottom-left (1)
- **Palette (measured):** #492631 dark red 56%, #febebd light red 11%, #817c7e grey 2%

### Base game background (portrait)

`default_webp80_jpg-1.cae779` · atlas · 1 parts · largest 1410×2040 · sheet `sheets/default_webp80_jpg-1.cae779.webp`

- **Role:** The same bazaar scene composed for a tall screen.
- **Subject:** The bazaar street seen in a taller frame: red cloth awnings sweep across the top with blue sky behind, stalls at left and right, an open paved floor in the lower half.
- **Style:** The same painterly 3D-looking environment art as the landscape picture.
- **Rendering:** One flat picture, soft detail, no outlines; the floor is left plain where the reels and controls sit in portrait.
- **Colour:** Measured: dark red #4a202b 51%, red #b84e43 25%, dark magenta #61384c 10%, blue #23397d 7%; warm 76%.
- **Lighting:** Warm light on the floor and stalls, cool blue from the sky and the upper walls.
- **Ambience:** The same evening market, with more sky and more empty floor.
- **Materials:** Stone, cloth, wood, clay, fruit.
- **Variants:** The portrait counterpart of the landscape background. It was loaded by the capture but not shown at 1280x720.
- **Motion:** Still.
- **Construction:** One 1410x2040 picture, the landscape size turned on its side.
- **Notes:** Not seen in play in this run: the capture was landscape only.
- **Measured:** dark, saturated, warm, medium contrast, hard-edged · brightness 26% · saturation 60% · contrast 38% · warm 76% / cool 19% · brighter towards: bottom (1)
- **Palette (measured):** #4a202b dark red 51%, #b84e43 red 25%, #61384c dark magenta 10%, #23397d blue 7%, #f46a53 red 4%

### Bonus background: the treasure cave (landscape)

`default_webp80_jpg-2.242151` · atlas · 1 parts · largest 2040×1410 · sheet `sheets/default_webp80_jpg-2.242151.webp`

- **Role:** The scene of the Mystery of the Lamp bonus (inference from the file set: it sits with the bonus pieces and matches the treasure theme; the bonus was not reached in play).
- **Subject:** The inside of a cave seen through a dark rock opening: shafts of blue light fall on ruined arches and columns, heaps of gold and jewels, and a rock path strewn with coins, gems and a gold lamp leading in.
- **Style:** Painterly fantasy environment, more saturated and more theatrical than the bazaar.
- **Rendering:** One flat picture; the light shafts are painted in, the rock frame is near-black.
- **Colour:** Measured: blue #474ebe 56%, dark blue #30216d 18%, near-black #130b2d 11%, blue #5d6ae2 8%; cool 97%. The only warm notes are the small gold and red jewels on the path.
- **Lighting:** Light comes from above and behind in broad blue-violet shafts; the foreground rock is in shadow.
- **Ambience:** A hidden vault: cold, still, magical. It is the cool opposite of the warm market.
- **Materials:** Wet rock, old masonry, gold coin, cut gems.
- **Variants:** Landscape here, portrait on its own sheet. A separate sprite, greben (2720x1709, on the interface sheet), is the rock ridge with treasure that lies in front of it.
- **Motion:** Still; inference: the star, smoke and diamond pieces of the bonusBgdanim skeleton move over it.
- **Construction:** One 2040x1410 picture plus one large foreground cut-out, so the scene has two depth layers.
- **Notes:** No real screen of this scene in the run.
- **Measured:** mid-tone, vivid, cool, low contrast, hard-edged · brightness 28% · saturation 69% · contrast 16% · warm 2% / cool 97%
- **Palette (measured):** #474ebe blue 56%, #30216d dark blue 18%, #130b2d black 11%, #5d6ae2 blue 8%

### Bonus background: the treasure cave (portrait)

`default_webp80_jpg-3.6aa947` · atlas · 1 parts · largest 1410×2040 · sheet `sheets/default_webp80_jpg-3.6aa947.webp`

- **Role:** The cave scene composed for a tall screen.
- **Subject:** The same cave opening, light shafts and treasure path, with the path running longer toward the viewer.
- **Style:** As the landscape cave.
- **Rendering:** One flat picture.
- **Colour:** Measured: blue #484abc 52%, dark blue #100e30 14% and #1b2762 10%, blue #6466e0 8%, dark purple #461065 4%; cool 94%.
- **Lighting:** Blue-violet shafts from above; dark rock frame.
- **Ambience:** Cold and magical.
- **Materials:** Rock, masonry, gold, gems.
- **Variants:** Portrait counterpart of the landscape cave.
- **Motion:** Still.
- **Construction:** One 1410x2040 picture.
- **Notes:** Not seen in play in this run.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 28% · saturation 70% · contrast 17% · warm 5% / cool 94%
- **Palette (measured):** #484abc blue 52%, #100e30 dark blue 14%, #1b2762 dark blue 10%, #6466e0 blue 8%, #461065 dark purple 4%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Bonus cell tile: the incoming animation

`bonusReels_png.a6b4a7` · atlas · 18 parts · largest 134×113 · sheet `sheets/bonusReels_png.a6b4a7.webp`

- **Role:** The tile that fills a reel cell in the bonus (inference from the names bonusReels and lockRespin; the bonus was not reached).
- **Subject:** A square slab of blue lapis-like stone with a thin gold edge, seen turning in space over 18 frames.
- **Style:** Chunky and tactile, a rendered 3D object.
- **Rendering:** 3D-rendered frames with a crackled surface texture and a bright gold rim; hard edges.
- **Colour:** Measured: blue #1e58da 43% and #144894 31%, dark blue #0b1a3e 5%; cool 89%.
- **Lighting:** Lit from the upper left; the rim catches the light as the slab turns.
- **Ambience:** Solid and precious.
- **Materials:** Lapis or painted stone, gold leaf edge.
- **Variants:** One tile, 18 frames; the skeleton names four animations (incoming from bottom, from top, full, static), read from its file.
- **Motion:** An 18-frame tumble into place.
- **Construction:** A frame sequence about 121x115 driven by a small Spine skeleton (bonusReels).
- **Notes:** Gold counterparts of the tile are on the two main sheets (lockRespinBgGold).
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 34% · saturation 81% · contrast 49% · warm 10% / cool 89% · brighter towards: top (7), top-left (6), right (2)
- **Palette (measured):** #1e58da blue 43%, #144894 blue 31%, #0b1a3e dark blue 5%, #155a66 dark cyan 3%, #4e90f6 blue 2%

### Treasure piles beside the lamps

`coinStates_png.b2a08b` · atlas · 18 parts · largest 246×171 · sheet `sheets/coinStates_png.b2a08b.webp`

- **Role:** The heap of gold at the foot of each lamp, which grows in three steps (inference from the names 1, 2 and 3 _state and the transition animations; one growth step is visible on the Ignite pile in the real screens).
- **Subject:** Heaps of gold coins in stacks and drifts, sprinkled with cut gems: blue gems in the Collect piles, white in the Jackpot piles, yellow in the Ignite piles.
- **Style:** Rendered 3D treasure, dense and sparkling.
- **Rendering:** Many small hard-edged coins with bright rims; tiny gems as accents.
- **Colour:** Measured: orange #f2a724 41% and #d3660e 18%, brown #943a08 17%, gold #fde640 5%; warm 96%.
- **Lighting:** Lit from above; the coin rims flash.
- **Ambience:** Abundance: the visible promise that a feature is close.
- **Materials:** Gold coin, cut gems.
- **Variants:** Three sizes for each of three lamps, nine pictures, plus loose stacks and single gems that fly in.
- **Motion:** The skeleton names states and transitions (1 to 2, 2 to 3, back to 1); loose stacks have three frames.
- **Construction:** Nine pre-rendered piles, the largest 246x171, swapped rather than built coin by coin.
- **Notes:** The file calls the blue pile double; on screen that lamp is labelled Collect.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 55% · saturation 83% · contrast 72% · warm 96% / cool 4% · brighter towards: top (2), right (1)
- **Palette (measured):** #f2a724 orange 41%, #d3660e orange 18%, #943a08 brown 17%, #450b02 dark red 5%, #fde640 gold 5%, #f9e595 light gold 2%

### The Collect lamp (blue), in parts

`lamps_2_png.39e731` · atlas · 4 parts · largest 159×111 · sheet `sheets/lamps_2_png.39e731.webp`

- **Role:** The lamp of the Collect feature, left of the three.
- **Subject:** The same bottle lamp in deep blue glass with a cyan inner glow.
- **Style:** As the orange lamp.
- **Rendering:** Smooth gradients, bright cyan core, crisp edges.
- **Colour:** Measured: blue #1944f4 39%, dark blue #051192 17%, cyan #0de8fd 14%; fully cool.
- **Lighting:** Lit from inside, cyan at the centre.
- **Ambience:** Cool and electric.
- **Materials:** Glass.
- **Variants:** Blue variant of the lamp; only the glass parts are here, the gold bands are shared with the orange sheet (inference from the part names).
- **Motion:** In the real screens a blue swirl of smoke turns above it behind the word Collect.
- **Construction:** 4 parts.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 34% · saturation 90% · contrast 58% · warm 0% / cool 100% · brighter towards: bottom (1), top (1), bottom-right (1)
- **Palette (measured):** #1944f4 blue 39%, #051192 dark blue 17%, #0de8fd cyan 14%, #0a13d7 blue 10%, #4c7efd blue 10%, #0fa6fd blue 5%

### The Jackpot lamp (pearl white), in parts

`lamps_3_png.a6ae86` · atlas · 4 parts · largest 159×112 · sheet `sheets/lamps_3_png.a6ae86.webp`

- **Role:** The lamp of the Jackpot feature, in the middle of the three.
- **Subject:** The same bottle lamp in milky pearl glass with a warm light inside and a mauve shadow side.
- **Style:** As the other lamps.
- **Rendering:** Soft gradients from cream to mauve; the neck is a pale flared tube.
- **Colour:** Measured: mauve #8a5e75 28%, peach #c89782 22%, sand #eac385 16%, orange #ad6e30 15%, cream #f6ebc5 13%.
- **Lighting:** Lit from inside and slightly from the front.
- **Ambience:** Soft and precious, the calmest of the three.
- **Materials:** Opal or pearl glass.
- **Variants:** White variant of the lamp.
- **Motion:** In the real screens pink smoke rises behind the word Jackpot above it.
- **Construction:** 4 parts.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged, strong highlights · brightness 60% · saturation 40% · contrast 48% · warm 87% / cool 0% · brighter towards: bottom-left (3)
- **Palette (measured):** #8a5e75 magenta 28%, #c89782 orange 22%, #eac385 orange 16%, #ad6e30 orange 15%, #f6ebc5 light gold 13%, #fbf2f7 light magenta 2%

### The Ignite lamp (orange), in parts

`lamps_png.254a83` · atlas · 13 parts · largest 160×112 · sheet `sheets/lamps_png.254a83.webp`

- **Role:** One of the three lamps that stand on top of the reel frame all through the base game; this one carries the Ignite feature.
- **Subject:** A round-bellied bottle lamp in glowing orange glass with spiral gold bands, a short neck, a gold foot and rings, cut into parts.
- **Style:** Stylised and jewel-like; a 3D-looking object painted smooth.
- **Rendering:** Smooth gradients with a bright inner glow in the glass and thin, crisp gold bands; no outline.
- **Colour:** Measured: orange #f16222 44% and #f5ba1e 32%, brown #703103 9%; fully warm.
- **Lighting:** Lit from inside: the belly is brightest at its centre, as if a flame sat in it.
- **Ambience:** Warm, lively, a little dangerous.
- **Materials:** Blown glass, gold wire.
- **Variants:** The same construction in three colours: orange here, blue (Collect) and pearl white (Jackpot) on their own sheets.
- **Motion:** In the real screens the lamp sits still with a flame above it and its gold pile beside it; the skeleton lists tension and jump animations (read from its file, not drawn).
- **Construction:** 13 parts (belly, bands, neck, foot rings in three frames, top pieces) for one Spine 4.0 skeleton, lamps, that holds all three lamps. A path string inside that skeleton names the sibling game Treasure Oasis, which suggests the lamp rig is shared with it (inference).
- **Notes:** The skeleton is binary Spine 4.0 and was not drawn by the tools: the real screens show the lamp whole.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 55% · saturation 88% · contrast 38% · warm 100% / cool 0% · brighter towards: top (1), bottom (1)
- **Palette (measured):** #f16222 orange 44%, #f5ba1e orange 32%, #703103 brown 9%, #d08d06 orange 6%, #a85a07 brown 5%, #f07758 red 3%

### Reel frame, reel backing, prize plaques and the large buttons

`default_webp80_png-1.22aa5a` · atlas · 48 parts · largest 1425×833 · sheet `sheets/default_webp80_png-1.22aa5a.webp`

- **Role:** What holds the symbols and the five prize meters; the sheet also carries the big round buttons, the royal symbols and some bonus tiles.
- **Subject:** A thin gold reel frame with four dividers and curled finials (893x487), a dark red damask backing in five panels, a darkening plate, five prize plaques named Grand, Major, Maxi, Mini and Minor, the intro panel's shaped backing, and the spin, play, skip and stop buttons as glass domes in gold rings.
- **Style:** Ornamental and theatrical: Art Nouveau-like gold scrollwork on deep red, with glossy jewel buttons.
- **Rendering:** Clean vector-like shapes with painted gradients. The frame is a thin line of gold with red inlay; the plaques have a bevelled gold edge and a mottled red field; the buttons have a hard specular highlight on a violet-to-blue dome.
- **Colour:** Measured over the sheet: near-black red #360106 63%, dark red #6c070a 10%, orange #e09a12 6%, gold #fbee31 3%; warm 81%. Each plaque title has its own colour: red Grand, green Major, magenta Maxi, orange Mini, cyan Minor. The buttons are violet and blue with yellow glyphs.
- **Lighting:** Even, frontal light; highlights sit at the top of the button domes and along the upper edge of the gold.
- **Ambience:** A velvet-lined jewel case: rich and formal.
- **Materials:** Polished gold, red velvet or damask, glass.
- **Variants:** Five plaques that differ only in the title lettering and its two jewels. Spin button in disabled, enabled, over and pressed; play, skip and slam-stop buttons in the same family. Royals (A, K, Q, J, 9) each as a still and a motion-blurred copy.
- **Motion:** On a win the symbols off the line are darkened (the reel_darken plate, seen in the real screens). The blue and gold tiles on this sheet are frames of the bonus's cell turn (16 frames here, more on the symbols sheet).
- **Construction:** Frame and backing are separate pieces so the backing can stay while symbols pass behind the frame. The plaques are 955x423 each, far larger than they are shown (about 330 wide at 1280x720).
- **Notes:** A mixed sheet: the sorting places it with the reel board.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 18% · saturation 93% · contrast 54% · warm 81% / cool 8% · brighter towards: top (15), top-left (9), bottom-left (2)
- **Palette (measured):** #360106 black 63%, #6c070a dark red 10%, #e09a12 orange 6%, #fbee31 gold 3%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Lamp coin flame (additive plates)

`coinIgnite_jpg.c83f33` · atlas · 16 parts · largest 299×344 · sheet `sheets/coinIgnite_jpg.c83f33.webp`

- **Role:** The same flame as opaque plates on black, with a light sweep.
- **Subject:** A yellow-white flame on black in 15 frames and a diagonal white light sweep.
- **Style:** Photographic effect.
- **Rendering:** Bright on black for additive blending.
- **Colour:** Measured: gold #f9f64e 41%, orange #eaa620 22%, brown #894a0d 15%.
- **Lighting:** Self-lit.
- **Ambience:** Hot.
- **Materials:** Fire.
- **Variants:** One sequence, one sweep.
- **Motion:** 15 frames.
- **Construction:** The flame exists twice, once with alpha and once on black, so it can be drawn solid and then brightened.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 68% · saturation 77% · contrast 58% · warm 99% / cool 0%
- **Palette (measured):** #f9f64e gold 41%, #eaa620 orange 22%, #894a0d brown 15%, #1f1004 black 5%, #da670c orange 5%, #fdfaa5 light gold 3%

### Lamp coin with flame (alpha parts)

`coinIgnite_png.916965` · atlas · 18 parts · largest 236×319 · sheet `sheets/coinIgnite_png.916965.webp`

- **Role:** The coin symbol and its burning state for the Ignite feature (inference from the name coinIgnite).
- **Subject:** The gold coin embossed with a lamp inside a ring of flame shapes, a grey stone-like copy of it, and a tall yellow-orange flame in 15 frames.
- **Style:** The coin is a chunky rendered object; the flame is photographic.
- **Rendering:** Hard-edged coin with deep relief; soft flame.
- **Colour:** Measured: gold #fef94f 39%, orange #f88312 36% and #fdc124 12%; warm 99%.
- **Lighting:** The flame lights itself; the coin is lit from the upper left.
- **Ambience:** Heat and value together.
- **Materials:** Gold, stone (the grey copy), fire.
- **Variants:** Coin in gold and in grey; one flame sequence.
- **Motion:** 15-frame flame; the skeleton names a loop and two static states.
- **Construction:** Coin 124x120; flame frames up to 260x288, more than twice the coin.
- **Notes:** The grey coin was not seen in play.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 75% · saturation 77% · contrast 49% · warm 100% / cool 0% · brighter towards: top-right (2)
- **Palette (measured):** #fef94f gold 39%, #f88312 orange 36%, #fdc124 orange 12%, #fefaa6 light gold 3%, #f8ac66 orange 2%, #b6a687 orange 2%

### Blue gem: the spin sequence

`symbolAnims_2_png.734216` · atlas · 17 parts · largest 161×161 · sheet `sheets/symbolAnims_2_png.734216.webp`

- **Role:** The blue gem turning when it is collected.
- **Subject:** The blue cushion-cut gem in its gold mount, shown rotating about its upright axis.
- **Style:** Rendered 3D object.
- **Rendering:** 17 pre-rendered frames with correct perspective and moving reflections.
- **Colour:** Measured: brown-gold #914904 19%, blues #0d2691 and #0840e9 14% each, orange #d67708 12%, gold #fee90b 6%.
- **Lighting:** Top-left light, reflections travel across the facets.
- **Ambience:** A jewel shown off.
- **Materials:** Sapphire-like stone, gold.
- **Variants:** One gem, 17 frames.
- **Motion:** A full turn in 17 frames; in the real screens the landed gems are wrapped in white lightning and send sparks up to the lamps.
- **Construction:** Frame sequence about 160 square.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 41% · saturation 87% · contrast 71% · warm 50% / cool 50% · brighter towards: top-left (9), top-right (4), top (3)
- **Palette (measured):** #914904 brown 19%, #0d2691 blue 14%, #0840e9 blue 14%, #d67708 orange 12%, #fee90b gold 6%, #f6a80f orange 6%

### Grey diamond sequence

`symbolAnims_3_png.833faf` · atlas · 11 parts · largest 153×117 · sheet `sheets/symbolAnims_3_png.833faf.webp`

- **Role:** A neutral diamond that tumbles, drawn in grey so it can be tinted (inference from its colourless frames and the name double_diamond).
- **Subject:** A brilliant-cut diamond seen from the side, rotating.
- **Style:** Rendered 3D object.
- **Rendering:** 11 frames, faceted, in greys only.
- **Colour:** Measured: greys #8d8d8d 70% and #c5c5c5 26%; no hue.
- **Lighting:** Top-left light.
- **Ambience:** Neutral.
- **Materials:** Cut stone.
- **Variants:** One stone, 11 frames; small coloured copies (gold, cyan, white) are in the bonus sheets.
- **Motion:** An 11-frame tumble.
- **Construction:** Greyscale art tinted in the engine is cheaper than three coloured sets.
- **Measured:** bright, muted, neutral, medium contrast, hard-edged · brightness 63% · saturation 0% · contrast 39% · warm 0% / cool 0% · brighter towards: top-left (11)
- **Palette (measured):** #8d8d8d grey 70%, #c5c5c5 grey 26%, #ebebeb white 4%

### Royals, gems and wild: the stills used by the symbol skeleton

`symbolAnims_4_png.a67688` · atlas · 10 parts · largest 164×145 · sheet `sheets/symbolAnims_4_png.a67688.webp`

- **Role:** The still pictures the win animations start from.
- **Subject:** A, K, Q, J, 10 and 9 as fat red letters with a gold edge; the three gems in their mounts; the carpet wild unrolled in its frame.
- **Style:** Royals in a rounded, slightly Art Nouveau display face; gems and wild realistic.
- **Rendering:** The letters are glossy red enamel with a mottled inner texture, a thin gold bevel and a small white glint; no black outline.
- **Colour:** Measured: red #a2140e 17%, orange #eb700e 15%, brown #914f06 8%, red #cc4d34 5%, with blue #094ced from the blue gem; warm 78%.
- **Lighting:** Top-left key light, a glint on each letter.
- **Ambience:** The royals stay quiet and uniform so the pictures and gems stand out.
- **Materials:** Enamel, gold, gemstone, carpet.
- **Variants:** Six royals all in the same red, told apart by shape only; three gems; one wild.
- **Motion:** Inference: the skeleton scales and shines these stills on a win; the real win screen shows winning symbols bright while the others darken.
- **Construction:** 10 stills at the cell size 164x145.
- **Notes:** All six royals share one colour, which is unusual: most games give each royal its own hue.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 46% · saturation 78% · contrast 73% · warm 78% / cool 21% · brighter towards: top (2), top-left (1), bottom-left (1)
- **Palette (measured):** #a2140e red 17%, #eb700e orange 15%, #914f06 brown 8%, #cc4d34 red 5%, #f5c08f light orange 5%, #f1f0eb light yellow 5%

### Wild 2X: unroll and loop

`symbolAnims_5_png.b80c34` · atlas · 39 parts · largest 194×172 · sheet `sheets/symbolAnims_5_png.b80c34.webp`

- **Role:** The wild that doubles: the carpet unrolls to show 2X.
- **Subject:** The rolled carpet in its oval gold frame opens flat, and a large yellow 2X with a magenta edge appears on it in a burst of cyan lightning.
- **Style:** Realistic prop with cartoon-bold lettering.
- **Rendering:** 39 pre-rendered frames; the lettering has a thick bevel and the lightning is soft cyan glow.
- **Colour:** Measured: blue #29639a 20%, dark blue #1a144c 13%, gold #fde208 8%, cyan #4bbddf 8%, purples #48197a and #8f20d7.
- **Lighting:** The lettering is self-lit; cyan rim light from the lightning.
- **Ambience:** A reveal: the carpet is the flying carpet of the tale.
- **Materials:** Woven carpet with tassels, gold frame.
- **Variants:** Two versions of the same reveal: 2X here and WILD on the next sheet.
- **Motion:** 39 frames: rolled, unrolling, flash, lettering held. The real screen shows the 2X standing on the reels after it lands.
- **Construction:** Full frame sequence up to 194x172, larger than the cell so the burst can overlap neighbours.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 41% · saturation 76% · contrast 77% · warm 37% / cool 59% · brighter towards: top (6)
- **Palette (measured):** #29639a blue 20%, #1a144c dark blue 13%, #fde208 gold 8%, #4bbddf cyan 8%, #48197a dark purple 7%, #f09513 orange 6%

### Wild: unroll and loop

`symbolAnims_6_png.5bf966` · atlas · 39 parts · largest 194×172 · sheet `sheets/symbolAnims_6_png.5bf966.webp`

- **Role:** The plain wild: the carpet unrolls to show WILD.
- **Subject:** The same carpet and frame; the word WILD in yellow with a red-magenta edge appears in cyan lightning.
- **Style:** As the 2X wild.
- **Rendering:** 39 pre-rendered frames.
- **Colour:** Measured: blue #315695 20%, dark blue #181949 8%, gold #fee90b 8%, red #87153a 6%, cyan #57caeb 6%, purples #3d1277 and #8b1ae1.
- **Lighting:** Self-lit lettering, cyan rim.
- **Ambience:** The same reveal.
- **Materials:** Carpet, gold.
- **Variants:** Twin of the 2X sequence.
- **Motion:** 39 frames, intro then loop (the folder is named wdIntroAndLoop).
- **Construction:** A second full sequence instead of swapping only the lettering: simple to make, heavy in texture.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 40% · saturation 75% · contrast 73% · warm 38% / cool 57% · brighter towards: top (4)
- **Palette (measured):** #315695 blue 20%, #181949 dark blue 8%, #fee90b gold 8%, #87153a red 6%, #57caeb cyan 6%, #3d1277 dark purple 5%

### Symbol effects: collect vortex, landing burst, stars

`symbolAnims_jpg.b745ff` · atlas · 43 parts · largest 298×191 · sheet `sheets/symbolAnims_jpg.b745ff.webp`

- **Role:** Light effects played over symbols.
- **Subject:** A blue-white spiral vortex on black (collectTwist, 22 frames), a small white burst (IntroBurst, 16 frames), a star field, a lens flare and green mask rectangles.
- **Style:** Photographic effect plates.
- **Rendering:** Bright shapes on black, made to be added to the picture beneath.
- **Colour:** Measured: blue #334784 41%, light cyan #ebf7fa 13%, near-black; the green #30fe02 is the masks, not art.
- **Lighting:** Self-lit.
- **Ambience:** Electric magic.
- **Materials:** Light, vapour.
- **Variants:** Two sequences and three single plates.
- **Motion:** 22-frame vortex and 16-frame burst.
- **Construction:** Opaque pages (the file calls them jpg) for additive effects, kept apart from the alpha pages: a clear, economical split used all through this game.
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged, strong highlights · brightness 43% · saturation 47% · contrast 58% · warm 0% / cool 90%
- **Palette (measured):** #334784 blue 41%, #ebf7fa light cyan 13%, #0b0f1a black 10%, #222a44 dark blue 9%, #acc8ef light blue 7%, #7995e1 blue 7%

### Picture symbols on clear ground and their four smoke swirls

`symbolAnims_png.9d9285` · atlas · 12 parts · largest 164×145 · sheet `sheets/symbolAnims_png.9d9285.webp`

- **Role:** The layers of the four picture symbols for their win animation.
- **Subject:** Bracelets (S01), a tray of brass pots (S02_Tray), pomegranates (S03_Axe by file name) and the oil and olives (S04_Lantern by file name), each without its halo, plus four spiral smoke swirls in purple, green, red-orange and yellow, a white puff and two small lightning strokes for the gems.
- **Style:** Realistic objects; the swirls are soft painted vortices.
- **Rendering:** Objects cut clean on transparency; swirls are soft-edged spirals meant to turn behind them.
- **Colour:** Measured: orange #dfae29 18%, purple #a619fc 13%, orange #f86007 12%, green #08cc6f 10%.
- **Lighting:** Objects lit from the upper left; swirls self-lit.
- **Ambience:** Each ware gets its own little magic storm.
- **Materials:** Brass, gold, fruit, glass; smoke.
- **Variants:** Four objects and four swirls, paired by colour: purple S01, green S02, red S03, yellow S04.
- **Motion:** Inference from the layering: on a win the swirl turns behind the object; in the real win screen the bracelets sit in a brighter violet cloud.
- **Construction:** Object and halo are separate here, while the reel still has them baked together.
- **Notes:** Two file names (Axe, Lantern) do not match what is drawn (pomegranates, oil and olives): they look like names kept from an earlier symbol set (inference). The numbers also differ from the reel sheet, where s02 is the oil and olives and s04 the brass pots.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 49% · saturation 74% · contrast 43% · warm 60% / cool 23% · brighter towards: top (3), right (1), top-right (1)
- **Palette (measured):** #dfae29 orange 18%, #a619fc purple 13%, #f86007 orange 12%, #08cc6f green 10%, #050302 black 6%, #fefcf9 light orange 5%

### Reel symbols as shown on the reels (pictures, gems, coin, wild)

`default_webp80_png-2.97b1a2` · atlas · 66 parts · largest 846×397 · sheet `sheets/default_webp80_png-2.97b1a2.webp`

- **Role:** The reel pictures of the four picture symbols, the three gems, the lamp coin and the rolled-carpet wild; the sheet also holds the 10, the small buttons and bonus tile frames.
- **Subject:** A bowl of pomegranates (s03), brass spice pots (s04), a tray with an oil bottle and olives (s02), three gems in gold mounts (b01 blue cushion, b02 orange shield-heart, b03 white round), a gold coin embossed with the lamp (c01) and a rolled carpet in a gold frame (w01).
- **Style:** Realistic still-life objects, painted with photographic detail, each sitting in its own cloud of coloured smoke.
- **Rendering:** Detailed, softly lit rendering without outlines; the smoke halo behind each picture fades to nothing, so the symbol has no hard cell edge. Gems are faceted with sharp white reflections.
- **Colour:** Measured over the sheet: gold #fbc80b 27%, dark red #470304 22%, blue #164ba0 14%, orange #ee8c09 7%, blue #2264f1 4%. Each picture symbol owns one halo colour: orange-red for the pomegranates, green for the spice pots, yellow for the olives, violet for the bracelets (on the other sheet).
- **Lighting:** Soft light from the upper left on the objects; the halo glows behind them as a back light.
- **Ambience:** Market goods as treasures: appetising, warm, precious.
- **Materials:** Fruit skin and seeds, brass, glass and oil, cut gemstone, chased gold, woven carpet.
- **Variants:** Every symbol in two pictures, a still (_static) and a vertically motion-blurred copy (_blur) for the spinning reel. Three gems that differ in cut, mount and colour.
- **Motion:** While the reels turn the blurred copies are shown (seen in the real screens). The blue and gold tiles are 44 frames of the bonus cell turning.
- **Construction:** Symbols are about 150 to 164 wide by 130 to 145 high, close to the size shown on a 1280x720 screen (about 130): the pack the client loaded is small. Blur is pre-rendered, not a shader.
- **Notes:** A mixed sheet: the sorting places it with the symbols.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 44% · saturation 87% · contrast 52% · warm 70% / cool 29% · brighter towards: top (16), top-left (9), right (4)
- **Palette (measured):** #fbc80b gold 27%, #470304 dark red 22%, #164ba0 blue 14%, #ee8c09 orange 7%, #2264f1 blue 4%, #f9e75a gold 2%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The genie's light effects

`genieAnims_jpg.ea4835` · atlas · 19 parts · largest 187×202 · sheet `sheets/genieAnims_jpg.ea4835.webp`

- **Role:** Glow and stars that go with the genie.
- **Subject:** Two star fields, a round pink-white glow and a 16-frame sparkle cluster for her hands.
- **Style:** Effect plates.
- **Rendering:** White shapes on black for additive blending.
- **Colour:** Measured: greys and white only (#f1eff0, #aaa8a9), almost no hue; the pink is added by tint.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle and enchantment.
- **Materials:** Light.
- **Variants:** Three plates and one sequence.
- **Motion:** 16-frame hand glow, seen as the white puffs at her palms in the intro screens.
- **Construction:** Opaque page beside the alpha page of the same skeleton.
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 57% · saturation 2% · contrast 57% · warm 11% / cool 0%
- **Palette (measured):** #f1eff0 white 34%, #1c1b1c black 24%, #aaa8a9 grey 23%, #5f5f5f grey 15%

### The genie, in parts

`genieAnims_png.d02b8a` · atlas · 37 parts · largest 695×561 · sheet `sheets/genieAnims_png.d02b8a.webp`

- **Role:** The game's one character: she presents the intro panel and (inference from the animation set) the bonus.
- **Subject:** A young woman genie with violet skin, pointed ears, a long black ponytail bound in gold, a red-jewelled gold circlet, a white top trimmed in gold and gold bracelets, holding a teal and gold oil lamp; below the waist she is a column of pink smoke.
- **Style:** Stylised 3D character in the manner of an animated feature film: large eyes, smooth simplified anatomy, friendly expression.
- **Rendering:** Smooth 3D-looking shading with soft gradients and thin bright gold lines; no outline. The parts come from 3D renders of the figure at several angles.
- **Colour:** Measured over the parts: near-white #fcfafe 50% (smoke and top), violet #b273f3 18%, dark grey-violet #2d2730 18% (hair). On screen: violet skin, white and gold dress, pink smoke, teal lamp.
- **Lighting:** Soft front light with a cool rim; her hands carry a white glow.
- **Ambience:** Warm and welcoming, a hostess more than a spirit.
- **Materials:** Skin, hair, silk, gold, enamelled lamp, smoke.
- **Variants:** One character, one costume. The body, head, hair, arms, forearms and hands each exist as front, back and side views (F_, B_, L_, R_), and the right hand has a click pose in two stages.
- **Motion:** Seen in the real intro screens: she sways, her smoke column billows and her hands glow. The skeleton lists IK controls for spine, neck, head, hair and legs, and precog star effects (read from its file, not drawn).
- **Construction:** 37 parts for one Spine 4.0 skeleton (binary, about 447 KB), genieAnims. The torso is cut into narrow vertical strips (about 80 to 94 by 577) of different views, which suggests the rig turns her body by cross-fading or deforming rendered views: a fake 3D turn (inference).
- **Notes:** The tools cannot draw this skeleton, so no assembled frame is published; the intro screens show her whole.
- **Measured:** bright, muted, warm and cool mixed, medium contrast, strong highlights · brightness 70% · saturation 23% · contrast 26% · warm 12% / cool 44% · brighter towards: bottom-right (5), bottom (2), bottom-left (2)
- **Palette (measured):** #fcfafe light purple 50%, #b273f3 purple 18%, #2d2730 grey 18%, #ddc6ef light purple 2%


## Logo and title

The game's own wordmark.

### Loading picture: genie, lamp and both wordmarks

`adb31342e428182ac8c4` · atlas · 1 parts · largest 779×557 · sheet `sheets/adb31342e428182ac8c4.webp`

- **Role:** The key art shown while the game loads.
- **Subject:** The violet-skinned genie in a white and gold top holds up the teal and gold lamp; she rises from a purple ribbon of smoke over the bazaar stalls, with the wordmark Mystery of the Lamp in gold and Secret Bazaar in red and gold below, all in a pink cloud vignette.
- **Style:** Stylised 3D character art over a painted scene; lettering in a storybook display style.
- **Rendering:** Smooth 3D-looking shading on the figure, heavy bevel and extrusion on the letters, sparkles and soft smoke around the edge.
- **Colour:** Measured: dark red-brown #58271d 19%, peach #cd8b6a 15%, brown #a2470d 9%, orange #ebab17 8%, rose #e84c7b 7%, pinks #f2b5cf and #fbe2f3, gold #fbe042; warm 83%.
- **Lighting:** Warm light from the front and below; the smoke glows pink behind.
- **Ambience:** Inviting and playful: a friendly genie, not a menacing one.
- **Materials:** Skin, silk, gold, enamel on the lamp, smoke.
- **Variants:** One picture, 779x557.
- **Motion:** Still.
- **Construction:** A single PNG shipped by the game's launcher, apart from the atlases.
- **Notes:** The only place where the genie, the lamp and both wordmarks appear together.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 47% · saturation 64% · contrast 70% · warm 83% / cool 13%
- **Palette (measured):** #58271d dark red 19%, #cd8b6a orange 15%, #a2470d brown 9%, #ebab17 orange 8%, #e84c7b red 7%, #f2b5cf light magenta 4%

### Logo effects: smoke and ribbon

`Logo_export_png.7ca5f3` · atlas · 4 parts · largest 417×298 · sheet `sheets/Logo_export_png.7ca5f3.webp`

- **Role:** The moving dressing behind the logo.
- **Subject:** A white smoke puff, a pair of violet brush-stroke ribbons and two tiny sparks.
- **Style:** Soft effect art.
- **Rendering:** Soft-edged alpha shapes meant to be tinted and layered.
- **Colour:** Measured: white with violet #7522cc 20%. On screen the smoke is tinted pink-magenta.
- **Lighting:** Self-lit.
- **Ambience:** Magic smoke, the genie's trail.
- **Materials:** Smoke, light.
- **Variants:** One puff reused many times at different sizes (the skeleton lists a dozen smoke slots).
- **Motion:** In the real screens the pink cloud drifts behind the logo and the logo alternates between the two wordmarks, Mystery of the Lamp and Secret Bazaar.
- **Construction:** 4 parts for the Logo_export skeleton; the two wordmarks themselves are stills on the interface sheet (388x86 and 173x70).
- **Measured:** bright, muted, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 83% · saturation 19% · contrast 10% · warm 0% / cool 24% · brighter towards: bottom-right (1)
- **Palette (measured):** #ffffff light purple 76%, #7522cc purple 20%, #a96ce3 purple 2%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Big win rays (additive)

`bigWinRaysAnims_jpg.090089` · atlas · 1 parts · largest 246×240 · sheet `sheets/bigWinRaysAnims_jpg.090089.webp`

- **Role:** The fan of light behind a big win.
- **Subject:** A fan of yellow rays opening upward from a point, on black.
- **Style:** Effect plate.
- **Rendering:** Soft rays on black for additive blending.
- **Colour:** Measured: gold-brown #a28614 41%, #52440a 26%, gold #e7c01d 14%.
- **Lighting:** Self-lit from the base of the fan.
- **Ambience:** Stage light.
- **Materials:** Light.
- **Variants:** One plate, 246x240, scaled up.
- **Motion:** The skeleton names two looping ray animations.
- **Construction:** A small plate stretched over the screen.
- **Notes:** Not seen in play in this run.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 39% · saturation 85% · contrast 42% · warm 100% / cool 0%
- **Palette (measured):** #a28614 brown 41%, #52440a brown 26%, #141103 black 20%, #e7c01d gold 14%

### Big win rays: beam, sparkle and ray

`bigWinRaysAnims_png.109b6f` · atlas · 3 parts · largest 200×200 · sheet `sheets/bigWinRaysAnims_png.109b6f.webp`

- **Role:** White shapes tinted for the big win.
- **Subject:** A white cone of light, a four-point sparkle and a thin vertical ray.
- **Style:** Effect parts.
- **Rendering:** Soft white alpha shapes.
- **Colour:** Measured: white only; colour comes from tint.
- **Lighting:** Self-lit.
- **Ambience:** Glitter.
- **Materials:** Light.
- **Variants:** Three parts; the skeleton places about 60 sparkles.
- **Motion:** Sparkles twinkle and rays loop (read from the skeleton's names).
- **Construction:** Three tiny textures for a full-screen effect.
- **Notes:** Not seen in play in this run.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Big win lettering, letter by letter

`bigWinTextsAnims_png.862f1f` · atlas · 65 parts · largest 742×126 · sheet `sheets/bigWinTextsAnims_png.862f1f.webp`

- **Role:** The words of the win tiers, built from single letters.
- **Subject:** Fat sans-serif capitals in yellow-to-gold with a white top edge, and for each letter a separate back piece: a deep stack of red-brown and gold outlines that gives the letter a long 3D extrusion seen from an angle.
- **Style:** Retro show lettering: a flat bright face on a layered, almost neon-sign extrusion.
- **Rendering:** Flat gradient faces with a crisp rim; the backs are concentric outlines stepping away in perspective.
- **Colour:** Measured: dark red #6b2d24 34%, orange-brown #a2552d 19%, gold #fbf061 16% and #f5c81f 12%, orange #d8a240 12%; warm 99%.
- **Lighting:** The faces are lit from above (white at the top, deep gold below); the extrusions glow from inside.
- **Ambience:** Loud, golden, celebratory.
- **Materials:** Polished gold face, lacquered sides.
- **Variants:** Five tiers named in the skeleton: big, huge, massive, extraordinary and spectacular win. Letters are reused between words; several letters have two or three back pieces for different angles.
- **Motion:** Inference from the parts: letters fly in on their extrusions and a light sweep crosses them. No big win came in play.
- **Construction:** 65 parts (about 100 to 150 pixels a letter) and one Spine 4.0 skeleton; building words from letters keeps five tier titles on one 997x997 page.
- **Notes:** Not seen in play in this run.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 51% · saturation 68% · contrast 48% · warm 99% / cool 0% · brighter towards: top-right (20), top-left (10), top (7)
- **Palette (measured):** #6b2d24 dark red 34%, #a2552d orange 19%, #fbf061 gold 16%, #f5c81f gold 12%, #d8a240 orange 12%, #b58041 orange 4%

### Prize meter orb

`jackpotCounterAnims_jpg.284887` · atlas · 6 parts · largest 200×200 · sheet `sheets/jackpotCounterAnims_jpg.284887.webp`

- **Role:** A flash of light on a prize meter.
- **Subject:** A white ball of light with fine lightning threads, on black, in 6 frames.
- **Style:** Effect plate.
- **Rendering:** Bright core, thin crackles, additive.
- **Colour:** Measured: greys and white only.
- **Lighting:** Self-lit.
- **Ambience:** A spark of magic.
- **Materials:** Light.
- **Variants:** One 6-frame sequence.
- **Motion:** 6 frames.
- **Construction:** 200x200 plates.
- **Notes:** Not seen in play in this run.
- **Measured:** mid-tone, muted, neutral, high contrast, hard-edged, strong highlights · brightness 56% · saturation 0% · contrast 63% · warm 0% / cool 0%
- **Palette (measured):** #a8a8a8 grey 32%, #393939 grey 28%, #ebebeb white 26%, #707070 grey 12%, #090909 black 3%

### Prize names: Mini, Minor, Maxi, Major, Grand

`jackpotCounterAnims_png.fdf5c0` · atlas · 12 parts · largest 683×535 · sheet `sheets/jackpotCounterAnims_png.fdf5c0.webp`

- **Role:** The titles of the five prize meters, with a white copy of each for a flash.
- **Subject:** Five words in a round, heavy script with curled initials, each in its own colour with a darker extrusion: orange Mini, cyan Minor, magenta Maxi, green Major, red Grand; plus two smoke puffs.
- **Style:** Seventies-style display script, playful and soft.
- **Rendering:** Bevelled faces with a gradient and a dark offset shadow side; the white copies are flat silhouettes.
- **Colour:** Measured over the sheet: mostly white (#fafafa 86%) because of the smoke and the white copies. The five tier colours are read from the sheet, not measured one by one.
- **Lighting:** Top light on the letters.
- **Ambience:** Friendly, a little retro.
- **Materials:** Enamel lettering; smoke.
- **Variants:** Five tiers, each coloured and white (Add).
- **Motion:** Inference: the white copy flashes over the coloured one when a prize is awarded, with smoke in the tier's colour (the fgSmoke skeleton names grand, major, minor, purple, green, yellow and white smokes).
- **Construction:** 12 parts for the jackpotCounterAnims skeleton; words about 210 to 224 wide.
- **Notes:** Five tiers, where many hold-and-win games have four.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 92% · saturation 8% · contrast 10% · warm 6% / cool 2% · brighter towards: top (2), top-right (1)
- **Palette (measured):** #fafafa white 86%, #d1d0d0 grey 3%


## Effects

Frame sequences, glows, particles and transitions.

### Collect vortex

`bonusBgdanim_2_jpg.dda721` · atlas · 22 parts · largest 298×191 · sheet `sheets/bonusBgdanim_2_jpg.dda721.webp`

- **Role:** The blue vortex of the Collect feature.
- **Subject:** A blue-white spiral of vapour on black, 22 frames.
- **Style:** Photographic effect.
- **Rendering:** Additive.
- **Colour:** Measured: blue #334785 46%, light cyan #ebf7fa 15%, dark blue #151e38 14%.
- **Lighting:** Self-lit.
- **Ambience:** Pulling in.
- **Materials:** Vapour.
- **Variants:** One sequence; the same frames are packed with the symbol effects.
- **Motion:** 22 frames.
- **Construction:** 298x191 plates.
- **Measured:** mid-tone, saturated, cool, high contrast, hard-edged, strong highlights · brightness 42% · saturation 49% · contrast 63% · warm 0% / cool 100%
- **Palette (measured):** #334785 blue 46%, #ebf7fa light cyan 15%, #151e38 dark blue 14%, #abc8f0 light blue 8%, #7995e1 blue 8%, #4b63d0 blue 7%

### Small gold diamond

`bonusBgdanim_3_png.73072a` · atlas · 11 parts · largest 39×29 · sheet `sheets/bonusBgdanim_3_png.73072a.webp`

- **Role:** A gem that travels to the Ignite lamp (inference from its folder, ignite).
- **Subject:** A tiny yellow-gold cut gem turning, 11 frames.
- **Style:** Rendered gem.
- **Rendering:** Hard-edged.
- **Colour:** Measured: gold #fad543 39%, orange #d4920c 30%, brown #994d06.
- **Lighting:** Top light.
- **Ambience:** A spark of value.
- **Materials:** Gemstone.
- **Variants:** Three colours of the same gem on three sheets.
- **Motion:** 11 frames; the skeleton has a diamonds_path, so gems follow a curve.
- **Construction:** 36x29 frames.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 60% · saturation 86% · contrast 77% · warm 100% / cool 0%
- **Palette (measured):** #fad543 gold 39%, #d4920c orange 30%, #994d06 brown 16%, #641801 dark red 10%

### Small cyan diamond

`bonusBgdanim_4_png.ca1f1f` · atlas · 11 parts · largest 37×29 · sheet `sheets/bonusBgdanim_4_png.ca1f1f.webp`

- **Role:** The gem of the Collect lamp (inference).
- **Subject:** A tiny cyan cut gem turning, 11 frames.
- **Style:** Rendered gem.
- **Rendering:** Hard-edged.
- **Colour:** Measured: cyan #1fa4d3 49%, dark cyan #086486 24%, light cyan #5ccef6 20%.
- **Lighting:** Top light.
- **Ambience:** Cool spark.
- **Materials:** Gemstone.
- **Variants:** Cyan variant.
- **Motion:** 11 frames.
- **Construction:** 36x29 frames.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 52% · saturation 82% · contrast 55% · warm 0% / cool 100%
- **Palette (measured):** #1fa4d3 cyan 49%, #086486 dark cyan 24%, #5ccef6 cyan 20%, #033046 dark cyan 4%, #8fe2fc light cyan 4%

### Fire burst

`bonusBgdanim_5_png.8497da` · atlas · 16 parts · largest 189×183 · sheet `sheets/bonusBgdanim_5_png.8497da.webp`

- **Role:** The fire of the Ignite feature.
- **Subject:** A ragged ball of orange and yellow flame, 16 frames.
- **Style:** Photographic fire.
- **Rendering:** Soft-edged alpha.
- **Colour:** Measured: orange #fdb656 51% and #f9731a 25%, red #f43507 12%.
- **Lighting:** Self-lit.
- **Ambience:** Sudden heat.
- **Materials:** Fire.
- **Variants:** A second, yellower copy is packed with the feature lettering.
- **Motion:** 16 frames.
- **Construction:** About 186x183.
- **Measured:** bright, vivid, warm, medium contrast · brightness 64% · saturation 74% · contrast 52% · warm 100% / cool 0%
- **Palette (measured):** #fdb656 orange 51%, #f9731a orange 25%, #f43507 red 12%, #fbdfa4 light orange 8%, #ed0815 red 3%

### Small white diamond

`bonusBgdanim_7_png.fb9d70` · atlas · 11 parts · largest 39×29 · sheet `sheets/bonusBgdanim_7_png.fb9d70.webp`

- **Role:** The gem of the Jackpot lamp (inference from its folder, jackpot).
- **Subject:** A tiny white cut gem turning, 11 frames.
- **Style:** Rendered gem.
- **Rendering:** Hard-edged.
- **Colour:** Measured: pale blue-white #eff3f9 41%, grey-blue #b1b4c4 35%.
- **Lighting:** Top light.
- **Ambience:** Clean sparkle.
- **Materials:** Gemstone.
- **Variants:** White variant.
- **Motion:** 11 frames; in the real screens small white gems fly from a landed diamond up to the Jackpot lamp.
- **Construction:** 36x29 frames.
- **Measured:** bright, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 75% · saturation 9% · contrast 59% · warm 0% / cool 100%
- **Palette (measured):** #eff3f9 light blue 41%, #b1b4c4 blue 35%, #7b7c90 grey 20%, #545468 grey 4%

### Bonus scene particles and stars

`bonusBgdanim_jpg.25a492` · atlas · 25 parts · largest 397×350 · sheet `sheets/bonusBgdanim_jpg.25a492.webp`

- **Role:** Light effects over the bonus scene.
- **Subject:** Star frames, a 12-frame shower of white particles, a diagonal light sweep and a white portrait panel, on black.
- **Style:** Effect plates.
- **Rendering:** Additive.
- **Colour:** Measured: black 77% with greys and white.
- **Lighting:** Self-lit.
- **Ambience:** Sparkle in the cave.
- **Materials:** Light.
- **Variants:** Two sequences and two plates.
- **Motion:** 12 and 11 frames.
- **Construction:** 25 parts.
- **Notes:** Not seen in play in this run.
- **Measured:** dark, muted, neutral, medium contrast, hard-edged · brightness 12% · saturation 0% · contrast 29% · warm 1% / cool 0%
- **Palette (measured):** #030303 black 77%, #373736 grey 8%, #656565 grey 6%, #939392 grey 4%, #fbfbfa white 4%, #c3c4c2 grey 2%

### Bonus smoke

`bonusBgdanim_png.b60e23` · atlas · 1 parts · largest 342×271 · sheet `sheets/bonusBgdanim_png.b60e23.webp`

- **Role:** A cloud for the bonus scene.
- **Subject:** One white cloud puff.
- **Style:** Soft smoke.
- **Rendering:** Soft alpha.
- **Colour:** White; tinted in use.
- **Lighting:** Self-lit.
- **Ambience:** Mist in the cave.
- **Materials:** Smoke.
- **Variants:** One part.
- **Motion:** The skeleton names smoke loops.
- **Construction:** 342x271.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Coin flip frames and small stacks

`coins_png.d1a3b5` · atlas · 10 parts · largest 94×90 · sheet `sheets/coins_png.d1a3b5.webp`

- **Role:** Coins that fly and stack on a win or collection (inference).
- **Subject:** The lamp coin in 6 turning frames, its edge, and three small stacks of coins.
- **Style:** Rendered coins.
- **Rendering:** Hard-edged, bright rims.
- **Colour:** Measured: orange #f9b80d 45%, brown #9d3f02 17%, orange #dc7107 13%, gold #fdf416 10%.
- **Lighting:** Top-left light.
- **Ambience:** Small change raining.
- **Materials:** Gold.
- **Variants:** 6 flip frames, 3 stacks.
- **Motion:** A 6-frame flip; the skeleton places about 30 coins left and right.
- **Construction:** Coins about 94x90.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 60% · saturation 87% · contrast 61% · warm 97% / cool 2% · brighter towards: top (4), top-right (1)
- **Palette (measured):** #f9b80d orange 45%, #9d3f02 brown 17%, #dc7107 orange 13%, #fdf416 gold 10%, #393939 grey 8%, #fdd649 gold 5%

### Counter burst

`fgCounterParticleBurstAnims_jpg.c4d3f5` · atlas · 23 parts · largest 100×100 · sheet `sheets/fgCounterParticleBurstAnims_jpg.c4d3f5.webp`

- **Role:** A burst on a counter (inference: fg in the name may stand for free games; no such counter was seen).
- **Subject:** A yellow spark that swells into a pink-magenta ball of light and fades, 23 frames on black.
- **Style:** Effect sequence.
- **Rendering:** Additive.
- **Colour:** Measured: dark #180b18, magentas #52214c, #e352ac, #f364da, light pink #fba0f4.
- **Lighting:** Self-lit.
- **Ambience:** A pop of magic.
- **Materials:** Light.
- **Variants:** One sequence.
- **Motion:** 23 frames.
- **Construction:** 100x100 plates.
- **Notes:** Not seen in play in this run.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 39% · saturation 54% · contrast 44% · warm 52% / cool 3%
- **Palette (measured):** #180b18 black 21%, #52214c dark magenta 18%, #fba0f4 light magenta 17%, #e352ac magenta 10%, #8d3676 magenta 10%, #f364da magenta 8%

### Smoke stars

`fgSmoke_jpg.84210e` · atlas · 21 parts · largest 397×350 · sheet `sheets/fgSmoke_jpg.84210e.webp`

- **Role:** Stars inside the smoke.
- **Subject:** Small white stars on black, 21 frames.
- **Style:** Effect plates.
- **Rendering:** Additive.
- **Colour:** Black and greys.
- **Lighting:** Self-lit.
- **Ambience:** Twinkle.
- **Materials:** Light.
- **Variants:** One sequence.
- **Motion:** 21 frames.
- **Construction:** 397x350 plates.
- **Measured:** dark, muted, neutral, low contrast, hard-edged · brightness 5% · saturation 0% · contrast 19% · warm 0% / cool 0%
- **Palette (measured):** #020202 black 88%, #363636 grey 6%, #646464 grey 4%, #8e8e8e grey 2%

### Foreground smoke puffs

`fgSmoke_png.4ad75d` · atlas · 2 parts · largest 683×535 · sheet `sheets/fgSmoke_png.4ad75d.webp`

- **Role:** The smoke that colours the prize meters, the intro and the lamps.
- **Subject:** Two white cloud puffs.
- **Style:** Soft painted smoke.
- **Rendering:** Soft-edged alpha.
- **Colour:** White; the skeleton names tints: grand, major, minor, purple, green, yellow, white.
- **Lighting:** Self-lit.
- **Ambience:** Genie smoke everywhere.
- **Materials:** Smoke.
- **Variants:** Two puffs reused at many sizes and colours.
- **Motion:** Seen in the real screens as the pink cloud behind the logo and the coloured clouds behind the lamp words; loops named for the jackpots and the tutorial.
- **Construction:** Two textures (683x535, 477x561) carry most of the game's atmosphere: its skeleton is 380 KB of motion for two pictures.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 97% · saturation 0% · contrast 5% · warm 0% / cool 0%
- **Palette (measured):** #fafafa white 94%, #d0d0d0 grey 4%

### Gold transition coins

`goldTransitionAnims_png.93936c` · atlas · 5 parts · largest 190×182 · sheet `sheets/goldTransitionAnims_png.93936c.webp`

- **Role:** A rush of coins across the screen between game and bonus (inference from the name goldTransition).
- **Subject:** Two large gold coins, one embossed with the genie's face in profile and one with the lamp, a coin edge, a soft particle and a spark.
- **Style:** Chunky rendered coins with a ring of flame shapes round the rim.
- **Rendering:** High relief, strong orange-to-yellow gradient, hard edges.
- **Colour:** Measured: orange #f6a906 54%, brown #b14303 17%, gold #fef20e 14%, orange #e76906; warm 99%.
- **Lighting:** Top-left light.
- **Ambience:** A flood of gold.
- **Materials:** Gold.
- **Variants:** Two faces of one coin and an edge-on strip so a coin can flip.
- **Motion:** The skeleton is the largest in the game (about 980 KB) with hundreds of bones on two paths: many coins streaming along curves (inference from its bone and path names).
- **Construction:** Five small parts drive a full-screen transition; all the weight is in the animation data.
- **Notes:** Not seen in play in this run.
- **Measured:** bright, vivid, warm, high contrast, hard-edged · brightness 62% · saturation 96% · contrast 65% · warm 99% / cool 0% · brighter towards: top-right (1)
- **Palette (measured):** #f6a906 orange 54%, #b14303 brown 17%, #fef20e gold 14%, #e76906 orange 6%

### Transition stars

`lamp_transition_jpg.5d5601` · atlas · 22 parts · largest 397×350 · sheet `sheets/lamp_transition_jpg.5d5601.webp`

- **Role:** Stars over the lamp transition.
- **Subject:** A few small white stars on black over 21 frames, and a white panel for the portrait layout.
- **Style:** Effect plates.
- **Rendering:** Additive.
- **Colour:** Measured: black with greys and white.
- **Lighting:** Self-lit.
- **Ambience:** Twinkle.
- **Materials:** Light.
- **Variants:** One 21-frame sequence.
- **Motion:** 21 frames.
- **Construction:** 397x350 plates, mostly empty: costly for what they show.
- **Notes:** The same star sequence is packed again in the fgSmoke and bonusBgdanim sheets.
- **Measured:** dark, muted, neutral, low contrast, hard-edged · brightness 6% · saturation 0% · contrast 19% · warm 0% / cool 0%
- **Palette (measured):** #020202 black 87%, #363636 grey 6%, #656565 grey 4%, #909090 grey 2%, #ffffff white 2%

### The genie's lamp for the transition, in parts

`lamp_transition_png.837a42` · atlas · 8 parts · largest 695×535 · sheet `sheets/lamp_transition_png.837a42.webp`

- **Role:** The teal and gold oil lamp built from pieces so it can turn and open in the transition to the bonus (inference from the name lamp_transition).
- **Subject:** The lamp's teal body with gold vine ornament and spout, a striped teal and gold conical lid, an orange-gold dish base, a curled gold handle, small caps, and a white smoke cloud.
- **Style:** Rendered 3D prop with enamel ornament.
- **Rendering:** Smooth shaded parts with crisp ornament; the pieces are views of a 3D model.
- **Colour:** Measured: white 74% (the smoke), orange #e87f05, gold #f6e40e, cyan #11e7ee.
- **Lighting:** Lit from the upper left, warm.
- **Ambience:** The one storybook object of the game, shown large.
- **Materials:** Enamel, gold.
- **Variants:** One lamp; the skeleton has a bone named fake_3D and animations for purple and blue smoke transitions and a portrait version (read from its file).
- **Motion:** Not drawn by the tools. Inference: the lamp spins by sliding its parts, then smoke fills the screen.
- **Construction:** 8 parts for the lamp_transition skeleton; the body is 504x172, the largest single prop in the game.
- **Notes:** Not seen in play in this run.
- **Measured:** bright, muted, warm and cool mixed, low contrast, strong highlights · brightness 90% · saturation 22% · contrast 17% · warm 15% / cool 10% · brighter towards: bottom-right (1), top-left (1), top-right (1)
- **Palette (measured):** #ffffff white 74%, #e87f05 orange 6%, #f6e40e gold 4%, #11e7ee cyan 2%

### Lamp lightning

`lamps_2_jpg.0965ab` · atlas · 8 parts · largest 101×240 · sheet `sheets/lamps_2_jpg.0965ab.webp`

- **Role:** A bolt for the Collect lamp (inference from its folder name, lighting, and blue colour).
- **Subject:** A blue-white lightning bolt on black in 8 frames.
- **Style:** Photographic.
- **Rendering:** Additive plate.
- **Colour:** Measured: dark blue #3a3f5e 23%, pale blue #e5eef8 22%, blues #8d96bb and #666c95.
- **Lighting:** Self-lit.
- **Ambience:** A jolt.
- **Materials:** Electric light.
- **Variants:** One 8-frame sequence.
- **Motion:** 8 frames.
- **Construction:** 101x240 plates.
- **Measured:** mid-tone, saturated, cool, high contrast, hard-edged, strong highlights · brightness 53% · saturation 25% · contrast 60% · warm 0% / cool 100%
- **Palette (measured):** #3a3f5e dark blue 23%, #e5eef8 light blue 22%, #8d96bb blue 16%, #666c95 blue 14%, #b8c2dd light blue 14%, #0c0e15 black 10%

### Lamp smoke flame and stars

`lamps_3_jpg.9ce2bd` · atlas · 14 parts · largest 101×240 · sheet `sheets/lamps_3_jpg.9ce2bd.webp`

- **Role:** A soft white flame and stars for a lamp, tinted in the engine.
- **Subject:** A soft white column, wider at the base, in 8 frames, and small stars in 6 frames, on black.
- **Style:** Soft effect.
- **Rendering:** Additive plates.
- **Colour:** Measured: black, cream #efefeb 26% and greys; no hue.
- **Lighting:** Self-lit.
- **Ambience:** Gentle glow.
- **Materials:** Smoke, light.
- **Variants:** Two sequences.
- **Motion:** 8 and 6 frames; the pink smoke behind the Jackpot lamp in the real screens is of this kind.
- **Construction:** 101x240 plates.
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 43% · saturation 1% · contrast 46% · warm 0% / cool 0%
- **Palette (measured):** #040404 black 37%, #efefeb light yellow 26%, #babbb8 grey 13%, #828381 grey 12%, #363636 grey 9%, #585857 grey 3%

### Lamp effects: tornado, rings and flames

`lamps_jpg.e2b616` · atlas · 51 parts · largest 200×200 · sheet `sheets/lamps_jpg.e2b616.webp`

- **Role:** What rises from a lamp when its feature wakes.
- **Subject:** A blue twisting column of smoke (tornado_lamp, 31 frames), a white ring of light (8 frames), a white flame (8 frames) and star particles, all on black.
- **Style:** Photographic smoke and light.
- **Rendering:** Bright on black, additive.
- **Colour:** Measured: blue #288ff2 26%, light blue #8bc2f5 18%, greys.
- **Lighting:** Self-lit.
- **Ambience:** The genie stirring in the lamp.
- **Materials:** Smoke, light.
- **Variants:** One tornado in blue; rings and flames in white to be tinted per lamp.
- **Motion:** 31-frame tornado, 8-frame ring and flame. The real screens show a small blue swirl over the Collect lamp and a flame over the Ignite lamp at rest.
- **Construction:** 51 frames on one opaque page.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 52% · saturation 44% · contrast 52% · warm 0% / cool 67% · brighter towards: bottom (1)
- **Palette (measured):** #288ff2 blue 26%, #8bc2f5 light blue 18%, #a6a6a7 grey 12%, #dfe7f0 light blue 9%, #2f333c dark blue 8%, #686868 grey 7%

### Spin button ring

`respinCircleAnims_jpg.61b052` · atlas · 40 parts · largest 302×293 · sheet `sheets/respinCircleAnims_jpg.61b052.webp`

- **Role:** A ring of light that runs round the spin button.
- **Subject:** A broken circle of yellow fire turning on black, 40 frames.
- **Style:** Effect sequence.
- **Rendering:** Additive plates.
- **Colour:** Measured: black #1a1202, browns, gold #eadb3b and #f8f170, pale gold #fefcbb.
- **Lighting:** Self-lit.
- **Ambience:** Energy while the reels turn.
- **Materials:** Light.
- **Variants:** One 40-frame turn.
- **Motion:** 40 frames.
- **Construction:** 302x293 plates, the longest sequence in the game for a small interface accent.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 50% · saturation 75% · contrast 61% · warm 100% / cool 0%
- **Palette (measured):** #1a1202 black 28%, #674a07 brown 19%, #b4981c gold 16%, #fefcbb light gold 14%, #eadb3b gold 13%, #f8f170 gold 10%

### Anticipation sparkle

`starTensionAnims_png.836196` · atlas · 1 parts · largest 44×44 · sheet `sheets/starTensionAnims_png.836196.webp`

- **Role:** The star used when a reel builds tension.
- **Subject:** A single white four-point sparkle.
- **Style:** Effect part.
- **Rendering:** Soft white.
- **Colour:** White; tinted in use.
- **Lighting:** Self-lit.
- **Ambience:** Expectation.
- **Materials:** Light.
- **Variants:** One part; the skeleton places 16 stars.
- **Motion:** Stars twinkle along a reel (inference from the skeleton's name, starsAnticipation).
- **Construction:** One 44x44 texture.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Win frame

`winFrame_png.47dbea` · atlas · 19 parts · largest 200×200 · sheet `sheets/winFrame_png.47dbea.webp`

- **Role:** The box drawn around each winning cell.
- **Subject:** A square frame of white light with a magenta neon glow, a grey disabled copy, a magenta smoke streak and a 15-frame glow that runs round the frame.
- **Style:** Neon sign.
- **Rendering:** A hard white line inside a soft magenta bloom.
- **Colour:** Measured: near-black #18031c 31%, pale pink #f5eaf6 25%, purples #440951 and #771289, magenta #d256e3 9%.
- **Lighting:** Self-lit.
- **Ambience:** Electric, a clear accent against the red and gold board.
- **Materials:** Neon light.
- **Variants:** Lit and disabled (grey) states.
- **Motion:** Seen in the real win screens: lit frames on the winning cells, grey frames on cells of a line already shown, a light running round each frame.
- **Construction:** 186x162, a little larger than the 164x145 cell; 15 glow frames at 200x200.
- **Notes:** Magenta is kept for wins and for the big-win digits: it is the game's signal colour for money won.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 41% · saturation 57% · contrast 60% · warm 33% / cool 33%
- **Palette (measured):** #18031c black 31%, #f5eaf6 light magenta 25%, #440951 dark purple 11%, #ebabf1 light magenta 9%, #d256e3 magenta 9%, #771289 magenta 8%

### Small coin spin

`coin.72ba94` · atlas · 19 parts · largest 50×50 · sheet `sheets/coin.72ba94.webp`

- **Role:** A particle coin.
- **Subject:** A small lamp coin turning in 19 frames.
- **Style:** Rendered coin.
- **Rendering:** Hard-edged, tiny.
- **Colour:** Measured: orange #f1a60d 63%, brown #bb6303 15%, gold #feef12 9%.
- **Lighting:** Top-left.
- **Ambience:** Glitter of money.
- **Materials:** Gold.
- **Variants:** One 19-frame turn.
- **Motion:** 19 frames.
- **Construction:** 50x50 frames in a strip: sized for a particle emitter.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 62% · saturation 95% · contrast 57% · warm 100% / cool 0%
- **Palette (measured):** #f1a60d orange 63%, #bb6303 brown 15%, #feef12 gold 9%, #943a02 brown 8%, #fbcc45 orange 2%, #612b01 brown 2%

### Smoke and sparkle (localised sheet)

`loc_webp80_png.4b3fe7` · atlas · 2 parts · largest 348×281 · sheet `sheets/loc_webp80_png.4b3fe7.webp`

- **Role:** A smoke puff and a sparkle on the sheet the client keeps per language.
- **Subject:** A white cloud and a four-point sparkle.
- **Style:** Effect parts.
- **Rendering:** Soft white.
- **Colour:** White.
- **Lighting:** Self-lit.
- **Ambience:** Smoke.
- **Materials:** Smoke, light.
- **Variants:** Two parts.
- **Construction:** The sheet is named loc, the place for language-dependent art; in English it holds no lettering.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%


## Game interface

Buttons, counters and panels drawn for this game.

### Interface sheet: buttons, switches, wordmarks and the cave foreground

`default_webp80_png-0.dcdec8` · atlas · 28 parts · largest 2720×1709 · sheet `sheets/default_webp80_png-0.dcdec8.webp`

- **Role:** The game's own controls, with a few large pieces packed alongside.
- **Subject:** Round glass-dome buttons in gold rings (play, skip, slam stop, autospin start and stop, bet settings), small plus and minus tiles for the bet, a pill switch for Do not show again, dark red meter plates, the two wordmarks, and greben, the rock ridge covered in treasure that fronts the bonus cave.
- **Style:** Glossy jewel-like interface with gold filigree rings, matching the reel frame.
- **Rendering:** Each button is a violet-to-blue dome with a hard highlight, a scalloped gold ring and a flat yellow glyph; disabled states are washed to grey-lilac.
- **Colour:** Measured over the sheet: near-black blue #071026 57% and dark blue #0a2f62 16% (both from the large cave ridge), blue #104ea3, dark red #50140f. The buttons themselves are violet, blue and yellow.
- **Lighting:** Top highlight on every dome; the ridge is lit in cold blue like its cave.
- **Ambience:** Toy-like and friendly controls against the rich frame.
- **Materials:** Glass, gold, enamel.
- **Variants:** Every button in disabled, enabled, over and pressed (the pressed state is 10% smaller, 180 against 200 pixels). Two wordmarks.
- **Motion:** The buttons swap state pictures; a ring of light turns around the spin button while it spins (respinCircle sequence).
- **Construction:** 28 sprites; buttons are 200x200 and 110 to 120 square, shown at about 60% on a 1280x720 screen.
- **Notes:** The provider's own console (bet list, menu, paytable frame) is HTML outside these sheets and is not this game's art.
- **Measured:** dark, vivid, cool, medium contrast, hard-edged · brightness 15% · saturation 82% · contrast 38% · warm 20% / cool 79% · brighter towards: top-left (9), top (3), top-right (2)
- **Palette (measured):** #071026 black 57%, #0a2f62 dark blue 16%, #104ea3 blue 4%, #50140f dark red 4%


## Typography

Embedded fonts and lettering.

### Feature-active lettering

`activeFont.99ac25` · atlas · 1 parts · largest 959×959 · sheet `sheets/activeFont.99ac25.webp`

- **Role:** Short words in several scripts for a feature being active (inference from the name activeFont).
- **Subject:** Heavy slab-like capitals in yellow with an orange edge, including Latin, Cyrillic and Japanese and Chinese characters.
- **Style:** Bold showcard lettering.
- **Rendering:** Yellow-to-orange gradient with an orange outline and a soft bevel.
- **Colour:** Measured: gold #fdde0d 52%, orange #fd8006 45%.
- **Lighting:** Top light.
- **Ambience:** Loud and warm.
- **Materials:** Enamel.
- **Variants:** One font with only the glyphs its few words need in each language.
- **Motion:** Static.
- **Construction:** One 959x959 page; the glyph set shows the game is localised into at least Japanese, Chinese and a Cyrillic language.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 71% · saturation 96% · contrast 38% · warm 100% / cool 0%
- **Palette (measured):** #fdde0d gold 52%, #fd8006 orange 45%, #fab028 orange 2%

### Win amount numerals (pink chrome)

`bigWinFont.c55a7e` · atlas · 1 parts · largest 580×608 · sheet `sheets/bigWinFont.c55a7e.webp`

- **Role:** The amount of a win, shown over the reels.
- **Subject:** Tall serif digits in pink-white chrome with a dark magenta edge.
- **Style:** Showcard numerals.
- **Rendering:** Chrome gradient from white to pink with a dark magenta outline.
- **Colour:** Measured: pale pink #fce4fa 38%, dark magenta #3a071d 22%, pink #f7abf6 12%, magentas #691045 and #8c1e78.
- **Lighting:** Polished, bright in the middle.
- **Ambience:** The one cool-pink note on a red and gold board, so the amount cannot be missed.
- **Materials:** Pink chrome.
- **Variants:** Digits, comma and point only.
- **Motion:** Seen in the real win screen: 7.80 in these digits over the reels, counting up.
- **Construction:** One 580x608 page.
- **Notes:** Matches the magenta win frame.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, strong highlights · brightness 56% · saturation 44% · contrast 94% · warm 60% / cool 1%
- **Palette (measured):** #fce4fa light magenta 38%, #3a071d dark magenta 22%, #f7abf6 light magenta 12%, #691045 dark magenta 8%, #9f698c magenta 6%, #8c1e78 magenta 4%

### Coin value numerals (ivory)

`coin.bc50be` · atlas · 1 parts · largest 874×873 · sheet `sheets/coin.bc50be.webp`

- **Role:** Values shown on coins in the bonus (inference from the name; not seen in play).
- **Subject:** The same tall serif numerals and currency signs in ivory with a heavy black outline.
- **Style:** Showcard numerals.
- **Rendering:** Flat ivory face with a faint marbling and a thick black edge.
- **Colour:** Measured: black #020202 45%, ivory #ede8d8 39%.
- **Lighting:** Flat.
- **Ambience:** Clear and readable on a busy coin.
- **Materials:** Ivory or bone.
- **Variants:** One of three coin fonts: ivory, yellow, orange.
- **Motion:** Static.
- **Construction:** One 874x873 page with an XML glyph table.
- **Measured:** mid-tone, muted, neutral, high contrast, strong highlights · brightness 43% · saturation 13% · contrast 98% · warm 100% / cool 0%
- **Palette (measured):** #020202 black 45%, #ede8d8 light yellow 39%, #575655 grey 8%

### Coin value numerals (orange)

`coinsOrange.56c4b2` · atlas · 1 parts · largest 874×874 · sheet `sheets/coinsOrange.56c4b2.webp`

- **Role:** Coin values, orange-red version, probably for the Ignite feature (inference from its fire colours).
- **Subject:** The same numerals in an orange-to-red fire gradient with a black outline.
- **Style:** Showcard numerals.
- **Rendering:** Hot gradient face with a pale core, thick black edge.
- **Colour:** Measured: black 47%, orange #d67613 24%, red #b52e09, brown #551e0a, gold #f2c521.
- **Lighting:** Glows from inside.
- **Ambience:** Heated metal.
- **Materials:** Molten gold.
- **Variants:** Orange variant.
- **Motion:** Static.
- **Construction:** One 874x874 page.
- **Measured:** dark, vivid, warm, high contrast · brightness 27% · saturation 67% · contrast 84% · warm 100% / cool 0%
- **Palette (measured):** #050201 black 47%, #d67613 orange 24%, #b52e09 red 6%, #551e0a brown 6%, #f2c521 gold 3%, #fdf7d9 light gold 2%

### Coin value numerals (yellow)

`coinsYellow.85e518` · atlas · 1 parts · largest 874×874 · sheet `sheets/coinsYellow.85e518.webp`

- **Role:** Coin values, yellow version.
- **Subject:** The same numerals in yellow gold with a black outline.
- **Style:** Showcard numerals.
- **Rendering:** Gold gradient face, thick black edge.
- **Colour:** Measured: black 46%, gold #ebcf0a 29%, brown #5b400b, orange-gold #c68e0d.
- **Lighting:** Light from above.
- **Ambience:** Readable gold.
- **Materials:** Gold.
- **Variants:** Yellow variant.
- **Motion:** Static.
- **Construction:** One 874x874 page.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 36% · saturation 70% · contrast 91% · warm 100% / cool 0%
- **Palette (measured):** #040201 black 46%, #ebcf0a gold 29%, #5b400b brown 10%, #c68e0d orange 8%, #faf471 gold 3%, #986c0d brown 2%

### Grand prize numerals

`grandJPFont.63d2da` · atlas · 1 parts · largest 891×893 · sheet `sheets/grandJPFont.63d2da.webp`

- **Role:** The figures on the Grand meter.
- **Subject:** Digits, currency signs and the letters needed for short currency codes, in a tall high-contrast serif with ball terminals (the style of a fat Didone face).
- **Style:** Showcard numerals: classic casino gold.
- **Rendering:** A bitmap font: each glyph has a chrome-like vertical gradient with a white band across the middle, a dark inner line and a coloured outer edge.
- **Colour:** Measured: red #ad2d17 21% and dark red #601a0c, gold #fcf965 and #f7d213, brown #8e5c25. Gold glyphs with a red edge.
- **Lighting:** Each glyph is lit as polished metal, bright in the middle band.
- **Ambience:** Money shown as jewellery.
- **Materials:** Polished gold.
- **Variants:** One of five prize fonts that differ only in the colour of the outer edge.
- **Motion:** Static glyphs; the values on the meters stood still during play.
- **Construction:** One page of about 891x893 with an XML glyph table; the reader keeps the page whole.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 50% · saturation 73% · contrast 94% · warm 100% / cool 0%
- **Palette (measured):** #ad2d17 red 21%, #fcf965 gold 13%, #8e5c25 brown 13%, #601a0c dark red 12%, #c18c36 orange 11%, #f7d213 gold 11%

### Major prize numerals

`majorFont.b366ed` · atlas · 1 parts · largest 891×893 · sheet `sheets/majorFont.b366ed.webp`

- **Role:** The figures on the Major meter.
- **Subject:** Digits, currency signs and the letters needed for short currency codes, in a tall high-contrast serif with ball terminals (the style of a fat Didone face).
- **Style:** Showcard numerals: classic casino gold.
- **Rendering:** A bitmap font: each glyph has a chrome-like vertical gradient with a white band across the middle, a dark inner line and a coloured outer edge.
- **Colour:** Measured: brown-gold #816024 23%, dark green #226f19 15%, gold #f7d213 and #fcf95a, green #5d9929. Gold glyphs with a green edge.
- **Lighting:** Each glyph is lit as polished metal, bright in the middle band.
- **Ambience:** Money shown as jewellery.
- **Materials:** Polished gold.
- **Variants:** One of five prize fonts that differ only in the colour of the outer edge.
- **Motion:** Static glyphs; the values on the meters stood still during play.
- **Construction:** One page of about 891x893 with an XML glyph table; the reader keeps the page whole.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 54% · saturation 69% · contrast 90% · warm 71% / cool 14%
- **Palette (measured):** #816024 brown 23%, #226f19 dark green 15%, #f7d213 gold 11%, #051605 black 10%, #fcf95a gold 10%, #fdfcf2 light gold 6%

### Maxi prize numerals

`maxiFont.8634a9` · atlas · 1 parts · largest 891×893 · sheet `sheets/maxiFont.8634a9.webp`

- **Role:** The figures on the Maxi meter.
- **Subject:** Digits, currency signs and the letters needed for short currency codes, in a tall high-contrast serif with ball terminals (the style of a fat Didone face).
- **Style:** Showcard numerals: classic casino gold.
- **Rendering:** A bitmap font: each glyph has a chrome-like vertical gradient with a white band across the middle, a dark inner line and a coloured outer edge.
- **Colour:** Measured: dark magenta #801377 13%, magenta #ba3986 11%, gold #fcf965 and #f7d213. Gold glyphs with a magenta edge.
- **Lighting:** Each glyph is lit as polished metal, bright in the middle band.
- **Ambience:** Money shown as jewellery.
- **Materials:** Polished gold.
- **Variants:** One of five prize fonts that differ only in the colour of the outer edge.
- **Motion:** Static glyphs; the values on the meters stood still during play.
- **Construction:** One page of about 891x893 with an XML glyph table; the reader keeps the page whole.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 50% · saturation 69% · contrast 93% · warm 86% / cool 0%
- **Palette (measured):** #801377 dark magenta 13%, #fcf965 gold 13%, #76451c brown 11%, #ba3986 magenta 11%, #f7d213 gold 10%, #130310 black 8%

### Mini prize numerals

`mini.f00b9b` · atlas · 1 parts · largest 900×893 · sheet `sheets/mini.f00b9b.webp`

- **Role:** The figures on the Mini meter.
- **Subject:** Digits, currency signs and the letters needed for short currency codes, in a tall high-contrast serif with ball terminals (the style of a fat Didone face).
- **Style:** Showcard numerals: classic casino gold.
- **Rendering:** A bitmap font: each glyph has a chrome-like vertical gradient with a white band across the middle, a dark inner line and a coloured outer edge.
- **Colour:** Measured: orange-gold #aa6c20 36%, brown #613613 16%, gold #fbf962 and #f7d213. Gold glyphs with an orange-gold edge.
- **Lighting:** Each glyph is lit as polished metal, bright in the middle band.
- **Ambience:** Money shown as jewellery.
- **Materials:** Polished gold.
- **Variants:** One of five prize fonts that differ only in the colour of the outer edge.
- **Motion:** Static glyphs; the values on the meters stood still during play.
- **Construction:** One page of about 891x893 with an XML glyph table; the reader keeps the page whole.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 53% · saturation 72% · contrast 94% · warm 100% / cool 0%
- **Palette (measured):** #aa6c20 orange 36%, #613613 brown 16%, #fbf962 gold 12%, #f7d213 gold 10%, #120803 black 10%, #fdfcf3 light gold 6%

### Minor prize numerals

`minor.83e1b7` · atlas · 1 parts · largest 891×893 · sheet `sheets/minor.83e1b7.webp`

- **Role:** The figures on the Minor meter.
- **Subject:** Digits, currency signs and the letters needed for short currency codes, in a tall high-contrast serif with ball terminals (the style of a fat Didone face).
- **Style:** Showcard numerals: classic casino gold.
- **Rendering:** A bitmap font: each glyph has a chrome-like vertical gradient with a white band across the middle, a dark inner line and a coloured outer edge.
- **Colour:** Measured: brown-gold #845c2a 20%, gold #fcf965 13%, dark cyan #1d6a78 12%, cyan #53928b. Gold glyphs with a cyan edge.
- **Lighting:** Each glyph is lit as polished metal, bright in the middle band.
- **Ambience:** Money shown as jewellery.
- **Materials:** Polished gold.
- **Variants:** One of five prize fonts that differ only in the colour of the outer edge.
- **Motion:** Static glyphs; the values on the meters stood still during play.
- **Construction:** One page of about 891x893 with an XML glyph table; the reader keeps the page whole.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 55% · saturation 64% · contrast 90% · warm 70% / cool 28%
- **Palette (measured):** #845c2a brown 20%, #fcf965 gold 13%, #1d6a78 dark cyan 12%, #f7d213 gold 11%, #53928b cyan 9%, #040b0e black 7%

### Spins counter numerals

`spinsFont.257332` · atlas · 1 parts · largest 265×405 · sheet `sheets/spinsFont.257332.webp`

- **Role:** The count of spins left in the bonus (inference from the name and the freeSpinsRemaining plate; not seen in play).
- **Subject:** The digits 0 to 3 only, in gold with a quilted diamond texture and a magenta edge.
- **Style:** Jewelled showcard numerals.
- **Rendering:** Textured gold face, magenta outline.
- **Colour:** Measured: gold-brown #c38d27 28%, near-black magenta #210421 17%, gold #e8cc49 15%, magenta #c91cbd 10%.
- **Lighting:** Top light.
- **Ambience:** Tension: the number that matters in a respin bonus.
- **Materials:** Hammered gold.
- **Variants:** Four digits: a counter that never shows more than 3, which fits a hold-and-respin bonus that resets to 3 (inference).
- **Motion:** Static.
- **Construction:** One 265x405 page.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 43% · saturation 79% · contrast 83% · warm 84% / cool 6%
- **Palette (measured):** #c38d27 orange 28%, #210421 black 17%, #e8cc49 gold 15%, #c91cbd magenta 10%, #642f0d brown 9%, #92532f brown 7%

### Feature words: Collect and Ignite

`bonusBgdanim_2_png.673d17` · atlas · 27 parts · largest 189×183 · sheet `sheets/bonusBgdanim_2_png.673d17.webp`

- **Role:** The words that hang over the blue and orange lamps, and their turn when a feature becomes active.
- **Subject:** Collect in yellow blackletter-like script with a blue extrusion and Ignite in yellow-orange with a red extrusion, each shown flat and in frames where the word swings round in 3D; a yellow fire burst is packed with them.
- **Style:** Decorative script between blackletter and Arabic-inspired calligraphy, extruded in 3D.
- **Rendering:** Flat yellow faces; the turning frames are 3D renders with deep coloured sides.
- **Colour:** Measured: pale gold #f7e377 36%, gold #fdf413 10%; warm 91%. The extrusions are blue for Collect and red-orange for Ignite.
- **Lighting:** Front-lit faces.
- **Ambience:** Storybook titles.
- **Materials:** Painted metal letters.
- **Variants:** Two words, each at rest and in 5 turning frames (the files call the turning sets Collect Active and Double Active).
- **Motion:** A 5-frame swing of the word; a 16-frame fire burst.
- **Construction:** 27 parts; words about 340x72.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 74% · saturation 61% · contrast 51% · warm 91% / cool 9% · brighter towards: bottom-left (3), left (2), bottom-right (1)
- **Palette (measured):** #f7e377 gold 36%, #fdf413 gold 10%, #fcfac9 light gold 9%

### Feature word: Jackpot

`bonusBgdanim_6_png.0d4d81` · atlas · 11 parts · largest 304×106 · sheet `sheets/bonusBgdanim_6_png.0d4d81.webp`

- **Role:** The word over the middle lamp and its turn.
- **Subject:** Jackpot in yellow script with a red extrusion, flat and in turning frames where the red sides dominate.
- **Style:** The same decorative script.
- **Rendering:** Flat yellow face, deep red 3D sides in the turning frames.
- **Colour:** Measured: red #f11306 20% and #a82409 15%, gold #fdf455 14%, orange #ef9515 11%.
- **Lighting:** Front-lit.
- **Ambience:** The loudest of the three words.
- **Materials:** Painted metal letters.
- **Variants:** At rest and two 5-frame turns.
- **Motion:** 5-frame swings.
- **Construction:** 11 parts; the word is 340x90.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 45% · saturation 87% · contrast 67% · warm 100% / cool 0% · brighter towards: right (4), top-right (1)
- **Palette (measured):** #f11306 red 20%, #a82409 red 15%, #fdf455 gold 14%, #ef9515 orange 11%, #3b0f02 black 10%, #fded10 gold 5%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `ticket`: 1 parts
- `PFSReveal.desktop`: 1 parts
- `PFSReveal.desktop1`: 2 parts
- `PFSReveal.desktop2`: 1 parts
- `chests`: 1 parts
- `lights_front`: 1 parts
- `reveal`: 1 parts
- `arrowWhite`: 1 parts
- `930967b02f5e7975f0d0`: 1 parts
- `info_open.2cfa81`: 1 parts
- `info_open_hover.00fe31`: 1 parts
- `networkActivity.c82b36`: 40 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Lato (Black); Lato (Bold); Lato (Regular); Noto Sans (Regular); Oswald (Bold); Oswald (Regular); Oswald (SemiBold); Yeseva One (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1011 components cut from 77 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
