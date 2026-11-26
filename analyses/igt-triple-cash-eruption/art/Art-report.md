# Triple Cash Eruption: art report

igt · run `2026-11-26-1019-igt-triple-cash-eruption` · captured 2026-11-26

Source: the provider's free-play demo, https://platform.ka.rgsgames.com/skb/gateway?channel=INT&countrycode=AT&currencycode=FPY&language=en&nscode=OLGP&skincode=OLB1&softwareid=200-1700-082&uniqueid=0&locale=en&technology=HTML&presenttype=STD

**Extracted:** 1913 named components from 76 textures in 76 atlases; 7 Spine skeletons; 77 frame sequences (1490 frames); 5 fonts. Grouped into 76 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A classic fruit machine set inside a volcano: glossy fruit, bells and sevens on calm teal cells, with all the heat, glow and budget given to four colours of burning fireball, three small colour-coded volcanoes and a great deal of simulated fire.

**Style.** Two registers side by side. The symbols are a traditional fruit set (two sevens, bell, melon, grapes, plum, orange, lemon, cherries) drawn as rounded, glossy 3D-look objects with a small engraved swirl each. The world around them is flat, hard-edged poster painting: a ruined temple for the base game, a crater under a spiral sky for the bonus. The feature pieces (fireballs, lava, eruptions) look simulated rather than drawn.

**Rendering.** Symbols: smooth airbrushed volume, a hard white specular spot, a four-point sparkle, a thin gold rim on the premium ones, no outlines. Backgrounds: a few flat tones per shape, crisp edges, strong vignette to black. Effects: soft glowing frames on black grounds. Interface plates are clean teal enamel with a gold rim.

**Colour.** Warm and dark overall. Measured over the game's own art: black #180908 24%, dark red #581413 14%, red #88172c 8%. Against that the reel cells are teal (#079a8f, #04655d), the one cool field in the base game, so warm symbols sit on their complement. Colour is also the rule system: red is the Multiplier volcano and fireball, green is Collect, blue is Double, orange is plain cash; the jackpots are orange (Grand), magenta (Major), blue (Minor) and green (Mini), and the multipliers are 2X blue, 3X green, 5X magenta. Fire leans to magenta and pink in the sky and haze (#780539, #d1065e) rather than staying orange.

**Lighting.** Symbols are lit from the top left with a soft shadow below. Everything that pays is self-lit: fireballs, lava, halos and frames glow past their own edges. Both backgrounds are lit from one hot source in the middle (the crack in the temple wall, the lava lake) and fall dark at the sides, which keeps the panels and the board readable.

**Ambience.** Familiar and safe on the reels, loud and hot around them. The base game is an expectant temple chamber; the bonus drops into the crater, darker and redder, where gold numbers in fire rings are the only bright things. The opening is a short disaster film: eruption, flaming rocks at the camera, title, wipe to yellow.

**Shape language.** Round and soft for everything collectable (fruit, bell, globes); square for everything structural (cells, frames, plates); the volcano cone is the one triangle and it is used as the game's badge. Frames are hairlines; the reel board has almost no body of its own.

**Materials.** Enamel-like fruit, polished gold, lacquered sevens, plasma globes, lava and lava rock with glowing cracks, carved stone, cloud and smoke, teal enamel with gold rims.

**Typography and lettering.** The logo and the labels MULTIPLIER, COLLECT, DOUBLE and the jackpot names are one flared serif display face with bevel and gold rim, coloured by meaning. Win amounts use a bitmap font of marbled gold serif numerals; fireball values use a second bitmap font, very condensed black figures with a yellow and orange outline. Five font files are embedded for running text (QTFrizQuad Bold, Noto Sans Condensed Bold, an Oswald cut with currency glyphs, and the provider's Lato and Gilroy).

**Motion.** Thirteen Spine 4.0 skeletons (binary) drive the scene, but most of what moves is frame sequences inside them: 30-frame loops for each fireball and each flame border, 30-frame fire frames for wins and anticipation, 22 to 38 frame bursts for hits, landings and eruptions, and 20 burning frames per letter of the win words. Seen in play: reels spin as vertical smears; a win dims the board, puts fire frames on the winning cells and counts a gold number up; a fireball flies from its cell to the volcano of its colour and the lava on that cone rises; at the trigger all three volcanoes erupt, rocks fly at the camera and the screen burns to the bonus, where two 5x3 reel sets respin and lock orange fireballs with values.

**Variants and themes.** One cone, three colours; one fireball, four colours, each with a matching flame border; one flared serif, six colour codes. Every reel symbol ships as a still, a spin-blur copy and as layers (body, gold contour, shadow). Backgrounds and menus have landscape and portrait versions. The bonus buy offers two cards: a mystery card and a hotter super card.

**How it is built.** The 7 skeletons in the counts above are JSON files of a promotional overlay the demo host loads beside the game (listed under the provider interface, not read); the game's own 13 skeletons are binary files the tools do not count or draw. 76 textures and 1,913 named sprites were captured, 63 units of this game's art among them. Effects take most of the texture space: of 51 Spine atlas pages, 34 are opaque pages of frames on black (named _jpg, to be added as light) and several large effects ship as a colour page plus a black-and-white matte page instead of one page with alpha. The same small sequences are packed more than once (the hit burst three times, the embers twice), one copy per skeleton. Pages are WebP at quality 80 (as their names say), up to 2048 px. Symbol stills are about 150x130 px in a 180x158 cell.

**Consistency.** Strong where it matters: the colour code is never broken, teal with gold is every number plate, the flared serif is every label. Three hands show otherwise: glossy rounded symbols, flat poster backgrounds and one soft painterly vortex behind the panels, and they are kept apart by where they appear, so they do not clash.

**What to take from it.** (1) A leading game can be a plain fruit set: nine fruit-machine symbols and a wild. The art effort goes into the money objects (four fireballs) and the feature's targets (three volcanoes), not into the paytable. (2) Colour as rules: red, green and blue each mean one feature everywhere (fireball, border, volcano, label, buy card), and the jackpots and multipliers have fixed colours too. A player reads the state of the game from colour alone at thumbnail size. (3) Put warm symbols on a cool cell. The teal reel ground is the only large cool area and it makes every fruit and fireball stand off the board; the board itself is a hairline frame. (4) A meter can be a character: the lava level on each cone is the feature's progress display, and a halo over the crater says it is live. No figure was drawn for this game. (5) Change the place, not only the tint, for the bonus: temple interior for the base game, the crater for the bonus, each lit from one hot spot in the middle with dark sides for the panels. (6) Effects are frame sequences on black added as light, in 20 to 38 frames at about 150 to 500 px. That is a production method an AI art pipeline can follow: generate short fire and burst loops on black, no alpha needed. (7) Two number styles that cannot be confused: marbled gold serif numerals for wins, condensed black figures with a fire outline for values on fireballs. (8) What to avoid copying: the same sequences packed several times and mattes shipped as separate pages cost texture memory; our own packages should share one copy.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm, medium contrast, hard-edged · brightness 37% · saturation 59% · contrast 42% · warm 75% / cool 5% · brighter towards: top (62), top-left (37), top-right (29)

Palette: #180908 black 24%, #581413 dark red 14%, #faf9f6 light yellow 9%, #88172c red 9%, #504e4a grey 5%, #d4cdc5 light orange 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 9 | 22% | 77% | 37% | 83% / 9% | #770b2a dark red 37%, #290a10 black 32% |
| Reel board | 2 | 63% | 64% | 45% | 78% / 22% | #fd6f1f orange 50%, #fccc59 orange 25%, #60687a grey 10% |
| Symbols | 9 | 50% | 35% | 49% | 36% / 14% | #0c0706 black 15%, #f5f5f3 light yellow 14%, #7a7677 grey 14% |
| Characters | 1 | 42% | 82% | 43% | 77% / 18% | #fdbf06 gold 28%, #610e0d dark red 11%, #130b0a black 10% |
| Logo and title | 2 | 47% | 86% | 86% | 100% / 0% | #ee6f1c orange 18%, #741906 dark red 16%, #fde50f gold 13% |
| Win celebrations and banners | 4 | 30% | 54% | 41% | 100% / 0% | #110b0a black 42%, #e3b83e orange 11%, #4c2f1d brown 11% |
| Effects | 27 | 43% | 55% | 43% | 78% / 0% | #140905 black 23%, #fcfbf8 light orange 14%, #582110 dark red 13% |
| Game interface | 7 | 22% | 81% | 35% | 94% / 2% | #310a07 black 57%, #871b0f dark red 12%, #fe0401 red 9% |
| Typography | 2 | 34% | 79% | 89% | 100% / 0% | #050200 black 44%, #f39804 orange 16%, #ffe004 gold 12% |
| Provider interface (shared) | 13 | 36% | 62% | 54% | 58% / 33% | #130416 black 30%, #453242 dark magenta 15%, #eeeeef white 9% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Loading screen background

`4d787f445e5f871068dd` · atlas · 1 parts · largest 1440×810 · sheet `sheets/4d787f445e5f871068dd.webp`

- **Role:** The picture behind the logo and the progress bar while the game loads (seen in the real screen of the loading page).
- **Subject:** The same crater and spiral sky as the bonus background, brighter and wider.
- **Style:** Flat graphic painting, as the bonus scene.
- **Rendering:** Hard-edged shapes, soft ember dots, vignette to black.
- **Colour:** Dark red #850a26 (41%), near black #370608, lava orange #f9ac04 and #f0550a, magenta haze #d1065e.
- **Lighting:** Lit by the lava lake and the haze on the horizon.
- **Ambience:** A promise of the eruption before the game opens.
- **Materials:** Lava, rock, cloud.
- **Variants:** A relative of bonusBg: the same view with more light in it.
- **Motion:** A still picture.
- **Construction:** One 1440x810 PNG outside the atlases, loaded by the splash page.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 20% · saturation 94% · contrast 47% · warm 92% / cool 0%
- **Palette (measured):** #850a26 dark red 41%, #370608 black 35%, #f9ac04 orange 9%, #d1065e magenta 5%, #f0550a orange 4%

### Base game background (landscape)

`default_land_landscape_webp80_jpg-0` · atlas · 1 parts · largest 2040×1410 · sheet `sheets/default_land_landscape_webp80_jpg-0.webp`

- **Role:** The full-screen scene behind the reels in the base game; the sprite is named baseGameBg and the layout places it as the layer baseGameBgd.
- **Subject:** The inside of a ruined stone temple: carved pillars with glyphs left and right, a broken wall in the middle with a white-hot crack of lava light pouring through it, and a cobbled floor leading to it.
- **Style:** Stylised digital painting with flat, poster-like shapes and hard shadow edges; the carvings are simplified geometric glyphs, not a quoted real culture (inference: a generic lost-temple look).
- **Rendering:** Broad flat planes with a few tones each and crisp edges; detail is in the glyph carving and the cracked bricks, and the outer quarter of the picture falls to near black so the board and panels sit on calm ground.
- **Colour:** Warm against cool, measured 57% warm to 39% cool: red and salmon stone around the opening (#b4464e, #bc867c), cream-yellow light (#f0d185, #fcf3d9), deep blue and violet shadow (#29466f, #4e6691, #150e28).
- **Lighting:** One light source, the glowing crack in the centre: everything near it is lit warm from behind and the pillars turn to blue-violet silhouette towards the edges.
- **Ambience:** A hidden chamber with something burning behind the wall: adventurous and expectant rather than dangerous.
- **Materials:** Carved stone blocks, cracked brick, cobbles; the lava is shown only as light.
- **Variants:** A portrait painting of the same scene ships as baseGameBg_prt; the bonus has its own background (bonusBg).
- **Motion:** A still picture; in the real game screens the reels cover its centre and no moving layer of the temple was seen.
- **Construction:** One 2040x1410 picture on its own WebP page (the sheet's name says quality 80, from a JPEG source), drawn larger than the 1280x720 view.
- **Notes:** The base game shows a temple and the bonus shows the volcano itself: the scene change carries the feature.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 42% · saturation 53% · contrast 59% · warm 57% / cool 39%
- **Palette (measured):** #150e28 black 19%, #b4464e red 15%, #f0d185 orange 13%, #bc867c red 13%, #29466f dark blue 12%, #4e6691 blue 6%

### Bonus background (landscape)

`default_land_landscape_webp80_jpg-1` · atlas · 1 parts · largest 2040×1410 · sheet `sheets/default_land_landscape_webp80_jpg-1.webp`

- **Role:** The full-screen scene of the Triple Cash Eruption bonus (sprite bonusBg), seen behind the two bonus reel sets in the real screens.
- **Subject:** The rim of a volcano seen from just above: a lake of yellow lava in the crater, dark ridged slopes, a red spiral of cloud turning in the sky and embers in the air.
- **Style:** The same flat, graphic painting as the base scene, with simpler shapes: bands of cloud, ridges drawn as strokes.
- **Rendering:** Few tones, hard edges, a strong vignette to black on all sides; embers are small soft dots.
- **Colour:** Almost one hue family: dark crimson (#730620, 54%) and near black (#310305), with orange and yellow only in the lava and embers (#f17008, #f9bb06) and a magenta haze on the horizon. Measured dark (brightness 0.16) and vivid (saturation 0.95).
- **Lighting:** Lit from below by the lava; the haze behind the rim glows magenta and the sky stays dark.
- **Ambience:** Hot, heavy and dramatic: the stake-raising scene.
- **Materials:** Lava, rock, smoke cloud, embers.
- **Variants:** The portrait version is bonusBg_prt; the loading splash uses a brighter painting of the same view.
- **Motion:** A still picture; in the bonus screens embers drift over it (the ember frames are in the effects units).
- **Construction:** One 2040x1410 picture on its own page.
- **Notes:** Kept much darker than the base scene, so the fire frames and gold numbers of the bonus are the brightest things on screen.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 16% · saturation 95% · contrast 47% · warm 94% / cool 0%
- **Palette (measured):** #730620 dark red 54%, #310305 black 24%, #f17008 orange 6%, #ee1204 red 5%, #080101 black 4%, #ae1008 red 4%

### Base game background (portrait)

`default_prt_portrait_webp80_jpg-0` · atlas · 1 parts · largest 1410×2040 · sheet `sheets/default_prt_portrait_webp80_jpg-0.webp`

- **Role:** The base-game scene for an upright phone (sprite baseGameBg_prt). The portrait layout was not played in this run.
- **Subject:** The same temple chamber recomposed tall: the glowing break in the wall in the upper middle, pillars close at both sides, a long cobbled floor below.
- **Style:** The same flat, hard-edged painting as the landscape version.
- **Rendering:** The same handling; the light area is larger in the frame, and the top and bottom fall to black where the logo and controls sit (inference from the dark bands).
- **Colour:** Measured 65% warm to 32% cool: salmon and red stone (#ca8368, #c94946), cream light (#f2d088, #fbf5e1), blue floor and shadow (#24416b, #3d82ac).
- **Lighting:** Back-lit from the opening, with a wide white bloom around it.
- **Ambience:** The same expectant chamber; a little brighter and more open than the landscape cut.
- **Materials:** Stone, brick, cobbles, light.
- **Variants:** The landscape version (baseGameBg) is the other layout of this piece.
- **Motion:** A still picture.
- **Construction:** One 1410x2040 picture on its own page.
- **Notes:** A recomposition, not a crop: the floor is extended and the pillars are moved in.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 50% · saturation 49% · contrast 62% · warm 65% / cool 32%
- **Palette (measured):** #ca8368 orange 14%, #f2d088 orange 13%, #24416b dark blue 11%, #c94946 red 10%, #150f1f black 9%, #fbf5e1 light gold 8%

### Bonus background (portrait)

`default_prt_portrait_webp80_jpg-1` · atlas · 1 parts · largest 1410×2040 · sheet `sheets/default_prt_portrait_webp80_jpg-1.webp`

- **Role:** The bonus scene for an upright phone (sprite bonusBg_prt). Not played in this run.
- **Subject:** The same crater rim and red spiral sky, recomposed tall with the crater in the lower middle and a long dark foreground.
- **Style:** As the landscape version.
- **Rendering:** As the landscape version; top and bottom thirds fall to black.
- **Colour:** Dark crimson #790625 (60%) and near black #270208, red #b80e10, small orange and magenta accents (#ed9214, #c7045e).
- **Lighting:** Lit from the lava below and the magenta haze behind.
- **Ambience:** The same heavy, hot mood.
- **Materials:** Lava, rock, cloud, embers.
- **Variants:** Landscape version: bonusBg.
- **Motion:** A still picture.
- **Construction:** One 1410x2040 picture on its own page.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 15% · saturation 95% · contrast 39% · warm 90% / cool 0%
- **Palette (measured):** #790625 dark red 60%, #270208 black 20%, #b80e10 red 8%, #ed9214 orange 4%, #c7045e magenta 3%, #d34e13 orange 2%

### Opening sequence sky

`intro_jpg` · atlas · 1 parts · largest 2044×2044 · sheet `sheets/intro_jpg.webp`

- **Role:** The back layer of the opening sequence that plays when the game is entered: the sky behind the erupting volcano.
- **Subject:** A red spiral of cloud over a magenta and violet haze with faint mountain shapes at the bottom.
- **Style:** Flat graphic painting, softer than the game backgrounds.
- **Rendering:** Large soft gradients below, hard-edged cloud bands above.
- **Colour:** Dark magenta #780539 (73%), near black #2f020e, magenta #9a036d and a little red #b40507; measured vivid (saturation 0.95) and dark.
- **Lighting:** The haze glows from below, as if lit by the volcano that is placed in front of it.
- **Ambience:** Ominous and theatrical.
- **Materials:** Cloud and haze.
- **Variants:** One version.
- **Motion:** In the opening sequence the volcano, lava, fire and title are layered over it (see the opening sequence parts).
- **Construction:** One 2044x2044 square page, larger than the view, so it can be scaled or moved (inference).
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 12% · saturation 95% · contrast 16% · warm 73% / cool 0%
- **Palette (measured):** #780539 dark magenta 73%, #2f020e black 17%, #9a036d magenta 5%, #070103 black 3%, #b40507 red 2%

### Opening sequence parts

`intro_png` · atlas · 23 parts · largest 848×551 · sheet `sheets/intro_png.webp`

- **Role:** The cut-out pieces of the opening sequence: the volcano erupts, flaming rocks fly at the camera, the title TRIPLE CASH ERUPTION lands and the screen burns to yellow before the reels appear (four real screens show it).
- **Subject:** A pink-red volcano cone in two pieces (front and back rim), lava streams, a fire burst, smoke puffs in red-orange and in grey, a flaming rock, fog, dust, rays, and the two title words as lettering.
- **Style:** Cartoon-graphic: the cone is faceted in flat pinks and reds, the smoke is drawn as scalloped puffs with a stipple texture.
- **Rendering:** Flat shapes with hard edges for rock and smoke, soft glow for lava and fire; the title is the game's bevelled red and gold lettering.
- **Colour:** Hot pink and red (#fd1d77, #cc162e, #990916) on dark red (#5d040b), with orange and yellow fire (#f58d1f, #fce526).
- **Lighting:** The cone is lit from its own crater and from a pink glow piece placed behind it.
- **Ambience:** A short disaster-film opening, loud and bright.
- **Materials:** Rock, lava, fire, smoke, fog.
- **Variants:** Fire and smoke come in small numbered sets (intro_tr_fire_00, _05, _07_00; intro_volcano_smoke a, b, c).
- **Motion:** A Spine 4.0 skeleton (binary .skel, not drawn by this run's tools) moves these pieces; in the real screens the smoke column grows, three flaming rocks cross the view from top right to bottom left, and the picture ends in a full yellow fire wipe.
- **Construction:** 23 parts on one 2006x1331 page plus the sky page; the layout names one animation, intro.
- **Notes:** The opening spends its budget on the volcano, which then appears in the game only as three small cones and a symbol.
- **Measured:** dark, vivid, warm, medium contrast · brightness 24% · saturation 91% · contrast 25% · warm 93% / cool 0% · brighter towards: bottom (4), top-left (2), left (2)
- **Palette (measured):** #1e0102 black 25%, #5d040b dark red 21%, #fd1d77 red 19%, #990916 red 9%, #f58d1f orange 7%, #cc162e red 5%

### Red cloud vortex (tutorial and feature panel background)

`swirlAnims_3_jpg` · atlas · 1 parts · largest 2042×2042 · sheet `sheets/swirlAnims_3_jpg.webp`

- **Role:** The background of the intro panel (COLLECT FIREBALLS) and of the bonus start panel (FEATURES ACTIVE); the sprite sheet also carries it as tutorialBg.
- **Subject:** A spiral of red storm cloud turning into a bright centre, with darker cloud walls around it.
- **Style:** Painterly, with far more texture than the game backgrounds: billowing cloud edges and fine wisps.
- **Rendering:** Soft, detailed cloud forms; the light falls off to near black at the corners.
- **Colour:** Dark red #2d1215 (78%) and #772024, with red #bc2929 and #e7473a in the spiral.
- **Lighting:** The spiral's core is the light; everything else is rim-lit cloud.
- **Ambience:** The eye of a firestorm: a calm, dark ground for panels of text.
- **Materials:** Cloud and smoke.
- **Variants:** A masked copy with a soft round edge ships as swirlAnims_png.
- **Motion:** The layout names an animation idleSwirlBgAnim; in the real screens of the panels the cloud is the ground and red particle clouds turn over it (inference from the particle frames in swirlAnims_jpg).
- **Construction:** One 2042x2042 page.
- **Notes:** The only art in the game painted in this soft, textured way.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 13% · saturation 60% · contrast 24% · warm 99% / cool 0% · brighter towards: top-left (1)
- **Palette (measured):** #2d1215 dark red 78%, #772024 dark red 13%, #bc2929 red 6%, #e7473a red 2%

### Red cloud vortex, masked

`swirlAnims_png` · atlas · 1 parts · largest 1363×1375 · sheet `sheets/swirlAnims_png.webp`

- **Role:** The same vortex cut to a soft-edged disc with transparency, so it can turn over another ground (inference from the alpha edge).
- **Subject:** The spiral of red cloud inside a feathered round mask.
- **Style:** As the full vortex.
- **Rendering:** As the full vortex; the edge fades over a wide band.
- **Colour:** Dark red #350c0d (63%), #7b0f0f, red #ca1915.
- **Lighting:** Lit from its centre.
- **Ambience:** As the full vortex.
- **Materials:** Cloud.
- **Variants:** The unmasked square is swirlAnims_3_jpg.
- **Motion:** Meant to rotate (inference: a round, feathered copy of a square picture has no other use).
- **Construction:** One 1363x1375 page with alpha.
- **Measured:** dark, vivid, warm, low contrast · brightness 12% · saturation 79% · contrast 22% · warm 100% / cool 0% · brighter towards: top-left (1)
- **Palette (measured):** #350c0d dark red 63%, #7b0f0f dark red 21%, #ca1915 red 15%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Win box

`winBox_png` · atlas · 16 parts · largest 198×198 · sheet `sheets/winBox_png.webp`

- **Role:** A plain square frame for a winning cell, with a moving shine.
- **Subject:** A thin silver-white square outline and 15 frames of the same outline with a highlight travelling around it.
- **Style:** Neutral, almost undesigned.
- **Rendering:** A thin line with a soft glow.
- **Colour:** Grey #60687a and white #ecedef: the only cool, colourless art in the game.
- **Lighting:** The highlight is the light.
- **Ambience:** Functional.
- **Materials:** Metal line.
- **Variants:** One.
- **Motion:** 15 frames (Box0001 to Box0015), animation winBox.
- **Construction:** 16 parts, 194x194, with a tiny skeleton of its own.
- **Notes:** Not seen in the real screens of this run, where winning cells wear the fire frame instead (inference: a fallback or a shared part).
- **Measured:** bright, muted, neutral, medium contrast, strong highlights · brightness 64% · saturation 12% · contrast 57% · warm 0% / cool 100%
- **Palette (measured):** #60687a grey 47%, #ecedef white 36%, #969aa6 grey 9%, #bdc1c8 grey 7%

### Fire win frame

`winFrameAnims_png` · atlas · 30 parts · largest 200×180 · sheet `sheets/winFrameAnims_png.webp`

- **Role:** The burning frame around each winning cell (seen on the bells and the sevens in the real screens).
- **Subject:** A rounded square of orange fire with a bright yellow core line, licking outwards.
- **Style:** Stylised real flame.
- **Rendering:** Soft, glowing, drawn frame by frame.
- **Colour:** Orange #fd6f1f (65%), #fccc59, light gold #fff094.
- **Lighting:** Self-lit.
- **Ambience:** The win is on fire.
- **Materials:** Flame.
- **Variants:** One colour; the fireball symbols have their own coloured borders.
- **Motion:** 30 frames (winframe_00 to _29), animation winFrame; the flame crawls around the square.
- **Construction:** 30 parts of about 200x180 with alpha.
- **Notes:** While it plays the rest of the board is dimmed, so the frames and the gold number carry the win.
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect · brightness 63% · saturation 79% · contrast 42% · warm 100% / cool 0%
- **Palette (measured):** #fd6f1f orange 65%, #fccc59 orange 32%, #fff094 light gold 3%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Symbol stills, fireballs, reel frames and controls

`default_shared_webp80_png-1` · atlas · 106 parts · largest 1081×652 · sheet `sheets/default_shared_webp80_png-1.webp`

- **Role:** The main sprite page: every reel symbol as a still and as a spin-blur copy, the four fireball stills, the wild, the reel frames, the jackpot labels and plates, the bonus buy button and the round control buttons.
- **Subject:** Two sevens (red with a gold ribbon band, blue), a gold bell, watermelon, grapes, plum, orange, lemon and cherries; green, blue, red and orange burning globes in square coloured borders; a WILD tile showing the volcano under a sunset sky; teal reel cells in a thin red frame; MAJOR, MINOR, MINI and GRAND words with 2X, 3X, 5X.
- **Style:** Classic fruit-machine set drawn as glossy, rounded 3D-look objects; each fruit carries a small engraved swirl or Greek-key mark, and the cells behind low symbols have a faint Greek-key pattern.
- **Rendering:** Smooth airbrushed volumes with a hard white specular spot and a tiny four-point sparkle on each symbol, a thin gold rim on sevens and bell; no outlines.
- **Colour:** Teal cells (#079a8f, #04655d) against warm symbols: the page measures 45% warm to 42% cool. Jackpot words are colour-coded: GRAND orange, MAJOR magenta, MINOR blue, MINI green.
- **Lighting:** Each symbol is lit from the top left with a strong highlight and a soft shadow underneath; the fireballs are self-lit and glow past their borders.
- **Ambience:** Bright, clean and familiar: a fruit machine with one loud new element.
- **Materials:** Enamel-like fruit, polished gold bell, lacquered sevens, molten globes.
- **Variants:** Every symbol has a _static and a _blur sprite (the blur is a vertical smear used while the reels turn: inference from the real spin screens). Jackpot labels come in 2x, 3x and 5x versions.
- **Motion:** Stills; movement is in the symbolsAnims units.
- **Construction:** 106 sprites on one 1975x1988 page; symbol stills are about 150x130 in a 180x158 cell.
- **Notes:** Nine paying symbols and a wild are all the picture symbols there are; the money is in the four fireballs, which are also the brightest and most saturated things on the board.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 35% · saturation 70% · contrast 48% · warm 45% / cool 42% · brighter towards: top (21), top-left (12), right (1)
- **Palette (measured):** #160a0a black 16%, #273635 dark cyan 15%, #079a8f cyan 14%, #04655d dark cyan 7%, #6a596f grey 4%, #f9f7f4 light orange 2%

### 5X glow and smoke puff

`symbolsAnims_2_jpg` · atlas · 31 parts · largest 566×500 · sheet `sheets/symbolsAnims_2_jpg.webp`

- **Role:** A glowing 5X tag and a puff of white smoke, both as frames on black.
- **Subject:** 5X in white with a magenta glow; a small white cloud that grows and breaks up.
- **Style:** Neon sign lettering; simulated smoke.
- **Rendering:** Soft glow on black.
- **Colour:** Mostly white and grey with magenta (#b7518c, #871f52); measured muted (saturation 0.07).
- **Lighting:** Self-lit.
- **Ambience:** A cool neon accent in a fire game.
- **Materials:** Light, smoke.
- **Variants:** Only the 5X has this glow sequence among the captured pages.
- **Motion:** 5x: 22 frames; nose_particle: 9 frames here and more on the next page.
- **Construction:** 31 parts on a 1947x1764 page.
- **Notes:** The file name nose_particle is the studio's own; what it is attached to was not seen.
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 57% · saturation 7% · contrast 48% · warm 11% / cool 0%
- **Palette (measured):** #ebebeb white 34%, #beb6bc grey 19%, #040202 black 19%, #91858b grey 12%, #60585a grey 8%, #3d292e dark red 3%

### Symbol animation parts: red and orange fireballs, bonus globes, expanded wild

`symbolsAnims_2_png` · atlas · 78 parts · largest 189×479 · sheet `sheets/symbolsAnims_2_png.webp`

- **Role:** More layered parts: the red and orange fireball loops, the four larger bonus globes with their square frames, and the pieces of the tall expanded wild.
- **Subject:** Red and orange plasma globes; four clean globes (bonus_blue, _green, _orange, _red) and four neon square frames; for the wild: a tall gold frame, a tall volcano picture with a lava stream, a sunset sky strip, a rocky foreground, smoke, sparkles and glow shapes.
- **Style:** As above; the wild's pictures are small painted landscapes, more illustrative than the rest of the symbols.
- **Rendering:** Globes as above; the wild's landscape has painted cloud and rock detail at very small size.
- **Colour:** Red #ef2f21 and #f6714e, orange #f6a94e, gold #fde279.
- **Lighting:** Self-lit globes; the wild's volcano glows from its lava stream.
- **Ambience:** The hottest symbols on the board.
- **Materials:** Plasma, lava, rock, sky.
- **Variants:** bonus_ globes are the larger, cleaner versions used when values are held in the bonus (inference from the bonus screens, where every held cell is an orange globe in a fire ring).
- **Motion:** 30-frame loops for red and orange; the expanding wild's pieces (frame, sky, volcano, rocks, smoke) are separate so the picture can grow to three cells (the paytable calls it the Expanding Wild Feature; it was not seen expanding in this run).
- **Construction:** 78 parts on a 1925x1336 page.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 48% · saturation 66% · contrast 68% · warm 86% / cool 10% · brighter towards: left (9), top-right (2), bottom-right (2)
- **Palette (measured):** #ef2f21 red 25%, #f6714e red 11%, #fac5b3 light red 8%, #f6a94e orange 8%, #fdefe9 light orange 6%, #0b070b black 6%

### Smoke puff, later frames

`symbolsAnims_3_jpg` · atlas · 9 parts · largest 566×500 · sheet `sheets/symbolsAnims_3_jpg.webp`

- **Role:** The rest of the white smoke puff sequence.
- **Subject:** A white cloud thinning to grey wisps on black.
- **Style:** Simulated smoke.
- **Rendering:** Soft, grey, on black.
- **Colour:** Greys only (#767676, #3a3a3a, #b7b7b7).
- **Lighting:** None.
- **Ambience:** Aftermath.
- **Materials:** Smoke.
- **Variants:** One.
- **Motion:** 9 frames (nose_particle_00014 onwards).
- **Construction:** 9 parts of 566x500 on a 1698x1500 page.
- **Notes:** A large page for nine frames of smoke: effects, not symbols, take the texture space in this game.
- **Measured:** mid-tone, muted, neutral, medium contrast, hard-edged · brightness 44% · saturation 0% · contrast 44% · warm 0% / cool 0%
- **Palette (measured):** #767676 grey 42%, #3a3a3a grey 18%, #b7b7b7 grey 17%, #090909 black 14%, #e0e0e0 white 9%

### Spin swirl

`symbolsAnims_3_png` · atlas · 30 parts · largest 160×160 · sheet `sheets/symbolsAnims_3_png.webp`

- **Role:** A white spiral used on a symbol position, 30 frames.
- **Subject:** A soft white spiral of two turns that rotates.
- **Style:** Simple brush shape.
- **Rendering:** White with soft edges and alpha.
- **Colour:** White #fdfdfd; colour would come from tinting (inference).
- **Lighting:** None.
- **Ambience:** Motion without content.
- **Materials:** Light or vapour.
- **Variants:** One.
- **Motion:** spinParticle, 30 frames of rotation.
- **Construction:** 30 parts of 160x160.
- **Notes:** Not identified in the real screens.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 98% · saturation 0% · contrast 12% · warm 0% / cool 0%
- **Palette (measured):** #fdfdfd white 95%, #d1d1d1 grey 5%

### Fireball landing ring

`symbolsAnims_4_jpg` · atlas · 22 parts · largest 160×160 · sheet `sheets/symbolsAnims_4_jpg.webp`

- **Role:** A ring of white smoke-light that opens when a fireball lands (folder FireballLandEffect).
- **Subject:** A ragged white ring with a dark centre on black.
- **Style:** Simulated smoke ring.
- **Rendering:** White on black, to be tinted and added (inference).
- **Colour:** White and greys only.
- **Lighting:** Self-lit.
- **Ambience:** Impact.
- **Materials:** Smoke, light.
- **Variants:** One, colourless.
- **Motion:** glow, 22 frames.
- **Construction:** 22 parts of 160x160.
- **Notes:** Kept grey so one sequence can serve all four fireball colours (inference).
- **Measured:** bright, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 83% · saturation 0% · contrast 56% · warm 0% / cool 0%
- **Palette (measured):** #fbfbfb white 61%, #c9c9c9 grey 17%, #9a9a9a grey 10%, #6a6a6a grey 6%, #3a3a3a grey 4%, #0b0b0b black 2%

### Wild volcano fire

`symbolsAnims_5_jpg` · atlas · 38 parts · largest 197×151 · sheet `sheets/symbolsAnims_5_jpg.webp`

- **Role:** The fire that bursts from the volcano on the wild symbol.
- **Subject:** A small orange fireball that swells, throws sparks and turns to pale smoke.
- **Style:** Simulated explosion at symbol size.
- **Rendering:** Soft, on black.
- **Colour:** Muted orange and brown (#bd9f94, #5c4842) with cream highlights (#f6d29e, #f9f6e1).
- **Lighting:** Self-lit.
- **Ambience:** A small eruption inside one cell.
- **Materials:** Fire, smoke.
- **Variants:** One.
- **Motion:** W01, 38 frames.
- **Construction:** 38 parts of 197x151.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 47% · saturation 36% · contrast 45% · warm 95% / cool 0%
- **Palette (measured):** #bd9f94 orange 20%, #120b08 black 18%, #5c4842 red 16%, #f6d29e light orange 12%, #f9f6e1 light gold 6%, #937369 red 6%

### Symbol light effects: seven outline, wild frame fire, bell sweep, multiplier splash

`symbolsAnims_jpg` · atlas · 84 parts · largest 264×558 · sheet `sheets/symbolsAnims_jpg.webp`

- **Role:** Light layers for symbol wins: a burning outline of the seven, a horizontal fire line for the wild's frame, a white sweep for the bell and a red splash for a multiplier.
- **Subject:** A glowing orange outline of a 7 on black; a short bar of yellow fire; white feather-like streaks; a ragged ring of red and yellow lava drops.
- **Style:** Hand-drawn effect frames.
- **Rendering:** Pictures on black with soft glow, to be added as light (inference from the black grounds; the blend mode is in the binary skeleton and was not read).
- **Colour:** Black #0c0602, gold #f5e75d and light gold #faf8ce, brown #5c4309.
- **Lighting:** These are the light.
- **Ambience:** A flash for each kind of win.
- **Materials:** Fire, light.
- **Variants:** One effect per symbol family: sevens, wild, bell, multiplier.
- **Motion:** frame_sevens_seq 21 frames, w01_frame_seq 31, bell_sweep 10, multiplier_splash 20. In the real win screens the sevens flash to a pale gold glow for a moment.
- **Construction:** 84 parts on an 1872x808 page without alpha; two empty black cells are placeholders.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged, strong highlights · brightness 40% · saturation 57% · contrast 47% · warm 82% / cool 0%
- **Palette (measured):** #0c0602 black 31%, #5c4309 brown 14%, #faf8ce light gold 9%, #f5e75d gold 9%, #9a830f brown 7%, #c5ae28 gold 6%

### Symbol animation parts: fireballs, borders, fruit layers

`symbolsAnims_png` · atlas · 293 parts · largest 142×286 · sheet `sheets/symbolsAnims_png.webp`

- **Role:** The layered parts the symbol animations are built from: 30-frame loops of the blue and green fireballs, their flaming square borders in four colours, and each fruit, bell and seven split into body, gold outline and shadow.
- **Subject:** Boiling plasma globes; open square brackets of blue, green, red and orange flame; the fruit again as clean cut-outs with a separate thin gold contour (melon_a, plum_a, lemon_a) and a soft black shadow shape; the bell in three pieces (top, bottom, shadow); 2X, 3X and 5X tags; a blurred wild.
- **Style:** As the stills; the fireballs are closer to a rendered fluid simulation than to drawing.
- **Rendering:** Globes: bright veins over a dark core with a soft halo, changing every frame. Fruit: the same airbrushed volumes as the stills.
- **Colour:** Blue #08589f and light cyan #9becfd, green #0cc70d and #95fe95; measured 53% cool, the coolest unit in a warm game.
- **Lighting:** Globes and borders are self-lit; fruit keep their top-left light.
- **Ambience:** Energy held in a box.
- **Materials:** Plasma, flame, enamel fruit, gold wire.
- **Variants:** Fireball loops in blue and green here, red and orange on the next page; borders in all four colours; one multiplier tag per value, colour-coded 2X blue, 3X green, 5X magenta.
- **Motion:** Frame loops of 30 frames for each fireball and border (inference from the parts: a win plays by pulsing the gold contour and shadow layers around the fruit; the symbols' skeleton file was not among the captured files, so this is read from the parts and the win screens).
- **Construction:** 293 parts on a 2047x2045 page.
- **Notes:** A fruit is three layers (body, gold contour, shadow), which is all a win highlight needs.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 57% · saturation 68% · contrast 60% · warm 29% / cool 53% · brighter towards: left (12), bottom (9), top-left (8)
- **Palette (measured):** #08589f blue 13%, #0cc70d green 11%, #95fe95 light green 8%, #effcf2 light green 7%, #9becfd light cyan 7%, #0b0809 black 5%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The three feature volcanoes

`volcanoAnims_png` · atlas · 20 parts · largest 314×261 · sheet `sheets/volcanoAnims_png.webp`

- **Role:** The game has no figures; its heroes are three small volcanoes above the reels (red MULTIPLIER, green COLLECT, blue DOUBLE) that take the fireballs of their colour, and stand large beside the reels in the bonus. This unit holds their cones, lava, labels and rocks.
- **Subject:** Three cones of the same faceted shape in red, green and blue; five levels of lava running down a cone, each with a glow copy; the labels MULTIPLIER, COLLECT, DOUBLE and a 3x; three lumps of cracked lava rock.
- **Style:** Low-polygon-looking cones in flat facets, cartoon simple; the rocks are painted with more realism than anything else in the unit.
- **Rendering:** Hard-edged facets in three or four tones for the cones; lava as soft yellow-to-red ribbons; rocks with glowing cracks.
- **Colour:** Gold lava #fdbf06 (28%), dark red #610e0d and red #a9130e, pure blue #0504a4; the green cone is the third hue.
- **Lighting:** Cones lit from above; lava and cracks self-lit, with a separate orange outer glow piece (volcano_OuterGlow).
- **Ambience:** Toy-like and friendly: three coloured targets, not a threat.
- **Materials:** Rock, lava.
- **Variants:** One cone shape in three colours; lava in five levels; three rocks.
- **Motion:** A Spine 4.0 skeleton (binary, not drawn here). The layout names animations level1, level3, level6, blink, Idle_1, Idle_2 and multiplierSmoke; in the real screens a fireball flies to its volcano, the lava rises, a halo of fire sits over the crater, and at the trigger all three erupt and throw rocks at the screen.
- **Construction:** 20 parts on one page; the eruption, smoke, hit and transition frames fill twelve more pages (the effects units).
- **Notes:** A meter drawn as a character: the amount of lava on each cone is the only progress display the feature has.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 42% · saturation 82% · contrast 43% · warm 77% / cool 18% · brighter towards: top-right (3), top (3)
- **Palette (measured):** #fdbf06 gold 28%, #610e0d dark red 11%, #130b0a black 10%, #0504a4 blue 7%, #a9130e red 5%, #fef419 gold 3%


## Logo and title

The game's own wordmark.

### Logo with fireball (loading screen)

`de9599e6fcd85ce5d973` · atlas · 1 parts · largest 667×583 · sheet `sheets/de9599e6fcd85ce5d973.webp`

- **Role:** The title as shown on the loading screen: the wordmark over a burning globe.
- **Subject:** TRIPLE in tall red letters above CASH ERUPTION in orange-to-yellow letters, both with a gold bevel and a dark red extrusion, in front of a molten orange globe with a yellow halo.
- **Style:** Casino display lettering: a flared serif face with chiselled bevels; the globe is the game's fireball symbol at large size.
- **Rendering:** Smooth gradients inside the letters, a thin gold rim, a hard dark drop; the globe has painted lava cracks and a soft outer glow.
- **Colour:** Orange #ef6f1c, gold #fde60e, red #e41508 on dark red #731a06; fully warm (measured warm 1.0).
- **Lighting:** Letters lit from above (lighter top edge of the bevel); the globe is self-lit and throws the halo.
- **Ambience:** Hot and showy.
- **Materials:** Polished metal lettering, molten rock.
- **Variants:** The in-game logo is the same wordmark without the globe.
- **Motion:** Still on the loading screen.
- **Construction:** One 667x583 PNG outside the atlases.
- **Notes:** TRIPLE is set larger than the family name CASH ERUPTION: the version word is the hero of the logo.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 47% · saturation 86% · contrast 87% · warm 100% / cool 0%
- **Palette (measured):** #ef6f1c orange 17%, #731a06 dark red 15%, #fde60e gold 13%, #1d0b02 black 10%, #e41508 red 9%, #ae4c12 brown 5%

### In-game logo

`default_land_shared_webp80_png` · atlas · 1 parts · largest 288×98 · sheet `sheets/default_land_shared_webp80_png.webp`

- **Role:** The wordmark at the top left of the base game and the bonus, and at the top of the intro panel.
- **Subject:** TRIPLE over CASH ERUPTION, the same lettering as the loading logo, at small size.
- **Style:** Flared serif display lettering with bevel.
- **Rendering:** Gradient fill, gold rim, dark red extrusion; legible at 288x98.
- **Colour:** Dark red #771204, orange #da6822, red #e01208, gold #fad334.
- **Lighting:** Top-lit bevel.
- **Ambience:** As the loading logo.
- **Materials:** Polished metal.
- **Variants:** A second copy (GameLogo, 288x98) is on the portrait interface page; the loading logo adds the fireball.
- **Motion:** Still in the screens captured.
- **Construction:** One sprite, gameLogo, on its own small page.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 40% · saturation 87% · contrast 76% · warm 100% / cool 0%
- **Palette (measured):** #771204 dark red 24%, #da6822 orange 23%, #e01208 red 19%, #fad334 gold 10%, #f5a213 orange 5%, #2d0301 black 4%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Big win text fire

`bigWinAnims_jpg` · atlas · 20 parts · largest 160×144 · sheet `sheets/bigWinAnims_jpg.webp`

- **Role:** A small fire loop for the big win lettering.
- **Subject:** A knot of red and yellow flame with dark gaps, like lava seen through cracks.
- **Style:** Hand-drawn stylised fire.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Dark red #5a1704, brown #923307, orange #da980b, gold #f6e411.
- **Lighting:** Self-lit.
- **Ambience:** Smouldering.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** big_win_txt_fire, 20 frames.
- **Construction:** 20 parts of 160x144.
- **Notes:** Probably masked into the letters (inference from its name).
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 36% · saturation 94% · contrast 53% · warm 100% / cool 0%
- **Palette (measured):** #1e0702 black 18%, #5a1704 dark red 17%, #923307 brown 17%, #da980b orange 16%, #f6e411 gold 12%, #b65e07 brown 9%

### Big win lettering, coins and shines

`bigWinAnims_png` · atlas · 299 parts · largest 482×359 · sheet `sheets/bigWinAnims_png.webp`

- **Role:** The pieces of the win celebration: the tier words and everything that flies around them. No celebration tier was reached in this run, so this is read from the parts only.
- **Subject:** The words BIG, WIN, MEGA, EPIC, HUGE and MASSIVE in letters of cracked, glowing lava rock; every letter again as a small burning glyph (20 frames each); a spinning gold coin, a diamond, a star flare, a lens shine and debris.
- **Style:** Heavy slab lettering made of molten rock: dark crust with orange cracks, a bright rim.
- **Rendering:** Painted texture inside hard letter shapes, soft orange glow outside; the coin is a smooth gold render in six turning frames.
- **Colour:** Orange #f36b26 (44%) and #faac36, dark red #5d160f; fully warm.
- **Lighting:** The cracks and rims are self-lit; a separate round glow (big_win_shine0) sits behind.
- **Ambience:** Weighty and hot: the words look as if they came out of the crater.
- **Materials:** Lava rock, gold, diamond.
- **Variants:** Five tier words over one WIN; per-letter burning copies for the letters a, b, c, e, g, h, i, m, n, p, s, u, v.
- **Motion:** A Spine 4.0 skeleton (binary, not drawn here); the layout names winTier1In and winIdle. The per-letter 20-frame shines suggest each letter flares in turn (inference).
- **Construction:** 299 parts on a 2016x653 page: six words, 13 letters x 20 frames, coins in 6 frames, single flares.
- **Notes:** The celebration is built from lettering and light alone: no figure, no scene.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 52% · saturation 75% · contrast 44% · warm 100% / cool 0% · brighter towards: top-right (4), top (3), top-left (1)
- **Palette (measured):** #f36b26 orange 44%, #faac36 orange 15%, #5d160f dark red 9%, #fbb574 orange 8%, #82554b red 7%, #e31305 red 2%

### Fireworks, fading frames

`fireworks_2_jpg` · atlas · 3 parts · largest 800×800 · sheet `sheets/fireworks_2_jpg.webp`

- **Role:** The last frames of the firework burst.
- **Subject:** A wide, thinning spray of orange and gold dots.
- **Style:** As the first page.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Brown and orange (#ba6330, #867151, #caa970) on black.
- **Lighting:** Self-lit.
- **Ambience:** Dying sparks.
- **Materials:** Sparks.
- **Variants:** One.
- **Motion:** firework1_00009 to _00013, 3 frames of 800x800.
- **Construction:** 3 parts on a 1601x1601 page.
- **Measured:** dark, saturated, warm, medium contrast, hard-edged · brightness 19% · saturation 42% · contrast 38% · warm 100% / cool 0%
- **Palette (measured):** #100b0a black 60%, #4b3122 brown 12%, #ba6330 orange 10%, #867151 orange 9%, #7c4225 brown 5%, #caa970 orange 4%

### Fireworks

`fireworks_jpg` · atlas · 11 parts · largest 700×700 · sheet `sheets/fireworks_jpg.webp`

- **Role:** Gold firework bursts; the layout names an animation firework2. Not seen in play in this run.
- **Subject:** A yellow-white burst that opens into a round spray of gold dots and fades to faint specks.
- **Style:** Photographic-looking particle burst.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Orange-gold #deb53f and #b5792f, light gold #f6ec6a, on black.
- **Lighting:** Self-lit.
- **Ambience:** Festive; the only effect in the game that is not fire or lava.
- **Materials:** Sparks.
- **Variants:** One burst in frames of growing size (250, 400, 700 px).
- **Motion:** firework1, 11 frames on this page and 3 more on the next.
- **Construction:** 11 parts on a 2002x1552 page.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 35% · saturation 52% · contrast 41% · warm 100% / cool 0%
- **Palette (measured):** #110c0a black 40%, #deb53f orange 20%, #4b3521 brown 11%, #805c2f brown 10%, #b5792f orange 10%, #f6ec6a gold 6%


## Effects

Frame sequences, glows, particles and transitions.

### Bonus anticipation frame

`bonusAnticipation_jpg` · atlas · 30 parts · largest 310×288 · sheet `sheets/bonusAnticipation_jpg.webp`

- **Role:** A square of fire around a cell while the game waits to see whether the bonus triggers (animation bonusAnticipation in the layout).
- **Subject:** A square ring of red-orange flame with a white-hot inner line.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Red #d33f29 (25%) and #f08261, near white #fcf3e6.
- **Lighting:** Self-lit.
- **Ambience:** Tension.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** bonusAnticipation, 30 frames.
- **Construction:** 30 parts of 310x288.
- **Notes:** Redder and whiter than the orange win frame: the hotter of the two cell frames.
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged, strong highlights · brightness 55% · saturation 56% · contrast 63% · warm 100% / cool 0%
- **Palette (measured):** #d33f29 red 25%, #fcf3e6 light orange 22%, #f08261 red 19%, #f7c5a4 light orange 11%, #812013 dark red 10%, #290a06 black 9%

### Bonus buy spark burst

`buyBonusAnims_2_jpg` · atlas · 12 parts · largest 650×436 · sheet `sheets/buyBonusAnims_2_jpg.webp`

- **Role:** The burst of sparks when a bonus buy card is shown or chosen (inference from its skeleton, buyBonusAnims).
- **Subject:** A tight knot of yellow-white sparks that scatters outwards.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Light gold #fefdec and #f7f6a2, yellow #aea852, on black.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Sparks.
- **Variants:** One.
- **Motion:** explosion, 12 frames here (00 to 22).
- **Construction:** 12 parts of 650x436 on a 1958x1754 page.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged, strong highlights · brightness 36% · saturation 39% · contrast 52% · warm 92% / cool 0%
- **Palette (measured):** #090903 black 42%, #474115 brown 14%, #766f2d brown 11%, #aea852 yellow 11%, #fefdec light gold 9%, #f7f6a2 light gold 6%

### Bonus buy spark burst, fading frames

`buyBonusAnims_3_jpg` · atlas · 9 parts · largest 650×436 · sheet `sheets/buyBonusAnims_3_jpg.webp`

- **Role:** The end of the same spark burst.
- **Subject:** A thin cloud of dim gold specks.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Brown-gold #433912, #746522, #a69232 on black; measured dark (brightness 0.10).
- **Lighting:** Self-lit.
- **Ambience:** Fading.
- **Materials:** Sparks.
- **Variants:** One.
- **Motion:** explosion, 9 frames (24 to 40).
- **Construction:** 9 parts of 650x436.
- **Measured:** dark, saturated, warm, low contrast, hard-edged · brightness 10% · saturation 39% · contrast 23% · warm 100% / cool 0%
- **Palette (measured):** #090703 black 76%, #433912 brown 14%, #746522 brown 7%, #a69232 gold 3%

### Collector explosion

`collectorExplosionAnims_jpg` · atlas · 22 parts · largest 151×141 · sheet `sheets/collectorExplosionAnims_jpg.webp`

- **Role:** The same hit burst as its own small skeleton (animation collectorExplosion in the layout); in the bonus screens a burst of this kind sits on a cell as a value is collected or multiplied.
- **Subject:** A yellow-white star burst with an orange edge.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Gold #faf351 (25%), orange #ed6f1d, brown #4f3015.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** volcanoHit1, 22 frames.
- **Construction:** 22 parts of 151x141 on a 1673x285 page.
- **Notes:** Third copy of this sequence in the package.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 49% · saturation 65% · contrast 36% · warm 91% / cool 0%
- **Palette (measured):** #faf351 gold 25%, #0f0704 black 22%, #ed6f1d orange 12%, #4f3015 brown 10%, #ecad33 orange 6%, #892c0c dark red 4%

### Embers (collector)

`fgCounterCollectAnims_2_jpg` · atlas · 22 parts · largest 164×193 · sheet `sheets/fgCounterCollectAnims_2_jpg.webp`

- **Role:** Rising embers behind the collector plate.
- **Subject:** A scatter of small orange sparks.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Brown and orange (#57260f, #8a4423, #b86034) on black.
- **Lighting:** Self-lit.
- **Ambience:** Background heat.
- **Materials:** Embers.
- **Variants:** One.
- **Motion:** fireEmbers, 22 frames (00030 to 00051).
- **Construction:** 22 parts of 164x193.
- **Notes:** The same ember frames ship again with the respin counter: each atlas carries its own copy.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 16% · saturation 78% · contrast 16% · warm 100% / cool 0%
- **Palette (measured):** #1b0b05 black 50%, #57260f brown 25%, #8a4423 brown 16%, #b86034 orange 9%

### Hit burst (collector)

`fgCounterCollectAnims_3_jpg` · atlas · 22 parts · largest 151×141 · sheet `sheets/fgCounterCollectAnims_3_jpg.webp`

- **Role:** The burst when a value hits the collector.
- **Subject:** A yellow-white star burst with an orange edge and a dark centre.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Gold #faf249 (26%), orange #ee6f1b and #eeaf31, brown #4f3015.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** volcanoHit1, 22 frames.
- **Construction:** 22 parts of 151x141.
- **Notes:** A copy of the volcano hit burst.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 52% · saturation 72% · contrast 37% · warm 95% / cool 0%
- **Palette (measured):** #faf249 gold 26%, #160a06 black 18%, #ee6f1b orange 12%, #4f3015 brown 10%, #eeaf31 orange 8%, #ad9637 gold 5%

### Collector fire frame

`fgCounterCollectAnims_jpg` · atlas · 16 parts · largest 585×205 · sheet `sheets/fgCounterCollectAnims_jpg.webp`

- **Role:** A burning rectangle that surrounds the collector plate (folder fireball_collector).
- **Subject:** A wide rounded rectangle of orange flame on black.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Orange #d49f50, gold #f3d986, brown #9c4b19.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** fireball_collector, 16 frames.
- **Construction:** 16 parts of 585x205.
- **Notes:** The same idea as the win frame, stretched to a plate.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 53% · saturation 67% · contrast 54% · warm 100% / cool 0%
- **Palette (measured):** #d49f50 orange 34%, #f3d986 gold 26%, #391908 brown 20%, #9c4b19 brown 19%

### Respin counter burst

`freeSpinsIndicatorAnims_2_png` · atlas · 25 parts · largest 88×92 · sheet `sheets/freeSpinsIndicatorAnims_2_png.webp`

- **Role:** A small explosion on a socket of the respin counter when a respin is used or restored (inference from its atlas).
- **Subject:** A yellow star burst that turns into a red smoke ring.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Soft-edged frames with alpha.
- **Colour:** Gold #fdf04e (32%), orange #ee4607 and #f2b322.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** explosion, 25 frames.
- **Construction:** 25 parts of at most 88x92, with alpha.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 67% · saturation 79% · contrast 39% · warm 100% / cool 0%
- **Palette (measured):** #fdf04e gold 32%, #ee4607 orange 23%, #f2b322 orange 16%, #ea7f15 orange 9%, #fef996 light gold 5%

### Respin counter glow

`freeSpinsIndicatorAnims_3_png` · atlas · 30 parts · largest 126×52 · sheet `sheets/freeSpinsIndicatorAnims_3_png.webp`

- **Role:** A glow that runs along the respin counter's edge.
- **Subject:** A short orange light bar with a soft trail, moving from the bottom edge to the top edge of a small rectangle.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Very soft (measured soft edge 0.96), with alpha.
- **Colour:** Orange #fe682d (78%) and #fec370.
- **Lighting:** Self-lit.
- **Ambience:** A small pulse.
- **Materials:** Light.
- **Variants:** One.
- **Motion:** frameGlow, 30 frames.
- **Construction:** 30 parts of about 125x52, with alpha.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 58% · saturation 76% · contrast 40% · warm 100% / cool 0% · brighter towards: top (5), bottom (5), bottom-left (5)
- **Palette (measured):** #fe682d orange 78%, #fec370 orange 19%, #ffeca3 light gold 3%

### Embers (respin counter)

`freeSpinsIndicatorAnims_jpg` · atlas · 22 parts · largest 164×193 · sheet `sheets/freeSpinsIndicatorAnims_jpg.webp`

- **Role:** Embers around the respin counter.
- **Subject:** A scatter of small orange sparks.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Brown and orange (#552612, #84462a, #b0633f) on black.
- **Lighting:** Self-lit.
- **Ambience:** Background heat.
- **Materials:** Embers.
- **Variants:** One.
- **Motion:** fireEmbers, 22 frames.
- **Construction:** 22 parts of 164x193.
- **Notes:** The same frames as the collector's embers.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 16% · saturation 75% · contrast 16% · warm 100% / cool 0%
- **Palette (measured):** #1b0b05 black 50%, #552612 brown 25%, #84462a brown 16%, #b0633f orange 9%

### Vortex particles, later frames

`swirlAnims_2_jpg` · atlas · 13 parts · largest 420×354 · sheet `sheets/swirlAnims_2_jpg.webp`

- **Role:** The rest of the red particle cloud.
- **Subject:** A round cloud of fine red particles.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Red #931b0a and dark red #360b07.
- **Lighting:** Self-lit.
- **Ambience:** A slow storm.
- **Materials:** Dust.
- **Variants:** One.
- **Motion:** swirlParticles, 13 frames (00010 to 00022).
- **Construction:** 13 parts of 420x354.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 16% · saturation 89% · contrast 10% · warm 100% / cool 0%
- **Palette (measured):** #931b0a red 66%, #360b07 dark red 34%

### Vortex particles and pink glow

`swirlAnims_jpg` · atlas · 32 parts · largest 420×354 · sheet `sheets/swirlAnims_jpg.webp`

- **Role:** Particle clouds that turn over the red vortex on the intro and feature panels.
- **Subject:** A round cloud of fine red particles; a cluster of pink, white and orange glowing dots.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Red #911e11 and #e46d5e, pink #f48ea8, light magenta #facbeb.
- **Lighting:** Self-lit.
- **Ambience:** A slow storm.
- **Materials:** Dust, light.
- **Variants:** One.
- **Motion:** swirlParticles 10 frames here, glowParticles 22 frames.
- **Construction:** 32 parts (420x354 and 324x316) on a 2046x2024 page.
- **Notes:** Pink is used here and in the intro haze: the game's fire leans to magenta rather than to pure orange.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 32% · saturation 74% · contrast 29% · warm 98% / cool 0%
- **Palette (measured):** #911e11 red 38%, #e46d5e red 20%, #1e0706 black 12%, #50110d dark red 9%, #f48ea8 light red 8%, #bc3c42 red 6%

### Transition masks, last frames

`volcanoAnims_10_jpg` · atlas · 3 parts · largest 512×512 · sheet `sheets/volcanoAnims_10_jpg.webp`

- **Role:** The last three mattes of the transition.
- **Subject:** Two pale grey cloud shapes and a plain white square.
- **Style:** A matte, not a picture.
- **Rendering:** Opaque greyscale.
- **Colour:** White #fcfcfc and greys.
- **Lighting:** None.
- **Ambience:** None: a mask.
- **Materials:** None: a mask.
- **Variants:** One.
- **Motion:** transitionBW_20, _21 and transitionPng_22.
- **Construction:** 3 parts of 512x512 on a 1540x514 page.
- **Measured:** bright, muted, neutral, medium contrast, hard-edged, strong highlights · brightness 83% · saturation 0% · contrast 29% · warm 0% / cool 0%
- **Palette (measured):** #fcfcfc white 53%, #b1b1b1 grey 37%, #848484 grey 10%

### Volcano explosion with mattes

`volcanoAnims_11_jpg` · atlas · 28 parts · largest 453×334 · sheet `sheets/volcanoAnims_11_jpg.webp`

- **Role:** The large explosion of a volcano, as colour frames and matching black-and-white mattes.
- **Subject:** A yellow-white fireball that swells into an orange cloud with a dark core; beside it the same shapes in black on white.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Gold #fceb4c and browns on black; white and black on the mattes.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** volcanoExplosion 14 frames and volcanoExplosionBW 14 frames.
- **Construction:** 28 parts up to 453x334 on a 1985x1879 page.
- **Notes:** Colour and matte pairs again.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 69% · saturation 26% · contrast 60% · warm 36% / cool 0%
- **Palette (measured):** #fcfcfc white 44%, #100a06 black 15%, #fceb4c gold 9%, #443324 brown 6%, #cbcbcb grey 4%, #6e685e grey 3%

### Volcano hit bursts

`volcanoAnims_12_jpg` · atlas · 91 parts · largest 151×141 · sheet `sheets/volcanoAnims_12_jpg.webp`

- **Role:** Three kinds of impact burst at a volcano, the first with mattes.
- **Subject:** A yellow star burst with a dark centre (hit 1) and its black-on-white matte; a low, wide fan of flame (hit 2); a small orange spark knot (hit 3).
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Gold #fbf03b and #fbeb8a, orange #eba959, brown #4c301a; white on the mattes.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** Three hit shapes.
- **Motion:** volcanoHit1 22 frames, volcanoHit1_BW 22, volcanoHit2 23, volcanoHit3 24.
- **Construction:** 91 parts of about 151x141 on a 1930x958 page.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged, strong highlights · brightness 59% · saturation 45% · contrast 53% · warm 72% / cool 0%
- **Palette (measured):** #fcfcf8 light yellow 21%, #0f0906 black 17%, #fbf03b gold 10%, #fbeb8a light gold 9%, #4c301a brown 8%, #eba959 orange 7%

### Small lava explosion

`volcanoAnims_2_jpg` · atlas · 13 parts · largest 150×130 · sheet `sheets/volcanoAnims_2_jpg.webp`

- **Role:** A small burst at a volcano's crater.
- **Subject:** A ball of red and yellow fire that opens and breaks up.
- **Style:** Hand-drawn stylised fire.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Gold #faec0f, orange #de650f and #f0a217, red #98260c.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** explosion, 13 frames.
- **Construction:** 13 parts of 150x130.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 32% · saturation 75% · contrast 32% · warm 100% / cool 0%
- **Palette (measured):** #0f0403 black 39%, #faec0f gold 16%, #de650f orange 11%, #5a1409 dark red 10%, #f0a217 orange 9%, #98260c red 8%

### Crater halo

`volcanoAnims_2_png` · atlas · 17 parts · largest 255×140 · sheet `sheets/volcanoAnims_2_png.webp`

- **Role:** The ring of fire that floats over a volcano's crater when its feature is live (seen over all three volcanoes at the trigger and through the bonus).
- **Subject:** A tilted ellipse of white-hot light with a red flame trail.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Soft glow with alpha (measured soft edge 0.83).
- **Colour:** Red #fc522b (64%), light orange #fef4dd, orange #fb9663.
- **Lighting:** Self-lit.
- **Ambience:** Charged, ready.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** glowArounVolcanoPng, 17 frames: the flame runs around the ring.
- **Construction:** 17 parts of about 245x138, with alpha.
- **Notes:** A halo is how the game marks an active feature: one small shape, readable at thumbnail size.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 59% · saturation 66% · contrast 56% · warm 100% / cool 0% · brighter towards: top (3), top-right (2)
- **Palette (measured):** #fc522b red 64%, #fef4dd light orange 17%, #fb9663 orange 12%, #fdc996 light orange 6%

### Crater glow

`volcanoAnims_3_jpg` · atlas · 6 parts · largest 73×43 · sheet `sheets/volcanoAnims_3_jpg.webp`

- **Role:** The glow inside a volcano's crater.
- **Subject:** A small yellow ellipse of light.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Gold #fdf574 (39%), orange #c68923 and #e8ba3d, brown #471c05.
- **Lighting:** Self-lit.
- **Ambience:** A pilot light.
- **Materials:** Light.
- **Variants:** One.
- **Motion:** glowInVolcano, 6 frames.
- **Construction:** 6 parts of 73x43.
- **Measured:** bright, vivid, warm, high contrast, hard-edged, strong highlights · brightness 62% · saturation 70% · contrast 60% · warm 100% / cool 0%
- **Palette (measured):** #fdf574 gold 39%, #471c05 brown 20%, #965310 brown 12%, #c68923 orange 11%, #e8ba3d orange 10%, #fdfcc6 light gold 5%

### Lava fountain

`volcanoAnims_3_png` · atlas · 19 parts · largest 127×230 · sheet `sheets/volcanoAnims_3_png.webp`

- **Role:** The spray of lava from a volcano when a fireball arrives.
- **Subject:** A fountain of yellow-orange droplets that rises and falls back in two arcs.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Soft particles with alpha.
- **Colour:** Orange #fc9a2d (72%), gold #fef36a, near white #fefef0.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Lava droplets.
- **Variants:** One.
- **Motion:** lavaEruption, 19 frames.
- **Construction:** 19 parts of about 120x225, with alpha.
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 73% · saturation 72% · contrast 43% · warm 100% / cool 0%
- **Palette (measured):** #fc9a2d orange 72%, #fef36a gold 15%, #fefef0 light gold 8%, #f86805 orange 2%, #fdfeaf light gold 2%

### Lava column

`volcanoAnims_4_jpg` · atlas · 35 parts · largest 329×521 · sheet `sheets/volcanoAnims_4_jpg.webp`

- **Role:** The tall column of fire of a volcano's full eruption (seen at the bonus trigger).
- **Subject:** A rising orange fireball on a thin stem that spreads into a cloud of sparks.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Orange #fa6c17 (50%) and #fdb83a, dark orange #be3405.
- **Lighting:** Self-lit.
- **Ambience:** The pay-off moment.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** lavaEruption2, 35 frames on this page (up to 329x521).
- **Construction:** 35 parts on a 2038x1770 page.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 46% · saturation 89% · contrast 38% · warm 100% / cool 0%
- **Palette (measured):** #fa6c17 orange 50%, #fdb83a orange 16%, #be3405 orange 11%, #812405 brown 9%, #1e0802 black 8%, #501603 dark red 4%

### Eruption with smoke

`volcanoAnims_4_png` · atlas · 34 parts · largest 148×683 · sheet `sheets/volcanoAnims_4_png.webp`

- **Role:** A second eruption drawn with its own smoke: a yellow fire head on a column of dark brown smoke.
- **Subject:** A bright yellow flame on top of a rising, twisting brown smoke column that thins to a wisp.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Painted frames with alpha; the dark smoke needs alpha because it cannot be added as light.
- **Colour:** Brown #3a1b0b (61%), gold #fef433, orange #ef8821.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire, smoke.
- **Variants:** One.
- **Motion:** volcanoEruption1, 34 frames, up to 148x683.
- **Construction:** 34 parts on a 1475x1539 page, with alpha.
- **Notes:** The one dark effect among the light ones.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 33% · saturation 80% · contrast 70% · warm 100% / cool 0% · brighter towards: top (12), top-right (7), top-left (6)
- **Palette (measured):** #3a1b0b brown 61%, #fef433 gold 11%, #ef8821 orange 9%, #8c4319 brown 7%, #fef579 gold 4%, #b95e25 orange 4%

### Lava column, further frames

`volcanoAnims_5_jpg` · atlas · 14 parts · largest 335×527 · sheet `sheets/volcanoAnims_5_jpg.webp`

- **Role:** More frames of the same eruption column.
- **Subject:** A tall plume of orange fire with bright streaks.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Orange #fc7e15 (55%) and #e74105, dark red #5a1903.
- **Lighting:** Self-lit.
- **Ambience:** The pay-off moment.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** lavaEruption2, 14 frames.
- **Construction:** 14 parts of about 335x525 on an 1861x1391 page.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 46% · saturation 92% · contrast 39% · warm 100% / cool 0%
- **Palette (measured):** #fc7e15 orange 55%, #e74105 orange 15%, #5a1903 dark red 14%, #a73106 brown 7%, #fdd930 gold 5%, #0f0401 black 3%

### Transition fire cloud

`volcanoAnims_6_jpg` · atlas · 16 parts · largest 511×512 · sheet `sheets/volcanoAnims_6_jpg.webp`

- **Role:** The fire cloud of the scene change into the bonus (folder transitionPng): in the real screens the board whites out in orange with rocks flying at the camera.
- **Subject:** A round red-orange cloud with a bright ring that grows to fill its square.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Red #8d321f (56%) and #ce441f on near black.
- **Lighting:** Self-lit.
- **Ambience:** Everything burns for a second.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** transitionPng, 15 frames on this page.
- **Construction:** 16 parts up to 511x512; scaled up to cover the screen (inference).
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 19% · saturation 78% · contrast 16% · warm 100% / cool 0% · brighter towards: bottom-left (2)
- **Palette (measured):** #8d321f red 56%, #170803 black 32%, #4e1804 brown 6%, #ce441f red 6%

### Transition fire cloud and first masks

`volcanoAnims_7_jpg` · atlas · 9 parts · largest 512×512 · sheet `sheets/volcanoAnims_7_jpg.webp`

- **Role:** More of the transition: the fullest fire-cloud frames and the first two black-and-white mask frames.
- **Subject:** A square filled with rolling red cloud; a white square with a small black blot.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Dark red #65211a and black, with pure white on the mask frames.
- **Lighting:** Self-lit.
- **Ambience:** Heat and impact.
- **Materials:** Fire.
- **Variants:** One.
- **Motion:** transitionPng 7 frames (49 to 61); transitionBW_00 and _01.
- **Construction:** 9 parts of 512x512.
- **Notes:** The black-and-white frames are mattes for the colour frames: the picture and its mask ship as two opaque pages instead of one page with alpha (inference from the matching names and shapes).
- **Measured:** mid-tone, saturated, warm, low contrast, hard-edged, strong highlights · brightness 32% · saturation 53% · contrast 18% · warm 78% / cool 0% · brighter towards: bottom-left (1)
- **Palette (measured):** #65211a dark red 40%, #1c0a08 black 36%, #fefefe white 22%

### Transition masks, frames 02 to 10

`volcanoAnims_8_jpg` · atlas · 9 parts · largest 512×512 · sheet `sheets/volcanoAnims_8_jpg.webp`

- **Role:** Black-and-white mattes of the transition cloud.
- **Subject:** A black blot on white that grows from a dot to most of the square.
- **Style:** A matte, not a picture.
- **Rendering:** Opaque greyscale.
- **Colour:** White, greys and black only.
- **Lighting:** None.
- **Ambience:** None: a mask.
- **Materials:** None: a mask.
- **Variants:** One.
- **Motion:** transitionBW, 9 frames.
- **Construction:** 9 parts of 512x512 on a 1540x1540 page. Which of the two 1540x1540 files is this page was decided by eye (the frames that start small).
- **Measured:** bright, muted, neutral, high contrast, hard-edged, strong highlights · brightness 80% · saturation 0% · contrast 74% · warm 0% / cool 0%
- **Palette (measured):** #fbfbfb white 68%, #cbcbcb grey 9%, #3b3b3b grey 8%, #080808 black 8%, #9a9a9a grey 5%, #707070 grey 2%

### Transition masks, frames 11 to 19

`volcanoAnims_9_jpg` · atlas · 9 parts · largest 512×512 · sheet `sheets/volcanoAnims_9_jpg.webp`

- **Role:** The later mattes of the transition cloud.
- **Subject:** A large grey cloud shape with a black edge on white, breaking up.
- **Style:** A matte, not a picture.
- **Rendering:** Opaque greyscale.
- **Colour:** Greys, white and black only.
- **Lighting:** None.
- **Ambience:** None: a mask.
- **Materials:** None: a mask.
- **Variants:** One.
- **Motion:** transitionBW, 9 frames.
- **Construction:** 9 parts of 512x512.
- **Measured:** mid-tone, muted, neutral, high contrast, hard-edged, strong highlights · brightness 51% · saturation 0% · contrast 87% · warm 0% / cool 0% · brighter towards: top-right (5), top (1)
- **Palette (measured):** #545454 grey 46%, #f8f8f8 white 23%, #c9c9c9 grey 9%, #0a0a0a black 8%, #979797 grey 8%, #282828 grey 5%

### Embers (volcanoes)

`volcanoAnims_jpg` · atlas · 10 parts · largest 146×262 · sheet `sheets/volcanoAnims_jpg.webp`

- **Role:** Embers rising around the feature volcanoes.
- **Subject:** A tall scatter of small orange sparks.
- **Style:** Simulated-looking fire and smoke, not drawn outlines.
- **Rendering:** Frames on a black ground without alpha, meant to be added over the scene as light (inference from the black ground and the page name _jpg; the blend mode is in the binary skeleton and was not read).
- **Colour:** Brown and orange (#552812, #844727, #b06238) on black.
- **Lighting:** Self-lit.
- **Ambience:** Background heat.
- **Materials:** Embers.
- **Variants:** One.
- **Motion:** embers, 10 frames.
- **Construction:** 10 parts of 146x262.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 15% · saturation 77% · contrast 14% · warm 100% / cool 0%
- **Palette (measured):** #1a0b04 black 55%, #552812 brown 24%, #844727 brown 14%, #b06238 orange 6%


## Game interface

Buttons, counters and panels drawn for this game.

### Bonus buy plaques, portrait buttons and volcano silhouettes

`default_portrait_webp80_png` · atlas · 13 parts · largest 317×416 · sheet `sheets/default_portrait_webp80_png.webp`

- **Role:** Interface pieces: the two bonus-buy plaque grounds, the BUY and jackpot panel plates, the three mystery volcano silhouettes with question marks shown on the BONUS BUY plaque, the COLLECT label and a copy of the logo.
- **Subject:** Two tall cards with a gold ornamental frame, one filled with yellow fire and one with red fire, each with a dark red price field; teal plates with a gold rim; black volcano silhouettes glowing blue, red and green with a white question mark.
- **Style:** Slot-cabinet interface: gold frames with a small repeating ornament, teal enamel plates.
- **Rendering:** Clean vector-like plates with a soft inner gradient; the fire inside the cards is painted.
- **Colour:** Dark red and black (#240b07, #691508), teal #058276, red #ea110a.
- **Lighting:** Plates are top-lit with a lighter upper edge; the silhouettes are back-lit by their colour.
- **Ambience:** Formal frames around loud fire.
- **Materials:** Gold metal, enamel, fire.
- **Variants:** Button plates in four states (disabled grey, enabled, over, pressed); silhouettes in the three feature colours.
- **Motion:** Still pieces; the plaques pulse and spark in the bonus buy animation (see the bonus buy units).
- **Construction:** 13 sprites on a 750x765 page named for the portrait layout, though the landscape screen uses the same plaques.
- **Notes:** Teal is the game's one cool interface colour: every panel that holds a number is teal with a gold rim.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 34% · saturation 82% · contrast 68% · warm 78% / cool 17% · brighter towards: top (4), bottom-left (2)
- **Palette (measured):** #240b07 black 22%, #691508 dark red 13%, #058276 dark cyan 8%, #ea110a red 4%

### Shared interface page: tutorial ground, bonus reel frame, feature labels, bars and icons

`default_shared_webp80_png-0` · atlas · 18 parts · largest 2040×1410 · sheet `sheets/default_shared_webp80_png-0.webp`

- **Role:** A mixed page: the tutorial background, the frame of a bonus reel set, the big MULTIPLIER and COLLECT labels, the bottom strip and top bar grounds, and small icons (auto spin, sound off, turbo).
- **Subject:** A copy of the red vortex; a thin red-brown frame of 5 by 3 empty cells; the words MULTIPLIER in red and COLLECT in green with a gold rim; dark gradient bars; white line icons.
- **Style:** The labels are small-caps display lettering; the icons are plain white glyphs.
- **Rendering:** Flat and thin: frames are hairlines with a faint ornament, bars are gradients to transparent.
- **Colour:** Dark red #360808 (70%) and #8b1713; the pure red #ff0100 is a mask rectangle (betContentMask), not art.
- **Lighting:** None to speak of.
- **Ambience:** Quiet service pieces.
- **Materials:** None depicted, except the gold rim of the labels.
- **Variants:** The DOUBLE label is on the other shared page.
- **Motion:** Still pieces.
- **Construction:** 18 sprites on a 2044x2042 page; the 2040x1410 tutorial ground takes most of it.
- **Notes:** The reel frames are deliberately slight: a hairline grid, so the cells' teal and the symbols carry the board.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 12% · saturation 83% · contrast 12% · warm 98% / cool 0% · brighter towards: top-left (1), bottom (1)
- **Palette (measured):** #360808 dark red 70%, #8b1713 red 14%, #ff0100 red 14%

### Bonus buy plaque shine overlays

`buyBonusAnims_jpg` · atlas · 4 parts · largest 550×765 · sheet `sheets/buyBonusAnims_jpg.webp`

- **Role:** Light layers for the bonus buy cards: a bright copy of each card for a flash, a star and a soft particle.
- **Subject:** Each card repeated on black with a strong outer glow (TCEplaqueShine, TCEplaqueShine2), a white four-point star and a round white dot.
- **Style:** As the cards.
- **Rendering:** Pictures on black, to be added over the cards as light (inference from the black ground and the _jpg page).
- **Colour:** Orange #e39c1d, dark red #5e0e06, near white #fdfbf3.
- **Lighting:** These are the light.
- **Ambience:** A flash of attention on the offer.
- **Materials:** Light only.
- **Variants:** One shine per card.
- **Motion:** Used by the bonus buy skeleton (binary, not drawn here).
- **Construction:** 4 parts on a 1561x554 page without alpha.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 45% · saturation 76% · contrast 77% · warm 97% / cool 1%
- **Palette (measured):** #e39c1d orange 26%, #130202 black 17%, #5e0e06 dark red 11%, #fdfbf3 light gold 11%, #c8530c orange 10%, #992307 red 10%

### Bonus buy plaques (animated version)

`buyBonusAnims_png` · atlas · 3 parts · largest 494×623 · sheet `sheets/buyBonusAnims_png.webp`

- **Role:** The two cards of the bonus buy panel as used by its skeleton: BONUS BUY (any 1, 2 or all 3 features) and SUPER BONUS BUY (all 3 features), and the enabled BUY button. Seen in two real screens.
- **Subject:** A gold-framed card with yellow fire and three black volcano silhouettes with question marks; a red-glowing card with the three coloured volcanoes erupting and their labels; a teal pill button with a gold rim.
- **Style:** Collectible-card layout in a slot-cabinet frame.
- **Rendering:** Painted fire inside a crisp ornamental frame; the super card has a red outer glow baked in.
- **Colour:** Orange #c77b1e, dark red #5b1307, red #f81c04, with teal #02766a on the button.
- **Lighting:** The fire lights each card from inside; the super card glows red at its edge.
- **Ambience:** Two offers side by side, the dearer one visibly hotter.
- **Materials:** Gold frame, fire, enamel button.
- **Variants:** Two cards: mystery (yellow, question marks) and super (red, all three volcanoes shown).
- **Motion:** In the real screens the cards arrive without text and the titles, prices (100.00 and 260.00 at a 2.00 bet) and BUY buttons come in after; the layout names the animation buyBonusStatic.
- **Construction:** 3 sprites on one page; the shine overlays are in buyBonusAnims_jpg.
- **Notes:** The buy panel reuses the game's own pieces (volcanoes, labels), so no new art language is needed for it.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 31% · saturation 84% · contrast 70% · warm 88% / cool 11% · brighter towards: bottom (1), top (1)
- **Palette (measured):** #1b0704 black 22%, #c77b1e orange 20%, #5b1307 dark red 15%, #f81c04 red 9%, #95210b red 7%, #02766a dark cyan 3%

### Fireball collector plate

`fgCounterCollectAnims_png` · atlas · 2 parts · largest 448×156 · sheet `sheets/fgCounterCollectAnims_png.webp`

- **Role:** A dark plate with a lava-crack border and a red outline frame, from the skeleton named FgCounterCollectAnims. Where it sits in play was not identified in the screens of this run.
- **Subject:** A black rounded rectangle edged with cracked molten rock; a thin red rounded frame with a glow.
- **Style:** The same molten-rock motif as the big win lettering.
- **Rendering:** Painted crack texture on the border, flat black inside.
- **Colour:** Black #060101 (60%), brown #59321e, red #fe0100, gold #c9aa38.
- **Lighting:** The cracks glow from inside.
- **Ambience:** A holder for a number.
- **Materials:** Cooled lava crust.
- **Variants:** Plate and outline.
- **Motion:** The layout names the animation fgCounterCollect; its fire frame and ember frames are separate units.
- **Construction:** 2 sprites.
- **Notes:** Not placed in a real screen: inference only that it holds a collected total.
- **Measured:** dark, saturated, warm, medium contrast · brightness 12% · saturation 50% · contrast 41% · warm 100% / cool 0%
- **Palette (measured):** #060101 black 60%, #59321e brown 19%, #fe0100 red 12%, #c9aa38 gold 4%, #9d3d1a brown 4%

### Respin counter

`freeSpinsIndicatorAnims_png` · atlas · 4 parts · largest 136×59 · sheet `sheets/freeSpinsIndicatorAnims_png.webp`

- **Role:** The small three-socket bar under each bonus reel set that shows the respins left, with its lit ember (seen in the bonus screens under both grids).
- **Subject:** A grey stone bar with three round sockets and red glowing cracks; a small orange ember ball that fills a socket.
- **Style:** Chunky carved stone, cartoon scale.
- **Rendering:** Soft painted stone with a light top edge; the ember is a tiny glossy ball.
- **Colour:** Grey #50414b, black #100a0c, orange #f46e0f, gold #fcc515.
- **Lighting:** Top-lit stone, self-lit ember.
- **Ambience:** A small, clear countdown.
- **Materials:** Stone, ember.
- **Variants:** Three ember sprites (the same ball, named respin_1 and two copies), one per socket.
- **Motion:** In the bonus screens the sockets empty one by one and refill when a new fireball lands; the burst and glow frames are separate units.
- **Construction:** 4 sprites, the bar 136x59.
- **Notes:** The only grey stone in the game.
- **Measured:** mid-tone, saturated, warm, high contrast · brightness 32% · saturation 45% · contrast 84% · warm 87% / cool 6% · brighter towards: top (1)
- **Palette (measured):** #50414b grey 38%, #100a0c black 23%, #f46e0f orange 16%, #3b1c22 dark red 7%, #f6f1f2 light red 4%, #fcc515 gold 4%

### Spin button with glow arc

`glowRespinCircle_jpg` · atlas · 32 parts · largest 190×190 · sheet `sheets/glowRespinCircle_jpg.webp`

- **Role:** The round spin button and the light that runs around it.
- **Subject:** A dark grey disc with a white circular arrow; a short golden arc of light on black, turning.
- **Style:** Neutral, flat control.
- **Rendering:** A flat disc with a thin lighter rim; the arc is a soft streak.
- **Colour:** Black #130b02 and browns of the glow (#533309, #956512), light gold #faefa2.
- **Lighting:** The arc is the light.
- **Ambience:** A quiet prompt to press.
- **Materials:** Light on a flat button.
- **Variants:** One.
- **Motion:** 31 frames of the arc circling the button (animation glowRespinCircleIdle in the layout); in the bonus start panel a golden arc circles the play button in the same way.
- **Construction:** The button plus a 31-frame sequence of 175x175 frames on black.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 31% · saturation 77% · contrast 54% · warm 87% / cool 0%
- **Palette (measured):** #130b02 black 42%, #533309 brown 20%, #faefa2 light gold 12%, #956512 brown 12%, #c09831 orange 8%, #e3c65b gold 6%


## Typography

Embedded fonts and lettering.

### Gold numeral font

`TriplecashEruption_bitmap_font` · atlas · 1 parts · largest 512×514 · sheet `sheets/TriplecashEruption_bitmap_font.webp`

- **Role:** A bitmap font of the digits 0 to 9 with comma, apostrophe and period: the big win amounts counted up over the reels in the real screens (3.00, 4.00).
- **Subject:** Heavy old-style serif numerals in polished gold with a dark red outline.
- **Style:** Classic serif figures, close to the logo's lettering.
- **Rendering:** A marbled gold fill with lighter swirls, a thin bright inner rim and a soft dark red outer stroke.
- **Colour:** Gold #fad142 (41%), orange #d69b17, red #cd0200 and dark red #630902.
- **Lighting:** Even, with a lighter band across the middle of each figure.
- **Ambience:** Rich and celebratory.
- **Materials:** Polished, veined gold.
- **Variants:** One size (72 px line height in the font file, glyphs drawn about 160 px tall on the page).
- **Motion:** Not animated itself; the game counts the number up.
- **Construction:** One 512x514 page with a BMFont .xml that maps 14 characters.
- **Notes:** The gold has a painted texture, unlike the flat value font used on the fireballs.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 52% · saturation 81% · contrast 93% · warm 100% / cool 0%
- **Palette (measured):** #fad142 gold 41%, #190301 black 14%, #d69b17 orange 12%, #cd0200 red 9%, #630902 dark red 9%, #ab6f14 brown 6%

### Fireball value font

`cashEruptionText_label` · atlas · 1 parts · largest 771×724 · sheet `sheets/cashEruptionText_label.webp`

- **Role:** A bitmap font for the cash values on fireballs and in the bonus cells (8.00, 12.00, 66.00 in the bonus screens), with currency signs.
- **Subject:** Very condensed, heavy sans-serif figures and letters in black with a yellow-to-orange outline.
- **Style:** Poster grotesque, compressed.
- **Rendering:** Flat black fill and a two-tone outline (yellow inside, orange outside) with a faint glow.
- **Colour:** Black #030200 (55%), orange #f79600, gold #ffe100.
- **Lighting:** None: flat, made to sit on a glowing ball.
- **Ambience:** Blunt and readable.
- **Materials:** None depicted.
- **Variants:** 34 characters: digits, $ £ € ¥, a few letters for currency codes and K.
- **Motion:** Not animated.
- **Construction:** One 771x724 page with a BMFont .xml.
- **Notes:** Dark figures on a bright ball, the reverse of the gold win numerals: the two number styles never compete.
- **Measured:** dark, vivid, warm, high contrast · brightness 28% · saturation 78% · contrast 88% · warm 100% / cool 0%
- **Palette (measured):** #030200 black 55%, #f79600 orange 18%, #ffe100 gold 15%, #7e4400 brown 7%, #bf6800 brown 3%, #452600 brown 2%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `LevelStage1.desktop`: 30 parts
- `LevelStage2.desktop`: 29 parts
- `WinCelebration.desktop`: 30 parts
- `Widgets_Transitions`: 1 parts
- `Widgets_Transitions_2`: 1 parts
- `Widgets_Transitions_3`: 1 parts
- `Widgets_Transitions_4`: 1 parts
- `arrowWhite`: 1 parts
- `305c3cb3f14af7d76a1d`: 1 parts
- `default_land_landscape_webp80_png`: 2 parts
- `default_prt_portrait_webp80_png`: 2 parts
- `default_shared_webp80_jpg`: 5 parts
- `networkActivity`: 40 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Gilroy (Black); Lato (Bold); Noto Sans (Condensed Bold); OswaldLocCur (Bold); QTFrizQuad (Bold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1913 components cut from 76 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
