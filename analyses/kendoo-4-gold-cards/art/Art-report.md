# 4 Gold Carts: art report

kendoo · run `2026-11-27-2126-kendoo-4-gold-carts` · captured 2026-11-27

Source: the provider's free-play demo, https://betman-demo.head.kendoo.pro/betman-demo/static/game.html?token=…&game=4_gold_carts&wl=demo&title=4%20Gold%20Carts&lang=en&exit_url=https://kendoo.com

**Extracted:** 3299 named components from 132 textures in 132 atlases; 84 Spine skeletons; 175 frame sequences (1785 frames); 6 fonts. Grouped into 120 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A mine of hot gold on dark violet: four toy-like carts in red, blue, green and violet, each heaped with nuggets, stand over a deliberately plain dark reel board, and those four colours code every feature, label, gem, trail and font in the game.

**Style.** Stylised 3D-look digital painting in a casual, toy-like manner. Objects are short, wide and rounded (carts, pots, helmet, satchel), the one human and the donkey are jolly cartoon heads, low symbols are fat extruded letters, and the environment is a theatre set of flat rock layers. Nothing is realistic or worn: everything looks new, polished and collectable.

**Rendering.** Smooth render-like gradients with clean hard silhouettes and no outlines; a bright rim on almost every form. Glow is never painted into an object: halos, flares, rings and rays are separate soft sprites on additive slots. Backdrops are fully soft gradients; the drawn rock is broad brushwork cut into layers. Lettering is flat-faced with a dark extrusion and a stroke.

**Colour.** Measured over the game's own art: dark violet #24083b is 48% of all pixels, then dark red #5d0e27 (8%), gold #fcdd21 (8%), orange #f5790f (7%), red #a21111 (5%) and near-white #fbfaf4 (4%); saturation 0.82 (vivid), brightness 0.30. Read: a dark violet and maroon ground carries hot gold and orange, and four accent colours are kept strictly for the four features: red for Expand, blue for Power, green for Collect, violet for Multi. Jackpots re-use three of them (green Mini, blue Minor, purple Major) and take orange-red for Grand and Royal.

**Lighting.** Light comes from the treasure and from inside the mountain: carts, nuggets, gems and lamps glow, an orange heat patch sits behind the board, and the tunnel is lit by embers. Objects are top- and top-left-lit with strong specular highlights (measured light direction over the parts: top 238, top-left 113, top-right 106). The bonus board is framed by the brightest edge in the game, a yellow-white glow line.

**Ambience.** Warm, loud and generous: a forge-like underground where everything valuable shines. Friendly instead of adventurous; the miner laughs, the donkey grins. The bonus turns hotter (red rock, glowing board) and the intro card is close to a sunrise.

**Shape language.** Rounded and chunky objects; trapezoid sign plates (wider at the top) for every label and jackpot panel; circles for nuggets, gems, coins and the Power wheel; thin straight gold lines for the reel frame. Sharp shapes appear only in light: star flares, rays, comet trails.

**Materials.** Polished gold (nuggets, coins, rims), glossy enamelled metal in the four feature colours, cut crystal gems, glass lamps, leather and brass on the mid symbols, rough timber and rock in the scene, and light itself as a material (halos, fire lines, neon-like rails).

**Typography and lettering.** All display words are drawn art in one family of heavy rounded capitals with a dark stroke and extrusion: the logo, the feature labels, the jackpot words, NICE, GREAT and the big win words. Numbers are eleven bitmap fonts of one rounded numeral, each coloured for its place (gold for wins, cream for nugget values, blue, green, red and pink for the four features). Six font files are embedded for running text: League Spartan and Myriad Pro (game), Gilroy (Kendoo's game runner).

**Motion.** Spine 3.8.99 throughout: 84 skeletons with 950 animations between them, and 175 frame sequences (1,785 frames) for flashes, sweeps, fire lines and trails. The carts are the most animated things in the game (46 to 49 animations each, ten fill levels with idle, win, impact and level-up). Symbols have a 1 s win; the miner and the nugget also have fall and idle. All 84 rigs bind to their own atlas and 80 were drawn by this project's tool; frames it drew are secondary to the game screens.

**Variants and themes.** Almost every interface rig carries a base-game (mg) and a bonus (bg) set, and most scene rigs a portrait and a landscape set. The scene exists in two colourings of the same layers (base and bonus). The cart exists three times at three sizes (above the reels, on the intro card, in the shop cards) and again as a pot symbol, a line badge and a coin emblem.

**How it is built.** 132 pictures hold 3,299 named sprites. Every skeleton has its own small atlas (one to four pages) and nothing is shared between rigs; loose sprites sit in eight TexturePacker sheets by game state (preloader, main, symbols, bonus, power, gamble, paytable, bigwin). The art is small: symbols are about 140x106 px, the largest cart part 262x158 px, the largest scene layer 838x672 px, the backdrops 1860x2144 px soft gradients. A resource map lists a half-size 'A1' variant of every picture; this run read the full-size 'default' set as PNG.

**Consistency.** Very high. One lettering family, one numeral, one plate shape, one gold, and a four-colour code applied without exception from cart to trail to font. The only pieces outside it are the white helper glyphs and Kendoo's shared button set.

**What to take from it.** (1) Pick the feature colours first and spend them everywhere: here red, blue, green and violet each own a cart, a label, a pot symbol, a rail, a trail, a landing light and a number font, so a player reads which feature is acting from colour alone. (2) Make the prize the hero. There is no mascot on stage; four carts of gold take that place and get the animation budget (about 190 parts and 46 to 49 animations each, ten fill levels). (3) Keep the reel board plain. A flat dark maroon panel with a thin gold line lets small, saturated symbols and the carts above carry the screen. (4) Build the environment as a few rock layers over a soft gradient and repaint the same layers for the bonus: two moods from one drawing. (5) Treat glow as parts, not paint: every halo, ring and flare is its own additive sprite, which is why one cart rig can show ten levels, a win flash and a gold version. (6) One numeral, many colourings: eleven bitmap number fonts share one rounded digit design; a new game needs the digits drawn once. (7) Re-use the hero at every scale (scene, intro card, shop card, pot symbol, badge, coin): the game feels rich while showing one object. (8) For AI art work: this package is a good target for a prompt-and-assemble pipeline because the pieces are small, isolated on clear ground and strictly colour-coded; the hard part is the rigging (hundreds of small parts per cart), not the painting.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 30% · saturation 82% · contrast 37% · warm 44% / cool 46% · brighter towards: top (238), top-left (113), top-right (106)

Palette: #24083b dark purple 48%, #5d0e27 dark red 8%, #fcdd21 gold 8%, #f5790f orange 7%, #a21111 red 5%, #fbfaf4 light gold 4%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 8 | 14% | 86% | 25% | 29% / 62% | #24083d dark purple 76%, #630e2e dark red 11%, #f9d820 gold 4% |
| Reel board | 14 | 41% | 82% | 31% | 81% / 14% | #35050f black 38%, #feaf18 orange 21%, #fef565 gold 7% |
| Symbols | 20 | 54% | 72% | 50% | 51% / 32% | #fafcfa light green 10%, #94280a red 10%, #f69c13 orange 7% |
| Characters | 4 | 69% | 68% | 49% | 75% / 16% | #fefdf8 light gold 22%, #fae50f gold 18%, #f68a06 orange 18% |
| Logo and title | 1 | 62% | 63% | 62% | 100% / 0% | #fce43e gold 18%, #e95628 red 16%, #fdf5e6 light orange 9% |
| Win celebrations and banners | 8 | 59% | 76% | 66% | 83% / 12% | #fdbc0f orange 17%, #fdf9ed light gold 12%, #461105 dark red 11% |
| Effects | 26 | 55% | 76% | 65% | 47% / 38% | #da1f0e red 12%, #fc730c orange 10%, #f5f5f5 white 9% |
| Game interface | 25 | 42% | 81% | 47% | 58% / 30% | #9f0705 red 14%, #37024a dark purple 12%, #fcc60f gold 9% |
| Typography | 11 | 42% | 83% | 91% | 84% / 12% | #480303 dark red 26%, #fbaa07 orange 14%, #981704 red 13% |
| Provider interface (shared) | 3 | 66% | 62% | 9% | 61% / 7% | #ef9106 orange 41%, #ffffff white 27%, #e5547c red 8% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Bonus game backdrop, landscape

`bonus_bg_h` · atlas · 1 parts · largest 1860×2144 · sheet `sheets/bonus_bg_h.webp`

- **Role:** The lowest layer of the Bonus Game screen.
- **Subject:** A near-uniform dark indigo field with a faint blue glow.
- **Style:** A soft painted gradient with faint cloud-like texture; no drawn objects.
- **Rendering:** Fully soft, low detail, made to sit behind everything.
- **Colour:** Measured: #1e0a3e 100%.
- **Lighting:** The light is a glow painted into the gradient itself.
- **Ambience:** Depth and heat without detail.
- **Materials:** Air and glow.
- **Variants:** A landscape (_h) and a portrait (_v) file of the same picture size, 1860x2144 px.
- **Construction:** One whole picture, listed in the client's resource map as a JPG-named resource and served as PNG, AVIF or WebP.
- **Notes:** The scene's drawn rock is not in this file: it is the layered skeleton bg_main / bg_background that stands on top of it.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 7% · saturation 85% · contrast 8% · warm 0% / cool 100%
- **Palette (measured):** #1e0a3e dark purple 100%

### Bonus game backdrop, portrait

`bonus_bg_v` · atlas · 1 parts · largest 1860×2144 · sheet `sheets/bonus_bg_v.webp`

- **Role:** The lowest layer of the Bonus Game in portrait.
- **Subject:** The same dark indigo field.
- **Style:** A soft painted gradient with faint cloud-like texture; no drawn objects.
- **Rendering:** Fully soft, low detail, made to sit behind everything.
- **Colour:** Measured: #1e0a3e 100%.
- **Lighting:** The light is a glow painted into the gradient itself.
- **Ambience:** Depth and heat without detail.
- **Materials:** Air and glow.
- **Variants:** A landscape (_h) and a portrait (_v) file of the same picture size, 1860x2144 px.
- **Construction:** One whole picture, listed in the client's resource map as a JPG-named resource and served as PNG, AVIF or WebP.
- **Notes:** The scene's drawn rock is not in this file: it is the layered skeleton bg_main / bg_background that stands on top of it.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 7% · saturation 85% · contrast 8% · warm 0% / cool 100%
- **Palette (measured):** #1e0a3e dark purple 100%

### Intro card backdrop, landscape

`intro_bg_h` · atlas · 1 parts · largest 1860×2144 · sheet `sheets/intro_bg_h.webp`

- **Role:** Behind the opening card 'Bonus Game Features' (seen in the game screens).
- **Subject:** A hot yellow-orange glow at the top falling through red into deep violet, with faint rays and a few sparks.
- **Style:** A soft painted gradient with faint cloud-like texture; no drawn objects.
- **Rendering:** Fully soft, low detail, made to sit behind everything.
- **Colour:** Measured: #260444 62%, #6a0a37 18%, #b41d27 8%, #fad41c 5%.
- **Lighting:** The light is a glow painted into the gradient itself.
- **Ambience:** Depth and heat without detail.
- **Materials:** Air and glow.
- **Variants:** A landscape (_h) and a portrait (_v) file of the same picture size, 1860x2144 px.
- **Construction:** One whole picture, listed in the client's resource map as a JPG-named resource and served as PNG, AVIF or WebP.
- **Notes:** The scene's drawn rock is not in this file: it is the layered skeleton bg_main / bg_background that stands on top of it.
- **Measured:** dark, vivid, warm and cool mixed, high contrast, hard-edged · brightness 16% · saturation 93% · contrast 66% · warm 37% / cool 50% · brighter towards: top (1)
- **Palette (measured):** #260444 dark purple 62%, #6a0a37 dark magenta 18%, #b41d27 red 8%, #fad41c gold 5%, #f68619 orange 4%, #e6481c red 3%

### Intro card backdrop, portrait

`intro_bg_v` · atlas · 1 parts · largest 1860×2144 · sheet `sheets/intro_bg_v.webp`

- **Role:** Behind the opening card in portrait.
- **Subject:** The same sun-like glow, larger in the frame.
- **Style:** A soft painted gradient with faint cloud-like texture; no drawn objects.
- **Rendering:** Fully soft, low detail, made to sit behind everything.
- **Colour:** Measured: #280545 35%, #f9d821 23%, #f57918 20%, #6b0c36 9%.
- **Lighting:** The light is a glow painted into the gradient itself.
- **Ambience:** Depth and heat without detail.
- **Materials:** Air and glow.
- **Variants:** A landscape (_h) and a portrait (_v) file of the same picture size, 1860x2144 px.
- **Construction:** One whole picture, listed in the client's resource map as a JPG-named resource and served as PNG, AVIF or WebP.
- **Notes:** The scene's drawn rock is not in this file: it is the layered skeleton bg_main / bg_background that stands on top of it.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 37% · saturation 90% · contrast 52% · warm 66% / cool 28%
- **Palette (measured):** #280545 dark purple 35%, #f9d821 gold 23%, #f57918 orange 20%, #6b0c36 dark magenta 9%, #d12920 red 9%, #9f132a red 3%

### Base game backdrop, landscape

`main_bg_h` · atlas · 1 parts · largest 1860×2144 · sheet `sheets/main_bg_h.webp`

- **Role:** The lowest layer of the base game screen.
- **Subject:** A dark violet field with a dull red glow in the upper part.
- **Style:** A soft painted gradient with faint cloud-like texture; no drawn objects.
- **Rendering:** Fully soft, low detail, made to sit behind everything.
- **Colour:** Measured: #2b083c 81%, #5f0f28 19%.
- **Lighting:** The light is a glow painted into the gradient itself.
- **Ambience:** Depth and heat without detail.
- **Materials:** Air and glow.
- **Variants:** A landscape (_h) and a portrait (_v) file of the same picture size, 1860x2144 px.
- **Construction:** One whole picture, listed in the client's resource map as a JPG-named resource and served as PNG, AVIF or WebP.
- **Notes:** The scene's drawn rock is not in this file: it is the layered skeleton bg_main / bg_background that stands on top of it.
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 9% · saturation 86% · contrast 10% · warm 35% / cool 47% · brighter towards: top (1)
- **Palette (measured):** #2b083c dark purple 81%, #5f0f28 dark red 19%

### Base game backdrop, portrait

`main_bg_v` · atlas · 1 parts · largest 1860×2144 · sheet `sheets/main_bg_v.webp`

- **Role:** The lowest layer of the base game in portrait.
- **Subject:** The same violet field with a red glow at the top.
- **Style:** A soft painted gradient with faint cloud-like texture; no drawn objects.
- **Rendering:** Fully soft, low detail, made to sit behind everything.
- **Colour:** Measured: #2b083c 81%, #5f0f28 19%.
- **Lighting:** The light is a glow painted into the gradient itself.
- **Ambience:** Depth and heat without detail.
- **Materials:** Air and glow.
- **Variants:** A landscape (_h) and a portrait (_v) file of the same picture size, 1860x2144 px.
- **Construction:** One whole picture, listed in the client's resource map as a JPG-named resource and served as PNG, AVIF or WebP.
- **Notes:** The scene's drawn rock is not in this file: it is the layered skeleton bg_main / bg_background that stands on top of it.
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 9% · saturation 86% · contrast 10% · warm 35% / cool 47% · brighter towards: top (1)
- **Palette (measured):** #2b083c dark purple 81%, #5f0f28 dark red 19%

### Mine entrance scene (base game)

`bg_main` · skeleton · 28 parts · largest 838×672 · sheet `sheets/bg_main.webp`

- **Role:** The drawn environment of the base game: the game screens show orange-red cave rock around and above the reel board with a timber frame; this rig is that scene in layers.
- **Subject:** The mouth of a mine: dark rock walls in several depths, a timber frame of two posts and a beam, loose stones at its feet and a glowing ember-like fire deep inside.
- **Style:** Painterly stylised rock in big simple masses, closer to a theatre set than to a landscape: flat-ish shapes stacked in depth.
- **Rendering:** Broad soft brushwork with hard cut silhouettes per layer; edge light in orange picks out the forms.
- **Colour:** Dark violet-black rock with orange and red edge light. Measured: #210c28 82%, #6c1416 8%, #eb4508 5%, #a6220e 3%.
- **Lighting:** Lit from inside the tunnel and from below by fire; 'light' copies of several rock layers and global glow patches are separate parts, so the heat can pulse.
- **Ambience:** A warm, glowing underground, more forge than cold cave.
- **Materials:** Rock, rough timber, embers.
- **Variants:** Landscape and portrait loops of 20 s, with two test loops left in the file.
- **Motion:** A slow 20 s loop; the layers and their light copies fade and shift (inference from the part names and the five drawn frames, which differ a lot from each other: the frames drawn by this tool are not a reliable picture of the scene, the game screens are). Spine 3.8.99 skeleton, 38 bones, 63 slots, 4 animations as the file names them: portrait/loop (20.0 s), landscape/loop (20.0 s), portrait/loop_test (20.0 s), landscape/loop_test (20.0 s).
- **Construction:** 28 parts: about ten rock layers (dark_m…, dark_mountains…) with lit copies, timber frame pieces, stones, a mask, fire light sprites and two glow patches. Largest part 838x672 px.
- **Notes:** The whole environment is small layered pieces over a gradient, not one painted background.
- **Skeleton (from the file):** Spine 3.8.99 · 38 bones · 63 slots · animations: portrait/loop (20.0 s), landscape/loop (20.0 s), portrait/loop_test (20.0 s), landscape/loop_test (20.0 s)
- **Measured:** dark, vivid, warm and cool mixed, low contrast · brightness 11% · saturation 74% · contrast 15% · warm 37% / cool 52% · brighter towards: bottom (6), bottom-right (5), left (4)
- **Palette (measured):** #210c28 black 82%, #6c1416 dark red 8%, #eb4508 orange 5%, #a6220e red 3%

### Mine entrance scene (bonus and Expand)

`bg_background` · skeleton · 23 parts · largest 838×672 · sheet `sheets/bg_background.webp`

- **Role:** The same scene for the Bonus Game; the animation landscape/loop_expand ties it to the Expand feature (file name).
- **Subject:** The same mine mouth, re-coloured: red-orange rock outside, violet-blue rock inside the tunnel, a lit doorway at the end.
- **Style:** As bg_main.
- **Rendering:** As bg_main, with a stronger colour split between the hot outside and the cool inside.
- **Colour:** Indigo and violet with saturated red. Measured: #1b0d36 70%, #880d06 8%, #3c227e 6%, #be2d08 3%.
- **Lighting:** Red light outside against blue-violet shadow inside; a reel glow patch (bg_reel_glow_blue) is among the parts.
- **Ambience:** Hotter and more theatrical than the base scene.
- **Materials:** Rock, timber, glow.
- **Variants:** Portrait loop, landscape loop, landscape loop for Expand.
- **Motion:** Spine 3.8.99 skeleton, 41 bones, 55 slots, 3 animations as the file names them: portrait/loop (20.0 s), landscape/loop (20.0 s), landscape/loop_expand (20.0 s).
- **Construction:** 23 parts, the same layer names as bg_main.
- **Notes:** One scene, two colourings: the bonus background is a repaint of the base layers, not new drawing (read from the matching part names and shapes).
- **Skeleton (from the file):** Spine 3.8.99 · 41 bones · 55 slots · animations: portrait/loop (20.0 s), landscape/loop (20.0 s), landscape/loop_expand (20.0 s)
- **Measured:** dark, vivid, cool, low contrast · brightness 12% · saturation 78% · contrast 20% · warm 21% / cool 73% · brighter towards: top-left (4), bottom (4), bottom-left (4)
- **Palette (measured):** #1b0d36 dark purple 70%, #880d06 dark red 8%, #3c227e purple 6%, #be2d08 red 3%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Bonus reel field

`bg` · atlas · 1 parts · largest 670×314 · sheet `sheets/bg.webp`

- **Role:** The plain field behind the Bonus Game board.
- **Subject:** A flat dark maroon rectangle.
- **Rendering:** Flat.
- **Colour:** Measured: #33010c 100%.
- **Construction:** One picture, 670x314 px.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 5% · saturation 98% · contrast 0% · warm 100% / cool 0%
- **Palette (measured):** #33010c black 100%

### Bonus cell plate

`plate` · atlas · 1 parts · largest 131×101 · sheet `sheets/plate.webp`

- **Role:** The tile of an empty cell in the Bonus Game (seen in the bonus screens: every empty cell shows the game's logo faintly).
- **Subject:** A dark red square with the 4 GOLD CARTS logo embossed tone on tone.
- **Rendering:** Flat with a low-contrast emboss.
- **Colour:** Measured: #450308 100%.
- **Variants:** plate and plate_moves (a brighter red copy).
- **Construction:** One picture, 131x101 px.
- **Notes:** Branding the empty cell keeps an almost empty bonus board from looking blank.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 7% · saturation 97% · contrast 8% · warm 100% / cool 0%
- **Palette (measured):** #450308 dark red 100%

### Bonus cell plate, moving

`plate_moves` · atlas · 1 parts · largest 131×101 · sheet `sheets/plate_moves.webp`

- **Role:** The brighter copy of the cell plate, used while cells move (file name).
- **Subject:** The same logo tile in a lighter crimson.
- **Rendering:** Flat.
- **Colour:** Measured: #7a0a22 100%.
- **Construction:** One picture, 131x101 px.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 14% · saturation 92% · contrast 9% · warm 100% / cool 0%
- **Palette (measured):** #7a0a22 dark red 100%

### Bonus board frames

`bonus-reels` · atlas · 3 parts · largest 681×321 · sheet `sheets/bonus-reels.webp`

- **Role:** The frame and dividers of the Bonus Game board.
- **Subject:** A thin orange-gold rectangle frame in two copies and a grid of dividers.
- **Rendering:** Thin lines.
- **Colour:** Measured: #ff9b05 92%, #f54d09 7%.
- **Variants:** frame_reel_bonus, frame_reel_bonus_move, dividers.
- **Construction:** 3 sprites, largest 681x321 px.
- **Measured:** bright, vivid, warm, low contrast · brightness 63% · saturation 98% · contrast 25% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #ff9b05 orange 92%, #f54d09 orange 7%

### Base reel board

`main-reels` · atlas · 1 parts · largest 720×335 · sheet `sheets/main-reels.webp`

- **Role:** The 5x3 reel board of the base game.
- **Subject:** A dark maroon panel in five columns with thin gold dividers and a thin gold frame.
- **Style:** Minimal: a flat dark field so the symbols carry all the colour.
- **Rendering:** Flat fill with a slight vertical gradient per column; a one-pixel-like gold line.
- **Colour:** Measured: #370306 91%, #f08e10 6%, #753501 2%.
- **Lighting:** None of its own.
- **Materials:** Dark lacquer, gold line.
- **Construction:** One sprite, 720x335 px, in the main sheet.
- **Notes:** The frame is deliberately thin; the weight sits in the carts above and the jackpot panels beside.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 10% · saturation 96% · contrast 50% · warm 100% / cool 0%
- **Palette (measured):** #370306 black 91%, #f08e10 orange 6%, #753501 brown 2%

### Power wheel cell pieces

`power` · atlas · 3 parts · largest 143×143 · sheet `sheets/power.webp`

- **Role:** Loose pieces of the Power Bonus Game wheel from the power sheet.
- **Subject:** A red disc used as a mask, a dark round plate and a faint cart emblem.
- **Colour:** Measured: #370c23 52%, #d40000 46%, #9b2c56 2%.
- **Construction:** 3 sprites, 143x143 px.
- **Notes:** The plain red disc is a mask, not art to be seen.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 13% · saturation 87% · contrast 4% · warm 78% / cool 0%
- **Palette (measured):** #370c23 dark magenta 52%, #d40000 red 46%, #9b2c56 red 2%

### Rails under the carts

`rails` · skeleton · 34 parts · largest 347×111 · sheet `sheets/rails.webp`

- **Role:** The track the four big carts stand on above the reels.
- **Subject:** Short pieces of rail and sleepers in perspective, each in the four feature colours with a glowing copy, meeting at a centre point.
- **Style:** Simplified, almost neon track.
- **Rendering:** Flat coloured bars with glow.
- **Colour:** Measured: #fdab0f 18%, #f8f634 14%, #fafce4 11%, #ef4427 9%.
- **Lighting:** Glow copies (_gl) light per cart.
- **Materials:** Coloured metal, light.
- **Variants:** Red, violet, green and blue rails and three sleepers each.
- **Motion:** Spine 3.8.99 skeleton, 57 bones, 95 slots, 1 animations as the file names them: idle (4.33 s).
- **Construction:** 34 parts.
- **Notes:** Even the ground under each cart carries its feature colour.
- **Skeleton (from the file):** Spine 3.8.99 · 57 bones · 95 slots · animations: idle (4.33 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 66% · saturation 66% · contrast 35% · warm 75% / cool 14% · brighter towards: top-right (5), top (4), top-left (4)
- **Palette (measured):** #fdab0f orange 18%, #f8f634 gold 14%, #fafce4 light gold 11%, #ef4427 red 9%, #9f2c1d red 8%, #fa8ee0 light magenta 7%

### Cart mark on a symbol

`carts` · skeleton · 25 parts · largest 368×175 · sheet `sheets/carts.webp`

- **Role:** The paytable says every Bonus and Jackpot symbol carries a coloured cart label tied to a feature; this rig is that label landing on a cell.
- **Subject:** A cart outline in gold with a round lamp, flat cart bodies in blue, green, red and violet, and flares and ray rings in the same colours.
- **Style:** An icon: the cart reduced to a line badge.
- **Rendering:** Flat fills, line and glow.
- **Colour:** Measured: #2854fe 20%, #753fff 18%, #3cff00 12%, #e2090a 5%.
- **Variants:** Four colours; fall, fall_autospin and idle.
- **Motion:** Spine 3.8.99 skeleton, 32 bones, 22 slots, 3 animations as the file names them: fall (1.0 s), fall_autospin (0.33 s), idle (2.0 s).
- **Construction:** 25 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 32 bones · 22 slots · animations: fall (1.0 s), fall_autospin (0.33 s), idle (2.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, low contrast, glow or soft effect · brightness 42% · saturation 86% · contrast 24% · warm 26% / cool 64% · brighter towards: top (5)
- **Palette (measured):** #2854fe blue 20%, #753fff purple 18%, #3cff00 green 12%, #e2090a red 5%, #0f7104 dark green 5%, #bc05f7 purple 5%

### Bonus board glow frame

`bonus_reels_win` · skeleton · 33 parts · largest 198×400 · sheet `sheets/bonus_reels_win.webp`

- **Role:** The bright frame round the Bonus Game board (seen in every bonus screen); its animations are named for board sizes 5x3, 5x4, 5x5 and 5x6, the rows the Expand feature adds.
- **Subject:** A thick glowing yellow-white rounded rectangle with sparks along it.
- **Rendering:** A soft bloom round a hot core line.
- **Colour:** Measured: #ffb91f 61%, #fffff4 18%, #fffa82 17%, #fff346 3%.
- **Lighting:** Emissive; the brightest edge in the game.
- **Ambience:** A stage lit for the bonus.
- **Materials:** Light.
- **Variants:** Idle and start for four board heights.
- **Motion:** Spine 3.8.99 skeleton, 139 bones, 120 slots, 8 animations as the file names them: 5x6/pt_idle (2.0 s), 5x5/pt_idle (2.0 s), 5x4/pt_idle (2.0 s), 5x3/pt_idle (2.0 s), 5x6/pt_start (1.0 s), 5x5/pt_start (1.0 s), 5x4/pt_start (1.0 s), 5x3/pt_start (1.0 s).
- **Construction:** 33 parts: frame segments as 29-frame sequences, a glow fill, a star and particles.
- **Skeleton (from the file):** Spine 3.8.99 · 139 bones · 120 slots · animations: 5x6/pt_idle (2.0 s), 5x5/pt_idle (2.0 s), 5x4/pt_idle (2.0 s), 5x3/pt_idle (2.0 s), 5x6/pt_start (1.0 s), 5x5/pt_start (1.0 s), 5x4/pt_start (1.0 s), 5x3/pt_start (1.0 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 82% · saturation 66% · contrast 29% · warm 100% / cool 0%
- **Palette (measured):** #ffb91f orange 61%, #fffff4 light gold 18%, #fffa82 light gold 17%, #fff346 gold 3%

### Feature colour frames

`reel_features` · skeleton · 8 parts · largest 342×319 · sheet `sheets/reel_features.webp`

- **Role:** Coloured frames round the board that mark which features are active (animation names collect_0…, expand_0…, and so on).
- **Subject:** Thin glowing rectangle frames in gold, blue, green, pink and red.
- **Rendering:** Line with glow.
- **Colour:** Measured: #ffff5f 18%, #d000ff 16%, #0073ff 16%, #11ff00 15%.
- **Lighting:** Emissive.
- **Variants:** Four feature colours and gold.
- **Motion:** Spine 3.8.99 skeleton, 3 bones, 3 slots, 16 animations as the file names them: collect_0 (0.0 s), collect_1 (0.0 s), collect_2 (0.0 s), collect_3 (0.0 s), expand_0 (0.0 s), expand_1 (0.0 s), expand_2 (0.0 s), expand_3 (0.0 s) and 8 more.
- **Construction:** 8 parts, largest 342x319 px.
- **Skeleton (from the file):** Spine 3.8.99 · 3 bones · 3 slots · animations: collect_0 (0.0 s), collect_1 (0.0 s), collect_2 (0.0 s), collect_3 (0.0 s), expand_0 (0.0 s), expand_1 (0.0 s), expand_2 (0.0 s), expand_3 (0.0 s), multi_0 (0.0 s), multi_1 (0.0 s), multi_2 (0.0 s), multi_3 (0.0 s), power_0 (0.0 s), power_1 (0.0 s), power_2 (0.0 s), power_3 (0.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 56% · saturation 88% · contrast 13% · warm 53% / cool 39%
- **Palette (measured):** #ffff5f gold 18%, #d000ff purple 16%, #0073ff blue 16%, #11ff00 green 15%, #ff0011 red 14%, #fcd13a gold 12%

### Feature frame flash

`reel_features_p2` · skeleton · 5 parts · largest 372×76 · sheet `sheets/reel_features_p2.webp`

- **Role:** A flash along the top of the board when a feature starts.
- **Subject:** A horizontal orange star flare with sparks on a three-sided gold frame.
- **Rendering:** Additive flare.
- **Colour:** Measured: #eb000c 68%, #fe9c18 19%, #fefa5e 8%, #ffe32c 4%.
- **Motion:** Spine 3.8.99 skeleton, 15 bones, 9 slots, 1 animations as the file names them: start (1.5 s).
- **Construction:** 5 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 15 bones · 9 slots · animations: start (1.5 s)
- **Measured:** mid-tone, vivid, warm, low contrast, glow or soft effect · brightness 38% · saturation 94% · contrast 8% · warm 100% / cool 0%
- **Palette (measured):** #eb000c red 68%, #fe9c18 orange 19%, #fefa5e gold 8%, #ffe32c gold 4%

### Power Bonus wheel

`base` · skeleton · 20 parts · largest 539×486 · sheet `sheets/base.webp`

- **Role:** The board of the Power Bonus Game: the paytable says it is played on a separate reel of six cells with a centre slot.
- **Subject:** Six round blue-rimmed cells in a ring round a centre socket, set on a bed of glowing lava-like gold rock, each cell showing a dark cart emblem.
- **Style:** Chunky toy-like machine, consistent with the carts.
- **Rendering:** Glossy rims, dark recessed cells, glowing cracked rock behind.
- **Colour:** Blue rims against orange-gold rock on dark plum cells. Measured: #2d0f2a 43%, #152270 8%, #fef117 4%.
- **Lighting:** Rock glows from within; a cyan ring glow is additive.
- **Ambience:** A machine inside the mountain.
- **Materials:** Blue enamel, gold rim, molten rock.
- **Variants:** start, idle, end.
- **Motion:** Spine 3.8.99 skeleton, 28 bones, 50 slots, 3 animations as the file names them: end (0.67 s), idle (3.0 s), start (1.0 s).
- **Construction:** 20 parts: a ring frame, the wheel half mirrored, rock chunks with bright 'add' copies, connectors.
- **Notes:** Not reached in play; read from the files.
- **Skeleton (from the file):** Spine 3.8.99 · 28 bones · 50 slots · animations: end (0.67 s), idle (3.0 s), start (1.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 31% · saturation 73% · contrast 46% · warm 46% / cool 42% · brighter towards: top-left (3), top (2), bottom (2)
- **Palette (measured):** #2d0f2a black 43%, #152270 dark blue 8%, #fef117 gold 4%

### Power wheel centre coin

`center_plate` · skeleton · 8 parts · largest 247×235 · sheet `sheets/center_plate.webp`

- **Role:** The centre slot of the Power wheel, where the paytable says a multiplier of x2 to x10 appears.
- **Subject:** A thick gold coin with a cart emblem and a glowing rim.
- **Rendering:** Glossy gold with a hot edge.
- **Colour:** Measured: #feb60b 53%, #f66b05 16%, #fff43c 15%, #b63a09 6%.
- **Materials:** Gold.
- **Variants:** 23 animations, loop and static per level.
- **Motion:** Spine 3.8.99 skeleton, 10 bones, 8 slots, 23 animations as the file names them: lvl_1_loop (2.0 s), lvl_1_static (0.0 s), lvl_2_loop (2.0 s), lvl_2_static (0.0 s), lvl_3_loop (2.0 s), lvl_3_static (0.0 s), lvl_4_loop (2.0 s), lvl_4_static (0.0 s) and 15 more.
- **Construction:** 8 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 10 bones · 8 slots · animations: lvl_1_loop (2.0 s), lvl_1_static (0.0 s), lvl_2_loop (2.0 s), lvl_2_static (0.0 s), lvl_3_loop (2.0 s), lvl_3_static (0.0 s), lvl_4_loop (2.0 s), lvl_4_static (0.0 s), lvl_5_loop (2.0 s), lvl_5_static (0.0 s), lvl_6_loop (2.0 s), lvl_6_start (0.5 s), lvl_6_static (0.0 s), lvl_0_loop (2.0 s), lvl_0_static (0.0 s), open_spin_1 (0.5 s), open_spin_2 (0.5 s), open_spin_3 (0.5 s), open_spin_4 (0.5 s), open_spin_5 (0.5 s), open_spin_6 (0.5 s), spin (0.5 s), spin_end (1.23 s)
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 70% · saturation 88% · contrast 54% · warm 100% / cool 0% · brighter towards: top (3)
- **Palette (measured):** #feb60b orange 53%, #f66b05 orange 16%, #fff43c gold 15%, #b63a09 brown 6%, #fef98a light gold 5%, #fbffd6 light gold 3%

### Power cell glint

`cell_blik` · skeleton · 4 parts · largest 81×69 · sheet `sheets/cell_blik.webp`

- **Role:** A glint passing over a Power wheel cell.
- **Subject:** A pink-white highlight in the shape of the cart emblem, in three pieces.
- **Rendering:** Soft line.
- **Colour:** Measured: #ff6f8c 54%, #ffcaf0 37%, #ff9ec0 8%.
- **Motion:** Spine 3.8.99 skeleton, 6 bones, 4 slots, 1 animations as the file names them: loop (6.0 s).
- **Construction:** 4 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 4 slots · animations: loop (6.0 s)
- **Measured:** bright, saturated, warm, medium contrast, glow or soft effect · brightness 68% · saturation 42% · contrast 33% · warm 95% / cool 0%
- **Palette (measured):** #ff6f8c red 54%, #ffcaf0 light magenta 37%, #ff9ec0 light red 8%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Symbol glow patches

`symbols-glow` · atlas · 3 parts · largest 139×277 · sheet `sheets/symbols-glow.webp`

- **Role:** Soft coloured patches placed behind feature symbols.
- **Subject:** Three blurred rounded rectangles in blue, green and violet.
- **Rendering:** Fully soft.
- **Colour:** Measured: #05f534 22%, #fe57fc 19%, #40f1ff 18%, #a404b9 10%.
- **Lighting:** Emissive.
- **Variants:** Three colours.
- **Construction:** 3 sprites, 139x277 px.
- **Notes:** No red patch is in this sheet.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 52% · saturation 87% · contrast 55% · warm 16% / cool 51%
- **Palette (measured):** #05f534 green 22%, #fe57fc magenta 19%, #40f1ff cyan 18%, #a404b9 magenta 10%, #016d16 dark green 10%, #0621e2 blue 9%

### Blurred symbol pictures

`symbols-blur` · atlas · 19 parts · largest 188×216 · sheet `sheets/symbols-blur.webp`

- **Role:** Vertically blurred copies of the symbols for spinning reels.
- **Subject:** Nineteen pictures: the feature pots, the three gems, the nugget and regular symbols, each smeared downward.
- **Rendering:** Baked motion blur.
- **Colour:** Measured: #93300e 18%, #ec9717 8%, #195d10 8%, #1894f3 3%.
- **Variants:** One per symbol.
- **Construction:** 19 sprites in the symbols sheet.
- **Notes:** Blur is baked art, not a shader.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 43% · saturation 79% · contrast 55% · warm 54% / cool 32% · brighter towards: top (6), top-right (4), top-left (1)
- **Palette (measured):** #93300e brown 18%, #ec9717 orange 8%, #195d10 dark green 8%, #1894f3 blue 3%, #4d190d dark red 2%, #f9112e red 2%

### Static symbol pictures

`symbols-static` · atlas · 11 parts · largest 141×121 · sheet `sheets/symbols-static.webp`

- **Role:** Flat copies of the symbols for reels at rest, from the symbols sheet.
- **Subject:** Eleven pictures; the sheet shows the donkey, the gold pan and the 10 first.
- **Style:** As the animated symbols.
- **Rendering:** Each symbol baked to one picture.
- **Colour:** Measured: #902508 23%, #49110a 11%, #1a5908 8%, #f2c113 7%.
- **Variants:** One per regular symbol.
- **Construction:** 11 sprites of about 141x121 px in one TexturePacker sheet.
- **Notes:** The reels show these; the skeleton takes over when a symbol wins (inference from the two sets existing side by side).
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 35% · saturation 82% · contrast 75% · warm 70% / cool 19% · brighter towards: top-right (4), top (2), top-left (1)
- **Palette (measured):** #902508 dark red 23%, #49110a dark red 11%, #1a5908 dark green 8%, #f2c113 gold 7%, #6e0667 dark magenta 6%, #0f3270 dark blue 5%

### Jackpot words on symbols

`symbols-text_holders` · atlas · 6 parts · largest 181×83 · sheet `sheets/symbols-text_holders.webp`

- **Role:** The words written across the jackpot gems.
- **Subject:** MAJOR, MINOR and MINI as rounded capitals with a coloured glow, each with a blurred copy.
- **Style:** Rounded heavy sans capitals.
- **Rendering:** White-to-colour fill, dark stroke, outer glow.
- **Colour:** Magenta for MAJOR, cyan for MINOR, green for MINI. Measured: #070c10 11%, #f391ef 10%, #b161b3 8%, #f2f3fc 6%.
- **Variants:** Three words, sharp and blurred.
- **Construction:** 6 sprites.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 50% · saturation 63% · contrast 82% · warm 16% / cool 55%
- **Palette (measured):** #070c10 black 11%, #f391ef light magenta 10%, #b161b3 magenta 8%, #f2f3fc light blue 6%, #18d6fd cyan 5%, #fa36e5 magenta 5%

### Feature symbols: Expand, Power, Collect pots

`sym14` · skeleton · 133 parts · largest 200×200 · sheet `sheets/sym14.webp`

- **Role:** The feature symbols of the Bonus Game. The paytable says the red Expand, blue Power and green Collect symbols land when their feature is active and start it.
- **Subject:** A small round pot of nuggets in red, blue or green with its word (EXPAND, POWER, COLLECT) on a band across the front.
- **Style:** The big carts reduced to a pot: a rounded bowl with a rim, drawn with the same toy-like volume.
- **Rendering:** Glossy gradients with rim light and a coloured halo.
- **Colour:** Body and halo in the feature's colour, gold load, white lettering with a dark stroke. Measured: #19a9fd 11%, #4ff40c 10%, #f40d10 8%, #f6fbf7 7%.
- **Lighting:** Rim-lit; rings, rays and flares in the feature colour are additive.
- **Ambience:** A small copy of the promise above the reels, landing on the board.
- **Materials:** Enamelled metal, gold, small gems.
- **Variants:** Three colours in one rig, 33 animations: collect, fall, idle and feature states per colour, including jackpot-collect versions.
- **Motion:** Lands with a ring and a burst of rays in its colour; the word plate flashes (a bright 'add' copy of each word is among the parts). Spine 3.8.99 skeleton, 146 bones, 135 slots, 33 animations as the file names them: expand/collect (1.0 s), expand/collect_2 (1.0 s), expand/collect_jp (2.43 s), expand/collect_jp_m_1 (2.43 s), expand/collect_jp_m_2 (2.43 s), collect/collect_value_1 (1.33 s), expand/collect_value_1 (1.37 s), collect/collect_value_2 (1.0 s) and 25 more.
- **Construction:** 133 parts: three pot bodies, front nugget rows, word plates in normal, bright and blurred copies, rings, rays, flares and sparks per colour.
- **Notes:** There is no purple pot here: the Multi feature acts through the multiplier tag instead (see multiplier).
- **Skeleton (from the file):** Spine 3.8.99 · 146 bones · 135 slots · animations: expand/collect (1.0 s), expand/collect_2 (1.0 s), expand/collect_jp (2.43 s), expand/collect_jp_m_1 (2.43 s), expand/collect_jp_m_2 (2.43 s), collect/collect_value_1 (1.33 s), expand/collect_value_1 (1.37 s), collect/collect_value_2 (1.0 s), expand/collect_value_2 (1.0 s), power/collect_value_2 (1.0 s), collect/fall (0.67 s), expand/fall (0.67 s), power/fall (0.67 s), collect/idle (3.0 s), expand/idle (3.0 s), power/idle (3.0 s), expand/idle_2 (3.0 s), power/idle_value (3.0 s), expand/idle_value (3.0 s), collect/idle_value (3.0 s), collect/multi (1.0 s), expand/multi (1.0 s), power/multi (1.0 s), expand/multi_value (1.0 s), collect/multi_value (1.0 s), collect/transform (1.67 s), expand/transform (1.67 s), power/transform_end (0.67 s), power/transform_end2 (0.67 s), power/transform_start (1.0 s), expand/transition (1.0 s), collect/value (0.67 s), power/win (1.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 58% · saturation 74% · contrast 42% · warm 38% / cool 45% · brighter towards: top (21), bottom (3)
- **Palette (measured):** #19a9fd blue 11%, #4ff40c green 10%, #f40d10 red 8%, #f6fbf7 light green 7%, #070c08 black 6%, #fecdc6 light red 4%

### Jackpot symbols: Mini, Minor, Major gems

`sym13_jackpot` · skeleton · 166 parts · largest 200×209 · sheet `sheets/sym13_jackpot.webp`

- **Role:** The three Jackpot symbols; the paytable says they land on all reels and award the Mini, Minor or Major prize, paid only in the Bonus Game.
- **Subject:** A round faceted gem in three colours, green (Mini), blue (Minor) and violet-magenta (Major), each with its word across it (the words are in the symbols sheet).
- **Style:** Stylised cut gem, rounder and fatter than a real stone, with large simple facets.
- **Rendering:** Bright gradients per facet, white edge lines, and an outer glow in the gem's colour.
- **Colour:** Three saturated colours with white highlights: green, cyan-blue, magenta. Measured: #f8fbfc 31%, #0cebfa 6%, #39f132 6%, #f246f7 6%.
- **Lighting:** Lit from inside: facet lines and the halo are additive, and coloured flares cross the stone.
- **Ambience:** The rare prize among the gold: colder and sharper than everything around it.
- **Materials:** Cut crystal with a net of facet lines.
- **Variants:** One rig with mini, minor and major sets, each with collect, collect_jp, fall, idle and multiplier states.
- **Motion:** Read from the motion sheet: on collect the gem flares with rays in its colour and settles back. Spine 3.8.99 skeleton, 120 bones, 103 slots, 36 animations as the file names them: mini/collect (0.73 s), minor/collect (0.73 s), major/collect (0.73 s), major/collect_jp (2.5 s), minor/collect_jp (2.5 s), mini/collect_jp (2.5 s), major/collect_jp_m_1 (2.5 s), mini/collect_jp_m_1 (2.5 s) and 28 more.
- **Construction:** 166 parts: three gem pictures, three facet nets, glows, rays, flares and long glow frame sequences per colour.
- **Notes:** The same three colours, with red, colour-code the four features; see the game reading.
- **Skeleton (from the file):** Spine 3.8.99 · 120 bones · 103 slots · animations: mini/collect (0.73 s), minor/collect (0.73 s), major/collect (0.73 s), major/collect_jp (2.5 s), minor/collect_jp (2.5 s), mini/collect_jp (2.5 s), major/collect_jp_m_1 (2.5 s), mini/collect_jp_m_1 (2.5 s), minor/collect_jp_m_1 (2.5 s), minor/collect_jp_m_2 (2.5 s), mini/collect_jp_m_2 (2.5 s), major/collect_jp_m_2 (2.5 s), major/collect_m (0.73 s), mini/collect_m (0.73 s), minor/collect_m (0.73 s), mini/fall (1.0 s), minor/fall (1.0 s), major/fall (1.0 s), mini/fallbg (1.0 s), minor/fallbg (1.0 s), major/fallbg (1.0 s), mini/idle (3.0 s), minor/idle (3.0 s), major/idle (3.0 s), major/idle_m (3.0 s), mini/idle_m (3.0 s), minor/idle_m (3.0 s), minor/multi (1.0 s), major/multi (1.0 s), mini/multi (1.0 s), mini/multi_m (1.0 s), major/multi_m (1.0 s), minor/multi_m (1.0 s), mini/win (1.0 s), minor/win (1.0 s), major/win (1.0 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 66% · saturation 58% · contrast 46% · warm 13% / cool 60% · brighter towards: bottom (2), bottom-left (1), right (1)
- **Palette (measured):** #f8fbfc light cyan 31%, #0cebfa cyan 6%, #39f132 green 6%, #f246f7 magenta 6%, #ea02ee magenta 5%, #0ca8fb blue 4%

### Low symbol J

`sym2` · skeleton · 14 parts · largest 52×78 · sheet `sheets/sym2.webp`

- **Role:** One of the five low-paying card symbols (10, J, Q, K, A) on the reels; the paytable page lists them together.
- **Subject:** The character J as a dark red, gold-rimmed block letter.
- **Style:** A fat slab-serif capital, extruded and bevelled, standing alone with no tile behind it.
- **Rendering:** Flat-shaded faces with a gradient from red to dark maroon, a thin bright gold rim and a darker extrusion; crisp edges, no texture.
- **Colour:** Dark red and maroon body with a yellow-gold outline; the five royals share one colouring instead of one colour each. Measured: #b32703 23%, #58110b 23%, #fcf314 13%, #190124 10%.
- **Lighting:** Top-lit bevel; a small white star glint and thin light sweeps cross the rim during the win.
- **Ambience:** Quiet and uniform, so the picture symbols and the gold read first.
- **Materials:** Lacquered red enamel inside a polished gold rim.
- **Variants:** A static letter, a gold-outline copy and a plain copy used for the win flash; a blurred copy for spinning reels is in the symbols sheet.
- **Motion:** One win animation: the rim lights in segments (the sweep frame sequences) and a star glint passes. Spine 3.8.99 skeleton, 6 bones, 16 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 14 parts: the letter in three states, a star and five-frame sweep sequences cut to follow the letter's outline.
- **Notes:** All five royals are built the same way, which keeps the low symbols cheap: one treatment, five outlines.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 16 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 40% · saturation 91% · contrast 39% · warm 91% / cool 4% · brighter towards: top (1)
- **Palette (measured):** #b32703 red 23%, #58110b dark red 23%, #fcf314 gold 13%, #190124 black 10%, #e5af10 orange 10%, #fe3101 red 7%

### Lantern symbol

`sym9` · skeleton · 33 parts · largest 120×127 · sheet `sheets/sym9.webp`

- **Role:** A mid-paying picture symbol on the reels (paytable page 1).
- **Subject:** A brass miner's lantern with a lit orange flame, hanging from a chain.
- **Style:** Stylised 3D-look object painting, chunky and slightly toy-like, set on a flat coloured square tile with a thin frame; the object overlaps the tile's edge a little.
- **Rendering:** Smooth gradients, soft painted reflections and small sharp highlights; clean silhouette, no outline.
- **Colour:** The object in warm leather, brass and gold tones on a magenta-purple tile; each mid symbol has its own tile colour, so symbols are told apart by colour before shape. Measured: #fff6f4 20%, #6f0369 16%, #b502a1 14%, #fef2a6 6%.
- **Lighting:** Lit from the top-left with a warm rim; a small glint star and a light sweep are separate additive parts.
- **Ambience:** Friendly prospecting gear, clean and new-looking instead of worn.
- **Materials:** Brass, glass, flame.
- **Variants:** A static copy and a motion-blurred copy in the symbols sheet; one win animation.
- **Motion:** One win animation of 1 s: the object lifts and tilts slightly while a sweep crosses it (read from the motion sheet). Spine 3.8.99 skeleton, 15 bones, 12 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 33 parts: tile background and frame, the object in a few pieces, shadow, star and sweep frame sequences.
- **Skeleton (from the file):** Spine 3.8.99 · 15 bones · 12 slots · animations: win (1.0 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, strong highlights · brightness 55% · saturation 60% · contrast 47% · warm 75% / cool 3%
- **Palette (measured):** #fff6f4 light red 20%, #6f0369 dark magenta 16%, #b502a1 magenta 14%, #fef2a6 light gold 6%, #fef065 gold 5%, #f37011 orange 4%

### Bonus symbol: gold nugget

`sym13_gold` · skeleton · 46 parts · largest 219×217 · sheet `sheets/sym13_gold.webp`

- **Role:** The Bonus symbol. The paytable says it lands on all reels and awards 1x to 5x the total bet, paid only in the Bonus Game; in play its value is written across it.
- **Subject:** A round, lumpy gold nugget with a bright rim.
- **Style:** Stylised, almost coin-like: a nugget simplified to a disc with soft facets so that a number reads on it.
- **Rendering:** Glossy gradients, a white-hot rim and a broad soft glow.
- **Colour:** Yellow gold with orange shadows. Measured: #fffe93 38%, #fb990a 20%, #feb93b 12%, #fee54f 9%.
- **Lighting:** Self-lit: the rim and a round glow behind are additive.
- **Ambience:** The unit of treasure; calm until collected.
- **Materials:** Polished gold.
- **Variants:** Collect, fall, fall_bg, idle and multi animations; values are drawn over it with the symbol_bit font.
- **Motion:** Falls in with a flash and a star; pulses when a multiplier lands on it; shrinks into a light when collected (animation names; frames read from the motion sheet). Spine 3.8.99 skeleton, 53 bones, 53 slots, 6 animations as the file names them: collect (0.73 s), fall (1.0 s), fall_bg (1.0 s), idle (3.0 s), multi (1.0 s), win (1.0 s).
- **Construction:** 46 parts: one nugget picture, glow discs, rays, particle and glow frame sequences.
- **Notes:** The same nugget is the pile in every cart, so symbol, cart load and coin share one gold.
- **Skeleton (from the file):** Spine 3.8.99 · 53 bones · 53 slots · animations: collect (0.73 s), fall (1.0 s), fall_bg (1.0 s), idle (3.0 s), multi (1.0 s), win (1.0 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 81% · saturation 62% · contrast 35% · warm 96% / cool 0% · brighter towards: top (1), top-right (1)
- **Palette (measured):** #fffe93 light gold 38%, #fb990a orange 20%, #feb93b orange 12%, #fee54f gold 9%, #fffffc light gold 8%, #c74d02 orange 7%

### Wild: the miner

`sym12` · skeleton · 67 parts · largest 194×210 · sheet `sheets/sym12.webp`

- **Role:** The Wild symbol; the paytable says it lands on reels 2 to 5 and substitutes for all but Bonus and Jackpot symbols. In the game screens it stacks down a reel.
- **Subject:** The head of a laughing, red-bearded miner in a red helmet with a lit lamp, wrapped in a ring of fire-like gold glow. He is the only human figure in the game.
- **Style:** Stylised 3D-look cartoon portrait, round and jolly, with big cheeks and a sculpted beard in large locks.
- **Rendering:** Smooth gradients with a hot rim light all round the silhouette; no outline, no tile.
- **Colour:** Orange-red beard and helmet inside a yellow-gold halo. Measured: #fcc335 25%, #fffff9 18%, #fbee89 17%, #4e0e05 15%.
- **Lighting:** Lit by his own lamp and by the glow behind him; the halo, lamp flare and sparks are additive layers.
- **Ambience:** Warm and welcoming, a host figure.
- **Materials:** Sculpted hair, painted helmet metal, glass lamp, fire-like glow.
- **Variants:** Fall, idle and win animations; a blurred copy for spinning reels.
- **Motion:** Read from the motion sheet: on landing a burst flashes behind the head; in idle the face moves a little (brows, moustache, eyes are separate parts); the win throws sparks and a ring of rays. Spine 3.8.99 skeleton, 85 bones, 71 slots, 3 animations as the file names them: fall (0.67 s), idle (3.0 s), win (1.0 s).
- **Construction:** 67 parts: the head, helmet, moustache halves, hair strands, brows, eyes and pupils, teeth and mouth as separate pieces, plus glow shapes, a noise frame sequence for the fire edge and spark sequences.
- **Notes:** With the donkey, the only symbol built as a face rig; everything else is an object.
- **Skeleton (from the file):** Spine 3.8.99 · 85 bones · 71 slots · animations: fall (0.67 s), idle (3.0 s), win (1.0 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 64% · saturation 64% · contrast 52% · warm 100% / cool 0% · brighter towards: bottom (1)
- **Palette (measured):** #fcc335 orange 25%, #fffff9 light gold 18%, #fbee89 light gold 17%, #4e0e05 dark red 15%, #982d08 brown 9%

### Low symbol Q

`sym3` · skeleton · 14 parts · largest 140×106 · sheet `sheets/sym3.webp`

- **Role:** One of the five low-paying card symbols (10, J, Q, K, A) on the reels; the paytable page lists them together.
- **Subject:** The character Q as a dark red, gold-rimmed block letter.
- **Style:** A fat slab-serif capital, extruded and bevelled, standing alone with no tile behind it.
- **Rendering:** Flat-shaded faces with a gradient from red to dark maroon, a thin bright gold rim and a darker extrusion; crisp edges, no texture.
- **Colour:** Dark red and maroon body with a yellow-gold outline; the five royals share one colouring instead of one colour each. Measured: #601702 39%, #b13403 19%, #fef019 8%, #f84802 6%.
- **Lighting:** Top-lit bevel; a small white star glint and thin light sweeps cross the rim during the win.
- **Ambience:** Quiet and uniform, so the picture symbols and the gold read first.
- **Materials:** Lacquered red enamel inside a polished gold rim.
- **Variants:** A static letter, a gold-outline copy and a plain copy used for the win flash; a blurred copy for spinning reels is in the symbols sheet.
- **Motion:** One win animation: the rim lights in segments (the sweep frame sequences) and a star glint passes. Spine 3.8.99 skeleton, 6 bones, 16 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 14 parts: the letter in three states, a star and five-frame sweep sequences cut to follow the letter's outline.
- **Notes:** All five royals are built the same way, which keeps the low symbols cheap: one treatment, five outlines.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 16 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 38% · saturation 92% · contrast 73% · warm 99% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #601702 dark red 39%, #b13403 brown 19%, #fef019 gold 8%, #f84802 orange 6%, #140002 black 4%

### Helmet symbol

`sym10` · skeleton · 29 parts · largest 149×158 · sheet `sheets/sym10.webp`

- **Role:** A mid-paying picture symbol on the reels (paytable page 1).
- **Subject:** A green miner's helmet with an orange brim band and a lit head lamp.
- **Style:** Stylised 3D-look object painting, chunky and slightly toy-like, set on a flat coloured square tile with a thin frame; the object overlaps the tile's edge a little.
- **Rendering:** Smooth gradients, soft painted reflections and small sharp highlights; clean silhouette, no outline.
- **Colour:** The object in warm leather, brass and gold tones on a green tile; each mid symbol has its own tile colour, so symbols are told apart by colour before shape. Measured: #f8fa11 23%, #2a7706 15%, #1a2c0d 12%, #599a10 8%.
- **Lighting:** Lit from the top-left with a warm rim; a small glint star and a light sweep are separate additive parts.
- **Ambience:** Friendly prospecting gear, clean and new-looking instead of worn.
- **Materials:** Painted metal, leather band, glass lamp.
- **Variants:** A static copy and a motion-blurred copy in the symbols sheet; one win animation.
- **Motion:** One win animation of 1 s: the object lifts and tilts slightly while a sweep crosses it (read from the motion sheet). Spine 3.8.99 skeleton, 9 bones, 7 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 29 parts: tile background and frame, the object in a few pieces, shadow, star and sweep frame sequences.
- **Skeleton (from the file):** Spine 3.8.99 · 9 bones · 7 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 59% · saturation 82% · contrast 59% · warm 58% / cool 21% · brighter towards: top-right (20)
- **Palette (measured):** #f8fa11 gold 23%, #2a7706 dark green 15%, #1a2c0d black 12%, #599a10 green 8%, #fb6809 orange 8%, #fdf959 gold 4%

### Satchel symbol

`sym8` · skeleton · 42 parts · largest 120×127 · sheet `sheets/sym8.webp`

- **Role:** A mid-paying picture symbol on the reels (paytable page 1).
- **Subject:** A blue leather satchel with tan straps and a brass buckle, a few gold nuggets spilling from it.
- **Style:** Stylised 3D-look object painting, chunky and slightly toy-like, set on a flat coloured square tile with a thin frame; the object overlaps the tile's edge a little.
- **Rendering:** Smooth gradients, soft painted reflections and small sharp highlights; clean silhouette, no outline.
- **Colour:** The object in warm leather, brass and gold tones on a blue tile; each mid symbol has its own tile colour, so symbols are told apart by colour before shape. Measured: #0751ae 23%, #1e1832 12%, #f1fdfb 11%, #3f80ee 8%.
- **Lighting:** Lit from the top-left with a warm rim; a small glint star and a light sweep are separate additive parts.
- **Ambience:** Friendly prospecting gear, clean and new-looking instead of worn.
- **Materials:** Dyed leather, brass, gold.
- **Variants:** A static copy and a motion-blurred copy in the symbols sheet; one win animation.
- **Motion:** One win animation of 1 s: the object lifts and tilts slightly while a sweep crosses it (read from the motion sheet). Spine 3.8.99 skeleton, 27 bones, 21 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 42 parts: tile background and frame, the object in a few pieces, shadow, star and sweep frame sequences.
- **Skeleton (from the file):** Spine 3.8.99 · 27 bones · 21 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, cool, medium contrast, strong highlights · brightness 49% · saturation 65% · contrast 57% · warm 22% / cool 76% · brighter towards: top-right (18), top-left (1)
- **Palette (measured):** #0751ae blue 23%, #1e1832 dark blue 12%, #f1fdfb light cyan 11%, #3f80ee blue 8%, #14326d dark blue 6%, #51e9fe cyan 5%

### Low symbol A

`sym5` · skeleton · 14 parts · largest 140×106 · sheet `sheets/sym5.webp`

- **Role:** One of the five low-paying card symbols (10, J, Q, K, A) on the reels; the paytable page lists them together.
- **Subject:** The character A as a dark red, gold-rimmed block letter.
- **Style:** A fat slab-serif capital, extruded and bevelled, standing alone with no tile behind it.
- **Rendering:** Flat-shaded faces with a gradient from red to dark maroon, a thin bright gold rim and a darker extrusion; crisp edges, no texture.
- **Colour:** Dark red and maroon body with a yellow-gold outline; the five royals share one colouring instead of one colour each. Measured: #5d0e06 41%, #f7de16 14%, #a32704 14%, #e72c01 13%.
- **Lighting:** Top-lit bevel; a small white star glint and thin light sweeps cross the rim during the win.
- **Ambience:** Quiet and uniform, so the picture symbols and the gold read first.
- **Materials:** Lacquered red enamel inside a polished gold rim.
- **Variants:** A static letter, a gold-outline copy and a plain copy used for the win flash; a blurred copy for spinning reels is in the symbols sheet.
- **Motion:** One win animation: the rim lights in segments (the sweep frame sequences) and a star glint passes. Spine 3.8.99 skeleton, 6 bones, 16 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 14 parts: the letter in three states, a star and five-frame sweep sequences cut to follow the letter's outline.
- **Notes:** All five royals are built the same way, which keeps the low symbols cheap: one treatment, five outlines.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 16 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 36% · saturation 93% · contrast 55% · warm 98% / cool 0% · brighter towards: left (1), top (1)
- **Palette (measured):** #5d0e06 dark red 41%, #f7de16 gold 14%, #a32704 red 14%, #e72c01 red 13%, #d5820f orange 11%, #fdfb4d gold 4%

### Pickaxe symbol

`sym7` · skeleton · 12 parts · largest 138×106 · sheet `sheets/sym7.webp`

- **Role:** A lower picture symbol on the reels (paytable page 1, pays with the gold pan).
- **Subject:** A pickaxe with a steel head and a rope-wrapped wooden handle, set diagonally.
- **Style:** Stylised 3D-look object painting, chunky and slightly toy-like, set on a flat coloured square tile with a thin frame; the object overlaps the tile's edge a little.
- **Rendering:** Smooth gradients, soft painted reflections and small sharp highlights; clean silhouette, no outline.
- **Colour:** The object in warm leather, brass and gold tones on a soft red-orange glow patch with no hard tile tile; each mid symbol has its own tile colour, so symbols are told apart by colour before shape. Measured: #952d0b 47%, #fffaf9 7%, #6a3b5c 6%, #fdec0e 6%.
- **Lighting:** Lit from the top-left with a warm rim; a small glint star and a light sweep are separate additive parts.
- **Ambience:** Friendly prospecting gear, clean and new-looking instead of worn.
- **Materials:** Steel, wood, rope.
- **Variants:** A static copy and a motion-blurred copy in the symbols sheet; one win animation.
- **Motion:** One win animation of 1 s: the object lifts and tilts slightly while a sweep crosses it (read from the motion sheet). Spine 3.8.99 skeleton, 13 bones, 15 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 12 parts: tile background and frame, the object in a few pieces, shadow, star and sweep frame sequences.
- **Skeleton (from the file):** Spine 3.8.99 · 13 bones · 15 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 44% · saturation 74% · contrast 46% · warm 87% / cool 8% · brighter towards: top-right (1)
- **Palette (measured):** #952d0b red 47%, #fffaf9 light red 7%, #6a3b5c magenta 6%, #fdec0e gold 6%, #c96521 orange 6%, #f9b278 orange 6%

### Low symbol 10

`sym1` · skeleton · 14 parts · largest 140×106 · sheet `sheets/sym1.webp`

- **Role:** One of the five low-paying card symbols (10, J, Q, K, A) on the reels; the paytable page lists them together.
- **Subject:** The character 10 as a dark red, gold-rimmed block letter.
- **Style:** A fat slab-serif capital, extruded and bevelled, standing alone with no tile behind it.
- **Rendering:** Flat-shaded faces with a gradient from red to dark maroon, a thin bright gold rim and a darker extrusion; crisp edges, no texture.
- **Colour:** Dark red and maroon body with a yellow-gold outline; the five royals share one colouring instead of one colour each. Measured: #5e1006 40%, #a72801 19%, #e4a10c 11%, #fdee13 10%.
- **Lighting:** Top-lit bevel; a small white star glint and thin light sweeps cross the rim during the win.
- **Ambience:** Quiet and uniform, so the picture symbols and the gold read first.
- **Materials:** Lacquered red enamel inside a polished gold rim.
- **Variants:** A static letter, a gold-outline copy and a plain copy used for the win flash; a blurred copy for spinning reels is in the symbols sheet.
- **Motion:** One win animation: the rim lights in segments (the sweep frame sequences) and a star glint passes. Spine 3.8.99 skeleton, 6 bones, 16 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 14 parts: the letter in three states, a star and five-frame sweep sequences cut to follow the letter's outline.
- **Notes:** All five royals are built the same way, which keeps the low symbols cheap: one treatment, five outlines.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 16 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 34% · saturation 90% · contrast 56% · warm 98% / cool 0% · brighter towards: top (3), bottom-left (1), top-right (1)
- **Palette (measured):** #5e1006 dark red 40%, #a72801 red 19%, #e4a10c orange 11%, #fdee13 gold 10%, #060006 black 7%, #d15603 orange 6%

### Donkey symbol

`sym11` · skeleton · 21 parts · largest 141×107 · sheet `sheets/sym11.webp`

- **Role:** The highest-paying regular symbol (paytable page 1: the only one that pays for two of a kind).
- **Subject:** The head of a grinning cartoon donkey with big teeth, turned three-quarters.
- **Style:** Stylised 3D-look object painting, chunky and slightly toy-like, set on a flat coloured square tile with a thin frame; the object overlaps the tile's edge a little.
- **Rendering:** Smooth gradients, soft painted reflections and small sharp highlights; clean silhouette, no outline.
- **Colour:** The object in warm leather, brass and gold tones on a red-orange tile; each mid symbol has its own tile colour, so symbols are told apart by colour before shape. Measured: #fbce54 19%, #991007 16%, #fcf1ab 14%, #e92407 14%.
- **Lighting:** Lit from the top-left with a warm rim; a small glint star and a light sweep are separate additive parts.
- **Ambience:** The comic relief of the set: the one face that jokes.
- **Materials:** Short fur, soft ears; a cartoon face with moving eyes.
- **Variants:** A static copy and a motion-blurred copy in the symbols sheet; one win animation.
- **Motion:** One win animation of 1 s: the object lifts and tilts slightly while a sweep crosses it (read from the motion sheet). Spine 3.8.99 skeleton, 24 bones, 22 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 21 parts: tile background and frame, the object in a few pieces, shadow, star and sweep frame sequences. The head is cut into ears, jaw, nose, crest, eyes and pupils, so the face can move.
- **Skeleton (from the file):** Spine 3.8.99 · 24 bones · 22 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 52% · saturation 76% · contrast 71% · warm 99% / cool 0% · brighter towards: top-right (2), left (1)
- **Palette (measured):** #fbce54 orange 19%, #991007 red 16%, #fcf1ab light gold 14%, #e92407 red 14%, #f78f11 orange 12%, #480a09 dark red 10%

### Low symbol K

`sym4` · skeleton · 14 parts · largest 140×106 · sheet `sheets/sym4.webp`

- **Role:** One of the five low-paying card symbols (10, J, Q, K, A) on the reels; the paytable page lists them together.
- **Subject:** The character K as a dark red, gold-rimmed block letter.
- **Style:** A fat slab-serif capital, extruded and bevelled, standing alone with no tile behind it.
- **Rendering:** Flat-shaded faces with a gradient from red to dark maroon, a thin bright gold rim and a darker extrusion; crisp edges, no texture.
- **Colour:** Dark red and maroon body with a yellow-gold outline; the five royals share one colouring instead of one colour each. Measured: #5d1105 41%, #b42c02 18%, #fdf113 11%, #e7a40c 9%.
- **Lighting:** Top-lit bevel; a small white star glint and thin light sweeps cross the rim during the win.
- **Ambience:** Quiet and uniform, so the picture symbols and the gold read first.
- **Materials:** Lacquered red enamel inside a polished gold rim.
- **Variants:** A static letter, a gold-outline copy and a plain copy used for the win flash; a blurred copy for spinning reels is in the symbols sheet.
- **Motion:** One win animation: the rim lights in segments (the sweep frame sequences) and a star glint passes. Spine 3.8.99 skeleton, 6 bones, 16 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 14 parts: the letter in three states, a star and five-frame sweep sequences cut to follow the letter's outline.
- **Notes:** All five royals are built the same way, which keeps the low symbols cheap: one treatment, five outlines.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 16 slots · animations: win (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 38% · saturation 93% · contrast 58% · warm 98% / cool 0% · brighter towards: top (2)
- **Palette (measured):** #5d1105 dark red 41%, #b42c02 red 18%, #fdf113 gold 11%, #e7a40c orange 9%, #fd2d01 red 6%, #e17104 orange 5%

### Gold pan symbol

`sym6` · skeleton · 30 parts · largest 138×106 · sheet `sheets/sym6.webp`

- **Role:** A lower picture symbol on the reels (paytable page 1, pays with the pickaxe).
- **Subject:** A steel prospector's pan seen from above at an angle, with small gold stones in it.
- **Style:** Stylised 3D-look object painting, chunky and slightly toy-like, set on a flat coloured square tile with a thin frame; the object overlaps the tile's edge a little.
- **Rendering:** Smooth gradients, soft painted reflections and small sharp highlights; clean silhouette, no outline.
- **Colour:** The object in warm leather, brass and gold tones on a soft red-orange blur with no hard tile (the pan and the pickaxe have a glow patch instead of a framed tile) tile; each mid symbol has its own tile colour, so symbols are told apart by colour before shape. Measured: #982e09 30%, #f7a33a 10%, #392d2c 10%, #fefbf5 9%.
- **Lighting:** Lit from the top-left with a warm rim; a small glint star and a light sweep are separate additive parts.
- **Ambience:** Friendly prospecting gear, clean and new-looking instead of worn.
- **Materials:** Brushed steel, gold grains, a few dark stones.
- **Variants:** A static copy and a motion-blurred copy in the symbols sheet; one win animation.
- **Motion:** One win animation of 1 s: the object lifts and tilts slightly while a sweep crosses it (read from the motion sheet). Spine 3.8.99 skeleton, 35 bones, 35 slots, 1 animations as the file names them: win (1.0 s).
- **Construction:** 30 parts: tile background and frame, the object in a few pieces, shadow, star and sweep frame sequences.
- **Skeleton (from the file):** Spine 3.8.99 · 35 bones · 35 slots · animations: win (1.0 s)
- **Measured:** mid-tone, saturated, warm, medium contrast, strong highlights · brightness 48% · saturation 57% · contrast 48% · warm 89% / cool 7% · brighter towards: bottom-left (1), top-right (1), top (1)
- **Palette (measured):** #982e09 brown 30%, #f7a33a orange 10%, #392d2c dark red 10%, #fefbf5 light orange 9%, #655862 grey 6%, #0c0706 black 6%

### Multiplier marker

`multiplier` · skeleton · 8 parts · largest 301×302 · sheet `sheets/multiplier.webp`

- **Role:** The mark of the Multi feature on a symbol; the paytable shows x2, x3 and x5 tags placed on symbols.
- **Subject:** A white cart-shaped stroke, a magenta glow in the same shape, a gold ring, a star flash and particles. The number itself is drawn with the multi_bit font.
- **Style:** Effect shapes only.
- **Rendering:** Soft glows and thin bright lines.
- **Colour:** Magenta with orange and white. Measured: #e900f6 47%, #ffa10e 24%, #fffffe 20%, #ffe00d 7%.
- **Lighting:** All emissive.
- **Ambience:** A quick magic stamp.
- **Materials:** Light.
- **Variants:** Animations empty_cell, idle, loop, multiplier, start.
- **Motion:** Spine 3.8.99 skeleton, 36 bones, 21 slots, 6 animations as the file names them: empty_cell (1.13 s), idle (0.0 s), loop (0.0 s), multiplier (0.5 s), start (1.33 s), start2 (0.67 s).
- **Construction:** 8 parts; the drawn frame shows only a placeholder point because the number is put in by the game.
- **Notes:** The frame this tool drew for the unit is empty apart from the placeholder: the reading is from the parts.
- **Skeleton (from the file):** Spine 3.8.99 · 36 bones · 21 slots · animations: empty_cell (1.13 s), idle (0.0 s), loop (0.0 s), multiplier (0.5 s), start (1.33 s), start2 (0.67 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 56% · saturation 78% · contrast 11% · warm 58% / cool 0%
- **Palette (measured):** #e900f6 magenta 47%, #ffa10e orange 24%, #fffffe light gold 20%, #ffe00d gold 7%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Green cart (Collect feature)

`green_cart` · skeleton · 163 parts · largest 262×158 · sheet `sheets/green_cart.webp`

- **Role:** One of the four large carts that stand in a row above the reel board in the base game (seen in the game screens); the Collect label under it lights when the feature is in play. The rig's level names (lvl_0 to lvl_9) say the heap grows in ten steps; in the bonus the active carts stand gold at the left of the board (seen in the bonus screens).
- **Subject:** A green metal mine cart with a glowing lamp, heaped with gold nuggets and green emeralds. The same rig holds an all-gold version of the cart (parts named gold/…), which is what the bonus screens show.
- **Style:** Stylised 3D-look toy mine cart: a short, wide tub on two small wheels with a round lamp on its front, drawn chunky and rounded, under a heap of faceted nuggets taller than the cart itself.
- **Rendering:** Smooth render-like gradients with hard, clean edges and no outline; every plane has a bright rim, and a white-to-colour halo is drawn as its own soft layers behind the cart.
- **Colour:** Green body against yellow-gold nuggets with white highlights; the halo repeats the body colour. Measured: #f8e60f 21%, #fefef7 21%, #f38107 13%, #058228 7%.
- **Lighting:** Lit from the top and top-left with strong specular highlights on metal and nuggets; the lamp and the halo are emissive and sit on additive slots.
- **Ambience:** A treasure about to spill: loud, glossy and inviting, the game's main promise shown as an object.
- **Materials:** Painted, riveted metal with a glossy enamel finish, polished gold nuggets, cut green emeralds, a glass lamp.
- **Variants:** Ten fill levels (idle, win and impact for each, lvl_up between them), a pending and a trigger state at level 9, and a gold 'bg' version for the bonus game. The four carts share one construction and differ in body colour, gem and a few effect parts.
- **Motion:** Read from the motion sheet: in idle the heap and lamp shimmer and light sweeps pass; win flashes the whole cart in its colour; impact squashes the cart as a prize lands and the heap grows a step. Spine 3.8.99 skeleton, 217 bones, 223 slots, 46 animations as the file names them: idle_bg (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s), lvl_up/lvl_1_to_2 (1.33 s) and 38 more.
- **Construction:** A Spine rig of many small parts: the tub in pieces (trunk, bands, wheels, lamp), nuggets and gems as separate sprites added level by level, frame sequences for flashes, light sweeps and glow, and soft glow shapes on additive slots.
- **Notes:** The game has no figure character on stage; these four carts take that place, which is why they are sorted under Characters here (a sorting decision of this run). Largest single part 262x158 px or smaller: the cart is built small and never shipped as one picture.
- **Skeleton (from the file):** Spine 3.8.99 · 217 bones · 223 slots · animations: idle_bg (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s), lvl_up/lvl_1_to_2 (1.33 s), idle/lvl_2 (5.33 s), win/lvl_2 (2.67 s), impact/lvl_2 (2.67 s), lvl_up/lvl_2_to_3 (1.33 s), idle/lvl_3 (5.33 s), win/lvl_3 (2.67 s), impact/lvl_3 (2.67 s), lvl_up/lvl_3_to_4 (1.33 s), idle/lvl_4 (5.33 s), win/lvl_4 (2.67 s), impact/lvl_4 (2.67 s), lvl_up/lvl_4_to_5 (1.33 s), idle/lvl_5 (5.33 s), win/lvl_5 (2.67 s), impact/lvl_5_impact_1 (2.67 s), impact/lvl_5_impact_2 (1.33 s), lvl_up/lvl_5_to_6 (1.33 s), impact/lvl_6 (2.67 s), idle/lvl_6 (5.33 s), win/lvl_6 (2.67 s), lvl_up/lvl_6_to_7 (1.33 s), win/lvl_7 (2.67 s), idle/lvl_7 (5.33 s), impact/lvl_7_impact_1 (2.67 s), impact/lvl_7_impact_2 (1.33 s), lvl_up/lvl_7_to_8 (1.33 s), win/lvl_8 (2.67 s), idle/lvl_8 (5.33 s), impact/lvl_8_impact_1 (2.67 s), impact/lvl_8_impact_2 (1.33 s), lvl_up/lvl_8_to_9 (1.33 s), idle/lvl_9 (4.0 s), win/lvl_9 (1.67 s), lvl_9_pending (4.0 s), lvl_9_pending_bg (4.0 s), lvl_9_trigger (3.37 s), lvl_up/lvl_0_to_1 (1.33 s), win_bg (1.67 s)
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 73% · saturation 69% · contrast 46% · warm 61% / cool 19% · brighter towards: top (10), top-left (7), top-right (4)
- **Palette (measured):** #f8e60f gold 21%, #fefef7 light gold 21%, #f38107 orange 13%, #058228 dark green 7%, #f7f159 gold 4%, #f7b914 orange 4%

### Red cart (Expand feature)

`red_cart` · skeleton · 191 parts · largest 191×286 · sheet `sheets/red_cart.webp`

- **Role:** One of the four large carts that stand in a row above the reel board in the base game (seen in the game screens); the Expand label under it lights when the feature is in play. The rig's level names (lvl_0 to lvl_9) say the heap grows in ten steps; in the bonus the active carts stand gold at the left of the board (seen in the bonus screens).
- **Subject:** A red metal mine cart with a glowing lamp, heaped with gold nuggets and red gems. The same rig holds an all-gold version of the cart (parts named gold/…), which is what the bonus screens show.
- **Style:** Stylised 3D-look toy mine cart: a short, wide tub on two small wheels with a round lamp on its front, drawn chunky and rounded, under a heap of faceted nuggets taller than the cart itself.
- **Rendering:** Smooth render-like gradients with hard, clean edges and no outline; every plane has a bright rim, and a white-to-colour halo is drawn as its own soft layers behind the cart.
- **Colour:** Red body against yellow-gold nuggets with white highlights; the halo repeats the body colour. Measured: #fefef6 23%, #fbd30d 22%, #f68104 12%, #d74b0e 10%.
- **Lighting:** Lit from the top and top-left with strong specular highlights on metal and nuggets; the lamp and the halo are emissive and sit on additive slots.
- **Ambience:** A treasure about to spill: loud, glossy and inviting, the game's main promise shown as an object.
- **Materials:** Painted, riveted metal with a glossy enamel finish, polished gold nuggets, cut red gems, a glass lamp.
- **Variants:** Ten fill levels (idle, win and impact for each, lvl_up between them), a pending and a trigger state at level 9, and a gold 'bg' version for the bonus game. The four carts share one construction and differ in body colour, gem and a few effect parts.
- **Motion:** Read from the motion sheet: in idle the heap and lamp shimmer and light sweeps pass; win flashes the whole cart in its colour; impact squashes the cart as a prize lands and the heap grows a step. Spine 3.8.99 skeleton, 242 bones, 276 slots, 49 animations as the file names them: idle_bg (4.0 s), idle_bg2 (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s) and 41 more.
- **Construction:** A Spine rig of many small parts: the tub in pieces (trunk, bands, wheels, lamp), nuggets and gems as separate sprites added level by level, frame sequences for flashes, light sweeps and glow, and soft glow shapes on additive slots. This rig also carries a second gold set (idle_bg2, win_bg2) not present in the green and blue rigs.
- **Notes:** The game has no figure character on stage; these four carts take that place, which is why they are sorted under Characters here (a sorting decision of this run). Largest single part 262x158 px or smaller: the cart is built small and never shipped as one picture.
- **Skeleton (from the file):** Spine 3.8.99 · 242 bones · 276 slots · animations: idle_bg (4.0 s), idle_bg2 (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s), lvl_up/lvl_1_to_2 (1.33 s), idle/lvl_2 (5.33 s), win/lvl_2 (2.67 s), impact/lvl_2 (2.67 s), lvl_up/lvl_2_to_3 (1.33 s), idle/lvl_3 (5.33 s), win/lvl_3 (2.67 s), impact/lvl_3 (2.67 s), lvl_up/lvl_3_to_4 (1.33 s), idle/lvl_4 (5.33 s), win/lvl_4 (2.67 s), impact/lvl_4 (2.67 s), lvl_up/lvl_4_to_5 (1.33 s), idle/lvl_5 (5.33 s), win/lvl_5 (2.67 s), impact/lvl_5_impact_1 (2.67 s), impact/lvl_5_impact_2 (1.67 s), lvl_up/lvl_5_to_6 (1.33 s), impact/lvl_6 (2.67 s), idle/lvl_6 (5.33 s), win/lvl_6 (2.67 s), lvl_up/lvl_6_to_7 (1.33 s), win/lvl_7 (2.67 s), idle/lvl_7 (5.33 s), impact/lvl_7_impact_1 (2.67 s), impact/lvl_7_impact_2 (1.33 s), lvl_up/lvl_7_to_8 (1.33 s), win/lvl_8 (2.67 s), idle/lvl_8 (5.33 s), impact/lvl_8_impact_1 (2.67 s), impact/lvl_8_impact_2 (1.33 s), lvl_up/lvl_8_to_9 (1.33 s), idle/lvl_9 (4.0 s), win/lvl_9 (1.47 s), lvl_9_pending (4.0 s), lvl_9_pending_bg (4.0 s), lvl_9_pending_bg2 (4.0 s), lvl_9_trigger (3.33 s), lvl_up/lvl_0_to_1 (1.33 s), win_bg (1.67 s), win_bg2 (1.67 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 67% · saturation 67% · contrast 49% · warm 98% / cool 0% · brighter towards: top-left (25), left (14), top (5)
- **Palette (measured):** #fefef6 light gold 23%, #fbd30d gold 22%, #f68104 orange 12%, #d74b0e orange 10%, #f61d13 red 6%, #fdf9a7 light gold 5%

### Violet cart (Multi feature)

`violet_cart` · skeleton · 216 parts · largest 262×158 · sheet `sheets/violet_cart.webp`

- **Role:** One of the four large carts that stand in a row above the reel board in the base game (seen in the game screens); the Multi label under it lights when the feature is in play. The rig's level names (lvl_0 to lvl_9) say the heap grows in ten steps; in the bonus the active carts stand gold at the left of the board (seen in the bonus screens).
- **Subject:** A violet metal mine cart with a glowing lamp, heaped with gold nuggets and violet crystals. The same rig holds an all-gold version of the cart (parts named gold/…), which is what the bonus screens show.
- **Style:** Stylised 3D-look toy mine cart: a short, wide tub on two small wheels with a round lamp on its front, drawn chunky and rounded, under a heap of faceted nuggets taller than the cart itself.
- **Rendering:** Smooth render-like gradients with hard, clean edges and no outline; every plane has a bright rim, and a white-to-colour halo is drawn as its own soft layers behind the cart.
- **Colour:** Violet body against yellow-gold nuggets with white highlights; the halo repeats the body colour. Measured: #fefbf7 23%, #fbd40d 22%, #f17a04 14%, #c04409 6%.
- **Lighting:** Lit from the top and top-left with strong specular highlights on metal and nuggets; the lamp and the halo are emissive and sit on additive slots.
- **Ambience:** A treasure about to spill: loud, glossy and inviting, the game's main promise shown as an object.
- **Materials:** Painted, riveted metal with a glossy enamel finish, polished gold nuggets, cut violet crystals, a glass lamp.
- **Variants:** Ten fill levels (idle, win and impact for each, lvl_up between them), a pending and a trigger state at level 9, and a gold 'bg' version for the bonus game. The four carts share one construction and differ in body colour, gem and a few effect parts.
- **Motion:** Read from the motion sheet: in idle the heap and lamp shimmer and light sweeps pass; win flashes the whole cart in its colour; impact squashes the cart as a prize lands and the heap grows a step. Spine 3.8.99 skeleton, 269 bones, 304 slots, 49 animations as the file names them: idle_bg (4.0 s), idle_bg2 (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s) and 41 more.
- **Construction:** A Spine rig of many small parts: the tub in pieces (trunk, bands, wheels, lamp), nuggets and gems as separate sprites added level by level, frame sequences for flashes, light sweeps and glow, and soft glow shapes on additive slots. Like the red rig it has the second gold set.
- **Notes:** The game has no figure character on stage; these four carts take that place, which is why they are sorted under Characters here (a sorting decision of this run). Largest single part 262x158 px or smaller: the cart is built small and never shipped as one picture.
- **Skeleton (from the file):** Spine 3.8.99 · 269 bones · 304 slots · animations: idle_bg (4.0 s), idle_bg2 (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s), lvl_up/lvl_1_to_2 (1.33 s), idle/lvl_2 (5.33 s), win/lvl_2 (2.67 s), impact/lvl_2 (2.67 s), lvl_up/lvl_2_to_3 (1.33 s), idle/lvl_3 (5.33 s), win/lvl_3 (2.67 s), impact/lvl_3 (2.67 s), lvl_up/lvl_3_to_4 (1.33 s), idle/lvl_4 (5.33 s), win/lvl_4 (2.67 s), impact/lvl_4 (2.67 s), lvl_up/lvl_4_to_5 (1.33 s), idle/lvl_5 (5.33 s), win/lvl_5 (2.67 s), impact/lvl_5_impact_1 (2.67 s), impact/lvl_5_impact_2 (1.33 s), lvl_up/lvl_5_to_6 (1.33 s), impact/lvl_6 (2.67 s), idle/lvl_6 (5.33 s), win/lvl_6 (2.67 s), lvl_up/lvl_6_to_7 (1.33 s), win/lvl_7 (2.67 s), idle/lvl_7 (5.33 s), impact/lvl_7_impact_1 (2.67 s), impact/lvl_7_impact_2 (1.33 s), lvl_up/lvl_7_to_8 (1.33 s), win/lvl_8 (2.67 s), idle/lvl_8 (5.33 s), impact/lvl_8_impact_1 (2.67 s), impact/lvl_8_impact_2 (1.33 s), lvl_up/lvl_8_to_9 (1.33 s), idle/lvl_9 (4.0 s), win/lvl_9 (1.67 s), lvl_9_pending (4.0 s), lvl_9_pending_bg (4.0 s), lvl_9_pending_bg2 (4.0 s), lvl_9_trigger (3.33 s), lvl_up/lvl_0_to_1 (1.33 s), win_bg (1.67 s), win_bg2 (1.67 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 66% · saturation 67% · contrast 51% · warm 74% / cool 12% · brighter towards: top-left (28), left (17), top (6)
- **Palette (measured):** #fefbf7 light orange 23%, #fbd40d gold 22%, #f17a04 orange 14%, #c04409 orange 6%, #f220fe magenta 5%, #870cd4 purple 4%

### Blue cart (Power feature)

`blue_cart` · skeleton · 163 parts · largest 262×158 · sheet `sheets/blue_cart.webp`

- **Role:** One of the four large carts that stand in a row above the reel board in the base game (seen in the game screens); the Power label under it lights when the feature is in play. The rig's level names (lvl_0 to lvl_9) say the heap grows in ten steps; in the bonus the active carts stand gold at the left of the board (seen in the bonus screens).
- **Subject:** A blue metal mine cart with a glowing lamp, heaped with gold nuggets and blue diamonds. The same rig holds an all-gold version of the cart (parts named gold/…), which is what the bonus screens show.
- **Style:** Stylised 3D-look toy mine cart: a short, wide tub on two small wheels with a round lamp on its front, drawn chunky and rounded, under a heap of faceted nuggets taller than the cart itself.
- **Rendering:** Smooth render-like gradients with hard, clean edges and no outline; every plane has a bright rim, and a white-to-colour halo is drawn as its own soft layers behind the cart.
- **Colour:** Blue body against yellow-gold nuggets with white highlights; the halo repeats the body colour. Measured: #fcfefa 22%, #fae60f 21%, #f78f08 15%, #0b4cdf 7%.
- **Lighting:** Lit from the top and top-left with strong specular highlights on metal and nuggets; the lamp and the halo are emissive and sit on additive slots.
- **Ambience:** A treasure about to spill: loud, glossy and inviting, the game's main promise shown as an object.
- **Materials:** Painted, riveted metal with a glossy enamel finish, polished gold nuggets, cut blue diamonds, a glass lamp.
- **Variants:** Ten fill levels (idle, win and impact for each, lvl_up between them), a pending and a trigger state at level 9, and a gold 'bg' version for the bonus game. The four carts share one construction and differ in body colour, gem and a few effect parts.
- **Motion:** Read from the motion sheet: in idle the heap and lamp shimmer and light sweeps pass; win flashes the whole cart in its colour; impact squashes the cart as a prize lands and the heap grows a step. Spine 3.8.99 skeleton, 195 bones, 206 slots, 46 animations as the file names them: idle_bg (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s), lvl_up/lvl_1_to_2 (1.33 s) and 38 more.
- **Construction:** A Spine rig of many small parts: the tub in pieces (trunk, bands, wheels, lamp), nuggets and gems as separate sprites added level by level, frame sequences for flashes, light sweeps and glow, and soft glow shapes on additive slots.
- **Notes:** The game has no figure character on stage; these four carts take that place, which is why they are sorted under Characters here (a sorting decision of this run). Largest single part 262x158 px or smaller: the cart is built small and never shipped as one picture.
- **Skeleton (from the file):** Spine 3.8.99 · 195 bones · 206 slots · animations: idle_bg (4.0 s), idle/lvl_0 (5.33 s), win/lvl_0 (2.67 s), impact/lvl_0 (2.67 s), idle/lvl_1 (5.33 s), win/lvl_1 (2.67 s), impact/lvl_1 (2.67 s), lvl_up/lvl_1_to_2 (1.33 s), idle/lvl_2 (5.33 s), win/lvl_2 (2.67 s), impact/lvl_2 (2.67 s), lvl_up/lvl_2_to_3 (1.33 s), idle/lvl_3 (5.33 s), win/lvl_3 (2.67 s), impact/lvl_3 (2.67 s), lvl_up/lvl_3_to_4 (1.33 s), idle/lvl_4 (5.33 s), win/lvl_4 (2.67 s), impact/lvl_4 (2.67 s), lvl_up/lvl_4_to_5 (1.33 s), idle/lvl_5 (5.33 s), win/lvl_5 (2.67 s), impact/lvl_5_impact_1 (2.67 s), impact/lvl_5_impact_2 (1.33 s), lvl_up/lvl_5_to_6 (1.33 s), impact/lvl_6 (2.67 s), idle/lvl_6 (5.33 s), win/lvl_6 (2.67 s), lvl_up/lvl_6_to_7 (1.33 s), win/lvl_7 (2.67 s), idle/lvl_7 (5.33 s), impact/lvl_7_impact_1 (2.67 s), impact/lvl_7_impact_2 (1.33 s), lvl_up/lvl_7_to_8 (1.33 s), win/lvl_8 (2.67 s), idle/lvl_8 (5.33 s), impact/lvl_8_impact_1 (2.67 s), impact/lvl_8_impact_2 (1.33 s), lvl_up/lvl_8_to_9 (1.33 s), idle/lvl_9 (4.0 s), win/lvl_9 (1.8 s), lvl_9_pending (4.0 s), lvl_9_pending_bg (4.0 s), lvl_9_trigger (3.33 s), lvl_up/lvl_0_to_1 (1.33 s), win_bg (1.67 s)
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 72% · saturation 66% · contrast 47% · warm 59% / cool 39% · brighter towards: top (10), top-left (8), top-right (7)
- **Palette (measured):** #fcfefa light green 22%, #fae60f gold 21%, #f78f08 orange 15%, #0b4cdf blue 7%, #faf05e gold 5%, #a5f9fe light cyan 3%


## Logo and title

The game's own wordmark.

### Game logo

`logo` · skeleton · 98 parts · largest 300×162 · sheet `sheets/logo.webp`

- **Role:** The 4 GOLD CARTS logo at the top left of the base game and on the intro card (seen in the game screens).
- **Subject:** A large red numeral 4 with a gold rim beside the words GOLD (yellow) and CARTS (white), stacked in two lines, all in heavy rounded capitals with a dark red extrusion and a warm glow.
- **Style:** Chunky extruded cartoon lettering, tilted slightly upward, compact two-line lock-up.
- **Rendering:** Flat bright faces with a soft inner gradient, dark red extrusion sides, a thin gold edge on the 4; clean vector-like edges.
- **Colour:** Red 4, yellow GOLD, white CARTS on dark red. Measured: #fce43e 18%, #e95628 16%, #fdf5e6 9%, #f8dea2 9%.
- **Lighting:** Top-lit faces; a 60-frame light sweep and star glints run over the letters.
- **Ambience:** Bold arcade signage.
- **Materials:** Enamel and gold.
- **Variants:** Loop and win animations.
- **Motion:** Spine 3.8.99 skeleton, 27 bones, 24 slots, 2 animations as the file names them: loop (5.0 s), win (1.33 s).
- **Construction:** 98 parts, most of them the frames of three 60-frame light sweeps and two 30-frame blink sequences; the lettering itself is three pieces (4, GOLD, CARTS) over a dark stroke.
- **Notes:** The number is the hero of the logo, as in Kendoo's other '3 …' and '4 …' titles listed on its site (the series naming is read from the site; the art comparison is not made here).
- **Skeleton (from the file):** Spine 3.8.99 · 27 bones · 24 slots · animations: loop (5.0 s), win (1.33 s)
- **Measured:** bright, vivid, warm, high contrast, glow or soft effect, strong highlights · brightness 62% · saturation 63% · contrast 62% · warm 100% / cool 0% · brighter towards: top (18), left (3)
- **Palette (measured):** #fce43e gold 18%, #e95628 red 16%, #fdf5e6 light orange 9%, #f8dea2 light orange 9%, #581a07 dark red 9%, #efb171 orange 9%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Big win coins

`bigwin-coin` · atlas · 30 parts · largest 195×195 · sheet `sheets/bigwin-coin.webp`

- **Role:** The coin shower of a big win (sheet bigwin).
- **Subject:** A gold coin stamped with the cart emblem, turning through 30 frames.
- **Style:** Stylised thick coin.
- **Rendering:** Glossy pre-rendered turn.
- **Colour:** Measured: #ffe72c 34%, #fba30f 21%, #e66902 17%, #a94101 14%.
- **Lighting:** Top-lit.
- **Materials:** Gold.
- **Motion:** A 30-frame turn as a frame sequence.
- **Construction:** 30 sprites of about 195x195 px.
- **Notes:** The cart emblem on the coin is the same badge as on the Power wheel and the cart mark.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 61% · saturation 91% · contrast 74% · warm 100% / cool 0% · brighter towards: top-right (7), top (4), bottom-right (3)
- **Palette (measured):** #ffe72c gold 34%, #fba30f orange 21%, #e66902 orange 17%, #a94101 brown 14%, #602000 brown 10%, #fffb8b light gold 3%

### NICE and GREAT win words

`nice_great` · skeleton · 14 parts · largest 205×112 · sheet `sheets/nice_great.webp`

- **Role:** Small win call-outs over the reels.
- **Subject:** The words NICE and GREAT in white capitals with a red stroke over an orange star flash.
- **Style:** As the logo lettering, smaller.
- **Colour:** Measured: #faf5fb 32%, #fbeb44 15%, #3a0101 13%, #a91514 10%.
- **Variants:** nice_loop, great_loop, numbers_loop.
- **Motion:** Spine 3.8.99 skeleton, 22 bones, 20 slots, 3 animations as the file names them: great_loop (2.0 s), nice_loop (2.0 s), numbers_loop (2.0 s).
- **Construction:** 14 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 22 bones · 20 slots · animations: great_loop (2.0 s), nice_loop (2.0 s), numbers_loop (2.0 s)
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 60% · saturation 56% · contrast 74% · warm 100% / cool 0% · brighter towards: top (4)
- **Palette (measured):** #faf5fb light purple 32%, #fbeb44 gold 15%, #3a0101 black 13%, #a91514 red 10%, #7c1f30 red 7%, #ffa10c orange 6%

### End of bonus burst

`end_bonus_game` · skeleton · 3 parts · largest 400×400 · sheet `sheets/end_bonus_game.webp`

- **Role:** The burst behind the bonus total.
- **Subject:** A large ring of orange rays with a dark centre.
- **Rendering:** Soft radial rays.
- **Colour:** Measured: #fd6f03 64%, #feb01a 17%, #ff1000 10%, #fed347 8%.
- **Lighting:** Emissive.
- **Motion:** Spine 3.8.99 skeleton, 8 bones, 6 slots, 1 animations as the file names them: start (2.17 s).
- **Construction:** 3 parts scaled up to about 1400 px across in the drawn frame.
- **Notes:** Three small sprites make a full-screen effect by scaling.
- **Skeleton (from the file):** Spine 3.8.99 · 8 bones · 6 slots · animations: start (2.17 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 56% · saturation 95% · contrast 33% · warm 100% / cool 0%
- **Palette (measured):** #fd6f03 orange 64%, #feb01a orange 17%, #ff1000 red 10%, #fed347 gold 8%

### Big win and jackpot banners

`big_wins` · skeleton · 89 parts · largest 399×387 · sheet `sheets/big_wins.webp`

- **Role:** The win celebration lettering. The parts spell BIG WIN, MEGA, SENSATIONAL, LEGENDARY, BRILLIANT, BONUS WIN, GRAND / ROYAL JACKPOT; the animations are named idle and end for levels 1 to 6 in portrait and landscape.
- **Subject:** Stacked heavy capitals in yellow-to-orange with a red extrusion over a round orange burst of rays.
- **Style:** The logo's lettering style turned up: fat rounded capitals, tilted.
- **Rendering:** Bright gradient faces, dark red sides, a yellow glow copy behind each word and blurred copies for the entrance.
- **Colour:** Yellow, orange and dark red, with white for WIN. Measured: #fcc40d 14%, #491101 14%, #fdf9e2 14%, #fef989 13%.
- **Lighting:** The burst behind is the light source; rays, rings and glows are additive.
- **Ambience:** A fanfare; the loudest lettering in the game.
- **Materials:** Enamel lettering, fire-like light.
- **Variants:** Six levels plus jackpot wordings, each in portrait and landscape.
- **Motion:** Read from the motion sheet: the word pulses over the burst and at the end shrinks into a spray of sparks. Spine 3.8.99 skeleton, 168 bones, 209 slots, 54 animations as the file names them: portrait/end_lvl1 (2.0 s), landscape/end_lvl1 (2.0 s), portrait/end_lvl2 (2.0 s), landscape/end_lvl2 (2.0 s), portrait/end_lvl3 (2.0 s), landscape/end_lvl3 (2.0 s), portrait/end_lvl4 (2.0 s), landscape/end_lvl4 (2.0 s) and 46 more.
- **Construction:** 89 parts: each word as front, blur and glow copies, ray and ring shapes, sweep sequences.
- **Notes:** No big win came in the played session, so there is no real screen of this; the frames are drawn from the parts.
- **Skeleton (from the file):** Spine 3.8.99 · 168 bones · 209 slots · animations: portrait/end_lvl1 (2.0 s), landscape/end_lvl1 (2.0 s), portrait/end_lvl2 (2.0 s), landscape/end_lvl2 (2.0 s), portrait/end_lvl3 (2.0 s), landscape/end_lvl3 (2.0 s), portrait/end_lvl4 (2.0 s), landscape/end_lvl4 (2.0 s), portrait/end_lvl5 (2.0 s), landscape/end_lvl5 (2.0 s), portrait/end_lvl6 (2.0 s), landscape/end_lvl6 (2.0 s), portrait/end_lvl7 (2.0 s), landscape/end_lvl7 (2.0 s), portrait/end_lvl8 (2.0 s), landscape/end_lvl8 (2.0 s), portrait/end_lvl9 (2.0 s), landscape/end_lvl9 (2.0 s), portrait/idle_lvl1 (2.0 s), landscape/idle_lvl1 (2.0 s), portrait/idle_lvl2 (2.0 s), landscape/idle_lvl2 (2.0 s), portrait/idle_lvl3 (2.0 s), landscape/idle_lvl3 (2.0 s), portrait/idle_lvl4 (2.0 s), landscape/idle_lvl4 (2.0 s), portrait/idle_lvl5 (2.0 s), landscape/idle_lvl5 (2.0 s), portrait/idle_lvl6 (2.0 s), landscape/idle_lvl6 (2.0 s), portrait/idle_lvl7 (2.0 s), landscape/idle_lvl7 (2.0 s), portrait/idle_lvl8 (2.0 s), landscape/idle_lvl8 (2.0 s), portrait/idle_lvl9 (2.0 s), landscape/idle_lvl9 (2.0 s), portrait/start_lvl1 (2.0 s), landscape/start_lvl1 (2.0 s), portrait/start_lvl2 (2.0 s), landscape/start_lvl2 (2.0 s), portrait/start_lvl3 (2.0 s), landscape/start_lvl3 (2.0 s), portrait/start_lvl4 (2.0 s), landscape/start_lvl4 (2.0 s), portrait/start_lvl5 (2.0 s), landscape/start_lvl5 (2.0 s), portrait/start_lvl6 (2.0 s), landscape/start_lvl6 (2.0 s), portrait/start_lvl7 (2.0 s), landscape/start_lvl7 (2.0 s), portrait/start_lvl8 (2.0 s), landscape/start_lvl8 (2.0 s), portrait/start_lvl9 (2.0 s), landscape/start_lvl9 (2.0 s)
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 60% · saturation 72% · contrast 70% · warm 100% / cool 0% · brighter towards: top (16), top-left (1), top-right (1)
- **Palette (measured):** #fcc40d gold 14%, #491101 dark red 14%, #fdf9e2 light gold 14%, #fef989 light gold 13%, #f1150a red 11%, #fff52c gold 8%

### Feature titles on the reels: COLLECT, POWER, MULTI

`titles_on_reels` · skeleton · 29 parts · largest 564×175 · sheet `sheets/titles_on_reels.webp`

- **Role:** The word that flashes over the board when a feature starts.
- **Subject:** The feature's name in its colour inside a ring and a burst of rays.
- **Style:** Rounded heavy capitals with a dark stroke.
- **Colour:** Measured: #0b0c13 14%, #07befa 14%, #37f43a 13%, #e845f8 12%.
- **Variants:** start_collect, start_multi, start_power.
- **Motion:** Spine 3.8.99 skeleton, 57 bones, 29 slots, 3 animations as the file names them: start_collect (1.33 s), start_multi (1.33 s), start_power (1.33 s).
- **Construction:** 29 parts, each word with a blurred copy.
- **Skeleton (from the file):** Spine 3.8.99 · 57 bones · 29 slots · animations: start_collect (1.33 s), start_multi (1.33 s), start_power (1.33 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, glow or soft effect · brightness 49% · saturation 80% · contrast 48% · warm 9% / cool 66% · brighter towards: top-left (3), top (1)
- **Palette (measured):** #0b0c13 black 14%, #07befa cyan 14%, #37f43a green 13%, #e845f8 magenta 12%, #fac3fb light magenta 5%, #096b07 dark green 4%

### Feature title on the reels: EXPAND

`expand_title_on_reels` · skeleton · 8 parts · largest 564×175 · sheet `sheets/expand_title_on_reels.webp`

- **Role:** The EXPAND word over the board.
- **Subject:** EXPAND in white on a red ring flash.
- **Colour:** Measured: #f21b06 28%, #fe3446 24%, #f57165 19%, #fec0a5 12%.
- **Motion:** Spine 3.8.99 skeleton, 25 bones, 15 slots, 1 animations as the file names them: start (1.0 s).
- **Construction:** 8 parts; the tool reports 2 parts not found for this rig, so the drawn frame is incomplete.
- **Notes:** The drawn frame shows the word faint; it is not a fault of the game's art.
- **Skeleton (from the file):** Spine 3.8.99 · 25 bones · 15 slots · animations: start (1.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 42% · saturation 75% · contrast 45% · warm 100% / cool 0%
- **Palette (measured):** #f21b06 red 28%, #fe3446 red 24%, #f57165 red 19%, #fec0a5 light orange 12%, #b24f43 red 6%, #800c09 dark red 6%

### POWER BONUS GAME title

`power_feature_txt` · skeleton · 5 parts · largest 407×96 · sheet `sheets/power_feature_txt.webp`

- **Role:** The heading of the Power Bonus Game.
- **Subject:** POWER BONUS GAME in cyan-to-white capitals with a dark blue stroke and an orange glow.
- **Colour:** Measured: #6ae7fd 20%, #0f2188 19%, #19ccf9 18%, #f4fcf0 14%.
- **Motion:** Spine 3.8.99 skeleton, 8 bones, 9 slots, 1 animations as the file names them: loop (4.01 s).
- **Construction:** 5 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 8 bones · 9 slots · animations: loop (4.01 s)
- **Measured:** mid-tone, vivid, cool, high contrast, strong highlights · brightness 57% · saturation 68% · contrast 63% · warm 10% / cool 90% · brighter towards: top (1)
- **Palette (measured):** #6ae7fd cyan 20%, #0f2188 dark blue 19%, #19ccf9 cyan 18%, #f4fcf0 light green 14%, #020832 black 9%, #0c7ae3 blue 6%

### Intro card: Bonus Game Features

`feature_preview` · skeleton · 346 parts · largest 290×205 · sheet `sheets/feature_preview.webp`

- **Role:** The opening card of the game and of the bonus (seen in the game screens), and the same cart pictures inside the buy cards.
- **Subject:** The logo, the heading BONUS GAME FEATURES, and the four carts each beside a small diagram of its feature: Expand with a growing grid, Power with the six-cell wheel, Collect with a pot gathering prizes, Multi with multiplier tags.
- **Style:** A poster of the game's own pieces: carts, pots, gems and labels re-used at larger size.
- **Rendering:** As the carts; diagrams are small flat panels.
- **Colour:** Each quarter in its feature colour on the hot intro gradient. Measured: #f78805 16%, #fefcf8 15%, #ffed10 10%, #420d0e 9%.
- **Lighting:** Each cart has its coloured halo.
- **Ambience:** A promise of four prizes at once.
- **Variants:** 32 animations: one per feature and per pair and set of features, portrait and landscape. The bonus intro in the game screens shows only the Expand part when only Expand is active.
- **Motion:** Spine 3.8.99 skeleton, 805 bones, 669 slots, 32 animations as the file names them: portrait/collect (5.33 s), landscape/collect (5.33 s), portrait/collect_multi (5.33 s), landscape/collect_multi (5.33 s), portrait/expand (5.33 s), landscape/expand (5.33 s), portrait/expand_collect (5.33 s), landscape/expand_collect (5.33 s) and 24 more.
- **Construction:** 346 parts and 805 bones, the largest rig in the game: it holds all four carts again in pieces, the feature diagrams and the labels.
- **Notes:** The frame drawn by this tool shows one state (Collect); the game screens show the whole card.
- **Skeleton (from the file):** Spine 3.8.99 · 805 bones · 669 slots · animations: portrait/collect (5.33 s), landscape/collect (5.33 s), portrait/collect_multi (5.33 s), landscape/collect_multi (5.33 s), portrait/expand (5.33 s), landscape/expand (5.33 s), portrait/expand_collect (5.33 s), landscape/expand_collect (5.33 s), portrait/expand_collect_multi (5.33 s), landscape/expand_collect_multi (5.33 s), portrait/expand_multi (5.33 s), landscape/expand_multi (5.33 s), portrait/expand_power (5.33 s), landscape/expand_power (5.33 s), portrait/expand_power_collect (5.33 s), landscape/expand_power_collect (5.33 s), portrait/expand_power_collect_multi (5.33 s), landscape/expand_power_collect_multi (5.33 s), portrait/expand_power_multi (5.33 s), landscape/expand_power_multi (5.33 s), portrait/feature_preview (5.33 s), landscape/feature_preview (5.33 s), landscape/multi (5.33 s), portrait/multi (5.33 s), landscape/power (5.33 s), portrait/power (5.33 s), portrait/power_collect (5.33 s), landscape/power_collect (5.33 s), portrait/power_collect_multi (5.33 s), landscape/power_collect_multi (5.33 s), portrait/power_multi (5.33 s), landscape/power_multi (5.33 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 57% · saturation 74% · contrast 60% · warm 66% / cool 23% · brighter towards: top (32), top-left (17), top-right (13)
- **Palette (measured):** #f78805 orange 16%, #fefcf8 light orange 15%, #ffed10 gold 10%, #420d0e dark red 9%, #cc480a orange 6%, #fef975 gold 5%


## Effects

Frame sequences, glows, particles and transitions.

### Sparks (bonus)

`bonus-particles` · atlas · 2 parts · largest 63×64 · sheet `sheets/bonus-particles.webp`

- **Role:** Two spark sprites for the bonus.
- **Subject:** A yellow and an orange star dot.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #fdec31 50%, #ffad6a 37%, #feffee 6%, #f5f396 6%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Construction:** 2 parts.
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 84% · saturation 65% · contrast 17% · warm 99% / cool 1%
- **Palette (measured):** #fdec31 gold 50%, #ffad6a orange 37%, #feffee light gold 6%, #f5f396 light gold 6%

### Gems and sparks (base game)

`main-particles` · atlas · 26 parts · largest 374×291 · sheet `sheets/main-particles.webp`

- **Role:** Loose gems for particle effects in the base game.
- **Subject:** Faceted gems in blue, green, red and violet, each as short turning sequences, with two spark dots.
- **Style:** Stylised cut gems, as the jackpot symbols.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #cd130a 12%, #027aec 10%, #eff0f4 9%, #03881b 9%.
- **Lighting:** Emissive.
- **Materials:** Cut crystal.
- **Construction:** 26 parts.
- **Notes:** Largest gem 374x291 px: the biggest single gem pictures in the game are particles.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 52% · saturation 73% · contrast 78% · warm 34% / cool 46% · brighter towards: bottom (8), bottom-right (6), bottom-left (3)
- **Palette (measured):** #cd130a red 12%, #027aec blue 10%, #eff0f4 light blue 9%, #03881b dark green 9%, #9310b8 purple 8%, #55d2fe cyan 6%

### Screen shake rig

`shaker` · skeleton · 5 parts · largest 12×12 · sheet `sheets/shaker.webp`

- **Role:** A rig with no picture, used to shake the scene (animation names fall, lvl_up_trigger).
- **Subject:** Only placeholder points.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #be0020 100%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 1 slots, 5 animations as the file names them: fall (0.17 s), scene/fall (0.33 s), scene/lvl_up_trigger (0.4 s), transform (0.4 s), value (0.3 s).
- **Construction:** 5 parts.
- **Notes:** Nothing to see: motion data only.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 1 slots · animations: fall (0.17 s), scene/fall (0.33 s), scene/lvl_up_trigger (0.4 s), transform (0.4 s), value (0.3 s)
- **Measured:** dark, vivid, warm, low contrast · brightness 17% · saturation 100% · contrast 0% · warm 100% / cool 0%
- **Palette (measured):** #be0020 red 100%

### Prize trails

`trails` · skeleton · 100 parts · largest 400×90 · sheet `sheets/trails.webp`

- **Role:** The streaks that fly from a symbol to a cart or prize (66 animations named by feature: power, expand, collect, multi).
- **Subject:** A comet-like streak in red, blue, green and violet as 24-frame sequences, with gold sparks.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #f32f17 18%, #fdfdfb 16%, #791def 16%, #1f5df2 15%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 50 bones, 16 slots, 66 animations as the file names them: power_bonus/trail_1 (0.93 s), expand/trail_1_1 (0.93 s), power/trail_1_1 (0.93 s), collect/trail_1_1 (0.93 s), multi/trail_1_1 (0.93 s), expand/trail_1_2 (0.93 s), power/trail_1_2 (0.93 s), collect/trail_1_2 (0.93 s) and 58 more.
- **Construction:** 100 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 50 bones · 16 slots · animations: power_bonus/trail_1 (0.93 s), expand/trail_1_1 (0.93 s), power/trail_1_1 (0.93 s), collect/trail_1_1 (0.93 s), multi/trail_1_1 (0.93 s), expand/trail_1_2 (0.93 s), power/trail_1_2 (0.93 s), collect/trail_1_2 (0.93 s), multi/trail_1_2 (0.93 s), expand/trail_1_3 (0.93 s), power/trail_1_3 (0.93 s), collect/trail_1_3 (0.93 s), multi/trail_1_3 (0.93 s), collect/trail_1_4 (0.93 s), expand/trail_1_4 (0.93 s), power/trail_1_4 (0.93 s), multi/trail_1_4 (0.93 s), collect/trail_1_5 (0.93 s), expand/trail_1_5 (0.93 s), power/trail_1_5 (0.93 s), multi/trail_1_5 (0.93 s), power_bonus/trail_2 (0.93 s), power/trail_2_1 (0.93 s), expand/trail_2_1 (0.93 s), collect/trail_2_1 (0.93 s), multi/trail_2_1 (0.93 s), power/trail_2_2 (0.93 s), expand/trail_2_2 (0.93 s), collect/trail_2_2 (0.93 s), multi/trail_2_2 (0.93 s), expand/trail_2_3 (0.93 s), power/trail_2_3 (0.93 s), collect/trail_2_3 (0.93 s), multi/trail_2_3 (0.93 s), collect/trail_2_4 (0.93 s), power/trail_2_4 (0.93 s), expand/trail_2_4 (0.93 s), multi/trail_2_4 (0.93 s), expand/trail_2_5 (0.93 s), power/trail_2_5 (0.93 s), collect/trail_2_5 (0.93 s), multi/trail_2_5 (0.93 s), power_bonus/trail_3 (0.93 s), power/trail_3_1 (0.93 s), expand/trail_3_1 (0.93 s), collect/trail_3_1 (0.93 s), multi/trail_3_1 (0.93 s), power/trail_3_2 (0.93 s), expand/trail_3_2 (0.93 s), collect/trail_3_2 (0.93 s), multi/trail_3_2 (0.93 s), expand/trail_3_3 (0.93 s), power/trail_3_3 (0.93 s), collect/trail_3_3 (0.93 s), multi/trail_3_3 (0.93 s), expand/trail_3_4 (0.93 s), power/trail_3_4 (0.93 s), collect/trail_3_4 (0.93 s), multi/trail_3_4 (0.93 s), expand/trail_3_5 (0.93 s), power/trail_3_5 (0.93 s), collect/trail_3_5 (0.93 s), multi/trail_3_5 (0.93 s), power_bonus/trail_4 (0.93 s), power_bonus/trail_5 (0.93 s), power_bonus/trail_6 (0.93 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 57% · saturation 72% · contrast 60% · warm 31% / cool 56% · brighter towards: right (8)
- **Palette (measured):** #f32f17 red 18%, #fdfdfb light yellow 16%, #791def purple 16%, #1f5df2 blue 15%, #53ff00 green 11%, #ec3cff magenta 5%

### Cart landing light, green

`vfx_green` · skeleton · 4 parts · largest 194×193 · sheet `sheets/vfx_green.webp`

- **Role:** The same light for the green cart.
- **Subject:** A green fan of rays in a soft dome.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #05ee00 53%, #76f30a 34%, #f7fff1 4%, #48f90f 4%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 14 bones, 11 slots, 1 animations as the file names them: idle (5.33 s).
- **Construction:** 4 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 14 bones · 11 slots · animations: idle (5.33 s)
- **Measured:** bright, vivid, warm and cool mixed, low contrast, glow or soft effect · brightness 74% · saturation 92% · contrast 16% · warm 1% / cool 49%
- **Palette (measured):** #05ee00 green 53%, #76f30a green 34%, #f7fff1 light green 4%, #48f90f green 4%, #b3ff4a green 2%, #d9ffb4 light green 2%

### Cart landing light, red

`vfx_red` · skeleton · 4 parts · largest 194×193 · sheet `sheets/vfx_red.webp`

- **Role:** The light under the red cart as a prize arrives.
- **Subject:** A red fan of rays in a soft dome with rising dots.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ff401d 61%, #ff8630 16%, #ffb15a 9%, #ff6d6d 6%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 14 bones, 11 slots, 1 animations as the file names them: idle (5.33 s).
- **Construction:** 4 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 14 bones · 11 slots · animations: idle (5.33 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 51% · saturation 78% · contrast 29% · warm 99% / cool 0%
- **Palette (measured):** #ff401d red 61%, #ff8630 orange 16%, #ffb15a orange 9%, #ff6d6d red 6%, #fff4ef light orange 5%, #ffe390 light gold 2%

### Cart landing light, violet

`vfx_violet` · skeleton · 4 parts · largest 194×193 · sheet `sheets/vfx_violet.webp`

- **Role:** The same light for the violet cart.
- **Subject:** A violet fan of rays in a soft dome.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #b223ff 72%, #e439ff 15%, #e777fe 8%, #fdecfe 5%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 14 bones, 11 slots, 1 animations as the file names them: idle (5.33 s).
- **Construction:** 4 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 14 bones · 11 slots · animations: idle (5.33 s)
- **Measured:** mid-tone, vivid, cool, low contrast, glow or soft effect · brightness 39% · saturation 78% · contrast 21% · warm 11% / cool 77%
- **Palette (measured):** #b223ff purple 72%, #e439ff magenta 15%, #e777fe purple 8%, #fdecfe light magenta 5%

### Cart landing light, blue

`vfx_blue` · skeleton · 4 parts · largest 194×193 · sheet `sheets/vfx_blue.webp`

- **Role:** The same light for the blue cart.
- **Subject:** A blue fan of rays in a soft dome.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #1a70ff 55%, #91e3ff 28%, #1ca4ff 11%, #e7fbff 6%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 14 bones, 11 slots, 1 animations as the file names them: idle (5.33 s).
- **Construction:** 4 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 14 bones · 11 slots · animations: idle (5.33 s)
- **Measured:** mid-tone, vivid, cool, low contrast, glow or soft effect, strong highlights · brightness 58% · saturation 72% · contrast 18% · warm 0% / cool 99%
- **Palette (measured):** #1a70ff blue 55%, #91e3ff light cyan 28%, #1ca4ff blue 11%, #e7fbff light cyan 6%

### Cart prize pop

`fake_collect_explosion` · skeleton · 13 parts · largest 198×198 · sheet `sheets/fake_collect_explosion.webp`

- **Role:** A star pop in the four feature colours.
- **Subject:** White and coloured star flashes and sparks.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #fefef1 20%, #fe5430 18%, #51d950 15%, #ef3ae7 15%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 35 bones, 17 slots, 1 animations as the file names them: explosion (0.83 s).
- **Construction:** 13 parts.
- **Notes:** The tool drew an empty frame for this rig; read from the parts.
- **Skeleton (from the file):** Spine 3.8.99 · 35 bones · 17 slots · animations: explosion (0.83 s)
- **Measured:** bright, saturated, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 67% · saturation 59% · contrast 24% · warm 32% / cool 33%
- **Palette (measured):** #fefef1 light gold 20%, #fe5430 red 18%, #51d950 green 15%, #ef3ae7 magenta 15%, #32bbfe cyan 12%, #1ffcf7 cyan 4%

### Transition to the bonus

`transition` · skeleton · 30 parts · largest 562×559 · sheet `sheets/transition.webp`

- **Role:** The screen change into the Bonus Game.
- **Subject:** A rain of large gems in four colours with vertical light streaks.
- **Style:** Stylised cut gems.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #cd140b 11%, #027bed 10%, #eff0f4 9%, #03881b 8%.
- **Lighting:** Emissive.
- **Materials:** Cut crystal, light.
- **Motion:** Spine 3.8.99 skeleton, 77 bones, 136 slots, 2 animations as the file names them: portrait/start (2.5 s), landscape/start (2.5 s).
- **Construction:** 30 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 77 bones · 136 slots · animations: portrait/start (2.5 s), landscape/start (2.5 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 52% · saturation 73% · contrast 77% · warm 33% / cool 47% · brighter towards: bottom (8), bottom-right (7), bottom-left (3)
- **Palette (measured):** #cd140b red 11%, #027bed blue 10%, #eff0f4 light blue 9%, #03881b dark green 8%, #9310b8 purple 7%, #54d2fd cyan 6%

### Win frame

`winframe` · skeleton · 34 parts · largest 184×154 · sheet `sheets/winframe.webp`

- **Role:** The frame round a winning symbol.
- **Subject:** A hand-drawn-looking orange-yellow fire line running round a rounded rectangle, 34 frames.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ff5a02 52%, #fff422 21%, #ff9a0d 20%, #fffffd 5%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 1 slots, 1 animations as the file names them: win (1.03 s).
- **Construction:** 34 parts.
- **Notes:** A frame sequence, not a rig: one bone.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 1 slots · animations: win (1.03 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 62% · saturation 90% · contrast 52% · warm 100% / cool 0%
- **Palette (measured):** #ff5a02 orange 52%, #fff422 gold 21%, #ff9a0d orange 20%, #fffffd light gold 5%

### Win ring

`win_effect` · skeleton · 5 parts · largest 245×231 · sheet `sheets/win_effect.webp`

- **Role:** A ring pulse on a win.
- **Subject:** Yellow concentric rings with dust.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #feed38 64%, #ffff00 23%, #944800 10%, #eb9500 2%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 7 bones, 5 slots, 1 animations as the file names them: explosion (1.0 s).
- **Construction:** 5 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 7 bones · 5 slots · animations: explosion (1.0 s)
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 84% · saturation 86% · contrast 5% · warm 100% / cool 0%
- **Palette (measured):** #feed38 gold 64%, #ffff00 gold 23%, #944800 brown 10%, #eb9500 orange 2%

### Collect burst

`collector_explosion` · skeleton · 6 parts · largest 128×128 · sheet `sheets/collector_explosion.webp`

- **Role:** The burst when the Collect pot gathers prizes.
- **Subject:** A green star burst in a ring.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #7aff00 72%, #b1ff00 21%, #ecff0d 5%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 38 bones, 19 slots, 2 animations as the file names them: impact (0.9 s), impact_1 (0.9 s).
- **Construction:** 6 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 38 bones · 19 slots · animations: impact (0.9 s), impact_1 (0.9 s)
- **Measured:** bright, vivid, warm and cool mixed, low contrast, glow or soft effect · brightness 83% · saturation 99% · contrast 4% · warm 8% / cool 46%
- **Palette (measured):** #7aff00 green 72%, #b1ff00 green 21%, #ecff0d gold 5%

### Trails to the collect panel

`trails_collect_panel` · skeleton · 27 parts · largest 400×90 · sheet `sheets/trails_collect_panel.webp`

- **Role:** Streaks flying to the total panel, named per layout.
- **Subject:** An orange comet streak sequence and sparks.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #eb580d 59%, #ffed2c 17%, #fffff4 10%, #ffff99 6%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 49 bones, 15 slots, 60 animations as the file names them: portrait_bg_expand/trail_1_1 (0.93 s), landscape_bg_expand/trail_1_1 (0.93 s), portrait_bg_expand/trail_1_2 (0.93 s), landscape_bg_expand/trail_1_2 (0.93 s), portrait_bg_expand/trail_1_3 (0.93 s), landscape_bg_expand/trail_1_3 (0.93 s), portrait_bg_expand/trail_1_4 (0.93 s), landscape_bg_expand/trail_1_4 (0.93 s) and 52 more.
- **Construction:** 27 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 49 bones · 15 slots · animations: portrait_bg_expand/trail_1_1 (0.93 s), landscape_bg_expand/trail_1_1 (0.93 s), portrait_bg_expand/trail_1_2 (0.93 s), landscape_bg_expand/trail_1_2 (0.93 s), portrait_bg_expand/trail_1_3 (0.93 s), landscape_bg_expand/trail_1_3 (0.93 s), portrait_bg_expand/trail_1_4 (0.93 s), landscape_bg_expand/trail_1_4 (0.93 s), portrait_bg_expand/trail_1_5 (0.93 s), landscape_bg_expand/trail_1_5 (0.93 s), portrait_bg_expand/trail_2_1 (0.93 s), landscape_bg_expand/trail_2_1 (0.93 s), portrait_bg_expand/trail_2_2 (0.93 s), landscape_bg_expand/trail_2_2 (0.93 s), portrait_bg_expand/trail_2_3 (0.93 s), landscape_bg_expand/trail_2_3 (0.93 s), portrait_bg_expand/trail_2_4 (0.93 s), landscape_bg_expand/trail_2_4 (0.93 s), portrait_bg_expand/trail_2_5 (0.93 s), landscape_bg_expand/trail_2_5 (0.93 s), landscape_bg_expand/trail_3_1 (0.93 s), portrait_bg_expand/trail_3_1 (0.93 s), landscape_bg_expand/trail_3_2 (0.93 s), portrait_bg_expand/trail_3_2 (0.93 s), landscape_bg_expand/trail_3_3 (0.93 s), portrait_bg_expand/trail_3_3 (0.93 s), portrait_bg_expand/trail_3_4 (0.93 s), landscape_bg_expand/trail_3_4 (0.93 s), portrait_bg_expand/trail_3_5 (0.93 s), landscape_bg_expand/trail_3_5 (0.93 s), portrait_bg_expand/trail_4_1 (0.93 s), landscape_bg_expand/trail_4_1 (0.93 s), portrait_bg_expand/trail_4_2 (0.93 s), landscape_bg_expand/trail_4_2 (0.93 s), portrait_bg_expand/trail_4_3 (0.93 s), landscape_bg_expand/trail_4_3 (0.93 s), portrait_bg_expand/trail_4_4 (0.93 s), landscape_bg_expand/trail_4_4 (0.93 s), portrait_bg_expand/trail_4_5 (0.93 s), landscape_bg_expand/trail_4_5 (0.93 s), landscape_bg_expand/trail_5_1 (0.93 s), portrait_bg_expand/trail_5_1 (0.93 s), landscape_bg_expand/trail_5_2 (0.93 s), portrait_bg_expand/trail_5_2 (0.93 s), landscape_bg_expand/trail_5_3 (0.93 s), portrait_bg_expand/trail_5_3 (0.93 s), portrait_bg_expand/trail_5_4 (0.93 s), landscape_bg_expand/trail_5_4 (0.93 s), portrait_bg_expand/trail_5_5 (0.93 s), landscape_bg_expand/trail_5_5 (0.93 s), landscape_bg_expand/trail_6_1 (0.93 s), portrait_bg_expand/trail_6_1 (0.93 s), landscape_bg_expand/trail_6_2 (0.93 s), portrait_bg_expand/trail_6_2 (0.93 s), landscape_bg_expand/trail_6_3 (0.93 s), portrait_bg_expand/trail_6_3 (0.93 s), portrait_bg_expand/trail_6_4 (0.93 s), landscape_bg_expand/trail_6_4 (0.93 s), portrait_bg_expand/trail_6_5 (0.93 s), landscape_bg_expand/trail_6_5 (0.93 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 63% · saturation 79% · contrast 54% · warm 100% / cool 0%
- **Palette (measured):** #eb580d orange 59%, #ffed2c gold 17%, #fffff4 light gold 10%, #ffff99 light gold 6%, #ffa714 orange 6%

### Collect panel pop

`collect_explosion` · skeleton · 3 parts · largest 175×175 · sheet `sheets/collect_explosion.webp`

- **Role:** A small pop on the total panel.
- **Subject:** An orange ring and flare.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ff9d0e 72%, #ff6503 15%, #ffc66d 6%, #f98c3b 5%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 6 bones, 4 slots, 1 animations as the file names them: win (0.5 s).
- **Construction:** 3 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 4 slots · animations: win (0.5 s)
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect · brightness 64% · saturation 91% · contrast 17% · warm 100% / cool 0%
- **Palette (measured):** #ff9d0e orange 72%, #ff6503 orange 15%, #ffc66d orange 6%, #f98c3b orange 5%

### Reel back glow

`bg_reel_glow_blue` · skeleton · 1 parts · largest 95×69 · sheet `sheets/bg_reel_glow_blue.webp`

- **Role:** A soft glow behind the board.
- **Subject:** A violet soft patch scaled up.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #741ea7 100%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 1 slots, 1 animations as the file names them: loop (0.0 s).
- **Construction:** 1 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 1 slots · animations: loop (0.0 s)
- **Measured:** dark, vivid, cool, low contrast, glow or soft effect · brightness 23% · saturation 82% · contrast 0% · warm 0% / cool 100%
- **Palette (measured):** #741ea7 purple 100%

### Cell glow

`cell_glow` · skeleton · 1 parts · largest 26×24 · sheet `sheets/cell_glow.webp`

- **Role:** A glow in a bonus cell.
- **Subject:** A small red soft patch.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ff000d 100%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 1 slots, 1 animations as the file names them: start (1.0 s).
- **Construction:** 1 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 1 slots · animations: start (1.0 s)
- **Measured:** dark, vivid, warm, low contrast, glow or soft effect · brightness 22% · saturation 100% · contrast 0% · warm 100% / cool 0%
- **Palette (measured):** #ff000d red 100%

### Cell anticipation

`anticipation_cell` · skeleton · 12 parts · largest 273×257 · sheet `sheets/anticipation_cell.webp`

- **Role:** The frame round a cell that may complete a prize.
- **Subject:** A glowing gold cell frame with rays.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ff9f15 64%, #ffe73f 17%, #fff6a8 15%, #fffdec 3%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 32 bones, 26 slots, 4 animations as the file names them: loop (1.0 s), loop_full (1.0 s), start (0.5 s), start_full (0.5 s).
- **Construction:** 12 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 32 bones · 26 slots · animations: loop (1.0 s), loop_full (1.0 s), start (0.5 s), start_full (0.5 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 76% · saturation 77% · contrast 35% · warm 100% / cool 0%
- **Palette (measured):** #ff9f15 orange 64%, #ffe73f gold 17%, #fff6a8 light gold 15%, #fffdec light gold 3%

### Anticipation ring

`anticipation` · skeleton · 30 parts · largest 167×149 · sheet `sheets/anticipation.webp`

- **Role:** A ring that spins up before a result.
- **Subject:** A gold-orange fire ring, 30 frames.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #fe7d0b 59%, #ffd11b 15%, #ffffc5 12%, #fffa37 10%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 1 slots, 2 animations as the file names them: loop (0.97 s), start (0.67 s).
- **Construction:** 30 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 1 slots · animations: loop (0.97 s), start (0.67 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 70% · saturation 83% · contrast 45% · warm 100% / cool 0%
- **Palette (measured):** #fe7d0b orange 59%, #ffd11b gold 15%, #ffffc5 light gold 12%, #fffa37 gold 10%, #fffe78 gold 4%

### Number impact

`effect_numbers` · skeleton · 7 parts · largest 200×200 · sheet `sheets/effect_numbers.webp`

- **Role:** The hit when a value changes.
- **Subject:** A yellow star burst with dots.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #feeb39 64%, #9b4800 13%, #f3930e 12%, #fef29c 5%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 39 bones, 20 slots, 1 animations as the file names them: impact (0.9 s).
- **Construction:** 7 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 39 bones · 20 slots · animations: impact (0.9 s)
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 77% · saturation 80% · contrast 15% · warm 100% / cool 0%
- **Palette (measured):** #feeb39 gold 64%, #9b4800 brown 13%, #f3930e orange 12%, #fef29c light gold 5%, #d46903 orange 3%

### Power centre effect

`effect_over` · skeleton · 13 parts · largest 221×221 · sheet `sheets/effect_over.webp`

- **Role:** The flare over the Power wheel when the multiplier applies (animations multiplier, open).
- **Subject:** Layered rings, rays and dots in orange and gold.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ff900c 46%, #ffeb09 33%, #fff46f 4%, #ff3503 4%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 110 bones, 90 slots, 2 animations as the file names them: multiplier (1.67 s), open (0.83 s).
- **Construction:** 13 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 110 bones · 90 slots · animations: multiplier (1.67 s), open (0.83 s)
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 74% · saturation 87% · contrast 24% · warm 100% / cool 0%
- **Palette (measured):** #ff900c orange 46%, #ffeb09 gold 33%, #fff46f gold 4%, #ff3503 red 4%, #ffd939 gold 3%

### Symbol ring

`effect_symbol` · skeleton · 1 parts · largest 318×283 · sheet `sheets/effect_symbol.webp`

- **Role:** A ring round a symbol.
- **Subject:** A gold fire ring.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #fe750a 51%, #ffef20 32%, #ffaf15 8%, #ffffe9 5%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 1 slots, 1 animations as the file names them: start (0.5 s).
- **Construction:** 1 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 1 slots · animations: start (0.5 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 71% · saturation 86% · contrast 48% · warm 100% / cool 0%
- **Palette (measured):** #fe750a orange 51%, #ffef20 gold 32%, #ffaf15 orange 8%, #ffffe9 light gold 5%, #ffff7f gold 3%

### Power opening

`open_inside` · skeleton · 2 parts · largest 175×175 · sheet `sheets/open_inside.webp`

- **Role:** The centre of the Power wheel opening.
- **Subject:** Yellow rings widening.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ffe437 69%, #ff8f00 22%, #ff1600 5%, #ffc800 2%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 6 bones, 6 slots, 1 animations as the file names them: start (0.57 s).
- **Construction:** 2 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 6 slots · animations: start (0.57 s)
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect · brightness 78% · saturation 85% · contrast 8% · warm 100% / cool 0%
- **Palette (measured):** #ffe437 gold 69%, #ff8f00 orange 22%, #ff1600 red 5%, #ffc800 gold 2%

### Power back flare

`bg_effect` · skeleton · 4 parts · largest 294×294 · sheet `sheets/bg_effect.webp`

- **Role:** A flare behind the Power wheel.
- **Subject:** An orange horizontal star flare in a disc.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ff8b00 60%, #feec2f 27%, #ff5500 12%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 6 bones, 4 slots, 3 animations as the file names them: end (0.67 s), open (1.5 s), start (1.0 s).
- **Construction:** 4 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 4 slots · animations: end (0.67 s), open (1.5 s), start (1.0 s)
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect · brightness 66% · saturation 94% · contrast 25% · warm 100% / cool 0%
- **Palette (measured):** #ff8b00 orange 60%, #feec2f gold 27%, #ff5500 orange 12%

### Power back disc

`bg_effect_part_1` · skeleton · 4 parts · largest 450×427 · sheet `sheets/bg_effect_part_1.webp`

- **Role:** A hot disc behind the Power wheel.
- **Subject:** A rough orange disc with a red halo and embers.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #ffb029 54%, #de1b0a 46%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 25 bones, 16 slots, 3 animations as the file names them: end (0.67 s), idle (3.0 s), start (1.0 s).
- **Construction:** 4 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 25 bones · 16 slots · animations: end (0.67 s), idle (3.0 s), start (1.0 s)
- **Measured:** mid-tone, vivid, warm, low contrast · brightness 51% · saturation 89% · contrast 2% · warm 100% / cool 0%
- **Palette (measured):** #ffb029 orange 54%, #de1b0a red 46%

### Heat glow behind the board

`mg_reel_glow` · skeleton · 6 parts · largest 151×176 · sheet `sheets/mg_reel_glow.webp`

- **Role:** The orange glow behind the reels and carts (animations for the base game, the bonus and each Expand height).
- **Subject:** Soft red-orange patches and faint rays.
- **Style:** Effect art: light shapes with no object in them.
- **Rendering:** Soft blooms and thin bright lines made to be added over the scene.
- **Colour:** Measured: #f05019 48%, #fdbb04 36%, #b1313e 9%, #ef8716 4%.
- **Lighting:** Emissive.
- **Materials:** Light and sparks.
- **Motion:** Spine 3.8.99 skeleton, 31 bones, 15 slots, 7 animations as the file names them: mg/loop (10.0 s), bg/loop (10.0 s), bg/loop_carts (10.0 s), bg/loop_expand_0 (10.0 s), bg/loop_expand_1 (10.0 s), bg/loop_expand_2 (10.0 s), bg/loop_expand_3 (10.0 s).
- **Construction:** 6 parts.
- **Notes:** This glow, not the backdrop file, is what makes the board look lit from behind in the game screens (inference from the animation names mg/loop, bg/loop).
- **Skeleton (from the file):** Spine 3.8.99 · 31 bones · 15 slots · animations: mg/loop (10.0 s), bg/loop (10.0 s), bg/loop_carts (10.0 s), bg/loop_expand_0 (10.0 s), bg/loop_expand_1 (10.0 s), bg/loop_expand_2 (10.0 s), bg/loop_expand_3 (10.0 s)
- **Measured:** mid-tone, vivid, warm, low contrast, glow or soft effect · brightness 54% · saturation 90% · contrast 19% · warm 98% / cool 1%
- **Palette (measured):** #f05019 orange 48%, #fdbb04 orange 36%, #b1313e red 9%, #ef8716 orange 4%


## Game interface

Buttons, counters and panels drawn for this game.

### Shop icon

`shop_icon` · atlas · 1 parts · largest 58×58 · sheet `sheets/shop_icon.webp`

- **Role:** The cart icon of the shop button at the right.
- **Subject:** A white shopping cart glyph.
- **Colour:** Measured: #ffffff 100%.
- **Construction:** 1 parts.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Shop icon, alternative

`shop_icon_soc` · atlas · 1 parts · largest 58×58 · sheet `sheets/shop_icon_soc.webp`

- **Role:** A star glyph in place of the cart.
- **Subject:** A white star.
- **Colour:** Measured: #ffffff 100%.
- **Construction:** 1 parts.
- **Notes:** The suffix _soc suggests a version for social casinos, where a purchase cart may not be shown (inference from the name only).
- **Measured:** bright, muted, neutral, low contrast, hard-edged, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Gamble wheel pieces

`gamble` · atlas · 6 parts · largest 114×89 · sheet `sheets/gamble.webp`

- **Role:** Pointer and markers of the gamble wheel.
- **Subject:** A gold arrow pointer with a blurred copy, a centre pin and green and red dots.
- **Colour:** Measured: #f4b700 58%, #fff800 10%, #e94402 8%, #5ed105 6%.
- **Construction:** 6 parts.
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect · brightness 64% · saturation 93% · contrast 41% · warm 90% / cool 6% · brighter towards: top-left (1)
- **Palette (measured):** #f4b700 orange 58%, #fff800 gold 10%, #e94402 orange 8%, #5ed105 green 6%, #060200 black 4%, #fefefe white 3%

### Shop tutorial pieces

`main-shop_popup` · atlas · 7 parts · largest 804×100 · sheet `sheets/main-shop_popup.webp`

- **Role:** White helper shapes of the shop's tutorial.
- **Subject:** Bars, a circle, pointer arrows and a close cross in plain white.
- **Colour:** Measured: #ffffff 100%.
- **Construction:** 7 parts.
- **Measured:** bright, muted, neutral, low contrast, hard-edged, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 100%

### Paytable pictures

`paytable` · atlas · 29 parts · largest 700×327 · sheet `sheets/paytable.webp`

- **Role:** The pictures of the paytable pages (seen in the game screens: 14 pages).
- **Subject:** Small composed diagrams of each feature, the jackpot plaques, the buy cards, the pots and the shop buttons.
- **Style:** The game's own pieces re-composed into explanatory diagrams.
- **Colour:** Measured: #4f060a 22%, #f39610 14%, #05397c 7%, #921b12 6%.
- **Construction:** 29 parts.
- **Notes:** The paytable's text is HTML; only these pictures are art.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 40% · saturation 83% · contrast 75% · warm 70% / cool 22% · brighter towards: top (8), top-right (4), top-left (3)
- **Palette (measured):** #4f060a dark red 22%, #f39610 orange 14%, #05397c dark blue 7%, #921b12 red 6%, #faec8e light gold 3%, #f81923 red 2%

### Loading bar

`preloader-preloader_progress_bar` · atlas · 3 parts · largest 483×11 · sheet `sheets/preloader-preloader_progress_bar.webp`

- **Role:** The loading bar under the Kendoo logo.
- **Subject:** Thin bars: a dark blue track, a white mask and a blue-cyan stripe.
- **Colour:** Measured: #fbfafd 33%, #3045cb 25%, #2cc1f7 16%, #0e0ba4 16%.
- **Construction:** 3 parts.
- **Measured:** mid-tone, saturated, warm and cool mixed, low contrast, hard-edged, strong highlights · brightness 56% · saturation 54% · contrast 18% · warm 0% / cool 67% · brighter towards: top (1)
- **Palette (measured):** #fbfafd light purple 33%, #3045cb blue 25%, #2cc1f7 cyan 16%, #0e0ba4 blue 16%, #5e78e4 blue 8%

### Second loading bar

`preloader-postloader_progress_bar` · atlas · 3 parts · largest 371×8 · sheet `sheets/preloader-postloader_progress_bar.webp`

- **Role:** The thinner bar on the intro card (seen at 100% in a game screen).
- **Subject:** A thin cyan stripe with mask and track.
- **Colour:** Measured: #00fdd9 46%, #ffffff 46%, #b4e1dc 9%.
- **Construction:** 3 parts.
- **Measured:** bright, saturated, warm and cool mixed, low contrast, hard-edged, strong highlights · brightness 88% · saturation 47% · contrast 0% · warm 0% / cool 46%
- **Palette (measured):** #00fdd9 cyan 46%, #ffffff white 46%, #b4e1dc light cyan 9%

### Feature labels under the carts

`titles_fc` · skeleton · 140 parts · largest 225×106 · sheet `sheets/titles_fc.webp`

- **Role:** The four labels EXPAND, POWER, COLLECT, MULTI between the carts and the reels (seen in the game screens).
- **Subject:** Four trapezoid plates in red, blue, green and purple with the feature's name in white capitals, each with a glowing frame.
- **Style:** Trapezoid plates, wider at the top, with a thin gold frame: the same sign shape as the feature labels under the carts.
- **Rendering:** Flat fill, gold frame, word with dark stroke; a bright copy of each word for flashes.
- **Colour:** Measured: #faf9f9 13%, #f42a03 10%, #fdfb19 9%, #2eff03 7%.
- **Materials:** Enamel signs.
- **Variants:** idle, impact, lvl_up, pending, glow_static; 30-frame letter sweeps per word.
- **Motion:** Spine 3.8.99 skeleton, 9 bones, 11 slots, 7 animations as the file names them: glow_static (0.0 s), idle (4.0 s), impact (0.6 s), lvl_up (1.0 s), pending (4.0 s), static (0.0 s), win (1.17 s).
- **Construction:** 140 parts.
- **Notes:** The drawn frame shows only one empty plate outline; the real labels are in the game screens.
- **Skeleton (from the file):** Spine 3.8.99 · 9 bones · 11 slots · animations: glow_static (0.0 s), idle (4.0 s), impact (0.6 s), lvl_up (1.0 s), pending (4.0 s), static (0.0 s), win (1.17 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 57% · saturation 78% · contrast 57% · warm 45% / cool 38% · brighter towards: top (21), top-left (2)
- **Palette (measured):** #faf9f9 white 13%, #f42a03 red 10%, #fdfb19 gold 9%, #2eff03 green 7%, #0e7601 dark green 5%, #f005fc magenta 5%

### Bonus total panel

`collect_panel` · skeleton · 9 parts · largest 396×114 · sheet `sheets/collect_panel.webp`

- **Role:** The red plate above the bonus board that shows the running total (seen at the end of the bonus: 54.00).
- **Subject:** A dark red trapezoid plate with a gold frame and a star flash.
- **Style:** Trapezoid plates, wider at the top, with a thin gold frame: the same sign shape as the feature labels under the carts.
- **Colour:** Measured: #a30101 73%, #530101 14%, #fda60e 5%.
- **Motion:** Spine 3.8.99 skeleton, 25 bones, 24 slots, 5 animations as the file names them: collect (0.67 s), collect_big (0.73 s), end (0.5 s), idle (1.67 s), start (0.5 s).
- **Construction:** 9 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 25 bones · 24 slots · animations: collect (0.67 s), collect_big (0.73 s), end (0.5 s), idle (1.67 s), start (0.5 s)
- **Measured:** dark, vivid, warm, low contrast · brightness 21% · saturation 98% · contrast 12% · warm 100% / cool 0%
- **Palette (measured):** #a30101 red 73%, #530101 dark red 14%, #fda60e orange 5%

### Gamble wheel

`wheel` · skeleton · 21 parts · largest 564×175 · sheet `sheets/wheel.webp`

- **Role:** The wheel of the Gamble feature; the paytable says a win can be gambled to double it or to win the Bonus Game.
- **Subject:** A round wheel with a green win zone and a red lose zone inside a gold rim.
- **Style:** Simple flat wheel.
- **Rendering:** Flat colour discs with a gold ring and a soft highlight.
- **Colour:** Measured: #941a14 18%, #fa2626 17%, #2a9006 16%, #40e905 13%.
- **Variants:** loop, loop_inactive, win.
- **Motion:** Spine 3.8.99 skeleton, 35 bones, 34 slots, 3 animations as the file names them: loop (0.0 s), loop_inactive (0.0 s), win (0.83 s).
- **Construction:** 21 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 35 bones · 34 slots · animations: loop (0.0 s), loop_inactive (0.0 s), win (0.83 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, low contrast · brightness 50% · saturation 86% · contrast 17% · warm 68% / cool 16% · brighter towards: top (2)
- **Palette (measured):** #941a14 red 18%, #fa2626 red 17%, #2a9006 dark green 16%, #40e905 green 13%, #fda423 orange 10%, #fff22b gold 7%

### Gamble loading dot

`gamble_load` · skeleton · 1 parts · largest 9×9 · sheet `sheets/gamble_load.webp`

- **Role:** A loading dot.
- **Subject:** One small red dot.
- **Colour:** Measured: #c42d06 100%.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 3 slots, 1 animations as the file names them: loop (0.97 s).
- **Construction:** 1 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 3 slots · animations: loop (0.97 s)
- **Measured:** mid-tone, vivid, warm, low contrast · brightness 29% · saturation 97% · contrast 0% · warm 100% / cool 0%
- **Palette (measured):** #c42d06 red 100%

### Mini gamble bar

`mini_gamble` · skeleton · 2 parts · largest 730×127 · sheet `sheets/mini_gamble.webp`

- **Role:** A dark bar for the small gamble prompt.
- **Subject:** A black translucent bar.
- **Colour:** Measured: #000000 100%.
- **Motion:** Spine 3.8.99 skeleton, 3 bones, 5 slots, 3 animations as the file names them: end (0.33 s), loop (0.0 s), start (0.33 s).
- **Construction:** 2 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 3 bones · 5 slots · animations: end (0.33 s), loop (0.0 s), start (0.33 s)
- **Measured:** dark, muted, neutral, low contrast, glow or soft effect · brightness 0% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #000000 black 100%

### Gamble popup

`gamble_popup` · skeleton · 8 parts · largest 744×505 · sheet `sheets/gamble_popup.webp`

- **Role:** The panel of the gamble.
- **Subject:** A purple panel with a gold rounded frame and sparks.
- **Colour:** Measured: #8c09c0 44%, #50057f 39%, #fb8b15 7%.
- **Motion:** Spine 3.8.99 skeleton, 23 bones, 31 slots, 3 animations as the file names them: end (1.0 s), loop (0.0 s), start (1.33 s).
- **Construction:** 8 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 23 bones · 31 slots · animations: end (1.0 s), loop (0.0 s), start (1.33 s)
- **Measured:** dark, vivid, cool, medium contrast, hard-edged · brightness 23% · saturation 92% · contrast 32% · warm 16% / cool 84%
- **Palette (measured):** #8c09c0 purple 44%, #50057f dark purple 39%, #fb8b15 orange 7%

### Respin counter

`respin_panel` · skeleton · 30 parts · largest 238×260 · sheet `sheets/respin_panel.webp`

- **Role:** The 1-2-3 counter under the bonus board (seen in the bonus screens).
- **Subject:** A small three-cell plate with the digits 1, 2, 3 that light in turn, in an orange and a blue version.
- **Style:** Trapezoid plates, wider at the top, with a thin gold frame: the same sign shape as the feature labels under the carts.
- **Colour:** Measured: #faac2b 22%, #07071c 21%, #470100 14%, #f25208 14%.
- **Variants:** 24 animations: levels per count for the bonus (bg) and a mini version.
- **Motion:** Spine 3.8.99 skeleton, 34 bones, 33 slots, 24 animations as the file names them: bg/1_static (0.0 s), mini_bg/1_static (0.0 s), bg/2_static (0.0 s), mini_bg/2_static (0.0 s), bg/3_static (0.0 s), mini_bg/3_static (0.0 s), bg/0_static (0.0 s), mini_bg/0_static (0.0 s) and 16 more.
- **Construction:** 30 parts.
- **Notes:** The blue version is for the Power Bonus Game (inference from the colour and the 'blue' part names).
- **Skeleton (from the file):** Spine 3.8.99 · 34 bones · 33 slots · animations: bg/1_static (0.0 s), mini_bg/1_static (0.0 s), bg/2_static (0.0 s), mini_bg/2_static (0.0 s), bg/3_static (0.0 s), mini_bg/3_static (0.0 s), bg/0_static (0.0 s), mini_bg/0_static (0.0 s), bg/lvl_1 (0.43 s), mini_bg/lvl_1 (0.43 s), bg/lvl_1_to_lvl_3 (0.73 s), mini_bg/lvl_1_to_lvl_3 (0.73 s), bg/lvl_2 (0.43 s), mini_bg/lvl_2 (0.43 s), bg/lvl_2_to_lvl_0 (0.67 s), mini_bg/lvl_2_to_lvl_0 (0.67 s), bg/lvl_2_to_lvl_3 (0.73 s), mini_bg/lvl_2_to_lvl_3 (0.73 s), bg/lvl_3 (0.43 s), mini_bg/lvl_3 (0.43 s), bg/lvl_3_to_lvl_0 (0.93 s), mini_bg/lvl_3_to_lvl_0 (0.93 s), bg/lvl_0_to_lvl_3 (0.73 s), mini_bg/lvl_0_to_lvl_3 (0.73 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, low contrast · brightness 35% · saturation 92% · contrast 22% · warm 70% / cool 30%
- **Palette (measured):** #faac2b orange 22%, #07071c black 21%, #470100 dark red 14%, #f25208 orange 14%, #1c00f0 blue 6%, #fdf57f gold 6%

### Jackpot panels

`jp_panel` · skeleton · 96 parts · largest 338×121 · sheet `sheets/jp_panel.webp`

- **Role:** The five jackpot signs at the left of the board: ROYAL, GRAND, MAJOR, MINOR, MINI with their amounts (seen in the game screens).
- **Subject:** Stacked trapezoid plates, each with its word above the amount: Royal and Grand in orange-red, Major in purple, Minor in blue and Mini in green, the last two sharing one row.
- **Style:** Trapezoid plates, wider at the top, with a thin gold frame: the same sign shape as the feature labels under the carts.
- **Rendering:** Flat saturated fills with a slight gradient, gold line frames, words in heavy capitals with a dark stroke.
- **Colour:** Measured: #ffd305 31%, #ffe547 13%, #fffef4 11%, #f47108 10%.
- **Lighting:** A comet of light travels round each frame (30-frame sequences).
- **Ambience:** A scoreboard that never stops moving.
- **Materials:** Enamel signs, gold trim.
- **Variants:** Animations for the base game (mg) and bonus (bg), loop and static per level; comet sequences run round the frames.
- **Motion:** Spine 3.8.99 skeleton, 59 bones, 62 slots, 32 animations as the file names them: mg/1_lvl_loop (2.0 s), bg/1_lvl_loop (2.0 s), mg/1_lvl_static (0.0 s), bg/1_lvl_static (0.0 s), mg/2_lvl_loop (1.5 s), bg/2_lvl_loop (1.5 s), mg/3_lvl_loop (1.0 s), bg/3_lvl_loop (1.0 s) and 24 more.
- **Construction:** 96 parts.
- **Notes:** The jackpot colours repeat the gem colours (green Mini, blue Minor, purple Major), and the top two take the game's orange-red.
- **Skeleton (from the file):** Spine 3.8.99 · 59 bones · 62 slots · animations: mg/1_lvl_loop (2.0 s), bg/1_lvl_loop (2.0 s), mg/1_lvl_static (0.0 s), bg/1_lvl_static (0.0 s), mg/2_lvl_loop (1.5 s), bg/2_lvl_loop (1.5 s), mg/3_lvl_loop (1.0 s), bg/3_lvl_loop (1.0 s), mg/grand (1.0 s), bg/grand (1.0 s), mg/grand_idle (4.67 s), bg/grand_idle (4.67 s), mg/grand_pending (1.0 s), bg/grand_pending (1.0 s), mg/grand_static (0.0 s), bg/grand_static (0.0 s), mg/major (1.0 s), bg/major (1.0 s), mg/major_static (0.0 s), bg/major_static (0.0 s), mg/mini (1.0 s), bg/mini (1.0 s), mg/mini_static (0.0 s), bg/mini_static (0.0 s), mg/minor (1.0 s), bg/minor (1.0 s), mg/minor_static (0.0 s), bg/minor_static (0.0 s), mg/royal_idle (4.67 s), bg/royal_idle (4.67 s), mg/royal_pending (1.0 s), bg/royal_pending (1.0 s)
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 64% · saturation 82% · contrast 33% · warm 88% / cool 6% · brighter towards: top (3)
- **Palette (measured):** #ffd305 gold 31%, #ffe547 gold 13%, #fffef4 light gold 11%, #f47108 orange 10%, #e43c15 red 8%, #960099 magenta 5%

### Power wheel progress arcs

`progress` · skeleton · 37 parts · largest 539×486 · sheet `sheets/progress.webp`

- **Role:** The arcs between the Power wheel's cells that fill as it advances (animations bar_01 to bar_06).
- **Subject:** Yellow glowing arc segments over the six-cell ring frame.
- **Colour:** Measured: #fff9b7 12%, #fff413 11%, #32a4f8 9%, #2a2654 8%.
- **Motion:** Spine 3.8.99 skeleton, 15 bones, 19 slots, 12 animations as the file names them: bar_01 (0.93 s), bar_01_start (0.93 s), bar_02 (0.93 s), bar_02_start (0.93 s), bar_03 (0.93 s), bar_03_start (0.93 s), bar_04 (0.93 s), bar_04_start (0.93 s) and 4 more.
- **Construction:** 37 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 15 bones · 19 slots · animations: bar_01 (0.93 s), bar_01_start (0.93 s), bar_02 (0.93 s), bar_02_start (0.93 s), bar_03 (0.93 s), bar_03_start (0.93 s), bar_04 (0.93 s), bar_04_start (0.93 s), bar_05 (0.93 s), bar_05_start (0.93 s), bar_06 (0.93 s), bar_06_start (0.93 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 57% · saturation 70% · contrast 57% · warm 48% / cool 52%
- **Palette (measured):** #fff9b7 light gold 12%, #fff413 gold 11%, #32a4f8 blue 9%, #2a2654 dark blue 8%, #fef971 gold 7%, #ff310c red 5%

### Gamble settings bar

`gamble_only` · skeleton · 2 parts · largest 837×140 · sheet `sheets/gamble_only.webp`

- **Role:** The blue bar in the shop with the gamble toggles (seen in the shop screen).
- **Subject:** A blue rounded bar with a divider.
- **Colour:** Measured: #033d7f 82%, #006bbc 14%, #000000 4%.
- **Motion:** Spine 3.8.99 skeleton, 6 bones, 8 slots, 1 animations as the file names them: loop (0.0 s).
- **Construction:** 2 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 6 bones · 8 slots · animations: loop (0.0 s)
- **Measured:** dark, vivid, cool, low contrast · brightness 22% · saturation 94% · contrast 20% · warm 0% / cool 100%
- **Palette (measured):** #033d7f dark blue 82%, #006bbc blue 14%, #000000 black 4%

### Loading dot

`load` · skeleton · 1 parts · largest 9×9 · sheet `sheets/load.webp`

- **Role:** A loading dot.
- **Subject:** One small grey dot.
- **Colour:** Measured: #d8dfe9 100%.
- **Motion:** Spine 3.8.99 skeleton, 2 bones, 3 slots, 1 animations as the file names them: loop (0.77 s).
- **Construction:** 1 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 2 bones · 3 slots · animations: loop (0.77 s)
- **Measured:** bright, muted, neutral, low contrast · brightness 87% · saturation 7% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #d8dfe9 light blue 100%

### Shop popup effects

`shop_popup` · skeleton · 7 parts · largest 564×175 · sheet `sheets/shop_popup.webp`

- **Role:** The flash when the shop opens.
- **Subject:** Flares, a ray ring and particles in orange.
- **Colour:** Measured: #ffb734 55%, #fe854e 12%, #ffcb83 11%, #faf539 8%.
- **Motion:** Spine 3.8.99 skeleton, 20 bones, 20 slots, 3 animations as the file names them: end (1.0 s), loop (0.0 s), start (1.33 s).
- **Construction:** 7 parts.
- **Notes:** The drawn frame is only a placeholder point.
- **Skeleton (from the file):** Spine 3.8.99 · 20 bones · 20 slots · animations: end (1.0 s), loop (0.0 s), start (1.33 s)
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 73% · saturation 73% · contrast 24% · warm 100% / cool 0%
- **Palette (measured):** #ffb734 orange 55%, #fe854e orange 12%, #ffcb83 light orange 11%, #faf539 gold 8%, #ff3414 red 7%, #fef7a5 light gold 5%

### Gold carts for the buy cards

`shields` · skeleton · 113 parts · largest 170×102 · sheet `sheets/shields.webp`

- **Role:** The four gold carts shown inside the shop cards, one animation per feature and a gold state each.
- **Subject:** The cart in gold with a tall heap, with trunks in the four colours and small gems among the parts.
- **Style:** As the big carts.
- **Rendering:** As the big carts.
- **Colour:** Measured: #fefefa 23%, #f68802 16%, #d0450d 9%, #ffea0c 8%.
- **Materials:** Gold, enamel, gems.
- **Variants:** collect, expand, multi, power, each plain and gold.
- **Motion:** Spine 3.8.99 skeleton, 142 bones, 165 slots, 8 animations as the file names them: collect (4.0 s), collect_gold (4.0 s), expand (4.0 s), expand_gold (4.0 s), multi (4.0 s), multi_gold (4.0 s), power (4.0 s), power_gold (4.0 s).
- **Construction:** 113 parts.
- **Notes:** A third copy of the cart art (after the big carts and the intro card), rebuilt at card size.
- **Skeleton (from the file):** Spine 3.8.99 · 142 bones · 165 slots · animations: collect (4.0 s), collect_gold (4.0 s), expand (4.0 s), expand_gold (4.0 s), multi (4.0 s), multi_gold (4.0 s), power (4.0 s), power_gold (4.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 61% · saturation 69% · contrast 63% · warm 59% / cool 28% · brighter towards: top-right (3), left (3), top (2)
- **Palette (measured):** #fefefa light gold 23%, #f68802 orange 16%, #d0450d orange 9%, #ffea0c gold 8%, #0b4bdd blue 5%, #058327 dark green 5%

### Shop card: Super Bonus (small)

`buy_bonus_super_fs_small` · skeleton · 20 parts · largest 359×360 · sheet `sheets/buy_bonus_super_fs_small.webp`

- **Role:** The Super Bonus card of the shop (seen in the game screens: the shop shows Random Bonus, '1-4 random features', and Super Bonus, '4 features guaranteed', each with a price and a BUY button).
- **Subject:** A rounded card with a ray burst in yellow on red, the heading in yellow capitals, a row of the four feature labels, and pale silhouettes where the game places the four gold carts.
- **Style:** Promotional card in the game's lettering, between a shop tile and a poster.
- **Rendering:** Flat rays, a glowing frame, glossy label plates.
- **Colour:** Measured: #a40100 43%, #fcfb6b 15%, #fbc60a 13%, #fceeb5 10%.
- **Lighting:** A burst from the centre.
- **Materials:** Enamel plates, light.
- **Motion:** Spine 3.8.99 skeleton, 40 bones, 47 slots, 1 animations as the file names them: loop (4.0 s).
- **Construction:** 20 parts.
- **Notes:** The pale cart-shaped blobs in the drawn frame are glow shapes behind carts that the game adds; the real card is in the game screens.
- **Skeleton (from the file):** Spine 3.8.99 · 40 bones · 47 slots · animations: loop (4.0 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 47% · saturation 82% · contrast 48% · warm 92% / cool 6% · brighter towards: top (5)
- **Palette (measured):** #a40100 red 43%, #fcfb6b gold 15%, #fbc60a gold 13%, #fceeb5 light gold 10%, #ec6c12 orange 3%, #fcf9f2 light orange 3%

### Shop card: Super Bonus (large)

`buy_bonus_super_fs_big` · skeleton · 21 parts · largest 718×484 · sheet `sheets/buy_bonus_super_fs_big.webp`

- **Role:** The Super Bonus card of the shop (seen in the game screens: the shop shows Random Bonus, '1-4 random features', and Super Bonus, '4 features guaranteed', each with a price and a BUY button).
- **Subject:** A rounded card with a ray burst in yellow on red, the heading in yellow capitals, a row of the four feature labels, and pale silhouettes where the game places the four gold carts.
- **Style:** Promotional card in the game's lettering, between a shop tile and a poster.
- **Rendering:** Flat rays, a glowing frame, glossy label plates.
- **Colour:** Measured: #a30100 63%, #fcc008 10%, #fcfa69 9%, #fceeb5 5%.
- **Lighting:** A burst from the centre.
- **Materials:** Enamel plates, light.
- **Variants:** buy, loop, start.
- **Motion:** Spine 3.8.99 skeleton, 48 bones, 54 slots, 3 animations as the file names them: buy (2.67 s), loop (4.0 s), start (0.67 s).
- **Construction:** 21 parts.
- **Notes:** The pale cart-shaped blobs in the drawn frame are glow shapes behind carts that the game adds; the real card is in the game screens.
- **Skeleton (from the file):** Spine 3.8.99 · 48 bones · 54 slots · animations: buy (2.67 s), loop (4.0 s), start (0.67 s)
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 35% · saturation 90% · contrast 52% · warm 95% / cool 3% · brighter towards: top (5)
- **Palette (measured):** #a30100 red 63%, #fcc008 gold 10%, #fcfa69 gold 9%, #fceeb5 light gold 5%, #fa790d orange 3%

### Shop card: Random Bonus (small)

`buy_bonus_fs_small` · skeleton · 19 parts · largest 362×374 · sheet `sheets/buy_bonus_fs_small.webp`

- **Role:** The Random Bonus card of the shop (seen in the game screens: the shop shows Random Bonus, '1-4 random features', and Super Bonus, '4 features guaranteed', each with a price and a BUY button).
- **Subject:** A rounded card with a ray burst in pink and magenta on dark purple, the heading in yellow capitals, a row of the four feature labels, and pale silhouettes where the game places the four gold carts.
- **Style:** Promotional card in the game's lettering, between a shop tile and a poster.
- **Rendering:** Flat rays, a glowing frame, glossy label plates.
- **Colour:** Measured: #330042 42%, #fcfb6b 14%, #ea0cc2 9%, #fdd1f5 8%.
- **Lighting:** A burst from the centre.
- **Materials:** Enamel plates, light.
- **Motion:** Spine 3.8.99 skeleton, 21 bones, 36 slots, 1 animations as the file names them: loop (4.0 s).
- **Construction:** 19 parts.
- **Notes:** The pale cart-shaped blobs in the drawn frame are glow shapes behind carts that the game adds; the real card is in the game screens.
- **Skeleton (from the file):** Spine 3.8.99 · 21 bones · 36 slots · animations: loop (4.0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 36% · saturation 83% · contrast 36% · warm 39% / cool 47% · brighter towards: top (5)
- **Palette (measured):** #330042 dark purple 42%, #fcfb6b gold 14%, #ea0cc2 magenta 9%, #fdd1f5 light magenta 8%, #a92f6f magenta 5%, #f8b32f orange 4%

### Shop card: Random Bonus (large)

`buy_bonus_fs_big` · skeleton · 24 parts · largest 718×484 · sheet `sheets/buy_bonus_fs_big.webp`

- **Role:** The Random Bonus card of the shop (seen in the game screens: the shop shows Random Bonus, '1-4 random features', and Super Bonus, '4 features guaranteed', each with a price and a BUY button).
- **Subject:** A rounded card with a ray burst in pink and magenta on dark purple, the heading in yellow capitals, a row of the four feature labels, and pale silhouettes where the game places the four gold carts.
- **Style:** Promotional card in the game's lettering, between a shop tile and a poster.
- **Rendering:** Flat rays, a glowing frame, glossy label plates.
- **Colour:** Measured: #350045 59%, #fcfa69 8%, #ef14bb 6%, #6b0702 3%.
- **Lighting:** A burst from the centre.
- **Materials:** Enamel plates, light.
- **Variants:** 17 animations (buy_1 … and loop, start): the buy plays a draw of which features come.
- **Motion:** Spine 3.8.99 skeleton, 55 bones, 51 slots, 17 animations as the file names them: buy_1 (5.0 s), buy_2 (5.0 s), buy_3 (5.0 s), buy_4 (5.0 s), buy_5 (5.0 s), buy_6 (5.0 s), buy_7 (5.0 s), buy_8 (5.0 s) and 9 more.
- **Construction:** 24 parts.
- **Notes:** The pale cart-shaped blobs in the drawn frame are glow shapes behind carts that the game adds; the real card is in the game screens.
- **Skeleton (from the file):** Spine 3.8.99 · 55 bones · 51 slots · animations: buy_1 (5.0 s), buy_2 (5.0 s), buy_3 (5.0 s), buy_4 (5.0 s), buy_5 (5.0 s), buy_6 (5.0 s), buy_7 (5.0 s), buy_8 (5.0 s), buy_9 (5.0 s), buy_10 (5.0 s), buy_11 (5.0 s), buy_12 (5.0 s), buy_13 (5.0 s), buy_14 (5.0 s), buy_15 (5.0 s), loop (3.0 s), start (0.67 s)
- **Measured:** dark, vivid, warm and cool mixed, medium contrast · brightness 26% · saturation 90% · contrast 34% · warm 29% / cool 61% · brighter towards: top (6)
- **Palette (measured):** #350045 dark purple 59%, #fcfa69 gold 8%, #ef14bb magenta 6%, #6b0702 dark red 3%, #b0326d magenta 2%

### Shop and gamble buttons

`button` · skeleton · 29 parts · largest 164×164 · sheet `sheets/button.webp`

- **Role:** The BUY button and the gamble toggles of the shop.
- **Subject:** Pill-shaped glossy buttons in lime green, yellow, grey and blue, and small round toggle knobs with tick and cross marks.
- **Style:** Glossy candy pills.
- **Rendering:** Two-tone gradient with a top highlight.
- **Colour:** Measured: #fcc80e 14%, #588d08 11%, #03a109 10%, #71f008 10%.
- **Materials:** Glossy plastic.
- **Variants:** 21 animations for active, inactive, on, off and pushed states.
- **Motion:** Spine 3.8.99 skeleton, 12 bones, 31 slots, 21 animations as the file names them: active_gamble (0.0 s), big_active_gamble (0.0 s), big_inactive_gamble (0.0 s), big_on_gamble (0.0 s), big_push_off_gamble (0.33 s), big_push_on_gamble (0.33 s), end_push_green (0.33 s), end_push_yellow (0.33 s) and 13 more.
- **Construction:** 29 parts.
- **Skeleton (from the file):** Spine 3.8.99 · 12 bones · 31 slots · animations: active_gamble (0.0 s), big_active_gamble (0.0 s), big_inactive_gamble (0.0 s), big_on_gamble (0.0 s), big_push_off_gamble (0.33 s), big_push_on_gamble (0.33 s), end_push_green (0.33 s), end_push_yellow (0.33 s), idle_green (3.0 s), idle_yellow (3.0 s), inactive_gamble (0.0 s), inactive_gamble_on (0.0 s), inactive_green_btn (0.33 s), inactive_yellow_btn (0.33 s), on_gamble (0.0 s), push_inactive_to_on_gamble (0.33 s), push_off_gamble (0.33 s), push_on_gamble (0.33 s), push_on_to_inactive_gamble (0.33 s), start_push_green (0.33 s), start_push_yellow (0.33 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, low contrast · brightness 51% · saturation 76% · contrast 20% · warm 25% / cool 46% · brighter towards: bottom (5), top (2)
- **Palette (measured):** #fcc80e gold 14%, #588d08 dark green 11%, #03a109 green 10%, #71f008 green 10%, #a5ea17 green 8%, #7d7e7e grey 8%


## Typography

Embedded fonts and lettering.

### Big win numerals

`big_wins_font` · atlas · 1 parts · largest 1469×167 · sheet `sheets/big_wins_font.webp`

- **Role:** The amount under a big win banner.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Yellow-to-orange fill, dark red stroke and extrusion; the largest set, 167 px high.
- **Colour:** Measured: #4f0400 27%, #fba806 21%, #b41802 17%, #fff7a3 9%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 44% · saturation 90% · contrast 92% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #4f0400 dark red 27%, #fba806 orange 21%, #b41802 red 17%, #fff7a3 light gold 9%, #fff61a gold 7%, #8c1f03 dark red 7%

### Collect value numerals

`collect_bit` · atlas · 1 parts · largest 533×54 · sheet `sheets/collect_bit.webp`

- **Role:** Values on the green Collect pot.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Pale green fill, dark green stroke.
- **Colour:** Measured: #042700 51%, #b1f5b3 18%, #0e630c 14%, #478b48 9%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 36% · saturation 76% · contrast 85% · warm 0% / cool 50% · brighter towards: top (1)
- **Palette (measured):** #042700 black 51%, #b1f5b3 light green 18%, #0e630c dark green 14%, #478b48 green 9%, #7fca82 green 7%

### Bonus total numerals

`collect_panel_font` · atlas · 1 parts · largest 572×65 · sheet `sheets/collect_panel_font.webp`

- **Role:** The total on the bonus panel.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Yellow fill, red stroke.
- **Colour:** Measured: #320300 25%, #ffe709 21%, #b11302 17%, #f7a20f 13%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 44% · saturation 92% · contrast 92% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #320300 black 25%, #ffe709 gold 21%, #b11302 red 17%, #f7a20f orange 13%, #6f1201 dark red 7%, #c55c0f orange 6%

### Expand value numerals

`expand_bit` · atlas · 1 parts · largest 533×54 · sheet `sheets/expand_bit.webp`

- **Role:** Values on the red Expand pots.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Cream fill, dark red stroke.
- **Colour:** Measured: #2f0000 36%, #7b0904 20%, #fbe0c2 19%, #a2594b 10%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 32% · saturation 75% · contrast 90% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #2f0000 black 36%, #7b0904 dark red 20%, #fbe0c2 light orange 19%, #a2594b red 10%, #ac180a red 7%, #d5a48b orange 7%

### Jackpot amount numerals

`jp_panel_font` · atlas · 1 parts · largest 325×35 · sheet `sheets/jp_panel_font.webp`

- **Role:** The amounts on the Major, Minor and Mini panels (seen in the game screens).
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** White fill with a dark stroke, small.
- **Colour:** Measured: #1f0408 32%, #fdf5eb 26%, #e1beb2 16%, #785b59 11%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, saturated, warm, high contrast, strong highlights · brightness 48% · saturation 44% · contrast 98% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #1f0408 black 32%, #fdf5eb light orange 26%, #e1beb2 light orange 16%, #785b59 red 11%, #572a27 dark red 8%, #a78681 red 6%

### Royal and Grand numerals

`jp_royal_grand` · atlas · 1 parts · largest 512×64 · sheet `sheets/jp_royal_grand.webp`

- **Role:** The amounts on the Royal and Grand panels.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Yellow fill with a dark red stroke.
- **Colour:** Measured: #5a0d01 31%, #f9e032 22%, #ce9113 17%, #f9e87c 12%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 52% · saturation 83% · contrast 87% · warm 100% / cool 0%
- **Palette (measured):** #5a0d01 dark red 31%, #f9e032 gold 22%, #ce9113 orange 17%, #f9e87c gold 12%, #9c4e12 brown 10%, #ca984d orange 5%

### Multiplier numerals

`multi_bit` · atlas · 1 parts · largest 533×54 · sheet `sheets/multi_bit.webp`

- **Role:** The x2, x3, x5 tags of the Multi feature.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Pink fill, purple stroke.
- **Colour:** Measured: #2b0036 34%, #fbcefb 21%, #620677 19%, #9022a3 15%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 32% · saturation 72% · contrast 86% · warm 18% / cool 64% · brighter towards: top (1)
- **Palette (measured):** #2b0036 black 34%, #fbcefb light magenta 21%, #620677 dark purple 19%, #9022a3 magenta 15%, #ae62bb magenta 6%, #d792de magenta 5%

### Power value numerals

`power_bit` · atlas · 1 parts · largest 533×54 · sheet `sheets/power_bit.webp`

- **Role:** Values on the blue Power pot.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Pale blue fill, dark blue stroke.
- **Colour:** Measured: #0a0a40 33%, #ddf0fb 20%, #0c238d 18%, #164bca 13%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, cool, high contrast, strong highlights · brightness 35% · saturation 69% · contrast 93% · warm 0% / cool 100% · brighter towards: top (1)
- **Palette (measured):** #0a0a40 dark blue 33%, #ddf0fb light blue 20%, #0c238d dark blue 18%, #164bca blue 13%, #5877ca blue 9%, #9bbae9 light blue 6%

### Symbol value numerals

`symbol_bit` · atlas · 1 parts · largest 481×49 · sheet `sheets/symbol_bit.webp`

- **Role:** The value written on a gold nugget (seen in the bonus screens: 1.00, 2.00 …).
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Cream fill with a dark red stroke.
- **Colour:** Measured: #530202 41%, #f7f3a4 24%, #920b0a 12%, #93473d 10%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 37% · saturation 72% · contrast 91% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #530202 dark red 41%, #f7f3a4 light gold 24%, #920b0a red 12%, #93473d red 10%, #cfb691 orange 6%, #cf0000 red 4%

### Symbol value numerals, blurred

`symbol_bit_blur` · atlas · 1 parts · largest 512×64 · sheet `sheets/symbol_bit_blur.webp`

- **Role:** The same values while reels spin.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** The symbol numerals with baked vertical blur.
- **Colour:** Measured: #bb865a 35%, #660504 31%, #972a1e 19%, #eadc8d 15%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 40% · saturation 69% · contrast 82% · warm 100% / cool 0%
- **Palette (measured):** #bb865a orange 35%, #660504 dark red 31%, #972a1e red 19%, #eadc8d gold 15%

### Win numerals

`win_1b` · atlas · 1 parts · largest 767×86 · sheet `sheets/win_1b.webp`

- **Role:** The win amount over the reels.
- **Subject:** The digits 0 to 9 with comma, point and x.
- **Style:** A heavy rounded sans numeral, the same shapes in every one of the game's number fonts.
- **Rendering:** Yellow-to-orange fill with a red stroke, 86 px high.
- **Colour:** Measured: #9b1502 25%, #4c0300 21%, #fca906 21%, #fff414 9%.
- **Lighting:** A top highlight inside each digit.
- **Construction:** A bitmap font: one page with an XML table of glyph boxes (the reader does not cut the glyphs; the page is kept whole).
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 46% · saturation 89% · contrast 92% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #9b1502 red 25%, #4c0300 dark red 21%, #fca906 orange 21%, #fff414 gold 9%, #fff6a4 light gold 8%, #d05512 orange 8%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `gr_ui_textures`: 43 parts
- `gr_autoplay_textures`: 8 parts
- `gr_bet_menu_textures`: 4 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Gilroy-Regular (?); League Spartan (Bold); League Spartan (Regular); My Font (Regular); Myriad Pro (Bold); Myriad Pro (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 3299 components cut from 132 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
