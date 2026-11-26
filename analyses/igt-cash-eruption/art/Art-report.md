# Cash Eruption: art report

igt · run `2026-11-25-1658-igt-cash-eruption` · captured 2026-11-25

Source: the provider's free-play demo, https://platform.ka.rgsgames.com/skb/gateway?channel=INT&countrycode=AT&currencycode=FPY&language=en&nscode=OLGP&skincode=OLB1&softwareid=200-1551-002&uniqueid=0&locale=en&technology=HTML&presenttype=STD

**Extracted:** 621 named components from 67 textures in 67 atlases; 7 Spine skeletons; 32 frame sequences (362 frames); 4 fonts. Grouped into 67 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A classic fruit machine set in a furnace-red Mesoamerican temple: nine glossy gold-rimmed fruit, bell and seven symbols on a teal board, a realistic molten fireball as the feature symbol, and one painted character, a feathered fire priestess, as the wild.

**Style.** Three manners side by side. The regular symbols are stylised, glossy, toy-like objects with a gold rim and small engraved spirals. The fireball, the flames and the win effects are photographic fire. The wild is a realistic painted pin-up figure in an Aztec or Maya costume. The setting is 3D-rendered stone architecture; the bonus backdrop is a flatter, posterised painting of a volcano.

**Rendering.** Smooth airbrushed gradients with hard silhouettes, a gold outline, one white star glint and a drop shadow on every regular symbol. Frames and panels are flat fretwork ornament with no depth. Fire is soft and bright with sharp embers. Nothing has a drawn black outline except the flat black value digits on the fireballs.

**Colour.** Red, black and gold, with teal as the single counter-colour. Measured over the game's own art, the palette is led by near-black #170507, dark red #5c0d0f and red #9b130f and #ee2509, then orange #ed9e1c and gold #f7dd5b; saturation 80%, warm 87% against cool 9%. The reel cells are teal (#07998e, #036156) in the base game, so the board separates from the red hall (#a31d05); in the free spins the cells turn red (#9b0108) and the hall brighter red (#f52205). The bonus adds magenta (#7e072a and a 19% magenta share of hues). Each fruit owns one hue. The four prize tiers own one flat text colour each: red Grand, pink Major (#fb67b1), green Minor (#32fa64), cyan Mini (#31c6f7). The spin button is green.

**Lighting.** Fire is the light everywhere: the hall is lit from below and in front as if by firelight, the fireball and flames are self-lit, the wild is lit warm from the fire behind her. The regular symbols alone have a neutral studio light from the upper left with a star glint.

**Ambience.** Hot, enclosed and ceremonial in the base game; hotter in the free spins; vast and ominous in the bonus, under a red spiral sky. Over it sits the plain cheer of a classic fruit machine: the theme is a dressing on familiar symbols, not a story.

**Shape language.** Round, full, simple silhouettes for the symbols; rectangles and thin rails for every frame; the step-fret (a squared spiral) as the one ornament, repeated on frames, button rings, the coin, the ribbon ends, the cell pattern and even the watermelon seeds.

**Materials.** Glossy fruit skin, enamel and polished gold; rough cut stone; gold fretwork; glass-dome buttons; feathers, turquoise and gold jewellery on the wild; molten rock, flame and embers.

**Typography and lettering.** The logo is heavy slab-serif capitals with a yellow-to-red gradient, a flame texture and a dark red extrusion; FREE SPINS and WILD are drawn in the same bevelled manner. Everything else is live text in Oswald (Bold, Regular and Light are embedded): condensed capitals in yellow or peach for labels and figures, and flat tier colours for the prize meters. The values on the fireballs are a black condensed bitmap font with an orange edge, in two sizes.

**Motion.** No skeletons: the game's own art is animated as Flash-style timelines at 30 frames a second (the files call them view-builder animations) over still pictures, with short frame sequences for fire. A winning symbol gets an outline glow, a spark and a looping 30-frame flame; the fireball boils over 30 frames; the Free Spins volcano throws lava in 30 frames over three stills of rising brightness; the full-reel wild moves only her headdress (13 frames), lips, brows and earrings, with two 27-frame flames at her hands. On a win every symbol off the line is dimmed and the winning cells get a sparkling frame, with the line amount in a small black box. Anticipation is a six-frame burning outline around a reel or a cell. Coins on a win are a particle emitter over a six-frame coin. The four Spine 4.1.24 skeletons among the captured files belong to a promotional overlay of the demo's host (a vault and raccoon theme), not to this game.

**Variants and themes.** One hall in two brightnesses (base and free spins) and one separate bonus scene, which is also the loading picture. Reel backing in teal and red. Each symbol in three forms: a reel picture, a small paytable copy and a layered win version. In the free spins the three middle reels are linked and show one giant symbol, the same reel picture at three cells high. The fireball as a blank ball, with a live value, and with Mini, Minor or Major lettering. The wild as a one-cell bust and a three-cell standing figure. One button family (gold fret ring with a glass dome) in green, yellow, blue and red, each with lit and grey states.

**How it is built.** 621 named sprites on 67 textures, of which 56 units are the game's own art; 362 of the sprites are frames of 32 sequences. Sheets are in IGT's own view-builder format (a JSON of named sprites with frame rectangles beside each PNG, and a timeline file). Reel symbols are 558x500 pictures for a 261x238 cell. Backgrounds are single 1920x1080 JPEGs with no layers. The flame frames are repeated on each symbol sheet. Large light effects are small (the impact explosion is 96x96) and scaled up.

**Consistency.** Tight in colour and ornament, loose in manner. The red-gold-teal palette and the step-fret hold everything together, which lets three rendering styles (toy fruit, photographic fire, pin-up figure) sit on one board. The bonus backdrop is the one piece in a different hand: flat and posterised against the rendered hall.

**What to take from it.** (1) The top-ranked game of the report is visually modest: stills, flat frames and short frame loops, with no rigged character and no layered background. Its strength is clarity, not production volume. (2) One counter-colour does the layout work. A teal board in a red room, and a green spin button on a red and gold screen, separate play area and main control without size or decoration. (3) The feature symbol is told apart by manner, not by a frame or a badge: a realistic burning ball among glossy toy fruit. Black flat digits on it stay readable on the brightest object of the board. (4) Mode changes are cheap and clear: the free spins are the same hall and board pushed to red; the bonus swaps the backdrop and dims every symbol that is not a fireball. The free spins reuse the reel pictures at three times the size as giant symbols, which is why they are shipped at 558x500. (5) One ornament (the step-fret) repeated on every frame, button, coin and ribbon is enough to theme a set of otherwise generic classic symbols. (6) A full-height character is made to feel alive with four small moving pieces and two flame loops over a still painting. For AI-made art this is a reachable target: a strong still plus a few cut pieces, rather than a full rig. (7) Each win version is the reel picture plus three shared layers (outline glow, spark, flame loop). A symbol set built this way needs one good still per symbol and one shared effects kit.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm, medium contrast, hard-edged · brightness 31% · saturation 80% · contrast 52% · warm 87% / cool 9% · brighter towards: bottom (66), top (47), top-left (32)

Palette: #170507 black 23%, #5c0d0f dark red 14%, #9b130f red 13%, #ee2509 red 10%, #ed9e1c orange 8%, #f7dd5b gold 5%, #f9f8e5 light gold 2%, #8c0849 dark magenta 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 4 | 16% | 94% | 30% | 95% / 0% | #31040b black 38%, #a4190c red 23%, #f21d08 red 18% |
| Reel board | 6 | 37% | 80% | 25% | 81% / 18% | #a30208 red 24%, #560206 dark red 24%, #07998e cyan 9% |
| Symbols | 23 | 45% | 74% | 82% | 81% / 15% | #110604 black 15%, #661510 dark red 11%, #f0be17 gold 10% |
| Characters | 3 | 42% | 73% | 58% | 72% / 27% | #983916 brown 16%, #13100e black 14%, #eca448 orange 14% |
| Logo and title | 3 | 48% | 82% | 88% | 100% / 0% | #f38f19 orange 16%, #9b2d0e red 15%, #feec7b gold 12% |
| Win celebrations and banners | 4 | 26% | 57% | 43% | 89% / 5% | #060301 black 49%, #591c07 brown 12%, #9b7012 brown 8% |
| Effects | 3 | 21% | 48% | 51% | 100% / 0% | #070404 black 49%, #e06814 orange 16%, #c81508 red 12% |
| Game interface | 8 | 44% | 67% | 72% | 69% / 24% | #090806 black 18%, #9b5d12 brown 15%, #f4d124 gold 11% |
| Typography | 2 | 14% | 31% | 64% | 100% / 0% | #010100 black 73%, #fc9700 orange 17%, #5f3900 brown 6% |
| Provider interface (shared) | 11 | 48% | 48% | 75% | 49% / 46% | #3e3041 dark purple 25%, #ededee white 12%, #957e85 grey 7% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Volcano crater, loading background

`background` · atlas · 1 parts · largest 1920×1080 · sheet `sheets/background.webp`

- **Role:** The picture behind the logo while the game loads (it is in the splash folder).
- **Subject:** The same volcano crater under a red spiral sky as the bonus background.
- **Style:** Posterised digital painting.
- **Rendering:** Hard-edged flat tones with a magenta gradient; identical in drawing to bgd_bg.
- **Colour:** #330310 at 45%, #7e0828 at 40%, #d50d1c at 13%; red 82% and magenta 18% of the hues.
- **Lighting:** From the lava lake below.
- **Ambience:** A dark, threatening opening.
- **Materials:** Rock, lava, cloud.
- **Variants:** The same painting as bgd_bg, saved as a separate file.
- **Motion:** None.
- **Construction:** One JPEG of 1920x1080.
- **Notes:** The loading screen and the bonus share one painting.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 12% · saturation 94% · contrast 20% · warm 91% / cool 0%
- **Palette (measured):** #330310 black 45%, #7e0828 dark red 40%, #d50d1c red 13%

### Temple hall, base game background

`bgd` · atlas · 1 parts · largest 1920×1080 · sheet `sheets/bgd.webp`

- **Role:** The backdrop of the base game, behind the reel board.
- **Subject:** The inside of a stone temple seen straight on: a flat back wall of large blocks, stepped stone piers left and right with carved bands and round rosettes, a ledge, and a stair with scroll-pattern risers running across the bottom.
- **Style:** Realistic 3D-rendered architecture in a Mesoamerican manner, symmetric and stage-like.
- **Rendering:** A clean render with a gritty stone texture overlay, sharp block edges and a strong vignette to black at the top and bottom; almost monochrome.
- **Colour:** Red and black: #a31d05 at 53%, #250603 at 28%, #6c1206, with a little orange on the ledge (#e87313). Measured dark (brightness 0.17) and fully warm.
- **Lighting:** As if lit by firelight from below and in front: the ledge and stair tops are brightest, the ceiling falls to black. The torches seen in the game are not in this picture.
- **Ambience:** Hot, enclosed, ceremonial; a furnace-red room that leaves the centre empty for the reels.
- **Materials:** Rough cut stone with carved fret and rosette ornament.
- **Variants:** bgd_fs is the same picture pushed brighter and redder for the free spins; bgd_bg is a different scene for the bonus.
- **Motion:** None in the file. In the game two torches with live flames stand at the sides (seen in the screens; their frames are not among the captured files, so they are probably drawn by the client's particle effects: inference).
- **Construction:** One JPEG of 1920x1080.
- **Notes:** The wall is deliberately blank where the reel board sits, and the detail is pushed to the edges: the background is designed around the board.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 17% · saturation 95% · contrast 34% · warm 100% / cool 0% · brighter towards: bottom-right (1)
- **Palette (measured):** #a31d05 red 53%, #250603 black 28%, #6c1206 dark red 16%, #e87313 orange 3%

### Volcano crater under a spiral sky, bonus background

`bgd_bg` · atlas · 1 parts · largest 1920×1080 · sheet `sheets/bgd_bg.webp`

- **Role:** The backdrop of the fireball bonus (named bg; inference that bg stands for the bonus game).
- **Subject:** A dark volcano seen from above its rim, with a lake of yellow-orange lava in the crater and red lava lines down its slopes, under a huge red spiral of cloud; magenta haze at the horizon.
- **Style:** Digital painting with a posterised, graphic look: flat bands of colour rather than a render.
- **Rendering:** Hard-edged cloud and rock shapes in a few flat tones, a soft magenta gradient in the middle distance, and a smooth swirl in the lava.
- **Colour:** Black-wine and dark red (#2f030f at 53%, #7e072a at 32%) with pure red (#e30b16) and a magenta share (hues: red 81%, magenta 19%); the lava is the only yellow.
- **Lighting:** Lit from the lava lake: the crater rim and the underside of the clouds catch red, the rest stays in shadow.
- **Ambience:** Ominous and vast; the outside world after the closed temple room.
- **Materials:** Rock, lava, storm cloud, haze.
- **Variants:** background (the loading picture) is the same painting.
- **Motion:** None in the file.
- **Construction:** One JPEG of 1920x1080.
- **Notes:** The bonus changes the place, the palette (magenta enters) and the manner (painted, not rendered) at once: the strongest break in the game's look.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 11% · saturation 93% · contrast 22% · warm 90% / cool 0%
- **Palette (measured):** #2f030f black 53%, #7e072a dark red 32%, #e30b16 red 11%, #b50814 red 3%

### Temple hall, free spins background

`bgd_fs` · atlas · 1 parts · largest 1920×1080 · sheet `sheets/bgd_fs.webp`

- **Role:** The backdrop of the free spins (named fs).
- **Subject:** The same temple hall as the base game.
- **Style:** The same 3D-rendered Mesoamerican hall.
- **Rendering:** The same render with brightness and saturation raised; block joints and texture are still visible.
- **Colour:** Bright red: #f52205 at 56%, with #400904, #982409 and orange on the ledge (#f69a14, #d46011). Brightness 0.26 against 0.17 for the base game.
- **Lighting:** The same set-up, hotter: the wall glows as if the room had caught fire.
- **Ambience:** The same room at a higher temperature: the mode change is told by heat alone.
- **Materials:** Stone, as in the base game.
- **Variants:** A recolour of bgd.
- **Motion:** None in the file.
- **Construction:** One JPEG of 1920x1080.
- **Notes:** A feature mode made from one colour adjustment of the base background: no new painting.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 26% · saturation 96% · contrast 45% · warm 100% / cool 0% · brighter towards: bottom (1)
- **Palette (measured):** #f52205 red 56%, #400904 dark red 25%, #982409 red 10%, #f69a14 orange 5%, #d46011 orange 3%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel backing strips

`reel_background_spritesheet` · atlas · 5 parts · largest 209×571 · sheet `sheets/reel_background_spritesheet.webp`

- **Role:** The colour behind each reel: teal in the base game, red in the free spins.
- **Subject:** Tall plain strips with a vertical gradient, two teal and two red.
- **Style:** Flat graphic ground.
- **Rendering:** A smooth gradient from light at the top to dark at the bottom, with a soft dark inner edge at the sides.
- **Colour:** Teal (#07998e, #036156, #013831) for the base game and red (#9b0108, #4d0106) for the free spins.
- **Lighting:** Lighter at the top, as if lit from above.
- **Ambience:** The teal is the one cool surface in a red room, so the board separates from the background at once.
- **Materials:** None; a flat colour field (the fret pattern seen in play is part of each symbol's picture).
- **Variants:** Two teal and two red strips of 209x571 (reel_back_1 and 2, reel_back_free_1 and 2).
- **Motion:** None.
- **Construction:** 5 sprites, one of them an empty placeholder.
- **Notes:** Complementary contrast does the work of a frame: teal board, red world. In the free spins the board turns red too and the contrast is given up for heat.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 23% · saturation 98% · contrast 25% · warm 50% / cool 50% · brighter towards: top (3), top-right (1)
- **Palette (measured):** #9b0108 red 29%, #07998e cyan 24%, #4d0106 dark red 21%, #036156 dark cyan 17%, #013831 black 9%

### Aspect frame placeholder

`aspect_frame_spritesheet` · atlas · 1 parts · largest 10×10 · sheet `sheets/aspect_frame_spritesheet.webp`

- **Role:** An empty placeholder the layout uses (its only sprite is named empty).
- **Subject:** Nothing visible: a 10x10 transparent square.
- **Style:** None.
- **Rendering:** None.
- **Colour:** None measured.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** None.
- **Motion:** None.
- **Construction:** One empty sprite.
- **Notes:** Listed because the game ships it; it holds no art.

### Reel frame and free spins panel

`reel_foreground_spritesheet` · atlas · 2 parts · largest 1146×646 · sheet `sheets/reel_foreground_spritesheet.webp`

- **Role:** The gold frame around the five reels with its four dividers, and a large red panel for the free spins.
- **Subject:** A thin orange-gold rectangular frame with four vertical dividers, with a fine pattern along its rails; and a plain dark red gradient panel with a thin gold edge.
- **Style:** Flat ornamental frame, thin and restrained.
- **Rendering:** Thin rails with a small repeating fret pattern, hard-edged.
- **Colour:** Red panel (#a40308, #560307) and orange-brown rails (#b96212, #7c4710).
- **Lighting:** Flat, with the panel lighter at the top.
- **Ambience:** Quiet: the frame is kept thin so the symbols carry the board.
- **Materials:** Gold fretwork, as a flat ornament.
- **Variants:** reel_fore (1146x646) and reel_back_free_2 (650x569): the wide red panel is the backing of the three middle reels when they are linked into one giant symbol in the free spins (seen in the screens).
- **Motion:** None.
- **Construction:** 2 sprites.
- **Notes:** The board is a thin frame over flat colour; no carved stone surround, unlike the heavy background.
- **Measured:** dark, vivid, warm, low contrast · brightness 15% · saturation 96% · contrast 18% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #a40308 red 43%, #560307 dark red 41%, #b96212 orange 10%, #7c4710 brown 3%, #030304 black 3%

### Win frame, greyed

`WIN_FRAME_DISABLED_VB_spritesheet` · atlas · 1 parts · largest 172×148 · sheet `sheets/WIN_FRAME_DISABLED_VB_spritesheet.webp`

- **Role:** The frame around cells that belong to another winning line than the one being shown (seen in the screens of a win through the expanded wild).
- **Subject:** A rounded grey rectangle outline with a soft edge.
- **Style:** Light effect, graphic.
- **Rendering:** Soft-edged grey line.
- **Colour:** Grey only (#acacac measured at 100%).
- **Lighting:** None.
- **Ambience:** Neutral.
- **Materials:** None.
- **Variants:** The grey twin of the yellow win frame.
- **Motion:** None.
- **Construction:** One sprite of 172x148.
- **Notes:** A grey copy rather than a tint in code.
- **Measured:** bright, muted, neutral, low contrast · brightness 67% · saturation 0% · contrast 1% · warm 0% / cool 0%
- **Palette (measured):** #acacac grey 100%

### Win frame for a paying cell

`WIN_FRAME_VB_spritesheet` · atlas · 5 parts · largest 248×218 · sheet `sheets/WIN_FRAME_VB_spritesheet.webp`

- **Role:** The frame drawn around each symbol of a winning line.
- **Subject:** A rounded yellow-orange glowing rectangle, three frames of fine white-green sparkles running around a rectangle, and a short white streak.
- **Style:** Light effect, graphic.
- **Rendering:** A soft-edged glowing line for the frame; the sparkles are tiny sharp dots and stars; measured soft-edge share 80%.
- **Colour:** Yellow and orange (#f5f139, #e09f2f) with white and pale green sparkles (#f6f8f1, #ceddb4, #94ae7f).
- **Lighting:** Emissive.
- **Ambience:** A light, glittering yes.
- **Materials:** Light only.
- **Variants:** One frame; a grey disabled copy is its own sheet.
- **Motion:** winframe_blick, 3 frames at 248x218: sparkles travel around the frame; the white streak sweeps along it (inference from its shape).
- **Construction:** 5 sprites; the frame is 172x148.
- **Notes:** The sparkles are pale green, not gold: a small cool accent that keeps the frame from disappearing against gold symbols.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 74% · saturation 44% · contrast 49% · warm 56% / cool 22%
- **Palette (measured):** #f6f8f1 light green 24%, #e09f2f orange 17%, #94ae7f green 14%, #f5f139 gold 12%, #ceddb4 light green 9%, #4d7533 green 7%

### Burning frames: anticipation on a reel and on a cell

`WIN_TENSION_FRAME_VB_spritesheet` · atlas · 12 parts · largest 350×850 · sheet `sheets/WIN_TENSION_FRAME_VB_spritesheet.webp`

- **Role:** The frame of fire drawn around a whole reel, and around one cell, while a feature may still land (named tension; fs in the cell frames suggests the free spins symbol: inference).
- **Subject:** A tall rectangle and a square, each drawn as a line of white-hot fire with orange sparks, in six frames each.
- **Style:** Fire effect, photographic.
- **Rendering:** A bright core line with soft orange bloom and small sparks; measured soft-edge share 67%.
- **Colour:** Orange and pale gold (#f3a868, #fdfbe5, #fbe3a3).
- **Lighting:** Emissive.
- **Ambience:** Suspense as heat: the reel that might pay is on fire.
- **Materials:** Fire.
- **Variants:** A reel-high frame (350x850) and a cell frame (350x354).
- **Motion:** Two loops of six frames each: the fire line flickers and sparks shift around the rectangle.
- **Construction:** 12 sprites.
- **Notes:** Six frames are enough for a convincing burning outline when the shape is thin and bright.
- **Measured:** bright, saturated, warm, medium contrast, glow or soft effect, strong highlights · brightness 82% · saturation 38% · contrast 35% · warm 100% / cool 0%
- **Palette (measured):** #f3a868 orange 44%, #fdfbe5 light gold 29%, #fbe3a3 light orange 24%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Gold bell (paytable)

`bell` · atlas · 1 parts · largest 157×143 · sheet `sheets/bell.webp`

- **Role:** Mid-paying symbol, shown in the paytable.
- **Subject:** A tilted golden hand bell seen from below, with three raised bands, a red-orange inside and a round clapper.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Gold and yellow (#f9c50d, #fae160) with a dark red interior (#6b0d07) and brown-orange shading (#a6450f, #da7710); warm throughout.
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Polished gold with engraved bands and a glossy red enamel inside.
- **Variants:** One design; the same art appears at reel size and as a layered win version.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The paytable copy is small and already baked onto the cell ground, so it is a reference for the look, not a working part.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 62% · saturation 64% · contrast 91% · warm 99% / cool 0% · brighter towards: top-left (1)
- **Palette (measured):** #f9c50d gold 17%, #fcf8eb light orange 15%, #6b0d07 dark red 12%, #fae160 gold 12%, #a6450f brown 9%, #da7710 orange 7%

### Blue seven (paytable)

`blue_7` · atlas · 1 parts · largest 157×143 · sheet `sheets/blue_7.webp`

- **Role:** High-paying symbol, shown in the paytable.
- **Subject:** A bold slab numeral 7 in blue with a gold bevelled rim and a fine scale texture on its face.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Cyan to deep blue (#10adf6, #256fd5, #1b27c0, #031362) inside a brown-gold rim (#be6d02); the only cool high symbol.
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Blue enamel or glass with a fine scale pattern, in a polished gold bezel.
- **Variants:** Pairs with the red Lucky 7: the same numeral in another colour, without the ribbon.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The paytable copy is small and already baked onto the cell ground, so it is a reference for the look, not a working part.
- **Measured:** mid-tone, vivid, cool, high contrast · brightness 42% · saturation 75% · contrast 92% · warm 24% / cool 76% · brighter towards: top (1)
- **Palette (measured):** #10adf6 cyan 18%, #0f0810 black 14%, #1b27c0 blue 12%, #be6d02 brown 9%, #256fd5 blue 9%, #f4f9fa light cyan 6%

### Cherries (paytable)

`cherry` · atlas · 1 parts · largest 157×143 · sheet `sheets/cherry.webp`

- **Role:** Low-paying fruit symbol, shown in the paytable.
- **Subject:** Two crimson cherries on gold-edged green stems with one leaf.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Crimson and red (#940521, #e10b32) with green (#267917, #56bb17) and a gold rim (#f5be0e, #b86103).
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Glossy candy-like fruit skin, waxy leaf, gold wire rim.
- **Variants:** One design; the same art appears at reel size and as a layered win version.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The paytable copy is small and already baked onto the cell ground, so it is a reference for the look, not a working part.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 40% · saturation 74% · contrast 88% · warm 68% / cool 12% · brighter towards: top-left (1)
- **Palette (measured):** #940521 red 15%, #267917 dark green 13%, #0c0d06 black 10%, #fdf5f1 light orange 9%, #b86103 brown 8%, #e10b32 red 5%

### Fireball (paytable)

`fireball` · atlas · 1 parts · largest 157×143 · sheet `sheets/fireball.webp`

- **Role:** Feature symbol: six or more start the bonus (stated on the intro panel).
- **Subject:** A glowing molten sphere in a black square cell with a thin burning border, without a label.
- **Style:** A photographic-looking molten sphere, close to a rendered sun or lava planet, set in a square black cell with a thin burning border; realistic where the fruit symbols are stylised.
- **Rendering:** Sharp mottled surface of white-yellow hot patches and dark red-black crust, with a soft orange halo around the sphere and a flame-edged square frame; flat label lettering on top.
- **Colour:** Black (#170402) around light gold, orange and red (#fef487, #f58d3c, #ed411d) with dark red crust (#6b1407, #af2e0f).
- **Lighting:** Self-lit: the sphere is the light source, brightest in the centre and upper left, with the black ground around it making it read as emissive.
- **Ambience:** Heat and danger: the one symbol that looks hot rather than lucky, which marks it as the feature symbol.
- **Materials:** Molten rock and fire with a cracked dark crust; flat coloured lettering with a dark outline.
- **Variants:** The blank ball; the four labelled copies (value, Mini, Minor, Major) are the same picture with text on it.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the fireball in its black cell; the label or value is baked into this paytable copy, while in the game the value is drawn as live text over the ball (the black bitmap digits of blackFont).
- **Notes:** The contrast in manner with the fruit is the point: a realistic hot object among glossy toys reads at once as special.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 46% · saturation 73% · contrast 98% · warm 100% / cool 0%
- **Palette (measured):** #170402 black 20%, #fef487 light gold 17%, #6b1407 dark red 14%, #f58d3c orange 14%, #ed411d red 13%, #af2e0f red 7%

### Fireball labelled MAJOR (paytable)

`fireball_major` · atlas · 1 parts · largest 175×152 · sheet `sheets/fireball_major.webp`

- **Role:** Paytable picture of a fireball that awards the Major prize.
- **Subject:** The molten sphere with MAJOR across it in pink condensed capitals.
- **Style:** A photographic-looking molten sphere, close to a rendered sun or lava planet, set in a square black cell with a thin burning border; realistic where the fruit symbols are stylised.
- **Rendering:** Sharp mottled surface of white-yellow hot patches and dark red-black crust, with a soft orange halo around the sphere and a flame-edged square frame; flat label lettering on top.
- **Colour:** The fireball's black, gold and reds (#180706, #f9e77f, #a93512) with pink-magenta lettering (#fb67b1).
- **Lighting:** Self-lit: the sphere is the light source, brightest in the centre and upper left, with the black ground around it making it read as emissive.
- **Ambience:** Heat and danger: the one symbol that looks hot rather than lucky, which marks it as the feature symbol.
- **Materials:** Molten rock and fire with a cracked dark crust; flat coloured lettering with a dark outline.
- **Variants:** One of three prize labels; pink is also the Major colour on the meters above the reels.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the fireball in its black cell; the label or value is baked into this paytable copy, while in the game the value is drawn as live text over the ball (the black bitmap digits of blackFont).
- **Notes:** Each prize tier owns one flat colour (pink Major, green Minor, cyan Mini, red Grand on the meters), used for its label and its meter.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 45% · saturation 69% · contrast 93% · warm 93% / cool 1%
- **Palette (measured):** #180706 black 20%, #f9e77f gold 17%, #e99f49 orange 13%, #a93512 red 12%, #5e1308 dark red 12%, #fb67b1 magenta 8%

### Fireball labelled MINI (paytable)

`fireball_mini` · atlas · 1 parts · largest 175×152 · sheet `sheets/fireball_mini.webp`

- **Role:** Paytable picture of a fireball that awards the Mini prize.
- **Subject:** The molten sphere with MINI across it in cyan condensed capitals.
- **Style:** A photographic-looking molten sphere, close to a rendered sun or lava planet, set in a square black cell with a thin burning border; realistic where the fruit symbols are stylised.
- **Rendering:** Sharp mottled surface of white-yellow hot patches and dark red-black crust, with a soft orange halo around the sphere and a flame-edged square frame; flat label lettering on top.
- **Colour:** The fireball's black, gold and reds (#170907, #faed91, #cf461b) with cyan lettering (#31c6f7).
- **Lighting:** Self-lit: the sphere is the light source, brightest in the centre and upper left, with the black ground around it making it read as emissive.
- **Ambience:** Heat and danger: the one symbol that looks hot rather than lucky, which marks it as the feature symbol.
- **Materials:** Molten rock and fire with a cracked dark crust; flat coloured lettering with a dark outline.
- **Variants:** One of three prize labels; cyan is also the Mini colour on the meters.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the fireball in its black cell; the label or value is baked into this paytable copy, while in the game the value is drawn as live text over the ball (the black bitmap digits of blackFont).
- **Notes:** The cool cyan label on the hot ball is the strongest colour contrast in the symbol set.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 46% · saturation 71% · contrast 92% · warm 91% / cool 9%
- **Palette (measured):** #170907 black 20%, #faed91 light gold 17%, #5d1207 dark red 11%, #982f10 red 9%, #f2bf58 orange 9%, #cf461b red 9%

### Fireball labelled MINOR (paytable)

`fireball_minor` · atlas · 1 parts · largest 175×152 · sheet `sheets/fireball_minor.webp`

- **Role:** Paytable picture of a fireball that awards the Minor prize.
- **Subject:** The molten sphere with MINOR across it in green condensed capitals.
- **Style:** A photographic-looking molten sphere, close to a rendered sun or lava planet, set in a square black cell with a thin burning border; realistic where the fruit symbols are stylised.
- **Rendering:** Sharp mottled surface of white-yellow hot patches and dark red-black crust, with a soft orange halo around the sphere and a flame-edged square frame; flat label lettering on top.
- **Colour:** The fireball's black, gold and reds (#170906, #f9e77f, #9a2f0f) with bright green lettering (#32fa64).
- **Lighting:** Self-lit: the sphere is the light source, brightest in the centre and upper left, with the black ground around it making it read as emissive.
- **Ambience:** Heat and danger: the one symbol that looks hot rather than lucky, which marks it as the feature symbol.
- **Materials:** Molten rock and fire with a cracked dark crust; flat coloured lettering with a dark outline.
- **Variants:** One of three prize labels; green is also the Minor colour on the meters.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the fireball in its black cell; the label or value is baked into this paytable copy, while in the game the value is drawn as live text over the ball (the black bitmap digits of blackFont).
- **Notes:** Same construction as the Major and Mini copies; only the word and its colour change.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 47% · saturation 71% · contrast 92% · warm 86% / cool 8%
- **Palette (measured):** #170906 black 20%, #f9e77f gold 16%, #5b1207 dark red 10%, #9a2f0f red 10%, #edae4d orange 9%, #32fa64 green 8%

### Fireball with a credit value (paytable)

`fireball_value` · atlas · 1 parts · largest 175×152 · sheet `sheets/fireball_value.webp`

- **Role:** Paytable picture of a fireball that carries a cash value.
- **Subject:** The molten sphere with the figure 30.00 across it in black condensed digits with an orange edge.
- **Style:** A photographic-looking molten sphere, close to a rendered sun or lava planet, set in a square black cell with a thin burning border; realistic where the fruit symbols are stylised.
- **Rendering:** Sharp mottled surface of white-yellow hot patches and dark red-black crust, with a soft orange halo around the sphere and a flame-edged square frame; flat label lettering on top.
- **Colour:** The fireball's black, gold and reds (#120604, #f9e67f, #97330f) with black digits edged in orange (#f0b613).
- **Lighting:** Self-lit: the sphere is the light source, brightest in the centre and upper left, with the black ground around it making it read as emissive.
- **Ambience:** Heat and danger: the one symbol that looks hot rather than lucky, which marks it as the feature symbol.
- **Materials:** Molten rock and fire with a cracked dark crust; flat coloured lettering with a dark outline.
- **Variants:** The value copy; in play the figure changes per ball.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the fireball in its black cell; the label or value is baked into this paytable copy, while in the game the value is drawn as live text over the ball (the black bitmap digits of blackFont).
- **Notes:** Black digits on the brightest object on the board stay readable where a light figure would not: the reason for the black bitmap font.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 45% · saturation 69% · contrast 93% · warm 100% / cool 0%
- **Palette (measured):** #120604 black 23%, #f9e67f gold 17%, #e8a250 orange 11%, #5a1305 dark red 11%, #97330f brown 10%, #f0b613 orange 6%

### Blue grapes (paytable)

`grapes` · atlas · 1 parts · largest 157×143 · sheet `sheets/grapes.webp`

- **Role:** Low-paying fruit symbol, shown in the paytable.
- **Subject:** A bunch of six round blue grapes, each with a spiral engraved on it, with a curled gold stem and a green leaf.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Deep and bright blue (#1722af, #2950f2, #0a0a71) with a green leaf (#189400) and brown-gold stem (#b86202, #5c3304).
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Glossy glass-like berries, gold stem, waxy leaf.
- **Variants:** One design; the same art appears at reel size and as a layered win version.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The paytable copy is small and already baked onto the cell ground, so it is a reference for the look, not a working part.
- **Measured:** mid-tone, vivid, cool, high contrast · brightness 37% · saturation 67% · contrast 94% · warm 21% / cool 73% · brighter towards: top-left (1)
- **Palette (measured):** #1722af blue 19%, #060b02 black 15%, #f8f7f2 light yellow 7%, #2950f2 blue 6%, #5c3304 brown 5%, #b86202 brown 4%

### Lemon (paytable)

`lemon` · atlas · 1 parts · largest 157×143 · sheet `sheets/lemon.webp`

- **Role:** Low-paying fruit symbol, shown in the paytable.
- **Subject:** A whole lemon lying on its side with engraved spirals on the peel.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Almost one colour: yellow-gold (#eed008 at 54%, #faf552, #c49b08) with a pale highlight (#f7f49a).
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Smooth glossy peel with faint engraved ornament and a gold rim.
- **Variants:** One design; the same art appears at reel size and as a layered win version.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The paytable copy is small and already baked onto the cell ground, so it is a reference for the look, not a working part.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 77% · saturation 79% · contrast 46% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #eed008 gold 54%, #faf552 gold 16%, #c49b08 gold 8%, #f7f49a light gold 7%, #fafcf0 light gold 6%, #0a0908 black 4%

### Watermelon half (paytable)

`melon` · atlas · 1 parts · largest 157×143 · sheet `sheets/melon.webp`

- **Role:** Low-paying fruit symbol, shown in the paytable.
- **Subject:** A halved watermelon facing the viewer: pink-red flesh with step-fret shaped seeds, white rind line and striped green skin.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Pink-red flesh (#ec194d, #f75282) with cream rind (#fefaef) and dark green skin (#116203).
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Wet glossy flesh, matte rind, gold rim.
- **Variants:** One design; the same art appears at reel size and as a layered win version.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The seeds are drawn as small step-fret marks, the same motif as the cell pattern: a classic fruit quietly tied to the temple setting.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 43% · saturation 68% · contrast 99% · warm 77% / cool 11% · brighter towards: top-left (1)
- **Palette (measured):** #ec194d red 34%, #fefaef light orange 13%, #080f03 black 12%, #116203 dark green 9%, #f75282 red 7%, #f7e2b3 light orange 4%

### Orange (paytable)

`orange` · atlas · 1 parts · largest 157×143 · sheet `sheets/orange.webp`

- **Role:** Low-paying fruit symbol, shown in the paytable.
- **Subject:** A whole orange with a small green calyx and engraved spirals low on the peel.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Orange in two steps (#fbad32, #f36220) with a pale highlight (#fbd981).
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Smooth glossy peel with engraved spirals and a gold rim.
- **Variants:** One design; the same art appears at reel size and as a layered win version.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The paytable copy is small and already baked onto the cell ground, so it is a reference for the look, not a working part.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 58% · saturation 73% · contrast 93% · warm 100% / cool 0% · brighter towards: top-left (1)
- **Palette (measured):** #fbad32 orange 44%, #f36220 orange 28%, #040303 black 9%, #fefbec light gold 6%, #fbd981 orange 4%

### Plum (paytable)

`plum` · atlas · 1 parts · largest 157×143 · sheet `sheets/plum.webp`

- **Role:** Low-paying fruit symbol, shown in the paytable.
- **Subject:** An oval purple plum with a short curled gold stem and a row of engraved spirals along its lower edge.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Purple and violet (#5a0789, #752dc5, #a476f1) with a brown-gold stem (#ae5607); cool.
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Glossy skin with a pale bloom highlight and gold stem.
- **Variants:** One design; the same art appears at reel size and as a layered win version.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The paytable copy is small and already baked onto the cell ground, so it is a reference for the look, not a working part.
- **Measured:** mid-tone, vivid, cool, high contrast · brightness 33% · saturation 70% · contrast 88% · warm 13% / cool 86% · brighter towards: top-left (1)
- **Palette (measured):** #5a0789 dark purple 34%, #752dc5 purple 21%, #a476f1 purple 14%, #060504 black 9%, #f7f1f3 light red 6%, #ae5607 brown 4%

### Red Lucky 7 (paytable)

`red_7` · atlas · 1 parts · largest 157×143 · sheet `sheets/red_7.webp`

- **Role:** Top-paying regular symbol; three of them beside four wild reels make the 1000x pattern the intro advertises.
- **Subject:** A bold slab numeral 7 in red with a gold rim, crossed by a red ribbon reading LUCKY in gold letters with step-fret scroll ends.
- **Style:** Glossy, rounded casino-classic object in a 3D-look painted manner, with a thin gold rim around the whole silhouette and small engraved spiral and step-fret ornaments on its surface.
- **Rendering:** Smooth airbrushed gradients with a hard clean silhouette, a gold outline, a white four-point sparkle on the highlight and a soft dark drop shadow to the lower right; no line drawing inside.
- **Colour:** Red (#bf0807, #f91512, #f84e34) and dark red (#5f0c07) with brown-gold trim (#bb6b02) and yellow lettering (#fef341).
- **Lighting:** Lit from the upper left, with one white star glint on the brightest point and a dark shadow cast to the lower right.
- **Ambience:** Bright, lucky, classic fruit-machine cheer, set against the dark teal cell with its faint step-fret pattern.
- **Materials:** Red enamel with a scale texture, gold bezel, satin ribbon with gold letters.
- **Variants:** Pairs with the blue 7; the ribbon is what sets the top symbol apart.
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture of the symbol on its reel-cell ground, shipped for the paytable page; the reel version of the same art is in reels_graphics_spritesheet and the layered win version in the WIN_SYMBOLS_MERGED sheets.
- **Notes:** The ribbon's scroll ends repeat the step-fret motif of the frame and the cell pattern.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 34% · saturation 81% · contrast 91% · warm 100% / cool 0% · brighter towards: left (1)
- **Palette (measured):** #bf0807 red 27%, #180307 black 15%, #5f0c07 dark red 9%, #f91512 red 8%, #bb6b02 brown 8%, #f84e34 red 8%

### Volcano, Free Spins symbol (paytable)

`volcano` · atlas · 1 parts · largest 156×140 · sheet `sheets/volcano.webp`

- **Role:** Scatter-type symbol: three or more start the free spins (stated on the intro panel).
- **Subject:** An erupting dark volcano with lava running down its ridges under a magenta-purple sky, in a red and yellow dashed square frame, with FREE SPINS lettered across the lower half.
- **Style:** A small painted scene, more illustrative and flatter than the fruit symbols, with heavy display lettering laid over it.
- **Rendering:** Flat shapes with simple gradients for the mountain and sky, bright lava streaks, and bevelled yellow-to-orange letters with a dark red outline.
- **Colour:** Black and dark wine (#0c0302, #550c2a), magenta (#940e4d), with orange and yellow for lava and letters (#f5a00d, #fce856, #fef003).
- **Lighting:** Lit by the eruption at the top centre: a yellow-white burst behind the crater, the slopes dark.
- **Ambience:** The game's title made literal: an eruption about to pay.
- **Materials:** Dark rock, glowing lava, a smoky coloured sky; enamel-like lettering.
- **Variants:** One design; it appears at reel size and as a layered win version (WIN_SYMBOLS_MERGED_VB_4).
- **Motion:** None in this file: a still picture for the paytable.
- **Construction:** One flat picture with the frame and lettering baked in.
- **Notes:** It is the only symbol that carries words in the base set besides the wild, and the only one with a magenta sky, the colour of the bonus backdrop.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 33% · saturation 73% · contrast 93% · warm 86% / cool 0%
- **Palette (measured):** #0c0302 black 25%, #550c2a dark red 22%, #f5a00d orange 10%, #fce856 gold 8%, #940e4d magenta 6%, #871905 dark red 4%

### Fireball cell mask, second copy

`big_fireball_labels_spritesheet` · atlas · 1 parts · largest 172×149 · sheet `sheets/big_fireball_labels_spritesheet.webp`

- **Role:** The same corner mask for the larger fireball of the bonus (inference from the name).
- **Subject:** A black square with a soft-edged round opening.
- **Style:** A technical mask, not a picture.
- **Rendering:** Solid black with a feathered inner edge.
- **Colour:** Black only (#000000 measured at 100%).
- **Lighting:** None.
- **Ambience:** None of its own.
- **Materials:** None.
- **Variants:** Twin of fireball_labels_spritesheet at 172x149.
- **Motion:** None.
- **Construction:** One sprite on its own sheet.
- **Notes:** Kept as its own unit because the game ships it as its own file.
- **Measured:** dark, muted, neutral, low contrast · brightness 0% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #000000 black 100%

### Fireball cell mask

`fireball_labels_spritesheet` · atlas · 1 parts · largest 172×157 · sheet `sheets/fireball_labels_spritesheet.webp`

- **Role:** A black mask with a rounded opening, laid over a fireball's cell where its label is shown (inference from its name, frameMaskMC, and its shape).
- **Subject:** A black square with a soft-edged round opening that leaves the four corners covered.
- **Style:** A technical mask, not a picture.
- **Rendering:** Solid black with a feathered inner edge.
- **Colour:** Black only (#000000 measured at 100%).
- **Lighting:** None.
- **Ambience:** None of its own; it darkens the corners so the ball sits in a black cell.
- **Materials:** None.
- **Variants:** A second, near-identical copy is big_fireball_labels_spritesheet.
- **Motion:** None.
- **Construction:** One sprite of 172x157 on its own sheet.
- **Notes:** It shows how the fireball's black cell is made: the ball is drawn, then the corners are masked to black.
- **Measured:** dark, muted, neutral, low contrast · brightness 0% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #000000 black 100%

### Reel symbols at reel size

`reels_graphics_spritesheet` · atlas · 12 parts · largest 578×500 · sheet `sheets/reels_graphics_spritesheet.webp`

- **Role:** The twelve symbols as the reels draw them: fireball, bell, blue 7, cherries, Free Spins volcano, grapes, lemon, watermelon, orange, plum, red Lucky 7 and the wild.
- **Subject:** Each symbol on its own cell: nine glossy gold-rimmed objects on a dark teal ground with a faint step-fret pattern, the fireball on black, the volcano in its dashed frame, and the wild as a bust of the feathered woman over the word WILD.
- **Style:** Three manners in one set: stylised glossy fruit, bell and sevens; a realistic molten ball; and an illustrated woman in a pin-up manner for the wild.
- **Rendering:** Fruit and sevens are smooth airbrushed forms with a gold outline, a star glint and a drop shadow; the wild is painted with skin tones, feather strokes and jewellery detail; the fireball is sharp and mottled.
- **Colour:** Gold, brown and dark red lead (#f1c016, #ab4e0f, #581218, #f8e987) over black (#110806), with one saturated body colour per fruit (purple #5d0b89 for the plum among them).
- **Lighting:** Top-left key light with a star glint on the fruit; the fireball and the fire behind the wild are self-lit.
- **Ambience:** A classic fruit machine dressed for a fire temple: familiar symbols first, theme second.
- **Materials:** Glossy fruit skin, gold and enamel, feathers, turquoise and gold jewellery, molten rock.
- **Variants:** Twelve symbols, one picture each. The wild also exists as a three-cell expanded figure, and each symbol has a layered win version in the WIN_ sheets.
- **Motion:** Stills. On the reels they scroll as they are; no blurred copies are shipped in this sheet.
- **Construction:** Twelve pictures of 558x500 (the fireball 578x500, the wild 450x467) on one sheet, far larger than the 261x238 cell the reel configuration states: they are scaled down on the reels, and in the free spins the same pictures fill the three linked middle reels as one giant symbol (seen in the screens).
- **Notes:** Each low symbol is one object in one colour, so the nine regular symbols are told apart by hue alone at a glance. The cell ground is part of each picture.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 43% · saturation 72% · contrast 87% · warm 75% / cool 20% · brighter towards: top-left (7), top (3), bottom (1)
- **Palette (measured):** #110806 black 15%, #f1c016 gold 11%, #ab4e0f brown 10%, #581218 dark red 8%, #f8e987 light gold 7%, #f4f1e3 light yellow 5%

### Watermelon, plum, bell and grapes, win animation parts

`WIN_SYMBOLS_MERGED_VB_2_spritesheet` · atlas · 72 parts · largest 421×377 · sheet `sheets/WIN_SYMBOLS_MERGED_VB_2_spritesheet.webp`

- **Role:** The layered parts four symbols are animated from when they win.
- **Subject:** The watermelon and plum whole; the bell split into body (fruit_bell), inner disc (bell2), clapper (stick_bell) and shadow; the grapes with their leaf and stem apart; two star sparks, two cell patterns and two flames of 30 frames each.
- **Style:** The reel symbols taken apart, in the same glossy gold-rimmed manner.
- **Rendering:** Smooth airbrushed forms with gold outline; sparks are white four-point stars with soft rays; flames are soft photographic fire.
- **Colour:** Mixed by symbol: purple (#580a8a), gold and orange (#f1ba1b, #e13d05), brown (#a14e0a) and pale gold highlights (#f7f3e4) over black.
- **Lighting:** Top-left highlights; sparks and flames are emissive.
- **Ambience:** The same bright fruit-machine cheer, with fire added on a win.
- **Materials:** Glossy fruit, polished gold bell, waxy leaf, fire.
- **Variants:** Four symbols share two flame sequences and the spark.
- **Motion:** Fire1 (100x153) and Fire2 (52x101), 30 frames each, burn on the winning symbol; the bell is cut so its body and clapper can swing apart and the grapes' leaf can move (inference from the split parts).
- **Construction:** 72 parts, 60 of them flame frames. Only the bell and the grapes are cut into moving pieces; the watermelon and plum are single pictures.
- **Notes:** The split is minimal: one or two moving pieces per symbol, and the shared flame does the rest.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 45% · saturation 72% · contrast 77% · warm 59% / cool 35% · brighter towards: bottom (17), bottom-right (4), top-left (4)
- **Palette (measured):** #080702 black 8%, #f7f3e4 light gold 8%, #f1ba1b orange 8%, #580a8a dark purple 8%, #a14e0a brown 8%, #65140a dark red 4%

### Lemon, orange and cherries, win animation parts

`WIN_SYMBOLS_MERGED_VB_3_spritesheet` · atlas · 66 parts · largest 526×471 · sheet `sheets/WIN_SYMBOLS_MERGED_VB_3_spritesheet.webp`

- **Role:** The layered parts three fruit symbols are animated from when they win.
- **Subject:** The lemon and orange whole, the cherries as a front cherry with its leaf and a back cherry, one star spark, the cell pattern and the same two 30-frame flames.
- **Style:** The reel symbols taken apart, in the same glossy gold-rimmed manner.
- **Rendering:** Smooth airbrushed forms with gold outline and drop shadow; soft fire.
- **Colour:** The warmest symbol sheet: yellow and orange (#f2b928 at 27%, #d89b07, #faf116), red (#ef4e1d) and a little leaf green (#287615); measured warm 92%.
- **Lighting:** Top-left highlights; spark and flames are emissive.
- **Ambience:** Bright and sunny, then on fire.
- **Materials:** Glossy peel and cherry skin, gold stems, fire.
- **Variants:** The two cherries are separate so they can swing against each other.
- **Motion:** Fire1 and Fire2, 30 frames each, as in the other symbol sheets; the two cherries move apart (inference from the split).
- **Construction:** 66 parts, 60 of them flame frames; lemon and orange at 526x471, larger than the other fruit.
- **Notes:** The flame frames are repeated on every symbol sheet, so each sheet stands alone at the cost of shipping the same fire three times.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 56% · saturation 81% · contrast 69% · warm 92% / cool 3% · brighter towards: bottom (16), bottom-right (4), top-left (3)
- **Palette (measured):** #f2b928 orange 27%, #d89b07 orange 10%, #ef4e1d red 10%, #060301 black 8%, #9c4e05 brown 6%, #f8f4e0 light gold 5%

### Free Spins volcano, win animation parts

`WIN_SYMBOLS_MERGED_VB_4_spritesheet` · atlas · 38 parts · largest 421×377 · sheet `sheets/WIN_SYMBOLS_MERGED_VB_4_spritesheet.webp`

- **Role:** The layered parts the Free Spins symbol is animated from when it lands or triggers.
- **Subject:** The dashed red and yellow frame, the FREE SPINS lettering and its highlight copy, the volcano picture in three states (bright magenta sky, dimmer, darkest), a ray burst in two copies and a 30-frame burst of lava drops.
- **Style:** An illustrated scene with heavy display lettering, as on the reel symbol.
- **Rendering:** Flat painted mountain with glowing lava streaks; bevelled yellow-orange letters with a red outline; the ray bursts are soft, the lava drops sharp orange blobs.
- **Colour:** Black and wine (#0d0201, #510a22), magenta-red (#af164f), orange and yellow (#ee8e11, #f8db1c, #f3e589); measured with no cool share.
- **Lighting:** The crater is the light: a yellow-white burst at the top centre that the three states brighten step by step.
- **Ambience:** A building eruption.
- **Materials:** Rock, lava, smoky sky, enamel lettering.
- **Variants:** Three brightness states of one volcano picture; lettering with and without highlight.
- **Motion:** sequens_animation, 30 frames at 158x98: lava drops are thrown up and out from the crater. The three sky states and the lettering highlight are cross-faded (inference from the parts).
- **Construction:** 38 parts, 30 of them the lava burst; frame, lettering and picture are separate layers at up to 526x258.
- **Notes:** The eruption is done with one small frame sequence over a still, and three stills of rising brightness: a cheap way to make a picture feel alive.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 39% · saturation 84% · contrast 72% · warm 90% / cool 0% · brighter towards: top (3), top-left (3), right (3)
- **Palette (measured):** #0d0201 black 24%, #ee8e11 orange 18%, #510a22 dark red 13%, #f3e589 gold 9%, #f8db1c gold 8%, #af164f red 6%

### Wild bust and fireball, win animation parts

`WIN_SYMBOLS_MERGED_VB_5_spritesheet` · atlas · 46 parts · largest 330×342 · sheet `sheets/WIN_SYMBOLS_MERGED_VB_5_spritesheet.webp`

- **Role:** The layered parts of the one-cell wild and of the fireball symbol.
- **Subject:** The woman's bust (girl_img) and a white-gold glowing copy of it (girl_sun_img), the WILD lettering and its highlight, her feather headdress apart, her eyebrows and two bead earrings as loose pieces, two fire backdrops, the frame as four rails, the whole wild cell as one picture, a light burst, and the fireball in 30 frames.
- **Style:** Painted pin-up figure for the wild; photographic molten ball for the fireball.
- **Rendering:** The bust is softly painted with fine jewellery detail; the fire backdrops are sharp photographic flame; the WILD letters are bevelled gold with a teal face; the fireball frames are sharp and mottled.
- **Colour:** Orange, gold and dark red (#c46024, #f7eb93, #eeb253, #5c1608, #9a3012) with the teal of her feathers as the small cool share (measured cool 6%).
- **Lighting:** The figure is lit warm from the fire behind and around her; the glowing copy turns her into a light source; the fireball is self-lit.
- **Ambience:** Heat and glamour: the wild is the game's face.
- **Materials:** Skin, teal and red feathers, gold and turquoise jewellery, beads, fire, carved gold frame rails.
- **Variants:** The wild has a normal and a glowing copy, and two fire backdrops (bg_img, rebg_img).
- **Motion:** The fireball's surface boils over 30 frames (Symbol, 172x149). The wild blinks or raises her brows and her earrings swing, as those pieces are cut loose (inference from the parts); the glowing copy and the burst flash on a win (inference).
- **Construction:** 46 parts, 30 of them fireball frames. The frame is four separate rails so it can be stretched to more than one cell.
- **Notes:** The fireball's own animation is a frame sequence of the whole ball, not a shader or a rig: 30 small pictures.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 46% · saturation 73% · contrast 85% · warm 94% / cool 6% · brighter towards: bottom (10), top (2), left (1)
- **Palette (measured):** #170603 black 17%, #c46024 orange 15%, #f7eb93 light gold 15%, #eeb253 orange 12%, #5c1608 dark red 11%, #9a3012 red 10%

### Sevens, win animation parts

`WIN_SYMBOLS_MERGED_VB_spritesheet` · atlas · 38 parts · largest 421×377 · sheet `sheets/WIN_SYMBOLS_MERGED_VB_spritesheet.webp`

- **Role:** The layered parts the red Lucky 7 and the blue 7 are animated from when they win.
- **Subject:** The red 7 and the blue 7 without ribbon, a gold outline glow for each, the LUCKY ribbon as its own piece, the step-fret cell pattern, a small light burst for each seven and a 30-frame flame.
- **Style:** The same glossy gold-rimmed numerals as on the reels, taken apart.
- **Rendering:** Clean bevelled numerals with a scale texture; the glows are soft outlines of the same silhouette; the flame is a soft photographic fire.
- **Colour:** Red and gold lead (#bf2502, #f6e992, #f2c516, #f17411) with dark red (#630f06); the blue seven adds the only cool note.
- **Lighting:** Top-left highlights on the numerals; the glow layers and flame are emissive.
- **Ambience:** A win makes the symbol catch fire: heat is the game's way of saying yes.
- **Materials:** Enamel numerals in gold bezels, satin ribbon, fire.
- **Variants:** Two sevens share one outline glow shape; the ribbon belongs to the red one only.
- **Motion:** A flame of 30 frames (Symbol 1, 90x177) plays on the symbol; the outline glow and the small burst are faded and scaled by the timeline (inference from the parts: the timeline itself was not played here).
- **Construction:** 38 parts: numerals at 421x377, glows at the same size, the ribbon at 440x153, and 30 flame frames. Animated as a Flash-style timeline at 30 frames a second (the view-builder file states fps 30), not as a skeleton.
- **Notes:** The win version is built from the same picture as the reel symbol plus three cheap layers: an outline glow, a spark and a looping flame.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 47% · saturation 78% · contrast 67% · warm 81% / cool 19% · brighter towards: bottom (9), top-left (2), top (1)
- **Palette (measured):** #bf2502 red 19%, #f6e992 light gold 14%, #150506 black 12%, #f2c516 gold 8%, #f17411 orange 8%, #f3f4e6 light yellow 6%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Expanding wild, paytable picture

`expanding_wild` · atlas · 1 parts · largest 157×569 · sheet `sheets/expanding_wild.webp`

- **Role:** Paytable picture that explains the feature: a one-cell wild on top, arrows, and the full three-cell wild below.
- **Subject:** A bronze-skinned woman in a gold helmet-crown with a tall headdress of teal and red feathers, a teal bikini top and loincloth with gold and turquoise jewellery, bead earrings and flames around her hands, standing in a gold fretwork frame over the word WILD; above her the bust version and a row of yellow arrows pointing down.
- **Style:** Glamour pin-up illustration in a realistic painted manner, with an Aztec or Maya priestess costume; far more realistic than the fruit symbols.
- **Rendering:** Smooth painted skin with strong specular highlights, fine feather strokes, detailed jewellery; fire is photographic; the frame is flat ornament.
- **Colour:** Warm skin and fire in brown and orange (#994218, #d27a1e, #e29d4f, #ebca69) against teal costume and feathers (#195957, #1c948e).
- **Lighting:** Warm light from the fire around her, with bright highlights on skin and gold; the fire behind acts as a rim light.
- **Ambience:** Seductive and fiery; she is the only living thing in the game.
- **Materials:** Skin, feathers, gold, turquoise, cloth, fire.
- **Variants:** Bust (one cell) and full figure (three cells).
- **Motion:** None in this file.
- **Construction:** One flat picture, 157x569.
- **Notes:** Teal against orange-red is the game's one complementary pair, and it is carried by her costume and by the reel cells.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 46% · saturation 70% · contrast 65% · warm 74% / cool 23%
- **Palette (measured):** #994218 brown 23%, #d27a1e orange 18%, #e29d4f orange 14%, #195957 dark cyan 13%, #ebca69 orange 7%, #1c1718 black 4%

### Pattern feature picture: three Lucky 7s and four wild reels

`queens` · atlas · 1 parts · largest 750×480 · sheet `sheets/queens.webp`

- **Role:** Illustration for the intro panel and the paytable: the pattern that pays 1000x the total bet.
- **Subject:** The reel board with three red Lucky 7s on the first reel and the full-height feathered woman on each of the other four reels, each over the word WILD, in the gold fretwork frame.
- **Style:** A composed screenshot-like picture of the game's own symbols.
- **Rendering:** As the symbols themselves: glossy sevens, painted figures, photographic fire.
- **Colour:** Orange and brown (#d17520 at 33%, #903d16, #f0a849) with teal (#216562).
- **Lighting:** Warm, from the fire behind each figure.
- **Ambience:** The promise of the game in one picture.
- **Materials:** As the wild and the sevens.
- **Variants:** A smaller copy is the first sprite of the tutorial sheet.
- **Motion:** None.
- **Construction:** One flat picture, 750x480.
- **Notes:** Four identical figures side by side is how the top win looks: the repeat is intended.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 43% · saturation 74% · contrast 59% · warm 80% / cool 18%
- **Palette (measured):** #d17520 orange 33%, #903d16 brown 20%, #216562 dark cyan 12%, #f0a849 orange 7%, #4f2c17 brown 7%, #1f1312 black 4%

### Expanding wild, animation parts

`WIN_EXPANDING_WILD_spritesheet` · atlas · 57 parts · largest 477×771 · sheet `sheets/WIN_EXPANDING_WILD_spritesheet.webp`

- **Role:** The full-reel wild as it is animated: the game's one character.
- **Subject:** The full standing figure (Girl, 314x757) and a soft orange glow copy of her (GirlHL), a column of fire as backdrop in two brightnesses, a dotted gold frame, her feather headdress in 13 frames, her eyebrows, lips in four shapes and two earrings as loose pieces, the WILD lettering with a glow copy, two star bursts, and two flames of 27 frames each.
- **Style:** Realistic painted pin-up figure with an Aztec or Maya costume.
- **Rendering:** Soft painted skin and cloth with sharp jewellery; the headdress frames are painted feathers; flames and backdrop are photographic fire.
- **Colour:** Black and orange fire (#120f0d, #ed520d, #9c2710), teal costume and feathers (#104c48, #118780), gold and pale gold highlights (#f1b859, #f8e390, #fcfadb).
- **Lighting:** Lit from the fire: warm from below and behind; the brief gives the light as coming from the top in 15 of 16 lit parts.
- **Ambience:** A fire priestess stepping forward; glamour and heat.
- **Materials:** Skin, feathers, gold, turquoise beads, cloth, fire.
- **Variants:** One figure. The same woman appears as a bust in the one-cell wild.
- **Motion:** Plmg, 13 frames: the feathers of the headdress sway. L, 4 frames: the lips change shape. Symbol 14 and Symbol 27, 27 frames each (153x173): flames burn at her hands. Symbol 1, 27 frames (259x256), is too faint on the sheet to describe. The view-builder file names three timelines (top, middle, bottom) with the labels firstFrame, loop_anim and end_frame.
- **Construction:** 57 parts. The body is a single painted picture; only the face details (brows, lips), the earrings and the headdress move, and fire is layered around her. Flash-style timeline at 30 frames a second, no skeleton and no mesh.
- **Notes:** A full-height character is brought to life with four small moving pieces and two flame loops. It is far cheaper than a rig, and the still body is the price: she does not shift her weight or breathe (inference from the parts).
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 42% · saturation 73% · contrast 57% · warm 70% / cool 30% · brighter towards: top (15), bottom-right (1)
- **Palette (measured):** #120f0d black 17%, #ed520d orange 15%, #104c48 dark cyan 12%, #9c2710 red 9%, #f1b859 orange 8%, #118780 dark cyan 8%


## Logo and title

The game's own wordmark.

### Loading logo: CASH ERUPTION across the fireball

`splash` · atlas · 1 parts · largest 1498×879 · sheet `sheets/splash.webp`

- **Role:** The title art of the loading screen.
- **Subject:** The words CASH ERUPTION in heavy slab-serif capitals laid across a large molten sphere with flames licking off its edge.
- **Style:** Display lettering over a photographic fire sphere.
- **Rendering:** Letters with a yellow-to-red vertical gradient, a fine inner flame texture, a thin yellow inline, a dark red extruded edge and a black glow; the sphere is sharp, mottled and haloed in orange.
- **Colour:** Orange, gold and red (#f38f1b, #feeb7d, #f0aa4a, #9b2d0e, #f21b03); fully warm.
- **Lighting:** The sphere is the light source; the letters are lit as if from within, brightest along the top.
- **Ambience:** Hot and loud: the feature symbol and the name in one image.
- **Materials:** Molten rock and fire; enamel-like letters with a dark bevel.
- **Variants:** The same lettering is the in-game logo, in one line and stacked.
- **Motion:** None in the file.
- **Construction:** One PNG of 1498x879 with the lettering and the sphere baked together.
- **Notes:** The logo is tied to the fireball from the first screen, so the player learns which symbol matters before the game opens.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 48% · saturation 81% · contrast 88% · warm 100% / cool 0% · brighter towards: bottom (1)
- **Palette (measured):** #9b2d0e red 16%, #f38f1b orange 15%, #feeb7d gold 13%, #f0aa4a orange 13%, #bf7329 orange 10%, #571807 dark red 9%

### Game logo, in-game

`logo_spritesheet` · atlas · 3 parts · largest 97×451 · sheet `sheets/logo_spritesheet.webp`

- **Role:** The title above the reels; pieces for a landscape and a portrait layout.
- **Subject:** CASH and ERUPTION as two separate words for the one-line landscape title (ERUPTION is stored turned on its side to save space), and a stacked two-line version for portrait.
- **Style:** Heavy slab-serif display capitals with flared feet.
- **Rendering:** Yellow-to-red vertical gradient with a flame texture, thin yellow inline, dark red extrusion and soft dark glow.
- **Colour:** Gold, orange and red (#f5f150, #f6a00f, #ea1707, #ed5c0d) over dark red (#4e0805, #831b09).
- **Lighting:** Brightest at the top of each letter, as if glowing from inside.
- **Ambience:** Hot, bold, simple.
- **Materials:** Glowing enamel or molten metal lettering.
- **Variants:** One-line (two pieces) and stacked.
- **Motion:** The view-builder file gives each version a one-frame timeline, so the logo is still (stated in the file).
- **Construction:** 3 sprites: 251x97, 97x451 and 299x118, scaled up 1.25 times in the landscape layout as the layout file states.
- **Notes:** A still logo: nothing in the title moves, the fire is all in the texture.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 48% · saturation 87% · contrast 86% · warm 100% / cool 0%
- **Palette (measured):** #f5f150 gold 19%, #4e0805 dark red 16%, #f6a00f orange 15%, #a96420 orange 15%, #ea1707 red 12%, #831b09 dark red 9%

### Game logo, paytable copy

`gameLogo` · atlas · 1 parts · largest 306×119 · sheet `sheets/gameLogo.webp`

- **Role:** The stacked logo at the top of the paytable page.
- **Subject:** CASH over ERUPTION in the same slab-serif fire lettering.
- **Style:** As the in-game logo.
- **Rendering:** Yellow-to-red gradient, yellow inline, dark red extrusion.
- **Colour:** #f17b10, #a96b22, #e91907, #f5eb51 over #490705.
- **Lighting:** Brightest at the top of the letters.
- **Ambience:** As the in-game logo.
- **Materials:** Glowing enamel lettering.
- **Variants:** A copy of the stacked version at 306x119.
- **Motion:** None.
- **Construction:** One PNG.
- **Notes:** Nothing new against the in-game logo.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 46% · saturation 87% · contrast 84% · warm 100% / cool 0%
- **Palette (measured):** #a96b22 orange 21%, #f17b10 orange 21%, #490705 dark red 13%, #e91907 red 11%, #f5eb51 gold 11%, #81220a dark red 10%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Popup panels

`popups_animation_spritesheet` · atlas · 5 parts · largest 850×511 · sheet `sheets/popups_animation_spritesheet.webp`

- **Role:** The panels of the feature messages (free spins won, bonus won, totals).
- **Subject:** A rectangle of fire as a border, a black panel with a thin gold line, and three black panels with a soft coloured edge glow in green, pink and red-orange.
- **Style:** Flat panels with light edges.
- **Rendering:** Solid black with a soft outer glow; the fire border is photographic flame.
- **Colour:** Black (#070401 at 64%) with brown-orange and gold (#561b07, #e03c04, #e6aa12).
- **Lighting:** Edge glow only.
- **Ambience:** A dark card that makes the text and figures the event.
- **Materials:** Fire, light.
- **Variants:** Green, pink and red glows match the Minor, Major and Grand colours (inference from the meter colours).
- **Motion:** None in the sprites. In play the free spins start message sat still on the black panel inside the burning border.
- **Construction:** 5 sprites; the fire border is 850x511, the panels 639x334 and 806x428.
- **Notes:** Popups are black cards with coloured edges and yellow condensed capitals (PRESS BUTTON TO START FREE SPINS! in the screens); no illustration is spent on them.
- **Measured:** dark, saturated, warm, low contrast · brightness 12% · saturation 56% · contrast 22% · warm 82% / cool 8%
- **Palette (measured):** #070401 black 64%, #561b07 brown 17%, #987111 brown 8%, #e03c04 orange 5%, #e6aa12 orange 4%, #253500 black 2%

### Popup buttons: start and skip

`popups_spritesheet` · atlas · 8 parts · largest 210×211 · sheet `sheets/popups_spritesheet.webp`

- **Role:** The buttons on the feature popups.
- **Subject:** Two round buttons in the gold fret ring: a green dome with a white play triangle (start) and a yellow dome with a double arrow (skip).
- **Style:** As the main controls.
- **Rendering:** Glossy dome, engraved ring; lit and grey states.
- **Colour:** Yellow and gold (#f6f02f, #e2ba15) with white highlight (#fafaec) and grey for the disabled state.
- **Lighting:** Top-lit.
- **Ambience:** As the main controls.
- **Materials:** Glass dome, gold ring.
- **Variants:** Two buttons, four frames each.
- **Motion:** State changes only.
- **Construction:** 8 sprites of 210x211.
- **Notes:** The same button art as the bonus panel; one button family serves the whole game.
- **Measured:** bright, vivid, warm, high contrast, hard-edged, strong highlights · brightness 66% · saturation 64% · contrast 84% · warm 95% / cool 3%
- **Palette (measured):** #f6f02f gold 22%, #fafaec light gold 14%, #e2ba15 gold 6%, #d7d5c9 light yellow 5%, #230c09 black 4%, #605e5c grey 4%

### Win meter glow and coins

`winmeter_flame_spritesheet` · atlas · 8 parts · largest 921×493 · sheet `sheets/winmeter_flame_spritesheet.webp`

- **Role:** The glow behind the win amount on a larger win, and the coins that fly.
- **Subject:** A wide soft yellow bar with an orange flame-like halo, a thin gold frame, and a gold coin with a step-fret face in six frames of a spin.
- **Style:** Light effect and a small rendered coin.
- **Rendering:** The glow is fully soft; the coin is sharp with an engraved face and a bright rim.
- **Colour:** Orange and yellow (#e24301 at 41%, #fbeb51 at 39%, #f5a61b).
- **Lighting:** Emissive glow; the coin catches light on its rim as it turns.
- **Ambience:** Warm payoff.
- **Materials:** Light; polished gold.
- **Variants:** One glow (921x493), one frame, one coin in six frames.
- **Motion:** coin, 6 frames: the coin turns from face-on to edge-on. A particle file beside it gives the coins a lifetime of 1.35 seconds, up to 50 at a time, shot at 200 to 800 pixels a second (stated in the file).
- **Construction:** 8 sprites; the coin fountain is a particle emitter over a six-frame sprite.
- **Notes:** The coin carries the same step-fret motif as every frame in the game.
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 63% · saturation 85% · contrast 53% · warm 100% / cool 0%
- **Palette (measured):** #e24301 orange 41%, #fbeb51 gold 39%, #f5a61b orange 12%, #f17e0d orange 4%

### Big win and colossal win plates

`winmeter_layout_spritesheet` · atlas · 3 parts · largest 209×608 · sheet `sheets/winmeter_layout_spritesheet.webp`

- **Role:** The plates behind the Big Win and Colossal Win titles (named BigWin and ColossWin).
- **Subject:** Two black plates in a red and gold fretwork frame, stored upright.
- **Style:** Ornamental frame, flat.
- **Rendering:** Hard-edged fret pattern, black centre.
- **Colour:** Black (#000001 at 69%) with gold (#e4b524) and red (#c2190b).
- **Lighting:** Flat.
- **Ambience:** Formal: the big win is announced on a plate, not by a mascot.
- **Materials:** Gold and red enamel fretwork.
- **Variants:** Two plates of 209x608, near identical.
- **Motion:** None in the sprites.
- **Construction:** 3 sprites, one empty; the titles themselves are live text, not drawn art (inference: no drawn title words are among the files).
- **Notes:** There is no drawn BIG WIN lettering in the captured files; the celebration is a plate, a glow and coins. A big win was not reached in play, so how it looks on screen is not confirmed.
- **Measured:** dark, saturated, warm, high contrast, hard-edged · brightness 16% · saturation 34% · contrast 74% · warm 100% / cool 0%
- **Palette (measured):** #000001 black 69%, #e4b524 gold 14%, #c2190b red 8%, #9b6d1b brown 7%


## Effects

Frame sequences, glows, particles and transitions.

### Small fire puff

`bonus_panels_animation_spritesheet` · atlas · 7 parts · largest 89×88 · sheet `sheets/bonus_panels_animation_spritesheet.webp`

- **Role:** A puff of fire on the bonus counter panel when a fireball is counted (inference from its folder).
- **Subject:** A small ball of flame that brightens to white-yellow and fades to dark smoke.
- **Style:** Photographic fire.
- **Rendering:** Soft, with fine embers.
- **Colour:** Brown, orange and pale gold (#552511, #b8501b, #f68332, #fdef85).
- **Lighting:** Emissive.
- **Ambience:** A small confirmation.
- **Materials:** Fire and smoke.
- **Variants:** One sequence.
- **Motion:** Symbol, 7 frames of about 80x80: ignite, flare, fade to smoke.
- **Construction:** 7 sprites.
- **Notes:** Seven frames for a full ignite-and-fade.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 36% · saturation 76% · contrast 36% · warm 100% / cool 0% · brighter towards: top-left (1)
- **Palette (measured):** #552511 brown 46%, #b8501b orange 23%, #f68332 orange 12%, #fdef85 light gold 6%, #f8bc59 orange 5%, #15130b black 4%

### Fireball trail and impact

`flying_fireballs_animation_spritesheet` · atlas · 21 parts · largest 99×99 · sheet `sheets/flying_fireballs_animation_spritesheet.webp`

- **Role:** The flame trail behind a flying fireball and its burst on landing.
- **Subject:** A soft red-orange glow disc, an explosion of embers in 15 frames and a small flame in 5 frames.
- **Style:** Photographic fire and embers.
- **Rendering:** Soft glow; the explosion is fine sharp particles; the flame is soft.
- **Colour:** Orange and red (#f1791f, #fa1c0d) with pale gold (#f8e689, #f4b44b).
- **Lighting:** Emissive.
- **Ambience:** A hit.
- **Materials:** Fire, embers, smoke.
- **Variants:** One explosion, one flame.
- **Motion:** explosion_frame, 15 frames at 96x96: a spark, a burst of embers spreading sideways, then fading smoke. fire_frame, 5 frames at 60x120: a flame flickers.
- **Construction:** 21 sprites, all small.
- **Notes:** The whole effect fits in 96x96 frames: it is scaled up in play, and softness hides the size.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 47% · saturation 74% · contrast 43% · warm 99% / cool 0% · brighter towards: top-left (6), bottom (5), top (4)
- **Palette (measured):** #f1791f orange 22%, #311a0b black 18%, #fa1c0d red 16%, #f8e689 light gold 12%, #f4b44b orange 11%, #7b3a17 brown 7%

### Flying fireball and winner panels

`flying_fireballs_spritesheet` · atlas · 4 parts · largest 784×486 · sheet `sheets/flying_fireballs_spritesheet.webp`

- **Role:** The blurred fireball that flies across the screen in the bonus, a large soft shadow, and two flame-edged panels for the winner message.
- **Subject:** A fireball smeared by motion blur, a black oval shadow, and two tall black panels with a red and orange burning edge (stored upright).
- **Style:** Photographic fire.
- **Rendering:** The ball is blurred along its path; the panels have a hard gold line and a soft flame edge.
- **Colour:** Black (#070404 at 52%) with orange, red and gold (#de6813, #c51507, #f4d011).
- **Lighting:** Emissive.
- **Ambience:** Impact and heat.
- **Materials:** Fire.
- **Variants:** Two winner panels (named GT and CE: probably two games sharing the feature, inference).
- **Motion:** None in the sprites; the ball is moved by the client.
- **Construction:** 4 sprites; the blurred ball is 200x188.
- **Notes:** A pre-blurred copy of the symbol is shipped for the flight instead of blurring at run time.
- **Measured:** dark, saturated, warm, medium contrast · brightness 19% · saturation 46% · contrast 52% · warm 100% / cool 0% · brighter towards: left (1)
- **Palette (measured):** #070404 black 52%, #de6813 orange 16%, #c51507 red 12%, #f4d011 gold 6%, #292929 grey 6%, #640300 dark red 5%


## Game interface

Buttons, counters and panels drawn for this game.

### Prize meter frame

`treasures_bar_spritesheet` · atlas · 1 parts · largest 54×337 · sheet `sheets/treasures_bar_spritesheet.webp`

- **Role:** The frame of each of the four prize meters above the reels (Grand, Major, Minor, Mini); the layout names four treasure bars.
- **Subject:** A long narrow gold fretwork frame, stored upright.
- **Style:** Ornamental frame, flat.
- **Rendering:** Hard-edged repeating fret pattern in orange-gold on black.
- **Colour:** Orange-gold (#c98210 at 63%, #e6b11b) on black (#130608).
- **Lighting:** Flat.
- **Ambience:** Matches the bottom panel.
- **Materials:** Gold fretwork.
- **Variants:** One frame used four times; each meter's colour comes from its text.
- **Motion:** None.
- **Construction:** One sprite of 54x337, turned on its side in the game.
- **Notes:** The four tiers differ only in text colour (red, pink, green, cyan in the screens), not in frame art.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 41% · saturation 88% · contrast 66% · warm 100% / cool 0%
- **Palette (measured):** #c98210 orange 63%, #130608 black 21%, #885013 brown 6%, #5c2509 brown 5%, #e6b11b orange 5%

### Bonus panel pieces

`bonus_panels_spritesheet` · atlas · 7 parts · largest 210×211 · sheet `sheets/bonus_panels_spritesheet.webp`

- **Role:** Pieces of the two counters shown above the reels during the fireball bonus (x6 COLLECTED and 15 FOR GRAND TREASURE in the screens), and its play button.
- **Subject:** A round button with a green glass dome and a white play triangle in a gold fret ring, a black bar with a gold edge, an end cap for it, and a small fireball icon.
- **Style:** As the main controls.
- **Rendering:** Glossy dome, engraved gold ring; flat black bar with a thin gold line.
- **Colour:** Yellow and lime (#f3f538, #cef006) with white highlight and black (#060202).
- **Lighting:** Top-lit dome; a lit state washes the face yellow.
- **Ambience:** As the main controls.
- **Materials:** Glass dome, gold ring.
- **Variants:** The button in four frames (normal, lit, grey visible).
- **Motion:** State changes only.
- **Construction:** 7 sprites; the button is 210x211, the fireball icon 60x55.
- **Notes:** The small fireball icon is the full symbol reduced, used as a counter.
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged, strong highlights · brightness 60% · saturation 58% · contrast 84% · warm 92% / cool 4% · brighter towards: top (1)
- **Palette (measured):** #f3f538 gold 19%, #f5f5e9 light yellow 14%, #060202 black 13%, #636805 brown 7%, #cef006 gold 5%, #f7fb96 light gold 5%

### Intro animation placeholder

`tutorial_animation_spritesheet` · atlas · 1 parts · largest 3×3 · sheet `sheets/tutorial_animation_spritesheet.webp`

- **Role:** An empty placeholder.
- **Subject:** Nothing visible: a 3x3 sprite.
- **Style:** None.
- **Rendering:** None.
- **Colour:** None measured.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** None.
- **Motion:** None.
- **Construction:** One empty sprite.
- **Notes:** Listed because the game ships it; it holds no art.

### Intro panel pieces

`tutorial_spritesheet` · atlas · 17 parts · largest 750×480 · sheet `sheets/tutorial_spritesheet.webp`

- **Role:** The parts of the intro panel shown when the game opens: the pattern picture, the Free Spins and fireball symbols, the close button and the 'don't show again' tick box.
- **Subject:** A reduced copy of the four-wild-reels picture, a black panel with a bright green glowing edge, yellow glow shapes, the Free Spins volcano and the fireball symbols, thin yellow divider lines, a carved-stone close button with an X in three states, a small gold fretwork tick box and a yellow tick.
- **Style:** The game's own symbols on a black panel; stone and gold fretwork controls.
- **Rendering:** Flat black panel with a neon-like green outer glow; symbols as on the reels.
- **Colour:** Black (#040302 at 26%) with gold and orange (#f9c520, #e48721) and a green accent (#5d9103).
- **Lighting:** The symbols sit on soft yellow glow shapes that light them from behind.
- **Ambience:** A quick, loud promise before the first spin.
- **Materials:** Stone button, gold fretwork, glow.
- **Variants:** Close button and tick box in four frames each.
- **Motion:** State changes only.
- **Construction:** 17 sprites; the panel ground is 542x281, the pattern picture 750x480.
- **Notes:** The green edge of the panel is the one place the game uses a neon outline; it matches the green of the spin button.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 39% · saturation 59% · contrast 66% · warm 66% / cool 21% · brighter towards: top (5), bottom (1)
- **Palette (measured):** #040302 black 26%, #f9c520 gold 13%, #e48721 orange 12%, #5d9103 dark green 2%

### Bonus picture: the big fireball on the middle reels

`mini_slot` · atlas · 1 parts · largest 362×197 · sheet `sheets/mini_slot.webp`

- **Role:** Paytable illustration of the free spins: the three middle reels linked into one giant symbol, here a fireball.
- **Subject:** A small red reel board with fruit and bells on the outer reels and one large fireball filling the three middle reels.
- **Style:** A composed picture of the game's own symbols.
- **Rendering:** As the symbols.
- **Colour:** Black and dark red (#280604, #751508, #ae210e) with orange and gold (#af5a1c, #f8e280, #ecae4a).
- **Lighting:** The fireball lights the picture.
- **Ambience:** A red board: this is the free spins look.
- **Materials:** As the symbols.
- **Variants:** One picture, 362x197.
- **Motion:** None.
- **Construction:** One flat PNG.
- **Notes:** In the free spins played, the linked reels showed a giant Lucky 7, cherries, watermelon, orange and bell; a giant fireball did not land, so this picture is the only view of it.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 36% · saturation 78% · contrast 91% · warm 97% / cool 3%
- **Palette (measured):** #280604 black 24%, #751508 dark red 18%, #af5a1c orange 14%, #f8e280 gold 10%, #e76430 orange 8%, #ecae4a orange 8%

### Bottom panel: total bet, win, balance

`freespins_betpanel_spritesheet` · atlas · 1 parts · largest 1078×179 · sheet `sheets/freespins_betpanel_spritesheet.webp`

- **Role:** The three-field panel under the reels.
- **Subject:** A wide gold fretwork frame split into three bays, each with a black window on top and a dark teal textured plate below.
- **Style:** Ornamental carved frame, flat.
- **Rendering:** Orange-gold rails with a repeating fret and diamond pattern, hard-edged; the teal plates have a faint mottled texture.
- **Colour:** Black (#030d09), dark teal (#01342c) and gold-brown (#79520a, #de5e0b, #ce980c).
- **Lighting:** Flat.
- **Ambience:** A plain, readable dashboard in the board's own colours.
- **Materials:** Gold fretwork, dark stone or enamel plates.
- **Variants:** One piece; the file name places it with the free spins, and the base game shows the same panel in the screens.
- **Motion:** None.
- **Construction:** One sprite of 1078x179.
- **Notes:** Black windows with yellow figures: the numbers are the brightest thing in the panel.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 18% · saturation 65% · contrast 55% · warm 48% / cool 52% · brighter towards: bottom (1)
- **Palette (measured):** #030d09 black 48%, #01342c black 23%, #79520a brown 14%, #de5e0b orange 7%, #ce980c orange 6%, #ab640d brown 2%

### Panel animation placeholder

`panel_animations_spritesheet` · atlas · 1 parts · largest 30×30 · sheet `sheets/panel_animations_spritesheet.webp`

- **Role:** An empty placeholder (its only sprite is named empty).
- **Subject:** Nothing visible: a 30x30 transparent square.
- **Style:** None.
- **Rendering:** None.
- **Colour:** None measured.
- **Lighting:** None.
- **Ambience:** None.
- **Materials:** None.
- **Variants:** None.
- **Motion:** None.
- **Construction:** One empty sprite.
- **Notes:** Listed because the game ships it; it holds no art.

### Control buttons and bet panel

`panel_layout_spritesheet` · atlas · 52 parts · largest 526×282 · sheet `sheets/panel_layout_spritesheet.webp`

- **Role:** The game's own controls: spin, skip, autoplay, stop autoplay, the bet panel opener, plus, minus and confirm, with the panel's rails and fills.
- **Subject:** A round spin button with a green glass dome and a white circular arrow in a gold ring engraved with a step-fret border; the same in yellow as a skip button; a triangular autoplay button in blue and a red one to stop it, in a gold fretwork triangle; an orange stone tab with a white chevron; small carved-stone tiles with a yellow minus, plus and a green tick; gold fretwork rails; a teal panel ground.
- **Style:** Chunky game buttons in the temple's vocabulary: gold fretwork rims, carved stone tiles, glass domes.
- **Rendering:** Glossy domes with a strong top highlight; rough stone tiles with a yellow edge glow; rims with crisp engraved pattern. Each button has normal, lit and grey states.
- **Colour:** Gold (#f0ca17), teal (#079e93, #094538, #04705f) and black (#14110c), with green, yellow, blue and red reserved for button faces and grey for the disabled state.
- **Lighting:** Top-lit domes; the lit state adds a bright glow over the face.
- **Ambience:** Solid and tactile; the spin button is the one green object on the screen.
- **Materials:** Glass or gem domes, polished gold with fret engraving, weathered stone.
- **Variants:** Ten buttons, each in four frames, of which three states are visible on the sheet: normal, lit and grey.
- **Motion:** State changes only: each button is a four-frame strip.
- **Construction:** 52 sprites: the spin and skip buttons at 301x301, autoplay at 162x146, the stone tiles at 61x96 and 63x63.
- **Notes:** The spin button is green on a red and gold screen: the complementary colour makes the main control impossible to miss without making it large.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 50% · saturation 72% · contrast 76% · warm 68% / cool 25% · brighter towards: top (6), bottom (4), top-right (4)
- **Palette (measured):** #f0ca17 gold 9%, #079e93 cyan 8%, #14110c black 8%, #094538 dark cyan 7%, #f7f8ee light yellow 6%, #cfd4cb grey 4%


## Typography

Embedded fonts and lettering.

### Black digits, large

`BlackFontBig` · atlas · 1 parts · largest 538×517 · sheet `sheets/BlackFontBig.webp`

- **Role:** The bitmap digits for the value written on a large fireball (inference from the name and the paytable picture).
- **Subject:** The digits 0 to 9, a comma and a full stop in a tall condensed sans-serif.
- **Style:** Condensed grotesque numerals, close to the Oswald faces the game embeds.
- **Rendering:** Solid black fill with a thin orange outline; no gradient, no bevel.
- **Colour:** Black (#010100 at 75%) with an orange edge (#fb9700).
- **Lighting:** None: flat.
- **Ambience:** Blunt and readable.
- **Materials:** None.
- **Variants:** A smaller set is blackFont.
- **Motion:** None.
- **Construction:** One 538x517 texture with an XML table of glyph positions.
- **Notes:** The only flat, unshaded lettering in the game, made to be read on top of the brightest symbol.
- **Measured:** dark, saturated, warm, high contrast, hard-edged · brightness 13% · saturation 29% · contrast 64% · warm 100% / cool 0%
- **Palette (measured):** #010100 black 75%, #fb9700 orange 15%, #5d3800 brown 6%, #b06900 brown 4%

### Black digits, small

`blackFont` · atlas · 1 parts · largest 273×274 · sheet `sheets/blackFont.webp`

- **Role:** The bitmap digits for the value on a reel-size fireball.
- **Subject:** The digits 0 to 9, a comma and a full stop in the same condensed sans-serif.
- **Style:** Condensed grotesque numerals.
- **Rendering:** Solid black with a thin orange outline.
- **Colour:** Black (#010000) with an orange edge (#fc9700 at 28%).
- **Lighting:** None: flat.
- **Ambience:** Blunt and readable.
- **Materials:** None.
- **Variants:** The small size of BlackFontBig.
- **Motion:** None.
- **Construction:** One 273x274 texture with an XML table.
- **Notes:** Two sizes are shipped instead of scaling one, so the outline keeps its weight at both sizes.
- **Measured:** dark, saturated, warm, high contrast · brightness 21% · saturation 40% · contrast 64% · warm 100% / cool 0%
- **Palette (measured):** #010000 black 64%, #fc9700 orange 28%, #814d00 brown 6%


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
- `IGTlogo`: 1 parts
- `promospins_banner_spritesheet`: 3 parts
- `preloader`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Gilroy (Black); Oswald (Bold); Oswald (Light); Oswald (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 621 components cut from 67 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
