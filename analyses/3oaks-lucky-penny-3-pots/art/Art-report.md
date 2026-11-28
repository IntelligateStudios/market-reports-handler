# Lucky Penny 3 Pots: Super Wheel: art report

3oaks · run `2026-11-28-1022-3oaks-lucky-penny-3-pots-super-wheel` · captured 2026-11-28

Source: the provider's free-play demo, https://betman-demo.head.3oaks.com/betman-demo/game/?game=lucky_penny_3_pots_super_wheel&ts=123&token=…&wl=demo

**Extracted:** 1151 named components from 76 textures in 76 atlases; 27 Spine skeletons; 37 frame sequences (659 frames); 3 fonts. Grouped into 56 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

An Irish-luck slot drawn as one big gold-and-rainbow toy: three glossy cauldrons heaped with clover coins sit on the reel board in front of a fairground Super Wheel, all in a clean casual 3D-look cartoon manner, against a dusk forest painted cool at the edges and blazing orange at the centre.

**Style.** Casual 3D-look cartoon, the manner of a casual mobile game more than of a classic Vegas slot: short, wide, toy-like objects (pots, mug, sack, harp, horseshoe, watch, pipe), a friendly leprechaun portrait with a large head and no caricature edge, coins drawn as jewellery. Lettering is casino-poster slab-serif capitals with big first letters (logo, pots, wheel words, win banners). The backdrop is a storybook painting of big scalloped leaf masses with no small detail.

**Rendering.** Smooth enamel gradients with a bright specular patch and a light rim, no line outline anywhere on the game art. The reel board is kept flat and quiet (cream reels, a thin wooden frame, a knot pattern at very low contrast) so the symbols carry the colour. Every glow, ray, rainbow, sparkle and win frame is a separate additive layer on a black ground, so the light is a layer, not paint.

**Colour.** Gold first: measured over the game's own art, orange #edaa0a 17%, gold #fcee0f 5%, orange #c1710d 6% and brown #7e3b0a 7% (black #0a0a0c 27% is mostly the ground of additive parts); hues orange 38%, yellow 24%, green 12%, blue 11%; vivid (saturation 0.68), warm 61% against cool 20%. Read: one saturated feature colour per piece on top of the gold, blue for Double, red for Multi, green for Extra and Mini, purple for Major, repeated on the pots, the coloured bonus coins, the wheel slices and the jackpot panels. The rainbow is the game's accent for wins and transitions. The background is the cool counterweight (dark blue #13192a 48% and purple #7148ba 11% around an orange core).

**Lighting.** Top light throughout (measured light direction over the game's art: top 83, top-right 75, top-left 72), with highlights high on bellies and rims and soft drop shadows as separate parts. The scene has one hot centre: a blaze of yellow-orange light behind the pots and the wheel (bg_animation), so in play the whole screen reads far warmer than the backdrop file. Feature moments add coloured light columns from the pots, rainbow rings and neon win frames.

**Ambience.** Cheerful abundance and luck: heaps of coins that never sit still, pots that visibly fill, a grinning leprechaun, a fairground wheel. Bright and friendly rather than mysterious; the dusk forest is only a frame for the gold.

**Shape language.** Round and chunky: fat cauldrons, round coins, clover pads, rounded tiles, ball-terminal numerals. The only straight-edged pieces are the long wheel wedges and the flat reel board.

**Materials.** Polished gold (coins, badges, rims, trims), glossy enamelled metal (pot bodies, coin rims), glazed ceramic and beer foam, cloth (sack, hat), carved wood (pipe, low letters, reel frame), enamel symbol tiles, and neon light for win frames.

**Typography and lettering.** Display words are drawn art in one family of heavy slab-serif capitals with a contrasting stroke and a bevel: the logo, the pot plates, the wheel words, the big-win banners (BIG, HUGE, MEGA, EPIC WIN, BONUS WIN, GRAND WIN) and the BONUS GAME title. Numbers are five bitmap fonts of the same ball-terminal numeral (big win, jackpots, coin values, multipliers in red, line wins). The interface uses Roboto Black and Gilroy, the platform's faces.

**Motion.** All 27 rigs are Spine 4.1.24 binary skeletons (.skel), drawn here with Spine's own runtime. The pots carry the most motion (76 animations: eleven fill levels with idle variants, a collect for each level, trigger start and loop); symbols have one 1 s win animation each, the Wild bends its hat and head on meshes; the big-win rig runs 6 to 11 s per tier. Sparkle, coin turns, sweeps and win-frame pulses are frame sequences (37 found) inside the rigs; small sparks are thrown by the client's particle emitters.

**Variants and themes.** Variety comes from recolouring one design: one pot rig with three skins (blue Double, green Extra, red Multi), a gold bonus coin with blue, green and red feature versions and green Mini, blue Minor and purple Major jackpot coins, seven wheel slices from one rig, four jackpot panels from one plate. Every symbol ships as a still, a reel-blur copy and a skeleton frame.

**How it is built.** 1,151 named sprites on 76 textures, 27 skeletons, 5 bitmap font pages and 3 embedded typefaces. Pieces are built in layers: a top symbol is tile, object, tile frame top, shadow and glint, so the object can pop out of its frame; a pot is body, plate, badge, front and back coin heaps and separate light. Eleven paying symbols share one skeleton and one atlas. The Super Wheel is the largest art (rim 1616x1616 px), and the start screen has its own scene of five large pictures.

**Consistency.** Tight: one rendering manner, one gold, one lettering family and one colour code for the features across pots, coins, wheel and panels. Two things sit apart: the backdrop is a looser painting than the clean 3D-look pieces, and the interface (spin button, menu, balance) is the platform's flat white-on-dark set, shared with Kendoo's game on the same demo server (inference from the shared gr_ rules and Gilroy files).

**What to take from it.** (1) A colour code carries the game design: each feature owns one colour, and that colour is repeated on every piece that belongs to it (pot, coin, wheel slice, panel), always on the same gold. A player reads the feature before reading the word. (2) The feature collectors are the stars of the screen: three pots stand where a mascot would, and their fill levels are drawn as eleven separate states, so progress is shown by the art itself. (3) Light is a separate layer everywhere (additive rays, glows, rainbows and neon frames on black grounds). That is what keeps the painted pieces reusable and what an image model does not give by itself. (4) The board is kept plain so the symbols and the pots carry the detail; the backdrop is cool and dark at the edges so the gold centre reads first. (5) One rig per family with skins (pots, coins, wheel slices, eleven symbols in one skeleton) keeps a lot of visible variety on little art.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 38% · saturation 68% · contrast 49% · warm 61% / cool 20% · brighter towards: top (83), top-right (75), top-left (72)

Palette: #0a0a0c black 27%, #edaa0a orange 17%, #312d2a grey 9%, #7e3b0a brown 6%, #c1710d orange 6%, #fcee0f gold 5%, #f9f5e9 light gold 2%, #e80e05 red 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 9 | 38% | 70% | 47% | 55% / 23% | #080b0e black 31%, #eea904 orange 23%, #2c302c grey 10% |
| Reel board | 14 | 39% | 71% | 46% | 55% / 26% | #0c0a0b black 18%, #773009 brown 11%, #e6a715 orange 10% |
| Symbols | 5 | 31% | 51% | 39% | 54% / 16% | #0d0c0b black 33%, #312f2b grey 14%, #f8d71b gold 6% |
| Characters | 1 | 51% | 72% | 54% | 86% / 7% | #fad819 gold 19%, #e08e14 orange 18%, #070603 black 16% |
| Logo and title | 1 | 30% | 50% | 66% | 80% / 8% | #050303 black 47%, #fcf9ec light gold 7%, #fda3fd light magenta 6% |
| Win celebrations and banners | 6 | 42% | 76% | 64% | 86% / 10% | #100803 black 20%, #eda71f orange 10%, #fbe412 gold 9% |
| Effects | 12 | 43% | 67% | 46% | 64% / 19% | #080606 black 24%, #fbe41d gold 11%, #313228 grey 6% |
| Game interface | 2 | 40% | 76% | 71% | 72% / 17% | #0e050f black 14%, #f0c01f gold 14%, #3d0a3c dark magenta 12% |
| Typography | 5 | 56% | 76% | 88% | 100% / 0% | #fddb0d gold 19%, #a50e05 red 16%, #230201 black 10% |
| Provider interface (shared) | 1 | 79% | 29% | 15% | 33% / 0% | #ffffff light orange 62%, #ed6604 orange 20%, #0b0907 black 8% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Start-screen coin arch

`back_coins_portrait_start_screen` · atlas · 1 parts · largest 1055×481 · sheet `sheets/back_coins_portrait_start_screen.webp`

- **Role:** The heap of coins behind the three pots on the start screen.
- **Subject:** An arch-shaped mound of clover coins with a yellow halo.
- **Style:** As the pots' coins.
- **Rendering:** Painted coins in warm gradients; a soft halo.
- **Colour:** Measured: light gold #fdde55 53%, orange #e36e0c 18%, yellow #fde40e 16%.
- **Lighting:** Top light; glowing edge.
- **Materials:** Gold.
- **Motion:** Still.
- **Construction:** One 1055x481 px picture.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 76% · saturation 78% · contrast 52% · warm 100% / cool 0%
- **Palette (measured):** #fdde55 gold 53%, #e36e0c orange 18%, #fde40e gold 16%, #fba538 orange 9%, #f3a711 orange 2%, #a63505 brown 2%

### Start-screen back light

`back_light_portrait_start_screen_add` · atlas · 1 parts · largest 1487×759 · sheet `sheets/back_light_portrait_start_screen_add.webp`

- **Role:** A soft orange light laid additively behind the start-screen pots.
- **Subject:** A blurred orange oval.
- **Style:** Pure light.
- **Rendering:** One soft gradient.
- **Colour:** Measured: orange #feaf04 100%.
- **Motion:** Still.
- **Construction:** One 1487x759 px picture.
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect · brightness 70% · saturation 98% · contrast 6% · warm 100% / cool 0%
- **Palette (measured):** #feaf04 orange 100%

### The forest at dusk (base and bonus backdrop)

`background` · atlas · 1 parts · largest 2000×2544 · sheet `sheets/background.webp`

- **Role:** The one painted scene behind everything; it is drawn tall enough to serve both the landscape and the portrait layout.
- **Subject:** A forest clearing: tall trees with rounded clumps of leaves on both sides, a grass path running into a blaze of golden light at the centre, a violet evening sky, firs on the horizon, clover leaves in the dark foreground.
- **Style:** Stylised storybook painting: big simple leaf masses with scalloped edges, no small detail, strong colour temperature contrast.
- **Rendering:** Broad soft gradients with crisp cut-out edges on the foliage; rim light in orange on everything that faces the glow.
- **Colour:** Measured: dark blue #13192a 48%, brown #5b3d20 13%, orange #ef9803 11%, purple #7148ba 11%, #d25d06 8%; brightness 0.25. Read: a cool violet-blue night frame around a hot orange-yellow core.
- **Lighting:** A single source inside the picture: the glow at the end of the path, where the treasure is (inference). Everything else is silhouette and rim.
- **Ambience:** Magical evening; the gold is somewhere in the woods and already lighting them.
- **Materials:** Foliage, grass, haze.
- **Variants:** One picture for both layouts; the base game lays strong yellow light over it (bg_animation), so in play it reads far warmer than the file.
- **Motion:** Still; the light over it is the bg_animation rig.
- **Construction:** One 2000x2544 px picture, the largest in the game.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 25% · saturation 69% · contrast 60% · warm 46% / cool 52% · brighter towards: top-left (1)
- **Palette (measured):** #13192a dark blue 48%, #5b3d20 brown 13%, #ef9803 orange 11%, #7148ba purple 11%, #d25d06 orange 8%, #353461 dark blue 4%

### Start-screen scene

`background_portrait_start_screen` · atlas · 1 parts · largest 2000×2544 · sheet `sheets/background_portrait_start_screen.webp`

- **Role:** The backdrop of the start screen (the opening card with the three pots and the wheel).
- **Subject:** The same forest clearing, bleached to yellow and green by the light, fading to black at the edges and the bottom.
- **Style:** As the main backdrop.
- **Rendering:** The backdrop repainted in two hues with a heavy vignette.
- **Colour:** Measured: yellow #fbd905 33%, #e69f03 27%, #b28802 11%, olive #786b03 7%; saturation 0.96.
- **Lighting:** Lit from the centre outwards.
- **Ambience:** Brighter and simpler than the game scene: a poster.
- **Motion:** Still.
- **Construction:** One 2000x2544 px picture; named for portrait and used in landscape too (the opening card of this run is landscape).
- **Measured:** bright, vivid, warm, medium contrast, hard-edged · brightness 63% · saturation 96% · contrast 53% · warm 82% / cool 9%
- **Palette (measured):** #fbd905 gold 33%, #e69f03 orange 27%, #b28802 brown 11%, #786b03 brown 7%, #0e1f02 black 5%, #7ada4e green 5%

### Glow behind the reel board

`bg_animation` · skeleton · 7 parts · largest 361×399 · sheet `sheets/bg_animation.webp`

- **Role:** The breathing golden light behind the board and the pots, and its stronger states.
- **Subject:** A board-shaped block of yellow light with rays fanning out of it.
- **Style:** Pure light.
- **Rendering:** Soft additive shapes; one grey ray fan tinted and turned.
- **Colour:** Measured: black #14100f 34% (ground of additive parts), yellow #fee101 34%, orange #fe6d01 5%.
- **Lighting:** It is the scene's key light in play.
- **Ambience:** The board itself seems to be made of gold.
- **Variants:** Seven animations by name: one, one_main, one_grand, double, double_grand, rise, rise_grand (one board or two, with or without the Grand state).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): slow pulses of the rays; 6 bones, 18 slots.
- **Construction:** 7 parts, the ray fan 361x399 px.
- **Skeleton (from the file):** Spine 4.1.24 · 6 bones · 18 slots · 18 region · animations: double (1.97 s), double_grand (1.97 s), one (2 s), one_grand (2 s), one_main (2 s), rise (1.5 s), rise_grand (1.5 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 44% · saturation 59% · contrast 48% · warm 65% / cool 0%
- **Palette (measured):** #14100f black 34%, #fee101 gold 34%, #46413b grey 11%, #fe6d01 orange 5%, #a97a28 orange 4%, #efac48 orange 4%

### Start-screen foreground

`front_of_wheel_portrait` · atlas · 1 parts · largest 1551×998 · sheet `sheets/front_of_wheel_portrait.webp`

- **Role:** A foreground layer of bushes and grass in front of the wheel on the start screen.
- **Subject:** Yellow-green bushes left and right and a dark green grass mound, with a notch cut out of the top edge.
- **Style:** As the backdrop.
- **Rendering:** Soft cut-out shapes fading to transparent at the edges.
- **Colour:** Measured: dark green #0b1e02 32%, #345d02 23%, yellow-green #c3b701 21%, #599202 18%.
- **Lighting:** Lit from behind and above.
- **Motion:** Still.
- **Construction:** One 1551x998 px picture.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 36% · saturation 96% · contrast 68% · warm 31% / cool 34% · brighter towards: top (1)
- **Palette (measured):** #0b1e02 black 32%, #345d02 dark green 23%, #c3b701 gold 21%, #599202 dark green 18%, #83a702 green 4%, #72d304 green 2%

### Start-screen coin floor

`grass_portrait_start_screen` · atlas · 1 parts · largest 1071×395 · sheet `sheets/grass_portrait_start_screen.webp`

- **Role:** The spread of coins in front of the pots on the start screen.
- **Subject:** A carpet of clover coins with loose ones at the front.
- **Style:** As the pots' coins.
- **Rendering:** Painted coins, darker and redder toward the front edge.
- **Colour:** Measured: orange-gold #e8a233 53%, #cc6413 26%, brown #9e360a 11%.
- **Lighting:** Top light.
- **Materials:** Gold.
- **Motion:** Still.
- **Construction:** One 1071x395 px picture. The file is named grass; it shows coins.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 54% · saturation 83% · contrast 64% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #e8a233 orange 53%, #cc6413 orange 26%, #9e360a brown 11%, #3d1105 dark red 4%, #f7df63 gold 2%, #6c1e07 dark red 2%

### Start-screen shade

`landscape_start_screen_shade` · atlas · 1 parts · largest 2000×1131 · sheet `sheets/landscape_start_screen_shade.webp`

- **Role:** A black gradient that darkens the lower part of the landscape start screen so the TAP ANYWHERE TO START line reads.
- **Subject:** Black, fading to clear at the top.
- **Rendering:** One gradient.
- **Colour:** Measured: black #000000 100%.
- **Motion:** Still.
- **Construction:** One 2000x1131 px picture.
- **Measured:** dark, muted, neutral, low contrast, hard-edged · brightness 0% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #000000 black 100%

### Start-screen burst

`start_anim` · skeleton · 19 parts · largest 596×598 · sheet `sheets/start_anim.webp`

- **Role:** The light that opens the start screen.
- **Subject:** A rainbow swirl with a white-gold star burst, rays and floating sparks.
- **Style:** Pure light.
- **Rendering:** Additive layers: a blurred rainbow spiral, ray fans, lens flare, particles.
- **Colour:** Measured: black #090805 54% (ground), brown-orange #9c5b09 10%. Read: full rainbow around a white-yellow core.
- **Lighting:** Emissive.
- **Ambience:** A pot-of-gold-at-the-end-of-the-rainbow moment.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation, start, on 333 bones and 275 slots, the heaviest rig in the game; a six-frame ray sequence.
- **Construction:** 19 parts reused many times over (275 slots).
- **Skeleton (from the file):** Spine 4.1.24 · 333 bones · 275 slots · 275 region · animations: start (2 s)
- **Measured:** dark, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 23% · saturation 44% · contrast 36% · warm 52% / cool 12% · brighter towards: top (3), top-right (2), bottom-right (2)
- **Palette (measured):** #090805 black 54%, #383127 brown 11%, #9c5b09 brown 10%, #949186 grey 3%, #685d50 brown 3%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Bonus board cell

`bonus-0` · atlas · 1 parts · largest 168×160 · sheet `sheets/bonus-0.webp`

- **Role:** One empty cell of the bonus board.
- **Subject:** A dark magenta square with a four-leaf clover pressed into it and a thin lighter border.
- **Style:** Flat, quiet, tone on tone.
- **Rendering:** Two tones only.
- **Colour:** Measured: dark magenta #330639 78%, #781343 22%.
- **Lighting:** A slightly lighter lower edge.
- **Motion:** Still.
- **Construction:** One 168x160 px picture (frame_back_bonus_game) in its own sheet (bonus-0).
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 10% · saturation 89% · contrast 16% · warm 35% / cool 36% · brighter towards: bottom (1)
- **Palette (measured):** #330639 dark magenta 78%, #781343 dark magenta 22%

### Bonus cell highlight

`cell` · skeleton · 1 parts · largest 118×112 · sheet `sheets/cell.webp`

- **Role:** The lit state of a bonus board cell.
- **Subject:** A magenta square frame with a soft violet fill, brighter at the top.
- **Style:** Flat with a soft inner glow.
- **Rendering:** Gradient fill inside a bright border.
- **Colour:** Measured: #771c7a 40%, #2f0a32 28%, #c84ecb 19%, #aa1eae 13%.
- **Lighting:** Glows from its border inwards.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one short animation of 2 bones and 1 slot (a fade).
- **Construction:** One 118x112 px part in a rig of its own.
- **Skeleton (from the file):** Spine 4.1.24 · 2 bones · 1 slots · 1 region · animations: animation (0.5 s)
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 23% · saturation 76% · contrast 16% · warm 50% / cool 0%
- **Palette (measured):** #771c7a dark magenta 40%, #2f0a32 black 28%, #c84ecb magenta 19%, #aa1eae magenta 13%

### Double feature: second board light

`double_board` · skeleton · 48 parts · largest 288×108 · sheet `sheets/double_board.webp`

- **Role:** The light show that plays when the Double pot opens a second board above the first (the paytable picture shows two boards stacked).
- **Subject:** A wall of rainbow light rising from a white-hot line, with coloured sparks.
- **Style:** Pure light effect.
- **Rendering:** Soft additive gradients; a 43-frame wave sequence gives the rising shimmer.
- **Colour:** Measured over the parts: black #090b09 72% (ground of additive parts), then dark yellow and blue. Read: the full rainbow from violet at the left to red at the right.
- **Lighting:** It is the light.
- **Ambience:** A curtain of luck opening.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation; frame sequence wave x43. 4 mesh parts (the lines bend).
- **Construction:** 48 parts, 43 of them wave frames of 237x102 px.
- **Skeleton (from the file):** Spine 4.1.24 · 12 bones · 10 slots · 6 region, 4 mesh · animations: animation (1.93 s)
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 10% · saturation 74% · contrast 29% · warm 41% / cool 50% · brighter towards: bottom-right (41), right (2)
- **Palette (measured):** #090b09 black 72%, #3f4009 brown 12%, #102951 dark blue 8%, #746e0b brown 2%

### Reel board, frame and jackpot panel plates

`frame-0` · atlas · 8 parts · largest 862×502 · sheet `sheets/frame-0.webp`

- **Role:** The 5x3 board of the base game, the dark board of the bonus game and the plates behind the four jackpot amounts.
- **Subject:** A cream panel of five columns with a faint Celtic knot pattern, a thin brown-and-gold frame with corner pieces, thin dividers; a dark magenta board of cells each embossed with a clover for the bonus; and stacks of four small plates (Grand red, Major purple, Minor blue, Mini green) laid out for landscape, portrait and the bonus.
- **Style:** Deliberately plain so the symbols carry the colour; the only ornament is the knot pattern at very low contrast.
- **Rendering:** Flat fills with soft gradients; the frame is a thin bevelled line.
- **Colour:** Measured: dark magenta #350739 28%, light cream #eadccb 28%, dark red #791940 12%, sand #d5bd9d 7%, red #d80c08 2%. Read: cream for the base game, magenta-black for the bonus.
- **Lighting:** None of its own; the scene's glow shows around it.
- **Ambience:** A calm, light ground in the base game; a night-club dark in the bonus.
- **Materials:** Painted wood or parchment (inference) for the cream panel; lacquer for the bonus cells.
- **Variants:** reels_background and reels_background_bonus; grand_panel_landscape, grand_panel_portrait and grand_panel_bonus (three layouts of the same four plates).
- **Motion:** Still pictures.
- **Construction:** 8 pictures in one sheet (frame-0); the board is 842x482 px, the frame 862x502 px.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 43% · saturation 60% · contrast 30% · warm 66% / cool 20% · brighter towards: top (2), bottom-right (2), bottom (1)
- **Palette (measured):** #350739 dark magenta 28%, #eadccb light orange 28%, #791940 dark red 12%, #d5bd9d orange 7%, #d80c08 red 2%

### Progress bar fill

`progress` · atlas · 1 parts · largest 298×32 · sheet `sheets/progress.webp`

- **Role:** The fill of a progress bar (where it is used was not seen in the played session).
- **Subject:** A rounded blue bar.
- **Style:** Flat UI.
- **Rendering:** A horizontal gradient.
- **Colour:** Measured: #0160d2 70%, #069ff9 20%, #002dab 5%.
- **Motion:** Still; the client scales it.
- **Construction:** One 298x32 px picture.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 37% · saturation 99% · contrast 42% · warm 0% / cool 100% · brighter towards: top-right (1)
- **Palette (measured):** #0160d2 blue 70%, #069ff9 blue 20%, #002dab blue 5%, #14c6f6 cyan 4%

### Progress bar back

`progress_bar_back` · atlas · 1 parts · largest 298×32 · sheet `sheets/progress_bar_back.webp`

- **Role:** The track behind the progress fill.
- **Subject:** A rounded blue bar with a light blue outline.
- **Style:** Flat UI.
- **Rendering:** Flat fill and outline.
- **Colour:** Measured: #0631e8 64%, #3dc9fe 24%, #336fed 6%.
- **Motion:** Still.
- **Construction:** One 298x32 px picture.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 34% · saturation 91% · contrast 53% · warm 0% / cool 100%
- **Palette (measured):** #0631e8 blue 64%, #3dc9fe cyan 24%, #336fed blue 6%, #0324b7 blue 6%

### Respin counter

`respins_frame_level` · skeleton · 29 parts · largest 594×218 · sheet `sheets/respins_frame_level.webp`

- **Role:** The row of numbered lamps under the bonus board that counts the respins left; it has three lamps and gains a fourth, green one from the Extra feature (the paytable pictures show both).
- **Subject:** A gold-framed bar of red lamps numbered 1, 2, 3 and a green lamp numbered 4.
- **Style:** Arcade lamp strip: chunky, glossy, numerals in the game's rounded heavy face.
- **Rendering:** Glossy fills with a white top highlight; iridescent pastel fills for the lamp that is lighting up; neon-like yellow outline.
- **Colour:** Measured: brown-orange #a44f24 18%, black #120a03 16%, dark red #551926 15%, gold #e1c734 10%. Read: red lamps, one green, gold frame.
- **Lighting:** Each lamp lights from inside; a yellow outline glow, a fire-like flash and star glints when the count changes.
- **Ambience:** A countdown you can read at a glance.
- **Materials:** Enamel lamps in a gold bezel.
- **Variants:** Animation names give the states: idle_0 to idle_4, transitions such as 3_2 or 0_3, add_respin, complete, each also in an _add form for the four-lamp bar.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): 26 animations on 47 bones and 65 slots.
- **Construction:** 29 parts; the bar is about 300 px wide. A part named placeholder_txt marks a text the client writes.
- **Skeleton (from the file):** Spine 4.1.24 · 47 bones · 65 slots · 64 region, 1 mesh · animations: 0_3 (0.5 s), 0_4_add (0.67 s), 1_0 (0.27 s), 1_0_add (0.27 s), 1_3 (0.47 s), 1_4_add (0.53 s), 2_1 (0.27 s), 2_1_add (0.23 s), 2_3 (0.43 s), 2_4_add (0.47 s), 3_2 (0.27 s), 3_2_add (0.27 s), 3_4_add (0.47 s), 4_3_add (0.3 s), add_respin (1.5 s), complete (1.5 s), complete_add (1.5 s), idle_0 (1.5 s), idle_0_add (1.5 s), idle_1 (1.5 s), idle_1_add (1.5 s), idle_2 (1.5 s), idle_2_add (1.5 s), idle_3 (1.5 s), idle_3_add (1.5 s), idle_4_add (1.5 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 43% · saturation 69% · contrast 46% · warm 86% / cool 7% · brighter towards: top (1)
- **Palette (measured):** #a44f24 orange 18%, #120a03 black 16%, #551926 dark red 15%, #e1c734 gold 10%, #d37c61 red 8%, #fceed3 light orange 6%

### Super Wheel: title, hub and pointer

`wheel-0` · atlas · 5 parts · largest 1042×298 · sheet `sheets/wheel-0.webp`

- **Role:** The fixed pieces of the wheel that stands behind the pots: its arched title, the hub coin, the pointer and its base.
- **Subject:** SUPER WHEEL in cream capitals on an arched brown-gold ribbon; a large gold clover coin for the hub; a red teardrop pointer with a gold rim; a small brown mount.
- **Style:** Fairground wheel in the game's chunky cartoon manner.
- **Rendering:** Gold gradients with bevels; the title has a dark stroke and extrusion.
- **Colour:** Measured: gold-orange #de9e0e 33%, brown #7b2a06 23%, dark brown #400d05 10%, #bd6708 8%.
- **Lighting:** Top light; an additive arc glint for the pointer.
- **Materials:** Gold, red enamel.
- **Motion:** Still pictures; the wheel's turning is done by the client.
- **Construction:** 5 pictures; the title is 1042x298 px and the hub coin 454x454 px, the largest loose pictures after the scene.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 50% · saturation 81% · contrast 71% · warm 100% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #de9e0e orange 33%, #7b2a06 brown 23%, #400d05 dark red 10%, #bd6708 orange 8%, #fdf9f1 light orange 7%

### Super Wheel rim

`wheel_el_border` · atlas · 1 parts · largest 1616×1616 · sheet `sheets/wheel_el_border.webp`

- **Role:** The outer ring of the wheel.
- **Subject:** A wide gold ring with a brown outer edge.
- **Style:** As the wheel.
- **Rendering:** Concentric gold gradients.
- **Colour:** Measured: brown #763406 56%, #bb7b15 20%, gold #eab01e 14%.
- **Lighting:** Even, with a brighter inner edge.
- **Materials:** Gold.
- **Motion:** Still.
- **Construction:** One 1616x1616 px picture, the largest square picture in the game.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 38% · saturation 92% · contrast 66% · warm 100% / cool 0%
- **Palette (measured):** #763406 brown 56%, #bb7b15 orange 20%, #eab01e orange 14%, #410a01 dark red 5%, #fbeb60 gold 3%

### Super Wheel pins

`wheel_el_pins` · atlas · 1 parts · largest 1479×1480 · sheet `sheets/wheel_el_pins.webp`

- **Role:** The twelve pegs on the rim that the pointer ticks over.
- **Subject:** Twelve small orange-gold studs on a circle.
- **Style:** As the wheel.
- **Rendering:** Small spheres with a highlight.
- **Colour:** Measured: orange #c56211 44%, dark brown #4d1303 21%, gold #eba81f 14%, #fde22e 13%.
- **Lighting:** Top-left highlight on each stud.
- **Materials:** Gold.
- **Motion:** Still; it turns with the wheel.
- **Construction:** One 1479x1480 px picture, almost all of it empty.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 45% · saturation 90% · contrast 77% · warm 100% / cool 0%
- **Palette (measured):** #c56211 orange 44%, #4d1303 dark red 21%, #eba81f orange 14%, #fde22e gold 13%, #83330a brown 8%

### Super Wheel spokes

`wheel_el_separators` · atlas · 1 parts · largest 1478×1478 · sheet `sheets/wheel_el_separators.webp`

- **Role:** The lines between the wheel's twelve slices.
- **Subject:** Twelve thin gold spokes from the centre.
- **Style:** As the wheel.
- **Rendering:** Thin bevelled gold lines.
- **Colour:** Measured: orange #cc7812 33%, brown #83470f 25%, #200601 18%, gold #e2bc32 16%.
- **Materials:** Gold.
- **Motion:** Still; it turns with the wheel.
- **Construction:** One 1478x1478 px picture.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 42% · saturation 87% · contrast 57% · warm 100% / cool 0%
- **Palette (measured):** #cc7812 orange 33%, #83470f brown 25%, #200601 black 18%, #e2bc32 gold 16%, #e9d865 gold 4%

### Super Wheel slices

`wheel_slice` · skeleton · 18 parts · largest 410×750 · sheet `sheets/wheel_slice.webp`

- **Role:** The seven kinds of slice on the wheel: DOUBLE, EXTRA, MULTI (the three pot features), MINI, MINOR, MAJOR (jackpots) and MORE.
- **Subject:** A long wedge with its word written down it letter by letter, over a faint pattern (scrolls on the feature slices, clovers on Mini).
- **Style:** Fairground wheel; the words are in the game's heavy serif capitals with a contrasting stroke.
- **Rendering:** A vertical gradient that brightens toward the tip; the word has a light face, a dark stroke and an outer glow in a matching colour.
- **Colour:** Measured: dark green #075e06 15%, blue #0330b8 12%, magenta #c202e0 6%, dark red #980702 6%, green #09eb0e 6%, red #e90d02 6%; saturation 0.93. Read: each slice in its feature's colour (blue Double, green Extra, red Multi, green Mini, blue Minor, purple Major, gold More).
- **Lighting:** Brighter toward the hub.
- **Materials:** Painted enamel panels.
- **Variants:** Seven slices, each with an idle and a win animation (14 animations).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): the win state brightens the wedge and its word (0.67 s); idle is a held pose.
- **Construction:** 18 parts: seven wedge grounds of about 408x750 px, seven word strips, four glow strips. One rig for all slices.
- **Notes:** The frame on the sheet is the first animation in the file's order; all seven are on the motion sheet.
- **Skeleton (from the file):** Spine 4.1.24 · 17 bones · 25 slots · 25 region · animations: double/idle (0 s), double/win (0.67 s), extra/idle (0 s), extra/win (0.67 s), major/idle (0 s), major/win (0.67 s), mini/idle (0 s), mini/win (0.67 s), minor/idle (0 s), minor/win (0.67 s), more/idle (0 s), more/win (0.67 s), multi/idle (0 s), multi/win (0.67 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 39% · saturation 93% · contrast 50% · warm 35% / cool 48% · brighter towards: bottom (6), top (1)
- **Palette (measured):** #075e06 dark green 15%, #0330b8 blue 12%, #c202e0 magenta 6%, #980702 red 6%, #09eb0e green 6%, #e90d02 red 6%

### Super Wheel winning-slice frame

`wheel_win_frame` · skeleton · 63 parts · largest 454×454 · sheet `sheets/wheel_win_frame.webp`

- **Role:** Marks the slice the wheel stopped on.
- **Subject:** A wedge-shaped outline in running rainbow colours over the hub coin, with a dark disc that dims the rest of the wheel.
- **Style:** Neon outline, as the winning cell frame.
- **Rendering:** A bright core with glow; a 45-frame sequence runs the colours and a 14-frame white light sweeps the slice.
- **Colour:** Measured: black #080808 18%, white #f9f9f8 16%, orange #d78008 11%.
- **Lighting:** Emissive against the dimming disc.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation, win, 10 bones. Frame sequences rain_shake x45 and sector_light x14.
- **Construction:** 63 parts, 59 of them sequence frames.
- **Notes:** The dark disc in the drawn frame is the rig's own shade (a tint part), not a fault.
- **Skeleton (from the file):** Spine 4.1.24 · 10 bones · 9 slots · 35 region · animations: win (4.03 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 50% · saturation 38% · contrast 59% · warm 30% / cool 9% · brighter towards: top-right (12), left (11), bottom-left (9)
- **Palette (measured):** #080808 black 18%, #f9f9f8 white 16%, #d78008 orange 11%, #363636 grey 9%, #f8ec0d gold 7%, #676767 grey 6%

### Winning cell frame

`win_line` · skeleton · 47 parts · largest 206×198 · sheet `sheets/win_line.webp`

- **Role:** The frame that lights around each symbol of a winning line.
- **Subject:** A rounded square outline in running rainbow colours with a yellow glow and sparks.
- **Style:** Neon tube.
- **Rendering:** A bright core line with a soft glow; the colours travel around the frame over a 20-frame sequence.
- **Colour:** Measured: light violet #d886f4 15%, yellow #fdf81a 14%, cyan #5af3f4 13%, lime #a9fe43 13%; brightness 0.75.
- **Lighting:** Emissive.
- **Ambience:** The rainbow of the theme used as the win colour.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation of 3 bones; frame sequences win_linen x20 and sparks x26.
- **Construction:** 47 parts, nearly all sequence frames; a frame is 191x182 px, slightly larger than a cell.
- **Notes:** Seen in the played session around three winning sack symbols.
- **Skeleton (from the file):** Spine 4.1.24 · 3 bones · 2 slots · 21 region · animations: animation (0.63 s)
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 75% · saturation 65% · contrast 35% · warm 45% / cool 42% · brighter towards: right (2), bottom (2), top-right (1)
- **Palette (measured):** #d886f4 purple 15%, #fdf81a gold 14%, #5af3f4 cyan 13%, #a9fe43 green 13%, #88b6ff light blue 11%, #fad83d gold 9%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Bonus coin and jackpot coins

`el_bonus` · skeleton · 124 parts · largest 273×272 · sheet `sheets/el_bonus.webp`

- **Role:** The coin that carries a cash value (5.00 and 10.00 were seen on the reels) or a jackpot name (MINOR was seen); in the bonus game it is what fills the board, as the paytable pictures show it.
- **Subject:** A thick gold coin with a raised rim and an embossed four-leaf clover. The jackpot versions keep the gold rim and fill the face with a coloured enamel clover.
- **Style:** Casual 3D-look, very clean; a coin drawn as jewellery more than money.
- **Rendering:** Concentric gradients for the rim, a soft emboss for the clover; sweeps of light across the face are a 60-frame sequence, not a shader.
- **Colour:** Measured: black #0d0c0b 41% and grey #30302a 17% (grounds of the additive parts), gold #fada1a 6%, blue #0577f8 4%, green #01fd0b 2%. Read: plain gold for a cash coin, magenta for Major, green for Mini, blue for Minor.
- **Lighting:** Top light; a white-yellow halo and a ring flash behind it when it lands; small star glints on the rim.
- **Ambience:** Every coin is a small prize in itself.
- **Materials:** Polished gold; glossy coloured enamel on the jackpot faces.
- **Variants:** Four skins: el_bonus (gold), el_major (magenta), el_mini (green), el_minor (blue). Ten-frame turning-coin sequences for each (coin, major, mini, minor).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): landing 0.67 s, idle 3.97 s (a light sweep and rim glints), collect 1 s, duplicate 1.47 s (a second coin lifts off the first), collected (a held state). 65 bones, 61 slots.
- **Construction:** 124 parts, most of them frames of the sweep (60) and of the four turning coins (10 each); a coin face is 150x150 px.
- **Notes:** A part named placeholder marks where the client writes the coin's value with the numbers_symbols font; it is not drawn here.
- **Skeleton (from the file):** Spine 4.1.24 · 65 bones · 61 slots · 135 region · animations: collect (1 s), collected (0 s), duplicate (1.47 s), idle (3.97 s), landing (0.67 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 28% · saturation 44% · contrast 33% · warm 50% / cool 14% · brighter towards: top-right (15), top-left (11), top (4)
- **Palette (measured):** #0d0c0b black 41%, #30302a grey 17%, #fada1a gold 6%, #0577f8 blue 4%, #01fd0b green 2%, #5a5bff blue 2%

### Coloured bonus coins (blue, green, red)

`el_bonus_progress` · skeleton · 70 parts · largest 279×285 · sheet `sheets/el_bonus_progress.webp`

- **Role:** The three coins that feed the three pots: a blue coin goes to Double, a green one to Extra, a red one to Multi (the paytable art pairs each coin with its pot by an arrow).
- **Subject:** The bonus coin with a gold rim and a face in one feature colour, the clover embossed in the same colour.
- **Style:** As the bonus coin.
- **Rendering:** A wide gold rim around a glossy enamel centre with radial brushed highlights.
- **Colour:** Measured over the parts: black #131212 69% and grey #3e3b36 12% (grounds of additive parts), gold #f8f147 3%. Read: saturated blue, green and red-orange faces in gold.
- **Lighting:** Top light; a ring of yellow light and a burst of rays behind it on landing.
- **Materials:** Gold and coloured enamel.
- **Variants:** Three skins: blue, green, red.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): landing 0.5 s and idle 3 s; a 60-frame light sweep (coin_sweep). 14 bones, 13 slots.
- **Construction:** 70 parts, 60 of them the sweep frames; each coin face is one 250x250 px picture.
- **Notes:** Drawn larger than a reel cell: in the game screens a coloured coin overlaps its neighbours.
- **Skeleton (from the file):** Spine 4.1.24 · 14 bones · 13 slots · 76 region · animations: idle (3 s), landing (0.5 s)
- **Measured:** dark, muted, warm and cool mixed, medium contrast, hard-edged · brightness 20% · saturation 23% · contrast 26% · warm 50% / cool 3% · brighter towards: top-right (7), top-left (4), top (1)
- **Palette (measured):** #131212 black 69%, #3e3b36 grey 12%, #f8f147 gold 3%

### Paying symbols, animated (11 rigs in one skeleton)

`el_symbols` · skeleton · 28 parts · largest 172×164 · sheet `sheets/el_symbols.webp`

- **Role:** The win animation of every regular symbol: el_01 to el_11.
- **Subject:** Five letter-and-number lows (10, J, Q, K, A) and six picture symbols: a pocket watch on a purple clover, a pipe on a blue clover, a beer mug with a clover badge (green tile), a sack of gold tied with a blue ribbon (blue tile), a harp with a clover (purple tile) and a horseshoe with a clover (red tile).
- **Style:** Casual 3D-look cartoon objects, chunky and rounded; the lows are fat serif capitals with a wood-grain face. The four top symbols sit on framed colour tiles, the two mid symbols on a clover-shaped pad, the lows directly on the cream reel.
- **Rendering:** Smooth gradients, bright top highlights, no outline; each top symbol is layered as tile, object, tile frame top, shadow and a small additive glint, so the object can pop out over its frame.
- **Colour:** Measured: dark green #065704 8%, green #139216 7%, red #d80c09 7%, dark red #660b0a 6%, blue #031fee 5%, magenta #e401f4 3%; saturation 0.83. Read: one saturated colour per symbol, gold on every object.
- **Lighting:** Top light with a soft drop shadow under each object (separate shadow parts); glints are additive stars.
- **Ambience:** Bright pub-and-luck props, clean and new.
- **Materials:** Gold, glazed ceramic and foam (mug), cloth (sack), carved wood (pipe, letters), enamel tiles.
- **Variants:** 11 symbols. Each top symbol has a tile, a frame and a frame_top part.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation per symbol, each 1 s, in one skeleton of 71 bones and 67 slots: the object swells out of its tile and a glint crosses it. A four-frame sequence (el x4) belongs to it.
- **Construction:** 28 parts; a tile is 172x164 px. All eleven symbols share one skeleton and one atlas instead of eleven rigs.
- **Notes:** The frame drawn on the sheet is el_08 (the mug); the motion sheet shows all eleven.
- **Skeleton (from the file):** Spine 4.1.24 · 71 bones · 67 slots · 67 region · animations: el_01 (1 s), el_02 (1 s), el_03 (1 s), el_04 (1 s), el_05 (1 s), el_06 (1 s), el_07 (1 s), el_08 (1 s), el_09 (1 s), el_10 (1 s), el_11 (1 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 35% · saturation 83% · contrast 48% · warm 51% / cool 34% · brighter towards: top (4), top-left (4), top-right (4)
- **Palette (measured):** #065704 dark green 8%, #139216 green 7%, #d80c09 red 7%, #660b0a dark red 6%, #031fee blue 5%, #a01910 red 4%

### Wild: the leprechaun

`el_wild` · skeleton · 9 parts · largest 358×358 · sheet `sheets/el_wild.webp`

- **Role:** The Wild symbol and the game's only figure; it lands stacked (two were seen on a reel in the played session).
- **Subject:** A leprechaun's head and shoulders in a gold shield-shaped frame: red beard, wide grin, rosy cheeks, a tall green hat with a gold buckle and a clover tucked in the band, a green bow tie. The hat breaks out over the top of the frame.
- **Style:** Friendly cartoon portrait in the casual 3D-look manner of the rest of the game; large head, small features, no caricature edge.
- **Rendering:** Soft painted volumes with clean edges and no outline; warm orange-to-yellow gradient inside the frame. The frame is split into a back board and a top lip so the head sits between them.
- **Colour:** Measured: black #0a0502 43% (additive rays), gold #fcdc25 19%, brown #5a290f 10%, orange #e95109 5%, dark cyan #143a3c 4%. Read: green hat and orange beard on a gold and orange field.
- **Lighting:** Front-top light on the face, a yellow rim around the whole frame; on a win a radial flare of rays opens behind it.
- **Ambience:** Cheerful and lucky; the one face in a game otherwise made of objects.
- **Materials:** Felt hat, gold buckle and frame, soft skin and hair.
- **Variants:** One design. A blurred copy for the spinning reel is in the symbols sheet (el_wild_move).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): idle 2 s (a slow breathing bob of hat and head), landing 0.33 s, win 1.2 s (the symbol pulses and an orange halo flares behind it). 37 bones, 25 slots.
- **Construction:** 9 parts (hat, head, body, mouth, frame back, frame board, frame top, ray, flare), the head 132x118 px; hat and head are meshes so they can bend. Symbol box about 168x160 px.
- **Skeleton (from the file):** Spine 4.1.24 · 37 bones · 25 slots · 23 region, 2 mesh · animations: idle (2 s), landing (0.33 s), win (1.2 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 32% · saturation 69% · contrast 50% · warm 92% / cool 6% · brighter towards: bottom (1), bottom-left (1), top (1)
- **Palette (measured):** #0a0502 black 43%, #fcdc25 gold 19%, #5a290f brown 10%, #e95109 orange 5%, #143a3c dark cyan 4%, #9a320b brown 4%

### Symbols as still pictures and reel-blur copies

`symbols-0` · atlas · 41 parts · largest 252×269 · sheet `sheets/symbols-0.webp`

- **Role:** What the reels draw while they turn and when they stop: every symbol once sharp (_static) and once blurred downwards (_move).
- **Subject:** The eleven paying symbols, the Wild, the gold bonus coin, the three coloured bonus coins (double, extra, multi), the three jackpot coins (mini, minor, major) and the three jackpot words as small labels.
- **Style:** The same art as the rigs, flattened to one picture per symbol.
- **Rendering:** The _move copies are the same picture with a vertical motion blur baked in, so a spinning reel needs no shader.
- **Colour:** Measured: orange #dc8d12 18%, magenta #b31dc8 7%, gold #f7cf28 7%, red #ba190c 6%, dark green #0e650e 5%, blue #138eee 4%; saturation 0.81, contrast 0.61 (high).
- **Lighting:** Top and top-left (measured: top 16, top-left 15).
- **Variants:** 41 pictures: static and move for each of 11 symbols, the Wild and the bonus coins, plus major_symbol, minor_symbol and mini_symbol word labels.
- **Motion:** None of its own: these are the stills. The blur copies stand in for motion.
- **Construction:** One TexturePacker sheet (symbols-0). A regular symbol is about 168x160 px, a coloured bonus coin 252x251 px (it overlaps its cell), a blurred coin 252x269 px.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 46% · saturation 81% · contrast 60% · warm 57% / cool 29% · brighter towards: top (16), top-left (15)
- **Palette (measured):** #dc8d12 orange 18%, #b31dc8 magenta 7%, #f7cf28 gold 7%, #ba190c red 6%, #0e650e dark green 5%, #138eee blue 4%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The three pots (Double, Multi, Extra)

`bonus_accum` · skeleton · 148 parts · largest 388×331 · sheet `sheets/bonus_accum.webp`

- **Role:** The feature collectors that stand on top of the reel board in the base game and beside the bonus board: each bonus coin of a pot's colour flies into it, and the pot's fill shows how close its feature is. They take the place a mascot would have on stage, which is why this run sorts them under Characters (a sorting decision).
- **Subject:** A fat round cauldron with two scroll handles, a four-leaf clover badge on its belly and a word plate on its rim (DOUBLE, EXTRA or MULTI), heaped with clover-stamped gold coins that pile higher in steps until they tower over the pot.
- **Style:** Casual 3D-look cartoon: short, wide, toy-like, with engraved scroll lines on the body. The same lettering as the logo sits on the plate.
- **Rendering:** Smooth enamel gradients with a bright specular patch and a light rim, no outline; the coins are painted piles, not single sprites. Glow, rainbow columns and sparkles are separate additive parts.
- **Colour:** Measured over the parts: gold #fad819 19%, orange #e08e14 18%, black #070603 16% (the ground of additive parts), brown #ac4b0c 10%; hues orange 47%, yellow 36%. Read: the body is the only place the feature colour sits (blue for Double, green for Extra, red for Multi); everything else is gold.
- **Lighting:** Lit from above with the highlight high on the belly (measured light direction over the parts: top-right 12, top 10, top-left 9). A yellow halo hugs the silhouette at rest; when a pot triggers, a column of light in its own colour, or a rainbow, shoots up from the mouth.
- **Ambience:** Abundance: the coins never sit still, and the pot visibly gets richer.
- **Materials:** Glossy enamelled metal for the body, polished gold for the badge, plate rim and coins.
- **Variants:** One rig, three skins: double_up (blue), extra_spins (green), multi_spins (red). Eleven fill levels (idle_0 to idle_10), each with three idle variants; collect_positive_1 to _10 and collect_positive_run_0 to _10 for a coin arriving at each level; trigger_start, trigger_loop and active states; separate coin heaps for the front and the back of the pot on the bonus desk. As shipped, the double_up skin is mirrored (its word reads backwards) and reads right only when the rig is flipped: that the game flips it is inference from the game screens, where DOUBLE reads right. The sheet shows it flipped.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): 76 animations on 138 bones and 185 slots. At rest the heap shimmers and sparkles cross it (idles of 1.3 to 3.3 s); a collected coin makes the pot squash, flash white-gold and settle one level fuller (1.33 s); the trigger bleaches the pot to white-gold under a rainbow column (trigger_start 0.6 s, trigger_loop 1.6 s). Frame sequences inside the rig: coin x10, coins x11, hit x21, pot_glow x29.
- **Construction:** 148 parts on two atlas pages; the largest is a coin heap of 388x331 px, a pot body is about 210 px wide. One skeleton serves all three pots through skins, so only the body, the word and the light colour are drawn three times. 3 meshes (coin heaps that bend), the rest plain regions; additive slots for all light.
- **Notes:** A part named placeholder_front marks where the client writes a number; it is not drawn here.
- **Skeleton (from the file):** Spine 4.1.24 · 138 bones · 185 slots · 438 region, 3 mesh · animations: active_idle (3.33 s), active_trigger_idle (1.03 s), active_trigger_idle_double (1.37 s), all_coin_up (0 s), all_coin_up_2 (0 s), back_coins (0 s), back_coins_bonus (0 s), back_coins_bonus_desk_1 (2.6 s), collect_negative (0.3 s), collect_positive_1 (1.33 s), collect_positive_2 (1.33 s), collect_positive_3 (1.33 s), collect_positive_4 (1.33 s), collect_positive_5 (1.33 s), collect_positive_6 (1.33 s), collect_positive_7 (1.33 s), collect_positive_8 (1.33 s), collect_positive_9 (1.33 s), collect_positive_10 (1.33 s), collect_positive_run_0 (2.83 s), collect_positive_run_1 (2.83 s), collect_positive_run_2 (2.83 s), collect_positive_run_3 (2.83 s), collect_positive_run_4 (2.83 s), collect_positive_run_5 (2.83 s), collect_positive_run_6 (2.83 s), collect_positive_run_7 (2.1 s), collect_positive_run_8 (2.1 s), collect_positive_run_9 (2.1 s), collect_positive_run_10 (2.1 s), front_coins_bonus (2.67 s), front_coins_bonus_desk_1 (2.6 s), front_coins_bonus_desk_1_1 (2.67 s), front_coins_bonus_desk_2 (2.6 s), front_coins_bonus_desk_2_back (1.33 s), front_coins_bonus_desk_3 (2.6 s), idle_0_0 (3.33 s), idle_0_1 (1.83 s), idle_0_2 (2 s), idle_1_0 (3.17 s), idle_1_1 (1.83 s), idle_1_2 (2 s), idle_2_0 (3.33 s), idle_2_1 (2 s), idle_2_2 (2 s), idle_3_0 (3.33 s), idle_3_1 (1.57 s), idle_3_2 (2 s), idle_4_0 (3.13 s), idle_4_1 (2 s), idle_4_2 (2 s), idle_5_0 (3.17 s), idle_5_1 (2 s), idle_5_2 (2 s), idle_6_0 (3.33 s), idle_6_1 (1.83 s), idle_6_2 (2 s), idle_7_0 (3.33 s), idle_7_1 (1.83 s), idle_7_2 (2 s), idle_8_0 (3.33 s), idle_8_1 (2.17 s), idle_8_2 (2.17 s), idle_9_0 (2.67 s), idle_9_1 (1.33 s), idle_9_2 (1.53 s), idle_10_0 (2.67 s), idle_10_1 (1.33 s), idle_10_2 (1.33 s), idle_glow (5.67 s), idle_popup (1.33 s), idle_popup_activate (1 s), idle_popup_startscr (1.33 s), idle_popup_tint (0.2 s), trigger_loop (1.6 s), trigger_start (0.6 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 51% · saturation 72% · contrast 54% · warm 86% / cool 7% · brighter towards: top-right (12), top (10), top-left (9)
- **Palette (measured):** #fad819 gold 19%, #e08e14 orange 18%, #070603 black 16%, #ac4b0c brown 10%, #fae65a gold 9%, #7a2408 dark red 5%


## Logo and title

The game's own wordmark.

### Logo: Lucky Penny 3 Pots Super Wheel

`logo` · skeleton · 119 parts · largest 399×189 · sheet `sheets/logo.webp`

- **Role:** The game's title, top left in the base game and on the start screen.
- **Subject:** LUCKY PENNY in cream capitals on a red band, a large red 3 with a gold edge, POTS in cream with the O replaced by a small six-colour prize wheel, and SUPER WHEEL in white italics on a purple ribbon.
- **Style:** Casino-poster lettering: heavy slab-serif capitals with big first letters, stacked and slightly arched.
- **Rendering:** Cream-to-yellow face, red stroke, dark red extrusion, a yellow outer glow; the purple ribbon has folded ends.
- **Colour:** Measured: black #050303 47% (ground of additive parts), cream #fcf9ec 7%, light magenta #fda3fd 6%, yellow #fdee0a 5%, magenta #ec16ee 5%, red #f70202 4%.
- **Lighting:** A star glint travels over the letters; a soft halo behind.
- **Ambience:** Loud and friendly.
- **Materials:** Enamel sign with gold edge.
- **Variants:** Two animations: start (4.67 s; the words arrive one by one: LUCKY PENNY, the wheel, 3 POTS, the ribbon) and idle (9.33 s).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): 31 bones, 36 slots; frame sequences lucky x30, 3 x26, logo x25 and pot_seq x21 are light sweeps across each word.
- **Construction:** 119 parts, about 100 of them sweep frames; the word plates are about 380 px wide, the whole logo about 430x330 px.
- **Skeleton (from the file):** Spine 4.1.24 · 31 bones · 36 slots · 36 region · animations: idle (9.33 s), start (4.67 s)
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged · brightness 30% · saturation 50% · contrast 66% · warm 80% / cool 8% · brighter towards: bottom-left (20), top-right (17), top-left (11)
- **Palette (measured):** #050303 black 47%, #fcf9ec light gold 7%, #fda3fd light magenta 6%, #fdee0a gold 5%, #ec16ee magenta 5%, #f70202 red 4%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### MORE popup

`add_coin_popup` · skeleton · 10 parts · largest 481×163 · sheet `sheets/add_coin_popup.webp`

- **Role:** The burst that announces the wheel's MORE slice (more coins added; the wording is the art's, the rule was not seen in play).
- **Subject:** The word MORE in red-and-yellow capitals in an orange fire burst with sparks.
- **Style:** As the big win words.
- **Rendering:** Yellow-to-red gradient face, red stroke; additive orange gradients and two particle pictures.
- **Colour:** Measured: dark brown #1f0e05 26%, brown #53280a 18%, yellow #fdf015 11%, red #ea0503 8%.
- **Lighting:** Emissive orange.
- **Ambience:** Hot and quick.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation of 2.17 s, 37 bones, 31 slots.
- **Construction:** 10 parts; the word is 481x163 px.
- **Skeleton (from the file):** Spine 4.1.24 · 37 bones · 31 slots · 31 region · animations: animation (2.17 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 37% · saturation 85% · contrast 57% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #1f0e05 black 26%, #53280a brown 18%, #fdf015 gold 11%, #ea0503 red 8%, #faf368 gold 7%, #fa9d06 orange 4%

### Win coin, turning

`coins` · atlas · 10 parts · largest 132×133 · sheet `sheets/coins.webp`

- **Role:** The coin that showers on big wins (the client's particle emitter throws it; the emitter settings are in bw_emitter.json).
- **Subject:** The clover coin seen face-on, edge-on and between.
- **Style:** As the bonus coin.
- **Rendering:** Ten painted frames of one turn.
- **Colour:** Measured: gold-orange #e09c1b 51%, yellow #f8e22f 20%, brown #a04b0b 17%.
- **Lighting:** Top light.
- **Materials:** Gold.
- **Motion:** A 10-frame turn (coin x10).
- **Construction:** 10 pictures of about 132x133 px in the bigwin-0 sheet.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged · brightness 65% · saturation 85% · contrast 49% · warm 100% / cool 0% · brighter towards: top (3), top-right (2)
- **Palette (measured):** #e09c1b orange 51%, #f8e22f gold 20%, #a04b0b brown 17%, #f9eb68 gold 9%, #c4680f orange 2%

### Big win banners and feature win banners

`bigwin` · skeleton · 56 parts · largest 511×513 · sheet `sheets/bigwin.webp`

- **Role:** The full-screen win celebrations: Big Win, Mega Win, Epic Win and Super Win, and (in the second rig that uses the same pictures, game_popups) Bonus Win, Grand Win and Double Grand Win.
- **Subject:** A two-word banner in heavy capitals over a rainbow swirl, a ray burst, a large green four-leaf clover, a small rainbow arc and tumbling clover coins.
- **Style:** Casino-poster lettering, the same family as the logo; each tier in its own colour.
- **Rendering:** Words with a gradient face, a contrasting stroke and a dark extrusion; the light behind is additive (rainbow blur, ray fan, lens flare, particles).
- **Colour:** Measured: black #0e0702 21% (ground of additive parts), orange #eda723 10%, red #e50503 9%, gold #fbe40f 8%, brown #582808 7%. Read: BIG WIN green, HUGE WIN blue on yellow, MEGA WIN magenta, EPIC WIN and the feature wins red on yellow.
- **Lighting:** Emissive: the word stands in a rotating rainbow light.
- **Ambience:** The rainbow is the win; gold falls out of it.
- **Materials:** Enamel letters, gold coins.
- **Variants:** Seven banner words as pictures (big, huge, mega, epic, bonus win, grand win, double grand win, and a plain DOUBLE). The rig names four tiers BigWin, MegaWin, EpicWin, SuperWin; which picture each tier shows was read from the drawn frames (BigWin green, EpicWin red).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): BigWin 6.33 s, SuperWin 7.97 s, MegaWin and EpicWin 11.33 s on 39 bones and 37 slots; the word punches in, the swirl turns behind it, coins tumble (chest_coin x12). game_popups: BonusWin 9.17 s, grand and double_grand 10.83 s.
- **Construction:** The parts sit on two atlas pages (bigwin) that two rigs share: bigwin.atlas and game_popups.atlas name the same pages, so each part is cut twice here (56 parts for 28 pictures). The largest is the rainbow swirl, 596x598 px; a word is about 600x110 px. A part named counter_placeholder marks where the amount is written.
- **Notes:** No big win came in the played session; this is read from the files and the drawn frames. In the drawn frames the word is small in a wide light field because the frame is cropped to the light's reach.
- **Skeleton (from the file):** Spine 4.1.24 · 39 bones · 37 slots · 62 region · animations: BigWin (6.33 s), EpicWin (11.33 s), MegaWin (11.33 s), SuperWin (7.97 s)
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 40% · saturation 75% · contrast 66% · warm 84% / cool 11% · brighter towards: top (10), top-left (2)
- **Palette (measured):** #0e0702 black 21%, #eda723 orange 10%, #e50503 red 9%, #fbe40f gold 8%, #582808 brown 7%, #a60804 red 6%

### Feature popups (x2, Double, +1 respin)

`bonus_popups` · skeleton · 46 parts · largest 240×185 · sheet `sheets/bonus_popups.webp`

- **Role:** The small popups that show which pot feature fired: a multiplier on a coin (x2), the doubled board (a blue-and-yellow board icon), and the fourth respin lamp.
- **Subject:** A Major coin with a red x2 tag; a small blue grid of two boards; a 1-2-3 lamp bar with a green 4; red-and-yellow numerals 2, 3, 5 and x.
- **Style:** Icons made from the game's own pieces at small size.
- **Rendering:** As their sources, with a white-gold halo and sparks.
- **Colour:** Measured: orange #f79107 17%, black #0e0906 15%, cream #fefee9 14%.
- **Lighting:** A halo flash behind each.
- **Variants:** Nine animations: x2, double and frame_4, each with an _activate and a _tint form.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): the main popups run 1.5 to 3 s, activate 0.83 s; particl x22 frame sequence.
- **Construction:** 46 parts, 22 of them spark frames; the board icon is 240x185 px.
- **Notes:** These three icons also sit on the start screen under the pots (seen in the opening card).
- **Skeleton (from the file):** Spine 4.1.24 · 48 bones · 59 slots · 313 region · animations: double (1.5 s), double_activate (0.83 s), double_tint (0 s), frame_4 (1.5 s), frame_4_activate (0.83 s), frame_4_tint (0 s), x2 (3 s), x2_activate (0.83 s), x2_tint (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 49% · saturation 66% · contrast 66% · warm 82% / cool 14% · brighter towards: right (1), bottom (1), top (1)
- **Palette (measured):** #f79107 orange 17%, #0e0906 black 15%, #fefee9 light gold 14%, #5a4a2c brown 9%, #faed6e gold 6%, #1827f3 blue 5%

### Line win flash

`label_win_vfx` · skeleton · 4 parts · largest 278×151 · sheet `sheets/label_win_vfx.webp`

- **Role:** The burst behind the amount of a line win (0.30 was seen over three sacks in the played session).
- **Subject:** An orange ray burst with gold sparks.
- **Style:** Pure light.
- **Rendering:** Additive rays over a dark ray shadow.
- **Colour:** Measured: orange-brown #b66f14 40%, black #0d0904 29%, #6a3d04 19%.
- **Lighting:** Emissive.
- **Variants:** small_win and medium_win.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): both 1.17 s; 21 bones, 17 slots.
- **Construction:** 4 parts; counter_placeholder marks where the amount is written with the numbers_win_lines font.
- **Skeleton (from the file):** Spine 4.1.24 · 21 bones · 17 slots · 17 region · animations: medium_win (1.17 s), small_win (1.17 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, low contrast, hard-edged · brightness 29% · saturation 63% · contrast 24% · warm 69% / cool 0%
- **Palette (measured):** #b66f14 orange 40%, #0d0904 black 29%, #6a3d04 brown 19%, #373028 brown 6%, #8e8e8e grey 3%, #646464 grey 2%

### BONUS GAME title

`popups-0` · atlas · 1 parts · largest 840×194 · sheet `sheets/popups-0.webp`

- **Role:** The title shown when the bonus game starts.
- **Subject:** BONUS GAME in arched red capitals with a yellow edge and a dark red extrusion.
- **Style:** The logo's lettering.
- **Rendering:** Red gradient face with a white top highlight, yellow stroke, dark extrusion.
- **Colour:** Measured: red #ed0502 24%, yellow #fce70a 16%, dark red #a71304 13%, gold #e9a719 11%.
- **Lighting:** Top highlight on each letter.
- **Motion:** A still picture; the client moves it.
- **Construction:** One 840x194 px picture in its own sheet.
- **Notes:** Not seen in play: the bonus game did not come in the played session.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 47% · saturation 86% · contrast 85% · warm 100% / cool 0%
- **Palette (measured):** #ed0502 red 24%, #fce70a gold 16%, #a71304 red 13%, #e9a719 orange 11%, #ce5f0e orange 8%, #843006 brown 7%


## Effects

Frame sequences, glows, particles and transitions.

### Bonus anticipation frame

`anticipation_bonus` · skeleton · 8 parts · largest 200×175 · sheet `sheets/anticipation_bonus.webp`

- **Role:** Lights a reel cell while the reels wait for another bonus coin (inference from its name).
- **Subject:** A rounded square of rainbow neon with star glints and violet light streaks inside.
- **Style:** Neon.
- **Rendering:** A bright line with glow; six frames of rising light.
- **Colour:** Measured: dark violet #0c051f 49%, #18135f 25%, #35229e 8%, pale yellow #f9f590 3%.
- **Lighting:** Emissive.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation of 0.97 s; light x6.
- **Construction:** 8 parts; the frame is 200x175 px.
- **Skeleton (from the file):** Spine 4.1.24 · 19 bones · 17 slots · 22 region · animations: animation (0.97 s)
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 15% · saturation 84% · contrast 16% · warm 10% / cool 88%
- **Palette (measured):** #0c051f black 49%, #18135f dark blue 25%, #35229e blue 8%, #f9f590 light gold 3%

### Transition to the bonus game

`bn_transition` · skeleton · 47 parts · largest 360×800 · sheet `sheets/bn_transition.webp`

- **Role:** The wipe between the base game and the bonus game.
- **Subject:** A broad rainbow wave sweeping across the screen, carrying coins in all four colours and small butterflies of light.
- **Style:** Painterly light.
- **Rendering:** Blurred rainbow bands (a tall band, a head, a curved blade, a swirl) with turning coins on top.
- **Colour:** Measured: gold #e6a51c 28%, red-orange #ec3a0e 12%, green #1f710f 8%, blue #1898f4 8%; saturation 0.84.
- **Lighting:** Emissive.
- **Ambience:** The rainbow arrives and takes you to the gold.
- **Variants:** fs_transition and fs_transition_fin.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): both 1.9 s, on 126 bones and 204 slots; ten-frame turning coins in blue, green, red and gold.
- **Construction:** 47 parts on one page; the tall rainbow band is 360x800 px.
- **Skeleton (from the file):** Spine 4.1.24 · 126 bones · 204 slots · 402 region · animations: fs_transition (1.9 s), fs_transition_fin (1.9 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 53% · saturation 84% · contrast 57% · warm 58% / cool 32% · brighter towards: top-left (6), bottom (5), top (5)
- **Palette (measured):** #e6a51c orange 28%, #ec3a0e red 12%, #1f710f dark green 8%, #1898f4 blue 8%, #fae442 gold 7%, #176199 blue 4%

### Pot collect effect

`bonus_accum_vfx` · skeleton · 5 parts · largest 385×240 · sheet `sheets/bonus_accum_vfx.webp`

- **Role:** The light over a pot when a coin arrives (in front of the pot).
- **Subject:** A small rainbow arc with a white flash and sparks.
- **Style:** Pure light.
- **Rendering:** A rainbow picture and a white copy of it, a star burst and a dot.
- **Colour:** Measured: black #0a0401 38% (ground), white #ffffff 24%, gold #bf9419 10%, blue #3a56d5 5%.
- **Lighting:** Emissive.
- **Variants:** collect_positive_front, collect_positive_run_front, collect_negative_front.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): 0.83 to 0.93 s each.
- **Construction:** 5 parts; the arc is 385x240 px.
- **Skeleton (from the file):** Spine 4.1.24 · 25 bones · 25 slots · 25 region · animations: collect_negative_front (0.93 s), collect_positive_front (0.93 s), collect_positive_run_front (0.83 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 43% · saturation 52% · contrast 45% · warm 64% / cool 11%
- **Palette (measured):** #0a0401 black 38%, #ffffff light gold 24%, #bf9419 orange 10%, #3a56d5 blue 5%, #5a3002 brown 5%, #509297 cyan 3%

### Disc glow

`drum_glow` · atlas · 1 parts · largest 204×204 · sheet `sheets/drum_glow.webp`

- **Role:** A flat yellow disc of light, used behind round pieces (the name says drum, the wheel).
- **Subject:** A soft-edged yellow circle.
- **Rendering:** One flat picture.
- **Colour:** Measured: yellow #ffed35 100%.
- **Motion:** Still.
- **Construction:** One 204x204 px picture.
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 89% · saturation 79% · contrast 0% · warm 100% / cool 0%
- **Palette (measured):** #ffed35 gold 100%

### Multiplier tag glow

`el_bonus_multiplier_glow` · skeleton · 1 parts · largest 133×85 · sheet `sheets/el_bonus_multiplier_glow.webp`

- **Role:** The soft light behind a multiplier tag on a coin, in three widths.
- **Subject:** A pale yellow blurred oval.
- **Style:** Pure light.
- **Rendering:** One soft picture scaled.
- **Colour:** Measured: black #090804 40% (ground), pale gold #f8de6e 36%.
- **Variants:** Three skins x_2, x_22, x_222: one, two or three digits wide.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): a held pose.
- **Construction:** One 133x85 px part.
- **Skeleton (from the file):** Spine 4.1.24 · 2 bones · 1 slots · 3 region · animations: animation (0 s)
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged, strong highlights · brightness 42% · saturation 49% · contrast 88% · warm 100% / cool 0%
- **Palette (measured):** #090804 black 40%, #f8de6e gold 36%, #9b8a45 yellow 11%, #463e1e brown 8%, #cdb65c gold 2%, #685c2d brown 2%

### Bonus coin landing ring

`el_bonus_vfx` · skeleton · 9 parts · largest 230×230 · sheet `sheets/el_bonus_vfx.webp`

- **Role:** The ring of light around a bonus coin as it lands or is collected.
- **Subject:** A thin gold ring with a flaring edge.
- **Style:** Pure light.
- **Rendering:** Several additive rings and two flares.
- **Colour:** Measured: black #050301 63% (ground), dark gold #5a4b07 14%, pale gold #e3d352 7%.
- **Lighting:** Emissive.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): one animation of 0.93 s; 35 bones, 26 slots.
- **Construction:** 9 parts of about 230x230 px.
- **Skeleton (from the file):** Spine 4.1.24 · 35 bones · 26 slots · 26 region · animations: animation (0.93 s)
- **Measured:** dark, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 18% · saturation 38% · contrast 35% · warm 68% / cool 0% · brighter towards: top-left (2)
- **Palette (measured):** #050301 black 63%, #5a4b07 brown 14%, #e3d352 gold 7%, #322b1d brown 3%, #6a6967 grey 2%

### Spark, orange

`glow` · atlas · 1 parts · largest 35×35 · sheet `sheets/glow.webp`

- **Role:** A particle picture.
- **Subject:** A small orange point of light.
- **Rendering:** One soft dot.
- **Colour:** Measured: orange #fd6902 69%, #ffc220 22%.
- **Motion:** Thrown by the client's particle emitters (bg_em_part.json, pot_part.json).
- **Construction:** 35x35 px.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 60% · saturation 94% · contrast 43% · warm 100% / cool 0%
- **Palette (measured):** #fd6902 orange 69%, #ffc220 orange 22%, #fff452 gold 9%

### Multiplier coin flight

`multiplier_effect` · skeleton · 37 parts · largest 410×205 · sheet `sheets/multiplier_effect.webp`

- **Role:** The coin that flies from the Multi pot to a coin on the board, and its miss.
- **Subject:** A gold clover coin with a rainbow tail, a violet-white flare where it lands.
- **Style:** Painterly light on a solid coin.
- **Rendering:** A turning coin sequence under a stretched rainbow; 4 mesh parts let the tail bend.
- **Colour:** Measured: black #050302 37% (ground), yellow #f9e93c 20%, gold #dda521 15%.
- **Lighting:** Emissive tail; flare at the end.
- **Variants:** animation (a hit, 1.67 s) and miss (2.33 s).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): 37 bones, 29 slots; coin x10 and pots_active x20 sequences.
- **Construction:** 37 parts; the motion streak is 410x205 px.
- **Skeleton (from the file):** Spine 4.1.24 · 37 bones · 29 slots · 4 mesh, 110 region · animations: animation (1.67 s), miss (2.33 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 42% · saturation 67% · contrast 41% · warm 93% / cool 4% · brighter towards: bottom (7), bottom-left (7), bottom-right (3)
- **Palette (measured):** #050302 black 37%, #f9e93c gold 20%, #dda521 orange 15%, #808408 brown 9%, #fdf780 gold 3%, #4d3e06 brown 3%

### Spark, small

`red_glow` · atlas · 1 parts · largest 25×25 · sheet `sheets/red_glow.webp`

- **Role:** A particle picture.
- **Subject:** A smaller orange point of light.
- **Rendering:** One soft dot.
- **Colour:** Measured: orange #fd6e01 69%, yellow #fdd923 26%.
- **Motion:** Thrown by a particle emitter.
- **Construction:** 25x25 px.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 61% · saturation 96% · contrast 39% · warm 100% / cool 0%
- **Palette (measured):** #fd6e01 orange 69%, #fdd923 gold 26%, #fea90b orange 5%

### Star glint

`star1` · atlas · 1 parts · largest 98×98 · sheet `sheets/star1.webp`

- **Role:** A particle picture.
- **Subject:** A four-point orange star.
- **Rendering:** One soft star.
- **Colour:** Measured: red-orange #fc4001 70%, #fca410 20%.
- **Motion:** Thrown by a particle emitter.
- **Construction:** 98x98 px.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 50% · saturation 95% · contrast 30% · warm 100% / cool 0%
- **Palette (measured):** #fc4001 red 70%, #fca410 orange 20%, #fff04d gold 10%

### Star glint, small

`star_2` · atlas · 1 parts · largest 68×68 · sheet `sheets/star_2.webp`

- **Role:** A particle picture.
- **Subject:** A four-point star with a yellow core.
- **Rendering:** One soft star.
- **Colour:** Measured: #fd4501 44%, yellow #fee232 26%, #fd9906 24%.
- **Motion:** Thrown by a particle emitter.
- **Construction:** 68x68 px.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 61% · saturation 91% · contrast 34% · warm 100% / cool 0%
- **Palette (measured):** #fd4501 orange 44%, #fee232 gold 26%, #fd9906 orange 24%, #ffff92 light gold 5%

### Wheel and pot back rays

`wheel_rays` · skeleton · 7 parts · largest 361×399 · sheet `sheets/wheel_rays.webp`

- **Role:** The rays behind the wheel and behind the board.
- **Subject:** A yellow disc of light with fine rays; in the bonus skin an arc of light over a round fan.
- **Style:** Pure light.
- **Rendering:** One grey ray fan tinted and turned many times (146 slots from 7 pictures).
- **Colour:** Measured: black #151413 42% (ground), yellow #feeb02 29%.
- **Lighting:** Emissive.
- **Variants:** Skins main and bonus; animations idle, part, static.
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): idle and part 2 s; 171 bones.
- **Construction:** 7 parts.
- **Skeleton (from the file):** Spine 4.1.24 · 171 bones · 146 slots · 157 region · animations: idle (2 s), part (2 s), static (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 39% · saturation 37% · contrast 41% · warm 41% / cool 0%
- **Palette (measured):** #151413 black 42%, #feeb02 gold 29%, #444242 grey 16%, #737373 grey 5%


## Game interface

Buttons, counters and panels drawn for this game.

### Jackpot panel lights

`grand_panel` · skeleton · 46 parts · largest 215×118 · sheet `sheets/grand_panel.webp`

- **Role:** The live layer over the four jackpot plates (Grand, Major, Minor, Mini): the name's shine, the plate's glow and the frame that runs around a plate about to pay.
- **Subject:** The four jackpot words in the logo's lettering, each in its own colour, with thin gold lines, soft glows and a rainbow outline for Grand.
- **Style:** Poster lettering on small plates.
- **Rendering:** Words with stroke and extrusion; additive glows; a 29-frame running frame.
- **Colour:** Measured: black #070503 45% (ground of additive parts), brown #64461d 12%, pale gold #f6e99d 11%. Read: Grand red and gold, Major magenta, Minor blue, Mini green.
- **Lighting:** A glint runs along the underline; the word brightens when its jackpot is active.
- **Variants:** 24 animations: idle and activ (or anticipation for Grand) for each of the four jackpots, in three layouts by prefix (d_, m_, b_double_).
- **Motion:** Frames drawn by Spine's own 4.1 runtime (prep/skel.js): idles of 4 s, activ 0.67 s, Grand anticipation 1 s.
- **Construction:** 46 parts, 29 of them frame steps; a word is about 160x45 px. The amounts are written by the client with the numbers_jackpots font.
- **Notes:** In the game the plates read GRAND 1,000.00, MAJOR 100.00, MINOR 30.00, MINI 15.00 at a bet of 1.00 (seen on the base screen).
- **Skeleton (from the file):** Spine 4.1.24 · 26 bones · 24 slots · 34 region · animations: b_double_grand_anticipation (1 s), b_double_grand_idle (4 s), b_double_major_activ (0.67 s), b_double_major_idle (4 s), b_double_mini_activ (0.67 s), b_double_mini_idle (4 s), b_double_minor_activ (0.67 s), b_double_minor_idle (4 s), d_grand_anticipation (1 s), d_grand_idle (4 s), d_major_activ (0.67 s), d_major_idle (4 s), d_mini_activ (0.67 s), d_mini_idle (4 s), d_minor_activ (0.67 s), d_minor_idle (4 s), m_grand_anticipation (1 s), m_grand_idle (4 s), m_major_activ (0.67 s), m_major_idle (4 s), m_mini_activ (0.67 s), m_mini_idle (4 s), m_minor_activ (0.67 s), m_minor_idle (4 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 30% · saturation 58% · contrast 56% · warm 87% / cool 10% · brighter towards: bottom-right (10), bottom-left (9), bottom (5)
- **Palette (measured):** #070503 black 45%, #64461d brown 12%, #f6e99d light gold 11%, #cfb569 orange 7%, #ce6f12 orange 5%, #957f43 orange 4%

### Paytable pictures

`paytable-0` · atlas · 9 parts · largest 424×257 · sheet `sheets/paytable-0.webp`

- **Role:** The pictures of the game's own help pages: one per feature.
- **Subject:** Nine small scenes made of the game's pieces: the three pots with their coins and what each gives (a second board, a x2 on a coin, a fourth respin lamp); the bonus board with coins; two stacked boards; the Multi pot with x2, x3, x5 tags; the jackpots (Major 100x, Minor 30x, Mini 15x, and a 15x coin beside GRAND JACKPOT); the half wheel; three coloured coins; and a reel with coins flying to the pots.
- **Style:** The game's art at thumbnail size, with arrows.
- **Rendering:** Flattened composites with soft halos.
- **Colour:** Measured: dark magenta #350738 20%, gold #f0bf1e 18%, orange #d47812 10%, #741b3f 8%; saturation 0.81.
- **Lighting:** As the pieces.
- **Motion:** Still pictures.
- **Construction:** 9 pictures in one sheet, the largest 424x257 px.
- **Notes:** The help pages themselves could not be opened in the played session (the menu showed no entries in this browser), so the rules are not quoted here; the multiples above are what these pictures print.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 43% · saturation 80% · contrast 75% · warm 68% / cool 20% · brighter towards: top (2), bottom-left (2), bottom-right (1)
- **Palette (measured):** #350738 dark magenta 20%, #f0bf1e gold 18%, #d47812 orange 10%, #741b3f dark red 8%, #85380d brown 6%, #f6e173 gold 6%


## Typography

Embedded fonts and lettering.

### Big win numerals

`bitmapFont` · atlas · 1 parts · largest 512×512 · sheet `sheets/bitmapFont.webp`

- **Role:** The large amount under a big win (inference from its size, 154 px high, the largest set).
- **Subject:** The digits 0 to 9, comma, point and x.
- **Style:** A heavy slab-serif numeral with ball terminals, matching the logo's capitals.
- **Rendering:** Yellow-to-orange face, dark red stroke and extrusion, a light inner highlight.
- **Colour:** Measured: yellow #fedc0b 28%, dark red #960b04 20%, pale gold #f8df7a 14%, orange #f59a0a 12%.
- **Lighting:** Top highlight inside each digit.
- **Construction:** A bitmap font: one 512x512 px page with an XML table of 13 glyph boxes (the reader keeps the page whole).
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 60% · saturation 81% · contrast 86% · warm 100% / cool 0%
- **Palette (measured):** #fedc0b gold 28%, #960b04 red 20%, #f8df7a gold 14%, #f59a0a orange 12%, #f9eed4 light orange 7%, #470101 dark red 6%

### Jackpot numerals

`numbers_jackpots` · atlas · 1 parts · largest 128×256 · sheet `sheets/numbers_jackpots.webp`

- **Role:** The amounts on the four jackpot plates.
- **Subject:** Digits, comma and point.
- **Style:** The same numeral, small.
- **Rendering:** Cream-to-gold face with a dark brown stroke.
- **Colour:** Measured: dark brown #180301 36%, pale gold #fcec86 21%, cream #fffdea 14%, gold #f3c952 11%.
- **Construction:** A bitmap font page of 128x256 px with an XML table.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 48% · saturation 68% · contrast 99% · warm 100% / cool 0%
- **Palette (measured):** #180301 black 36%, #fcec86 light gold 21%, #fffdea light gold 14%, #f3c952 orange 11%, #c21707 red 7%, #6a1909 dark red 4%

### Multiplier numerals

`numbers_multiplier` · atlas · 1 parts · largest 512×64 · sheet `sheets/numbers_multiplier.webp`

- **Role:** The multiplier tags (x2, x3, x5) on coins.
- **Subject:** Digits and x.
- **Style:** The same numeral in red.
- **Rendering:** Red face with a yellow edge and an orange outer stroke.
- **Colour:** Measured: orange #e98b17 18%, red #cc0b01 18%, #5c4d31 15%, cream #f7f7cc 15%.
- **Construction:** A bitmap font page of 512x64 px with an XML table.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 53% · saturation 68% · contrast 81% · warm 100% / cool 0%
- **Palette (measured):** #e98b17 orange 18%, #cc0b01 red 18%, #5c4d31 brown 15%, #f7f7cc light gold 15%, #f9d41a gold 9%, #bcbb9b yellow 5%

### Coin value numerals

`numbers_symbols` · atlas · 1 parts · largest 256×256 · sheet `sheets/numbers_symbols.webp`

- **Role:** The cash value written on a bonus coin (5.00, 10.00 seen).
- **Subject:** Digits, comma and point.
- **Style:** The same numeral.
- **Rendering:** Cream-to-gold face, dark brown stroke.
- **Colour:** Measured: dark brown #1d0201 30%, pale gold #fcec85 23%, cream #fffeeb 15%, gold #f1c452 12%.
- **Construction:** A bitmap font page of 256x256 px with an XML table.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 52% · saturation 66% · contrast 98% · warm 100% / cool 0%
- **Palette (measured):** #1d0201 black 30%, #fcec85 light gold 23%, #fffeeb light gold 15%, #f1c452 orange 12%, #c21306 red 7%, #d8762c orange 5%

### Line win numerals

`numbers_win_lines` · atlas · 1 parts · largest 256×256 · sheet `sheets/numbers_win_lines.webp`

- **Role:** The amount of a line win over the reels (0.30 seen).
- **Subject:** Digits, comma, point and x.
- **Style:** The same numeral.
- **Rendering:** Yellow-to-orange face, dark red stroke and extrusion.
- **Colour:** Measured: yellow #fcde13 18%, dark red #5e0602 14%, #1c0101 12%, red #9b0f07 12%.
- **Construction:** A bitmap font page of 256x256 px with an XML table.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 49% · saturation 81% · contrast 90% · warm 100% / cool 0%
- **Palette (measured):** #fcde13 gold 18%, #5e0602 dark red 14%, #1c0101 black 12%, #9b0f07 red 12%, #f7d65a gold 11%, #f19a0b orange 9%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `textures`: 48 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Gilroy-Regular (?); My Font (Regular); Roboto (Black).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1151 components cut from 76 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
