# Huff N Even More Puff Grand: art report

lnw · run `2026-11-26-1842-lnw-huff-n-even-more-puff-grand` · captured 2026-11-26

Source: the provider's free-play demo, https://ogs-gl-usnj.nyxop.net/game/?nogsoperatorid=386&nogsgameid=71871&nogsmode=demo&nogslang=EN_EN&nogscurrency=USD&clienttype=flash

**Extracted:** 1535 named components from 140 textures in 140 atlases; 11 Spine skeletons; 48 frame sequences (996 frames); 3 fonts. Grouped into 53 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

The Three Little Pigs on a building site at night: a glossy, toy-bright cartoon cast in gold, red and orange on see-through reels, with a two-ring fairground prize wheel turning behind them, six jackpot plaques down the side and a cool blue-green storybook garden around it all.

**Style.** Family-animation cartoon. Pigs and wolf are rounded mascots with big heads and readable expressions; tools (saw, hard hat, tape, toolbox) are chunky and simplified; houses are doll's-house fronts whose material is exaggerated (straw, logs, brick, pale stone). Prize art borrows from fairground and work-site signage.

**Rendering.** Smooth digital painting with airbrushed gradients, strong white gloss highlights, a thin outline of a darker tone and often a pale rim so pieces lift off the dark reel backing. Lettering is fat, bevelled, outlined and rimmed. Effects are flat hand-drawn frames with glow. The background is the one finely textured painting.

**Colour.** Warm cast on a cool stage. Feature and prize art is gold, orange and red (hat and saw rig: #8e2215, #f8ae0c, #d84f07, 88% warm); the background is 84% cool (#143240, #2f7040, #455787, #0d1a88) and the wolf is blue-violet (#56558c). Royals are a single emerald green (#1a6348). Prize tiers keep one colour each wherever they appear: magenta Mini, green Minor, blue Major, red Grand, white-blue Ultra. Measured over the game's own captured art: black #080907 13%, dark blue #162946 7%, orange #f4aa14 7%, dark red #590e23 6%.

**Lighting.** Night scene lit from inside the picture by lamps; objects are top-lit with hard gloss. Glow is kept as separate additive layers and outline sprites (hat glow, wedge glow, row highlight), not painted in. On screen the reel window is the darkest area and the wheel and lawn the brightest.

**Ambience.** Cheerful, loud and crowded, as the base-game screens show: the wheel, the rolling sign, six plaques and the logo all compete around a dark reel window, and the calm garden is reduced to a green and blue margin. The wolf is a comic villain, present in the base game only as a tail swishing under the reels. The pace of wins and features is not known from this run.

**Shape language.** Round and chunky everywhere: domed hats, circular saws and coins, rounded topiary, bubble letters. Sharpness is kept for the saw teeth, the wolf's muzzle and ears, and spark bursts.

**Materials.** Glossy plastic (hard hats, button), steel, gem-set steel and gold (saws, coins), straw, logs, brick and stone (houses and their frames), fur, clipped hedge and cobbles, varnished wood and brass (the wheel drum), hazard tape, soap bubbles and chrome in the logo.

**Typography and lettering.** Display lettering is drawn art: the logo gives each word its own material (wood HUFF, bubble PUFF, chrome GRAND), and prize and feature words are heavy rounded capitals with bevel, outline and rim, coloured by tier. Words are swapped as whole sprites for Spanish (PREMIO for JACKPOT). Running text is Noto Sans as twelve distance-field font pages, with Frutiger Neue in the provider's frame; both are the provider's.

**Motion.** Seen in the real frames: the two wheel rings turn slowly, the 3D sign above rolls from plate to plate, the wolf's tail swishes under the reels (1.33 s animations in the file), and on the one spin the spin button becomes a white stop square. Everything else is read from the files: eleven Spine 4.1.24 skeletons with symbol landings of 1.3 to 3.3 s and wins of 2 to 3 s, the wolf's pop-up (3.1 s in, 6.8 s loop) and blow (1.5 s in, 4.2 s loop), houses that build in 1.2 s and are blown away in 1.0 s, feature banners of 1.8 s, a 1.75 s caution-tape transition and a four-tier big win whose intro grows from 0.4 to 3.1 s. Faces, destruction and wind are drawn frame sequences (up to 89 frames; the three wind sheets total 137). Sprite sheets state 24 frames a second. No skeleton frame is shown in this report: the project's drawing tool does not read Spine 4.1 correctly.

**Variants and themes.** Grades by recolour on shared rigs: the saw in steel, diamond and gold; the wheel in silver and gold; features in plain, Super and Ultra; four houses on one rig. The hat and mansion blocks in 2x2, 3x3 and 3x5. English and Spanish versions of every worded picture. Landscape and portrait versions of most animations and plaques.

**How it is built.** PixiJS client. In this run: 140 textures, 1,535 named sprites, 11 skeletons, 3 fonts, 48 frame sequences. Sprite sheets are 'Red 7 Exporter' packs; skeletons are Spine 4.1.24 with few meshes and many additive slots; parts of one rig share one canvas size so grades, houses and banners swap part for part (saw parts 360x374, house parts 360x360, banner parts 1148x720). The background is one square 1920x1920 picture for both orientations. The reel board is a plain see-through dark rectangle with no drawn frame. The sign is a glTF model with a 1024x1024 texture; the wheel is assembled from wedge sprites.

**Consistency.** High: one outline-and-gloss treatment on every object, one lettering system, one colour per prize tier (blue-white for the top: Ultra, diamond saw, mansion frame), and the building-site motif carried into signs, stripes and the transition. The Buy Pass dialog's buttons are the one generic-looking set. The wolf's howling-moon win picture is a deliberate change of register.

**What to take from it.** (1) Keep the bonus in sight: the prize wheel turns permanently behind see-through reels and the sign above rolls through the features, so the top prizes are on screen on every spin. It costs a busy picture; the plain dark reel window is what keeps the symbols readable. (2) Set a warm, glossy cast on a cool, dark stage: the background measures 84% cool, the feature symbols 88% warm. (3) Tell the premium tier apart three ways at once: gold, a glowing patterned backing, and size beyond the cell. The royals are one colour and sit inside the cell. (4) Give each prize tier one colour and use it on every surface that names the tier: coin, plaque title, wheel wedge, halo. Reserve blue-white for the top. (5) Build grades as swaps on a shared rig and a shared canvas size: three saws from one animation set, four houses from one rig, eleven feature banners from one skeleton. (6) Rig what moves mechanically and draw what is chaotic: houses build from rigged parts and are destroyed in drawn frames; the wolf's body is rigged and his face is drawn. (7) Make the celebration from the cast: the big win is the wolf blowing down a better house per tier, and its particles are the game's own coin, hat and saw. (8) Carry the theme into the system art: hazard stripes for Super and Ultra, a road-sign diamond for the wheel, caution tape for the transition. (9) For an AI art package on this model the static pieces are few and large: one square background, about 18 symbol stills at 300 px, four houses with matching frames and backings, a coin with swappable words, wedges and plates with words, a logo. The cost sits in the drawn sequences (destruction, wind, swirls), which is where generated art would need the most hand work. (10) Limits of this report: seen on real screens are the loading screen, the base-game layout, eleven of the eighteen symbols, the turning wheel, the rolling sign, the wolf's tail and one spin. The free-play session expired after that spin, so every win, the hard hat and buzz saw features, the wolf's pop-up and blow, the houses, the wheel feature, free spins, the big win, the transition, the Buy Pass panel and the paytable are read from the files alone (parts, animation names, lengths measured from the skeleton files). No skeleton is drawn here, whatever the method notes below say: the project's drawing tool does not read Spine 4.1 correctly.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm and cool mixed, medium contrast · brightness 43% · saturation 60% · contrast 46% · warm 53% / cool 31% · brighter towards: top (113), bottom (50), top-left (23)

Palette: #0c0c09 black 14%, #fafaf7 light yellow 8%, #172846 dark blue 7%, #f1a915 orange 7%, #b4a386 orange 6%, #d0530c orange 6%, #c4c8d8 light blue 4%, #fbe80d gold 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 29% | 63% | 52% | 3% / 84% | #143240 dark cyan 46%, #2f7040 green 15%, #455787 blue 11% |
| Reel board | 2 | 38% | 73% | 39% | 24% / 49% | #091909 black 25%, #305c55 dark cyan 21%, #366315 dark green 13% |
| Symbols | 5 | 46% | 74% | 40% | 80% / 12% | #8e2314 red 21%, #f7ad0d orange 15%, #54092f dark magenta 11% |
| Characters | 1 | 36% | 58% | 50% | 19% / 68% | #13233a dark blue 22%, #56558c blue 20%, #c4c4d8 light blue 16% |
| Logo and title | 1 | 34% | 61% | 66% | 55% / 31% | #191c11 black 23%, #23632b dark green 13%, #56251b dark red 11% |
| Win celebrations and banners | 3 | 45% | 60% | 54% | 60% / 32% | #0d0a0e black 12%, #cc730d orange 11%, #651e10 dark red 9% |
| Effects | 13 | 55% | 26% | 28% | 46% / 20% | #010101 black 27%, #fbfefd light cyan 22%, #b1a583 orange 19% |
| Game interface | 5 | 36% | 72% | 64% | 63% / 26% | #2a130e black 26%, #891712 red 7%, #e66c0e orange 7% |
| Provider interface (shared) | 22 | 55% | 21% | 16% | 22% / 34% | #838481 grey 36%, #ffffff light blue 22%, #181819 black 11% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Base game background

`background` · atlas · 1 parts · largest 1920×1920 · sheet `sheets/background.webp`

- **Role:** The full scene behind the base game (frame name bg_basegame). In play, as the real screens show, only its upper part is seen: the night sky, the tall trees and the lamps either side of the wheel. The mansion and the avenue are hidden behind the wheel, the sign and the reels.
- **Subject:** A cobbled avenue running straight to a pale violet mansion with two white domes and a red, gold-lit entrance, between rows of rounded topiary trees, clipped box hedges, flower beds and lit street lamps, under a deep blue night sky with clouds, a few stars and far mountains.
- **Style:** Storybook illustration with a strong one-point perspective; every plant is a smooth rounded mass, the mansion a detailed doll's house.
- **Rendering:** Clean digital painting with fine texture in the cobbles and foliage, smooth gradients in the sky, and small glows on every lamp and window. One square picture, sharp throughout; the blur on the loading screen is added by the client.
- **Colour:** Cool: 84% of the measured colour. Dark blue-green #143240 (46%), greens #2f7040 and #5cab3b (19%), blue-violet stone #455787, #8e8ebd, #656da3 (23%), night blue #0d1a88 (7%). Warm appears only as lamp and window light and the red doorway.
- **Lighting:** Night, lit from inside the picture: warm lamps along the path and the mansion's windows and door, with a pool of warm light on the cobbles at the steps.
- **Ambience:** A calm, rich evening: the brick-and-better house the pigs built, seen from the gate where the wolf waits.
- **Materials:** Cobblestone, clipped foliage, flowers, painted stone, iron lamps.
- **Variants:** One background picture in the capture. The free spins pieces (a hedge overlay strip, a counter) suggest the same scene is kept for free spins with overlays (inference); not seen.
- **Motion:** None in the file, and none visible between the real frames of the base game: trees, lamps and sky are identical in all of them.
- **Construction:** One 1920x1920 picture on its own page (WebP), square so that the same file serves landscape and portrait; the reel board and the wheel cover its lower middle.
- **Notes:** Cool, dark and low in the centre, so the warm gold symbols sit on it with the greatest possible contrast. In play the centre is covered anyway: the painting's job is the green and blue margin around the machinery.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 29% · saturation 63% · contrast 52% · warm 3% / cool 84%
- **Palette (measured):** #143240 dark cyan 46%, #2f7040 green 15%, #455787 blue 11%, #8e8ebd blue 8%, #0d1a88 dark blue 7%, #656da3 blue 4%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Free spins pieces

`freespins` · atlas · 5 parts · largest 884×850 · sheet `sheets/freespins.webp`

- **Role:** What the free spins add to the board: a giant gold hard hat, a counter plate, a 'Reel Ways' tag and a hedge overlay strip. Not seen in play.
- **Subject:** The gold hard hat with pig badge at 884x850 (named megahat), an orange rounded counter plate with a dark rim, a blue REEL WAYS tag in a horizontal and a vertical cut, and a 1920 px strip of glowing cyan hedge edge.
- **Style:** As the base game's symbols and plaques.
- **Rendering:** The hat is the most finished single painting in the capture: smooth gradients, hard gloss, an orange outer glow.
- **Colour:** The most saturated unit (86%): gold #ebb818 (34%), orange #d26005 (22%), cyan #09c3c5 and #20fbe8 (22%).
- **Lighting:** Top light with hot highlights on the hat; the hedge strip is emissive cyan.
- **Ambience:** Inference: a brighter, more excited version of the same garden.
- **Materials:** Glossy plastic, enamel plate.
- **Variants:** The tag in landscape and portrait cuts.
- **Motion:** None in the sheet; the hat's landings are in the sym12-13 rig.
- **Construction:** One 'Red 7 Exporter' sheet, 5 frames on one page.
- **Notes:** The free spins have no background of their own in the files: inference, the same scene with overlays.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 59% · saturation 86% · contrast 62% · warm 72% / cool 28% · brighter towards: top (1)
- **Palette (measured):** #ebb818 gold 34%, #d26005 orange 22%, #09c3c5 cyan 18%, #20fbe8 cyan 4%, #47110d dark red 4%, #f9f4da light gold 3%

### Reel board, jackpot plaques and base-game furniture

`basegame` · atlas · 28 parts · largest 1920×1277 · sheet `sheets/basegame.webp`

- **Role:** What surrounds the reels in the base game: the reel window, the lawn and bushes it stands in, the jackpot plaques and their titles, the total-win meter, the click-to-start button and the wheel's pointer and wedge glows. The real screens show it assembled.
- **Subject:** A flat near-black green reel backing (1095x640) with a hairline top edge, drawn see-through in play so the turning wheel shows faintly behind the symbols; a strip of bright lawn and two dark bushes at its foot; plaques for Ultra, Super, Grand, Major, Minor and Mini stacked down the left edge, each a dark blue glass field with a thin jewelled gold frame and a title word above it: ULTRA and SUPER on hazard-stripe plates, GRAND (red), MAJOR (blue), MINOR (green), MINI (magenta); a yellow-and-red win meter; a glossy yellow pill button in two states; a gold arrow pointer; long wedge-shaped yellow and silver glows.
- **Style:** The reel board is deliberately plain so the symbols carry the picture. The plaques are slot-cabinet jewellery; SUPER and ULTRA borrow building-site hazard stripes.
- **Rendering:** Flat fills and thin bevelled frames for the board and plaques; fat bevelled lettering with outline and rim for the titles; soft painted foliage for the bushes.
- **Colour:** Green and dark: near-black green #091909 (28%), dark teal #305c55 (24%), greens #366315 and #649328 (29%), with yellow #f8f504 (6%) from the glows and button.
- **Lighting:** Little modelling on the board; the plaques have a diagonal glass sheen; the wedge glows are pure emissive outlines.
- **Ambience:** Quiet stage furniture around a loud cast. On screen the board is the darkest thing in the picture, with the bright wheel and the lime lawn around it.
- **Materials:** Dark glass, thin gold with gems, striped painted metal, clipped bush, glossy plastic for the button.
- **Variants:** Plaques come in a landscape and a portrait cut (names ending _L and _P). The wedge glow exists in yellow and silver; the button in base and hover.
- **Motion:** None in the sheet. The wedge glows are animated by the small superwheelfire skeleton (1.87 s).
- **Construction:** One 'Red 7 Exporter' sheet over three pages, 28 frames; the largest is the 1920x1277 ground picture. No drawn reel frame or dividers: the board is a single dark rectangle.
- **Notes:** All six jackpot levels show at once in the base game, largest at the top and shrinking downwards (at a $2.00 bet: $20,000, $15,000, $10,000, $2,000, $200.00, $40.00, as the screen states). The reels have no drawn frame or dividers at all; the 5x3 grid is read from the symbols alone.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 36% · saturation 72% · contrast 36% · warm 18% / cool 52% · brighter towards: top (6), top-left (1), left (1)
- **Palette (measured):** #091909 black 28%, #305c55 dark cyan 24%, #366315 dark green 15%, #649328 green 14%, #f8f504 gold 6%, #bfd5e0 light blue 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Hard hat and buzz saw symbols (skeleton)

`sym12-13` · atlas · 392 parts · largest 1502×895 · sheet `sheets/sym12-13.webp`

- **Role:** The animated versions of the two feature symbols, named sym12 (the hard hat, with its Mega Hat and Mega Mansion blocks) and sym13 (the buzz saw in its three grades), with their landings, wins, cuts and exits.
- **Subject:** A large gold hard hat with the pig badge; a red brick mansion; square patterned backings in three block sizes (2x2, 3x3, 3x5) in orange-red for the hat and magenta for the mansion; a circular saw taken apart into blade, hub, guard, cover, lever and button in steel, diamond and gold; chevron backings in blue, red and yellow; and many effect frames: fire swirls, sparkle dots, wood chips, saw sparks, a spinning hat.
- **Style:** The same glossy cartoon as the stills, at larger size. The saw is drawn as a toy-like power tool; the mansion as a doll's-house brick front with lit windows.
- **Rendering:** Smooth painted volumes with strong white highlights and a pale rim; backings are flat halftone or woven patterns with a soft blurred copy for the 'shine' and 'glow' versions; effect frames are thin bright shapes on transparency.
- **Colour:** Warm: 88% of the measured colour. Red #8e2215 (25%), gold-orange #f8ae0c (18%), dark magenta #580632 (12%), orange #d84f07 (11%), with near-white highlights #fcf6f4 (9%) and yellow #fef70e (6%). Blue appears only in the diamond saw and the blue chevrons.
- **Lighting:** Top light on the solid objects, with glow layers (bighat_glow, bigmansion_glow, the pig-badge pulse) stored as separate soft white or yellow shapes to be added on top.
- **Ambience:** Loud and celebratory: these are the symbols the game wants watched, and everything about them is gold, red and glowing.
- **Materials:** Glossy plastic, brushed and gem-set steel, gold, painted brick, and fire and sparks as flat glowing shapes.
- **Variants:** The saw's every part exists in three grades (plain steel with orange, diamond blue, gold). The hat and the mansion each have backings for three block sizes. Chevron backings come in blue, red and yellow.
- **Motion:** 37 animations, measured from the file: hat landings of 1.25 to 3.25 s (one per block size, for hat and for mansion), hat wins of 2.04 s (single, two, three), saw landing and win of 3.04 s per grade, 'cut' 3.67 s, 'exit' 4.17 s and 'transform' 2.50 s per grade. Frame sequences carry the effects: saw particles (89 frames), saw intro particles (53), mansion swirl (43), hat swirl (34), a second swirl (28), dot backing (20), hat spin (18), wood chips (11), a hat loop (11), sparks (10). Inference from the names: the saw lands, cuts across symbols and leaves, and can change grade. Not seen in play.
- **Construction:** Spine 4.1.24, 108 bones, 139 slots, 392 parts over 23 atlas pages, no meshes, 33 additive slots. The saw parts all share one 360x374 canvas, so the three grades swap part for part. The largest part is a 1502x895 backing for the 3x5 block.
- **Notes:** This one rig is the largest in the capture and holds two symbols and two features. Grade is a texture swap on a shared rig, the cheapest way to get nine saw states from one animation set.
- **Skeleton (from the file):** Spine 4.1.24 · 108 bones · 139 slots · animations: sym12_land (0 s), sym12_land_fs (0 s), sym12_land_megahat (0 s), sym12_land_megahat_2x2 (0 s), sym12_land_megahat_3x3 (0 s), sym12_land_megahat_3x5 (0 s), sym12_land_megamansion_2x2 (0 s), sym12_land_megamansion_3x3 (0 s), sym12_land_megamansion_3x5 (0 s), sym12_win_backup (0 s), sym12_win_bkg_anim (0 s), sym12_win_hat_anim (0 s), sym12_win_hat_three_anim (0 s), sym12_win_hat_three_land_anim (0 s), sym12_win_hat_two_anim (0 s), sym12_win_hat_two_land_anim (0 s), sym13_bigwin_diamond (0 s), sym13_cut (0 s), sym13_cut_diamond (0 s), sym13_cut_gold (0 s), sym13_exit (0 s), sym13_exit_diamond (0 s), sym13_exit_gold (0 s), sym13_landing (0 s), sym13_landing_diamond (0 s), sym13_landing_diamond_particle (0 s), sym13_landing_gold (0 s), sym13_landing_gold_particle (0 s), sym13_transform (0 s), sym13_transform_diamond (0 s), sym13_transform_gold (0 s), sym13_win (0 s), sym13_win_diamond (0 s), sym13_win_gold (0 s), sym_13_blade (0 s), sym_13_hat_land (0 s), sym_13_hat_loop (0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 47% · saturation 77% · contrast 33% · warm 88% / cool 3% · brighter towards: top (18), bottom (13), top-right (7)
- **Palette (measured):** #8e2215 red 25%, #f8ae0c orange 18%, #580632 dark magenta 12%, #d84f07 orange 11%, #fcf6f4 light orange 9%, #fef70e gold 6%

### Jackpot coin (skeleton)

`coin` · atlas · 24 parts · largest 521×285 · sheet `sheets/coin.webp`

- **Role:** The prize coin that carries a jackpot or wheel label, and a glow for the free spins counter. The paytable sheet shows the finished coins: Grand, Major, Minor, Mini, Super, Ultra, Wheel, and x2 versions of Mini and Minor.
- **Subject:** A gold coin with a pig's face on the front and a house on the back, a wheel-spoke front for the wheel coin, a rounded and a straight edge piece for the turn, and lettering as separate pieces: GRAND, MAJOR, MINOR, MINI, SUPER, ULTRA, WHEEL, JACKPOT, PREMIO, X2.
- **Style:** A chunky cartoon coin with a studded rim; the words are fat rounded capitals with a bevel, a dark outline and a white rim, one colour per tier.
- **Rendering:** Smooth metallic gradients with a diagonal sheen, embossed line art for the pig and the house; lettering has a two-tone vertical gradient and a hard drop outline.
- **Colour:** Gold #fae172 (22%) and orange #e5780c (14%) for the coin; tier colours on the words: red GRAND and SUPER, blue MAJOR, green MINOR, magenta MINI, white-blue ULTRA, purple WHEEL, orange JACKPOT. Warm 81%, high contrast (0.73).
- **Lighting:** Top-lit metal with a separate sparkle and a sweep 'shine' strip that the rig can pass across the face.
- **Ambience:** Cash-prize bright: the coin is the reward marker.
- **Materials:** Polished gold, enamel lettering.
- **Variants:** One coin, many labels: seven tier words, a JACKPOT or PREMIO second line (English and Spanish), x2 tags in the Mini and Minor colours, and a wheel face.
- **Motion:** 19 animations: one per label at 3.33 s, each with an '_h' twin (inference: a highlighted or held state), a 1.33 s particle_coin and a 1.00 s counter glow. The front, back and two edge pieces say the coin turns over (inference). Not seen in play.
- **Construction:** Spine 4.1.24, 22 bones, 23 slots, 24 parts on one page, no meshes, 8 additive slots. The coin faces are 320x320; the words 299x135.
- **Notes:** Tier colour is consistent everywhere this capture shows a tier: the coin words, the jackpot titles on the reel board and the wheel wedges use the same red, blue, green and magenta.
- **Skeleton (from the file):** Spine 4.1.24 · 22 bones · 23 slots · animations: fs_counter_glow_anim (0 s), jackpot_grand (0 s), jackpot_grand_h (0 s), jackpot_major (0 s), jackpot_major_h (0 s), jackpot_mini (0 s), jackpot_mini_h (0 s), jackpot_mini_h_multiplier (0 s), jackpot_minor (0 s), jackpot_minor_h (0 s), jackpot_minor_h_multiplier (0 s), jackpot_super (0 s), jackpot_super_h (0 s), jackpot_super_wheel (0 s), jackpot_ultra (0 s), jackpot_ultra_h (0 s), jackpot_ultra_wheel (0 s), jackpot_wheel (0 s), particle_coin (0 s)
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 57% · saturation 60% · contrast 72% · warm 81% / cool 9% · brighter towards: top (3)
- **Palette (measured):** #fae172 gold 22%, #e5780c orange 14%, #f9f6f0 light orange 12%, #120304 black 10%, #f2b631 orange 7%, #d8d2c6 light orange 4%

### Wolf symbol (skeleton)

`sym00` · atlas · 13 parts · largest 572×572 · sheet `sheets/sym00.webp`

- **Role:** The animated version of the wolf reel symbol; its one animation is named 'win'.
- **Subject:** The wolf's head and shoulders in a thin gold-to-orange frame, eyes closed in a grin on the head part, with separate eye strips (open and half shut), a starry night sky in two layers, a full moon with a glow, a grass silhouette, and a black howling-wolf silhouette with a cyan outline.
- **Style:** The same cartoon wolf as the still: angular muzzle, large ears, heavy brows, a sly smile. The howling silhouette is a flat graphic shape, a different register used for the win beat.
- **Rendering:** Painted with soft gradients and a darker outline on the fur; the moon is painted with crater texture and a wide soft halo; the sky is a smooth blue gradient with sharp four-point stars.
- **Colour:** Cool: 75% of the measured colour is cool. Dark blue #041c6f (24%), fur blue-violet #51528b (18%), bright blue #023dc0 (14%), with the moon's pale yellow #fcfce6 and #fbf9a6 (20% together) as the only warm.
- **Lighting:** Moonlight: the moon and its glow are the light source in the picture, the outline glow is cyan, and the fur takes a cool front light.
- **Ambience:** Night-time menace played for fun: the villain gets a howl at the moon.
- **Materials:** Fur, a painted night sky, a cratered moon, a glowing outline.
- **Variants:** One version. The still in the symbols sheet (sym_wolf) is the resting picture.
- **Motion:** One animation, 'win', 1.46 s (measured from the skeleton file). From the parts, inference: the framed head gives way to the moon scene, with the howling silhouette, the two sky layers, the star and the blinking eyes brought in by the rig. Not seen in play; no frame of this skeleton is shown because the project's skeleton drawing does not read Spine 4.1 correctly.
- **Construction:** Spine 4.1.24 skeleton, 21 bones, 12 slots, 13 parts on one 572 px-wide page, one mesh and two additive slots (inference: the glow and the moon glow). Every part is stored at the full cell width (572 px), so layers register without offsets.
- **Notes:** A whole second picture (moon, sky, silhouette) is hidden inside one symbol for its win; that is where this client spends animation budget on a low-count rig.
- **Skeleton (from the file):** Spine 4.1.24 · 21 bones · 12 slots · animations: win (0 s)
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged, strong highlights · brightness 41% · saturation 61% · contrast 39% · warm 24% / cool 75% · brighter towards: bottom (4), top (2), top-left (1)
- **Palette (measured):** #041c6f dark blue 24%, #51528b blue 18%, #fcfce6 light gold 14%, #023dc0 blue 14%, #060a12 black 9%, #fbf9a6 light gold 6%

### The four houses (skeleton)

`houses` · atlas · 169 parts · largest 550×480 · sheet `sheets/houses.webp`

- **Role:** The house that stands in a reel cell during the Mansions and Palaces features (inference from the feature names and the paytable): straw, stick, brick and mansion, each with a frame, a backing, a build, a loop and a blow-away.
- **Subject:** Four houses, each also taken apart: the straw hut as roof, wall and door; the log cabin as roof, four wall courses, door and windows; the brick house as roof, wall sections, door, door frame and three rows of windows; the mansion as floors. Four cell frames (rough orange sticks, twisted straw rope with blue ties, gold brick, blue jewelled) each with its own tile backing (wood grain, woven straw, gold brick, violet cobble), thin pulse outlines, and blow-away frames in which each house breaks up: straw scatters in flames of yellow, logs spin apart, bricks fly, the palace is knocked over in a dust cloud.
- **Style:** Doll's-house fronts with a white or coloured glow outline; each material is exaggerated so the four read apart at a glance: shaggy yellow straw, orange logs with a blue door, red brick with white gables and lit windows, pale violet stone with domes and gold.
- **Rendering:** Smooth painting with crisp outlines; the blow-away frames are hand-drawn with motion smears and debris.
- **Colour:** Warm 70%: dark red #4f0f10 (14%) and brick red #932a16 (11%), straw and log tones #eedca7, #b7a487 (14%), with the mansion's dark blue #221a56 as the cool pole. Contrast 0.65.
- **Lighting:** Top light, with warm lit windows on the brick house and the mansion and a glow outline around every house.
- **Ambience:** The fairy tale itself: build it up, blow it down.
- **Materials:** Straw, logs, brick, stone, gold, cut gems.
- **Variants:** Four tiers of one design: house, frame, backing and pulse outline each exist once per material.
- **Motion:** 14 animations, the same four per house, measured from the file: build 1.21 s, in 1.29 s, loop 1.04 s (brick and mansion), out 1.04 s. The 'build' assembles the house from its parts (inference from the separate roof, wall and window pieces). The 'out' is a drawn frame sequence: straw 22 frames, stick 22, brick 18, palace 24, with a 7-frame poof. Not seen in play.
- **Construction:** Spine 4.1.24, 78 bones, 73 slots, 169 parts over four pages, no meshes, 5 additive slots. Frames, backings and house parts all sit on one 360x360 canvas, so one rig serves four houses.
- **Notes:** A build animation made of real parts and a destroy animation made of drawn frames: rigging where the motion is mechanical, drawing where it is chaotic.
- **Skeleton (from the file):** Spine 4.1.24 · 78 bones · 73 slots · animations: brick_build (0 s), brick_in (0 s), brick_loop (0 s), brick_out (0 s), mansion_build (0 s), mansion_in (0 s), mansion_loop (0 s), mansion_out (0 s), stick_build (0 s), stick_in (0 s), stick_out (0 s), straw_build (0 s), straw_in (0 s), straw_out (0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 42% · saturation 66% · contrast 64% · warm 70% / cool 27% · brighter towards: top (16), right (4), bottom (3)
- **Palette (measured):** #4f0f10 dark red 14%, #932a16 red 11%, #eedca7 light orange 8%, #b7a487 orange 6%, #8b6959 orange 4%, #221a56 dark blue 4%

### Reel symbols (stills)

`symbols` · atlas · 18 parts · largest 336×286 · sheet `sheets/symbols.webp`

- **Role:** The still picture of every reel symbol, 18 in one sheet. The real screens show eleven of them on the reels (tape measure, toolbox, the three pigs, the hard hat, K, J, A and Q, with the boss pig and worker pig in two frames), each in a cell of about 135 px at 1280x720, on a see-through dark window. The saws, the wolf, the double and triple hats, 9 and 10 were not on a screen.
- **Subject:** Three circular saws (sym_woodcutter in orange, sym_woodcutter_diamond in blue with a gem-set blade, sym_super_woodcutter in gold), a gold hard hat with a pig badge alone, in twos and in threes, the wolf in a gold frame, three pigs (a boss in a suit holding a hammer, a worker in blue cap and overalls, a piglet in a green cap lying on straw), a tape measure, a toolbox, and six royals: 9, 10, J, Q, K, A.
- **Style:** Cartoon building-site take on the Three Little Pigs. Pigs and wolf are drawn as rounded mascots with large heads and clear expressions; tools are chunky and simplified; royals are heavy serif letters, each with one small ornament (a crown on Q and K, a shield on J, a gem on A).
- **Rendering:** Smooth digital painting with soft airbrushed gradients, a thin dark outline on the pigs and tools and a light rim around most pictures so they lift off the dark backing. Detail sits in the faces, the saw teeth and the hat badge. The hats and saws carry a square patterned backing inside the cell; pigs, tools and royals are cut to their silhouette.
- **Colour:** Measured over the sheet: gold and orange lead (#efb81d 18%, #d66a0b 9%), then the wolf's blue (#51568b 8%) and the royals' dark green (#1a6348 8%), pig skin (#f5bca2 7%). All six royals are one emerald green with a silver-blue rim, so value in this set is carried by subject and by gold, not by letter colour. Vivid (saturation 66%), high contrast (0.78).
- **Lighting:** Top light on most pieces, with hot white highlights on the hats and saw housings and an orange glow behind the feature symbols. The wolf is lit cool from the front against a deep blue night.
- **Ambience:** Bright, friendly and busy: a children's-story cast on a work site, with the gold hats and saws shouting loudest.
- **Materials:** Glossy moulded plastic for the hard hats, brushed steel and gem-set steel for the blades, painted wood for the toolbox, soft matte skin and cloth for the pigs, fur in broad locks for the wolf, enamelled metal for the royals.
- **Variants:** The saw exists in three grades (orange, diamond blue, gold) and the hat in three counts (one, two, three), each a separate picture. The three pigs are three ranks, named high, mid and low by the files.
- **Motion:** None in this unit: these are stills. The hat, the saws and the wolf have skeletons of their own (sym12-13, sym00). The client ships no skeleton for the pigs, tools or royals; how they show a win was not seen (no win came up in the one spin).
- **Construction:** One 'Red 7 Exporter' sprite sheet on one page, 18 frames from 159x174 (the 9) to 336x286 (the saw), each trimmed and stored with its untrimmed size (290 to 316 px square), so a cell is about 300 px at the shipped desktop size.
- **Notes:** The premium tier is told apart from the royals by three things at once: gold, a glowing square backing, and size. The base-game screens confirm it: the hard hat fills and overflows its cell with an orange glow, while K and J sit small in theirs.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 51% · saturation 66% · contrast 78% · warm 60% / cool 32% · brighter towards: top (5), bottom (3), top-right (2)
- **Palette (measured):** #efb81d orange 18%, #d66a0b orange 9%, #51568b blue 8%, #1a6348 dark green 8%, #f5bca2 light orange 7%, #ebefee light green 5%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The wolf and the hedge gate (skeleton)

`wolf` · atlas · 81 parts · largest 879×820 · sheet `sheets/wolf.webp`

- **Role:** The game's character: the wolf who appears over a garden hedge and gate, pops up, and blows. The same file holds the hedge and gate he appears behind. In the base-game screens only his tail is seen, swishing up from below the reels in front of the bottom row.
- **Subject:** A blue-violet wolf built from a head in many drawn angles and expressions (calm, sly, eyes shut, mouth open with teeth), a body, a neck ruff, a tail, clawed paws in four poses, eye strips, eyeballs, irises and a licking tongue; plus a dark red plank gate with iron fittings (a green version too), gate posts, a handle, hinges and lock, tall clipped hedges with bright lime tops, and thin white 'air' streaks for his breath.
- **Style:** Family-animation villain: a long angular muzzle, big pointed ears, heavy brows over small pale-blue eyes, a white chest ruff. More comic than frightening. The hedge and gate match the background painting's rounded storybook garden.
- **Rendering:** Flat-leaning painting with soft shading and a darker outline of the same hue around each fur shape; the head is redrawn rather than deformed for its turn. Hedges are painted with a leafy lit top edge fading to a flat dark blue below.
- **Colour:** Cool against one warm accent: dark blue #13233a (22%), fur blue-violet #56558c (20%), pale ruff #c4c4d8 (16%), the gate's dark red #59170f (16%), hedge greens #689327 and #1c6508 (16% together). The tongue is the only pink.
- **Lighting:** Soft, even night light with no strong key on the wolf; the hedge tops are lit lime as if by the garden lamps of the background (inference).
- **Ambience:** Mischief at night: the villain peeking over the garden gate of the pigs' mansion.
- **Materials:** Fur in broad locks, painted plank wood with black iron, clipped hedge, breath as white streaks.
- **Variants:** The gate ships in dark red and in green. Many animations exist twice, for landscape and portrait, and several are marked 'backup' or 'precog' by their authors.
- **Motion:** 34 animations, measured from the file: pop up in 3.08 s, a 6.83 s pop-up loop, out in 1.38 s; blow in 1.50 s, a 4.17 s blow loop, out in 0.92 s; a 5.04 s 'blow reveal'; tail swishes of 1.33 s. The real screens confirm the tail: it shows at a different place along the bottom of the reels in four of the frames and is absent in others. The head turn is a 19-frame drawn sequence, the lick 25 frames, blinks 3, paws and the raised head 4 each, so the body is rigged and the face is frame animation. The pop-up and the blow were not seen in play, and no frame of the rig is drawn here: the project's skeleton drawing does not read Spine 4.1 correctly.
- **Construction:** Spine 4.1.24, 27 bones, 42 slots, 81 parts over three pages, two meshes, no additive slots. The largest part is the gate at 879x820; the head frames are about 400 to 540 px.
- **Notes:** The villain is kept present in the base game by a tail alone, a cheap and funny idle. A second wolf rig carries the big win (unit newbigwin).
- **Skeleton (from the file):** Spine 4.1.24 · 27 bones · 42 slots · animations: bkg_landscape (0 s), bkg_landscape_FG (0 s), blow_in_landscape (0 s), blow_in_portrait (0 s), blow_loop_landscape (0 s), blow_loop_portrait (0 s), blow_loop_portrait_bkg (0 s), blow_loop_portrait_origional_backup (0 s), blow_out_landscape (0 s), blow_out_portrait (0 s), blow_reveal_blow_portrait (0 s), blow_reveal_landscape (0 s), blow_reveal_landscape_BG_precog (0 s), blow_reveal_landscape_BG_precog_origional_backup (0 s), blow_reveal_portrait (0 s), blow_reveal_portrait_origional_backup_v01 (0 s), blow_reveal_portrait_origional_backup_V02 (0 s), popup_in_landscape (0 s), popup_in_landscape_BG (0 s), popup_in_portrait (0 s), popup_loop_landscape (0 s), popup_loop_landscape_BG (0 s), popup_loop_portrait (0 s), popup_out_landscape (0 s), popup_out_landscape_BG (0 s), popup_out_landscape_BG_precog (0 s), popup_out_portrait (0 s), tail_left (0 s), tail_left_backup (0 s), tail_loop (0 s), tail_portrait_bkg (0 s), tail_right (0 s), tail_right_backup (0 s), tail_right_portrait_backup (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 36% · saturation 58% · contrast 50% · warm 19% / cool 68% · brighter towards: bottom-left (12), bottom (10), top (8)
- **Palette (measured):** #13233a dark blue 22%, #56558c blue 20%, #c4c4d8 light blue 16%, #59170f dark red 16%, #689327 green 8%, #1c6508 dark green 8%


## Logo and title

The game's own wordmark.

### Logo and loading screen art

`loading` · atlas · 12 parts · largest 878×578 · sheet `sheets/loading.webp`

- **Role:** The game logo and the pictures the loading screen rotates through: the wheel, the Ultra wheel drum and a sample of the reels. The real screens show the loading screen, and the same logo small in the top right corner of the base game.
- **Subject:** The logo: HUFF in yellow riveted plank letters, N' as a small nail-studded sign, EVEN MORE in red, PUFF in glossy blue bubble letters, GRAND in blue-white chrome with a purple base, on a cluster of soap bubbles. A half wheel of prize wedges behind a hedge, in a silver and a gold version; a wooden drum showing ULTRA JACKPOT between gold arrows; a 5x3 reel sample full of gold hats; the Light & Wonder mark and the load bar.
- **Style:** A stacked, toy-like wordmark in which each word takes the material of its meaning: wood for HUFF, breath bubbles for PUFF, jewel chrome for GRAND.
- **Rendering:** Heavily bevelled 3D-look lettering with gloss highlights, drop shadows and outlines; the wheel and drum are painted to look like physical fairground props.
- **Colour:** Mixed warm and cool, high contrast (0.66): yellow, red and blue letters on pale blue-grey bubbles; the wheel wedges run through red, orange, blue, purple and green.
- **Lighting:** Top-lit gloss on every letter; the gold wheel has a warm inner glow.
- **Ambience:** Loud, cheerful and physical: a toy sign and a fairground wheel.
- **Materials:** Painted wood with rivets, glossy plastic, soap bubbles, chrome set with small lights, varnished wood and brass for the drum.
- **Variants:** Each feature picture ships in English and Spanish (_EN and _SP; 'ULTRA PREMIO'). The wheel ships silver (SW) and gold (GW).
- **Motion:** None in the sheet; the loading screen swaps the pictures and their captions, as the two screens show.
- **Construction:** One 'Red 7 Exporter' sheet over two pages, 12 frames; the logo is 750x471, the wheel pictures 878x578.
- **Notes:** The logo is the only place the run shows the game's name as art. The Light & Wonder mark and load bar in this sheet are the provider's.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 34% · saturation 61% · contrast 66% · warm 55% / cool 31% · brighter towards: top (4), top-right (2), left (1)
- **Palette (measured):** #191c11 black 23%, #23632b dark green 13%, #56251b dark red 11%, #f4f5f6 light cyan 2%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Big win: the wolf blows the houses down (skeleton)

`newbigwin` · atlas · 108 parts · largest 688×688 · sheet `sheets/newbigwin.webp`

- **Role:** The big win celebration, in four tiers (the animations are named tier_4 to tier_7). Not seen in play.
- **Subject:** A second copy of the wolf (head in several drawn angles, body, eye strips, a dark silhouette version with glowing blue eyes) behind the hedge and gate; the four houses whole and in their blow-away frames (straw in flames of scattered stalks, logs flying, bricks bursting, the palace toppling in dust); a gold buzz saw with its guard; green star flares, rays and a pulse ring; a pine tree, a bush, a hill; speed lines, wood chips and breath streaks.
- **Style:** The game's cartoon at its most theatrical: a small stage set on a hill with the houses as targets.
- **Rendering:** Painted parts with outlines, drawn destruction frames, soft green glow shapes.
- **Colour:** Mixed, 52% cool: dark blue #16192c (19%), wolf blue #54538c (17%), dark red #691510 (14%), dark green #2b5e2f (13%). Green light is new here: the star, ray and pulse are lime.
- **Lighting:** Glow shapes behind the scene; the wolf silhouette is back-lit with only its eyes showing.
- **Ambience:** The story's climax used as the reward: the bigger the win, the better the house he blows down (inference from the four tiers and four houses).
- **Materials:** Fur, straw, logs, brick, stone, steel, light.
- **Variants:** Four tiers, each with landscape and portrait versions.
- **Motion:** 23 animations, measured: tier ins of 0.42, 0.71, 1.08 and 3.08 s, growing with the tier, and loops of 2.08 s (tier 6) and 4.17 s (tier 7); an 'effect' of 0.83 s with a 1.25 s loop. Drawn sequences: each house's destruction in 9 to 10 frames, speed lines 12, wood chips 11, head 5, blink 3.
- **Construction:** Spine 4.1.24, 64 bones, 72 slots, 108 parts over two pages, no meshes, 8 additive slots. It reuses the wolf, the houses and the saw from their own rigs at smaller size.
- **Notes:** The big win is built from the game's existing cast rather than a generic coin shower, so the celebration tells the story.
- **Skeleton (from the file):** Spine 4.1.24 · 64 bones · 72 slots · animations: effect (0 s), effectloop (0 s), sym13_win_gold (0 s), tier_4_in_landscape (0 s), tier_4_in_portrait (0 s), tier_4_loop_landscape (0 s), tier_4_loop_portrait (0 s), tier_5_in_landscape (0 s), tier_5_in_portrait (0 s), tier_5_loop_landscape (0 s), tier_5_loop_portrait (0 s), tier_6_in_landscape (0 s), tier_6_in_portrait (0 s), tier_6_in_portrait2 (0 s), tier_6_loop_landscape (0 s), tier_6_loop_portrait (0 s), tier_6_loop_portrait2 (0 s), tier_7_in_landscape (0 s), tier_7_in_portrait (0 s), tier_7_in_portrait2 (0 s), tier_7_loop_landscape (0 s), tier_7_loop_portrait (0 s), tier_7_loop_portrait2 (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast · brightness 37% · saturation 60% · contrast 45% · warm 38% / cool 52% · brighter towards: top (12), bottom (8), bottom-left (7)
- **Palette (measured):** #16192c dark blue 19%, #54538c blue 17%, #691510 dark red 14%, #2b5e2f dark green 13%, #c5c5d7 light blue 7%, #b9a987 orange 3%

### Feature intro panels (skeleton)

`fs_panels` · atlas · 123 parts · largest 1148×720 · sheet `sheets/fs_panels.webp`

- **Role:** The banner that announces a feature: Buzz Saw, Mega Hat, Mansions, Palaces and the Wheel, each in plain, Super and Ultra grades.
- **Subject:** A rounded striped plate per feature (blue stripes for Buzz Saw, red for Mansions, yellow hazard stripes for Mega Hat, purple for Ultra Palace, a gold diamond road sign for the Wheel), the feature's object (gold hat, saw, brick mansion, violet palace), and its words as separate pieces: MEGA HAT FEATURE, SUPER BUZZ SAW FEATURE, ULTRA MEGA MANSIONS FEATURE, WHEEL FEATURE and so on; plus soft blurred backings, thin outline glows, white brush swirls, cyan sparkle dots and a purple 'palaces unlocked' bar.
- **Style:** Building-site signage: hazard stripes and a road-sign diamond, with the same fat outlined lettering as the jackpot words.
- **Rendering:** Flat glossy plates with a diagonal sheen; lettering with a vertical two-tone gradient and outline; swirls drawn as dry-brush strokes.
- **Colour:** Mixed: black #070608 (16%) and greys from the stripes and swirls, orange #d66c0b (12%), gold #edba1e (9%). Grade is colour-coded in the words: magenta SUPER, white or red ULTRA.
- **Lighting:** Top-left sheen on the plates; outline glows and a yellow sheen strip as separate emissive pieces.
- **Ambience:** A quick, punchy announcement.
- **Materials:** Painted metal sign plates, gold, brush-stroke air.
- **Variants:** Eleven feature intros from one rig by swapping plate, object and words; the wheel intro in plain, Super and Ultra, each for landscape and portrait with a loop.
- **Motion:** 23 animations, measured: every feature intro 1.83 s; wheel intros 1.88 s with 1.46 s loops. Frame sequences: sparkle particles (37 frames) and two brush swirls (26 and 20). Not seen in play.
- **Construction:** Spine 4.1.24, 18 bones, 20 slots, 123 parts over 10 pages, 4 meshes, 3 additive slots. Plates, objects and words are all stored on one 1148x720 canvas so they register without offsets.
- **Notes:** One rig, eleven banners: the lesson is the shared canvas and the split into plate, object and words. The same plates and words appear on the rolling sign in the base-game screens.
- **Skeleton (from the file):** Spine 4.1.24 · 18 bones · 20 slots · animations: buzzsaw_intro (0 s), buzzsaw_super_intro (0 s), hat_ultra_intro (0 s), mansions_intro (0 s), mansions_super_intro (0 s), mansions_ultra_intro (0 s), mansions_ultra_mega_intro (0 s), megahat_intro (0 s), megahat_super_intro (0 s), megahat_ultra_intro (0 s), palace_intro (0 s), wheel_intro_landscape (0 s), wheel_intro_landscape_loop (0 s), wheel_intro_portrait (0 s), wheel_intro_portrait_loop (0 s), wheel_intro_super_landscape (0 s), wheel_intro_super_landscape_loop (0 s), wheel_intro_super_portrait (0 s), wheel_intro_super_portrait_loop (0 s), wheel_intro_ultra_landscape (0 s), wheel_intro_ultra_landscape_loop (0 s), wheel_intro_ultra_portrait (0 s), wheel_intro_ultra_portrait_loop (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast · brightness 43% · saturation 54% · contrast 55% · warm 59% / cool 32% · brighter towards: top-left (6), bottom (1), top (1)
- **Palette (measured):** #070608 black 16%, #d66c0b orange 12%, #cecbc9 grey 12%, #edba1e gold 9%, #484145 grey 8%, #887b81 grey 6%

### Big win digit flare

`bigwin` · atlas · 24 parts · largest 468×182 · sheet `sheets/bigwin.webp`

- **Role:** Named fx_digits: inference, the flare behind the win amount in the big win.
- **Subject:** A horizontal burst of gold light with sparks, on a black field.
- **Style:** Lens-flare glare.
- **Rendering:** Photographic-looking glow frames on black, meant to be added to the picture.
- **Colour:** Gold only: #dcaf21 (26%), #f9ec64 (20%), browns #a9770f and #71490d, near-white core.
- **Lighting:** Emissive.
- **Ambience:** Jackpot glare.
- **Materials:** Light.
- **Variants:** One.
- **Motion:** 24 frames, one second at the exporter's stated 24 frames a second.
- **Construction:** One 'Red 7 Exporter' sheet on a single JPEG page, 468x182 a frame. JPEG with a black ground is the client's way to ship an additive effect cheaply.
- **Notes:** The only JPEG sprite sheet in the capture.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 62% · saturation 72% · contrast 63% · warm 100% / cool 0%
- **Palette (measured):** #dcaf21 gold 26%, #f9ec64 gold 20%, #a9770f brown 17%, #331f06 black 12%, #71490d brown 11%, #feffeb light gold 9%


## Effects

Frame sequences, glows, particles and transitions.

### Smoke puff and sparkle outro (skeleton)

`fg_outro` · atlas · 12 parts · largest 892×839 · sheet `sheets/fg_outro.webp`

- **Role:** Named 'fg_outro' with an animation 'wolf_smoke': inference from the names, the puff that ends a feature or covers the wolf's exit.
- **Subject:** Clusters of grey-beige cartoon smoke clouds that break up into small curls, and two fields of white sparkle dots.
- **Style:** Classic cartoon dust cloud: lumpy rounded blobs with a darker underside.
- **Rendering:** Flat two-tone shapes with clean edges; ten drawn frames.
- **Colour:** Two greys only: #a4a197 (78%) and #757269 (21%); saturation 8%.
- **Lighting:** A simple darker underside; no glow.
- **Ambience:** A comic 'poof'.
- **Materials:** Dust or smoke as flat shapes.
- **Variants:** One.
- **Motion:** Two animations: 'animation' 1.60 s and 'wolf_smoke' 0.43 s; the smoke is a 10-frame sequence that opens out and thins. Not seen in play.
- **Construction:** Spine 4.1.24, 5 bones, 73 slots, 12 parts over three pages, 36 additive slots. The star and dot fields carry the names of the mansion's particles (bigmansion_dot), so they are shared art.
- **Notes:** The only muted unit in the capture.
- **Skeleton (from the file):** Spine 4.1.24 · 5 bones · 73 slots · animations: animation (0 s), wolf_smoke (0 s)
- **Measured:** mid-tone, muted, neutral, low contrast · brightness 60% · saturation 8% · contrast 20% · warm 98% / cool 1%
- **Palette (measured):** #a4a197 grey 78%, #757269 grey 21%

### Wheel wedge upgrade glow (skeleton)

`superwheelfire` · atlas · 2 parts · largest 668×1170 · sheet `sheets/superwheelfire.webp`

- **Role:** The outline that lights a wheel wedge when it upgrades.
- **Subject:** A long wedge outline (668x1170) in yellow and in silver-blue.
- **Style:** A neon outline.
- **Rendering:** A hard bright line with a soft outer glow, on transparency.
- **Colour:** Yellow #ffff05 and pale cyan #b7dae3, half each.
- **Lighting:** Emissive only.
- **Ambience:** A flash of attention.
- **Materials:** Light.
- **Variants:** Gold and silver, matching the gold and silver wheels.
- **Motion:** Two animations of 1.87 s, one per colour (inference: a pulse). Not seen in play.
- **Construction:** Spine 4.1.24, 2 bones, 1 slot, 2 parts on one page.
- **Notes:** The same two glows are also in the basegame sheet.
- **Skeleton (from the file):** Spine 4.1.24 · 2 bones · 1 slots · animations: wheel_upgrade_glow_anim (0 s), wheel_upgrade_silver_glow_anim (0 s)
- **Measured:** bright, saturated, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 88% · saturation 59% · contrast 1% · warm 50% / cool 50%
- **Palette (measured):** #b7dae3 light cyan 50%, #ffff05 gold 50%

### Ultra wheel highlight (skeleton)

`ultrawheel_highlight` · atlas · 37 parts · largest 991×229 · sheet `sheets/ultrawheel_highlight.webp`

- **Role:** The highlight on the Ultra wheel's winning row and its arrow.
- **Subject:** A thin horizontal orange light bar with drifting sparks (34 frames), a wider soft glow, and a glowing chevron for the arrow.
- **Style:** Hot light streak.
- **Rendering:** Soft additive shapes: 87% of the edges are soft.
- **Colour:** Orange only: #fa6b05 (39%), #f5bf64 (37%), pale #fdf4da (12%).
- **Lighting:** Emissive.
- **Ambience:** Heat and anticipation on the selected prize.
- **Materials:** Light and sparks.
- **Variants:** One.
- **Motion:** Two animations of 0.97 s (highlight and arrow), driven by a 34-frame loop. The loading sheet's drum picture shows the result: an orange outline around the middle row with gold arrows either side.
- **Construction:** Spine 4.1.24, 16 bones, 18 slots, 37 parts on one page, 10 additive slots.
- **Notes:** Short and loopable: under a second.
- **Skeleton (from the file):** Spine 4.1.24 · 16 bones · 18 slots · animations: ultra_wheel_arrow_anim (0 s), ultra_wheel_highlight_anim (0 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 68% · saturation 71% · contrast 32% · warm 100% / cool 0%
- **Palette (measured):** #fa6b05 orange 39%, #f5bf64 orange 37%, #fdf4da light orange 12%, #f49c2e orange 8%, #fadda8 light orange 2%

### Caution-tape transition (skeleton)

`transition` · atlas · 5 parts · largest 2130×373 · sheet `sheets/transition.webp`

- **Role:** The wipe between scenes.
- **Subject:** Two lengths of yellow-and-black hazard tape (2130 and 1692 px long), a roll of yellow tape, a black cover and a four-point gold star.
- **Style:** Building-site caution tape, glossy and slightly curved.
- **Rendering:** Flat stripes with a soft highlight along the tape; the roll is a simple shaded cylinder.
- **Colour:** Black #050404 (37%) and yellows #edc332 and #fef876 (40%); contrast 0.80.
- **Lighting:** A single sheen along the tape.
- **Ambience:** On-theme and brisk.
- **Materials:** Plastic tape.
- **Variants:** Landscape and portrait animations.
- **Motion:** Two animations of 1.75 s. Inference from the parts and the two meshes: tapes are pulled across the screen from the roll while the black cover hides the change. Not seen in play.
- **Construction:** Spine 4.1.24, 25 bones, 18 slots, 5 parts on one page, 2 meshes (inference: the tapes, so they can bend), 1 additive slot.
- **Notes:** A whole scene change from five small parts.
- **Skeleton (from the file):** Spine 4.1.24 · 25 bones · 18 slots · animations: transition_landscape (0 s), transition_portrait (0 s)
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 44% · saturation 37% · contrast 80% · warm 84% / cool 0% · brighter towards: top-right (1)
- **Palette (measured):** #050404 black 37%, #edc332 gold 23%, #fef876 gold 17%, #3e3c36 grey 16%, #ffffb5 light gold 4%

### Gold brick frame loop

`house_frame_gold` · atlas · 25 parts · largest 286×289 · sheet `sheets/house_frame_gold.webp`

- **Role:** The looping shine on the brick house's cell frame (sequence houses-brick_loop).
- **Subject:** A square frame of gold bricks with corner bolts; a sparkle travels round it.
- **Style:** Jewellery-like gold blocks.
- **Rendering:** Hard-edged gold with sharp white glints; contrast 0.93.
- **Colour:** Gold #f9c918 (24%), #fdea80 (14%), orange #dd6d10 (14%), dark browns for the joints.
- **Lighting:** Moving specular glints.
- **Ambience:** Rich.
- **Materials:** Gold.
- **Variants:** The mansion's frame is the same idea in blue gems.
- **Motion:** 25 frames, about one second at 24 frames a second, matching the 1.04 s loop of the houses rig.
- **Construction:** One 'Red 7 Exporter' sheet, 25 frames of about 280 px on one page.
- **Notes:** A pre-rendered loop rather than a rigged shine.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 52% · saturation 81% · contrast 93% · warm 100% / cool 0%
- **Palette (measured):** #f9c918 gold 24%, #170502 black 15%, #fdea80 gold 14%, #dd6d10 orange 14%, #571a06 brown 11%, #a73808 brown 8%

### Jewelled mansion frame loop

`house_frame_mansion` · atlas · 25 parts · largest 316×295 · sheet `sheets/house_frame_mansion.webp`

- **Role:** The looping shine on the mansion's cell frame (sequence houses-mansion_loop).
- **Subject:** A square frame of deep blue metal set with round white-blue gems; glints pass over the gems.
- **Style:** Costume-jewel frame.
- **Rendering:** Hard-edged with bright white highlights; contrast 0.92.
- **Colour:** Blue only: #0d0e64 (20%), #262ea4 (14%), pale #e3eefc and #b2c3ef (35%).
- **Lighting:** Moving glints.
- **Ambience:** The top tier, cold and precious beside the warm lower houses.
- **Materials:** Enamelled metal and gems.
- **Variants:** See the gold frame.
- **Motion:** 25 frames, about one second.
- **Construction:** One 'Red 7 Exporter' sheet, 25 frames of 266 to 316 px on one page.
- **Notes:** Blue-white marks the top tier here as it does for Ultra and for the diamond saw.
- **Measured:** mid-tone, saturated, cool, high contrast, hard-edged, strong highlights · brightness 50% · saturation 50% · contrast 92% · warm 0% / cool 100%
- **Palette (measured):** #0d0e64 dark blue 20%, #e3eefc light blue 19%, #8595dc blue 16%, #b2c3ef light blue 16%, #262ea4 blue 14%, #5868be blue 13%

### Blow against the brick house

`windbrick_blow` · atlas · 83 parts · largest 936×539 · sheet `sheets/windbrick_blow.webp`

- **Role:** The long gust (sequence windbricks_blow); inference from the name: the blow that the brick house withstands or that builds up before the blast.
- **Subject:** White wind streaks that gather into a broad rotating swirl and die away.
- **Style:** Cartoon wind lines.
- **Rendering:** Pure white soft strokes on transparency.
- **Colour:** White only (#ffffff 100%).
- **Lighting:** None.
- **Ambience:** A long held breath.
- **Materials:** Air.
- **Variants:** One.
- **Motion:** 83 frames, about 3.5 s at 24 frames a second, the longest sequence in the capture.
- **Construction:** One 'Red 7 Exporter' sheet over twelve pages; frames up to 936x539.
- **Notes:** Twelve atlas pages for one white effect: the costliest single effect in the files.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Smoke particle

`freespins_particle` · atlas · 1 parts · largest 191×177 · sheet `sheets/freespins_particle.webp`

- **Role:** A single soft blob used by a particle system in free spins (name particle_smoke).
- **Subject:** One beige smoke puff.
- **Style:** Soft cartoon dust.
- **Rendering:** Fully soft-edged.
- **Colour:** Beige #b7ab85 (87%).
- **Lighting:** None.
- **Ambience:** Dust.
- **Materials:** Smoke.
- **Variants:** One.
- **Motion:** None in the file.
- **Construction:** One 191x177 picture.
- **Notes:** The same beige as the brick blast dust.
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect · brightness 64% · saturation 28% · contrast 19% · warm 100% / cool 0%
- **Palette (measured):** #b7ab85 yellow 87%, #867c59 yellow 13%

### The wolf's blow

`wind` · atlas · 34 parts · largest 942×525 · sheet `sheets/wind.webp`

- **Role:** The gust of the wolf's breath (sequence Blow).
- **Subject:** White curved wind streaks that grow into a wide swirl carrying yellow leaves or straw, then thin out.
- **Style:** Cartoon wind lines.
- **Rendering:** Soft white brush strokes, fully soft-edged.
- **Colour:** White #fffffc (72%) with yellow #fed904 (21%).
- **Lighting:** None; light strokes for adding over the scene.
- **Ambience:** Huff and puff.
- **Materials:** Air and flying straw.
- **Variants:** One; the brick versions are separate sheets.
- **Motion:** 34 frames, about 1.4 s at 24 frames a second. Not seen in play.
- **Construction:** One 'Red 7 Exporter' sheet over four pages; frames up to 942x525.
- **Notes:** The title's action is three hand-drawn sheets (wind, windbrick_blow, windbrick_blast): 137 frames in all.
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect, strong highlights · brightness 95% · saturation 25% · contrast 10% · warm 80% / cool 0%
- **Palette (measured):** #fffffc light gold 72%, #fed904 gold 21%, #fdf1a2 light gold 4%, #fce662 gold 3%

### Brick blast dust

`windbrick_blast` · atlas · 20 parts · largest 960×540 · sheet `sheets/windbrick_blast.webp`

- **Role:** The burst at the end of the blow (sequence windbricks_blast).
- **Subject:** A beige dust cloud that opens into scattered round puffs and debris.
- **Style:** Cartoon dust burst.
- **Rendering:** Soft two-tone shapes.
- **Colour:** Beige #b2a781 (94%).
- **Lighting:** A darker underside only.
- **Ambience:** Impact.
- **Materials:** Dust.
- **Variants:** One.
- **Motion:** 20 frames, under a second.
- **Construction:** One 'Red 7 Exporter' sheet over three pages; frames up to 960x540.
- **Notes:** Half-screen-sized frames.
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect · brightness 64% · saturation 28% · contrast 15% · warm 100% / cool 0% · brighter towards: bottom-left (1)
- **Palette (measured):** #b2a781 yellow 94%, #897f5d yellow 6%

### Big win particles

`bigwin_particles` · atlas · 4 parts · largest 161×133 · sheet `sheets/bigwin_particles.webp`

- **Role:** The objects thrown in the big win shower (inference from the name).
- **Subject:** Four small pictures: a gold pig coin, a gold bar, a hard hat with a red glow, and the diamond buzz saw.
- **Style:** The game's own symbols at particle size.
- **Rendering:** As the symbols, simplified.
- **Colour:** Gold #fcf39d, #f0c022, #f5d563 (47% together), orange #d86d0d, with the saw's pale blue.
- **Lighting:** Top-lit with gloss.
- **Ambience:** A shower of the game's own valuables.
- **Materials:** Gold, plastic, steel.
- **Variants:** Four particles.
- **Motion:** None in the sheet; a particle system moves them.
- **Construction:** One 'Red 7 Exporter' sheet, 4 frames of about 130 to 160 px.
- **Notes:** Themed particles instead of generic coins.
- **Measured:** bright, vivid, warm, high contrast, strong highlights · brightness 64% · saturation 65% · contrast 68% · warm 75% / cool 25% · brighter towards: top-right (1), bottom-right (1)
- **Palette (measured):** #fcf39d light gold 20%, #f0c022 gold 18%, #d86d0d orange 10%, #f5d563 gold 9%, #d1e0f4 light blue 6%, #fa2002 red 5%

### Wheel spin and clicker effects

`wheel_fx` · atlas · 47 parts · largest 1544×1544 · sheet `sheets/wheel_fx.webp`

- **Role:** Effects for the wheel: its rim, a shadow mask that leaves one wedge lit, the dust and fire of the spin and the sparks at the clicker.
- **Subject:** A thin silver ring and a thin gold ring (about 1540 px across), two black discs with one wedge cut out, a 31-frame arc of yellow fire and grey smoke, and a 12-frame spiky orange spark burst.
- **Style:** Cartoon impact effects: spiked star bursts and rolling flame with smoke puffs.
- **Rendering:** Hand-drawn frames with flat fills and a light glow; the rings are fine clean lines.
- **Colour:** Black #000000 (57%, the masks), then gold and orange #fab836, #baa677, pale #fcf68f.
- **Lighting:** Emissive fire and sparks; the mask darkens everything but the winning wedge.
- **Ambience:** Fairground friction: the wheel throws sparks.
- **Materials:** Fire, smoke, sparks, a metal rim.
- **Variants:** Silver and gold for both the ring and the mask.
- **Motion:** Two frame sequences: fx_spin, 31 frames, and fx_clicker, 12 frames. At the sheets' 24 frames a second (the exporter's stated rate) that is about 1.3 s and 0.5 s.
- **Construction:** One 'Red 7 Exporter' sheet over six pages, 47 frames; no skeleton.
- **Notes:** The dim-all-but-one mask is a single black sprite, not a shader.
- **Measured:** mid-tone, muted, warm and cool mixed, low contrast · brightness 31% · saturation 21% · contrast 14% · warm 40% / cool 3% · brighter towards: top (2), bottom (2), bottom-right (2)
- **Palette (measured):** #000000 black 57%, #baa677 orange 13%, #fab836 orange 10%, #fcf68f light gold 9%, #8d805d orange 2%, #fefeee light gold 2%

### Ultra wheel blast

`ultra_wheel_blast_particle` · atlas · 47 parts · largest 1031×661 · sheet `sheets/ultra_wheel_blast_particle.webp`

- **Role:** The flash when the Ultra wheel lands (inference from the name).
- **Subject:** A white rounded rectangle with a blue glow that breaks into a cloud of white sparkle points.
- **Style:** Clean light burst.
- **Rendering:** Soft glow frames: 85% of the edges are soft.
- **Colour:** Near-white #fbfefe (85%) with blue #2087fe (11%).
- **Lighting:** Emissive.
- **Ambience:** A cold bright flash against the warm wheel, which is what makes it read as the top prize.
- **Materials:** Light.
- **Variants:** One.
- **Motion:** One sequence of 47 frames, about 2 s at the exporter's 24 frames a second.
- **Construction:** One 'Red 7 Exporter' sheet over seven pages; the largest frame is 1031x661.
- **Notes:** The only cool-coloured effect in the capture; the Ultra tier is marked white-blue throughout.
- **Measured:** bright, muted, cool, low contrast, glow or soft effect, strong highlights · brightness 93% · saturation 12% · contrast 13% · warm 0% / cool 73%
- **Palette (measured):** #fbfefe light cyan 85%, #2087fe blue 11%, #a3ebfa light cyan 2%, #67bdfa blue 2%


## Game interface

Buttons, counters and panels drawn for this game.

### Wheel texture, Spanish

`WheelWegesCol_01_sp` · atlas · 1 parts · largest 1024×1024 · sheet `sheets/WheelWegesCol_01_sp.webp`

- **Role:** The same wheel texture with Spanish prize words, for the Spanish-language version of the game.
- **Subject:** The twelve plates of the English texture, with PREMIO replacing JACKPOT on the four jackpot plates; the feature plates keep their English words.
- **Style:** As the English texture.
- **Rendering:** As the English texture.
- **Colour:** Measured the same within a point: dark red #540d08 (28%), oranges #ec6a06 and #b6410a (19%), purple and blue plates.
- **Lighting:** As the English texture.
- **Ambience:** As the English texture.
- **Materials:** As the English texture.
- **Variants:** This is the variant; only four plates differ.
- **Motion:** None.
- **Construction:** One 1024x1024 JPEG for a second copy of the same glTF model (folder wheel3d_sp).
- **Notes:** Localisation is done by swapping whole textures and whole sprite frames, not by live text.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 27% · saturation 76% · contrast 60% · warm 75% / cool 22% · brighter towards: top (1)
- **Palette (measured):** #540d08 dark red 28%, #17111c black 13%, #b6410a brown 10%, #ec6a06 orange 9%, #3d3c7b blue 7%, #6d1695 purple 5%

### Wheel texture (3D model)

`WheelWegesCol_01` · atlas · 1 parts · largest 1024×1024 · sheet `sheets/WheelWegesCol_01.webp`

- **Role:** The colour texture of the 3D drum (a glTF model, wheel_blnd_V02). The real screens show the drum as the wooden sign above the wheel in the base game, rolling from one plate to the next.
- **Subject:** Twelve wedge faces as rectangular plates: ULTRA JACKPOT, MAJOR JACKPOT, GRAND JACKPOT, SUPER JACKPOT, and feature plates with a small picture each: Super Mega Hat, Ultra Mega Mansion, Ultra Palaces (twice), Super Buzz Saw (twice), Ultra Hat, Super Mansions. Beside them, stretched strips of orange varnished wood with rivets for the drum's body.
- **Style:** Sign-painting for a fairground drum: each plate has its own patterned ground (stripes, brick, diamond plate) and stacked two-colour lettering.
- **Rendering:** Flat painted plates with bevelled, outlined lettering and small symbol pictures; the wood is a painted grain texture meant to wrap a cylinder.
- **Colour:** Dark and warm: dark red #540d08 (28%), orange wood #ec6a06 and #b74009 (18%), with purple #6d1695 and blue #3d3c7b plates. Saturation 76%.
- **Lighting:** Baked into the paint: a centre glow on each plate. Any further light comes from the 3D drawing in the client, not seen in this run.
- **Ambience:** Fairground prize wheel.
- **Materials:** Varnished wood, painted metal plates.
- **Variants:** A Spanish twin (WheelWegesCol_01_sp) with PREMIO in place of JACKPOT.
- **Motion:** None in the texture; the model turns. In the real frames the sign shows a different plate each time (SUPER MANSIONS FEATURE, ULTRA PALACES FEATURE, SUPER BUZZ SAW, MAJOR JACKPOT, ULTRA MEGA MANSION), sometimes caught between two, so it rolls continuously in the base game.
- **Construction:** One 1024x1024 JPEG mapped onto a glTF model with three meshes. On screen the drum sits in a wooden frame with gold arrow pointers at both sides, top centre.
- **Notes:** A real 3D drum is unusual among the games read so far: it gives true perspective and a continuous roll for the cost of one small texture.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 27% · saturation 76% · contrast 60% · warm 75% / cool 22% · brighter towards: top (1)
- **Palette (measured):** #540d08 dark red 28%, #17111c black 13%, #b74009 brown 9%, #ec6a06 orange 9%, #3d3c7b blue 7%, #6d1695 purple 5%

### Buy Pass panel and button

`buypass` · atlas · 24 parts · largest 1264×906 · sheet `sheets/buypass.webp`

- **Role:** The feature-buy dialog and its button. The real screens show the blue BUY PASS button at the left under the jackpot plaques; the panel was not opened.
- **Subject:** A full-screen panel picture (a dimmed, green-framed view of the mansion avenue with a title bar), a dark brown inner panel, a thumbnail of the reels in a silver frame, red No and green Yes buttons, orange minus and plus buttons with a glass sheen, black digit screens, a green cross, and the square BUY PASS button in blue with a gold rim.
- **Style:** Standard glossy casino dialog furniture; only the panel background carries the game's scene.
- **Rendering:** Flat fills with gloss highlights and thin rims; every button in four states.
- **Colour:** Dark overall (brightness 0.18): near-black green #161b10 (73%) from the panel, with green, red and orange buttons.
- **Lighting:** Top gloss on every button.
- **Ambience:** Functional.
- **Materials:** Glossy plastic and glass.
- **Variants:** Base, hover, down and disabled states for each button.
- **Motion:** None in the sheet.
- **Construction:** One 'Red 7 Exporter' sheet of 23 frames on one page, plus the button picture from the provider's shared folder (the two share a name, so they form one unit here).
- **Notes:** The orange plus and minus buttons and the red and green pair are generic; inference: they are the provider's stock dialog set, reskinned only by the background.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 18% · saturation 70% · contrast 30% · warm 37% / cool 34% · brighter towards: top (17), top-left (4)
- **Palette (measured):** #161b10 black 73%, #235820 dark green 9%, #5e2615 dark red 4%, #e67b0e orange 3%

### Prize wheel wedges and clickers

`wheel_with_text` · atlas · 21 parts · largest 549×1059 · sheet `sheets/wheel_with_text.webp`

- **Role:** The wedges of the two-ring prize wheel and its pointers. The real screens show the wheel behind the reels in the base game: a large outer ring with a silver-blue rim and a smaller inner ring with a gold rim, both turning.
- **Subject:** Long triangular wedges, each a coloured field with its prize lettered across the wide end: GRAND, MAJOR, MINOR, MINI and SUPER JACKPOT, BUZZ SAW, MEGA HAT and MANSIONS features with their Super versions, and UPGRADE in gold and in diamond blue; empty wedge frames in gold and silver; a gold and a silver clicker (a shield-shaped pointer) with their base plates.
- **Style:** Fairground wheel: saturated wedges with patterned fields (hazard stripes for Super Jackpot, diamond plate for Upgrade) and the game's fat outlined lettering.
- **Rendering:** Flat painted fields with a centre glow and a darker tip; bevelled metal for the clickers.
- **Colour:** Vivid (saturation 75%) and high in contrast (0.72): dark red #3d0b0c (12%), orange #e17218 (8%), red #c23613 (7%), with purple, blue, green and magenta wedges in the tier colours.
- **Lighting:** Baked glow at the wide end of each wedge; top-lit chrome and gold on the clickers.
- **Ambience:** The fair's prize wheel, always turning behind the game.
- **Materials:** Painted panels, chrome and gold.
- **Variants:** Names ending _g belong to the gold wheel and _s to the silver one. A Spanish set of the same sheet exists in the client and was left out of the run.
- **Motion:** None in the sheet. In the real frames both rings stand at a different angle each time, so the wheel turns slowly through the base game; its feature spin was not seen.
- **Construction:** One 'Red 7 Exporter' sheet over six pages, 21 frames, wedges about 548x1059. The wheel is assembled from wedges at run time, so its layout is data.
- **Notes:** Showing the bonus wheel permanently, half hidden behind see-through reels, keeps the top prizes in view on every spin. It is the most distinctive layout decision in this game.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 39% · saturation 75% · contrast 72% · warm 58% / cool 32% · brighter towards: top (13), bottom (2)
- **Palette (measured):** #3d0b0c dark red 12%, #e17218 orange 8%, #c23613 red 7%, #8a150a dark red 6%, #4d0d55 dark magenta 5%, #0d4a80 dark blue 4%

### Paytable pictures

`paytable` · atlas · 46 parts · largest 586×323 · sheet `sheets/paytable.webp`

- **Role:** The pictures the paytable pages use: the four houses, the house frames, the finished jackpot coins, the block symbols, the wheel and the drum. The paytable itself was not opened in play.
- **Subject:** Four houses in rising order: a straw hut, a log cabin (stick), a red brick house and the violet mansion; four matching cell frames (stick, brick, straw rope, and a blue jewelled mansion frame); Mega Hat and Mega Mansion blocks in 2x2, 3x3 and 3x5; the wheel and the Ultra drum; the full set of jackpot coins in English and Spanish; the saws and hats again; a loading ring and a turbo switch.
- **Style:** Same glossy cartoon as the symbols. Each house is a small front view with a white glow outline, its material exaggerated: shaggy straw, orange logs, red brick with white trim, pale violet stone with gold.
- **Rendering:** Smooth painting with crisp outlines and a pale rim; coins have a studded edge and a coloured halo per tier.
- **Colour:** Warm and high in contrast (0.80): red #952418 (17%), gold #efba23 (13%), pale gold #f5efde and #f9e989 (17%), orange #d66514 (8%), dark magenta #4d122c (7%). Each tier's halo repeats its word colour: magenta Mini, green Minor, blue Major, red Grand.
- **Lighting:** Top light with lit windows on the brick house and the mansion.
- **Ambience:** A prize catalogue: everything gold-rimmed and glowing.
- **Materials:** Straw, logs, brick, stone, gold coin, plastic hat, steel blade.
- **Variants:** English and Spanish versions of every worded coin and of the wheel; block pictures in three sizes.
- **Motion:** None; these are stills. The animated houses are the unit 'houses'.
- **Construction:** One 'Red 7 Exporter' sheet over two pages, 46 frames, most about 300 px.
- **Notes:** The house ladder (straw, stick, brick, mansion) is the game's progression told as four materials; the frames repeat it, so a cell's border alone says which house it holds.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 49% · saturation 67% · contrast 80% · warm 81% / cool 13% · brighter towards: bottom (3), top (3), top-left (1)
- **Palette (measured):** #952418 red 17%, #efba23 orange 13%, #f5efde light gold 9%, #f9e989 light gold 8%, #d66514 orange 8%, #4d122c dark magenta 7%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `notosans`: 12 parts
- `check`: 1 parts
- `lnw_logo`: 1 parts
- `no_check`: 1 parts
- `progressbar_ninepatch`: 1 parts
- `ui_icon_replay`: 1 parts
- `info`: 1 parts
- `autospins`: 1 parts
- `autospinsrectangle`: 1 parts
- `buypassclicked`: 1 parts
- `buypassdisabled`: 1 parts
- `buypasshover`: 1 parts
- `turbohover`: 1 parts
- `turboon`: 1 parts
- `eclipse`: 1 parts
- `eclipse_glow`: 1 parts
- `swedish_depositlimit_icon`: 1 parts
- `swedish_selfassessment_icon`: 1 parts
- `swedish_selfexclusion_icon`: 1 parts
- `betautoplayswitchbuttons`: 8 parts
- `settings-menu`: 8 parts
- `basegameui`: 56 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Frutiger Neue LT Pro (Medium); Noto Sans (Regular); icomoon (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1535 components cut from 140 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
