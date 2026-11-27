# Huff N Puff Money Mansion: art report

lnw · run `2026-11-27-0457-lnw-huff-n-puff-money-mansion` · captured 2026-11-27

Source: the provider's free-play demo, https://ogs-gl-usnj.nyxop.net/game/?nogsoperatorid=386&nogsgameid=71743&nogsmode=demo&nogslang=EN_EN&nogscurrency=USD&clienttype=flash

**Extracted:** 3579 named components from 349 textures in 349 atlases; 19 Spine skeletons; 107 frame sequences (3189 frames); 3 fonts. Grouped into 61 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

The Three Little Pigs as a building firm in front of their finished mansion: a glossy, toy-bright cartoon cast in gold, orange and brick red on see-through reels, with the mansion's front itself as the prize board, four neon jackpot plaques at the side and a blue-violet wolf as the one cool figure.

**Style.** Family-animation cartoon. Pigs and wolf are rounded mascots with big heads and readable expressions; tools (hard hat, hammer, paint brush, cones, toolbox) are chunky and simplified; houses are doll's-house fronts whose material is exaggerated (straw, logs, brick, gold brick). Signs and transitions borrow from road-works: hazard stripes, caution tape, a diamond road sign.

**Rendering.** Smooth digital painting with airbrushed gradients, strong white gloss highlights, a darker outline and often a pale rim so pieces lift off the dark reel panel. Lettering is fat, bevelled, outlined and rimmed. Effects are flat hand-drawn shapes with glow (fire swirls, wind lines, splashes). The wolf and the big-win pigs are whole softly shaded frames, close to pre-rendered animation. The background is drawn brick by brick.

**Colour.** Warm cast on a cyan sky. Symbols and props are gold, orange and red (reel stills: #f9dd0c 14%, #750f05 10%; hat rig: #f8ad0a 27%, #e05a0a 18%); the day background is red brick and gold under cyan (#5cceed, #12bef8); the wolf is blue-violet (#6d72a0, #9099c7). Royals are a single emerald green. Prize tiers keep one colour each wherever they appear: red Grand, blue Major, green Minor, magenta Mini; the mansion's prize plates are gold at the top, blue in the middle, dark at the bottom. The palette measured over all captured art (#6d729f 21%, #8f9ac8 15%, #c0c5cf 10%) is the wolf's, because his frames fill 132 of the 349 textures; it is not what the screen looks like.

**Lighting.** Daylight from above on a clear day; objects are top-lit with hard gloss. Glow is kept as separate additive layers and outline sprites (hat glow, frame pulses, plate highlights), not painted in. The background is repainted for evening and night, with lit windows and lantern pools at night, and the prize plates have day and night versions to follow it.

**Ambience.** Sunny, proud and busy, as the base-game screens show: the mansion fills the picture behind the reels, prize plates glow on its roof, four plaques stand at the left and the logo at the right, and the reel window is the one dark area. Wins in the base game are modest: a line of text names the ways at the foot of the reels, the wolf is boxed in gold, and a larger win ($12.00 at a $2.00 bet) puts gold digits on a flare. The wolf is a comic villain who appears in the base game only as a reel symbol. The pace of features is not known from this run: none came in about 32 spins.

**Shape language.** Round and chunky everywhere: domed hats, coins, rounded topiary, bubble letters, pill buttons. Straight edges belong to the house: bricks, frames, plates, the hairline reel frame. Sharpness is kept for the wolf's ears and teeth, sparks and shards.

**Materials.** Glossy plastic (hard hats, tool grips, buttons), polished steel and gold (hammer, coins, the door), parchment and wax (deed), straw, cord, logs, painted planks, brick and gold brick (houses, frames, mansion), fur, clipped hedge and cobbles, enamel and neon (plaques), hazard tape, wet paint.

**Typography and lettering.** Display lettering is drawn art: the logo gives each word its own material (riveted gold HUFF, hazard-tape N', bubble PUFF, comic 3D block MONEY MAN$ION), and prize and feature words are heavy rounded capitals with bevel, outline and rim, coloured by tier. Multiplier numbers are lettered sprites in a normal and a highlighted state. Running text is Noto Sans as distance-field font pages (four styles loaded), with Frutiger Neue in the provider's frame; both are the provider's.

**Motion.** Seen in the real frames: the loading cards slide in turn; reels turn with a vertical blur and the spin button becomes a white stop square; hard hats land on glowing backings; Construction Pigs rise over a reel; the deed lands larger than its cell; a win shows a strip of text, a gold box on the wolf and, when larger, gold digits on a flare. Everything else is read from the files: 19 Spine 4.1.24 skeletons with hat landings of 1.3 to 3.0 s and wins of 2.0 s, the Construction Pig's pop-ups of 0.3 to 1.0 s, the wolf's blow in stages of 0.3 to 3.0 s, frames that arrive in 1.0 s and houses that build in 1.0 to 2.3 s and are blown away in 1.0 to 1.3 s, feature signs of 1.3 to 1.9 s, a 1.75 s caution-tape transition, a gold door that opens in 2.0 s, a paint pour of 4.3 s, day-evening-night changes of 2.0 s and a big win where each pig enters in 0.5 s and the wolf in 5.5 s. Acting is drawn frame by frame inside the rigs: the wolf's face up to 83 frames, pig loops of 25 to 29, two wind sequences of 136 and 165 half-screen frames. Sprite sheets state 24 frames a second. No skeleton frame is shown in this report: the project's drawing tool does not read Spine 4.1 correctly.

**Variants and themes.** Three times of day for the background and the prize plates. Three tiers of frame and house on one rig (straw, stick, brick). The hat at symbol size and as Mega Hat (the text names 2x2, 3x3 and 3x5). Reel frames in gold and blue-white for 3 and 4 rows. Every plaque, plate and number in a resting and a highlighted state. Three copies of the wolf (main, Major, Grand). Landscape and portrait versions of the transition.

**How it is built.** PixiJS client. In this run: 349 textures, 3,579 named sprites, 19 skeletons, 3 fonts, 107 frame sequences (3,189 frames). Sprite sheets are 'Red 7 Exporter' packs; skeletons are Spine 4.1.24 with few bones (4 to 62) and most of their weight in frame sequences played inside the rig. Parts of one rig share a canvas so tiers swap part for part (house parts 302x303 and 352x351, symbol parts 336x336). The mansion is a 1920x1920 picture per time of day over a 1920x2472 sky. The reel board is a see-through dark panel in a hairline frame. Atlas pages are 2048x2048; the three wolf rigs take 132 of them and the prize meters 54.

**Consistency.** High: one outline-and-gloss treatment on every object, one lettering system, one colour per prize tier, and the building-site motif carried into symbols, signs, the transition, the feature props and the logo. Two things stand apart: the wolf and the big-win pigs are animated as whole frames while everything else is parts and overlays, and one stray sequence (a fire dragon) belongs to another game. Part names left from the earlier Huff N' Puff games (buzzsaw, wheel) show the rigs were carried over and re-dressed (inference).

**What to take from it.** (1) Make the scene the prize board. The mansion is at once background, theme and the place where the feature's prizes sit, colour-banded gold, blue and dark for the three prize ranges; the player reads the top prizes off the house before a spin. A see-through reel panel in a hairline frame is what makes that possible. (2) Carry one motif through every layer. The building site is in the symbols (hat, cones, toolbox), the signs (hazard stripes), the transition (caution tape), the feature props (brush, hammer), the tiers (straw, stick, brick frames) and the logo. Each new feature got one prop and one stripe colour rather than a new look. (3) Sell the features on the loading screen with three cards: the jackpots, the trigger (six hats) and the choice of features. Each is one picture and one line. (4) One colour per prize tier, used on plaques, labels and effects, and one glow colour per house tier (magenta straw, cyan stick, yellow brick). It lets small frames on a busy board be read at a glance. (5) Spend drawn animation where the character is. The wolf's face and the big-win pigs are full-frame sequences; frames, plates, coins and signs are stills moved by a rig with glow overlays. For our AI art work this splits the job cleanly: stills and overlays suit generation and re-tinting, the acted sequences need an animator or a consistent frame-by-frame method. (6) Tiers by re-dressing a rig: straw, stick and brick share bones and canvas sizes, and the same three house paintings serve as reel symbols, paytable pictures, feature houses and big-win props. (7) Repainting beats tinting for time of day: the night mansion has its own lit windows and lantern light, and the prize plates have day and night versions to match. (8) What it costs: three near-identical wolf rigs on 132 atlas pages, two near-identical symbol rigs and a stray sequence from another game. A build audit would have saved a large share of the download; worth a check on our own builds. (9) Not seen in play, so not yet a reference for us: the wolf himself, the free spins, the four features, jackpot awards, the big win and the paytable's lower pages. In about 32 base spins no feature came and this demo shows no Buy Pass button; a longer played session is still needed before using this game as a motion or pacing reference.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 55% · saturation 44% · contrast 55% · warm 32% / cool 64% · brighter towards: top (747), top-right (184), bottom (54)

Palette: #6d729f blue 21%, #8f9ac8 blue 16%, #c0c5cf light blue 10%, #f2f8f5 light green 9%, #0e0710 black 5%, #f6a614 orange 4%, #b9a47f orange 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 2 | 58% | 54% | 64% | 35% / 62% | #f6fbf0 light green 16%, #5bd1f1 cyan 12%, #b3c1c8 cyan 12% |
| Reel board | 1 | 9% | 77% | 42% | 15% / 69% | #02061d black 86%, #e2a810 orange 3% |
| Symbols | 5 | 64% | 60% | 62% | 68% / 27% | #f1f9f8 light cyan 20%, #f8ad0b orange 18%, #e0580c orange 13% |
| Characters | 4 | 55% | 29% | 50% | 5% / 94% | #6d72a0 blue 43%, #9099c8 blue 32%, #bcc7d5 light blue 16% |
| Logo and title | 2 | 54% | 72% | 78% | 57% / 38% | #5bd6f7 cyan 14%, #771606 dark red 10%, #1f0b08 black 9% |
| Win celebrations and banners | 8 | 51% | 46% | 58% | 30% / 65% | #6f74a0 blue 21%, #c3becb grey 17%, #8994c7 blue 9% |
| Effects | 10 | 56% | 54% | 51% | 72% / 22% | #f7faf5 light green 16%, #f0872a orange 15%, #bbab82 orange 12% |
| Game interface | 6 | 66% | 44% | 38% | 32% / 46% | #fcfefe light cyan 39%, #110a0f black 10%, #fae51c gold 6% |
| Provider interface (shared) | 23 | 60% | 17% | 17% | 13% / 27% | #ffffff light blue 37%, #838481 grey 21%, #171617 black 18% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Loading screen background

`loading_bg` · atlas · 1 parts · largest 1920×1920 · sheet `sheets/loading_bg.webp`

- **Role:** The picture behind the loading screen, seen on the real loading frames: the garden and drive without the mansion.
- **Subject:** A blue sky with flat white clouds, a far line of blue-green hedge, cypress trees and four clipped bushes on a lawn, a strip of flowers, and the crazy-paved drive falling to dark brown at the bottom.
- **Style:** The same storybook garden as the main background, emptied to leave room for the loading cards.
- **Rendering:** Flat painted shapes with gradient fills and no texture noise; the distance is blurred, the paving sharp.
- **Colour:** Measured: sky cyans #5ad7f8 31%, #b5eff9 14%, #16c0f7 7%; paving #d3a34b 10% and #b15d18 9%; near-black #250802 14% at the foot. 64% cool.
- **Lighting:** Even daylight from above.
- **Ambience:** A clear summer day; calm before the game's noise.
- **Materials:** Hedge, lawn, stone.
- **Variants:** One picture; the same garden appears with the mansion in the background rig.
- **Motion:** Still. On the real loading screen the cards in front of it change every few seconds.
- **Construction:** One JPEG of 1920x1920, square so that it serves landscape and portrait (inference).
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 58% · saturation 67% · contrast 88% · warm 31% / cool 64% · brighter towards: top (1)
- **Palette (measured):** #5ad7f8 cyan 31%, #b5eff9 light cyan 14%, #250802 black 14%, #d3a34b orange 10%, #b15d18 orange 9%, #16c0f7 cyan 7%

### Mansion background, three times of day

`background` · atlas · 10 parts · largest 1920×2472 · sheet `sheets/background.webp`

- **Role:** The scene behind everything: the Money Mansion at the end of a cobbled drive, in a day, an evening and a night version with skies and clouds to match. The base-game screen shows the day version, the mansion's brick front rising behind and above the reels with prize meters set into it.
- **Subject:** A red-brick mansion with a gold-brick mansard roof, two dormer towers, blue cornices and a lit white doorway with lanterns; cypress trees and clipped round bushes on a lawn; a wide crazy-paved drive in the foreground. Three skies (blue day, violet and yellow evening with rays, deep blue night), day and night cloud banks, a glowing moon.
- **Style:** Storybook illustration with a strong one-point perspective that pulls the eye to the door.
- **Rendering:** Clean painted shapes with gradient fills, brick and paving drawn stone by stone; hard-edged (soft edge 2%). The paving darkens to near black at the bottom edge, where the interface sits.
- **Colour:** Measured over the unit: pale sky #f8fbef 18%, grey-blue #b3c1c8 13%, night #0a0324 11%, cyan #5cceed 9%, evening peach #f8cd8d 8%, night blue #0c1884 7%. Day is red brick and gold on cyan; evening turns the brick orange-red under a yellow sky; night turns it purple with a blue drive.
- **Lighting:** Each version is repainted for its light, not tinted: the night mansion has lit windows and warm pools of light at the lanterns.
- **Ambience:** Sunny suburban pride by day, showy by evening, calm by night.
- **Materials:** Brick, gold brick, stone steps, clipped hedge, cobbles.
- **Variants:** Day, evening and night, each as mansion picture, sky and clouds; twelve transitions between them.
- **Motion:** From the skeleton file (Spine 4.1.24, 16 bones, 16 slots, 12 animations): every change between day, evening and night is 2.0 s, each in a version with clouds and one without ('seprated'). Only the day version was seen on a real screen; when the time of day changes is not known from this run.
- **Construction:** One skeleton, atlas on 7 pages, 10 parts: three mansion pictures of 1920x1920, three skies of 1920x2472 (taller, so the sky can serve a portrait layout; inference), four cloud and moon pieces.
- **Notes:** The mansion is both the backdrop and the prize board: the jackpot meters rig places its multiplier plates on this facade.
- **Skeleton (from the file):** Spine 4.1.24 · 16 bones · 16 slots · animations: MM_Day_to_Eve (0 s), MM_Day_to_Eve_with&cloud (0 s), MM_Day_to_Night_seprated (0 s), MM_Day_to_Night_with&cloud (0 s), MM_even_to_day_seprated (0 s), MM_even_to_day_with&cloud (0 s), MM_even_to_night_seprated (0 s), MM_even_to_night_with&cloud (0 s), MM_Night_to_Day_seprated (0 s), MM_Night_to_Day_withcloud (0 s), MM_Night_to_even_seprated (0 s), MM_Night_to_even_with&cloud (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 58% · saturation 52% · contrast 60% · warm 36% / cool 61% · brighter towards: top (3), bottom (3), bottom-left (1)
- **Palette (measured):** #f8fbef light green 18%, #b3c1c8 blue 13%, #0a0324 black 11%, #5cceed cyan 9%, #f8cd8d light orange 8%, #0c1884 dark blue 7%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel frames, jackpot plaques and message bar

`basegame` · atlas · 12 parts · largest 1106×725 · sheet `sheets/basegame.webp`

- **Role:** The reel board and what stands round it in the base game. The real screens show a 5x3 window with a thin gold frame and gold dividers over a see-through dark panel, four jackpot plaques down the left (GRAND $10,000, MAJOR $2,000, MINOR $200, MINI $40 at a $2.00 bet) and the game's name on a small bar at the top left. A win is named in a dark see-through strip across the foot of the reels ('12 WAYS PAY $6.00').
- **Subject:** Two reel frames in gold and two in pale blue-white, each at two heights (1039x517 for three rows and about 1030x680 for four); a blurred dark patch that goes behind the reels; four empty jackpot plaques (GRAND red in gold, MAJOR blue in white, MINOR green, MINI magenta); a yellow and red total-win bar; an orange striped message bar; a game-name strip.
- **Style:** Minimal on purpose: hairline frames, no carved cabinet. The plaques carry the decoration, each with its tier word in fat bevelled capitals on a hazard-striped tab.
- **Rendering:** Thin vector-like lines for the frames; the plaques are glossy and bevelled with neon-tube rims on Minor and Mini.
- **Colour:** Measured: 86% is the panel's near-black blue #02061d, with gold #e2a810 3%. Tier colours: red and gold Grand, blue Major, green Minor, magenta Mini.
- **Lighting:** No light of its own; the plaques have a top highlight.
- **Ambience:** A quiet stage that lets the symbols and the mansion carry the picture.
- **Materials:** Gold wire, dark glass, enamel and neon on the plaques, hazard tape.
- **Variants:** Gold and blue-white frames, each for 3 and for 4 rows. By the client's text the grid grows to 4 rows in the Home Improvement feature; which feature uses the blue-white frame was not seen.
- **Motion:** Seen on the real frames: reels turn with a vertical blur and stop left to right, and the spin button becomes a white stop square while they turn. The hammer rig holds a 30-frame 'grow_reels' sequence in which the frame grows taller; that was not seen.
- **Construction:** One 'Red 7 Exporter' sheet on 2 pages, 12 frames.
- **Notes:** On the base-game screen the mansion's prize plates show dimly through the reel window: the see-through panel is doing real work.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, glow or soft effect · brightness 9% · saturation 77% · contrast 42% · warm 15% / cool 69% · brighter towards: top (3), top-left (1)
- **Palette (measured):** #02061d black 86%, #e2a810 orange 3%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Jackpot coins and counter rig

`coin` · atlas · 60 parts · largest 500×501 · sheet `sheets/coin.webp`

- **Role:** Coins and labels for the jackpot awards and the free-spin counter, loaded with the main slot (manifest name Game.Jackpot.Animation).
- **Subject:** Three gold coins with beaded rims: one stamped with a house, one with a pig's face, one with a spoked wheel; coin edge pieces for a turning coin; MINOR BONUS and MINI BONUS lettering; an orange striped counter plate with a glow version; star sparkles, a white ring of fire and a shine bar.
- **Style:** Toy-bright cartoon gold with thick embossed line art; lettering in the tier colours used across the game.
- **Rendering:** Smooth gradients with a stepped highlight band across each coin; lettering is fat, outlined and bevelled with a white rim.
- **Colour:** Measured: orange gold #f5b32b 16%, pale gold #fae878 9%, deep orange #d8700f 8%, with white and grey from the sparkle and ring layers. MINOR is green over blue, MINI magenta over blue-violet.
- **Lighting:** Top light on the coins; sparkle and glow as separate additive layers.
- **Ambience:** Rewarding and shiny.
- **Materials:** Polished gold, enamel-like lettering, a plastic-looking striped plate.
- **Variants:** Three coin faces on one coin; Mini and Minor labels (Major and Grand have animations in the file but no label picture in this atlas).
- **Motion:** From the skeleton file (20 bones, 24 slots, 11 animations): jackpot_mini, jackpot_minor, jackpot_major, jackpot_grand and jackpot_wheel 3.3 s each, the mini and minor intros 2.7 s, coin rings 2.5 s, fs_counter_anim 1.7 s, particle_coin 1.3 s. The sparkle is a 30-frame sequence, the fire ring 17. Not seen on a real screen.
- **Construction:** One skeleton, atlas on 2 pages, 60 named parts. The coin turns by swapping front, back and two edge pieces (coin-side-round, coin-side-straight) rather than by a 3D model.
- **Notes:** The spoked-wheel coin and a jackpot_wheel animation suggest a wheel award carried over from the earlier Huff N' Puff games (inference); the client's text for this game still names a WHEEL FEATURE in its Buy Pass lines.
- **Skeleton (from the file):** Spine 4.1.24 · 20 bones · 24 slots · animations: fs_counter_anim (0 s), jackpot_grand (0 s), jackpot_major (0 s), jackpot_mini (0 s), jackpot_mini_coin_ring (0 s), jackpot_mini_in (0 s), jackpot_minor (0 s), jackpot_minor_coin_ring (0 s), jackpot_minor_in (0 s), jackpot_wheel (0 s), particle_coin (0 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 68% · saturation 35% · contrast 45% · warm 43% / cool 2% · brighter towards: top (5)
- **Palette (measured):** #989898 grey 28%, #f5b32b orange 16%, #c2c1c1 grey 13%, #fcfcf8 light yellow 12%, #fae878 gold 9%, #d8700f orange 8%

### Hard hat, deed and wolf symbol rig (base set)

`symbol` · atlas · 193 parts · largest 935×899 · sheet `sheets/symbol.webp`

- **Role:** The animated versions of the three special symbols on the reels: the hard hat (sym12 in the animation names), the deed and the wolf. The client's text calls the hat HARD HAT and names a BONUS symbol that triggers the Money Mansion feature; that the deed is that BONUS symbol is inference from its animation names. On the real screens the deed lands larger than its cell, overlapping its neighbours, on a red backing; two came at once twice, never the three the text asks for.
- **Subject:** A large gold hard hat with a round pig badge (bighat, 935x899), a medium hat (336x336), the DEED scroll as frame sequences with and without a backing, the wolf symbol as a 27-frame sequence that ends on a howl against a full moon, and the rings, swirls, sparks and dotted red and orange backings that go with them.
- **Style:** The same cartoon as the stills, with flat hand-drawn fire swirls and glow outlines layered on.
- **Rendering:** Painted objects with gloss highlights; effects are flat shapes with soft glow (a crescent swirl of flame, thin rings, a burning outline in the deed's shape). The square backings are a halftone dot pattern over red and over orange.
- **Colour:** Measured: orange #f8ad0a 27%, deep orange #e05a0a 18%, near-white #f2f9f5 16%, yellow #fef90b 9%; 75% warm. The wolf frames bring the only blue (#2d3a58).
- **Lighting:** Top light on the hat with a white hot spot on its crown; the deed is lit evenly; glows are separate layers (bighat_glow, pig_pulse, ring).
- **Ambience:** Hot and loud: every special symbol is announced with fire or gold light.
- **Materials:** Glossy plastic (hat), parchment with a wax seal and ribbon (deed), fur (wolf), flame drawn as flat graphic shapes.
- **Variants:** The hat at two sizes (hat 336 px, bighat 935 px; the client's text names MEGA HAT 2x2, 3x3 and 3x5) and as an 18-frame spin (hat_spin). The deed with a backing, without one, and as a glowing outline. The dotted backing in red and in orange.
- **Motion:** From the skeleton file (Spine 4.1.24, 62 bones, 61 slots, 11 animations): sym12_land 3.0 s, sym12_land_fs 1.25 s, sym12_land_megahat 2.5 s, three win animations of about 2.0 s, deed 1.8 s, deed_anticipation 0.4 s, deed_with_fire_loop 1.2 s, wolf 1.25 s. The fire swirl is 34 drawn frames, the deed 33, the wolf 27. On the real screens hats were seen landed, up to five at once and three high on a reel, each on its glowing dotted backing; six are needed for free spins and that did not come in about 32 spins. No frame of the rig is shown: the project's drawing tool does not read Spine 4.1 correctly.
- **Construction:** One skeleton with its atlas on 8 pages, 193 named parts. The deed, the wolf, the hat spin and the swirls are frame sequences played inside the rig; the hat itself is a still with glow, pulse and blink layers.
- **Notes:** Two rigs carry the same name (hat&deed_sym) in two folders, symbol and symbolanimations; this is the one the manifest calls Game.Symbol.Spine. The prepared files keep them apart.
- **Skeleton (from the file):** Spine 4.1.24 · 62 bones · 61 slots · animations: deed (0 s), deed_anticipation (0 s), deed_withoutbg (0 s), deed_with_fire_loop (0 s), sym12_land (0 s), sym12_land_fs (0 s), sym12_land_megahat (0 s), sym12_win_backup (0 s), sym12_win_bkg_anim (0 s), sym12_win_hat_anim (0 s), wolf (0 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 65% · saturation 69% · contrast 59% · warm 75% / cool 23% · brighter towards: bottom (16), top (15), top-right (14)
- **Palette (measured):** #f8ad0a orange 27%, #e05a0a orange 18%, #f2f9f5 light green 16%, #fef90b gold 9%, #2d3a58 dark blue 4%, #0b0c14 black 3%

### Hard hat, deed and wolf symbol rig (longer deed)

`symbolanimations` · atlas · 250 parts · largest 935×899 · sheet `sheets/symbolanimations.webp`

- **Role:** A second copy of the special-symbol rig, the one the manifest calls Game.Symbol.Animation and loads with the main slot. It differs from the base set in the deed: a longer landing sequence with a red sunburst backing.
- **Subject:** The same hard hat at two sizes, pig badge, swirls, rings and wolf frames as the symbol rig; the DEED scroll here has 76 frames (33 there), in some of which it stands on a red and gold sunburst card.
- **Style:** As the symbol rig: glossy cartoon objects with flat graphic fire.
- **Rendering:** As the symbol rig. The deed's sunburst backing is flat red rays with a gold edge.
- **Colour:** Measured: near-white #f0f9f9 29%, orange #f8ad0a 18%, deep orange #e0590a 13%, yellow #fef90c 6%, the wolf's light blue #afd0ec 4%. Cooler than the base set (63% warm against 75%) because the longer deed sequence adds white parchment.
- **Lighting:** Top light and separate glow layers, as in the symbol rig.
- **Ambience:** The same heat as the symbol rig, with a more showy deed.
- **Materials:** Plastic, parchment, wax, fur and flat flame, as in the symbol rig.
- **Variants:** The deed in three sequences: 76 frames with backing, 23 without, 29 as a burning outline.
- **Motion:** From the skeleton file (62 bones, 61 slots, 11 animations): deed 3.6 s (1.8 s in the other copy), deed_land 0.8 s in place of deed_anticipation, the hat and wolf animations at the same lengths as the symbol rig. Not seen on a real screen.
- **Construction:** One skeleton, atlas on 11 pages, 250 named parts. Same bones and slots as the symbol rig.
- **Notes:** Two near-identical rigs are shipped where one with one more animation would do. It reads as a late change to the deed kept beside the earlier version (inference).
- **Skeleton (from the file):** Spine 4.1.24 · 62 bones · 61 slots · animations: deed (0 s), deed_land (0 s), deed_withoutbg (0 s), deed_with_fire_loop (0 s), sym12_land (0 s), sym12_land_fs (0 s), sym12_land_megahat (0 s), sym12_win_backup (0 s), sym12_win_bkg_anim (0 s), sym12_win_hat_anim (0 s), wolf (0 s)
- **Measured:** bright, saturated, warm and cool mixed, high contrast, strong highlights · brightness 70% · saturation 56% · contrast 61% · warm 63% / cool 34% · brighter towards: bottom (16), top (15), top-right (14)
- **Palette (measured):** #f0f9f9 light cyan 29%, #f8ad0a orange 18%, #e0590a orange 13%, #fef90c gold 6%, #afd0ec light blue 4%, #0a0b15 black 3%

### Houses and frames rig

`houses` · atlas · 179 parts · largest 360×360 · sheet `sheets/houses.webp`

- **Role:** The three little pigs' houses and the frames that stand for them on the reels during the features. By the client's text, a hard hat that lands in a feature adds a STRAW frame to its position or upgrades it to STICK and then BRICK, and at the end each frame becomes its house and reveals a prize.
- **Subject:** A straw hut, a log cabin and a brick mansion, each about 300 to 352 px, each with a build-in and a blown-away sequence; three frames to match (plaited green straw tied with blue cord, red-painted planks nailed at the corners, gold bricks with a star sparkle); three tile backings (bricks lit orange, purple planks, red straw weave) and glow and pulse outlines in yellow, cyan and magenta.
- **Style:** Doll's-house fronts drawn head-on, with the material exaggerated so each reads at a glance. The blow-away frames break the house into flying planks, straw and dust.
- **Rendering:** Painted with fine texture inside (brick courses, log ends, straw strands), a coloured rim light round each house (yellow on brick, blue on wood, magenta on straw) and smoke puffs drawn as soft grey-beige clouds.
- **Colour:** Measured over the unit: straw and wood tans (#8d7d52 17%, #c1b79a 12%) and dark brick red (#49131c 13%); hues split between red 31%, orange 25%, yellow 25% and green 11%. Each tier has its own glow colour: magenta straw, cyan stick, yellow brick.
- **Lighting:** Light from the top left on the houses (9 of 11 measured); the brick mansion's windows are lit from inside.
- **Ambience:** Storybook and cosy, with comic destruction.
- **Materials:** Straw, cord, logs, painted planks with nail heads, brick, gold brick.
- **Variants:** Three tiers on one rig: straw, stick (the files say both stick and wood) and brick, each as frame, glow, pulse, backing and house.
- **Motion:** From the skeleton file (53 bones, 56 slots, 11 animations): straw_in, stick_in and brick_in 1.0 s each; Straw_house_in and Wood_house_in 1.0 s, Brick_house_in 2.3 s; the three house_out animations 1.0 to 1.3 s; brick_loop 0.8 s. House building and destruction are drawn sequences of 23 to 24 frames. Not seen on a real screen.
- **Construction:** One skeleton, atlas on 5 pages, 179 named parts. House parts share a canvas (302x303 for straw and wood, 352x351 for brick), so tiers swap part for part.
- **Notes:** The same three houses are the reel stills, the paytable pictures and, in the big-win rig, what the wolf blows down: one set of paintings reused four times.
- **Skeleton (from the file):** Spine 4.1.24 · 53 bones · 56 slots · animations: Brick_house_in (0 s), Brick_house_out (0 s), brick_in (0 s), brick_loop (0 s), stick_in (0 s), Straw_house_in (0 s), Straw_house_out (0 s), straw_in (0 s), straw_stiatic (0 s), Wood_house_in (0 s), Wood_house_out (0 s)
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 47% · saturation 60% · contrast 67% · warm 75% / cool 18% · brighter towards: top-left (9), right (1), bottom (1)
- **Palette (measured):** #8d7d52 orange 17%, #49131c dark red 13%, #c1b79a orange 12%

### Reel symbols (stills)

`static_sym` · atlas · 20 parts · largest 933×371 · sheet `sheets/static_sym.webp`

- **Role:** The still picture of every reel symbol and the logo, 20 frames in one sheet. The real screens show fourteen of them on the 5x3 reels (cones, toolbox, the three pigs, the hard hat, the deed, the wolf, 9, 10, J, Q, K and A), each in a cell of about 144 px at 1280x720 on a see-through dark window. The three houses were not on a screen; they belong to the features.
- **Subject:** A rolled DEED with a red seal, a gold hard hat with a pig badge (with and without its glow backing), three houses (brick mansion, log cabin, straw hut), the wolf in a gold frame against a starry night, a wooden toolbox lettered BACON BROS BUILDING CO., a pair of traffic cones, three pigs (a boss in a pinstripe suit with a pencil behind his ear, on an orange backing, a worker in a blue cap and dungarees carrying an axe, a piglet in a green cap lying on a hay bale), and six royals: 9, 10, J, Q, K, A. The logo and a 3x3 blank are in the same sheet.
- **Style:** Cartoon building-site take on the Three Little Pigs. Pigs and wolf are rounded mascots with large heads and clear expressions; the houses are doll's-house fronts; tools are chunky and simplified; royals are heavy serif letters with one small ornament each (crowns on Q and K, a shield on J, a gem on A).
- **Rendering:** Smooth digital painting with airbrushed gradients, a darker outline and a pale rim so each picture lifts off the dark reel backing. Detail sits in the faces, the brickwork and the hat badge. The hat, the wolf and the boss pig carry a square backing; the other pictures are cut to their silhouette.
- **Colour:** Measured over the sheet: gold and orange lead (#f9dd0c 14%, #f7c74e 6%, #e59a0c 6%), then brick red (#750f05 10%, #b1230a 4%). All six royals are one emerald green with a silver-blue rim, so value in the set is carried by subject and by gold, not by letter colour. Vivid (saturation 68%) and high contrast (0.85).
- **Lighting:** Top light on most pieces (8 of 11 measured), with hot white highlights on the hat and an orange glow behind it. The wolf is lit cool from the front against a blue backing.
- **Ambience:** Bright, friendly and busy: a children's-story cast on a work site, with the gold hat shouting loudest.
- **Materials:** Glossy moulded plastic for the hard hat, parchment and wax for the deed, brick, logs and straw for the houses, painted wood for the toolbox, soft matte skin and cloth for the pigs, fur in broad locks for the wolf, enamelled metal for the royals.
- **Variants:** The hat in two states (sym_hat with its glow backing, sym_hat_withoutbg). The three pigs are named pig_one, pig_two and pig_three by the files. The three houses appear here as symbols and again, larger and animated, in the houses rig.
- **Motion:** None in this unit: these are stills. The hat, the deed and the wolf have a skeleton of their own (symbol, symbolanimations); the client ships no skeleton for the pigs, tools or royals. On the real win frames the winning ways are named in a dark strip across the foot of the reels ('12 WAYS PAY $6.00'), a larger win adds its amount in gold digits on a flare over the darkened bottom row, and the wolf, which completed the wins seen from reels 3 and 4, is boxed in gold; that he is the WILD of the client's text (reels 2 to 4) is inference. How pigs, tools and royals move on a win was caught only as single frames.
- **Construction:** One 'Red 7 Exporter' sprite sheet on one page, 20 frames from 106x117 (the 9) to 236x192 (the brick house), trimmed and stored with an untrimmed size of 236x236, so a cell is about 236 px at the shipped desktop size. The logo frame is 933x371.
- **Notes:** Premium symbols are told apart from royals by three things at once: gold or red, a glowing backing, and size. The base-game screens confirm it: hard hats fill and overflow their cells and stack three high, the boss pig brings an orange block of colour, while the royals sit small and green in theirs.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 53% · saturation 68% · contrast 84% · warm 69% / cool 26% · brighter towards: top (8), top-left (2), bottom (1)
- **Palette (measured):** #f9dd0c gold 14%, #750f05 dark red 10%, #f1f6f7 light cyan 9%, #f7c74e orange 6%, #e59a0c orange 6%, #0d0a0c black 5%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Construction pig

`hat_pig` · atlas · 82 parts · largest 366×491 · sheet `sheets/hat_pig.webp`

- **Role:** The pig that pops up above a reel wearing a hard hat. By the client's text, Construction Pigs may appear over any number of reels in the base game, count toward the six hard hats that trigger free spins and may add hats to their reel. On every base-game screen five hat tops peek over the top edge of the reels, one per reel; on two real frames the pigs over reels 2 and 3 have risen far enough to show hat, ears and eyes.
- **Subject:** A smiling pink pig in a white vest with yellow hi-vis braces, drawn rising from behind an edge (41 frames from ears only to head and shoulders), his head alone bobbing, and an orange hard hat with the pig badge and a white outline.
- **Style:** The same mascot cartoon as the reel pigs, flatter and more sticker-like: a white stroke runs round the whole figure.
- **Rendering:** Soft airbrushed shading inside a clean white outline; hard-edged (soft edge 4%).
- **Colour:** Measured: pig pinks #f5a1a5 29% and #c7666d 19%, dark red-brown #9f2f10 22% (the shaded head frames), yellow #eee611 2% on the braces; 100% warm.
- **Lighting:** Top light (all 31 measured parts).
- **Ambience:** Cheerful helper; the friendly counterpart of the wolf.
- **Materials:** Soft skin, cloth, glossy plastic hat.
- **Variants:** Animations for one, two and three hats (SingleHat, doubleHat, ThreeHat).
- **Motion:** From the skeleton file (6 bones, 7 slots, 19 animations): entries of 0.3 to 0.9 s, blinks of 0.7 to 1.0 s, bounces of 1.0 s, exits of 0.6 to 1.0 s. The rise is a 41-frame sequence, the head bob 22 and 18 frames. On the real frames he was caught part-risen over two reels; the full rise to head and shoulders, and what he does with the hats, were not seen.
- **Construction:** One skeleton, atlas on 3 pages, 82 named parts, almost all frames of three sequences.
- **Notes:** A still of the same pig at 192x246 is the paytable's picture (c_pig_sym).
- **Skeleton (from the file):** Spine 4.1.24 · 6 bones · 7 slots · animations: doubleHat_A_Entry (0 s), doubleHat_B_blink (0 s), doubleHat_C_Up (0 s), doubleHat_D_Blink (0 s), doubleHat_E_Exit (0 s), doubleHat_F_bounce (0 s), SingleHat_A_Entry (0 s), SingleHat_B_Entry (0 s), SingleHat_C_blink (0 s), SingleHat_D_bounce (0 s), SingleHat_E_pigUp (0 s), SingleHat_F_Blink (0 s), SingleHat_G_Down (0 s), ThreeHat_A_Entry (0 s), ThreeHat_B_Blink (0 s), ThreeHat_C_Entry (0 s), ThreeHat_D_Blink (0 s), ThreeHat_E_Down (0 s), ThreeHat_F_Bounce (0 s)
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged · brightness 57% · saturation 51% · contrast 66% · warm 100% / cool 0% · brighter towards: top (31)
- **Palette (measured):** #f5a1a5 light red 29%, #9f2f10 red 22%, #c7666d red 19%, #f2e5e4 light red 13%, #f9564c red 4%, #dccac2 light orange 3%

### The wolf (main rig)

`wolf` · atlas · 297 parts · largest 908×776 · sheet `sheets/wolf.webp`

- **Role:** The Big Bad Wolf, the game's one full character: he rises behind the reels, puffs his cheeks and blows. Loaded with the main slot (manifest name Game.Wolf.Animation). He was not on a real screen in this run.
- **Subject:** A blue-violet wolf seen from the front and in three-quarter view: head low and scowling, cheeks puffed white, head thrown back in a howl with a red mouth and teeth, a back view howling upward, two paws with claws that grip an edge, grey wind streaks, white blow lines and a clipped round bush.
- **Style:** Family-animation villain: big head, heavy brow, small bright eyes, a comic rather than frightening scowl.
- **Rendering:** Smooth, softly shaded frames with fur in broad locks and no hard outline; every pose is a whole frame of 908x776, which reads as pre-rendered or fully painted animation rather than a puppet of parts (inference from the sheet).
- **Colour:** Measured: three blue-violets carry it, #6d72a0 45%, #9099c7 33%, #bac7d5 16%; 98% cool. The only warm note is the red of the open mouth.
- **Lighting:** Top light (144 of 149 measured parts), soft, with the muzzle and chest lighter than the back.
- **Ambience:** Comic menace. He is the one cool-coloured thing in a warm cast.
- **Materials:** Fur in soft locks, a wet dark nose, drawn wind.
- **Variants:** The same frames are shipped three times (wolf, wolf1-major, wolf1-grand); this rig and wolf1-major hold the full set with the howl, the wind and the bush.
- **Motion:** From the skeleton file (Spine 4.1.24, 19 bones, 18 slots, 17 animations): W_blow_In 0.7 s, then blow stages W_blowa to W_blowi between 0.3 and 3.0 s, wolf_howl 1.4 s, W_Eye_blink 0.3 s, Wind 3.2 s, Wind_blow_line 1.6 s, bush 0.4 s. The face is frame sequences (seq_01 has 83 frames, eight sequences in all), the howl 31 frames, the paws 15, the wind 48. No frame of the rig is shown: the project's drawing tool does not read Spine 4.1 correctly. The wolf's head and body here are whole drawn frames, so the sheet's own frames are true pictures of him.
- **Construction:** One skeleton whose atlas spreads over 49 pages of 2048x2048, 297 named parts: the weight of full-frame animation at 908x776.
- **Notes:** At 24 frames a second (the rate the sprite sheets state) the 83-frame sequence is about 3.5 s of drawn acting. The wolf is where this game spends its texture budget.
- **Skeleton (from the file):** Spine 4.1.24 · 19 bones · 18 slots · animations: bush (0 s), Wind (0 s), Wind_blow_line (0 s), wolf_howl (0 s), W_blowa (0 s), W_blowa01 (0 s), W_blowah01 (0 s), W_blowb (0 s), W_blowc (0 s), W_blowd (0 s), W_blowe (0 s), W_blowf (0 s), W_blowg_play_reverse (0 s), W_blowh (0 s), W_blowi (0 s), W_blow_In (0 s), W_Eye_blink (0 s)
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged · brightness 55% · saturation 28% · contrast 49% · warm 1% / cool 98% · brighter towards: top (144), top-right (3), left (2)
- **Palette (measured):** #6d72a0 blue 45%, #9099c7 blue 33%, #bac7d5 light blue 16%, #383469 blue 3%

### The wolf (Grand jackpot rig)

`wolf1-grand` · atlas · 171 parts · largest 908×776 · sheet `sheets/wolf1-grand.webp`

- **Role:** A shorter copy of the wolf for the Grand jackpot award (manifest name Game.WolfAnimGrand.Spine); not seen on a real screen.
- **Subject:** The wolf's scowl, puffed cheeks and open-mouthed blow, and the two paws; no howl, wind or bush in this copy.
- **Style:** As the main wolf rig.
- **Rendering:** As the main wolf rig.
- **Colour:** Measured: #6c71a0 46%, #8f99c9 34%, #b7c2ce 11%; 98% cool.
- **Lighting:** Top light, soft.
- **Ambience:** Comic menace.
- **Materials:** Fur.
- **Variants:** Five of the face sequences (seq_01 to seq_05) and the paws: 171 parts against 297.
- **Motion:** From the skeleton file (8 bones, 7 slots, 5 animations): W_Grand_a 2.0 s, W_Grand_b_reverse 0.4 s, W_Grand_c 1.7 s, W_Grand_d 0.4 s, W_Grand_e 3.0 s. No frame of the rig is shown: the project's drawing tool does not read Spine 4.1 correctly. The wolf's head and body here are whole drawn frames, so the sheet's own frames are true pictures of him.
- **Construction:** One skeleton, atlas on 34 pages.
- **Notes:** Three copies of the wolf total 132 atlas pages of 2048x2048 out of the run's 349 textures.
- **Skeleton (from the file):** Spine 4.1.24 · 8 bones · 7 slots · animations: W_Grand_a (0 s), W_Grand_b_reverse (0 s), W_Grand_c (0 s), W_Grand_d (0 s), W_Grand_e (0 s)
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged · brightness 54% · saturation 30% · contrast 49% · warm 2% / cool 98% · brighter towards: top (86), top-right (3), left (2)
- **Palette (measured):** #6c71a0 blue 46%, #8f99c9 blue 34%, #b7c2ce light blue 11%, #c2e0f6 light blue 4%

### The wolf (Major jackpot rig)

`wolf1-major` · atlas · 297 parts · largest 908×776 · sheet `sheets/wolf1-major.webp`

- **Role:** A copy of the wolf for the Major jackpot award (manifest name Game.WolfAnimMajor.Spine). By its part and animation names he blows at the Major meter; not seen on a real screen.
- **Subject:** The same wolf frames as the main rig: scowl, puffed cheeks, howl, paws, wind streaks, blow lines and the bush.
- **Style:** As the main wolf rig.
- **Rendering:** As the main wolf rig: whole softly shaded frames of 908x776.
- **Colour:** Measured the same as the main rig: #6d72a0 45%, #9099c7 33%, #bac7d5 16%; 98% cool.
- **Lighting:** Top light, soft.
- **Ambience:** Comic menace.
- **Materials:** Fur, drawn wind.
- **Variants:** Same 297 parts as the main rig; two bones and two slots fewer, and without the W_blowa01 and W_blowah01 animations.
- **Motion:** From the skeleton file (17 bones, 16 slots, 15 animations): the same blow stages, howl 1.4 s, Wind 3.2 s. No frame of the rig is shown: the project's drawing tool does not read Spine 4.1 correctly. The wolf's head and body here are whole drawn frames, so the sheet's own frames are true pictures of him.
- **Construction:** One skeleton, atlas on 49 pages. The pictures are byte-for-byte separate files from the main rig's, in their own folder.
- **Notes:** A second 49-page copy of the same frames for one award is costly; a shared atlas would have served (a remark on construction, not on how it looks).
- **Skeleton (from the file):** Spine 4.1.24 · 17 bones · 16 slots · animations: bush (0 s), Wind (0 s), Wind_blow_line (0 s), wolf_howl (0 s), W_blowa (0 s), W_blowb (0 s), W_blowc (0 s), W_blowd (0 s), W_blowe (0 s), W_blowf (0 s), W_blowg_play_reverse (0 s), W_blowh (0 s), W_blowi (0 s), W_blow_In (0 s), W_Eye_blink (0 s)
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged · brightness 55% · saturation 28% · contrast 49% · warm 1% / cool 98% · brighter towards: top (144), top-right (3), left (2)
- **Palette (measured):** #6d72a0 blue 45%, #9099c7 blue 33%, #bac7d5 light blue 16%, #383469 blue 3%


## Logo and title

The game's own wordmark.

### Logo rig

`game_logo` · atlas · 23 parts · largest 1920×1920 · sheet `sheets/game_logo.webp`

- **Role:** The game's logo, seen on the real screens at the top right of the base game and on the loading screen.
- **Subject:** HUFF in gold riveted metal with purple sides, a small N' in black and yellow hazard tape, PUFF in glossy blue bubble letters, and MONEY MAN$ION below in tall yellow block capitals with deep red extruded sides, each letter a separate piece. A sparkle, a TM, a drop shadow and a copy of the loading background are in the same atlas.
- **Style:** Three lettering styles in one mark, one per word group: riveted sheet metal, soap-bubble gloss and comic-book 3D block letters.
- **Rendering:** Fat outlined letters with bevels and white gloss; MONEY MANSION has a dotted halftone on its faces and a long extrusion drawn in perspective from below.
- **Colour:** Measured over the unit (the loading background included): cyan #5bd6f7 18%, dark red #771505 12%, yellow #fce711 7%. The mark itself is yellow and gold on red-brown, with the blue PUFF as the cool accent.
- **Lighting:** Top light on the letter faces; the extrusions fall into dark red.
- **Ambience:** Loud, comic and money-minded: the S of MANSION is a dollar sign.
- **Materials:** Riveted metal, hazard tape, glossy blue plastic, painted block letters.
- **Variants:** The whole MONEY MANSION as one picture in three states (mm_logo, logo_3d, logo) and as twelve separate letters.
- **Motion:** From the skeleton file (Spine 4.1.24, 29 bones, 33 slots): one animation, logo_loop, 2.0 s. With one bone per letter, the letters can move one by one (inference from the bone count). On the two real base-game frames the logo looks the same.
- **Construction:** One skeleton, atlas on 3 pages, 23 parts; the rig's own size is 388x233, about the size the logo has on the desktop screen.
- **Notes:** The series mark (HUFF N' PUFF) is kept small and the game's own name is the large line.
- **Skeleton (from the file):** Spine 4.1.24 · 29 bones · 33 slots · animations: logo_loop (0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 54% · saturation 73% · contrast 79% · warm 56% / cool 41% · brighter towards: top-right (7), top (7), top-left (5)
- **Palette (measured):** #5bd6f7 cyan 18%, #771505 dark red 12%, #240803 black 8%, #fce711 gold 7%, #adedf8 light cyan 7%, #fdf585 light gold 5%

### Loading screen pieces

`loading` · atlas · 10 parts · largest 855×859 · sheet `sheets/loading.webp`

- **Role:** What the loading screen is built from. The real frames show them: three cards that take turns on the left, the logo on the right, a caption under it, and the provider's green strip with the load bar at the bottom.
- **Subject:** Card A: the four jackpot words GRAND, MAJOR, MINOR, MINI stacked with sparkles (caption WIN MULTIPLE JACKPOTS!). Card B: a tilted reel board full of gold hard hats (6 hats AWARDS THE FREE SPINS!). Card C: a paint brush dripping yellow paint over a brick tile and a claw hammer over a blueprint, with small versions for the caption (brush OR hammer YOUR WAY TO WINNINGS!). Also the logo, the green strip, the striped load bar and the Light & Wonder mark.
- **Style:** Poster-like teasers in the game's own cartoon, each showing one promise.
- **Rendering:** Painted and glossy, as the symbols; the reel-board card is drawn in perspective with glow round each hat.
- **Colour:** Measured: provider green #1e6929 19% (the strip), gold #f6d21e 12%, near-black #111017 12% (the reel card), orange #e18307 8%.
- **Lighting:** Top light; sparkles and glows painted into the cards.
- **Ambience:** Inviting; it tells the three things the game sells before a spin is made.
- **Materials:** Plastic, steel, bristle and paint, blueprint paper.
- **Variants:** Three cards; brush and hammer at card size and at caption size.
- **Motion:** Seen on the real frames: the cards slide in from the left one after another and the caption changes with them; the bar fills in orange stripes and CLICK ANYWHERE TO CONTINUE fades in over it when loading ends.
- **Construction:** One 'Red 7 Exporter' sheet on one page, 10 frames, the largest 968x625.
- **Notes:** The captions come from the client's text file, where the brush-or-hammer line is written with placeholders named BUZZSAW and HARDHAT: a trace of the earlier game this one was built from (inference).
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 50% · saturation 66% · contrast 71% · warm 60% / cool 26% · brighter towards: top (2), top-left (1), left (1)
- **Palette (measured):** #1e6929 dark green 19%, #f6d21e gold 12%, #111017 black 12%, #fceaa3 light gold 8%, #e18307 orange 8%, #f8f9f0 light yellow 6%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Jackpot meter burst

`jackpot_tally_fx` · atlas · 104 parts · largest 1773×997 · sheet `sheets/jackpot_tally_fx.webp`

- **Role:** What happens to a jackpot meter when it is won (manifest name Game.JPMeterShatterAnim). Not seen on a real screen.
- **Subject:** The Grand plate (red in gold) and the Major plate (blue in white) breaking into flying shards over 11 and 15 frames, a fan of grey rays, a yellow outline in the shape of the mansion's roofline (1773x997), yellow and white splash bursts, glitter and a soft glow.
- **Style:** Comic-book smash: chunky shards, no smoke.
- **Rendering:** Flat coloured shards with a light edge; particles are soft white dots.
- **Colour:** Measured: white #f6fdf3 24%, grey #9b9b9a 17% (rays and backing), yellow #fcf02d 10%, blue #70abfa 7%, red #f20501 6%.
- **Lighting:** Self-lit; a yellow glow rises from below on the Grand.
- **Ambience:** A prize bursting open.
- **Materials:** Enamel plates as brittle shards, light.
- **Variants:** Grand and Major versions.
- **Motion:** From the skeleton file (18 bones, 30 slots, 9 animations): the meter blasts 0.4 to 0.5 s, particle 0.8 s, and two background loops (Grand_bg_anim, Major_bg_anim) keyed to 66.7 s, long slow turns of the rays (inference from the length).
- **Construction:** One skeleton, atlas on 13 pages, 104 named parts.
- **Skeleton (from the file):** Spine 4.1.24 · 18 bones · 30 slots · animations: Dark patch (0 s), Grand_bg_anim (0 s), grand_meter_blast_l2 (0 s), grand_meter_blast_main (0 s), Major_bg_anim (0 s), major_meter_blast_l (0 s), major_meter_blast_r (0 s), mansion_highlight (0 s), particle (0 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 66% · saturation 46% · contrast 56% · warm 45% / cool 34% · brighter towards: bottom (4), top (1)
- **Palette (measured):** #f6fdf3 light green 24%, #9b9b9a grey 17%, #fcf02d gold 10%, #70abfa blue 7%, #f20501 red 6%, #fefb96 light gold 5%

### Big win: the three pigs and the wolf

`newbigwin` · atlas · 441 parts · largest 458×760 · sheet `sheets/newbigwin.webp`

- **Role:** The big-win celebration. The client's text names four tiers (BIG WIN, HUGE WIN, SUPER BIG WIN, MEGA BIG WIN); the rig has three pigs and the wolf, so one figure per tier is a fair guess but it is inference. Not seen on a real screen.
- **Subject:** Three pigs standing and dancing at full length: the worker in a blue cap, red shirt and blue dungarees; the piglet in a green cap and green dungarees holding an ear of wheat; the boss in a purple pinstripe suit and red tie with his arms up. The wolf at large size: scowling face, puffed cheeks, blowing in profile (54 frames) and howling from behind (60 frames). The three houses breaking apart, wind streaks, a bush and a cypress.
- **Style:** The reel cast brought out at full figure and acted like a cartoon short.
- **Rendering:** Whole painted frames, softly shaded, hard-edged against transparency (soft edge 6%); the pigs have a glossy snout and cheek highlights, the wolf broad fur locks.
- **Colour:** Measured: the wolf's blues lead (#6f74a1 28%, #939cc4 18%), then pig pink-grey #d1c4ce 16%, the boss's suit #160980 6% and #5e1590 6%; 78% cool overall because the wolf frames are the largest.
- **Lighting:** Top light on nearly every frame (181 top, 84 top-right of 270 measured).
- **Ambience:** A party: the pigs celebrate, the wolf huffs and the houses fly.
- **Materials:** Skin, cloth, fur, straw, logs and brick.
- **Variants:** Three pigs, each with an in, a loop and an out; the wolf with an in and a loop; three houses with an out.
- **Motion:** From the skeleton file (Spine 4.1.24, 25 bones, 20 slots, 16 animations): each pig comes in 0.5 s, loops 1.3 to 1.5 s and leaves in 0.7 to 1.0 s; wolf_in 5.5 s, wolf_loop 2.5 s; house_in and house_out 0.8 s; wind 2.0 s. The acting is drawn: pig loops of 25 to 29 frames, house break-ups of 24, wind 48. No frame of the rig is shown (Spine 4.1); the sheet's frames are whole pictures of the figures.
- **Construction:** One skeleton, atlas on 13 pages, 441 named parts, nearly all of them frames of 14 sequences.
- **Notes:** The pigs are redrawn for this: on the reels the boss is a head-and-shoulders portrait and the piglet lies on hay; here all three stand and move.
- **Skeleton (from the file):** Spine 4.1.24 · 25 bones · 20 slots · animations: blue_pig_in (0 s), blue_pig_loop (0 s), blue_pig_out (0 s), bushesh (0 s), bushesh_static (0 s), green_pig_in (0 s), green_pig_loop (0 s), green_pig_out (0 s), house_in (0 s), house_out (0 s), purple_pig_in (0 s), purple_pig_loop (0 s), purple_pig_out (0 s), wind (0 s), wolf_in (0 s), wolf_loop (0 s)
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged · brightness 50% · saturation 42% · contrast 58% · warm 19% / cool 78% · brighter towards: top (181), top-right (84), left (5)
- **Palette (measured):** #6f74a1 blue 28%, #939cc4 blue 18%, #d1c4ce grey 16%, #160980 dark blue 6%, #5e1590 purple 6%, #16578d blue 3%

### Feature announcement panels

`tally` · atlas · 74 parts · largest 1169×613 · sheet `sheets/tally.webp`

- **Role:** The signs that announce a feature. The client's text names the features: MONEY MANSION FEATURE, TOUCH-UP FEATURE, HOME IMPROVEMENT FEATURE, MANSIONS FEATURE. Not seen on a real screen.
- **Subject:** Wide panels striped like hazard tape: orange and black in a yellow glow (panel_paint), red and black (Mansion_feature, with a blurred copy), blue and black (panel_buzzsaw); a yellow diamond road sign (panel_wheel) with a cyan diamond glow; the words MONEY MANSION FEATURE in stacked orange capitals; white brush-stroke swirls and a flickering blue-white outline.
- **Style:** Road-works signage turned into title cards.
- **Rendering:** Glossy stripes with a soft highlight band; lettering is fat, outlined and bevelled; swirls are flat white strokes.
- **Colour:** Measured: black #08050a 28%, red #f50a04 11%, orange #f59d0a 8%, blue #1f49f9 3%: one stripe colour per feature.
- **Lighting:** Top light on the panels; glows as separate layers.
- **Ambience:** Urgent and playful, like a barrier going up.
- **Materials:** Painted metal sign, hazard tape.
- **Variants:** Three stripe colours and the diamond sign. Two part names (panel_buzzsaw, panel_wheel) come from the earlier Huff N' Puff games.
- **Motion:** From the skeleton file (13 bones, 10 slots, 7 animations): Door_feature and the two hammer_feature animations 1.3 s, wheel_intro and its loop 1.9 s, wheel_outro 1.5 s. Swirls are 20 and 26 drawn frames.
- **Construction:** One skeleton (file name fs_panels), one atlas page, 74 named parts.
- **Notes:** Only MONEY MANSION FEATURE is a drawn word here; the other feature names would be set in live text (inference).
- **Skeleton (from the file):** Spine 4.1.24 · 13 bones · 10 slots · animations: Door_feature (0 s), Door_feature_blur (0 s), hammer_feature (0 s), hammer_feature2 (0 s), wheel_intro (0 s), wheel_intro_loop (0 s), wheel_outro (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 37% · saturation 55% · contrast 62% · warm 64% / cool 28% · brighter towards: top (2), top-left (1)
- **Palette (measured):** #08050a black 28%, #d0cecd grey 12%, #f50a04 red 11%, #f59d0a orange 8%, #dbf1fa light cyan 7%, #2f285d dark blue 5%

### Big win stage dressing

`bigwin_assets` · atlas · 3 parts · largest 1100×1100 · sheet `sheets/bigwin_assets.webp`

- **Role:** Backdrop pieces for the big-win scene. Not seen on a real screen.
- **Subject:** A cyan burst of rays 1100 px across, a long strip of hedge and flowers (1890x227) and a picture of a clipped bush beside a cypress.
- **Style:** The garden of the background, reused as a stage.
- **Rendering:** Painted leaves with dotted highlights; the rays are soft with a white core.
- **Colour:** Measured: cyan #54c6d8 26%, dark teal #26494d 25%, white #f3fefe 14%, greens #4e7e2a 11% and #8cb737 3%; 83% cool.
- **Lighting:** The burst is the light source; plants are lit from above.
- **Ambience:** Open-air celebration.
- **Materials:** Foliage and light.
- **Variants:** One of each.
- **Motion:** Stills, moved by the big-win rig (it has a 'bushesh' animation of 0.3 s).
- **Construction:** One sheet, 3 frames.
- **Measured:** mid-tone, saturated, cool, medium contrast, strong highlights · brightness 57% · saturation 52% · contrast 48% · warm 5% / cool 83%
- **Palette (measured):** #54c6d8 cyan 26%, #26494d dark cyan 25%, #f3fefe light cyan 14%, #4e7e2a green 11%, #848353 yellow 7%, #9cf6f8 light cyan 6%

### Big win fireworks

`bigwin_firework` · atlas · 140 parts · largest 331×331 · sheet `sheets/bigwin_firework.webp`

- **Role:** Fireworks for the big win. Not seen on a real screen.
- **Subject:** Four bursts of small glowing dots, in yellow-orange, blue, green and red, each opening and fading.
- **Style:** Simple particle fireworks.
- **Rendering:** Soft dots with a white core (soft edge 93%).
- **Colour:** Measured: orange #ff9504 23%, red #fa0707 11%, blue #0725fa 11%, green #11fa05 10%: pure primaries.
- **Lighting:** Self-lit.
- **Ambience:** Festive.
- **Materials:** Light.
- **Variants:** Four colours on the same shape.
- **Motion:** 35 frames each; about 1.5 s at the stated 24 frames a second.
- **Construction:** One sheet on 4 pages, 140 frames of about 300 px.
- **Notes:** The four colours are the game's four jackpot tier colours less magenta (yellow for it); whether that is meant is not known.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 59% · saturation 78% · contrast 50% · warm 58% / cool 31% · brighter towards: bottom-left (6), right (4), bottom (2)
- **Palette (measured):** #ff9504 orange 23%, #f2e7dd light orange 11%, #fa0707 red 11%, #0725fa blue 11%, #11fa05 green 10%, #ff5300 orange 4%

### Jackpot tally backdrop

`jackpot_tally_assets_desktop` · atlas · 2 parts · largest 1000×1000 · sheet `sheets/jackpot_tally_assets_desktop.webp`

- **Role:** Two large pictures behind the jackpot tally. Not seen on a real screen.
- **Subject:** A brick wall lit hot orange in the middle, fading to dark at the floor with a purple band at the top (1000x1000), and a blue panel with a pale glow in its centre in a blue frame (900x457).
- **Style:** The mansion's brick, seen close.
- **Rendering:** Painted bricks course by course under a strong painted spotlight.
- **Colour:** Measured: orange #f47d17 21%, near-black #2e100f 19%, red #cd3c0f 15%, blues #1768f2 13% and #8fb5f9 9%.
- **Lighting:** A spotlight from above on the wall; the blue panel glows from its centre.
- **Ambience:** Stage-lit and warm for Grand, cool for Major (inference from the two colours).
- **Materials:** Brick, enamel.
- **Variants:** One wall, one panel.
- **Motion:** Stills.
- **Construction:** One sheet, 2 frames.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 38% · saturation 80% · contrast 58% · warm 66% / cool 32% · brighter towards: top (1)
- **Palette (measured):** #f47d17 orange 21%, #2e100f black 19%, #cd3c0f red 15%, #1768f2 blue 13%, #8fb5f9 light blue 9%, #812211 dark red 6%

### Win number flare

`bigwin` · atlas · 24 parts · largest 468×182 · sheet `sheets/bigwin.webp`

- **Role:** A burst of gold light behind the win amount (frames named fx_digits). Seen on a real frame: a $12.00 win is shown in fat red and gold digits on this flare across the bottom row of the reels, which is darkened under it. So it serves ordinary wins as well as the big win its file name suggests.
- **Subject:** A wide horizontal flare with rays and gold dust, 468x182, on black.
- **Style:** Lens-flare effect, the one photographic-looking piece in a drawn game.
- **Rendering:** Soft light on a black ground, meant to be added over the picture.
- **Colour:** Measured: golds #dcaf21 26%, #f9ec64 20%, browns #a9770f 17% and #71490d 11%; 100% warm.
- **Lighting:** It is the light.
- **Ambience:** Jackpot shine.
- **Materials:** Light and dust.
- **Variants:** One sequence.
- **Motion:** 24 frames; at the sheet's stated 24 frames a second, one second. One frame of it was caught in play.
- **Construction:** One 'Red 7 Exporter' sheet, 24 frames. A second sheet with the same file name (bigwin-hd) in another folder is the same file byte for byte; the prepared files keep one.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 62% · saturation 72% · contrast 63% · warm 100% / cool 0%
- **Palette (measured):** #dcaf21 gold 26%, #f9ec64 gold 20%, #a9770f brown 17%, #331f06 black 12%, #71490d brown 11%, #feffeb light gold 9%

### Big win falling pieces

`bigwin_particles` · atlas · 4 parts · largest 145×143 · sheet `sheets/bigwin_particles.webp`

- **Role:** Small pictures thrown about during a big win. Not seen on a real screen.
- **Subject:** A gold hard hat, an ear of wheat, a gold coin with a pig's face and a green banknote with a pig's head between two dollar signs.
- **Style:** The game's own objects as confetti.
- **Rendering:** Clean cartoon icons with outline and gloss, about 140 px.
- **Colour:** Measured: gold #efbd14 34% and #feef7f 19%, banknote greens #65e183 11% and #038e0c 5%.
- **Lighting:** Top light.
- **Ambience:** Money raining.
- **Materials:** Plastic, gold, paper.
- **Variants:** Four pieces.
- **Motion:** Stills, to be scattered by a particle emitter (inference).
- **Construction:** One sheet, 4 frames.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 71% · saturation 72% · contrast 58% · warm 80% / cool 10%
- **Palette (measured):** #efbd14 gold 34%, #feef7f gold 19%, #65e183 green 11%, #d66e04 orange 10%, #fdf8c9 light gold 6%, #038e0c dark green 5%


## Effects

Frame sequences, glows, particles and transitions.

### Caution-tape transition

`fstally` · atlas · 5 parts · largest 2130×373 · sheet `sheets/fstally.webp`

- **Role:** The wipe between the base game and a feature (animations transition_landscape and transition_portrait). Not seen on a real screen.
- **Subject:** Two lengths of yellow and black caution tape (2130x373 and 1692x359), a roll of yellow tape, a black square and a star glint.
- **Style:** The building-site motif used as a curtain.
- **Rendering:** Glossy tape with a highlight along its length.
- **Colour:** Measured: black #050404 37%, yellows #edc332 23% and #fef876 17%.
- **Lighting:** Top-right light on the tape.
- **Ambience:** Work in progress.
- **Materials:** Plastic tape.
- **Variants:** Landscape and portrait versions of the move.
- **Motion:** From the skeleton file (25 bones, 18 slots): both transitions 1.75 s. The rig's own size is 5205x1927, so the tapes sweep well past the screen.
- **Construction:** One skeleton (file name tally), one atlas page, 5 parts.
- **Notes:** A whole transition from five small pictures.
- **Skeleton (from the file):** Spine 4.1.24 · 25 bones · 18 slots · animations: transition_landscape (0 s), transition_portrait (0 s)
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 44% · saturation 37% · contrast 80% · warm 84% / cool 0% · brighter towards: top-right (1)
- **Palette (measured):** #050404 black 37%, #edc332 gold 23%, #fef876 gold 17%, #3e3c36 grey 16%, #ffffb5 light gold 4%

### The mansion's gold door

`door` · atlas · 31 parts · largest 386×416 · sheet `sheets/door.webp`

- **Role:** The gold double door that opens in a blaze of light. By its place in the files it belongs to the base game; that it is the door of the Money Mansion feature is inference. Not seen on a real screen.
- **Subject:** A panelled gold double door seen head-on, turning open over 29 frames until only its two edges show, and a white-hot rectangle of light with an orange halo.
- **Style:** Realistic gold door in a cartoon world: it reads as a 3D-rendered turn (inference from the even perspective across the frames).
- **Rendering:** Smooth metal shading with moulded panels; the glow is a soft additive burst.
- **Colour:** Measured: gold-brown #ae7a1b 53%, #6b4912 14%, bright gold #f4bc29 11%, white #fffffa 10%; 100% warm.
- **Lighting:** Lit from the top; then flooded from behind by the glow.
- **Ambience:** A vault opening.
- **Materials:** Polished gold.
- **Variants:** One door, two glow frames.
- **Motion:** From the skeleton file (4 bones, 6 slots, 4 animations): door_anticipation 0.7 s, door_open_WithGlow 2.0 s with a 2.0 s loop, door_close 0.7 s. The door turn is a 29-frame sequence.
- **Construction:** One skeleton, atlas on 2 pages, 31 parts.
- **Notes:** On the base-game screen a gold double door stands at the foot of the mansion under the reels.
- **Skeleton (from the file):** Spine 4.1.24 · 4 bones · 6 slots · animations: door_anticipation_without_mask (0 s), door_close (0 s), door_open_WithGlow (0 s), door_open_WithGlow_loop (0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 56% · saturation 74% · contrast 48% · warm 100% / cool 0% · brighter towards: top (6), bottom (1)
- **Palette (measured):** #ae7a1b orange 53%, #6b4912 brown 14%, #f4bc29 orange 11%, #fffffa light gold 10%, #fdf951 gold 5%

### Paint pouring down a reel

`touchup-paint_dripping` · atlas · 119 parts · largest 243×803 · sheet `sheets/touchup-paint_dripping.webp`

- **Role:** The yellow paint that covers a reel in the Touch-Up feature (inference from the names and the client's text). Not seen on a real screen.
- **Subject:** A tall column of yellow-orange paint the width of a reel (243x803) with gold flecks, a white shine, a wavy leading edge, and a 114-frame sequence of drips running down from a line.
- **Style:** Flat cartoon paint.
- **Rendering:** Flat fill with a soft gradient; drips are simple rounded shapes.
- **Colour:** Measured: yellow #fcc206 77%, white 16%, orange #e18212 5%.
- **Lighting:** A white shine passes over it.
- **Ambience:** Satisfying, like a roller covering a wall.
- **Materials:** Wet gloss paint.
- **Variants:** From the top and from the bottom.
- **Motion:** From the skeleton file (7 bones, 9 slots): paint_dripping_fromTop and fromBottom, 4.3 s each.
- **Construction:** One skeleton, one atlas page, 119 parts; the rig's own size is 244x558, one reel of three rows.
- **Skeleton (from the file):** Spine 4.1.24 · 7 bones · 9 slots · animations: paint_dripping_fromBottom (0 s), paint_dripping_fromTop (0 s)
- **Measured:** bright, vivid, warm, low contrast, strong highlights · brightness 78% · saturation 82% · contrast 16% · warm 84% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #fcc206 gold 77%, #fefefe light yellow 16%, #e18212 orange 5%, #eec142 orange 2%

### Hammer (Home Improvement)

`hammer` · atlas · 127 parts · largest 666×670 · sheet `sheets/hammer.webp`

- **Role:** The claw hammer of the loading screen's 'brush OR hammer' card. By the client's text the grid grows to 4 rows in the HOME IMPROVEMENT FEATURE, and this rig holds the growing reel frame, so the hammer is taken to be that feature's prop (inference). Seen on a real screen only on the loading card.
- **Subject:** A claw hammer with a steel head, a cyan shaft and an orange rubber grip, idle (48 frames), spinning (19 frames), blurred and as a white glow; a blueprint tile behind it; impact sparks and white splashes; a dust cloud over a dark blue 5-reel frame that grows taller over 30 frames.
- **Style:** Chunky toy tool with high gloss.
- **Rendering:** Smooth 3D-looking shading on the hammer with a magenta rim on the grip; effects are flat white shapes.
- **Colour:** Measured: the reel frame's dark blue #0f115b 39% and #222e9c 5%, steel whites #ecf6f8 21% and #bcdceb 8%, orange #f65914 3%; 78% cool.
- **Lighting:** Top-right light on the hammer (48 of 87 measured), with a bright highlight on the head.
- **Ambience:** Energetic: a bang, dust, and the board gets bigger.
- **Materials:** Polished steel, rubber grip, blueprint paper.
- **Variants:** Idle, spin, blur and glow versions of the one hammer.
- **Motion:** From the skeleton file (11 bones, 15 slots, 11 animations): Hammer_ideal 3.7 s, Hammer_Hit 2.6 s, Hit2 2.0 s, Hit3 1.5 s, single bangs 0.3 s, hammer_bang_on_reelframe_growth 1.2 s, anticipation 0.7 s.
- **Construction:** One skeleton, atlas on 6 pages, 127 named parts.
- **Notes:** 'ideal' in the file names is the artists' spelling of idle.
- **Skeleton (from the file):** Spine 4.1.24 · 11 bones · 15 slots · animations: BG_anticipation (0 s), Hammer_anticipation (0 s), hammer_bang_FX (0 s), hammer_bang_on_reelframe_growth (0 s), hammer_bang_single (0 s), Hammer_Hit (0 s), Hammer_Hit2 (0 s), Hammer_Hit3 (0 s), Hammer_ideal (0 s), reelframe_growth_static (0 s), woithOut_hammer_reelframe_growth (0 s)
- **Measured:** mid-tone, saturated, cool, high contrast, strong highlights · brightness 43% · saturation 54% · contrast 65% · warm 16% / cool 78% · brighter towards: top-right (48), top (35), bottom-left (4)
- **Palette (measured):** #0f115b dark blue 39%, #ecf6f8 light cyan 21%, #bcdceb light cyan 8%, #010101 black 5%, #222e9c blue 5%, #f65914 orange 3%

### Paint brush (Touch-Up)

`touchup-paint_brush` · atlas · 83 parts · largest 564×1127 · sheet `sheets/touchup-paint_brush.webp`

- **Role:** The paint brush of the loading screen's 'brush OR hammer' card. By the client's text, in the TOUCH-UP FEATURE 2 to 5 reels are painted over before the free spins; this is that feature's prop. Seen on a real screen only on the loading card.
- **Subject:** A wide brush with white bristles loaded with dripping yellow paint, a steel ferrule and an orange handle with a hang hole; it spins (11 frames), blurs, glows white and throws stars; a gold tile with a brick wall half painted yellow stands behind it.
- **Style:** Chunky toy tool, like the hammer.
- **Rendering:** Glossy gradients with a strong highlight on the handle; the paint is a flat yellow with a lighter rim.
- **Colour:** Measured: pale yellow #fdf8c0 44%, orange #fb6f0d 15%, yellow #fbf334 6%, red #f91b08 5%; 96% warm.
- **Lighting:** Top light (23 of 27 measured).
- **Ambience:** Light-hearted; decorating as a prize.
- **Materials:** Bristle, wet paint, steel, lacquered wood.
- **Variants:** Idle, three painting poses, spin, blur, glow and shadow.
- **Motion:** From the skeleton file (16 bones, 18 slots, 8 animations): Paint_brush_ideal 4.0 s, hold_and_extract 3.3 s, highlights 2.0 s, three 'twril_to_reel' moves of 0.8 to 0.9 s. Star particles are a 26-frame sequence.
- **Construction:** One skeleton, atlas on 5 pages, 83 named parts.
- **Notes:** Brush and hammer are a pair: same grip colour, same gloss, same blur and glow layers, same splash frames (fx_00143 to fx_00156 are in both).
- **Skeleton (from the file):** Spine 4.1.24 · 16 bones · 18 slots · animations: hold_and_extract (0 s), paint_brush static (0 s), Paint_brush_highlight (0 s), Paint_brush_ideal (0 s), Paint_tile_highlight (0 s), twril_to_reel_seq01 (0 s), twril_to_reel_seq03 (0 s), twril_to_reel_seq04 (0 s)
- **Measured:** bright, saturated, warm, medium contrast, strong highlights · brightness 81% · saturation 44% · contrast 47% · warm 96% / cool 3% · brighter towards: top (23), top-right (3), top-left (1)
- **Palette (measured):** #fdf8c0 light gold 44%, #fb6f0d orange 15%, #f8fefc light cyan 11%, #fbf334 gold 6%, #f91b08 red 5%

### Wolf's wind with debris

`windbrickc` · atlas · 165 parts · largest 960×540 · sheet `sheets/windbrickc.webp`

- **Role:** A second wind sequence in which the gust carries rubble (frames named wolf_wind_bricks). Not seen on a real screen.
- **Subject:** White streaks across a 960x540 frame filled with tan chunks of rubble.
- **Style:** Hand-drawn wind with flat debris.
- **Rendering:** Soft strokes and flat two-tone chunks.
- **Colour:** Measured: tan #b6aa86 63%, white #fefefd 27%, darker tan #887c5b 6%.
- **Lighting:** None.
- **Ambience:** Demolition.
- **Materials:** Dust and broken masonry.
- **Variants:** One sequence.
- **Motion:** 165 frames; about 6.9 s at the stated 24 frames a second.
- **Construction:** One sheet on 23 pages of half-screen frames.
- **Notes:** With the plain wind this is 301 full-width frames, 32 pages, for one gust: the second largest drawn animation after the wolf.
- **Measured:** bright, muted, warm, medium contrast, glow or soft effect, strong highlights · brightness 75% · saturation 20% · contrast 26% · warm 81% / cool 0% · brighter towards: left (1)
- **Palette (measured):** #b6aa86 yellow 63%, #fefefd light gold 27%, #887c5b orange 6%, #e1d9ba light yellow 3%

### Star glints

`center_particles` · atlas · 5 parts · largest 121×112 · sheet `sheets/center_particles.webp`

- **Role:** Small glints for the big-win scene (folder newbigwin/centerparticles). Not seen on a real screen.
- **Subject:** Four four-pointed glints in green, red, violet and yellow, and a round yellow star.
- **Style:** Standard sparkle.
- **Rendering:** Soft glow with a white core (soft edge 97%).
- **Colour:** Measured: yellow #e8cd5a 36%, green #7cff5a 11%, violet #d956ff 10%, red #ff4c4b 8%.
- **Lighting:** Self-lit.
- **Ambience:** Twinkle.
- **Materials:** Light.
- **Variants:** Five.
- **Motion:** Stills for a particle emitter (inference).
- **Construction:** One sheet, 5 frames of about 120 px.
- **Measured:** bright, saturated, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 74% · saturation 57% · contrast 20% · warm 66% / cool 21%
- **Palette (measured):** #e8cd5a gold 36%, #7cff5a green 11%, #f9f6f1 light orange 10%, #d956ff purple 10%, #ff4c4b red 8%, #fceb9f light gold 6%

### Fire dragon (a stray)

`dragon_in` · atlas · 57 parts · largest 512×512 · sheet `sheets/dragon_in.webp`

- **Role:** A 57-frame sequence of a dragon of fire coiling into a figure 8. The manifest lists it with the base game (Game.Dragon.Dragon), but nothing in this game's theme, text or screens uses a dragon; it looks like art from another title left in the build (inference). Not seen on a real screen.
- **Subject:** A Chinese-style dragon made of flame, drawing a burning figure 8 on black.
- **Style:** Realistic fire, unlike anything else in the game.
- **Rendering:** Photographic-looking flame on black, JPEG pages.
- **Colour:** Measured: orange #f0872e 31%, browns #361a0a 17% and #874116 17%; 100% warm.
- **Lighting:** Self-lit.
- **Ambience:** Does not belong to this game's mood.
- **Materials:** Fire.
- **Variants:** One sequence.
- **Motion:** 57 frames of 512x512; about 2.4 s at 24 frames a second.
- **Construction:** One sheet on 4 JPEG pages.
- **Notes:** Left out of the art direction below. A build can carry another game's files; an art inventory should say so rather than read them as design.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 50% · saturation 72% · contrast 54% · warm 100% / cool 0%
- **Palette (measured):** #f0872e orange 31%, #361a0a brown 17%, #874116 brown 17%, #f0c36c orange 13%, #f5e4aa light gold 10%, #be5b1e orange 9%

### Dust puff

`freespins_particle` · atlas · 1 parts · largest 191×177 · sheet `sheets/freespins_particle.webp`

- **Role:** One soft beige blob, by its folder a particle of the free spins. Not seen on a real screen.
- **Subject:** A rounded tan cloud shape, 191x177, half transparent.
- **Style:** Flat cartoon dust.
- **Rendering:** Two flat tones with a soft edge.
- **Colour:** Measured: #b7ab85 87%, #867c59 13%.
- **Lighting:** None.
- **Ambience:** Dry dust.
- **Materials:** Dust.
- **Variants:** One.
- **Motion:** A still for a particle emitter (inference).
- **Construction:** One sheet, one frame.
- **Notes:** The same tan as the debris in the wind sequences.
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect · brightness 64% · saturation 28% · contrast 19% · warm 100% / cool 0%
- **Palette (measured):** #b7ab85 yellow 87%, #867c59 yellow 13%

### Wolf's wind (free spins)

`wind` · atlas · 136 parts · largest 960×540 · sheet `sheets/wind.webp`

- **Role:** The wind the wolf blows across the screen in the free spins (folder freespins). Not seen on a real screen.
- **Subject:** White streaks sweeping across a 960x540 frame, carrying small yellow straws.
- **Style:** Hand-drawn wind lines.
- **Rendering:** Thin soft strokes, mostly transparent.
- **Colour:** Measured: white #fffffc 70%, straw yellow #fedb05 24%.
- **Lighting:** None.
- **Ambience:** A gust.
- **Materials:** Air and straw.
- **Variants:** One sequence.
- **Motion:** 136 frames at 960x540; about 5.7 s at the stated 24 frames a second.
- **Construction:** One sheet on 9 pages; frames are stored at half the screen size, to be scaled up (inference from 960x540).
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect, strong highlights · brightness 95% · saturation 27% · contrast 10% · warm 82% / cool 0%
- **Palette (measured):** #fffffc light gold 70%, #fedb05 gold 24%, #fdf1a4 light gold 4%, #fce863 gold 3%


## Game interface

Buttons, counters and panels drawn for this game.

### Construction pig (paytable picture)

`c_pig_sym` · atlas · 1 parts · largest 192×246 · sheet `sheets/c_pig_sym.webp`

- **Role:** The Construction Pig as the paytable shows him. The paytable page with him was not reached in this run.
- **Subject:** A laughing pink pig in an orange hard hat with the pig badge, a white vest and yellow hi-vis braces, head and shoulders, with a white outline and a thin red one.
- **Style:** Sticker-like mascot.
- **Rendering:** Soft shading inside a clean double outline.
- **Colour:** Measured: pinks #e8cfd4 24% and #f89b9a 19%, yellow #f8e017 13%, orange #f37b0b 10%; 100% warm.
- **Lighting:** Front and top light.
- **Ambience:** Friendly.
- **Materials:** Skin, cloth, plastic.
- **Variants:** One picture.
- **Motion:** Still; the hat_pig rig animates the same pig.
- **Construction:** One PNG of 192x246.
- **Measured:** bright, saturated, warm, high contrast, hard-edged, strong highlights · brightness 67% · saturation 52% · contrast 72% · warm 100% / cool 0%
- **Palette (measured):** #e8cfd4 light red 24%, #f89b9a light red 19%, #f8e017 gold 13%, #f37b0b orange 10%, #eb5f5d red 8%, #bd351a red 7%

### Prize meters on the mansion

`jackpot_meters` · atlas · 324 parts · largest 587×582 · sheet `sheets/jackpot_meters.webp`

- **Role:** The prize board of the Money Mansion feature, placed on the mansion's front. The base-game screen shows part of it: five gold-zone plates on the roof reading x3750, x4000, x750, x2500, x1250, and dimmer plates (x30, x60 and x75 can be read) through the reel window.
- **Subject:** Plates and numbers: a GRAND plate in red and gold, a MAJOR plate in blue with a white frame, MINOR and MINI neon plaques, gold-brick and blue-brick frames, eight smaller dark plates in blue or silver frames, and multiplier numbers from x5 up to x4000 as lettered sprites, each in a normal and a highlighted state; glitter, particle bursts and a white flash.
- **Style:** Scoreboard set into architecture: every prize is a framed window on the house.
- **Rendering:** Bevelled frames with flat dark glass; numbers are fat outlined digits in white-to-red (gold zone), white-to-blue (blue zone) or pale gold and blue (bottom row), each with a glow copy.
- **Colour:** Measured: 47% is the white of flashes and glitter; then near-black #10080e 10%, blue #047ff7 5% and #042565 5%, yellow #faee19 5%, red #fb0501 3%. Zones are colour-coded: gold and red at the top, blue in the middle, dark at the bottom.
- **Lighting:** Top highlight on the frames; win states are made by a brighter copy of the same plate.
- **Ambience:** Game-show prize wall.
- **Materials:** Gold brick, blue brick, enamel, neon tube, dark glass.
- **Variants:** Every plate and number in a resting and a highlight state; day versions of the eight bottom plates (bottom_jp_01_day) and a day-to-night animation for each, to follow the background.
- **Motion:** From the skeleton file (Spine 4.1.24, 51 bones, 61 slots, 77 animations): each meter has a 1.7 s animation and a 0.8 s stop; highlights 0.8 s; sparkles 1.6 s; the Grand and Major multiplier animations 2.9 s; day-to-night 2.0 s. Glitter is a 72-frame sequence, the highlight sweeps 47 and 48 frames. Only the resting state was seen on a real screen.
- **Construction:** One skeleton whose atlas has 54 pages and 324 named parts; the rig's own size is 337x351.
- **Notes:** By the client's text the gold zone runs 750x to 4000x, the blue zone 250x to 500x and the bottom eight 5x to 75x of the bet: the art's three colour zones follow the three prize bands exactly.
- **Skeleton (from the file):** Spine 4.1.24 · 51 bones · 61 slots · animations: blue_JP1 (0 s), blue_JP1_stop (0 s), blue_JP2 (0 s), blue_JP2_stop (0 s), blue_JP3 (0 s), blue_JP3_stop (0 s), blue_JP4 (0 s), blue_JP4_stop (0 s), bottom_jp_01 (0 s), bottom_jp_01_day (0 s), bottom_jp_01_day_night_anim (0 s), bottom_jp_01_stop (0 s), bottom_jp_01_stop_sparkle (0 s), bottom_jp_02 (0 s), bottom_jp_02_day (0 s), bottom_jp_02_day_night_anim (0 s), bottom_jp_02_stop (0 s), bottom_jp_02_stop_sprakle (0 s), bottom_jp_03 (0 s), bottom_jp_03_day (0 s), bottom_jp_03_day_night_anim (0 s), bottom_jp_03_stop (0 s), bottom_jp_03_stop_sparkle (0 s), bottom_jp_04 (0 s), bottom_jp_04_Day (0 s), bottom_jp_04_day_night_anim (0 s), bottom_jp_04_stop (0 s), bottom_jp_04_stop_sparkle (0 s), bottom_jp_05 (0 s), bottom_jp_05_Day (0 s), bottom_jp_05_day_night_anim (0 s), bottom_jp_05_stop (0 s), bottom_jp_05_stop_sparkle (0 s), bottom_jp_06 (0 s), bottom_jp_06_Day (0 s), bottom_jp_06_day_night_anim (0 s), bottom_jp_06_stop (0 s), bottom_jp_06_stop_sparkle (0 s), bottom_jp_07 (0 s), bottom_jp_07_Day (0 s), bottom_jp_07_day_night_anim (0 s), bottom_jp_07_stop (0 s), bottom_jp_07_stop_sparkle (0 s), bottom_jp_08 (0 s), bottom_jp_08_Day (0 s), bottom_jp_08_day_night_anim (0 s), bottom_jp_08_stop (0 s), bottom_jp_08_stop_sparkle (0 s), glitter (0 s), Grand (0 s), Grand_multiplier (0 s), Grand_multiplier_loop (0 s), Grand_stop (0 s), Grand_title (0 s), Grand_wall_highlight (0 s), JP_01 (0 s), JP_01_highlight (0 s), JP_02 (0 s), JP_02_highlight (0 s), JP_03 (0 s), JP_03_highlight (0 s), JP_04 (0 s), JP_04_highlight (0 s), JP_05 (0 s), JP_05_highlight (0 s), j_glow (0 s), loop_particle (0 s), Major (0 s), Major_multiplier_anim (0 s), Major_multiplier_title (0 s), Major_stop (0 s), Mini (0 s), Mini_sparkle (0 s), Mini_stop (0 s), Minor (0 s), Minor_sparkle (0 s), Minor_stop (0 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 70% · saturation 38% · contrast 28% · warm 24% / cool 50% · brighter towards: top (21), bottom (5), top-right (1)
- **Palette (measured):** #fdfefe light cyan 47%, #10080e black 10%, #047ff7 blue 5%, #faee19 gold 5%, #7f7f7e grey 5%, #042565 dark blue 5%

### Press-to-start button

`ui` · atlas · 2 parts · largest 608×163 · sheet `sheets/ui.webp`

- **Role:** A long pill button in two states; by its name (btn_clicktostart) and the client's text PRESS TO START it starts a feature. Not seen on a real screen.
- **Subject:** An orange-gold pill with a pale blue metal rim, and a brighter yellow hover state.
- **Style:** Glossy toy button.
- **Rendering:** Gradient fill with a soft top gloss.
- **Colour:** Measured: orange #fabc2e 33%, pale gold #ffeb9d 18%, rim blues #d7f2f5 16% and #8db4c0 9%.
- **Lighting:** Top light.
- **Ambience:** Friendly and obvious.
- **Materials:** Glossy plastic in a brushed metal rim.
- **Variants:** Base and hover.
- **Motion:** Still states.
- **Construction:** One sheet, 2 frames of 608x163; the label is live text.
- **Measured:** bright, saturated, warm, high contrast, hard-edged, strong highlights · brightness 74% · saturation 52% · contrast 63% · warm 83% / cool 14% · brighter towards: top (1)
- **Palette (measured):** #fabc2e orange 33%, #ffeb9d light gold 18%, #d7f2f5 light cyan 16%, #8db4c0 cyan 9%, #ffe66f gold 6%, #5a716f grey 5%

### Buy Pass button and title

`buypass_desktop` · atlas · 5 parts · largest 459×118 · sheet `sheets/buypass_desktop.webp`

- **Role:** The game's Buy Pass button in four states and the title of its panel. Not on the base-game screen of this demo, and the panel was not opened.
- **Subject:** BUY PASS in fat slanted capitals, purple with a gold edge, on a dark blue oval with a gold rim; a grey disabled state; a wide one-line title.
- **Style:** The provider's shared Buy Pass mark, the same shape as in Huff N' Even More Puff Grand.
- **Rendering:** Bevelled letters with a gloss band and a thick extrusion.
- **Colour:** Measured: dark magenta #3a223e 30%, purple #47045b 12%, brown-gold #793c0d 6%.
- **Lighting:** Top light.
- **Ambience:** A premium offer, set apart from the game's warm palette by its purple.
- **Materials:** Enamel and gold.
- **Variants:** Base, hover, press, disabled; the one-line title.
- **Motion:** Still states.
- **Construction:** One sheet of 5 frames, 163x127 for the button.
- **Notes:** It is the provider's brand mark for a paid feature, so it keeps its own colours whatever the game.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 35% · saturation 59% · contrast 81% · warm 54% / cool 43% · brighter towards: top (1)
- **Palette (measured):** #3a223e dark magenta 30%, #47045b dark purple 12%, #0a0321 black 6%, #793c0d brown 6%, #785f6f grey 6%, #faf5e7 light orange 5%

### Paytable pictures

`help` · atlas · 8 parts · largest 222×213 · sheet `sheets/help.webp`

- **Role:** Pictures the paytable uses beside its rules: the hat, the three houses and the three frames. The paytable's first page is on a real screen (the payouts of the five picture symbols at a $2.00 bet, on a dark blue panel under the logo); the lower pages, where these pictures are used, were not reached.
- **Subject:** The hard hat on its dotted orange backing, the brick mansion, the log cabin and the straw hut, the gold-brick, red-plank and plaited-straw frames, and a grey loading ring.
- **Style:** The reel art at paytable size.
- **Rendering:** As the houses rig and the reel stills.
- **Colour:** Measured: gold #ebc019 17%, orange #d5560f 12%; vivid (saturation 70%).
- **Lighting:** Top and top-left light.
- **Ambience:** Clear and explanatory.
- **Materials:** Plastic, brick, logs, straw.
- **Variants:** House and frame for each of the three tiers.
- **Motion:** Stills.
- **Construction:** One sheet, 8 frames of about 210 to 233 px.
- **Notes:** The paytable's own words give the tiers their names: STRAW FRAME, STICK FRAME, BRICK FRAME and the matching houses.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 48% · saturation 70% · contrast 79% · warm 76% / cool 17% · brighter towards: top (1), top-left (1)
- **Palette (measured):** #ebc019 gold 17%, #d5560f orange 12%, #140609 black 7%, #eeefeb white 5%

### Jackpot plaques (states)

`jackpot` · atlas · 18 parts · largest 301×128 · sheet `sheets/jackpot.webp`

- **Role:** The four jackpot plaques in their lit and highlighted states, with the shadow and thickness pieces that give them depth. The base-game screen shows them down the left with their amounts.
- **Subject:** GRAND (red field, gold frame, hazard-striped tab), MAJOR (blue field, white frame), MINOR (green neon), MINI (magenta neon), each as 'on' and 'highlight'; side and bottom slabs in dark red and in iridescent blue-white.
- **Style:** Fairground signage with a building-site tab.
- **Rendering:** Glossy bevels, neon rims with a white core, flat fields.
- **Colour:** Measured: dark fields #1d061b 26% and #023501 9%, red #fe0101 8%, blue #0b40fc 6%, yellow #fcec0e 3%; saturation 79%.
- **Lighting:** Top light (7 of 9 measured).
- **Ambience:** Bright promise at the edge of the screen.
- **Materials:** Enamel, neon tube, gold trim.
- **Variants:** Four tiers by two states.
- **Motion:** Stills; the jackpot meters rig animates the same plaques.
- **Construction:** One 'Red 7 Exporter' sheet, 18 frames, the largest 301x128.
- **Notes:** One colour per tier everywhere in the game: red Grand, blue Major, green Minor, magenta Mini.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 35% · saturation 79% · contrast 79% · warm 41% / cool 45% · brighter towards: top (7), top-right (1), top-left (1)
- **Palette (measured):** #1d061b black 26%, #023501 black 9%, #fe0101 red 8%, #0b40fc blue 6%, #f2fbfb light cyan 5%, #7c0f03 dark red 5%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `notosans`: 4 parts
- `check`: 1 parts
- `lnw_logo`: 1 parts
- `no_check`: 1 parts
- `progressbar_ninepatch`: 1 parts
- `ui_icon_replay`: 1 parts
- `info`: 1 parts
- `autospins`: 1 parts
- `autospinsrectangle`: 1 parts
- `buypass`: 1 parts
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
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 3579 components cut from 349 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
