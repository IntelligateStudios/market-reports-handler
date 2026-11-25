# Zeus vs Hades POP: art report

pragmatic · run `2026-11-24-1733-pragmatic-zeus-vs-hades-pop` · captured 2026-11-24

Source: the provider's free-play demo, https://demogamesfree.pragmaticplay.net/gs2c/openGame.do?gameSymbol=vs10zsvhdspp&websiteUrl=https%3A%2F%2Fdemogamesfree.pragmaticplay.net&jurisdiction=99&lobby_url=https%3A%2F%2Fwww.pragmaticplay.com%2Fen%2F&lang=en&cur=USD

**Extracted:** 3550 named components from 243 textures in 235 atlases; 39 Spine skeletons; 217 frame sequences (1578 frames); 22 fonts. Grouped into 110 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A two-sided cartoon mythology: Zeus's blue storm sky against Hades's red lava underworld, drawn as stylised 3D-look paintings with polished gold as the trim that holds both sides together, and a third, candy-bright register reserved for the POP prize feature.

**Style.** Stylised 3D-look digital painting in a family-animation manner. Characters have large heads, barrel torsos and big hands; Zeus is round and friendly, Hades angular with spikes, pointed ears and claws; Pegasus is cute and pastel. Low symbols are extruded slab-serif letters. Architecture (temple, prize bar, logo slab) is chunky carved stone with Greek key borders.

**Rendering.** Smooth gradients that read like a soft 3D render, clean hard silhouettes and no line outlines anywhere. Detail is concentrated in faces, gold trim and jewellery; backgrounds are soft-focus paintings kept low in detail so the board reads first. Effects are the opposite: thin, sharp, bright shapes with glow.

**Colour.** Two opposed families and one shared metal. Zeus and the base game: cyan and blue (#22efff, #2b7cf2, #3986ce, #324382). Hades and free spins: red, orange and dark crimson (#8e1f15, #540e19, #d92d11, #f49419). Gold (#f9ea77, #f49419) trims every symbol and frame on both sides. Purple marks what belongs to neither god (the VS coin's galaxy, the Ace, cloth shadows). Lime, pink and cyan neon appear only on the three POP prize fields. Measured over the game's own art: vivid (saturation 63%), mid-tone, warm 54% against cool 40%.

**Lighting.** Each side is lit by its own element: cool cyan light from lightning on Zeus pieces, warm light from fire on Hades pieces, usually against the opposite temperature in the shadows (purple-blue shadows on warm skin). Bevels are top-lit. Lightning, fire, frame edges and eyes are emissive and drawn as separate additive layers, so glow is a layer, not paint.

**Ambience.** A playful rivalry rather than a solemn myth: loud, bright, friendly menace. The base game is an airy storm sky, calm between flashes; free spins is a hot, busy underworld of lava falls, chains and stone pillars. POP moments switch to soap bubbles and pastel rainbow, closer to a casual mobile game than to the Greek set.

**Shape language.** Rounded and chunky throughout, with angular accents (spikes, zigzag lightning, flames) reserved for power and danger. Frames are thin rails with Greek-key corners; figures break out of their frames.

**Materials.** Polished gold with engraved Greek key, white cloth in broad folds, matte skin, sculpted hair in large locks, blue marble and ice-blue crystal, cut gems, lava and fire, cloud, bone and skulls, soap bubbles and glossy candy plastic for POP.

**Typography and lettering.** Display lettering is drawn art, not type: ice-blue faceted ZEUS, gold flaming HADES and a gold bubble POP in the logo; bevelled gold words for the win tiers; extruded letters with a gold rim for A, K, Q and J. Seventeen typefaces are embedded for running text and numbers, most of them the provider's interface faces.

**Motion.** Spine 3.7 skeletons carry almost all movement: symbols have landing (0.5 s), win (1.5 s) and sometimes idle and anticipation animations; the two mascots have six each (idle, idle break, two annoyed, two win). Fire, lightning, hair and sparkle are short hand-drawn frame sequences (3 to 21 frames) played inside the rigs. The expanding VS symbol plays as a duel with two outcomes, fire for Hades and lightning for Zeus. The scene transition is a video-like run of 25 full frames that shows Hades, then Zeus, then breaks open from the centre.

**Variants and themes.** Nearly everything exists twice, as a blue base-game version and a red free-spins recolour: backgrounds, reel frame, backing, rails, bars, reel highlights and win-meter effects. Each reel symbol ships as a sharp still, a vertically smeared still (probably the spin blur: inference) and a skeleton. Win tiers are split between the gods: Zeus carries Mega and Sensational, Hades carries Nice and Superb. The three POP result banners (Burst magenta, Spark blue, Snap green) are one design recoloured.

**How it is built.** 3,550 named sprites on 243 textures, 39 skeletons. A character is 73 to 221 parts, with a painted shadow piece for nearly every overlapping part and separate additive glow layers; meshes are used for cloth, hair and faces, regions for rigid parts. The four royals share one 9 to 10 part template: a coloured letter face with flickering lightning at rest, and a lava-cell picture that fills the face, clipped to the letter, during the win. Atlas textures are shipped at 50 to 69% of the source art and as 8-bit palette PNGs. The reel board is deliberately plain (flat backing, thin frame, gold dividers); the prize bar is its one decorated piece.

**Consistency.** The Greek set is tight: one rendering manner, one frame construction, one gold. Three things sit outside it and look like shared platform art or a different hand: the POP bubble symbol and banners (glossy candy style), the flat gold title plates in the big-win atlas, and loose shared sprites such as number fonts, coins and a red envelope (inference).

**What to take from it.** (1) Colour does the storytelling: one hue family per side, the opposite temperature in the shadows, and one metal shared by both. A recolour of the same asset is enough to say which mode you are in. (2) Glow, shadow and fire are separate layers on every character. That is what lets a painted figure animate in Spine without repainting, and it is the part a generated image does not give you by itself. (3) The board is kept quiet so that symbols and characters carry the detail; decoration is spent on one piece (the prize bar). (4) A feature can have its own visual register (POP's candy pastel) as long as it is confined to that feature's symbols, bar fields and banners.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast · brightness 50% · saturation 63% · contrast 45% · warm 54% / cool 40% · brighter towards: top (134), top-left (127), bottom-right (94)

Palette: #540e19 dark red 7%, #f49419 orange 6%, #f3f4f2 white 6%, #8e1f15 red 4%, #2b2c64 dark blue 4%, #f9ea77 gold 4%, #0e0509 black 4%, #1cf2f7 cyan 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 8 | 39% | 68% | 44% | 35% / 64% | #3b82cd blue 32%, #2d4e9f blue 17%, #a43633 red 16% |
| Reel board | 16 | 26% | 76% | 19% | 55% / 37% | #45000d dark red 42%, #1f215a dark blue 24%, #6dc0e2 cyan 6% |
| Symbols | 23 | 52% | 68% | 47% | 62% / 33% | #881209 dark red 14%, #f6ecf0 light magenta 8%, #4f2c66 dark purple 5% |
| Characters | 10 | 46% | 65% | 46% | 72% / 25% | #8e2e23 red 24%, #eb701f orange 14%, #f5b533 orange 6% |
| Logo and title | 1 | 77% | 44% | 48% | 83% / 17% | #feffff light cyan 42%, #ef9021 orange 37%, #87baf3 blue 4% |
| Win celebrations and banners | 13 | 56% | 60% | 43% | 55% / 37% | #efb341 orange 9%, #f3f3f1 white 8%, #580f1d dark red 8% |
| Effects | 8 | 53% | 60% | 53% | 50% / 42% | #faa110 orange 11%, #040304 black 10%, #a2e7fb light cyan 7% |
| Game interface | 2 | 37% | 88% | 64% | 79% / 21% | #ca0915 red 30%, #08888e dark cyan 20%, #e53a31 red 14% |
| Provider interface (shared) | 29 | 33% | 10% | 50% | 23% / 5% | #030303 black 57%, #fefefd white 20%, #686867 grey 6% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Intro screen key art

`lumo_intro_bkg_port` · atlas · 1 parts · largest 1034×1250 · sheet `sheets/lumo_intro_bkg_port.webp`

- **Role:** Full-screen portrait illustration for the intro/loading screen (brief: Loader IntroScreen background); seen in the first screenshot. Shown before play, so not tied to base game or free spins.
- **Subject:** Zeus (white hair and beard, white chiton with gold trim, lightning bolt in his raised fist) and Hades (red skin, flaming hair, gold wolf-head shoulder guard, purple cape, gold staff) lean into each other above the game logo, inside a swirl of light in a blue storm-cloud sky.
- **Style:** Stylised 3D-look painted key art; chibi-leaning proportions with large heads and hands; diagonal, confrontational composition with the logo as the base of the triangle.
- **Rendering:** Fully painted illustration with a 3D-render finish, soft cloud forms, sharp lightning and sparkle accents, no outlines; high detail on the characters, looser on the clouds.
- **Colour:** Dominated by saturated blues (#183cb4, #3b77db, #5ec0f6) with pale cyan-white light (#a5d6f1, #e4eff5); Hades and the HADES lettering supply the only strong red-orange, which makes them the focal contrast.
- **Lighting:** A bright white-cyan burst behind the logo back-lights both figures; lightning from the top left is the key on Zeus, while Hades is lit by his own flames; edges of the frame fall to deep blue.
- **Ambience:** Energetic clash on Olympus; dramatic but cartoon-friendly.
- **Materials:** Cloud, lightning, polished gold, white cloth, red skin, fire, purple cloth, carved stone slab.
- **Variants:** Portrait version only in this unit (1034x1250). The landscape screenshot shows it centred over the wide cloud backdrop.
- **Construction:** One flattened atlas image; characters and logo are baked in, not layered.
- **Notes:** This is the reference for how the two characters look together at full quality; the in-game mascots and expanded wilds follow the same designs.
- **Measured:** mid-tone, vivid, cool, high contrast, hard-edged · brightness 41% · saturation 72% · contrast 66% · warm 9% / cool 91%
- **Palette (measured):** #183cb4 blue 48%, #3b77db blue 18%, #5ec0f6 blue 14%, #a5d6f1 light blue 3%, #868ac9 blue 2%, #e4eff5 light cyan 2%

### Base game sky backdrop (loader atlas)

`basegame_bg` · atlas · 2 parts · largest 691×1726 · sheet `sheets/basegame_bg.webp`

- **Role:** Static sky images referenced under the loader's PortOnLandBkg holder: a tall portrait sky and a wide sky used as side filler when the portrait game sits in a landscape window (inference from the node names and the screenshots). Base game.
- **Subject:** Blue storm sky with banks of cumulus cloud and thin lightning forks; the portrait part is a clearer, brighter sky with a light band low down, the wide part has darker violet-tinted cloud masses left and right.
- **Style:** Painted, soft-focus environment art; rounded cloud shapes, no hard structure.
- **Rendering:** Digital painting with soft brushwork and gradients; lightning is the only sharp element; low detail so it stays behind the board.
- **Colour:** All blue: mid blue #3986ce dominant, deeper #345198 and indigo #393d78 in the cloud shadows, pale #77bbee in the lit areas.
- **Lighting:** Diffuse light from within the cloud gap, brighter towards the bottom of the portrait part; lightning adds small emissive accents.
- **Ambience:** Calm before the storm; airy Olympus sky.
- **Materials:** Cloud and electrical discharge only.
- **Variants:** Two orientations: bg 691x1726 (portrait) and basegame_bg 1725x689 (wide). The free-spins counterparts are freegame_green_bg and freegame_left.
- **Construction:** Two opaque atlas images, no layers.
- **Notes:** The wide part matches lumo_bkg_port_on_land in composition; it appears to be the same painting at slightly higher saturation (inference).
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 44% · saturation 66% · contrast 35% · warm 0% / cool 100% · brighter towards: bottom (2)
- **Palette (measured):** #3986ce blue 61%, #345198 blue 23%, #393d78 blue 7%, #72769c blue 4%, #77bbee blue 4%

### Landscape side backdrop, base game

`lumo_bkg_port_on_land` · atlas · 1 parts · largest 1725×689 · sheet `sheets/lumo_bkg_port_on_land.webp`

- **Role:** Wide cloud painting shown to the left and right of the portrait game area when the window is landscape (brief: PortOnLandBkg Left/Right sprites); visible in both screenshots. Base game.
- **Subject:** Storm clouds framing an open blue gap, with lightning forks running down both sides and small sparks near the bottom corners.
- **Style:** Soft painted environment, large rounded cloud masses arranged symmetrically so the centre stays empty.
- **Rendering:** Soft, slightly blurred digital painting with thin crisp lightning; deliberately low contrast and low detail.
- **Colour:** Muted blues: #3963a4 dominant, lighter #6a85b4, indigo #393d78 and a little dusty purple #736a8c on the cloud undersides.
- **Lighting:** Glow from the centre gap and from the lightning; cloud edges catch pale cyan light, undersides go violet.
- **Ambience:** Brooding but calm sky that keeps attention on the board.
- **Materials:** Cloud and lightning.
- **Variants:** One wide image (1725x689) used mirrored or split for left and right; freegame_left is its free-spins replacement at the same size.
- **Construction:** Single opaque atlas image.
- **Notes:** Less saturated than the portrait background so the playfield reads as the bright centre.
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged · brightness 38% · saturation 59% · contrast 31% · warm 0% / cool 100% · brighter towards: bottom (1)
- **Palette (measured):** #3963a4 blue 70%, #6a85b4 blue 13%, #393d78 blue 13%, #736a8c purple 2%

### Landscape side backdrop, free spins

`freegame_left` · atlas · 1 parts · largest 1725×689 · sheet `sheets/freegame_left.webp`

- **Role:** Wide underworld painting swapped in for the side areas during free spins (brief: SpriteL_Free / SpriteR_Free in the same holder as the base side backdrop).
- **Subject:** A red storm sky with a glowing vortex at the top, lightning in white and violet, jagged mountains, and in the foreground a cracked lava floor with broken columns, hanging chains and two stairways.
- **Style:** Painted fantasy environment with a centred, symmetric composition; more scenic detail than the base sky.
- **Rendering:** Digital painting with soft clouds and firmer rock and column shapes; glowing lava cracks are sharp; heavy dark vignette at the sides.
- **Colour:** Dark reds throughout: #47121f in the shadows, #8d2b2e and #c14940 in the clouds and rock, orange #e37d4b where lava and the sky glow.
- **Lighting:** Lit from below by lava and from above by the vortex; lightning adds cool violet accents; edges fall into near-black red.
- **Ambience:** Hades' realm: hot, threatening, theatrical.
- **Materials:** Lava, basalt rock, weathered stone columns, iron chains, smoke-like cloud.
- **Variants:** Free-spins version of lumo_bkg_port_on_land, same 1725x689 size.
- **Construction:** Single opaque atlas image.
- **Notes:** Direct warm inversion of the base side backdrop: same layout idea (dark sides, bright centre, lightning) with the hue flipped from blue to red.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 23% · saturation 72% · contrast 44% · warm 97% / cool 0%
- **Palette (measured):** #47121f dark red 48%, #8d2b2e red 28%, #c14940 red 18%, #e37d4b orange 6%

### Base game animated background

`zvhp_basegame_portrait` · skeleton · 26 parts · largest 380×592 · sheet `sheets/zvhp_basegame_portrait.webp`

- **Role:** Animated cloud layer of the portrait base-game background (brief: BkgPortrait/Base/Spine); it supplies the moving clouds seen above and below the board in the main screenshot.
- **Subject:** Layered blue cumulus clouds grouped at the top and bottom of the screen, leaving the middle clear for the reels, plus short blue lightning arcs.
- **Style:** Painted stylised clouds with rounded billows and long horizontal wisps; cut-out shapes arranged in depth.
- **Rendering:** Soft painted volumes with clean silhouette edges; brighter cyan rims on the nearer clouds; lightning has a thin white core and blue glow.
- **Colour:** Blue only: #387bcb dominant, lighter #75afe9, deep #1f48a4 in the far clouds and cyan #2fb7f3 on the lit rims.
- **Lighting:** Clouds are lit from the centre gap, with cyan rim light on the inner edges; lightning arcs are emissive.
- **Ambience:** Open, breezy sky of Olympus.
- **Materials:** Cloud and lightning.
- **Variants:** Portrait layout only; the free-spins counterpart is zvhp_freegame.
- **Motion:** One looping animation, zvhp_basegame_portrait 3.33s. The cloud stacks hold their places while their edges and the small wisps between the lower stacks change shape slightly (cloud frame sequences x8, x3, x3 and x7), and a single thin blue bolt (bizli x4) flashes near the top in the middle of the loop, at a different spot in successive frames, then is gone.
- **Construction:** Spine 3.7.91 skeleton with 6 bones and 47 slots: 40 mesh, 16 region and 1 clipping attachment, with additive blending for the lightning. 26 unique parts sit over a static sky sprite.
- **Notes:** Clouds are split into separate left and right stacks so they can move independently; the empty middle is by design.
- **Skeleton (from the file):** Spine 3.7.91 · 6 bones · 47 slots · 40 mesh, 16 region, 1 clipping · animations: zvhp_basegame_portrait (3.33 s)
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 48% · saturation 70% · contrast 28% · warm 0% / cool 100% · brighter towards: bottom-left (3), top-left (3), bottom-right (3)
- **Palette (measured):** #387bcb blue 77%, #75afe9 blue 14%, #2fb7f3 cyan 4%, #1f48a4 blue 4%

### Free spins animated background

`zvhp_freegame` · skeleton · 76 parts · largest 476×247 · sheet `sheets/zvhp_freegame.webp`

- **Role:** Animated layer of the portrait free-spins background (brief: BkgPortrait/Free/Spine_green/Spine_port), drawn over the static painting freegame_green_bg.
- **Subject:** Red storm clouds across the top with pink-violet lightning, and at the bottom a lava pool fed by two lava falls, with ripples, drips, rocks in the lava, small fires, smoke, rock walls and a stone pillar at each side, one with a chain.
- **Style:** Painted stylised underworld set pieces; chunky rocks with faceted planes and rounded lava blobs.
- **Rendering:** Painted cut-outs with clean edges; lava is treated as bright flat yellow-orange shapes with darker rims; smoke and the light spot are soft.
- **Colour:** Reds and oranges: #982d36 dominant, red-orange #db6245 in the lava and fire, dark #4d1025 in shadow; yellow at the hottest points and pink-white lightning cores are too small to appear in the measured palette.
- **Lighting:** Lava is the light source from below, giving rocks and pillars orange under-lighting; fire and lightning are emissive.
- **Ambience:** Hot, restless underworld.
- **Materials:** Molten lava, cracked rock, stone pillars, chain, flame, smoke, cloud.
- **Variants:** Portrait layout only; the base-game counterpart is zvhp_basegame_portrait.
- **Motion:** One looping animation, zvhp_freegame 2.0s. The cloud bank and pillars stay put; a pink bolt (thunder x5) flashes below the left of the clouds early in the loop and a smaller one inside the clouds later; in the pool the lava falls, ripples (x10) and drips cycle and small sparks rise above the rocks (particals x4), with fx_fire x8 and lava_stone x20 as further frame sequences.
- **Construction:** Spine 3.7.91 skeleton with 91 bones and 166 slots: 129 region and 44 mesh attachments, additive blending for glow and lightning. 76 unique parts, including a soft eff_spot glow sprite.
- **Notes:** Much denser than the base background (76 parts against 26): the free-spins mood is carried by many small looping effects rather than by one large painting.
- **Skeleton (from the file):** Spine 3.7.91 · 91 bones · 166 slots · 129 region, 44 mesh · animations: zvhp_freegame (2.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 36% · saturation 72% · contrast 31% · warm 96% / cool 0% · brighter towards: bottom (5), bottom-right (4), bottom-left (2)
- **Palette (measured):** #982d36 red 58%, #db6245 red 15%, #4d1025 dark red 9%

### Free spins static background

`freegame_green_bg` · atlas · 1 parts · largest 689×1725 · sheet `sheets/freegame_green_bg.webp`

- **Role:** Full portrait painting behind the free-spins board (brief: BkgPortrait/Free/Spine_green/sprite); the animated zvhp_freegame layer sits on top.
- **Subject:** A tall red-orange sky with heavy clouds and a lightning strike near the top, a glowing horizon in the middle, and a lava lake with a rock ledge and steps at the bottom.
- **Style:** Painted fantasy environment, vertically stacked in three bands (storm sky, bright horizon, lava foreground) so the reel board covers the calm middle.
- **Rendering:** Digital painting with soft cloud volumes and firmer rock forms; fine sparks and glowing cracks; no outlines.
- **Colour:** Orange #e38140 and red #ab362f dominate, with dark #6d1d2b in the cloud shadows and upper sky, pale orange #efb972 at the horizon and hot red #d44829 in the lava.
- **Lighting:** Strong warm glow from the horizon and from the lava below; a white-pink lightning strike is the brightest point at the top.
- **Ambience:** Infernal sunset; dangerous but richly coloured.
- **Materials:** Cloud, lava, rock, stone steps.
- **Variants:** Portrait 689x1725; the base-game equivalent is the bg part of basegame_bg, and the landscape side version is freegame_left.
- **Construction:** Single opaque atlas image used as the bottom layer under a Spine effects layer.
- **Notes:** The "green" in the name is an atlas page tag, not a colour of the art.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 43% · saturation 72% · contrast 59% · warm 97% / cool 0% · brighter towards: bottom (1)
- **Palette (measured):** #e38140 orange 40%, #ab362f red 32%, #6d1d2b dark red 16%, #efb972 orange 5%, #d44829 red 4%, #bb555d red 2%

### Paytable overlay panel

`paytable_overlay_bg` · atlas · 1 parts · largest 469×258 · sheet `sheets/paytable_overlay_bg.webp`

- **Role:** Background panel of the paytable overlay tab shown over the reels (brief: LUMO_OverlayPaytable/.../OverlayTab/Background). Both modes (inference).
- **Subject:** A dark red panel with a faint ornamental pattern and a bright centre, in a gold frame with a red diamond gem set in a winged mount at the top and bottom centre.
- **Style:** Ornate casual-slot UI panel; rectangular with symmetrical jewelled mounts.
- **Rendering:** Smooth painted gold with bright specular spots, crisp inner line, subtle tone-on-tone damask pattern inside, strong vignette.
- **Colour:** Dark red #46070b field with #871a0d at the centre; gold-orange frame #b76310.
- **Lighting:** Radial glow in the centre of the panel; point highlights spaced along the gold frame.
- **Ambience:** Rich, slightly regal.
- **Materials:** Polished gold, rubies, patterned red fabric or lacquer.
- **Variants:** One size, 469x258.
- **Construction:** Single sprite; the frame is regular enough to scale as a 9-slice, but the centred gems would need to stay fixed (inference).
- **Notes:** Red and gold regardless of game mode; shares its gem-and-gold language with free_spin_left.
- **Measured:** dark, vivid, warm, high contrast, hard-edged · brightness 17% · saturation 89% · contrast 62% · warm 100% / cool 0%
- **Palette (measured):** #46070b dark red 80%, #b76310 orange 8%, #871a0d dark red 3%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel backing, base game

`baseReel` · atlas · 1 parts · largest 499×527 · sheet `sheets/baseReel.webp`

- **Role:** Dark panel behind the symbols in the base game (brief: ReelsBkg/BaseGame/BaseReel/BG); visible as the navy field behind the symbols in the main screenshot.
- **Subject:** A plain dark navy rectangle with slightly darker edges.
- **Style:** Flat fill.
- **Rendering:** Near-uniform colour with a faint vignette at the edges; no texture.
- **Colour:** Single dark blue #1c1e53.
- **Lighting:** None; slight edge darkening only.
- **Ambience:** Quiet, lets symbols read.
- **Variants:** Free-spins counterpart is reel_freespin_bg.
- **Construction:** One opaque 499x527 image, stretched to the board size.
- **Notes:** Kept very dark and unsaturated in value so the bright symbols and gold dividers stand out.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 13% · saturation 67% · contrast 3% · warm 0% / cool 100%
- **Palette (measured):** #1c1e53 dark blue 100%

### Reel frame, base game

`reel_frame` · atlas · 1 parts · largest 689×720 · sheet `sheets/reel_frame.webp`

- **Role:** Thin border around the reel area in the base game (brief: BaseReel/Frame).
- **Subject:** A thin blue line frame, empty in the middle.
- **Style:** Minimal line border.
- **Rendering:** Thin soft-edged line with a lighter core.
- **Colour:** Blue #396390 with lighter #79a4cc.
- **Lighting:** Slight highlight along the line; no glow beyond its width.
- **Ambience:** Unobtrusive.
- **Materials:** Reads as blue metal or stone edging.
- **Variants:** Free-spins counterpart is reel_frame_freegame (red).
- **Construction:** Single 689x720 sprite, transparent centre; thin enough to scale as a 9-slice (inference).
- **Notes:** The board relies on the top bar, not this frame, for decoration.
- **Measured:** mid-tone, saturated, cool, medium contrast, glow or soft effect · brightness 46% · saturation 53% · contrast 33% · warm 0% / cool 100%
- **Palette (measured):** #396390 blue 62%, #79a4cc blue 38%

### Reel side rail, base game

`reel_frame_side_base` · atlas · 1 parts · largest 31×1043 · sheet `sheets/reel_frame_side_base.webp`

- **Role:** Vertical rail on the left and right edges of the reel board in the base game (brief: BaseReel/Side_frame/left and right).
- **Subject:** A narrow vertical blue bar with a lighter stripe.
- **Style:** Minimal bevelled strip.
- **Rendering:** Smooth vertical gradient bands suggesting a rounded moulding; clean edges.
- **Colour:** Blue #47719d with lighter #80abd9.
- **Lighting:** Highlight stripe down the length, as if lit from the front.
- **Ambience:** Neutral structural trim.
- **Materials:** Painted blue stone or metal moulding.
- **Variants:** Free-spins counterpart is reel_frame_side_free.
- **Construction:** Single 31x1043 strip used twice (left and right), stretchable vertically.
- **Notes:** Colour matches the blue stone of the base top bar.
- **Measured:** mid-tone, saturated, cool, medium contrast · brightness 52% · saturation 49% · contrast 33% · warm 0% / cool 100%
- **Palette (measured):** #47719d blue 59%, #80abd9 blue 41%

### Reel divider

`reel_divider` · atlas · 1 parts · largest 13×663 · sheet `sheets/reel_divider.webp`

- **Role:** Vertical divider between reels, used in both the base and free-spins boards (the brief lists it under BaseReel and under Free/freeReel1).
- **Subject:** A thin vertical gold bar with a dark outline.
- **Style:** Minimal bevelled strip.
- **Rendering:** Flat gold with a brighter centre line and dark edges.
- **Colour:** Gold #f8cd2a with darker #ae8830 and brown #6f5123 edges.
- **Lighting:** Highlight on one side, as measured from the right.
- **Ambience:** Small touch of richness.
- **Materials:** Polished gold.
- **Variants:** Same piece in both modes.
- **Construction:** Single 13x663 strip, instanced per gap and stretched vertically.
- **Notes:** In the main screenshot the reel gaps are barely visible, so the divider is used very lightly.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 56% · saturation 75% · contrast 48% · warm 100% / cool 0% · brighter towards: right (1)
- **Palette (measured):** #ae8830 orange 35%, #f8cd2a gold 35%, #6f5123 brown 30%

### Prize bar, base game

`reel_top_bar_base` · atlas · 1 parts · largest 1070×163 · sheet `sheets/reel_top_bar_base.webp`

- **Role:** Bar across the top of the reel board that carries the three fixed prize values (brief: BaseReel/BG_pop); in the main screenshot its three fields are labelled SNAP, BURST and SPARK. Base game.
- **Subject:** A blue stone entablature with a Greek key frieze above and below and an Ionic column at each end, framing three colour fields (green-yellow, pink and cyan) separated by white lightning-bolt shapes.
- **Style:** Stylised 3D-look architecture with flat graphic colour panels; symmetrical, wide and low.
- **Rendering:** Painted stone with bevels and carved key pattern at high detail; the colour fields are smooth gradients with hard zigzag dividers.
- **Colour:** Blue stone #5b8db4 and #375d8f; fields in lime #96ef08 to yellow #d9fb23, pink #fe67a7 and #ed3da1, and cyan #69c0e1 with pale #b3deed.
- **Lighting:** Even front light on the stone with highlights on the upper mouldings; the colour fields look back-lit.
- **Ambience:** Greek temple meets candy-bright arcade display.
- **Materials:** Carved blue marble; glossy coloured panels.
- **Variants:** Free-spins counterpart is reel_top_bar_free (red stone); this base file is larger (1070x163 against 739x112).
- **Construction:** Single flattened sprite; prize text is drawn separately on top.
- **Notes:** The three neon fields are the only place these lime, pink and cyan hues appear, which marks them as the "POP" feature colours.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 64% · saturation 59% · contrast 49% · warm 21% / cool 66%
- **Palette (measured):** #69c0e1 cyan 33%, #5b8db4 blue 21%, #fe67a7 magenta 18%, #d9fb23 gold 10%, #96ef08 green 7%, #375d8f blue 3%

### Message bar, base game

`reel_bottom_base` · atlas · 1 parts · largest 689×103 · sheet `sheets/reel_bottom_base.webp`

- **Role:** Bar under the reels that holds status text such as "PLACE YOUR BETS!" in the main screenshot (brief: BaseReel/BG_bottom). Base game.
- **Subject:** A dark indigo band with a thin gold line along the top and bottom.
- **Style:** Flat UI band with pinstripe trim.
- **Rendering:** Smooth horizontal gradient, slightly lighter at the ends; crisp gold lines.
- **Colour:** Indigo #30307a with gold lines #dab341 and #a6945a.
- **Lighting:** No directional light; faint sheen on the gold.
- **Ambience:** Calm and formal.
- **Materials:** Matte blue panel, gold inlay.
- **Variants:** Free-spins counterpart is reel_bottom_free, same 689x103 size.
- **Construction:** Single opaque sprite, stretchable horizontally.
- **Notes:** Gold pinstripes link it to the reel dividers and the spin button rim.
- **Measured:** dark, saturated, cool, medium contrast, hard-edged · brightness 25% · saturation 60% · contrast 38% · warm 9% / cool 91%
- **Palette (measured):** #30307a blue 86%, #a6945a yellow 7%, #6d6369 grey 4%, #dab341 orange 2%

### Reel frame, free spins

`reel_frame_freegame` · atlas · 1 parts · largest 999×1044 · sheet `sheets/reel_frame_freegame.webp`

- **Role:** Thin border around the reel area in free spins (brief: Free/freeReel1/Frame_holder/Frame).
- **Subject:** A thin red line frame, empty in the middle.
- **Style:** Minimal line border.
- **Rendering:** Thin soft-edged line with a lighter core.
- **Colour:** Red #a5181e with lighter #df4854.
- **Lighting:** Slight highlight along the line.
- **Ambience:** Unobtrusive; warm.
- **Materials:** Reads as red stone or lacquer edging.
- **Variants:** Red version of reel_frame; this file is larger (999x1044 against 689x720).
- **Construction:** Single sprite with transparent centre.
- **Notes:** Recoloured counterpart of the base frame.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 28% · saturation 79% · contrast 26% · warm 100% / cool 0%
- **Palette (measured):** #a5181e red 65%, #df4854 red 35%

### Reel side rail, free spins

`reel_frame_side_free` · atlas · 1 parts · largest 30×1043 · sheet `sheets/reel_frame_side_free.webp`

- **Role:** Vertical rail on the left and right edges of the reel board in free spins (brief: Free/freeReel1/Side_frame).
- **Subject:** A narrow vertical red bar with a lighter stripe.
- **Style:** Minimal bevelled strip.
- **Rendering:** Smooth vertical gradient bands; clean edges.
- **Colour:** Red #a92329 with lighter #e95364.
- **Lighting:** Highlight stripe down the length.
- **Ambience:** Neutral structural trim in the free-spins colour.
- **Materials:** Painted red stone moulding.
- **Variants:** Red version of reel_frame_side_base (30x1043).
- **Construction:** Single strip used left and right.
- **Notes:** Matches the red stone of the free-spins top bar.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 34% · saturation 73% · contrast 31% · warm 100% / cool 0%
- **Palette (measured):** #a92329 red 59%, #e95364 red 41%

### Reel backing, free spins

`reel_freespin_bg` · atlas · 1 parts · largest 689×744 · sheet `sheets/reel_freespin_bg.webp`

- **Role:** Dark panel behind the symbols in free spins (brief: Free/freeReel1/BG).
- **Subject:** A plain very dark red rectangle with slightly darker edges.
- **Style:** Flat fill.
- **Rendering:** Near-uniform colour with a faint vignette; no texture.
- **Colour:** Single dark red #43000d.
- **Lighting:** None.
- **Ambience:** Quiet, hot-toned ground for the symbols.
- **Variants:** Red version of baseReel; taller (689x744).
- **Construction:** One opaque image stretched to the board.
- **Notes:** Darker than the base backing (measured brightness 0.059 against 0.131).
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 6% · saturation 100% · contrast 1% · warm 100% / cool 0%
- **Palette (measured):** #43000d dark red 100%

### Prize bar, free spins

`reel_top_bar_free` · atlas · 1 parts · largest 739×112 · sheet `sheets/reel_top_bar_free.webp`

- **Role:** Bar across the top of the reel board carrying the three prize fields during free spins (brief: Free/freeReel1/BG_pop).
- **Subject:** The same entablature with key friezes and Ionic end columns as the base bar, in red stone, framing the same lime, pink and cyan fields with white lightning dividers.
- **Style:** Stylised 3D-look architecture with flat graphic colour panels.
- **Rendering:** Painted stone with carved key pattern; smooth gradient fields with hard zigzag dividers.
- **Colour:** Red stone #b72b31 and #d44e5c; fields lime #9bf408 to yellow #dbfc23, pink #fc6ea9 and #fe3dae, cyan #69e0f9.
- **Lighting:** Even front light with highlights on the mouldings; fields look back-lit.
- **Ambience:** Same arcade-temple feel, heated up.
- **Materials:** Carved red stone; glossy coloured panels.
- **Variants:** Red recolour of reel_top_bar_base at a smaller size (739x112).
- **Construction:** Single flattened sprite; prize text separate.
- **Notes:** Only the stone changes colour between modes; the three prize fields keep their hues, so players read them as the same prizes.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 55% · saturation 69% · contrast 67% · warm 65% / cool 23%
- **Palette (measured):** #b72b31 red 30%, #fc6ea9 red 22%, #69e0f9 cyan 16%, #dbfc23 gold 9%, #9bf408 green 7%, #d44e5c red 7%

### Message bar, free spins

`reel_bottom_free` · atlas · 1 parts · largest 689×103 · sheet `sheets/reel_bottom_free.webp`

- **Role:** Bar under the reels for status text during free spins (brief: Free/freeReel1/BG_bottom).
- **Subject:** A dark crimson band with a thin gold line along the top and bottom.
- **Style:** Flat UI band with pinstripe trim.
- **Rendering:** Smooth horizontal gradient; crisp gold lines.
- **Colour:** Dark red #5e0314 with gold lines #c19d44 and brown #8d5832.
- **Lighting:** No directional light.
- **Ambience:** Formal, warm.
- **Materials:** Matte red panel, gold inlay.
- **Variants:** Red version of reel_bottom_base, same 689x103 size.
- **Construction:** Single opaque sprite.
- **Notes:** Straight hue swap of the base bar.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 15% · saturation 93% · contrast 46% · warm 100% / cool 0%
- **Palette (measured):** #5e0314 dark red 86%, #c19d44 orange 7%, #8d5832 brown 6%

### Reel dimmer

`reelDark` · atlas · 1 parts · largest 108×115 · sheet `sheets/reelDark.webp`

- **Role:** Dark overlay placed over the reels when the paytable overlay is open (brief: LUMO_OverlayPaytable/.../DarkBG).
- **Subject:** A soft-edged black rounded rectangle with small tabs at the top and bottom.
- **Style:** Plain mask shape.
- **Rendering:** Solid black with a blurred, semi-transparent edge.
- **Colour:** Black #000000 only.
- **Ambience:** Neutral; pushes the board back.
- **Variants:** One small image, 108x115.
- **Construction:** Single small sprite scaled up over the reels; the soft edge suggests it is stretched, possibly as a 9-slice (inference).
- **Notes:** Utility piece with no theme styling.
- **Measured:** dark, muted, neutral, low contrast, glow or soft effect · brightness 0% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #000000 black 100%

### Win line strokes

`WinLines1` · atlas · 5 parts · largest 1159×448 · sheet `sheets/WinLines1.webp`

- **Role:** Thin lines drawn across the reels to show winning paylines (brief: Lines/WinLines/lineN). Both modes (inference).
- **Subject:** Thin white polylines: a straight horizontal line, a line with a raised plateau, and a zigzag.
- **Style:** Minimal line graphics.
- **Rendering:** One-pixel-class white strokes with a soft glow and small end dots.
- **Colour:** White and grey only (#ededed, #a0a0a0); colour would be applied by tinting in the engine (inference).
- **Lighting:** Soft glow along the stroke.
- **Ambience:** Functional.
- **Variants:** Three line shapes shown (line_01, line_03, line_05), up to 1159x448.
- **Motion:** Each line is a five-frame sequence (line x5).
- **Construction:** Five atlas parts in total; neutral white art meant to be tinted and flashed.
- **Notes:** Kept thin so it does not cover the symbols.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 81% · saturation 0% · contrast 21% · warm 0% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #ededed white 68%, #a0a0a0 grey 19%, #cbcbcb grey 6%, #0b0b0b black 4%, #5f5f5f grey 3%

### Payline shapes and line markers

`WinLines` · atlas · 5 parts · largest 910×467 · sheet `sheets/WinLines.webp`

- **Role:** Coloured payline shapes and the small markers at the reel edges that number the lines (brief: Lines_symbolSquares/WinLinesReferencePoints/.../lineNo). Both modes (inference).
- **Subject:** A yellow V-shaped line, a red inverted-V line, a cyan straight line, a white glow dot and a purple round marker with a gold rim.
- **Style:** Flat vector line graphics.
- **Rendering:** Thin flat-colour strokes; the marker is a simple glossy disc; the highlight is a soft white blur.
- **Colour:** Pure signal colours: red #ed1c24, yellow #ede61c, cyan-green #00ffbf and white #ffffff.
- **Lighting:** Only the highlight dot glows.
- **Ambience:** Functional, generic.
- **Variants:** Three line shapes (winLines_1_2_3 straight, winLines_4, winLines_5), one marker and one marker highlight.
- **Construction:** Five atlas parts; the straight line is reused for lines 1 to 3.
- **Notes:** These look like stock framework assets rather than theme art (inference); they do not follow the game palette.
- **Measured:** bright, vivid, warm and cool mixed, low contrast · brightness 62% · saturation 88% · contrast 3% · warm 69% / cool 27%
- **Palette (measured):** #ed1c24 red 35%, #ede61c gold 34%, #00ffbf cyan 25%, #ffffff light gold 3%

### Winning symbol square

`winlines` · atlas · 1 parts · largest 64×64 · sheet `sheets/winlines.webp`

- **Role:** Square outline drawn over a winning symbol position (brief: Lines_symbolSquares/SymbolSquares/ReelN/PosN/OverSymbol). Both modes (inference).
- **Subject:** A small square frame in light grey with a darker inner edge and a soft shadow.
- **Style:** Plain bevelled square outline.
- **Rendering:** Simple bevel with soft outer shadow.
- **Colour:** Greys only (#dddddd, #b6b6b6, #565656, #000000); meant to be tinted (inference).
- **Lighting:** Light bevel, soft drop shadow.
- **Ambience:** Functional.
- **Variants:** One 64x64 sprite.
- **Construction:** Single small sprite, scaled to the symbol cell and instanced per position.
- **Notes:** Stock-looking utility art (inference).
- **Measured:** mid-tone, muted, neutral, medium contrast · brightness 60% · saturation 0% · contrast 55% · warm 0% / cool 0%
- **Palette (measured):** #b6b6b6 grey 40%, #dddddd white 30%, #565656 grey 15%, #000000 black 15%

### Payline diagrams for the paytable

`paylines_triple_hop_pot` · atlas · 2 parts · largest 392×68 · sheet `sheets/paylines_triple_hop_pot.webp`

- **Role:** Small numbered diagrams of the paylines shown on a paytable page (brief: Paytable_portrait/Page6/.../PaylinesHolder).
- **Subject:** Rows of numbered mini grids with the cells of each payline filled in: one image with ten numbered grids in two rows, one with five grids in a single row.
- **Style:** Flat monochrome pictograms.
- **Rendering:** Pixel-sharp small grids in white and grey with numerals.
- **Colour:** Greys, black and white only (#6b6f6e, #3e4140, #a8a8a8, #010101, #ffffff).
- **Ambience:** Plain information graphic.
- **Variants:** Two layouts: 3x5_zeusvshadespop2 (392x68, ten lines) and a 3x3 five-payline sheet (264x22).
- **Construction:** Two flattened atlas images; no per-line parts.
- **Notes:** The second part carries another title's name (triple hop pot family naming), so the atlas looks shared across games (inference).
- **Measured:** mid-tone, muted, neutral, high contrast · brightness 41% · saturation 2% · contrast 100% · warm 0% / cool 0%
- **Palette (measured):** #6b6f6e grey 32%, #3e4140 grey 27%, #a8a8a8 grey 18%, #010101 black 14%, #ffffff white 8%, #232524 grey 2%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Temple on a cloud, scatter (animated)

`zvhp_scatter` · skeleton · 58 parts · largest 656×553 · sheet `sheets/zvhp_scatter.webp`

- **Role:** Special symbol: the scatter, S01 by its scene paths; the animated version used on the reels, in the idle state and in the overlay paytable.
- **Subject:** A small Greek temple with four blue marble columns, gold capitals, bases and pediment, and a glowing white doorway, floating on a bank of pink-lilac clouds inside a cyan burst of rays.
- **Style:** Stylised 3D-look painted prop with compact, toy-like proportions: thick columns, oversized gold scroll capitals and a low wide roof; rounded, friendly shape language.
- **Rendering:** Smooth digital painting that imitates a 3D render: clean hard edges on the architecture, soft airbrushed clouds, faint veining on the marble and no outlines; the effects (rays, glows, sparks) are soft-edged.
- **Colour:** Cool and vivid: cyan glow #22efff dominates, with blues #2aa9fb, #2b50b8 and #547dea on the marble, pale lilac-pink clouds #efdfed and #c5b4ec, and gold #fceb2b as the single warm accent.
- **Lighting:** Lit from the top, with a strong cyan back glow and radial rays behind the temple and a cyan rim under the clouds; the doorway and the star glints are emissive.
- **Ambience:** Mount Olympus as a bright, heavenly, inviting place: the Zeus side of the theme.
- **Materials:** Blue veined marble with a glossy vertical highlight, polished yellow gold with orange shadow, fluffy matte clouds with a cyan under-glow, and light as rays and sparkles.
- **Variants:** One design; the brief lists four states by animation (idle, land, anticipation, win). The S01 atlas holds its still version.
- **Motion:** zvhp_scatter_idle 1.5s and zvhp_scatter_anticipation 1.5s: the temple bobs gently on the cloud while the rays behind it turn, stars twinkle and small blue lightning arcs flick under the cloud. zvhp_scatter_land 0.5s: temple and cloud dip and spring back, with blue lightning arcs and sparks shooting out to both sides half-way through; zvhp_scatter_win 1.5s: the symbol starts small and swells, a thin flare ring with orange glints and green sparks opens around the temple and a shine runs up the columns, then it settles.
- **Construction:** 58 parts on 15 bones and 96 slots (80 meshes, 52 regions): roof, wall, bottom_oom base, four separate pillars, about a dozen cloud pieces in front of and behind the columns, door_light, a large back_glow (656x553), symbol_glow, a multicoloured flare (hb_rays_big) and star glints, with additive blending for the glows. The blue, cyan and red folder names are atlas page tags.
- **Notes:** The glow is larger than the temple itself and carries the cyan identity of the symbol, so the object needs a clean silhouette without it. Gold is always paired with one cool or warm body colour across the set; here it is blue marble.
- **Skeleton (from the file):** Spine 3.7.91 · 15 bones · 96 slots · 80 mesh, 52 region · animations: zvhp_scatter_anticipation (1.5 s), zvhp_scatter_idle (1.5 s), zvhp_scatter_land (0.5 s), zvhp_scatter_win (1.5 s)
- **Measured:** bright, vivid, cool, medium contrast · brightness 68% · saturation 68% · contrast 34% · warm 15% / cool 85% · brighter towards: top (6), bottom-left (2), top-right (1)
- **Palette (measured):** #22efff cyan 36%, #efdfed light magenta 8%, #2b50b8 blue 8%, #2aa9fb blue 8%, #c5b4ec light purple 8%, #547dea blue 8%

### Temple on a cloud, scatter (still)

`S01` · atlas · 2 parts · largest 836×705 · sheet `sheets/S01.webp`

- **Role:** Special symbol: the scatter still for the reels (Normal sprite) and the mobile paytable's ScatterHolder.
- **Subject:** The same blue-and-gold four-column temple on a pink-lilac cloud with a cyan halo around the whole shape.
- **Style:** Stylised 3D-look painted prop, compact and toy-like, matching the animated scatter.
- **Rendering:** Smooth painted render look with hard edges on the architecture and a soft outer glow; no outlines.
- **Colour:** Blue and cyan with lilac cloud and gold trim: #22b4fa, #7f92e9, #276af2 and #355abd for sky glow and marble, #ddcbea for the cloud, #efb320 and #fbec30 for the gold.
- **Lighting:** The doorway glows white from inside and a cyan halo surrounds the silhouette; no cast shadow.
- **Ambience:** Heavenly and bright; the Olympus side of the theme.
- **Materials:** Blue marble, polished gold, soft cloud, light glow.
- **Variants:** Two parts, 836x705 and 727x613: the smaller is sharp and the larger is smeared vertically, which reads as the spin-blur version (inference). A SpriteDark slot uses the same atlas.
- **Construction:** A flat atlas of 2 region pictures with the halo baked in; these are by far the largest still symbols in the set (the next largest, S10's blurred part, is 635 px wide).
- **Notes:** The scatter is the only still that is not a framed tile or a letter: a free-standing object with a halo, which sets it apart on the reels.
- **Measured:** bright, saturated, cool, medium contrast · brightness 64% · saturation 57% · contrast 53% · warm 24% / cool 75%
- **Palette (measured):** #22b4fa cyan 24%, #ddcbea light purple 20%, #7f92e9 blue 14%, #b9ac5a yellow 10%, #efb320 orange 6%, #276af2 blue 6%

### WILD on lava, wild symbol (animated)

`zvhp_wild` · skeleton · 51 parts · largest 268×165 · sheet `sheets/zvhp_wild.webp`

- **Role:** Special symbol: the wild, S02_wild by its scene paths; the landing, win and highlight animation.
- **Subject:** The word WILD in thick gold capitals on a cracked red lava tile inside a thin gold frame with scroll corners and a red gem at the top centre.
- **Style:** Stylised 3D-look lettering: tall, slightly irregular chiselled capitals with nicks and cracks, bevelled faces and a visible extrusion; the frame is a thin double gold rail with spiral ornaments.
- **Rendering:** Painted 3D look with hard edges and crisp bevel planes on the letters; the lava tile is a looser painting of dark cells with bright seams; splash and lava effects are high-contrast silhouettes with a glowing core.
- **Colour:** Hot and saturated: dark red #6f0b03 and #b02306 for the lava, bright red #f33702 and orange #ef870a in the seams and splashes, gold #feea0f, #f5bc1d and #fcee52 on the letters, with near-black #110201 in the sunk letter shapes. A thin blue line runs inside the gold frame on all four sides.
- **Lighting:** Letters are lit from the top and top-right with pale yellow highlights on the upper bevels and orange in the lower planes; the lava seams are emissive; each letter has its own soft red-brown drop shadow.
- **Ambience:** Volcanic and aggressive: the Hades, underworld side of the theme.
- **Materials:** Polished, slightly battered gold; molten lava with a dark cooled crust; a cabochon red gem with a specular dot; scorched black-and-ember letter shapes (w_sink, d_sink).
- **Variants:** Each letter exists as a gold face, a depth piece, a shadow and a charred 'sink' version; the win frames show the gold letters replaced by the charred ones and then returning. The S02 atlas holds the still version.
- **Motion:** zvhp_wild_landing 0.5s: a dark lava splash rises over the tile and two bright lava blobs flare along its lower edge, the splash breaks into droplets across the frame and the letters settle. zvhp_wild_win 1.5s: the gold letters fade to their charred, ember-edged versions as if sunk into the lava, then burst back out in gold, larger than the frame and one after another, with a dark splash, and settle with a few droplets.
- **Construction:** 51 parts on 45 bones and 64 slots (77 regions, 10 meshes): bg tile, frame built from top, bottom, left and right rails plus scroll ornaments and their shadows, gem with gem_sh, shine, bubble, and for each letter a face, depth, shadow and sink layer; additive blend for the fire. The red folder name is an atlas page tag.
- **Notes:** The assembled symbol matches the S02 still: letters, frame and gem sit as one tile. The lava-cell picture is the same motif that fills the royals' letters in their win animations, which ties wild and low symbols to the underworld palette.
- **Skeleton (from the file):** Spine 3.7.91 · 45 bones · 64 slots · 10 mesh, 77 region · animations: zvhp_wild_landing (0.5 s), zvhp_wild_win (1.5 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 32% · saturation 94% · contrast 42% · warm 99% / cool 1% · brighter towards: bottom-right (3), top (3), bottom-left (2)
- **Palette (measured):** #6f0b03 dark red 42%, #f33702 red 21%, #b02306 red 10%, #ef870a orange 8%, #feea0f gold 6%, #f5bc1d orange 4%

### WILD on lava, wild symbol (still)

`S02` · atlas · 2 parts · largest 431×321 · sheet `sheets/S02.webp`

- **Role:** Special symbol: the wild still on the reels (S02_wild); the same atlas is also referenced by S13_Expanding's Normal sprite.
- **Subject:** Gold WILD lettering on a dark red cracked-lava tile in a gold frame with scroll corners and a red gem at the top.
- **Style:** Stylised 3D-look lettering with tall, uneven chiselled capitals and a thin ornamental frame; landscape tile format.
- **Rendering:** Hard-edged painted render look, the measured soft-edge value is low (0.127); bright bevel highlights and fine crack lines on the tile.
- **Colour:** Gold on dark red: #f4b71f, #feee47 and #fef68f for the letters and frame, #881306 and #c2470c for the lava, with brown-gold #bd8530 in the frame shadows.
- **Lighting:** Top light on the letters with near-white highlights on the upper bevels; glowing seams in the lava; high measured contrast (0.811).
- **Ambience:** Hot, heavy, underworld.
- **Materials:** Polished gold, molten lava, red gem.
- **Variants:** Two parts: sharp 306x210 and a larger vertically smeared 431x321, which reads as the spin-blur version (inference). A SpriteDark slot uses the same atlas.
- **Construction:** A flat atlas of 2 region pictures, everything baked.
- **Notes:** Reads at small size because of the strong value step between pale gold letters and dark red ground; that light-on-dark step is the rule for all text symbols in this set.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 50% · saturation 84% · contrast 81% · warm 97% / cool 3%
- **Palette (measured):** #f4b71f orange 28%, #881306 dark red 22%, #c2470c orange 18%, #bd8530 orange 13%, #fef68f light gold 6%, #feee47 gold 4%

### Zeus, high symbol (animated)

`zvhp_hv_01` · skeleton · 109 parts · largest 279×181 · sheet `sheets/zvhp_hv_01.webp`

- **Role:** High symbol 1 (hv_01), S03 by its scene paths; the idle, landing and win animation and the overlay paytable version.
- **Subject:** Zeus as a cheerful older man with big white hair and beard, a white toga with a gold Greek-key border, gold bangles and a gold forehead piece, raising a fist that holds a lightning bolt, in a blue frame with jewelled corners.
- **Style:** Stylised 3D-look painted character in a family-animation manner: large head and hands, round nose, bulky arms, soft rounded forms; bust crop that breaks out of the frame.
- **Rendering:** Painted to look like a soft 3D render: smooth gradients, clean edges, no outlines, hair in large sculpted locks; lightning and particles are thin bright shapes with glow.
- **Colour:** Blue and white with gold and skin accents: frame and background blues #324382, #2b7bf2 and #426fab, white hair and cloth #ebeef4, lightning #54b2f5 and #90ecfd, with skin #c07c75 and dark warm shadow #5d303c.
- **Lighting:** A cool blue-cyan light from the lightning he holds against warm skin tones, with purple-blue shadows; the bolt, the frame edge and the glow shapes are emissive.
- **Ambience:** Friendly, powerful sky god: bright and heroic rather than severe.
- **Materials:** Soft matte skin, fluffy stylised hair, white cloth with broad folds, polished gold with engraved Greek key, a glassy blue frame with cut gems in the corners, and electric light.
- **Variants:** One design with a single listed animation (win); the scene paths also use it for idle and landing. The S03 atlas holds the still.
- **Motion:** zvhp_hv_01_win 1.5s: he starts with the bolt held across his chest, shuts his eyes and pulls it down, then thrusts the fist up out of the top of the frame with the bolt level above his head while branching blue arcs and sparks burst around it and a thin arc curls at his shoulder. The arcs fade with the arm still raised, and he returns to the first pose; hair and beard follow the movement.
- **Construction:** 109 parts on 75 bones and 104 slots (113 meshes, 80 regions, 1 clipping mask that keeps parts inside the frame): face, beard, moustache halves, many hair locks each with its own shadow piece, body, cloth, both arms in segments with bangles, belt, and a frame in four pieces over a hexagon-patterned bg; additive blend for lightning and glow. The blue, cyan and red folder names are atlas page tags.
- **Notes:** Every body part that overlaps another has a painted shadow layer of its own (beard_shadow, r_hair2_shadow, button_sh), so shading stays correct while parts move. The frame colour codes the character: blue for Zeus, red for Hades, green for Pegasus.
- **Skeleton (from the file):** Spine 3.7.91 · 75 bones · 104 slots · 113 mesh, 80 region, 1 clipping · animations: zvhp_hv_01_win (1.5 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast · brightness 47% · saturation 52% · contrast 46% · warm 31% / cool 65% · brighter towards: bottom-left (2), left (2), right (2)
- **Palette (measured):** #324382 blue 21%, #2b7bf2 blue 13%, #c07c75 red 10%, #5d303c dark red 10%, #426fab blue 7%, #ebeef4 light blue 6%

### Zeus, high symbol (still)

`S03` · atlas · 2 parts · largest 431×353 · sheet `sheets/S03.webp`

- **Role:** High symbol (S03), the reel still and the mobile paytable's Symbol3; the top character tile (inference from hv_01 naming).
- **Subject:** Zeus smiling, white hair and beard, white toga and gold bangles, holding a white-blue lightning bolt in his raised right hand, on a blue background in a blue jewelled frame.
- **Style:** Stylised 3D-look painted character with a large head, big eyes and rounded forms; landscape tile with the head and bolt overlapping the top edge of the frame.
- **Rendering:** Smooth painted render look, hard-edged (measured soft edge 0.121), no outlines, simplified detail that holds at small size.
- **Colour:** Blue dominated: #2c438a and #3674bd background and frame, #48a6e0 lightning glow, whites #e6eef4 and #c1c4d7 for hair and cloth, skin #edbc9f and warm shadow #7e5965.
- **Lighting:** The bolt lights the face and hand from the left with a cool glow; soft warm shading elsewhere.
- **Ambience:** Cheerful, heroic, heavenly.
- **Materials:** Skin, sculpted white hair, white cloth, gold jewellery, glowing lightning, blue stone frame.
- **Variants:** Two parts under one name: a sharp picture and a larger one that is smeared vertically, which reads as the spin-blur version (inference). The scene paths also name a SpriteDark slot that uses the same atlas, so the dimmed state is probably a tint in the engine (inference).
- **Construction:** A flat atlas of 2 region pictures, no layers; glow and lightning are baked into the picture.
- **Notes:** The bolt and hair break the frame, which gives the high symbols more presence than the letters; keep the break-out modest so the tile still reads as a rectangle.
- **Measured:** mid-tone, saturated, cool, high contrast, hard-edged · brightness 54% · saturation 46% · contrast 70% · warm 27% / cool 72% · brighter towards: left (2)
- **Palette (measured):** #2c438a blue 24%, #3674bd blue 13%, #e6eef4 light blue 10%, #c1c4d7 light blue 10%, #9088a9 blue 8%, #48a6e0 blue 7%

### Hades, high symbol (animated)

`zvhp_hv_02` · skeleton · 107 parts · largest 300×183 · sheet `sheets/zvhp_hv_02.webp`

- **Role:** High symbol 2 (hv_02), S04 by its scene paths; the idle, landing and win animation and the overlay paytable version.
- **Subject:** Hades as a red-skinned, muscular demon with a head of flame, a spiked crown, a dark goatee, a gold wolf-head shoulder guard, a dark strap with a teal gem and a purple cloth, with a swirling ball of fire beside his head, in a red frame over a wall of flames. A belt of skulls and the palm and finger parts are in the rig but fall outside the frames seen.
- **Style:** Stylised 3D-look painted character, exaggerated and angular: wide shoulders, sharp claws, pointed ears and spikes, in contrast to Zeus's round forms; bust crop that breaks out of the frame at the top.
- **Rendering:** Painted render look with hard edges and firm plane changes on the muscles; the flames are graphic, hard-edged shapes in three or four flat tones; glows are soft blurred discs.
- **Colour:** All warm: reds #d92d11 and #831c14 for skin and frame, orange #f7711b and gold #fede16, #fef15b and #fefa93 for fire and the wolf head, near-black #310c09 for the strap and shadows; the only cool notes are a small teal gem and the purple cloth.
- **Lighting:** Lit from below and the left by his own fire, with yellow rim light on the arm and face (face_glow, body_glow, finger_glow parts); fire, eyes and skull eyes are emissive.
- **Ambience:** Menacing but comic: a cartoon villain of the underworld.
- **Materials:** Glossy red skin, graphic fire, polished gold armour with engraved fur lines, dark leather, bone skulls, purple cloth.
- **Variants:** One design with a single listed animation (win); the scene paths also use it for idle and landing. The S04 atlas holds the still.
- **Motion:** zvhp_hv_02_win 1.5s: the ball of fire at his left grows and rises from shoulder height to above the frame's top corner, throwing embers, while the flame hair flickers throughout. His closed grin opens into a laugh, low flames rise along the bottom of the background, and he ends with a wink as the fire sinks back.
- **Construction:** 107 parts on 83 bones and 126 slots (82 meshes, 65 regions, 1 clipping mask): two face pieces, crown, body, arms and palm in segments, wolf head as base, face and lower jaw, belts with skulls, cloth, a four-piece frame with shadows, bg and fire_bg; additive and multiply blends (multiply for the shadow pieces, inference). The red and yellow folder names are atlas page tags.
- **Notes:** The parts are named fox_face, though the head reads as a wolf. Fire is drawn as flat graphic shapes while the body is softly modelled; that mix of graphic effects on a modelled character is consistent across the set.
- **Skeleton (from the file):** Spine 3.7.91 · 83 bones · 126 slots · 82 mesh, 65 region, 1 clipping · animations: zvhp_hv_02_win (1.5 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 46% · saturation 81% · contrast 42% · warm 98% / cool 1% · brighter towards: top-left (6), bottom-left (6), bottom (5)
- **Palette (measured):** #d92d11 red 19%, #f7711b orange 18%, #831c14 dark red 14%, #310c09 black 13%, #fede16 gold 12%, #fef15b gold 6%

### Hades, high symbol (still)

`S04` · atlas · 2 parts · largest 431×437 · sheet `sheets/S04.webp`

- **Role:** High symbol (S04), the reel still and the mobile paytable's Symbol4.
- **Subject:** Hades grinning, red skin, flame hair and spiked crown, a gold wolf-head shoulder guard and a raised hand holding fire, in a red frame with gold-lit corners over flames.
- **Style:** Stylised 3D-look painted character with angular, aggressive shapes; the flame hair rises well above the frame, so the tile is taller than the other character tiles (306x295 against about 306x240).
- **Rendering:** Smooth painted render look with firm edges; graphic flames; no outlines.
- **Colour:** Red and orange: #bf331b, #621910 and #ef5a33 for skin, frame and background, #f9a62b and #fee74a for fire and gold, warm brown #9d5944 in shadows.
- **Lighting:** Self-lit by fire from above and from the hand; strong warm rim on the face; high measured contrast (0.716).
- **Ambience:** Fiery, villainous, playful.
- **Materials:** Red skin, fire, gold armour, dark leather.
- **Variants:** Two parts under one name: a sharp picture and a larger one that is smeared vertically, which reads as the spin-blur version (inference). The scene paths also name a SpriteDark slot that uses the same atlas, so the dimmed state is probably a tint in the engine (inference).
- **Construction:** A flat atlas of 2 region pictures, no layers; glow and fire are baked into the picture.
- **Notes:** Mirror of the Zeus tile in pose (raised hand with an element, three-quarter bust) and opposite in temperature; design the two as a pair.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 39% · saturation 78% · contrast 72% · warm 99% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #bf331b red 29%, #621910 dark red 24%, #ef5a33 red 15%, #f9a62b orange 10%, #9d5944 red 8%, #e7925d orange 4%

### Pegasus, high symbol (animated)

`zvhp_hv_03` · skeleton · 73 parts · largest 433×177 · sheet `sheets/zvhp_hv_03.webp`

- **Role:** High symbol 3 (hv_03), S05 by its scene paths; the idle, landing and win animation and the overlay paytable version.
- **Subject:** A rearing pink-white winged horse with a flowing pink mane and tail, large blue eyes, an open smiling mouth, a gold jewelled collar and gold bands above the hooves, in a green Greek-key frame over a cyan cloudy sky.
- **Style:** Stylised 3D-look painted character, cute and toy-like: oversized head and eyes, short muzzle, rounded limbs, feathers in neat overlapping rows; the head, mane and wing tip break the top of the frame, and in the win the forelegs and both wings reach outside it.
- **Rendering:** Smooth painted render look, hard-edged (measured soft edge 0.111), soft pastel gradients on the body, each feather defined by a light edge; no outlines.
- **Colour:** Pastel pink against cyan: body and wings #f3d4de and #c498aa with mauve shadow #8f657d, sky #11e0f9, #0c90b2, #095777 and #59fafd; the frame is a saturated green and the jewellery gold.
- **Lighting:** Soft light from the top and top-right, cool blue bounce on the underside of the body and legs; a star flare part (star_25) and small star dots are emissive.
- **Ambience:** Sweet, light and magical; the gentlest symbol of the set.
- **Materials:** Soft matte coat, feathered wings, silky mane and tail in large locks, polished gold with a faceted gem, a glossy green jade-like frame.
- **Variants:** Three states by animation (idle, land, win), with blink frames and alternative mouth pieces (lower_mouth, lower_mouth_02, lower_mouth_smile). The S05 atlas holds the still.
- **Motion:** zvhp_hv_03_idle 1.5s: a small breathing loop, the head nodding and the wing and mane tips swaying; zvhp_hv_03_land 0.5s: the body dips and rises once and the wing tip flexes. zvhp_hv_03_win 1.5s: the horse starts crouched at the left with the wing folded upright, rears up so that head and forelegs come out over the top of the frame with both wings spread wide and a glint on the collar, sweeps the wings down and settles with the near wing stretched out past the right edge.
- **Construction:** 73 parts on 118 bones and 83 slots (64 meshes, 29 regions, 2 clipping masks): the highest bone count in the category, used for the mane, tail and wings; a face with separate eye bases, pupils, brows and lids, mouth parts, neck, body, leg segments, a four-piece frame with shadow pieces, bg and stars. The red and yellow folder names are atlas page tags.
- **Notes:** In the win the horse rears out of the frame and shows a second wing, which is why the rig carries full leg segments and several wing pieces that the still does not show. Eyes are built for blinking, which the two god characters' part lists do not show.
- **Skeleton (from the file):** Spine 3.7.91 · 118 bones · 83 slots · 64 mesh, 29 region, 2 clipping · animations: zvhp_hv_03_idle (1.5 s), zvhp_hv_03_land (0.5 s), zvhp_hv_03_win (1.5 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 64% · saturation 55% · contrast 43% · warm 39% / cool 51% · brighter towards: top-right (4), right (2), top (2)
- **Palette (measured):** #f3d4de light red 27%, #0c90b2 cyan 17%, #c498aa red 16%, #11e0f9 cyan 16%, #095777 dark cyan 8%, #8f657d magenta 4%

### Pegasus, high symbol (still)

`S05` · atlas · 2 parts · largest 432×357 · sheet `sheets/S05.webp`

- **Role:** High symbol (S05), the reel still and the mobile paytable's Symbol5.
- **Subject:** A smiling pink-white Pegasus with a raised wing, a gold collar and gold leg bands, in a green Greek-key frame over a cyan sky with clouds.
- **Style:** Stylised 3D-look painted character, cute proportions with a large head and eyes; the mane and wing tip break the top of the frame.
- **Rendering:** Smooth painted render look, hard-edged (0.121), pastel gradients, no outlines.
- **Colour:** Light pink #eccdd4 and #cda1ad on cyan #19d9f2, #11859a and #21b0c7, with the green frame #31b443 and small gold accents; the brightest of the character tiles (brightness 0.682).
- **Lighting:** Even soft light from above; no strong shadows; small white sparkles in the sky.
- **Ambience:** Sweet, airy, magical.
- **Materials:** Soft coat and feathers, gold jewellery, green stone frame.
- **Variants:** Two parts under one name: a sharp picture and a larger one that is smeared vertically, which reads as the spin-blur version (inference). The scene paths also name a SpriteDark slot that uses the same atlas, so the dimmed state is probably a tint in the engine (inference).
- **Construction:** A flat atlas of 2 region pictures, no layers; the sky and sparkles are baked into the picture.
- **Notes:** The three character tiles share the frame construction (thin rails with Greek-key corners) and differ by frame colour: blue, red, green.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 68% · saturation 46% · contrast 50% · warm 20% / cool 66%
- **Palette (measured):** #eccdd4 light red 35%, #cda1ad red 12%, #11859a cyan 11%, #31b443 green 10%, #19d9f2 cyan 8%, #21b0c7 cyan 4%

### Ace, low symbol (animated)

`zvhp_a` · skeleton · 10 parts · largest 269×163 · sheet `sheets/zvhp_a.webp`

- **Role:** Low symbol, the Ace, S06 by its scene paths (the overlay names it lumo_hv4, but it is a royal letter); the idle, landing and win animation.
- **Subject:** A capital A with a purple face and gold rim, crossed by pink-white lightning; in the win the face is replaced by glowing red lava cells with a floating bubble, seen through the letter's shape.
- **Style:** The same extruded slab-serif letter split into flat layers; a painted lava-cell picture fills the letter's face in the win, so the letter stays graphic while its filling turns painterly.
- **Rendering:** Letter layers are clean, hard-edged gradients; the lava picture is a soft digital painting of dark red cells with glowing orange seams; bubbles are small glossy spheres.
- **Colour:** Measured on the whole unit, the lava picture (the largest part) dominates: dark red #8b1206 and orange #b23f12 with near-black #080013 from the shadow; the letter face is purple #a814d7 and the lightning is pink-white (magenta-tagged frames).
- **Lighting:** Top light on the gold rim with a bright specular line; the lava seams and the lightning are emissive; a separate soft dark shadow shape sits behind the letter.
- **Ambience:** Bright, toy-like and electrically charged at rest; the win fills the letter with the underworld's lava.
- **Materials:** Gold rim (royal_frame) and gold-brown extrusion (royal_depth), enamel-like coloured face (royal), molten lava with cooled crust, translucent bubbles.
- **Variants:** Three states by animation (idle, landing, win). The S06 atlas holds the still. An extra part holds the gold inner triangle of the A.
- **Motion:** zvhp_a_idle 1.0s: the letter holds still while three lightning arcs flicker in place over the face and rim. zvhp_a_landing 0.5s: a small swell and settle with the same lightning; zvhp_a_win 1.5s: the lightning stops, the purple face gives way to lava cells with a bubble rising inside the letter, the letter swells to its largest half-way as the lightning returns, pale wisps show at its upper left and the purple face comes back.
- **Construction:** 10 parts: bg (the lava picture), royal_shadow, royal_depth (extrusion), royal_frame (gold rim), royal (coloured face), three 3-frame thunder sequences and a bubble, plus an 'extra' piece for the counter of the A. The skeleton has 10 meshes, 3 paths (probably the bubbles' or lightning's routes, inference) and 1 clipping attachment, which keeps the lava picture and bubble inside the letter's face in the frames seen, with an additive blend for the lightning; the colour-named folder on the thunder frames is an atlas page tag.
- **Notes:** All four royals share the same rig layout, lava picture and bubble, so one template serves the set; only the face colour, the letter shapes and the lightning tint change. The lava shows only in the win frames, inside the letter; idle and landing keep the coloured face.
- **Skeleton (from the file):** Spine 3.7.91 · 34 bones · 39 slots · 25 region, 10 mesh, 1 clipping, 3 path · animations: zvhp_a_idle (1.0 s), zvhp_a_landing (0.5 s), zvhp_a_win (1.5 s)
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 26% · saturation 91% · contrast 27% · warm 83% / cool 14% · brighter towards: top (1)
- **Palette (measured):** #8b1206 dark red 53%, #b23f12 orange 16%, #080013 black 9%, #facb29 gold 5%, #a814d7 purple 4%, #f137fd magenta 2%

### Ace, low symbol (still)

`S06` · atlas · 2 parts · largest 398×407 · sheet `sheets/S06.webp`

- **Role:** Low symbol (S06), the reel still and the mobile paytable's Symbol6; the highest of the letters (inference from order).
- **Subject:** A purple capital A with a thick gold rim and pink-white lightning across it.
- **Style:** Chunky slab-serif capital drawn as an extruded 3D letter seen slightly from below-left, with a coloured face, a raised gold rim and a darker gold side; rounded, inflated shape language.
- **Rendering:** Smooth airbrushed 3D-look painting with clean hard silhouettes, soft gradients on the face and thin specular lines on the rim; no outline other than the gold rim itself, and no surface texture.
- **Colour:** Purple and magenta face #ad1dd4 and #e33ef5 with pink lights #f5a1f1, gold rim #f6d448 over orange-brown sides #d18e3c and #9d5f20, and near-white pink lightning #fde9ef.
- **Lighting:** Top light: the upper face is lighter and the rim carries a bright line; the lightning is emissive and tints the face near it.
- **Ambience:** Bright, toy-like, charged.
- **Materials:** Polished gold rim and side with glossy gradients; the face reads as coloured enamel or glass; lightning as a white-cored glow.
- **Variants:** Two parts under one name: a sharp picture and a larger one that is smeared vertically, which reads as the spin-blur version (inference). The scene paths also name a SpriteDark slot that uses the same atlas, so the dimmed state is probably a tint in the engine (inference).
- **Construction:** A flat atlas of 2 region pictures, no layers; glow and lightning are baked into the picture.
- **Notes:** Each royal has its own face colour and a lightning tint to match: A purple with pink, K red with yellow, Q gold with pale yellow, J blue with cyan.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 52% · saturation 67% · contrast 66% · warm 70% / cool 18% · brighter towards: top (2)
- **Palette (measured):** #ad1dd4 purple 17%, #f6d448 gold 14%, #9d5f20 brown 14%, #c66687 red 14%, #d18e3c orange 12%, #e33ef5 magenta 7%

### King, low symbol (animated)

`zvhp_k` · skeleton · 9 parts · largest 371×225 · sheet `sheets/zvhp_k.webp`

- **Role:** Low symbol, the King, S07 by its scene paths; the idle, landing and win animation.
- **Subject:** A capital K with a red-orange face and gold rim, crossed by yellow lightning; in the win the face is replaced by glowing red lava cells with a floating bubble, seen through the letter's shape.
- **Style:** The same extruded slab-serif letter split into flat layers; a painted lava-cell picture fills the letter's face in the win, so the letter stays graphic while its filling turns painterly.
- **Rendering:** Letter layers are clean, hard-edged gradients; the lava picture is a soft digital painting of dark red cells with glowing orange seams; bubbles are small glossy spheres.
- **Colour:** The lava picture dominates the measure: dark red #8d1107, brown #9c4e18 and near-black #080013; the letter face is red-orange #ef3707 and #cc0e04, close to the lava's colour, so the change of filling in the win is less marked than on the other letters.
- **Lighting:** Top light on the gold rim with a bright specular line; the lava seams and the lightning are emissive; a separate soft dark shadow shape sits behind the letter.
- **Ambience:** Hot and charged; the win fills the letter with the underworld's lava.
- **Materials:** Gold rim (royal_frame) and gold-brown extrusion (royal_depth), enamel-like coloured face (royal), molten lava with cooled crust, translucent bubbles.
- **Variants:** Only a win animation is listed for this letter, where A, Q and J also list idle and landing. The S07 atlas holds the still.
- **Motion:** zvhp_k_win 1.5s: the red-orange face gives way to lava cells with bubbles drifting inside the letter, the letter swells and yellow lightning arcs flicker at its left side and lower right, then the red-orange face returns as the lightning fades.
- **Construction:** 9 parts: bg (the lava picture), royal_shadow, royal_depth (extrusion), royal_frame (gold rim), royal (coloured face), three 3-frame thunder sequences and a bubble. The skeleton has 10 meshes, 3 paths (probably the bubbles' or lightning's routes, inference) and 1 clipping attachment, which keeps the lava picture and bubble inside the letter's face in the frames seen, with an additive blend for the lightning; the colour-named folder on the thunder frames is an atlas page tag.
- **Notes:** All four royals share the same rig layout, lava picture and bubble, so one template serves the set; only the face colour, the letter shapes and the lightning tint change. The lava shows only in the win frames, inside the letter; the still shows the coloured face. The K's red face is the closest of the four to the lava's colour.
- **Skeleton (from the file):** Spine 3.7.91 · 34 bones · 38 slots · 24 region, 10 mesh, 1 clipping, 3 path · animations: zvhp_k_win (1.5 s)
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 26% · saturation 92% · contrast 28% · warm 90% / cool 10% · brighter towards: top (1), bottom-right (1)
- **Palette (measured):** #8d1107 dark red 56%, #9c4e18 brown 12%, #080013 black 10%, #ef3707 red 8%, #cc0e04 red 2%

### King, low symbol (still)

`S07` · atlas · 2 parts · largest 237×281 · sheet `sheets/S07.webp`

- **Role:** Low symbol (S07), the reel still and the mobile paytable's Symbol7.
- **Subject:** A red-orange capital K with a thick gold rim and yellow-white lightning.
- **Style:** Chunky slab-serif capital drawn as an extruded 3D letter seen slightly from below-left, with a coloured face, a raised gold rim and a darker gold side; rounded, inflated shape language.
- **Rendering:** Smooth airbrushed 3D-look painting with clean hard silhouettes, soft gradients on the face and thin specular lines on the rim; no outline other than the gold rim itself, and no surface texture.
- **Colour:** Fully warm: red face #f23a09 with an orange lower gradient #ef8e26, gold rim #f6cc39 and #fceb7b, brown-gold sides #b16b20, near-white lightning #fffdeb.
- **Lighting:** Top light with a vertical gradient on the face from red to orange; emissive lightning.
- **Ambience:** Bright, hot, toy-like.
- **Materials:** Polished gold rim and side with glossy gradients; the face reads as coloured enamel or glass; lightning as a white-cored glow.
- **Variants:** Two parts under one name: a sharp picture and a larger one that is smeared vertically, which reads as the spin-blur version (inference). The scene paths also name a SpriteDark slot that uses the same atlas, so the dimmed state is probably a tint in the engine (inference).
- **Construction:** A flat atlas of 2 region pictures, no layers; glow and lightning are baked into the picture.
- **Notes:** Same construction and viewing angle as A, Q and J; only colour and letterform change.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 56% · saturation 81% · contrast 68% · warm 100% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #f23a09 red 27%, #ef8e26 orange 21%, #b16b20 orange 18%, #f6cc39 gold 17%, #fceb7b gold 6%, #fffdeb light gold 2%

### Queen, low symbol (animated)

`zvhp_q` · skeleton · 9 parts · largest 371×225 · sheet `sheets/zvhp_q.webp`

- **Role:** Low symbol, the Queen, S08 by its scene paths; the overlay paytable also uses this skeleton in the S11 and S12 slots.
- **Subject:** A capital Q with a yellow-gold face and gold rim, crossed by pale yellow lightning; in the win the face is replaced by glowing red lava cells with a floating bubble, seen through the letter's shape.
- **Style:** The same extruded slab-serif letter split into flat layers; a painted lava-cell picture fills the letter's face in the win, so the letter stays graphic while its filling turns painterly.
- **Rendering:** Letter layers are clean, hard-edged gradients; the lava picture is a soft digital painting of dark red cells with glowing orange seams; bubbles are small glossy spheres.
- **Colour:** Lava picture #890f08 and #ac420f with near-black #080013; the letter face is gold #fecd12, the lightest of the four and the strongest contrast with the lava filling.
- **Lighting:** Top light on the gold rim with a bright specular line; the lava seams and the lightning are emissive; a separate soft dark shadow shape sits behind the letter.
- **Ambience:** Bright and charged at rest; the win fills the letter with the underworld's lava.
- **Materials:** Gold rim (royal_frame) and gold-brown extrusion (royal_depth), enamel-like coloured face (royal), molten lava with cooled crust, translucent bubbles.
- **Variants:** Three states by animation (idle, landing, win). The S08 atlas holds the still.
- **Motion:** zvhp_q_idle 1.0s: the letter holds still while pale lightning arcs flicker across it from upper left to lower left. zvhp_q_landing 0.5s: a small swell and settle with the same lightning; zvhp_q_win 1.5s: the lightning stops, the gold face gives way to lava cells with bubbles inside the letter, the letter swells as the lightning returns, and the gold face comes back.
- **Construction:** 9 parts: bg (the lava picture), royal_shadow, royal_depth (extrusion), royal_frame (gold rim), royal (coloured face), three 3-frame thunder sequences and a bubble. The skeleton has 10 meshes, 3 paths (probably the bubbles' or lightning's routes, inference) and 1 clipping attachment, which keeps the lava picture and bubble inside the letter's face in the frames seen, with an additive blend for the lightning; the colour-named folder on the thunder frames is an atlas page tag.
- **Notes:** All four royals share the same rig layout, lava picture and bubble, so one template serves the set; only the face colour, the letter shapes and the lightning tint change. The lava shows only in the win frames, inside the letter; idle and landing keep the gold face.
- **Skeleton (from the file):** Spine 3.7.91 · 34 bones · 37 slots · 23 region, 10 mesh, 1 clipping, 3 path · animations: zvhp_q_idle (1.0 s), zvhp_q_landing (0.5 s), zvhp_q_win (1.5 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 30% · saturation 91% · contrast 25% · warm 91% / cool 9% · brighter towards: bottom-right (1)
- **Palette (measured):** #890f08 dark red 53%, #ac420f brown 16%, #fecd12 gold 10%, #080013 black 9%

### Queen, low symbol (still)

`S08` · atlas · 2 parts · largest 237×286 · sheet `sheets/S08.webp`

- **Role:** Low symbol (S08), the reel still; the scene paths also place this atlas in the S11 symbol's Normal sprite.
- **Subject:** A yellow-gold capital Q with a gold rim and thin white lightning.
- **Style:** Chunky slab-serif capital drawn as an extruded 3D letter seen slightly from below-left, with a coloured face, a raised gold rim and a darker gold side; rounded, inflated shape language.
- **Rendering:** Smooth airbrushed 3D-look painting with clean hard silhouettes, soft gradients on the face and thin specular lines on the rim; no outline other than the gold rim itself, and no surface texture.
- **Colour:** Monochrome gold: #f9c618 and #fbeb59 on the face and rim, #ba7522 on the sides, pale highlights #fbf2a2 and #fefee7; the brightest still in the set (brightness 0.738).
- **Lighting:** Top-left light with strong highlights; because face and rim are both gold, the form relies on the darker side wall and the inner bevel.
- **Ambience:** Bright, rich, toy-like.
- **Materials:** Polished gold throughout, in two tones; lightning as a white glow.
- **Variants:** Two parts under one name: a sharp picture and a larger one that is smeared vertically, which reads as the spin-blur version (inference). The scene paths also name a SpriteDark slot that uses the same atlas, so the dimmed state is probably a tint in the engine (inference).
- **Construction:** A flat atlas of 2 region pictures, no layers; glow and lightning are baked into the picture.
- **Notes:** The only royal without a contrasting face colour; a recreation should keep the rim readable through value alone.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 74% · saturation 77% · contrast 56% · warm 100% / cool 0% · brighter towards: top-left (2)
- **Palette (measured):** #f9c618 gold 44%, #fbeb59 gold 25%, #ba7522 orange 18%, #fbf2a2 light gold 3%, #fefee7 light gold 3%

### Jack, low symbol (animated)

`zvhp_j` · skeleton · 9 parts · largest 371×225 · sheet `sheets/zvhp_j.webp`

- **Role:** Low symbol, the Jack, S09 by its scene paths; the idle, landing and win animation.
- **Subject:** A capital J with a blue face and gold rim, crossed by cyan lightning; in the win the face is replaced by glowing red lava cells with a floating bubble, seen through the letter's shape.
- **Style:** The same extruded slab-serif letter split into flat layers; a painted lava-cell picture fills the letter's face in the win, so the letter stays graphic while its filling turns painterly.
- **Rendering:** Letter layers are clean, hard-edged gradients; the lava picture is a soft digital painting of dark red cells with glowing orange seams; bubbles are small glossy spheres.
- **Colour:** Lava picture reds #8f170f, #c71a06 and #640503 with near-black #080011; the letter face is a saturated blue and the lightning cyan-white, the only cool notes against the warm gold and lava.
- **Lighting:** Top light on the gold rim with a bright specular line; the lava seams and the lightning are emissive; a separate soft dark shadow shape sits behind the letter.
- **Ambience:** A cool, electric letter that fills with hot lava in the win: the game's fire-and-sky contrast in one symbol.
- **Materials:** Gold rim (royal_frame) and gold-brown extrusion (royal_depth), enamel-like coloured face (royal), molten lava with cooled crust, translucent bubbles.
- **Variants:** Three states by animation (idle, landing, win). The S09 atlas holds the still.
- **Motion:** zvhp_j_idle 1.0s: the letter holds still while cyan lightning arcs flicker down its stem. zvhp_j_landing 0.5s: a small swell and settle with the same lightning; zvhp_j_win 1.5s: the lightning stops, the blue face gives way to lava cells with a bubble inside the letter, the letter swells as the lightning returns, and the blue face comes back.
- **Construction:** 9 parts: bg (the lava picture), royal_shadow, royal_depth (extrusion), royal_frame (gold rim), royal (coloured face), three 3-frame thunder sequences and a bubble. The skeleton has 10 meshes, 3 paths (probably the bubbles' or lightning's routes, inference) and 1 clipping attachment, which keeps the lava picture and bubble inside the letter's face in the frames seen, with an additive blend for the lightning; the colour-named folder on the thunder frames is an atlas page tag.
- **Notes:** All four royals share the same rig layout, lava picture and bubble, so one template serves the set; only the face colour, the letter shapes and the lightning tint change. The lava shows only in the win frames, inside the letter; idle and landing keep the blue face.
- **Skeleton (from the file):** Spine 3.7.91 · 34 bones · 38 slots · 24 region, 3 path, 10 mesh, 1 clipping · animations: zvhp_j_idle (1.0 s), zvhp_j_landing (0.5 s), zvhp_j_win (1.5 s)
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 25% · saturation 89% · contrast 28% · warm 84% / cool 16% · brighter towards: top-right (1), right (1)
- **Palette (measured):** #8f170f red 64%, #080011 black 8%, #c71a06 red 5%, #640503 dark red 4%

### Jack, low symbol (still)

`S09` · atlas · 2 parts · largest 202×290 · sheet `sheets/S09.webp`

- **Role:** Low symbol (S09), the reel still and the mobile paytable's Symbol9; the lowest letter seen in this category (no 10 is present).
- **Subject:** A blue capital J with a thick gold rim and cyan-white lightning.
- **Style:** Chunky slab-serif capital drawn as an extruded 3D letter seen slightly from below-left, with a coloured face, a raised gold rim and a darker gold side; rounded, inflated shape language.
- **Rendering:** Smooth airbrushed 3D-look painting with clean hard silhouettes, soft gradients on the face and thin specular lines on the rim; no outline other than the gold rim itself, and no surface texture.
- **Colour:** Blue face #1a5ef5 and #2e2ad8 inside a gold rim #f1ce3a and #f7f17e with orange-brown sides #a76722 and #c49649; near-white lightning #f2fdf2 and a little near-black #0e0814 in the deepest shadow.
- **Lighting:** Top light with a lighter upper face and a specular line on the rim; emissive lightning.
- **Ambience:** Cool, bright, toy-like.
- **Materials:** Polished gold rim and side with glossy gradients; the face reads as coloured enamel or glass; lightning as a white-cored glow.
- **Variants:** Two parts under one name: a sharp picture and a larger one that is smeared vertically, which reads as the spin-blur version (inference). The scene paths also name a SpriteDark slot that uses the same atlas, so the dimmed state is probably a tint in the engine (inference).
- **Construction:** A flat atlas of 2 region pictures, no layers; glow and lightning are baked into the picture.
- **Notes:** Complementary blue and gold give this letter the clearest read of the four.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 54% · saturation 67% · contrast 72% · warm 57% / cool 42% · brighter towards: top (2)
- **Palette (measured):** #a76722 orange 19%, #1a5ef5 blue 15%, #f1ce3a gold 15%, #2e2ad8 blue 6%, #c49649 orange 6%, #f7f17e gold 5%

### VS coin on a galaxy, special wild (animated)

`zvhp_vs_wild` · skeleton · 76 parts · largest 296×190 · sheet `sheets/zvhp_vs_wild.webp`

- **Role:** Special symbol: the VS wild, S10 by its scene paths (the mobile paytable calls its holder SpecialWildHolder); the idle, landing and win animation.
- **Subject:** Large gold VS letters over a gold coin ring engraved with a Greek key, the ring enclosing a purple-pink-blue galaxy, in a gold frame with scroll corners and a galaxy background.
- **Style:** Stylised 3D-look lettering and ornament: heavy italic block capitals with deep extrusion, a thick round coin and a classical frame with volutes; bold, rounded and weighty.
- **Rendering:** Painted render look with hard edges and broad gradient planes on the gold; the galaxy is a soft, photographic-looking nebula with star dots; energy and hit effects are thin scribbled arcs and spark bursts.
- **Colour:** Gold against violet: #fce577, #fbb716 and #cc6711 for the letters, coin and frame, dark purple #240a5a and near-black #09040e in the galaxy, with blue-cyan energy #55c2fe, #a2edfb and #f2fcfc.
- **Lighting:** Letters lit from the upper left with pale yellow faces and orange side walls; separate soft shadows for coin, frame and each letter; the galaxy, the energy rings and the flames are emissive.
- **Ambience:** A clash between the two gods: cosmic and weighty, combining the blue-cyan of Zeus's lightning with flame effects.
- **Materials:** Polished gold in pale and orange tones with engraved Greek key; a glassy sphere holding the galaxy (coin_bg, with coin_bg_highlight); electricity and fire as light.
- **Variants:** Three states by animation (idle, landing, win); in the win the V takes red flames and the S blue electricity, the two gods' elements. The S10 atlas holds the still; the win probably leads into the tall zeus_vs_hades or hades_vs_zeus backdrop (inference).
- **Motion:** zvhp_vs_wild_idle 1.0s: almost still, with a light sweep around the frame and over the letters (shine x16). zvhp_vs_wild_landing 0.5s: the coin and letters drop below centre, bounce up past the top of the frame and settle. zvhp_vs_wild_win 1.5s: the tile pales, the V drops to the lower left in red flame and the S flies to the upper right in a blue electric outline as the coin shrinks to a small ring, then both come back together larger than the frame, still burning and crackling, and settle on the coin.
- **Construction:** 76 parts on 21 bones and 50 slots, all 190 attachments are regions plus 1 clipping mask, so the motion is frame-swapping and transforms rather than mesh deformation: bg, four-piece frame with shadows, coin_shadow, coin_depth, coin_bg sphere, coin_upper_part ring, and V and S each as face, depth and shadow; additive blend for the effects. The cyan and yellow folder names are atlas page tags.
- **Notes:** Shares the gold-letter construction of the WILD symbol (face, depth, shadow) and the frame-with-volutes language, but swaps lava for a galaxy; purple here marks the neutral, special symbols rather than either god.
- **Skeleton (from the file):** Spine 3.7.91 · 21 bones · 50 slots · 190 region, 1 clipping · animations: zvhp_vs_wild_idle (1.0 s), zvhp_vs_wild_landing (0.5 s), zvhp_vs_wild_win (1.5 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 57% · saturation 60% · contrast 33% · warm 52% / cool 46% · brighter towards: bottom-right (3), left (2), bottom-left (1)
- **Palette (measured):** #cc6711 orange 16%, #fce577 gold 16%, #55c2fe blue 12%, #f2fcfc light cyan 11%, #09040e black 10%, #fbb716 orange 5%

### VS coin on a galaxy, special wild (still)

`S10` · atlas · 2 parts · largest 635×472 · sheet `sheets/S10.webp`

- **Role:** Special symbol (S10), the reel still and the mobile paytable's SpecialWildHolder on page 2.
- **Subject:** Gold VS letters on a gold coin ring over a purple galaxy tile in a gold frame with scroll corners.
- **Style:** Stylised 3D-look lettering and ornament, heavy and rounded; landscape tile with the coin overlapping the frame at top and bottom.
- **Rendering:** Hard-edged painted render look (soft edge 0.14) with strong gradient planes; the galaxy is soft and textured.
- **Colour:** Gold #ebaa23, #feeb47 and #fdf38b with orange-brown shadow #ba671c over purple #410e76 and #5d1bbc.
- **Lighting:** Top-left light on the gold with bright highlights; high measured contrast (0.79); the galaxy glows softly.
- **Ambience:** Cosmic, weighty, a confrontation.
- **Materials:** Polished gold, galaxy seen through glass.
- **Variants:** Two parts: sharp 312x215 and a larger vertically smeared 635x472, which reads as the spin-blur version (inference). A SpriteDark slot uses the same atlas.
- **Construction:** A flat atlas of 2 region pictures, no layers; everything is baked into the picture.
- **Notes:** Gold on purple separates this special from the gold-on-red WILD at a glance.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 55% · saturation 77% · contrast 79% · warm 77% / cool 21%
- **Palette (measured):** #ebaa23 orange 42%, #ba671c orange 11%, #410e76 dark purple 10%, #feeb47 gold 9%, #5d1bbc purple 6%, #fdf38b light gold 4%

### POP bubble, special symbol (animated)

`zvhp_pop_symbol` · skeleton · 26 parts · largest 365×366 · sheet `sheets/zvhp_pop_symbol.webp`

- **Role:** Special symbol: the POP symbol, S11 by its scene paths (idle, landing and blurred states); the mobile paytable shows it in POPScatterHolder.
- **Subject:** The word POP in glossy yellow-orange balloon letters with a small gold crown on the O, on a pink-and-orange sticker-like backing with a white outline, in front of an iridescent soap bubble filled with a pastel galaxy and stars.
- **Style:** Casual, candy-like cartoon lettering: fat rounded bubble letters, thick offset outlines and a sticker silhouette; a different, more playful register from the classical gold of WILD and VS.
- **Rendering:** Smooth glossy painting with hard outer edges, soft inner gradients and sharp white specular spots on the letters; the bubble is semi-transparent with rainbow rim colours and a soft outer glow.
- **Colour:** Pastel rainbow with hot accents: white-pink #fcf2f6 outline, magenta #fd27ab backing, gold #fed424 and orange #f97a4a letters, lilac #d7aef8 and plum #5f2d65 inside the bubble, and dark red #840202 for the letter shadows.
- **Lighting:** Top light with glossy highlights on each letter and a large highlight arc on the bubble's upper left (bubble_light); the flare, the glow disc and the stars are emissive; low measured contrast (0.23) overall.
- **Ambience:** Playful, sweet and celebratory; the 'POP' brand element rather than the Greek theme.
- **Materials:** Glossy plastic or jelly letters, a soap bubble with iridescent film, a flat sticker backing, sparkles.
- **Variants:** Four states by animation (idle, idle_anticipation, landing, hit). The S12 atlas holds its paytable still.
- **Motion:** idle 1.0s and idle_anticipation 1.0s: bubble and word swell and shrink once while the rainbow glow around the bubble spreads and fades and the stars twinkle. landing 0.5s: the word arrives squashed wide and low with the bubble behind and above it, then both rise and settle. hit 1.0s: the first P and then the second P swell far out of the bubble towards the viewer, one after the other, the glow flares, and the word snaps back; the bubble does not burst in the frames seen.
- **Construction:** 26 parts on 10 bones and 33 slots (17 meshes, 16 regions): glow, bubble, bubble_shine, bubble_light, four backing silhouettes (pop_1 to pop_4), letters p1, o1 and p2 each with a dark red shadow, crown with crown_shadow, a rainbow lens flare and stars; additive blend for glow and flare. The yellow folder name is an atlas page tag.
- **Notes:** Its animation names (idle, hit, landing) do not carry the zvhp_ prefix the other symbols use, and its style is shared with the POP series look rather than this game's set (inference), so treat it as a brand asset placed among the symbols.
- **Skeleton (from the file):** Spine 3.7.91 · 10 bones · 33 slots · 17 mesh, 16 region · animations: hit (1.0 s), idle (1.0 s), idle_anticipation (1.0 s), landing (0.5 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, low contrast, strong highlights · brightness 62% · saturation 47% · contrast 23% · warm 58% / cool 27% · brighter towards: top (3), left (1)
- **Palette (measured):** #fcf2f6 light magenta 24%, #5f2d65 dark magenta 13%, #c49eb3 magenta 11%, #fd27ab magenta 10%, #840202 dark red 8%, #d7aef8 light purple 5%

### Symbol thumbnails

`symbolThumbs` · atlas · 11 parts · largest 48×55 · sheet `sheets/symbolThumbs.webp`

- **Role:** Small thumbnails of the symbols, one per symbol number (frame sequence S x11); probably for a history or win-list view (inference, the brief names no scene that uses them).
- **Subject:** Miniatures of the symbols; the three shown on the sheet are a purple faceted gem in a gold octagonal setting (S11), the purple Ace with gold rim (S06) and the temple on its cloud (S01).
- **Style:** Reduced versions of the symbol art with the same 3D-look painted treatment, simplified to read at about 48 px.
- **Rendering:** Hard-edged (soft edge 0.103) with strong highlights; fine detail is dropped and the silhouettes are kept.
- **Colour:** The set's palette in small: gold #fde321, #f2a416 and #fcf46e, orange-brown #ae5919, dark red #781009, magenta-purple #960bae and white #f6f3f1.
- **Lighting:** Baked top light and highlights; no separate glow.
- **Ambience:** Same themes as the full symbols.
- **Materials:** Gold, gem, enamel letter, marble, as in the full symbols.
- **Variants:** 11 thumbnails named S, at most 48x55 px. The S11 thumbnail shows a purple gem in a gold octagon, which is not the POP bubble that the S11 skeleton shows.
- **Construction:** One atlas of 11 small region pictures; only three are drawn on the sheet, so the other eight are not described here.
- **Notes:** The gem thumbnail for S11 does not match the other S11 art in this category; check which is live before recreating it.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 55% · saturation 72% · contrast 78% · warm 70% / cool 24%
- **Palette (measured):** #fde321 gold 11%, #ae5919 orange 10%, #f2a416 orange 8%, #f6f3f1 light orange 6%, #781009 dark red 6%, #fcf46e gold 6%

### POP bubble, paytable picture

`S12` · atlas · 1 parts · largest 345×331 · sheet `sheets/S12.webp`

- **Role:** Paytable picture of the POP symbol (mobile paytable, POPScatterHolder); the still of the zvhp_pop_symbol art.
- **Subject:** Glossy yellow-orange POP balloon letters with a gold crown on the O, on a pink and orange sticker backing with a white outline, in front of an iridescent bubble with stars.
- **Style:** Casual, candy-like cartoon lettering with fat rounded forms and thick offset outlines.
- **Rendering:** Smooth glossy painting, hard-edged (soft edge 0.124), with white specular spots and a soft rainbow glow around the bubble.
- **Colour:** Gold #fdce25, #f8e86b and #f7f0a5 letters, orange #f37041 and red-pink #ee4570 backing on the left turning to magenta #f92b9e and #f75ae6 on the right, white-pink outline #fbf5f3.
- **Lighting:** Top light with glossy highlights on the letters; the bubble has a bright highlight at upper left and an emissive rainbow rim.
- **Ambience:** Playful, sweet, celebratory.
- **Materials:** Glossy jelly-like letters, soap bubble, sticker backing, sparkles.
- **Variants:** One part only (345x331); no blur or second size.
- **Construction:** A single flat region picture with everything baked.
- **Notes:** The backing shifts hue from orange to magenta across the word, a gradient the god-themed symbols do not use.
- **Measured:** bright, saturated, warm, high contrast, hard-edged, strong highlights · brightness 73% · saturation 52% · contrast 65% · warm 80% / cool 10%
- **Palette (measured):** #fdce25 gold 20%, #fbf5f3 light red 18%, #f37041 orange 11%, #f8e86b gold 8%, #f92b9e magenta 5%, #f7f0a5 light gold 4%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Expanded wild duel, Zeus side

`zvhp_exp_wild_zuse_vs_hadis` · skeleton · 176 parts · largest 380×891 · sheet `sheets/zvhp_exp_wild_zuse_vs_hadis.webp`

- **Role:** Full-reel expanded wild animation showing the two gods fighting (brief: Expanding_feature/reelN/zeus_win). It holds both outcomes, a Zeus win and a Hades win; when it plays in base game or free spins is not stated.
- **Subject:** A tall gold scroll-cornered frame with WILD plates near the top and bottom: Zeus above, facing the viewer with a lightning bolt, and Hades in the foreground seen from behind, his flaming crown and dark hair filling the lower half and a flaming trident raised at the right. The rig also holds a defeated Zeus set (closed-eye face, slumped body and hanging arms).
- **Style:** Stylised 3D-look painted cartoon character with a large head, barrel torso, big hands and feet and short legs; rounded, chunky shape language. The frame is a narrow column with gold Ionic-style scroll corners.
- **Rendering:** Smooth painted shading that reads like a 3D render: soft gradients, clean alpha edges, no line outlines, small specular highlights on gold and skin; detail is concentrated in the face, key pattern trims and jewellery. Shadow shapes are painted as separate soft dark pieces.
- **Colour:** Split palette: dark maroon #481e28 and red #a6341e for Hades and the WILD plate, gold #fbc92f for frame, armour and flames, orange #ed7517 fire, cyan #4cd8f2 and blue #2973f6 for lightning.
- **Lighting:** Each god carries his own light: cyan-blue glow and bolts on Zeus, yellow-orange fire on Hades; additive glow gradients sit behind them.
- **Ambience:** A fight at its peak; comic-heroic.
- **Materials:** Gold frame and jewellery, white cloth with gold key trim, skin, grey-white hair, dark purple cloth, fire, lightning, a gold wolf-head shoulder guard (parts named "fox").
- **Variants:** Two outcome animations in one rig; counterpart rig zvhp_exp_wild_hades_vs_zeus is used for the hades_win node. Idle versions are the two raising-pose rigs.
- **Motion:** hadis_win 1.5s: Zeus shouts with his bolt raised while Hades lifts the flaming trident, fire sweeps up and fills the column, hiding Zeus, and when it clears Zeus hangs slumped with eyes shut and arms down. zuse_win 1.5s: the same opening, then a blue-white lightning arc fills the column, Zeus rises with the bolt held high, and Hades' crown fire dies down to a dull flame while blue lightning crawls over his back.
- **Construction:** Spine 3.7.91, 187 bones, 148 slots; 179 region, 85 mesh and 1 clipping attachment, additive blending. 176 parts: body pieces, separate shadow pieces (_sh, _shadow), glow gradients, and the WILD plate split into depth, face and yellow letter layers.
- **Notes:** The same opening pose serves both outcomes, and the swap to the winner and loser poses happens behind a full-column flash of fire or lightning. Asset names spell the gods "zuse" and "hadis".
- **Skeleton (from the file):** Spine 3.7.91 · 187 bones · 148 slots · 85 mesh, 179 region, 1 clipping · animations: hadis_win (1.5 s), zuse_win (1.5 s)
- **Measured:** mid-tone, saturated, warm, medium contrast · brightness 51% · saturation 60% · contrast 33% · warm 73% / cool 21% · brighter towards: top-left (14), left (8), top (8)
- **Palette (measured):** #fbc92f gold 16%, #481e28 dark red 16%, #4cd8f2 cyan 9%, #13070b black 8%, #a6341e red 8%, #ed7517 orange 5%

### Expanded wild, Zeus

`zvhp_zeus_raising_pose` · skeleton · 147 parts · largest 442×364 · sheet `sheets/zvhp_zeus_raising_pose.webp`

- **Role:** Zeus as a full-reel expanded wild standing in his frame (brief: Expanding_feature/reelN/zeus_pose). Game mode not stated.
- **Subject:** Zeus stands holding a cyan lightning bolt overhead in his right fist, looking up with blue eyes and a slight smile, in a white chiton with gold key-pattern trim, gold arm bands, a gold belt with a red gem and gold greaves, inside a thin gold frame with scroll corners and a WILD plate at the top.
- **Style:** Stylised 3D-look painted cartoon character with a large head, barrel torso, big hands and feet and short legs; rounded, chunky shape language.
- **Rendering:** Smooth painted shading that reads like a 3D render: soft gradients, clean alpha edges, no line outlines, small specular highlights on gold and skin; detail is concentrated in the face, key pattern trims and jewellery.
- **Colour:** Warm skin and gold against white cloth: off-white #faf4f0, skin tones #b86e53 and #ceb1ba, red-brown #a53b24 and #733a32 in the WILD plate and shadows, black #030101 frame shadow, with blue #277bff from the lightning.
- **Lighting:** Key light from the upper left with soft shading on the right; the bolt is emissive cyan and his eyes glow cyan only during the win; white sparkles drift at the lower left.
- **Ambience:** Confident, commanding, friendly.
- **Materials:** Skin, white cloth with lilac shadows, polished gold, red gem, white hair and beard, lightning.
- **Variants:** Idle and win animations; the Hades equivalent is zvhp_expanded_wild_hadis_raising_pose and the static backdrop behind it is zeus_pose.
- **Motion:** expanded_wild_zuse_raising_pose_idle 1.0s: he holds the pose with a small bob of body and bolt while sparkles drift at the lower left. expanded_wild_zuse_raising_pose_win2 1.5s: blue sparks crackle around the bolt, his mouth opens and his eyes turn glowing cyan, white lightning strikes around his feet and thin arcs run over his body, the WILD plate lifts slightly, then he settles back with the arcs fading.
- **Construction:** Spine 3.7.91, 100 bones, 140 slots; 178 mesh, 162 region and 1 clipping attachment, additive blending. 147 parts: limbs cut at joints, cloth in several panels, face as a mask with eye holes, separate shadow pieces and black frame-shadow shapes.
- **Notes:** The frame is built from corner and edge pieces with a four-frame sequence, so it can shimmer. Clipping keeps the figure inside the reel column.
- **Skeleton (from the file):** Spine 3.7.91 · 100 bones · 140 slots · 178 mesh, 162 region, 1 clipping · animations: expanded_wild_zuse_raising_pose_idle (1.0 s), expanded_wild_zuse_raising_pose_win2 (1.5 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, strong highlights · brightness 53% · saturation 50% · contrast 36% · warm 73% / cool 15% · brighter towards: top-left (9), left (8), top-right (6)
- **Palette (measured):** #faf4f0 light orange 15%, #b86e53 orange 11%, #030101 black 10%, #a53b24 red 10%, #ceb1ba light red 9%, #733a32 red 6%

### Expanded wild duel, Hades side

`zvhp_exp_wild_hades_vs_zeus` · skeleton · 221 parts · largest 558×303 · sheet `sheets/zvhp_exp_wild_hades_vs_zeus.webp`

- **Role:** Full-reel expanded wild animation of the fight (brief: Expanding_feature/reelN/hades_win), holding both a Hades win and a Zeus win. Game mode not stated.
- **Subject:** Hades above, facing the viewer with flaming crown and flaming gold trident, and Zeus in the foreground seen from behind with white hair and gold circlet, inside a gold scroll-cornered frame with WILD plates near the top and bottom; skulls on Hades' belt and a wolf-head shoulder guard.
- **Style:** Stylised 3D-look painted cartoon character with a large head, barrel torso, big hands and feet and short legs; rounded, chunky shape language. Poses are more extreme than the idle rigs, with foreshortened fists and feet.
- **Rendering:** Smooth painted shading that reads like a 3D render: soft gradients, clean alpha edges, no line outlines, small specular highlights on gold and skin; detail is concentrated in the face, key pattern trims and jewellery.
- **Colour:** Red-led: #7a2a27, #b24b35 and #8e5d71 for Hades and cloth, orange #f0731d and pale gold #faf08b for fire and frame, blue #2e7ffd for lightning, near-white #f0edf1 for Zeus' hair.
- **Lighting:** Fire lights Hades from above, cyan-blue lightning lights Zeus; mixed warm and cool rim light where they meet.
- **Ambience:** Violent but cartoonish clash.
- **Materials:** Red skin, gold armour and bands, purple cloth and cloak, bone skulls, fire, lightning, white hair, leather sandals.
- **Variants:** Two outcome animations; pairs with zvhp_exp_wild_zuse_vs_hadis.
- **Motion:** hades_win 1.5s: Hades roars and swings the trident upright, a fire blast bursts over the lower half of the column, Zeus sinks lower with embers on him and Hades hangs above with the trident held high. zeus_win 1.5s: the same opening, then a white-blue lightning arc sweeps up the column on a cyan flash, Zeus turns side-on with a lightning-charged fist forward, and Hades shrinks back and drops lower, wrapped in his cloak.
- **Construction:** Spine 3.7.91, 183 bones, 179 slots; 167 region, 131 mesh, 8 linked mesh and 1 clipping attachment, additive blending. 221 parts with prefixes h_/h2_ for two Hades poses and z_/z2_ for two Zeus poses.
- **Notes:** Each god is drawn twice (winner pose and loser pose), which is why the part count is the highest of the character rigs. The WILD lettering here is a finished yellow-on-red plate.
- **Skeleton (from the file):** Spine 3.7.91 · 183 bones · 179 slots · 131 mesh, 8 linkedmesh, 167 region, 1 clipping · animations: hades_win (1.5 s), zeus_win (1.5 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 46% · saturation 65% · contrast 43% · warm 83% / cool 12% · brighter towards: top-left (12), top (10), bottom-right (9)
- **Palette (measured):** #7a2a27 red 29%, #b24b35 red 14%, #f0731d orange 12%, #faf08b light gold 5%, #8e5d71 red 5%, #2e7ffd blue 4%

### Expanded wild, Hades

`zvhp_expanded_wild_hadis_raising_pose` · skeleton · 110 parts · largest 272×857 · sheet `sheets/zvhp_expanded_wild_hadis_raising_pose.webp`

- **Role:** Hades as a full-reel expanded wild standing in his frame (brief: Expanding_feature/reelN/hades_pose). Game mode not stated.
- **Subject:** Hades laughs with a flaming gold trident raised in his right fist: red skin, flaming hair with a spiked crown, dark beard, gold wolf-head shoulder guard, belt of skulls, purple skirt with a gold chevron panel and tassels, and a cape whose edges burn. He stands in a gold frame with scroll corners and a WILD plate at the top.
- **Style:** Stylised 3D-look painted cartoon character with a large head, barrel torso, big hands and feet and short legs; rounded, chunky shape language. Sharper accents than Zeus: pointed ears, spiked crown, clawed fingers.
- **Rendering:** Smooth painted shading that reads like a 3D render: soft gradients, clean alpha edges, no line outlines, small specular highlights on gold and skin; detail is concentrated in the face, key pattern trims and jewellery.
- **Colour:** Red #b6241c and dark red #501217 body and cape, purple #572a4c cloth, black #0b0305 shadows, with yellow #feec3f, orange #f59415 and pale gold #fef68a from fire and gold.
- **Lighting:** Self-lit by fire: yellow glow from the hair and trident, orange rim on the cape, light mostly from the top left and lower right.
- **Ambience:** Gleeful villain.
- **Materials:** Red skin, gold, purple cloth with gold embroidery, bone, burning cloth, fire.
- **Variants:** Idle and win animations; the Zeus equivalent is zvhp_zeus_raising_pose and the static backdrop behind it is hades_pose.
- **Motion:** zvhp_expanded_wild_hadis_raising_pose_idle 1.0s: he sways slightly with the trident held up, the hair fire flickers (head_fire x15) and yellow embers float around him. zvhp_expanded_wild_hadis_raising_pose_win 1.5s: he pulls the trident down out of view and leans in as the hair fire flares taller, then thrusts the trident up past the WILD plate, which lifts slightly, and returns to the raised pose.
- **Construction:** Spine 3.7.91, 119 bones, 148 slots; 92 mesh, 81 region and 1 clipping attachment, with additive and multiply blending. 110 parts, with many separate shadow pieces (the multiply layers are probably these: inference).
- **Notes:** The only rig in this set that uses multiply blending. Skirt is cut into many named folds for cloth motion.
- **Skeleton (from the file):** Spine 3.7.91 · 119 bones · 148 slots · 92 mesh, 81 region, 1 clipping · animations: zvhp_expanded_wild_hadis_raising_pose_idle (1.0 s), zvhp_expanded_wild_hadis_raising_pose_win (1.5 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 40% · saturation 70% · contrast 33% · warm 92% / cool 2% · brighter towards: bottom-right (8), top-left (7), bottom-left (4)
- **Palette (measured):** #0b0305 black 18%, #b6241c red 15%, #feec3f gold 14%, #572a4c dark magenta 12%, #501217 dark red 11%, #f59415 orange 11%

### Zeus-wins backdrop for the expanding symbol

`zeus_vs_hades` · atlas · 1 parts · largest 493×1384 · sheet `sheets/zeus_vs_hades.webp`

- **Role:** Background picture of the expanding VS symbol when Zeus wins (S13_Expanding/expanding_symbol/zeus_win); a tall reel-height panel, not a paying symbol in itself.
- **Subject:** A storm sky with a bright blue-white cloud core and faint lightning in the upper two thirds, over a band of orange and yellow lava or fire-lit cloud in the lower third.
- **Style:** Painterly atmospheric background, loose and soft, with no characters or hard shapes; a tall 493x1384 column format.
- **Rendering:** Soft digital painting with blended brushwork and low detail, although the measured edge value is hard (soft edge 0.0) because the panel is an opaque rectangle; a few thin lightning lines are the only fine detail.
- **Colour:** Split by temperature: blues #283e90, #4785d9, #7ac4f7 and deep #0b1054 above, orange #cf410e and muted red #843b3b below.
- **Lighting:** The cloud core is the light source in the upper part and the lava glows from below; darkening towards the top.
- **Ambience:** Sky overpowering the underworld: stormy and triumphant on Zeus's side.
- **Materials:** Cloud, lightning and molten lava, all as soft light.
- **Variants:** Paired with hades_vs_zeus, the same format for the other outcome.
- **Construction:** A single opaque 493x1384 picture in its own atlas, meant to sit behind a character or effect layer (inference).
- **Notes:** Kept deliberately low in detail and contrast in the middle, so whatever is placed over it reads; the blue upper and orange lower halves repeat the game's two-sided palette.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 38% · saturation 71% · contrast 60% · warm 33% / cool 66% · brighter towards: bottom (1)
- **Palette (measured):** #283e90 blue 27%, #4785d9 blue 26%, #cf410e orange 15%, #843b3b red 12%, #0b1054 dark blue 6%, #7ac4f7 blue 5%

### Expanded wild backdrop, Zeus

`zeus_pose` · atlas · 1 parts · largest 493×1383 · sheet `sheets/zeus_pose.webp`

- **Role:** Tall still image placed behind the Zeus expanded wild inside the expanding symbol (brief: S13_Expanding/expanding_symbol/zeus_pose/sprite); it is a blurred backdrop, not the character itself.
- **Subject:** An out-of-focus blue image with a pale glow in the lower middle and soft shapes that suggest a figure or clouds; no readable detail.
- **Style:** Abstract blurred backdrop.
- **Rendering:** Heavily blurred and low in detail, apparently a small image scaled up; no edges or outlines.
- **Colour:** Blues #5786f1 and #323c8e with pale cyan-white #e3f3f3 and #c2cfe1 in the glow, and a little violet #93629c at the bottom.
- **Lighting:** A soft bright core low in the frame, darkening to deep blue at the top.
- **Ambience:** Cool, misty, celestial.
- **Materials:** None readable; cloud-like haze.
- **Variants:** One 493x1383 image; hades_pose is the warm counterpart.
- **Construction:** Single opaque atlas image sized to a full reel column, used under the Spine character.
- **Notes:** Listed under characters because of its name, but it works as a reel-column background that tints the column blue behind Zeus.
- **Measured:** mid-tone, saturated, cool, high contrast, hard-edged, strong highlights · brightness 57% · saturation 45% · contrast 75% · warm 2% / cool 95% · brighter towards: bottom-left (1)
- **Palette (measured):** #5786f1 blue 26%, #323c8e blue 20%, #e3f3f3 light cyan 13%, #89a9e0 blue 13%, #c2cfe1 light blue 12%, #93629c magenta 6%

### Hades-wins backdrop for the expanding symbol

`hades_vs_zeus` · atlas · 1 parts · largest 493×1384 · sheet `sheets/hades_vs_zeus.webp`

- **Role:** Background picture of the expanding VS symbol when Hades wins (S13_Expanding/expanding_symbol/hades_win); a tall reel-height panel, not a paying symbol in itself.
- **Subject:** A fiery sky of red, orange and yellow smoke and cloud with embers, over a dark red ground with bright lava streams at the bottom; a small pale pink shape is cut off at the left edge.
- **Style:** Painterly atmospheric background, loose and soft, with no characters; a tall 493x1384 column format.
- **Rendering:** Soft digital painting with blended brushwork, wispy flame strokes and scattered ember dots; opaque rectangle (measured soft edge 0.0).
- **Colour:** Entirely warm (warm 1.0): dark red #943123 at the top and bottom, orange #f2891c, #d6541f and #e38e54 in the central glow.
- **Lighting:** A large yellow-orange glow in the middle acts as the light source, with the top fading to dark red; lava and embers are emissive.
- **Ambience:** The underworld in full blaze: hot and threatening on Hades's side.
- **Materials:** Smoke, fire, embers and lava as soft light.
- **Variants:** Paired with zeus_vs_hades, the same format for the other outcome.
- **Construction:** A single opaque 493x1384 picture in its own atlas, meant to sit behind a character or effect layer (inference).
- **Notes:** Unlike its pair it has no cool half: the whole panel is one temperature. The cut-off pink shape at the left edge looks like a remnant of another layer (inference) and need not be recreated.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 44% · saturation 81% · contrast 46% · warm 100% / cool 0% · brighter towards: bottom (1)
- **Palette (measured):** #943123 red 42%, #f2891c orange 38%, #d6541f orange 12%, #e38e54 orange 5%

### Expanded wild backdrop, Hades

`hades_pose` · atlas · 1 parts · largest 514×1324 · sheet `sheets/hades_pose.webp`

- **Role:** Tall still image placed behind the Hades expanded wild inside the expanding symbol (brief: S13_Expanding/expanding_symbol/hades_pose/sprite); a blurred backdrop, not the character.
- **Subject:** A blurred red underworld scene: red haze above, a paler orange band in the middle, dark rock terraces and a yellow glow of lava at the bottom.
- **Style:** Soft painted backdrop, low detail.
- **Rendering:** Blurred painting with only faint rock edges and lava streaks visible; no outlines.
- **Colour:** Reds #d04830 and #95200a with dusky #8b343e at the top and orange #e47c45 in the glow.
- **Lighting:** Glow from the lava at the bottom and from the hazy middle band; top and rock in shadow.
- **Ambience:** Smouldering, oppressive heat.
- **Materials:** Haze, rock, lava.
- **Variants:** One 514x1324 image; zeus_pose is the cool counterpart.
- **Construction:** Single opaque atlas image sized to a full reel column, used under the Spine character.
- **Notes:** Follows the same cool-versus-warm pairing as the two environments.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 32% · saturation 82% · contrast 38% · warm 100% / cool 0% · brighter towards: top-left (1)
- **Palette (measured):** #d04830 red 42%, #95200a red 41%, #8b343e red 10%, #e47c45 orange 7%

### Zeus mascot

`zeha_mascot_zeus` · skeleton · 115 parts · largest 246×277 · sheet `sheets/zeha_mascot_zeus.webp`

- **Role:** Animated Zeus character beside the logo at the top of the reel board (brief: Reels/ResizeEffect/character/zeus); the main screenshot shows him at the top left. Both modes (inference).
- **Subject:** Zeus in a wide stance holding a glowing lightning bolt in his raised right hand with his left fist thrust forward: white swept hair and beard, gold circlet, white chiton with gold key-pattern borders, red diamond gem on a gold belt, gold arm bands and greaves, brown sandals.
- **Style:** Stylised 3D-look painted cartoon character with a large head, barrel torso, big hands and feet and short legs; rounded, chunky shape language.
- **Rendering:** Smooth painted shading that reads like a 3D render: soft gradients, clean alpha edges, no line outlines, small specular highlights on gold and skin; detail is concentrated in the face, key pattern trims and jewellery.
- **Colour:** Warm skin and browns (#81331c, #4d2a32, #2e0707) against white and grey cloth and hair (#e9eaec, #cdc1c2, #a3929d), slate blue #515468 in the hair shadow, and cyan #74f4fc from the bolt.
- **Lighting:** Soft key from above and slightly left; a cyan rim on the left side of the robe and arm from the lightning; the bolt has a separate glow layer.
- **Ambience:** Stern but likeable hero.
- **Materials:** Skin, white cloth, polished gold with engraved key pattern, faceted red gem, leather, hair, lightning.
- **Variants:** One rig with six animations; his opposite number is zvhp_mascot_hades.
- **Motion:** Animations (names carry a [GREEN] tag). idle 2.0s: he holds the stance while the bolt flickers. idle_break 4.0s: the same with one eye narrowing and a cyan glow pulsing on his robe. anoyed_1 1.5s: he scowls and shakes the bolt. anoyed_2 1.33s: eyes shut, he drops the bolt to upright in front of his shoulder and lifts it again. win_1 1.83s: eyes closed, he swings the bolt upright and back twice. win_2 1.5s: a cyan glow rises over his robe, he lifts the bolt level above his head, shouts as thin forks shoot up from it, then returns to the stance.
- **Construction:** Spine 3.7.91, 76 bones, 110 slots; 111 region and 85 mesh attachments, additive blending. 115 parts: face mask with eye holes, hair and beard in several locks, robe in panels, separate shadow pieces, and the bolt as thunder_light plus thunder_light_glow.
- **Notes:** Small source size (largest part 246x277) because he is shown small on screen. The annoyed and win animations suggest he reacts to results in tandem with Hades (inference).
- **Skeleton (from the file):** Spine 3.7.91 · 76 bones · 110 slots · 85 mesh, 111 region · animations: [GREEN]zeha_mascot_zeus_anoyed_1 (1.5 s), [GREEN]zeha_mascot_zeus_anoyed_2 (1.33 s), [GREEN]zeha_mascot_zeus_idle (2.0 s), [GREEN]zeha_mascot_zeus_idle_break (4.0 s), [GREEN]zeha_mascot_zeus_win_1 (1.83 s), [GREEN]zeha_mascot_zeus_win_2 (1.5 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 53% · saturation 44% · contrast 44% · warm 73% / cool 26% · brighter towards: top-right (6), left (5), top (5)
- **Palette (measured):** #81331c red 15%, #cdc1c2 grey 13%, #515468 blue 13%, #a3929d grey 10%, #e9eaec white 9%, #4d2a32 dark red 4%

### Hades mascot

`zvhp_mascot_hades` · skeleton · 177 parts · largest 216×213 · sheet `sheets/zvhp_mascot_hades.webp`

- **Role:** Animated Hades character beside the logo at the top of the reel board (brief: Reels/ResizeEffect/character/hades); the main screenshot shows him at the top right. Both modes (inference).
- **Subject:** Hades standing with a gold trident topped with flame in his left hand and fire curling from his right: red skin, flaming hair inside a spiked crown, dark beard, gold wolf-head shoulder guard, a belt of four skulls (one with glowing eyes) and a long purple skirt with gold hem.
- **Style:** Stylised 3D-look painted cartoon character with a large head, barrel torso, big hands and feet and short legs; rounded, chunky shape language. More angular accents than Zeus (spikes, pointed ears, claws).
- **Rendering:** Smooth painted shading that reads like a 3D render: soft gradients, clean alpha edges, no line outlines, small specular highlights on gold and skin; detail is concentrated in the face, key pattern trims and jewellery.
- **Colour:** Orange #f36f25 and gold-orange #fbc246 fire, reds #b95d4c and #aa231c skin, dark plum #502844 cloth, with a pink #e96a84 glow behind the trident.
- **Lighting:** Lit by his own fire: warm light from the hair above and the hand flame at lower left; pink-magenta glow layer behind the trident head.
- **Ambience:** Mischievous, menacing in a cartoon way.
- **Materials:** Red skin, gold armour, purple cloth, bone, fire, dark leather belt.
- **Variants:** One rig with six animations mirroring the Zeus mascot's set.
- **Motion:** idle 2.0s: he stands with a slight sway while the crown, hand and trident flames flicker. idle_break 3.0s: the hand flame grows taller and his grin widens, then both settle. annoyed_1 1.5s: the hand flame goes out to embers and smoke, he frowns at his empty hand and a faint flame returns. annoyed_2 1.5s: he glares while the trident flame flares and sheds sparks. win_1 1.67s: he laughs open-mouthed with the hand flame flaring. win_2 1.67s: he raises his hand and the flame shoots up into a tall plume while he laughs, then lowers it.
- **Construction:** Spine 3.7.91, 91 bones, 128 slots; 139 region, 111 mesh and 81 linked mesh attachments, additive blending. 177 parts; fire is hand-drawn frame animation in three places (crown, hand, weapon).
- **Notes:** More parts and longer flame sequences than Zeus because fire is frame-animated. The shoulder guard is named "fox" in the files but reads as a wolf or jackal head.
- **Skeleton (from the file):** Spine 3.7.91 · 91 bones · 128 slots · 111 mesh, 81 linkedmesh, 139 region · animations: zvhp_mascot_hades_annoyed_1 (1.5 s), zvhp_mascot_hades_annoyed_2 (1.5 s), zvhp_mascot_hades_idle (2.0 s), zvhp_mascot_hades_idle_break (3.0 s), zvhp_mascot_hades_win_1 (1.67 s), zvhp_mascot_hades_win_2 (1.67 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 46% · saturation 70% · contrast 50% · warm 91% / cool 4% · brighter towards: top-left (5), top-right (4), left (4)
- **Palette (measured):** #f36f25 orange 31%, #502844 dark magenta 14%, #b95d4c red 14%, #fbc246 orange 12%, #aa231c red 11%, #e96a84 red 4%


## Logo and title

The game's own wordmark.

### Game logo and provider logo

`logo` · atlas · 4 parts · largest 1209×556 · sheet `sheets/logo.webp`

- **Role:** Atlas with the game logo and the Pragmatic Play provider logo; the brief places it on the loader, the loader progress bar and a promotions panel. The same logo design sits at the top of the reel board in the main screenshot (both modes: inference).
- **Subject:** "ZEUS vs HADES POP": ZEUS in ice-blue faceted letters, HADES in gold-orange letters topped with flames, a small "vs" on a plaque between them, and a rounded gold "POP" below, all set on a blue-grey stone slab with a Greek key border and lightning around it. The other parts are the white-and-orange Pragmatic Play wordmark with its crowned circle, and a short orange glow bar.
- **Style:** Chunky extruded 3D-look lettering, slightly irregular carved-stone letterforms for ZEUS and HADES and a soft bubble face for POP; compact stacked lock-up.
- **Rendering:** Painted to look like a 3D render: bevelled faces, dark extrusion sides, crisp edges with a soft outer glow; the provider logo is flat vector.
- **Colour:** Two-sided scheme: blue and cyan for Zeus (#28b4fb, #87baf3, #6d7ac5) against orange-gold for Hades and POP (#ef9021); the measured white (#feffff) is mostly the provider wordmark.
- **Lighting:** Top-lit bevels with bright upper faces; cyan lightning glow around the Zeus half and flame glow on the Hades half act as emissive accents.
- **Ambience:** Rivalry of sky and underworld, loud and playful rather than solemn.
- **Materials:** Ice or crystal blue stone, polished gold, fire, cracked grey-blue marble slab with a meander border.
- **Variants:** Two sizes of the provider logo (anim_33 at 1209x556 and anim_32 at 244x113); one game logo at 289x174. No separate free-spins logo in this unit.
- **Construction:** Four atlas parts: game logo as a single flattened sprite, provider logo at two sizes, and an "Orangeglow" bar used as the loader progress fill (the brief links it to ProgressBar/foreground).
- **Notes:** The logo is baked as one image, so the split blue/orange colouring is fixed; it summarises the whole palette logic of the game (cool Zeus left, warm Hades right, gold as the shared accent).
- **Measured:** bright, saturated, warm, medium contrast, strong highlights · brightness 77% · saturation 44% · contrast 48% · warm 83% / cool 17% · brighter towards: bottom-left (2)
- **Palette (measured):** #feffff light cyan 42%, #ef9021 orange 37%, #87baf3 blue 4%, #b0e3e8 light cyan 3%, #6d7ac5 blue 2%, #28b4fb blue 2%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Win meter effect

`zeha_win_met_fx` · skeleton · 39 parts · largest 544×73 · sheet `sheets/zeha_win_met_fx.webp`

- **Role:** Effect on the win display of the reels in base and free games (scene path Reels/ResizeEffect/win_effect/base and /free); inference from the name: it plays on the win meter when a win is shown.
- **Subject:** A horizontal bar of light the width of the win meter: a rounded capsule flash in the middle (plain cyan in the base game, cream with a pink glow and a dark-centred ring in the free game) that gives way to thin horizontal strokes, short upright arcs and tiny sparks along the line.
- **Style:** Abstract light strokes with rounded ends; no lettering.
- **Rendering:** Hand-drawn frame animation of glowing lines with soft edges; very little drawn per frame.
- **Colour:** Base game in cyan #65e3fd and green-cyan #1df7e6 / #07cca6; free game in pink-red #ff608b and orange-red #fb4d16 with a cream core #fef5cf and peach #ffbb96.
- **Lighting:** Emissive; a near-white core flash with a coloured halo, and thin bright strokes on transparency.
- **Ambience:** A short, sharp accent on the win amount.
- **Materials:** Light and sparks only.
- **Variants:** Two colour versions: zeha_win_met_fx_basegame (cyan) and zeha_win_met_fx_freegame (pink, orange and cream).
- **Motion:** Two animations: zeha_win_met_fx_basegame 0.6 s from cyan/win_met_fx (18 frames) and zeha_win_met_fx_freegame 0.7 s from red/win_met_freegame (21 frames). Base game: a cyan capsule appears in the centre, widens with bracket shapes at its ends and sparks inside, then breaks into thin strokes and arcs spread along the meter that thin out and vanish. Free game: it starts as a thin cream line with pink ends, swells into a cream capsule with a dark-centred ring and red dots, then breaks into orange strokes and arcs that fade the same way.
- **Construction:** Spine skeleton with 1 bone and 4 slots holding 78 region attachments from 39 images (largest 544x73), with additive blending; the frames are wide strips trimmed tightly to their lit area.
- **Notes:** As with the reel highlight, the free game replaces cyan with pink and orange and replaces the white core with cream.
- **Skeleton (from the file):** Spine 3.7.91 · 1 bones · 4 slots · 78 region · animations: zeha_win_met_fx_basegame (0.6 s), zeha_win_met_fx_freegame (0.7 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 76% · saturation 53% · contrast 35% · warm 62% / cool 38% · brighter towards: top (2), left (1), top-right (1)
- **Palette (measured):** #fef5cf light gold 30%, #65e3fd cyan 23%, #ff608b red 12%, #1df7e6 cyan 8%, #fb4d16 red 8%, #ffbb96 light orange 7%

### POP feature congratulation, three levels

`zeha_pop_congrats` · skeleton · 296 parts · largest 601×976 · sheet `sheets/zeha_pop_congrats.webp`

- **Role:** The main celebration of the POP feature (scene path POP_Feature/Pivot/Spine); inference from the animation names: it plays when a POP level is reached, at three rising levels.
- **Subject:** Zeus with a lightning bolt and Hades with flaming hair and a gold staff side by side in the upper part of the screen, above a single 'POP' logo set inside a large iridescent soap bubble, over a full-height rainbow background with small bubbles, four-point sparkles and rainbow swooshes circling the bubble.
- **Style:** Stylised 3D-cartoon characters with large heads and exaggerated muscles; bubbly, rounded 'POP' lettering in glossy yellow with a pink outline, a dark red drop shadow and a small crown on the O.
- **Rendering:** Characters and letters are painted to look like smooth 3D renders with clean edges; the background is a soft blurred rainbow gradient; bubbles are glassy with rainbow rims. Rigged parts carry the characters, with frame sequences for the effects.
- **Colour:** The widest palette in the game: pastel rainbow with light magenta #f6e8f1 and #eba5f3, peach #f1b590, mint #9ddab4, blue #5e6bde and hot pink #fc28aa, against the characters' dark red #7e130a and plum #5f2f57.
- **Lighting:** Top light on the characters (the brief measures light mostly from the top); additive cyan lightning glows, rainbow swooshes, a white star flare with a rainbow halo, and specular highlights on the bubbles and letters.
- **Ambience:** Playful and sweet, a deliberate contrast with the stormy mythological base game.
- **Materials:** Soap bubbles (clear with rainbow sheen, and one filled with a rainbow galaxy swirl), glossy plastic-like lettering, skin, cloth with Greek key trim, gold, lightning and fire.
- **Variants:** Three levels: 1st (3.0 s), 2nd (4.4 s) and 3rd (6.0 s). Both Zeus and Hades appear in the same rig, with an angry-eye alternative for Hades among the parts.
- **Motion:** Animations zeha_pop_congrats_1st_level 3.0 s, 2nd_level 4.4 s and 3rd_level 6.0 s; frame sequences ring_bubbles_fx (8, 7 and 6), thunder_u 5, fx_round 3, trail 12, blusr 13, new_crown_fire 14 and star 23. In each, the two gods appear first on the rainbow backdrop, the POP bubble forms below them (in the 2nd level from a cluster of small bubbles, in the 3rd from a single 'O' inside a ring of small bubbles, with comet trails crossing), and rainbow swooshes circle it. The 1st level ends with the bubble shrinking and the scene fading to a few drifting bubbles; in the 2nd the bubble swells and squashes the logo wide before settling, and the 2nd and 3rd end with the logo growing until it fills the screen.
- **Construction:** The largest rig of the set: 296 images, 258 bones, 361 slots, with 236 region, 209 mesh and 37 linked-mesh attachments, 1 clipping mask and 2 paths, plus additive slots. Zeus and Hades are built from the same kind of body parts as the big-win rigs (torso, limbs, cloth, cape, face with eye variants); 172 smaller parts are not shown on the sheet.
- **Notes:** The 'POP' wordmark is built from separate letters (p1, p2 and a shared o) with matching shadow copies and solid pink and white backing shapes (pop_1 to pop_4), so the outline layers can pop in one after another. Zeus's face changes during the animations, from a frown to an open-mouthed look at the bubble.
- **Skeleton (from the file):** Spine 3.7.91 · 258 bones · 361 slots · 236 region, 209 mesh, 1 clipping, 37 linkedmesh, 2 path · animations: [GREEN]zeha_pop_congrats_1st_level (3.0 s), [GREEN]zeha_pop_congrats_2nd_level (4.4 s), [GREEN]zeha_pop_congrats_3rd_level (6.0 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 63% · saturation 47% · contrast 32% · warm 61% / cool 29% · brighter towards: top (12), top-left (12), top-right (7)
- **Palette (measured):** #f6e8f1 light magenta 15%, #f1b590 light orange 13%, #eba5f3 light magenta 6%, #5f2f57 dark magenta 6%, #9ddab4 green 6%, #7e130a dark red 4%

### POP Burst banner

`geol_pop_burst_banner` · skeleton · 58 parts · largest 595×1144 · sheet `sheets/geol_pop_burst_banner.webp`

- **Role:** The banner of the 'Burst' result in the POP feature (scene path POP_Feature/Pivot/Banner/Burst); inference: one of three named POP outcomes, with Spark and Snap.
- **Subject:** A yellow 'POP' wordmark with a crown on a pink and dark red backing, under a folded magenta ribbon with gold stars at its ends, surrounded by soap bubbles, gold stars, coins, confetti and sparkles.
- **Style:** Rounded, inflated cartoon lettering with a thick two-step outline (pink, then white) and a dark red drop shadow; the ribbon is faceted like folded paper.
- **Rendering:** 3D-render look with smooth gradients and crisp edges on letters, stars, ribbon and coins; glassy bubbles; soft additive flares behind. Rigged parts with short frame sequences.
- **Colour:** Magenta and gold: hot pink #f028ad, plum #642664 and purple-magenta #bd29c4, dark red #840202 for the shadows, gold #fce355 / #fcbe20, and near-white #fcf0f1 for the outline and flare.
- **Lighting:** A white-pink radial flare and a rainbow-edged ring flare behind the wordmark, a yellow back glow above it, and specular highlights on the letters and stars.
- **Ambience:** Festive and loud, the warmest of the three POP banners.
- **Materials:** Glossy plastic-like letters, folded satin ribbon, gold stars and coins, soap bubbles, paper confetti.
- **Variants:** The magenta member of a set of three banners (Burst magenta, Spark blue, Snap green) that share the wordmark, stars, coins and bubbles.
- **Motion:** Animations geol_pop_burst_banner_in 1.0 s, _loop 1.0 s and _out 1.0 s; frame sequences magenta/ribon 5, red/pop 3 and yellow/coin 6. In: from an empty frame the ribbon and a dim orange wordmark appear inside a yellow-green ray burst with a ring flare, rainbow glints fly outwards, and the burst gives way to the white-pink glow with the coins and stars below. Loop: the wordmark holds while bubbles drift around it and confetti moves above the ribbon. Out: the ray burst returns, the ribbon and backing disappear, the bare gold letters spread apart with the O enlarged, and a single fading P and rainbow glints are left.
- **Construction:** 58 images, 144 bones, 118 slots, 159 region and 15 mesh attachments, with additive slots; the letters p1, p2 and o1 each have a separate dark red shadow image, and fifteen small 'cloud_particles' sheets supply the dust.
- **Notes:** The stacked outline is built from separate flat shapes (pop_1 to pop_5), not painted into the letters, which is what lets one wordmark be recoloured for the three banners.
- **Skeleton (from the file):** Spine 3.7.91 · 144 bones · 118 slots · 159 region, 15 mesh · animations: geol_pop_burst_banner_in (1.0 s), geol_pop_burst_banner_loop (1.0 s), geol_pop_burst_banner_out (1.0 s)
- **Measured:** mid-tone, saturated, warm, low contrast, strong highlights · brightness 56% · saturation 57% · contrast 20% · warm 71% / cool 11% · brighter towards: top (4), bottom-left (3), right (1)
- **Palette (measured):** #fcf0f1 light red 23%, #642664 dark magenta 16%, #840202 dark red 12%, #f028ad magenta 12%, #fce355 gold 10%, #ec6fe2 magenta 5%

### POP Burst backdrop

`POP_Burst` · atlas · 1 parts · largest 689×1725 · sheet `sheets/POP_Burst.webp`

- **Role:** The background image behind the Burst banner (scene path POP_Feature/Pivot/Banner/Burst/Bg/Sprite).
- **Subject:** A tall portrait backdrop: a magenta sky with small stars at the top, soft pink and yellow light columns in the middle and a heap of gold coins and gold stars at the bottom.
- **Style:** A blurred, dreamlike gradient above a sharply drawn cartoon coin pile; no lettering.
- **Rendering:** A single opaque painted image, hard-edged rectangle; the coin pile has a 3D-render look with star-embossed coins, and the upper two thirds are a soft-focus gradient.
- **Colour:** Pink #e77faa and magenta #d527c0 above, pale gold #ead78f and yellow #f4d657 in the light, orange-gold #e0953d in the coins.
- **Lighting:** Soft yellow light rises from behind the coin pile; the coins carry top highlights.
- **Ambience:** Sweet and celebratory, a candy-coloured treasure scene.
- **Materials:** Gold coins and gold stars with polished highlights; the rest is light and haze.
- **Variants:** One of three backdrops with the same layout and the same coin pile: Burst (magenta), Spark (blue and pastel), Snap (green).
- **Motion:** None; a still image.
- **Construction:** One image of 689x1725 in its own atlas, placed behind the banner skeleton.
- **Notes:** The centre is kept soft and empty so the banner and the amount read on top of it.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 60% · saturation 58% · contrast 59% · warm 78% / cool 1% · brighter towards: bottom (1)
- **Palette (measured):** #e77faa red 30%, #d527c0 magenta 25%, #ead78f gold 20%, #e0953d orange 13%, #f4d657 gold 6%, #d98ede magenta 3%

### POP Spark banner

`geol_POP_total_spark` · skeleton · 48 parts · largest 540×371 · sheet `sheets/geol_POP_total_spark.webp`

- **Role:** The banner of the 'Spark' result in the POP feature (scene path POP_Feature/Pivot/Banner/Spark/Spine_pop); inference: one of three named POP outcomes.
- **Subject:** A yellow 'POP' wordmark with a crown on a blue backing, under a curved turquoise ribbon with star-tipped ends, with a pastel starburst behind and bubbles, gold stars, coins, confetti and white sparkles around.
- **Style:** The same inflated cartoon lettering as the Burst banner, here with a deep blue outline and a white outer edge; the ribbon is smooth and curved with printed stars.
- **Rendering:** 3D-render look with clean edges and smooth gradients; glassy bubbles; soft additive starbursts. Rigged parts with short frame sequences.
- **Colour:** Blue and gold: dark blue #093f7c for the backing, turquoise #2fcbd0 and #88f5f4 for the ribbon and glow, blue #4386d8, gold #fdd22d / #fdf07b for the letters and near-white #f5eef2.
- **Lighting:** A pastel rainbow ray burst and a white streak burst behind the wordmark, a rainbow ring flare, and four-point white sparkles in front.
- **Ambience:** Bright, cool and sparkling.
- **Materials:** Glossy letters, satin ribbon, gold stars and coins, clear soap bubbles, small confetti pieces.
- **Variants:** The blue member of the three POP banners; it shares its skeleton layout, part names and counts with the Snap banner.
- **Motion:** Animations geol_pop_spark_banner_in 1.0 s, _loop 1.0 s and _out 1.0 s; frame sequences blue/bubble 8, cyan/particals 3, cyan/ribon 5, yellow/coin 5 and yellow/particals 4. In: a small white streak burst appears first, then the ribbon, wordmark and coins inside a yellow-green ray burst with a ring flare, which fades to leave the pastel starburst, bubbles and confetti. Loop: the wordmark holds while bubbles drift, sparkles change place and confetti falls towards the coins and stars. Out: the yellow ray burst returns, the ribbon and blue backing disappear, the bare gold letters remain for a moment and a single fading P is left inside the fading ring.
- **Construction:** 48 images, 61 bones, 130 slots, 113 region and 17 mesh attachments, with additive slots; the backing 'pop_back' is one image holding the outline, and the letters p, p1 and 0 sit on top as separate parts.
- **Notes:** Spark and Snap are the same rig with recoloured backing, ribbon and glows; the yellow letters, stars, coins, bubbles and confetti are identical.
- **Skeleton (from the file):** Spine 3.7.91 · 61 bones · 130 slots · 113 region, 17 mesh · animations: geol_pop_spark_banner_in (1.0 s), geol_pop_spark_banner_loop (1.0 s), geol_pop_spark_banner_out (1.0 s)
- **Measured:** bright, saturated, cool, medium contrast, strong highlights · brightness 66% · saturation 57% · contrast 47% · warm 26% / cool 73% · brighter towards: top (3), bottom-left (2), bottom-right (2)
- **Palette (measured):** #093f7c dark blue 21%, #f5eef2 light magenta 20%, #fdd22d gold 12%, #2fcbd0 cyan 7%, #88f5f4 cyan 7%, #4386d8 blue 6%

### POP Spark backdrop

`POP_Spark` · atlas · 1 parts · largest 689×1725 · sheet `sheets/POP_Spark.webp`

- **Role:** The background image behind the Spark banner (scene path POP_Feature/Pivot/Banner/Spark/Bg/Sprite).
- **Subject:** A tall portrait backdrop: a blue starry sky at the top, blurred pastel patches of mint, lilac, white and peach in the middle and the gold coin and star pile at the bottom.
- **Style:** A blurred pastel gradient above the sharply drawn coin pile; no lettering.
- **Rendering:** A single opaque painted image with a soft-focus upper part and a 3D-render look coin pile.
- **Colour:** Blue #3668d9 and #688ace above, mint #9ddbcc, lilac #cf9ee7 and near-white #eeeaf3 in the middle, gold #f4d868 and orange #e1953d in the coins.
- **Lighting:** A white glow sits in the upper middle, where the banner goes; the coins are lit from above.
- **Ambience:** Light, airy and cool.
- **Materials:** Gold coins and stars; the rest is light and haze.
- **Variants:** The blue and pastel member of the three backdrops (Burst, Spark, Snap).
- **Motion:** None; a still image.
- **Construction:** One image of 689x1725 in its own atlas.
- **Notes:** The coin pile matches the one in the Burst backdrop in layout; only the sky and light change.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 69% · saturation 44% · contrast 58% · warm 33% / cool 62% · brighter towards: bottom (1)
- **Palette (measured):** #9ddbcc cyan 17%, #3668d9 blue 15%, #f4d868 gold 13%, #688ace blue 12%, #cf9ee7 light purple 11%, #eeeaf3 light purple 9%

### POP Snap banner

`geol_pop_total_snap` · skeleton · 48 parts · largest 540×371 · sheet `sheets/geol_pop_total_snap.webp`

- **Role:** The banner of the 'Snap' result in the POP feature (scene path POP_Feature/Pivot/Banner/Snap/Spine_pop_snap); inference: one of three named POP outcomes.
- **Subject:** A yellow 'POP' wordmark with a crown on a green backing, under a curved green ribbon with star-tipped ends, with a mint starburst behind and bubbles, gold stars, coins, confetti and white sparkles around.
- **Style:** The same inflated cartoon lettering, here with a dark green outline and a white outer edge; smooth curved ribbon with printed stars.
- **Rendering:** 3D-render look with clean edges and smooth gradients; glassy bubbles; soft additive starbursts. Rigged parts with short frame sequences.
- **Colour:** Green and gold: dark green #004717 for the backing, green #03a834 and #49da7e, mint #a4f3b7 for the glow, gold #fdd22d / #fdf07b for the letters and white #f4f1f2.
- **Lighting:** A mint-white ray burst and glow behind the wordmark, a rainbow ring flare, and white four-point sparkles in front.
- **Ambience:** Fresh and bright.
- **Materials:** Glossy letters, satin ribbon, gold stars and coins, clear soap bubbles, confetti.
- **Variants:** The green member of the three POP banners; the same rig as the Spark banner with recoloured backing, ribbon and glows.
- **Motion:** Animations geol_pop_snap_banner_in 1.0 s, _loop 1.0 s and _out 1.0 s; frame sequences blue/bubble 8, cyan/particals 3, cyan/ribon 4, yellow/coin 5 and yellow/particals 4. The frames match the Spark banner step for step: a small white streak burst, then ribbon, wordmark and coins inside a yellow-green ray burst that fades to the mint starburst; a loop of drifting bubbles, sparkles and falling confetti; and an exit in which the ray burst returns, ribbon and green backing disappear and a single fading P is left.
- **Construction:** 48 images, 61 bones, 130 slots, 113 region and 17 mesh attachments, with additive slots, the same counts as the Spark banner; a separate soft ribbon shadow (ribon_sh, 596x219) sits behind the ribbon.
- **Notes:** To add a fourth banner in this style, only pop_back, the ribbon frames, the two glows and the backdrop need new colours.
- **Skeleton (from the file):** Spine 3.7.91 · 61 bones · 130 slots · 113 region, 17 mesh · animations: geol_pop_snap_banner_in (1.0 s), geol_pop_snap_banner_loop (1.0 s), geol_pop_snap_banner_out (1.0 s)
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 65% · saturation 62% · contrast 42% · warm 25% / cool 50% · brighter towards: top (3), bottom-left (2), bottom-right (2)
- **Palette (measured):** #004717 dark green 21%, #f4f1f2 white 19%, #fdd22d gold 11%, #03a834 green 11%, #a4f3b7 light green 8%, #49da7e green 8%

### POP Snap backdrop

`POP_Snap` · atlas · 1 parts · largest 1000×2036 · sheet `sheets/POP_Snap.webp`

- **Role:** The background image behind the Snap banner (scene path POP_Feature/Pivot/Banner/Snap/Bg/Sprite).
- **Subject:** A tall portrait backdrop: blurred green and teal with an orange patch on the right and a white glow in the middle, above the gold coin and star pile.
- **Style:** A blurred gradient above the sharply drawn coin pile; no lettering and no stars in the sky.
- **Rendering:** A single opaque painted image with a soft-focus upper part and a 3D-render look coin pile.
- **Colour:** Teal-green #0b9a6c, green #69aa5c, bright cyan-green #1de5c2 and #54e8b2, pale green #d7f5d6, with orange #e8b750 and #c5692a in the patch and the coins.
- **Lighting:** A white glow in the middle where the banner sits; the coins are lit from above with a few white glints.
- **Ambience:** Fresh, with a warm accent.
- **Materials:** Gold coins and stars; the rest is light and haze.
- **Variants:** The green member of the three backdrops; it is larger than the other two (1000x2036 against 689x1725).
- **Motion:** None; a still image.
- **Construction:** One image of 1000x2036 in its own atlas.
- **Notes:** The coins here are drawn smaller and denser than in the other two backdrops, which follows from the larger image size.
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 68% · saturation 62% · contrast 52% · warm 42% / cool 40% · brighter towards: bottom-right (1)
- **Palette (measured):** #e8b750 orange 26%, #0b9a6c cyan 17%, #69aa5c green 12%, #d7f5d6 light green 7%, #c5692a orange 6%, #1de5c2 cyan 6%

### Free spins intro banner

`zvhp_banner_intro` · skeleton · 223 parts · largest 509×1151 · sheet `sheets/zvhp_banner_intro.webp`

- **Role:** The start banner of the free spins (scene path FS_Banner/StartBanner/content/Spine).
- **Subject:** Zeus and Hades side by side, Zeus on the left with a lightning bolt in his raised hand and Hades on the right with a flame in one hand and a flaming trident in the other, above a cream scroll with gold rods and tassels, a blue gem-cut meter box below it inside a ring of sparks, on a backdrop split between blue storm clouds and red-purple clouds.
- **Style:** Stylised 3D-cartoon characters with large heads; painted, soft-edged clouds; an ornate scroll and a bevelled octagonal box. No lettering is in the art itself (inference: the text is set by the game's fonts).
- **Rendering:** Characters painted to a smooth 3D-render look with clean edges; clouds and effects are painterly and softer. Rigged parts for the characters, hand-drawn frame sequences for fire, lightning and clouds.
- **Colour:** Split in two: Zeus side in blue #434fc2 / #6c94f2 and purple #4d3c86 with cyan accents #8ee9dd, Hades side in dark red #641836 with orange fire and yellow #feed39; white #f7f8f6 on the scroll and hair.
- **Lighting:** Fire on Hades's head and staff and lightning beside Zeus act as light sources; an orange ray burst, a cyan ring flare and gold spark rings glow behind the meter box.
- **Ambience:** A face-off before a duel, charged but still cartoon in tone.
- **Materials:** Storm clouds, fire, lightning, parchment, gold trim, blue enamel or gem for the box, skin, cloth, and a skull belt on Hades.
- **Variants:** One banner holding both characters, each on a colour side; no separate Zeus or Hades version.
- **Motion:** Animations zvhp_banner_intro_in 1.0 s, _loop 2.0 s and _out 1.07 s; frame sequences cloude 6 and 4, baaz 8 (lightning bolts), star_sparkel 18, eye_lid 6, fx 3 and 3, weapon_fire 15, fox_shine 6, hand_fire 6 and head_fire 15. In: a cyan ring of concentric circles expands from the centre while the backdrop, characters, scroll and meter box fade in behind it, then the ring is gone. Loop: the layout holds, with the fires, the lightning beside Zeus and the spark ring around the box changing from frame to frame. Out: the cyan ring returns over the meter box and expands as the banner fades, and the last frame is empty.
- **Construction:** 223 images, 117 bones, 219 slots, with 129 mesh, 144 region and 14 linked-mesh attachments, and both additive and multiply blend slots; the characters reuse the same kind of parts as the big-win rigs (face, body, hair pieces, belt, staff). 106 smaller parts are not shown on the sheet.
- **Notes:** This is the only unit in the set that lists a multiply blend, used for shadow layers (inference from parts named dark1 and the belt shadows). The cyan ring (bigin_fx) is used only for the entrance and the exit; the gold spark ring stays around the box in the loop.
- **Skeleton (from the file):** Spine 3.7.91 · 117 bones · 219 slots · 129 mesh, 144 region, 14 linkedmesh · animations: zvhp_banner_intro_in (1.0 s), zvhp_banner_intro_loop (2.0 s), zvhp_banner_intro_out (1.07 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 44% · saturation 65% · contrast 37% · warm 48% / cool 45% · brighter towards: bottom-right (9), bottom-left (8), top (6)
- **Palette (measured):** #641836 dark red 21%, #434fc2 blue 9%, #4d3c86 blue 9%, #6c94f2 blue 7%, #f7f8f6 light green 6%, #feed39 gold 5%

### Free spins outro banner

`zvhp_banner_outro` · skeleton · 244 parts · largest 574×1464 · sheet `sheets/zvhp_banner_outro.webp`

- **Role:** The end banner of the free spins (scene path FS_Banner/EndBanner/content/Spine); inference from part names 'you_have_won' and 'cradits': it shows the total won.
- **Subject:** Zeus and Hades side by side with folded arms behind a heap of gold coins on top of a cream scroll with gold ends and a red gem, a dark red meter bar with a gold frame below, inside a swirling ring of fire, on a backdrop of blue and red clouds.
- **Style:** The same 3D-cartoon characters, here with arms folded; painted clouds; an ornate scroll and a pill-shaped bar. No lettering in the art itself.
- **Rendering:** Characters and coins painted to a smooth 3D-render look; clouds painterly; fire ring and bursts soft and additive. Rigged parts with frame sequences for fire, coins and sparkles.
- **Colour:** Warmer than the intro: dark red #5c071c (25%) and reds #c64a38 / #98271e, blue-violet #504997 and magenta #8c3258 in the clouds, gold #fdf67f / #fee229 in the coins and glow.
- **Lighting:** Yellow glows behind each character, a fiery ring and a gold spark ring around the banner, an orange ray burst, and white four-point sparkles on the coins.
- **Ambience:** Triumphant and friendly; the two rivals share the winnings.
- **Materials:** Gold coins in a heap and in flight with motion streaks, parchment scroll, red enamel bar, fire, storm clouds, gold armour, cloth.
- **Variants:** One banner with both characters; the brief lists no tiers.
- **Motion:** Animations zvhp_banner_outro_in 1.0 s, _loop 2.0 s and _out 1.1 s; frame sequences cloude 7 and 6, star_sparkel 18, con_coin 18 with con_coin_shadow 7, coin 10, h_beard 3, h_left_hand 3, z_right_hand 3, scroll_gem 4, sperkal_o 7, fx 6, head_fire 15 and meter_frame 4. In: gold concentric rings set with four-point sparks expand from the centre while the banner fades in behind them, and pass out of the frame. Loop: the layout holds inside the ring of fire, with coins falling below it and the head fire and sparkles changing. Out: the gold rings return and expand as the banner fades, and only the fading rings are left.
- **Construction:** 244 images, 124 bones, 338 slots, 234 region and 118 mesh attachments, with additive slots; the background is one 574x1464 image, the coin heap is a frame sequence, and the flying coins are separate parts with painted motion blur. 112 smaller parts are not shown.
- **Notes:** It shares the head-fire sequence (15 frames), the scroll and the cloud drawing with the intro banner; the meter here is red where the intro's is blue.
- **Skeleton (from the file):** Spine 3.7.91 · 124 bones · 338 slots · 234 region, 118 mesh · animations: zvhp_banner_outro_in (1.0 s), zvhp_banner_outro_loop (2.0 s), zvhp_banner_outro_out (1.1 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 37% · saturation 68% · contrast 37% · warm 67% / cool 28% · brighter towards: top (12), bottom-left (9), bottom-right (8)
- **Palette (measured):** #5c071c dark red 25%, #504997 blue 20%, #8c3258 magenta 14%, #c64a38 red 7%, #fdf67f gold 6%, #98271e red 4%

### Big win title plates and value window

`atlas_BigWin` · atlas · 7 parts · largest 764×245 · sheet `sheets/atlas_BigWin.webp`

- **Role:** The title plates and the amount window of the big-win screen, used on desktop and mobile (scene path BigWin_Custom/.../TitleHolder/TitleJackpot).
- **Subject:** Gold title plates reading 'NICE!', 'EPIC!', 'SENSATIONAL!' and 'JACKPOT!!!', and a dark rounded window with a gold rim for the amount.
- **Style:** Angular, chiselled capital letters cut into rounded gold plates, with a thin dark outline and a lighter bevel; the look of stamped metal signage.
- **Rendering:** Flat-shaded vector-like art with hard edges and simple two- or three-tone bevels; much plainer than the character rigs. Still images.
- **Colour:** Monochrome gold on dark: brown-gold #8c6a1d (35%), pale gold #e9df95, mid gold #c4a440, with near-black #070915 and dark blue #253543 in the window.
- **Lighting:** No glow; a simple bevel suggests light from above, and the window has a faint horizontal sheen.
- **Ambience:** Formal and restrained, a plain label beside the animated characters.
- **Materials:** Brushed or stamped gold plate; dark glass or enamel for the window.
- **Variants:** Levels as title plates: the sheet shows level_1 'NICE!', level_3 'EPIC!', level_5 'SENSATIONAL!' and a separate 'JACKPOT!!!'; the brief counts a 'level' sequence of 5, so two more levels exist that the sheet does not show.
- **Motion:** No animation data; 'level x5' is a set of five alternative plates, not an animation (inference).
- **Construction:** A plain sprite atlas of 7 images (largest: value_window 764x245); the plates differ in width with the word.
- **Notes:** This lettering is not the lettering in the Zeus and Hades big-win rigs, which have their own 3D gold words; inference: these plates serve the generic or jackpot title path.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 49% · saturation 64% · contrast 62% · warm 88% / cool 12% · brighter towards: right (1)
- **Palette (measured):** #8c6a1d brown 35%, #e9df95 gold 21%, #070915 black 17%, #c4a440 gold 16%, #4c3615 brown 4%, #253543 dark blue 2%

### Big win, Zeus tiers (Mega and Sensational)

`zvhp_zeus_bigwin` · skeleton · 218 parts · largest 811×1346 · sheet `sheets/zvhp_zeus_bigwin.webp`

- **Role:** The big-win celebration led by Zeus for the Mega and Sensational tiers (scene path BigWin_Custom/Desktop/TextHolder/Pivot/TitleHolder, used for background, character and text holders).
- **Subject:** Zeus in front of a small blue and gold temple, over a gold word and a purple amount frame with a silver rim resting on a white cloud, in a tall burst of cyan rays with falling gold coins. In the Sensational tier he raises a fist holding a lightning bolt; in the Mega tier, as far as the small frames show, both arms are flexed at his sides.
- **Style:** 3D-cartoon character with a large head, white beard and stocky body; condensed, angular gold capitals with a hard bevel for 'MEGA!' and 'SENSATIONAL!'; rounded cartoon clouds.
- **Rendering:** Painted to a smooth 3D-render look with clean edges and soft shading on skin and cloth; lightning is hand-drawn in frames; glows are soft. The body is rigged from many mesh parts.
- **Colour:** Cool and bright: cyan #39e9f3 (18%) and #9ffafc, blue #3992f8, near-white #ecfbfb, with lilac cloth #cbbfdb, brown #7c3610 in the lettering's depth, skin tones and gold lettering; purple in the amount frame.
- **Lighting:** The cyan ray burst behind and the lightning are the light sources; the brief measures light from the top-left, left and top. Text has a separate dark teal shadow copy and a depth layer.
- **Ambience:** Heroic and electric.
- **Materials:** Lightning, cloud, marble and gold temple, white hair and beard, skin, cloth with gold Greek key trim, gold belt with a red gem, polished gold lettering, silver frame.
- **Variants:** Two tiers in one rig, Mega and Sensational, each with its own word, body, cloth and effect parts (mega_*, sensational_*). Zeus version; the Hades rig covers Nice and Superb.
- **Motion:** Animations zvhp_zeus_bigwin_mega_in 1.0 s, mega_loop 2.0 s, mega_outro 0.37 s, sensational_in 1.0 s, sensational_loop 2.0 s and sensational_out 0.67 s; frame sequences include electric_effect_new 8, in_thunder_effect 4 and 6, thuder_b 6 and 4, beard 3 and 4, hair_p 4, mega_hair 3, cloth 3, mega_finger 11, mega_hand 3, mega_gold 3 and sensational_coin_1_glow 3. Each entrance opens with lightning across the frame, through which the temple, Zeus, the word and the amount frame appear and settle in the cyan rays; the loops hold that layout while coins fly outwards and fall and small bolts flicker; each exit is a white-cyan lightning flash that fills the frame and fades to a few thin bolts.
- **Construction:** 218 images, 205 bones, 295 slots, 207 mesh and 134 region attachments, with additive slots; one skeleton is instanced three times, for the background, the character and the number. The words are built as a gold face, a depth piece and a shadow. 121 smaller parts are not shown.
- **Notes:** The background ray image is the largest part (811x1346) and sets the whole colour of the screen. The word sits in front of the temple and below the character, clear of both.
- **Skeleton (from the file):** Spine 3.7.91 · 205 bones · 295 slots · 207 mesh, 134 region · animations: zvhp_zeus_bigwin_mega_in (1.0 s), zvhp_zeus_bigwin_mega_loop (2.0 s), zvhp_zeus_bigwin_mega_outro (0.37 s), zvhp_zeus_bigwin_sensational_in (1.0 s), zvhp_zeus_bigwin_sensational_loop (2.0 s), zvhp_zeus_bigwin_sensational_out (0.67 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 66% · saturation 56% · contrast 42% · warm 30% / cool 68% · brighter towards: top-left (17), left (15), top (13)
- **Palette (measured):** #39e9f3 cyan 18%, #ecfbfb light cyan 15%, #3992f8 blue 15%, #7c3610 brown 6%, #cbbfdb light purple 6%, #9ffafc light cyan 4%

### Big win, Hades tiers (Nice and Superb)

`zvhp_hades_bigwin_superb_nice` · skeleton · 245 parts · largest 676×1117 · sheet `sheets/zvhp_hades_bigwin_superb_nice.webp`

- **Role:** The big-win celebration led by Hades for the Nice and Superb tiers (scene path BigWin_Custom/Mobile/TextHolder/Pivot/TitleHolder, character and number holders for Nice and Superb).
- **Subject:** Hades, red-skinned with a flaming head, spiked crown and wolf-head shoulder guard, laughing in front of an orange-red temple, over a gold word ('NICE!' or 'SUPERB!'), a purple amount frame with a silver rim on burning rocks, and a red-orange glow of rays with falling coins. In the Superb tier he raises a flaming trident and holds a flame in the other hand; in the Nice tier, as far as the small frames show, he holds a flame out at each side.
- **Style:** 3D-cartoon character with a large head and heavy muscles; blocky gold capitals with a thick bevel, set on an arc; jagged flame shapes.
- **Rendering:** Painted to a smooth 3D-render look with clean edges; fire is hand-drawn in frames with flat cartoon shapes and a glow; the body is rigged from mesh parts.
- **Colour:** Hot and saturated: red #c23c1c (21%), #f7481f and #fd0b01, dark red #6a1912, orange #f79e2b, yellow #feeb72 / #fee82f, with near-black #1d0e1f and purple in the cape and amount frame.
- **Lighting:** Fire lights everything: a red-orange ray burst behind, a ring of flame at entry and exit, and glowing lava under the amount frame; the brief measures light from below, the top-left and the top.
- **Ambience:** Fierce and gleeful, the underworld counterpart of the Zeus screen.
- **Materials:** Fire, lava and cracked burning stone, red skin, a purple cape with gold edge, dark leather belts, a skull belt, gold armour and trident, polished gold lettering, silver frame.
- **Variants:** Two tiers in one rig, Nice and Superb, each with its own body, cloth and word parts (nice_*, superb_*). Hades version; the Zeus rig covers Mega and Sensational.
- **Motion:** Animations zvhp_hades_bigwin_nice_in, nice_loop, nice_out, superb_in, superb_loop and superb_out, 1.0 s each; frame sequences fire_hand 9, h_ryt_hand_fngr 3, nice_eye_ball 4, nice_eyeblink 6, nice_finger 9, nice_hand 5, nice_skull 5, skull 4, superb_eye_blink 6, superb_stone 10, weapon_fire 8 and head_fire 15. Each entrance starts with a red glow and the burning rocks, then a burst of flame that opens outwards as a ragged ring while Hades, the word and the amount frame appear and settle; the loops hold the layout with the fires and rays changing and a few coins falling; each exit is a yellow star-shaped flash at the centre that grows into a ball of flame over the whole group and leaves a fading ring of embers.
- **Construction:** 245 images, 175 bones, 298 slots, 137 mesh and 321 region attachments, with additive slots; the amount frame is split into rim, shadow and purple fill (superb_stone_full_frame parts), and the words have face, depth and shadow pieces. 137 smaller parts are not shown.
- **Notes:** The layout mirrors the Zeus rig part for part (bg_rays, bg_pillar, bg_pillar_glow, character, word, amount frame), with cyan and lightning exchanged for red and fire; the head-fire sequence is shared with the free spins banners.
- **Skeleton (from the file):** Spine 3.7.91 · 175 bones · 298 slots · 137 mesh, 321 region · animations: zvhp_hades_bigwin_nice_in (1.0 s), zvhp_hades_bigwin_nice_loop (1.0 s), zvhp_hades_bigwin_nice_out (1.0 s), zvhp_hades_bigwin_superb_in (1.0 s), zvhp_hades_bigwin_superb_loop (1.0 s), zvhp_hades_bigwin_superb_out (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 45% · saturation 76% · contrast 49% · warm 92% / cool 4% · brighter towards: bottom (14), top-left (13), top (12)
- **Palette (measured):** #c23c1c red 21%, #6a1912 dark red 19%, #f79e2b orange 15%, #f7481f red 10%, #feeb72 gold 10%, #fee82f gold 4%


## Effects

Frame sequences, glows, particles and transitions.

### Free spins left counter burst

`zeha_free_spin_left_fx` · skeleton · 9 parts · largest 101×101 · sheet `sheets/zeha_free_spin_left_fx.webp`

- **Role:** A small burst played on the 'free spins left' counter of the free-game background (scene path Background/BkgPortrait/Free/FSLeft/FreeSpinsLeft/effect); inference from the path: it fires when the remaining-spins number changes.
- **Subject:** A round fireball flash that breaks into a scalloped, flower-like ring of flame with small white stars thrown outwards, then fades to faint smoke.
- **Style:** Cartoon explosion with rounded, puffy lobes and five-point stars; no lettering.
- **Rendering:** Hand-drawn frame animation with a soft outer glow on the first frames and cleaner cartoon edges on the ring; low detail, made to read at about 100 px.
- **Colour:** Warm only: orange #ff9945 dominates, with a pink-red rim #ff407c, a near-white core #fffef5 and yellow #fff26f.
- **Lighting:** Self-lit; the first frame is an almost white disc with an orange halo and the brightness drops frame by frame until the last frame is nearly invisible.
- **Ambience:** A quick, cheerful pop that draws the eye to the counter without weight or menace.
- **Materials:** Fire and sparks treated as flat cartoon shapes with a glow, plus small solid white stars.
- **Variants:** One version only; no Zeus, Hades or base-game alternative is in the unit.
- **Motion:** One animation, zeha_free_spin_left_fx, 0.67 s, driven by the frame sequence red/free_spin_left_fx (7 frames in the brief): a white-yellow disc with an orange halo, then a scalloped orange burst with white stars around it, then the burst opens into a hollow ring with a pink haze inside while the stars drift outwards and shrink. The ring breaks into separate flame wisps and the last frame is a faint pink trace.
- **Construction:** Spine skeleton with 2 bones and 2 slots holding 18 region attachments from 9 images (largest 101x101), with an additive blend slot; the same frames are used in both slots (inference: one normal and one additive copy for the glow).
- **Notes:** The whole effect is seven small frames; the look comes from the white-to-orange-to-pink falloff and the additive copy, not from detail.
- **Skeleton (from the file):** Spine 3.7.91 · 2 bones · 2 slots · 18 region · animations: zeha_free_spin_left_fx (0.67 s)
- **Measured:** bright, saturated, warm, medium contrast, glow or soft effect, strong highlights · brightness 70% · saturation 60% · contrast 39% · warm 98% / cool 0%
- **Palette (measured):** #ff9945 orange 47%, #ff407c red 14%, #fffef5 light gold 13%, #fff26f gold 12%, #ffb3a9 light red 8%, #ff5924 red 4%

### Expanding wild reel overlay

`zeha_olfx_ex_wild` · skeleton · 14 parts · largest 225×703 · sheet `sheets/zeha_olfx_ex_wild.webp`

- **Role:** Overlay effect on a reel when the expanding feature runs (scene path Reels/ResizeEffect/Expanding_feature/reel0 to reel2); inference from the name 'ex_wild': it covers the reel as a wild expands.
- **Subject:** A full-reel-height column: a cyan lightning bolt running top to bottom with a small flame at its foot, replaced by red-orange fire with a white-hot core that fills the whole column, then by scattered red-rimmed embers.
- **Style:** Stylised energy effect: lightning drawn as thick, angular ribbons with a soft glow, fire as blocky flame shapes with triangular sparks; no lettering.
- **Rendering:** Hand-drawn frame animation with soft, glowing edges; flat colour fills with a lighter core, little internal detail.
- **Colour:** Two opposed hues: red #f74718 (33%) with orange #fea12b, gold #ffee37 and a near-white core #fffff5 (23%) against pure cyan #08ffff (16%).
- **Lighting:** Entirely emissive; the cyan bolt and the fire cores are the brightest areas and the red fades to transparent at its edges.
- **Ambience:** A clash of the two gods' elements, lightning against fire, tense and energetic.
- **Materials:** Lightning and fire, both treated as glowing flat shapes with no surface texture.
- **Variants:** Both elements are in one effect, cyan for Zeus and red for Hades (inference from the game's colour coding); no separate base and free-game versions.
- **Motion:** One animation, zeha_olfx_ex_wild, 0.83 s, from two frame sequences, cyan/olfx_ex_wild (3 frames) and red/olfx_ex_wild (10 frames). The cyan bolt fills the column first with a small flame at its base; fire then takes over the column, its white core rising from the bottom until it covers more than half the height; the fire breaks into red-rimmed white embers on a red glow, which thin out and fade.
- **Construction:** Spine skeleton with 1 bone and 2 slots holding 28 region attachments from 14 images, one slot additive; every frame is a tall column (225x703 for the lightning, 196x611 for the fire and embers) sized to one reel, and the instance is repeated on three reels.
- **Notes:** The lightning column is only three frames, so its flicker is fast and coarse; the fire carries the longer motion. Keep the two colours unmixed so each reads as its own element.
- **Skeleton (from the file):** Spine 3.7.91 · 1 bones · 2 slots · 28 region · animations: zeha_olfx_ex_wild (0.83 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 68% · saturation 66% · contrast 60% · warm 81% / cool 19% · brighter towards: bottom-right (5), bottom (3), right (2)
- **Palette (measured):** #f74718 red 33%, #fffff5 light gold 23%, #08ffff cyan 16%, #fea12b orange 11%, #ffee37 gold 4%, #b72f17 red 4%

### Reel spin-down highlight

`zeha_reel_highligher_fx` · skeleton · 18 parts · largest 201×639 · sheet `sheets/zeha_reel_highligher_fx.webp`

- **Role:** A glow on a reel of the base reel set (scene path ReelsBkg/Pivot/BaseGame/BaseReel/GlowFx_base/Reel0 to Reel2, node Spinereel_glow); inference from the animation names: it plays as a reel spins down and stops.
- **Subject:** Soft vertical bars and rounded blocks of light with no drawn object: a tall cyan-white capsule, blue fades, and pink blocks with a peach-white centre.
- **Style:** Abstract gradient shapes with rounded ends; no lettering and no line work.
- **Rendering:** Soft airbrushed gradients with blurred edges, built as a frame sequence; no detail beyond the falloff.
- **Colour:** Base-game version in light cyan #a7eaff and blue #34b5ff / #4d84ff; free-game version in pink-red #ff3777 and magenta #ff6dbd with a pale peach core #ffb8b5.
- **Lighting:** Pure light: a near-white core that falls off to a saturated rim and then to transparent.
- **Ambience:** A clean flash of attention on one reel, cool in the base game and hot in the free game.
- **Materials:** Light only.
- **Variants:** Two colour versions in one skeleton: reel_spin_down_basegame (cyan and blue) and reel_spin_down_freegame (pink and peach).
- **Motion:** Two animations of 0.53 s each, reel_spin_down_basegame and reel_spin_down_freegame, from frame sequences cyan/reel_spin_down_fx and red/reel_spin_down_freegame_fx (9 frames each in the brief). Base game: a blue arc appears near the top, a pale capsule with a rounded bright lower edge grows downwards until it fills the reel, then shrinks to a short bar at the bottom and fades. Free game: the glow starts low, a peach block with a rounded top rises through pink to the top of the reel, and ends as a short pink bar at the top.
- **Construction:** Spine skeleton with 1 bone and 4 slots holding 36 region attachments from 18 images (largest 201x639), with additive blending; all frames are upright columns cropped to their lit area, so their heights differ.
- **Notes:** The base and free versions use the same kind of shapes recoloured, and the free-game version has a warm peach core instead of white; in the frames the base-game light travels down the reel and the free-game light travels up.
- **Skeleton (from the file):** Spine 3.7.91 · 1 bones · 4 slots · 36 region · animations: reel_spin_down_basegame (0.53 s), reel_spin_down_freegame (0.53 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast · brightness 65% · saturation 58% · contrast 39% · warm 43% / cool 50% · brighter towards: top (4)
- **Palette (measured):** #ff3777 red 20%, #34b5ff blue 19%, #a7eaff light cyan 19%, #ffb8b5 light red 18%, #ff6dbd magenta 8%, #4d84ff blue 5%

### Reel anticipation effect

`zeha_anticipation` · skeleton · 15 parts · largest 156×393 · sheet `sheets/zeha_anticipation.webp`

- **Role:** Anticipation effect on the third reel (scene path ReelsManager/Reel2/ReelFx/content/Spine_anticipation); inference: it plays while that reel keeps spinning when a feature could still land.
- **Subject:** A reel-height curtain of blue light with fine vertical streaks and small bright flecks, like rain or falling sparks inside a glowing column, with a pale mist that gathers in it.
- **Style:** Abstract streaked light with soft top edges and a hard bottom edge; no lettering.
- **Rendering:** Frame animation of soft, blurred streaks, close to a rendered particle effect in look; soft edges (measured soft edge 0.633).
- **Colour:** Cool only: blue #71ccfb (56%), light cyan #a8f2fe for the streak highlights and a deeper blue #5090e8.
- **Lighting:** Emissive, brightest at the bottom and in the thin streaks, fading upwards into transparency.
- **Ambience:** Suspense and expectation, cool and electric.
- **Materials:** Light and fine sparks, treated as blurred vertical lines.
- **Variants:** One version, blue; no free-game or Hades colour version is in the unit.
- **Motion:** One animation, zeha_anticipation, 0.93 s, from the frame sequence cyan/anticipation (15 frames). The streaks stay vertical while the flecks shift from frame to frame; a pale cloud of mist appears in the middle of the column, spreads, and by the last frame whitens most of the upper half.
- **Construction:** Spine skeleton with 1 bone and 1 slot holding 15 region attachments, no additive blend listed; each frame is one whole column of about 154x393 that covers the reel.
- **Notes:** This is the only effect in the set without an additive slot, so its blue is the colour seen on screen; keep the streaks thin and vertical.
- **Skeleton (from the file):** Spine 3.7.91 · 1 bones · 1 slots · 15 region · animations: zeha_anticipation (0.93 s)
- **Measured:** bright, saturated, cool, medium contrast, glow or soft effect, strong highlights · brightness 77% · saturation 49% · contrast 32% · warm 0% / cool 100% · brighter towards: bottom (11)
- **Palette (measured):** #71ccfb blue 56%, #a8f2fe light cyan 33%, #5090e8 blue 11%

### Symbol landing flare

`zeha_landing_fx` · skeleton · 2 parts · largest 393×680 · sheet `sheets/zeha_landing_fx.webp`

- **Role:** Landing effect behind symbols S01 and S10 (scene path SymbolsManager/Symbols/S01 and S10/Landing_effect); inference: it plays when one of those symbols lands on the reels.
- **Subject:** A tall plume of wispy flame rising from a point, one in cyan-blue with thin orange-yellow vertical streaks at its sides and one in yellow with an orange core.
- **Style:** Semi-realistic fire wisps with thin vertical strands, softer and less cartoon than the other effects; no lettering.
- **Rendering:** A single soft, translucent image per colour, with very soft edges (measured soft edge 0.954), animated by the rig and not by frames.
- **Colour:** Yellow version: orange #f3aa3c with gold #fddb27 and #fcf057. Blue version: cyan #59ecfb and blue #23a1f6 with the same orange and gold at its edges.
- **Lighting:** Self-lit and translucent; brightest in the strands near the base, fading to nothing at the top.
- **Ambience:** A brief flare of power under a symbol that matters.
- **Materials:** Fire or energy, shown as translucent strands.
- **Variants:** Two colour versions, zeha_landing_fx_blue and zeha_landing_fx_yellow; inference: blue for the Zeus-side symbol and yellow for the other.
- **Motion:** Two animations of 0.5 s each, zeha_landing_fx_blue and zeha_landing_fx_yellow; no frame sequence. In the frames the plume stands at full strength with almost no change of shape for most of the time and then fades out as a whole.
- **Construction:** Spine skeleton with 3 bones and 4 slots holding 4 region attachments from 2 images (blue_land 393x680, yellow_land 382x680), with additive blending; inference: each image is used twice, once normal and once additive.
- **Notes:** The cheapest effect in the set: two stills and a rig. The blue plume keeps warm edges, so it does not read as pure cyan.
- **Skeleton (from the file):** Spine 3.7.91 · 3 bones · 4 slots · 4 region · animations: zeha_landing_fx_blue (0.5 s), zeha_landing_fx_yellow (0.5 s)
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 75% · saturation 66% · contrast 31% · warm 68% / cool 31%
- **Palette (measured):** #f3aa3c orange 35%, #fddb27 gold 15%, #59ecfb cyan 12%, #23a1f6 blue 8%, #fcf057 gold 7%, #f1c080 orange 5%

### Win frame

`zeha_winframe` · skeleton · 11 parts · largest 229×168 · sheet `sheets/zeha_winframe.webp`

- **Role:** A glowing frame for a winning position; the brief lists it under Character_Dragon overlay and idle nodes, so where it shows in play is not certain. Inference from the name: it outlines winning symbols.
- **Subject:** A thin rectangular outline of golden light with small sparks along its edges.
- **Style:** A plain geometric outline with a slightly uneven, sparkling edge; no lettering.
- **Rendering:** Frame animation of a glowing line with very soft edges (measured soft edge 0.984) and tiny spark dots; minimal detail.
- **Colour:** Warm only: orange #ff8a03 (68%) for the glow, gold #fff66b and #ffd32c for the line.
- **Lighting:** Emissive; a bright yellow core line with an orange halo, and sparks that flicker along it.
- **Ambience:** A clear, warm marker of a win.
- **Materials:** Light and sparks, read as molten gold or fire.
- **Variants:** One version only.
- **Motion:** One animation, zeha_winframe, 0.67 s, from the frame sequence yellow/winframe (11 frames); the frame stays in place at full brightness while small kinks travel along the line and the sparks outside its edges change position from frame to frame.
- **Construction:** Spine skeleton with 1 bone and 2 slots holding 22 region attachments from 11 images of about 227x167, one slot additive (inference: the frames are doubled, normal plus additive).
- **Notes:** The frame is wider than tall at about 4:3, matching a symbol cell; the centre is empty so the symbol stays fully visible.
- **Skeleton (from the file):** Spine 3.7.91 · 1 bones · 2 slots · 22 region · animations: zeha_winframe (0.67 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 69% · saturation 88% · contrast 30% · warm 100% / cool 0%
- **Palette (measured):** #ff8a03 orange 68%, #fff66b gold 18%, #ffd32c gold 12%

### Scene transition

`zvhp_transition` · skeleton · 36 parts · largest 250×625 · sheet `sheets/zvhp_transition.webp`

- **Role:** Full-screen transition used by the POP feature and by the game's transition node (scene paths POP_Feature/Pivot/Spine/Transition_Spine_jpeg and Tranisation/content/Spine/Spine_jpeg); inference: it covers the change between base game and feature.
- **Subject:** A portrait frame sequence: yellow-orange fire and embers over black, Hades in profile with flaming hair and a gold wolf-head shoulder guard gripping a gold staff above lava, then Zeus standing with a raised lightning bolt above cracked glowing ground under a storm sky, and last a blue sky with lightning that breaks apart from the centre.
- **Style:** Fully painted, cinematic frames in the game's stylised 3D-cartoon character style; no lettering.
- **Rendering:** Pre-rendered full frames, hard-edged rectangles (measured soft edge 0.016), with separate greyscale alpha frames; the frames look like a rendered or composited video, not rigged parts.
- **Colour:** Dark ground, black #040304 and dark blue #35334d, with orange fire #f9a50b / #ee5b0d and blue lightning and sky #49a8eb / #265497.
- **Lighting:** High contrast: fire lights Hades from below and behind, the lightning bolt lights Zeus against a dark sky, and the ground cracks glow orange under him.
- **Ambience:** Dramatic and stormy, a moment of confrontation before the feature.
- **Materials:** Fire, embers, smoke, lightning, cracked lava ground and the two painted figures with gold armour and trim.
- **Variants:** One sequence that shows both gods in turn, Hades first and Zeus second.
- **Motion:** One animation, zvhp_transition, 1.5 s, from the frame sequences transition (25 frames, 250x625) and alpha (11 frames, 172x430). Fire and embers fill the screen, Hades appears in close-up profile, the picture changes to Zeus full-figure with his bolt raised and then moves closer on him, and the last frames show blue sky and lightning with the centre breaking into fragments and opening to transparency.
- **Construction:** Spine skeleton with 1 bone and 1 slot holding 25 region attachments from 36 images, additive blend listed; the node names end in '_jpeg' and the alpha frames are stored apart, so inference: colour is kept as opaque JPEG frames and transparency comes from the separate alpha frames.
- **Notes:** The frames are small (250x625) and scaled up to full screen, which is acceptable because the transition is fast and dark; this is the only effect built as video-like full frames.
- **Skeleton (from the file):** Spine 3.7.91 · 1 bones · 1 slots · 25 region · animations: zvhp_transition (1.5 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 40% · saturation 59% · contrast 57% · warm 44% / cool 44% · brighter towards: top-left (7), top-right (7), bottom-left (3)
- **Palette (measured):** #040304 black 17%, #35334d dark blue 16%, #f9a50b orange 14%, #49a8eb blue 9%, #ee5b0d orange 6%, #265497 blue 5%

### Loose sprites: number fonts, coins and red envelope

`no-atlas` · atlas · 8 parts · largest 1000×1000 · sheet `sheets/no-atlas.webp`

- **Role:** Loose images that sit in no atlas: three bitmap number fonts with currency signs, two gold coins, a gold ingot, a red envelope with coins and a small white sparkle; the brief gives no scene path, so where each is used is inference (win amounts, coin showers and a promotional gift).
- **Subject:** Glossy gold digits with currency symbols ($, euro, pound, yen, won, bitcoin and others) in two sizes, a yellow digit set with a red outline including 'X' and '+', a gold coin with a dollar sign, a gold coin with a crown, a boat-shaped gold ingot, a red silk envelope printed 'PLAY' with a crown and Chinese text spilling coins, and a four-point sparkle.
- **Style:** Rounded, heavy cartoon numerals with bevelled faces; the red-outlined set is flatter with a thick dark red stroke. The coins and ingot are glossy 3D-style icons.
- **Rendering:** Clean, hard-edged sprites with smooth gradients and specular highlights, a 3D render look for the coins, ingot and envelope; static images, no animation data.
- **Colour:** Gold and red: light gold #fef38f, gold #fee311, orange-gold #fdd051 / #fba814, red #b41718 and dark red #5c0f11.
- **Lighting:** Top light on the digits and coins with bright specular spots and a darker lower edge; the sparkle is a pure white cross flare.
- **Ambience:** Wealth and luck, with an East Asian gift motif in the envelope and ingot.
- **Materials:** Polished gold for digits, coins and ingot; red satin with gold trim for the envelope.
- **Variants:** Three number fonts (large gold 1000x1000, smaller gold 630x630, yellow with red outline 353x353) and two coin faces (dollar, crown).
- **Motion:** None listed; these are still sprites.
- **Construction:** 8 separate images, the fonts packed as glyph sheets with shuffled glyph order, the coins at 128x128 and the sparkle at 64x64; file names are hashes, so these come from the platform's shared assets (inference).
- **Notes:** The envelope, ingot and crown coin carry the operator's or provider's branding, not the game's Greek theme; treat them as shared platform art, not part of this game's style.
- **Measured:** bright, vivid, warm, high contrast, strong highlights · brightness 63% · saturation 70% · contrast 75% · warm 100% / cool 0% · brighter towards: top (3), bottom (1)
- **Palette (measured):** #fef38f light gold 29%, #b41718 red 20%, #fee311 gold 11%, #fdd051 orange 11%, #fba814 orange 8%, #5c0f11 dark red 5%


## Game interface

Buttons, counters and panels drawn for this game.

### Spin button base

`button` · atlas · 1 parts · largest 159×159 · sheet `sheets/button.webp`

- **Role:** Base disc of the spin button (brief: Spin_button/L1_Sprite_Base); the main screenshot shows the round spin control below the board in a darker teal with white arrows on top. Both modes (inference).
- **Subject:** A round teal button face with a gold rim.
- **Style:** Simple glossy casual-game UI disc; perfect circle, thin bevelled ring.
- **Rendering:** Smooth gradient face with a soft inner shadow, thin dark inner line and a bright gold bevel; crisp edge.
- **Colour:** Teal #08888e face with a lighter cyan lip #08b6b9 and dark green inner line #054c2f; gold rim #fcb941 with highlight #fdfc4e and brown shade #b46905.
- **Lighting:** Soft top-down shading on the face; rim highlighted at the top and darker below.
- **Ambience:** Clean, neutral control that does not compete with the theme art.
- **Materials:** Enamel or glass face, polished gold ring.
- **Variants:** One state at 159x159; icons and other states are separate layers not in this unit.
- **Construction:** Single sprite used as layer 1 of a stacked button (name L1_Sprite_Base); arrows and effects sit on other layers.
- **Notes:** Gold rim ties the control to the gold dividers and bars of the reel board.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 47% · saturation 92% · contrast 43% · warm 16% / cool 83%
- **Palette (measured):** #08888e dark cyan 77%, #fcb941 orange 11%, #054c2f dark green 4%, #08b6b9 cyan 3%, #b46905 brown 2%, #fdfc4e gold 2%

### Free spins counter panel

`free_spin_left` · atlas · 1 parts · largest 330×228 · sheet `sheets/free_spin_left.webp`

- **Role:** Panel behind the remaining free spins counter (brief: BkgPortrait/Free/FSLeft/BG). Free spins only.
- **Subject:** A rectangular glossy red plate in a gold frame with a red gem at each corner.
- **Style:** Glossy casual-slot UI panel; simple rectangle with small ornamental corner mounts.
- **Rendering:** Smooth gradients with a hard gloss band across the upper third, bevelled gold frame, soft red outer glow; crisp edges.
- **Colour:** Reds #ca0915 and #e53a31 with a pink gloss #d65d72 and dark red #480504 at the edge; gold frame #f3c91f.
- **Lighting:** Glass-like highlight across the top of the plate; frame lit from above; faint red glow around the outside.
- **Ambience:** Rich and celebratory, matched to the Hades palette.
- **Materials:** Red glass or enamel, polished gold, faceted rubies.
- **Variants:** One size, 330x228; text is drawn separately on top.
- **Construction:** Single sprite; the plain centre and regular frame would allow 9-slice scaling, though no border data is given (inference).
- **Notes:** Shares the gold-frame-and-ruby language of paytable_overlay_bg.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 34% · saturation 87% · contrast 71% · warm 100% / cool 0%
- **Palette (measured):** #ca0915 red 40%, #e53a31 red 19%, #f3c91f gold 12%, #d65d72 red 11%, #480504 dark red 10%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `common`: 1 parts
- `fullscreen`: 2 parts
- `client`: 3 parts
- `AGCC`: 1 parts
- `IntroScreenPlayButton`: 2 parts
- `volatility`: 3 parts
- `BlurShadow`: 1 parts
- `clientSkin_fp`: 4 parts
- `volatility_indicator`: 11 parts
- `GUI_v11_mobile`: 22 parts
- `GUI_v11_desktop`: 20 parts
- `GUI_v11`: 57 parts
- `TimeToSpin`: 1 parts
- `GUI_Mobile`: 28 parts
- `GUI_Paytable`: 4 parts
- `GUI`: 44 parts
- `promo_v5`: 27 parts
- `WOPAtlas`: 1 parts
- `notification`: 5 parts
- `LobbyAnimation`: 35 parts
- `lobby_button`: 38 parts
- `common_add`: 1 parts
- `zeha_button_fx`: 10 parts
- `shapes`: 2 parts
- `lumo_topbar_transparent`: 1 parts
- `paytable_common`: 14 parts
- `IntroScreen_misc`: 4 parts
- `GUI_desktop2017`: 5 parts
- `manual_bet_menu_paytable`: 2 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Bango Pro (Regular); Carbon Black (Regular); Comic Helvetic (Heavy); Futura (Condensed ExtraBold); Futura Book (Bold); FuturaMediumC (Regular); GROBOLD (Regular); Gang of Three (Regular); Go Noto Kurrent-Medium (Regular); Go Noto Kurrent-Regular (Regular); Montserrat Medium (Regular); Norse (Bold); Noto Sans Condensed Black (Regular); Poetsen One (Regular); Protest Strike (Regular); VNI-Revue (Bold); Verdana (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the provider's bundle format, so every name is the studio's own (extract.py): 3550 components cut from 243 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
