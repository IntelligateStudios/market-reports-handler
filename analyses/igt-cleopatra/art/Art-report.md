# Cleopatra: art report

igt · run `2026-11-26-1045-igt-cleopatra` · captured 2026-11-26

Source: the provider's free-play demo, https://platform.ka.rgsgames.com/skb/gateway?skincode=AG01&countrycode=US&nscode=AGLC&language=en&technology=HTML&currencycode=FPY&softwareid=200-1173-001&presenttype=STD

**Extracted:** 705 named components from 19 textures in 19 atlases; 0 Spine skeletons; 14 frame sequences (611 frames); 2 fonts. Grouped into 19 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A land-based classic kept almost as it was: a gold and red-lacquer Egyptian shrine of 5x3 reels on a one-colour purple dusk, gold-and-enamel symbols each on its own coloured cloth, and a single face, Cleopatra's green eyes under a jewelled headdress, as key art, logo and wild.

**Style.** Casino cabinet glass art: comic-style glamour illustration with hard outlines for Cleopatra and the logo, airbrushed gold-and-enamel objects for the picture symbols, gold Art Nouveau letters with lotus buds for the card ranks, and a flat poster-like Sphinx for the scatter. The cabinet and plaques are cleaner, smoother illustration; the backdrop is a one-hue tinted photo-based picture (inference); the one fire effect is naturalistic.

**Rendering.** Hard-edged throughout (soft edge 0.05 over the game's art), smooth airbrushed gradients inside thin dark outlines, white streak highlights on gold, a woven texture on the symbol cloths and a fibre texture on the free-spin papyrus. Everything is a flat finished picture: nothing is layered or lit by the scene.

**Colour.** Gold on purple. Measured over the game's own art the palette is gold #f0c70a (15%), orange #de7f25 (13%), near-black #120a04, sand #eeca79, brown #67370a, red #861425 and cream #f9e9bc; saturation 0.76, warm 90% against cool 6%. The backdrop is the counter-colour, magenta #9d1cae and purple #6a0cca in the base game, and turns dark red #880d30 in the free spins. The reel cells are cream #f8e6bf in the base game and tan #e8c684 in the free spins. Each picture symbol owns a cloth colour (scarab green #3a8467, lotus violet #753e7e, cartouche blue #3f55b1, crook and flail yellow #e8ad1e, eye red #b92911) and each of the 20 paylines owns a bead colour that its line and cell frames repeat.

**Lighting.** No scene lighting. Each object carries its own frontal highlight; the cabinet has banded reflections like polished metal; the Sphinx (scatter and Big Win) and the fire are self-lit. The backdrop is a plain vertical gradient with no sun or lamp.

**Ambience.** Opulent, calm and familiar: a jewel box at dusk. The base game is cool purple around warm gold; the free spins heat the whole screen to crimson and age the reels to tan papyrus. Nothing moves until a win, so the game feels like a machine rather than a scene.

**Shape language.** Square opaque cells in a strict grid; a symmetrical shrine frame with a curved cornice, two lotus columns and a boat-shaped base with fan prows; round beads and round buttons; the lotus fan as the repeating ornament (on the letters, the logo, the cabinet, the plaque).

**Materials.** Polished gold, blue and turquoise enamel, cut gems, red lacquer, woven cloth, cream paper and tan papyrus, sandstone, glass beads and glass-dome buttons, fire.

**Typography and lettering.** The wordmark is drawn: red capitals with a yellow inner line, a blue band and a gold rim, the C and the R enlarged, in the same comic manner as the face. The words on symbols (SCATTER, BONUS, DOUBLE) are fat cartoon capitals in red-to-yellow or red on violet. Everything else is live text in two embedded sans-serif fonts, Lato Bold and Roboto Regular: yellow for the free-spin messages, blue capitals for BIG WIN, white amounts, orange labels and green win figures on the meter bar. The paytable is a plain white web page with a blue-headed table.

**Motion.** No skeletons and no timelines in the files: all animation is frame by frame, as full pictures. The wild has an 80-frame sequence in which the cell turns gold and two hands cross and open over the logo plate to show DOUBLE (and a second 80-frame version that keeps the logo); the Sphinx has 40-frame sequences in which the face glows, flames rise and SCATTER or BONUS wipes in; the Big Win is a 40-frame glow pulse of a Sphinx over a plaque with a counting number; the transition into and out of the free spins is 32 frames of fire inside a gold frame on black; a payline bead gets a 30-frame sparkle. The regular symbols do not animate: a win greys every other cell, frames the winning cells in the line's colour, draws the line to its bead and shows the amount in a small black tag (seen on the screens). The backdrop and cabinet never move.

**Variants and themes.** Two modes made by recolour: backdrop purple or crimson, cabinet window cream or tan, every symbol on a cream or tan ground, and each animated sequence shipped once per ground. Scatter in two words (SCATTER, BONUS), wild in two plates (DOUBLE, Cleopatra). Twenty bead colours and a grey. Buttons in four states. The client ships a desktop pack (symbols 244x244, backdrop 1920x1080, read here) and a mobile pack with the same art at half size in fewer atlases (symbols 122x122; captured first by mistake, see the record).

**How it is built.** A small package: 19 textures, 705 named sprites, 14 frame sequences with 611 frames, 2 fonts. Every atlas is a TexturePacker JSON with the studio's own names. Symbols are untrimmed opaque 244x244 cells with the ground baked in; the cabinet is one 1645x1080 picture per mode with the window painted in and a divider grid laid over the symbols; the backdrop is one mirrored JPEG per mode. Mode differences are made by whole second copies, not by layers or tints: 320 of the 611 animation frames are the wild, and half of all animation frames exist only to change a cell margin from cream to tan. Text is live, so the art holds no language.

**Consistency.** The identity is tight where it matters: one face and one wordmark serve as key art, logo and wild, and gold with lotus ornament runs through symbols, cabinet and plaques. Around that the manners differ openly: outlined comic face, airbrushed objects, flat Sphinx, smooth vector-like cabinet, tinted photo backdrop, naturalistic fire, and generic blue and red web buttons for autospin. The game reads as one because of its strict grid, its gold and its single counter-colour, not because the rendering is uniform.

**What to take from it.** (1) A top-20 game in this report runs on 19 textures and frame-by-frame art with no skeletons, no particles and a backdrop that never moves: at this end of the market, recognition and readability outweigh production depth. Inference: its rank rests on the brand's long history, not on the art's finish. (2) One colour per symbol. Each picture symbol sits on its own cloth colour and each rank has its own inlay, so the board is read by colour before shape; worth copying in any dense 5x3 set. (3) One key image used three ways (loading picture, logo, wild) gives a simple game a strong face. Plan the wild, the logo and the key art as one drawing. (4) The rule is shown on the symbol: the wild's plate changes to DOUBLE when it doubles a win, and the scatter writes SCATTER or BONUS on itself. Stating the mechanic in the art, at the point the player is looking, replaces a popup. (5) A feature mode from recolour alone: backdrop hue, cell ground and meter bar change, nothing else. It is cheap and it reads at once; with layered symbols and a tint it would cost a fraction of the copies shipped here. (6) Payline colour as the win language (bead, line and cell frame in one colour, everything else greyed) is clear with one line and gets muddy with several close colours; a modern version would keep the idea with fewer, better separated colours. (7) For AI art work: the set is a clean reference for 'classic land-based Egyptian' as a style target (gold and enamel objects on coloured cloth, Art Nouveau gold letters, comic glamour face), and its flat, unlayered cells are easy to match piece for piece in a concept.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm, high contrast, hard-edged · brightness 48% · saturation 76% · contrast 75% · warm 90% / cool 6% · brighter towards: top (94), bottom (33), left (33)

Palette: #f0c70a gold 16%, #de7f25 orange 13%, #120a04 black 12%, #eeca79 orange 10%, #67370a brown 9%, #861425 red 9%, #f9e9bc light orange 7%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 2 | 18% | 89% | 15% | 60% / 23% | #850d35 dark red 56%, #9d1cae magenta 18%, #6a0cca purple 17% |
| Reel board | 3 | 65% | 50% | 57% | 97% / 3% | #e5c487 orange 28%, #fce9cc light orange 26%, #904715 brown 19% |
| Symbols | 3 | 50% | 71% | 84% | 96% / 3% | #db882b orange 25%, #89180b dark red 14%, #f8e7bb light orange 10% |
| Characters | 4 | 50% | 85% | 87% | 92% / 5% | #efc605 gold 29%, #cd7a05 orange 14%, #0c0d02 black 13% |
| Logo and title | 1 | 53% | 77% | 49% | 84% / 14% | #e8b213 orange 29%, #c07017 orange 18%, #f2cf58 gold 7% |
| Win celebrations and banners | 3 | 46% | 65% | 61% | 82% / 7% | #0c0403 black 22%, #fccd5c orange 22%, #f66a2b orange 22% |
| Effects | 1 | 50% | 72% | 92% | 100% / 0% | #fce780 gold 26%, #270c04 black 21%, #743015 brown 19% |
| Game interface | 1 | 36% | 67% | 52% | 89% / 4% | #773f10 brown 34%, #150a03 black 24%, #a97a39 orange 12% |
| Provider interface (shared) | 1 | 71% | 100% | 0% | 100% / 0% | #ffb100 orange 100% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Base-game backdrop: purple sky and temple columns

`backgroundBasegame` · atlas · 1 parts · largest 1920×1080 · sheet `sheets/backgroundBasegame.webp`

- **Role:** The full-screen picture behind the cabinet in the base game.
- **Subject:** An empty sky graded from violet at the top to magenta, with a ruined Egyptian colonnade (papyrus-capital columns, a statue, drifted sand) at the lower left, mirrored at the lower right.
- **Style:** A tinted photograph or photo-based painting reduced to one hue (inference from the grain and detail of the columns), unlike the drawn art in front of it.
- **Rendering:** Low contrast (0.167) and soft; the columns are a monochrome magenta print fading into the gradient. A 1920x1080 JPEG.
- **Colour:** Magenta #9d1cae (36%), purple #6a0cca (33%), dark magenta #81145f and #540b36: two hues only, magenta 54% and purple 46%.
- **Lighting:** No light source drawn: a vertical gradient, darker at the top, with the columns slightly darker than the haze around them.
- **Ambience:** Dusk over ruins, calm and a little unreal; its job is to stay behind the gold cabinet, which it does by being the cabinet's complementary colour.
- **Materials:** Stone and sand, seen as a tint.
- **Variants:** One of two: the free-spin backdrop is the same picture in red.
- **Motion:** None: a still. Nothing in it moves on the screens.
- **Construction:** A single 1920x1080 JPEG, the centre left empty because the cabinet covers it; the two sides are one picture mirrored.
- **Notes:** Mirrored sides and a single hue are the cheapest possible backdrop; it works because the cabinet carries all the detail.
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 20% · saturation 88% · contrast 17% · warm 27% / cool 46%
- **Palette (measured):** #9d1cae magenta 36%, #6a0cca purple 33%, #81145f dark magenta 19%, #540b36 dark magenta 10%

### Free-spin backdrop: crimson sky and temple columns

`backgroundFreespins` · atlas · 1 parts · largest 1920×1080 · sheet `sheets/backgroundFreespins.webp`

- **Role:** The full-screen picture behind the cabinet during the free spins.
- **Subject:** The same mirrored colonnade and empty sky, recoloured from purple to red.
- **Style:** As the base backdrop: a one-hue tinted photo-based picture.
- **Rendering:** Low contrast (0.134), dark (brightness 0.155). A 1920x1080 JPEG.
- **Colour:** Dark red #880d30 (92%) and #3a050b: red 85% of hues, magenta 15%.
- **Lighting:** A vertical gradient, darker wine at the top, brighter crimson in the middle.
- **Ambience:** Hotter and heavier than the base game: the mode change is said by one colour shift of the whole screen.
- **Materials:** Stone and sand as a red tint.
- **Variants:** The recolour of backgroundBasegame.
- **Motion:** None: a still. The game cuts to it through the gold-frame transition.
- **Construction:** A single JPEG, the same composition as the base backdrop.
- **Notes:** A feature mode made from a hue shift of the backdrop plus the tan symbol grounds.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 16% · saturation 91% · contrast 13% · warm 92% / cool 0%
- **Palette (measured):** #880d30 dark red 92%, #3a050b dark red 8%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel cabinet, base game, and the reel dividers

`frameII` · atlas · 2 parts · largest 1645×1080 · sheet `sheets/frameII.webp`

- **Role:** The frame the reels sit in during the base game, and the grid of thin dividers drawn over the cells.
- **Subject:** A shrine-like cabinet: a curved gold cornice with rows of hieroglyphs, red-brown lacquered beams, two side columns with blue lotus capitals, a gold boat-shaped base ending in two lotus-fan prows, around a plain cream window. `reelsFrame` is a 5-column grid of thin bead-like red, blue and gold dividers with a dark outer line.
- **Style:** Clean vector-like illustration with smooth metallic gradients, flatter and more modern in finish than the symbols.
- **Rendering:** Long smooth gradients banded like polished metal, thin gold edge lines, small flat hieroglyphs in darker gold; hardly any texture except a light mottling on the boat base.
- **Colour:** Cream window #fce9cb (53%), red-brown #904815 (19%), bronze #9e713b, gold #dca721; blue only in the lotus capitals and fans. The divider grid adds blue #37598f and red #b2431a.
- **Lighting:** Reflections run as vertical light bands across the beams, as on a polished cylinder; no cast shadows except a soft inner shadow around the window.
- **Ambience:** A jewel box or shrine holding the reels: formal, symmetrical, warm.
- **Materials:** Polished gold, red lacquer or copper, blue enamel lotus petals.
- **Variants:** Base-game version; frameIII is the free-spin version with a tan window. The divider grid is shared.
- **Motion:** None in the files: stills. Inference from the screens: the cabinet never moves.
- **Construction:** Two parts: the cabinet with its cell ground painted in as one 1645x1080 picture, and the divider grid (1306x762) laid over the symbols. The symbols carry their own grounds, so the window colour shows only between and behind them.
- **Notes:** The window colour matches the symbol paper (#f8e6bf against #fce9cb), which hides the seams between cells.
- **Measured:** bright, saturated, warm, high contrast, hard-edged, strong highlights · brightness 68% · saturation 45% · contrast 63% · warm 96% / cool 4%
- **Palette (measured):** #fce9cb light orange 49%, #914715 brown 19%, #9d713b orange 14%, #dca722 orange 8%, #191110 black 2%, #d0c1a7 orange 2%

### Reel cabinet, free spins

`frameIII` · atlas · 1 parts · largest 1645×1080 · sheet `sheets/frameIII.webp`

- **Role:** The same cabinet for the free spins.
- **Subject:** The cabinet of frameII with the window in tan.
- **Style:** As frameII.
- **Rendering:** As frameII; the only change is the window fill.
- **Colour:** Tan #e6c487 (56%) in place of cream, with the same red-brown #904815, bronze #9d6f38 and gold #dda81f.
- **Lighting:** As frameII.
- **Ambience:** Slightly darker and older, matching the tan symbol grounds and the crimson backdrop.
- **Materials:** Gold, red lacquer, blue enamel.
- **Variants:** The free-spin copy of frameII's cabinet.
- **Motion:** None: a still.
- **Construction:** One 1645x1080 picture: the whole cabinet is shipped a second time for a change of window colour.
- **Notes:** A third instance of the same habit: a full copy where a tint or a layer would do.
- **Measured:** bright, saturated, warm, medium contrast, hard-edged · brightness 63% · saturation 56% · contrast 51% · warm 99% / cool 1%
- **Palette (measured):** #e6c487 orange 56%, #904815 brown 19%, #9d6f38 orange 13%, #dda81f orange 8%, #bb9a5f orange 2%

### Payline beads and their sparkle

`pips` · atlas · 51 parts · largest 70×63 · sheet `sheets/pips.webp`

- **Role:** The twenty payline markers down the two sides of the reels, and the glint that plays on one.
- **Subject:** Twenty round glass beads in gold rings, each a different colour, an unlit grey one, and a 30-frame white sparkle.
- **Style:** Small glossy jewel icons, in the manner of interface buttons more than of the Egyptian art.
- **Rendering:** Each bead is a tinted sphere with a soft white highlight at the top and a darker rim, in a thin gold ring; soft-edged (0.357). The sparkle is a white streaked disc with a star flare.
- **Colour:** One colour per line, measured bead by bead: pale pink #dfbfdf, amber #d09532, magenta #d033d0, red #cd2e2d, violet #7657d1, yellow #d0b32e, pinks #d37ad3 and #d49bd4, green #70ce51, orange #cd6a2d, purple #9337d1, cream #d4d4b1, blue #3793d1, dark green #2e632a, blue #5676d1, turquoise #7ad3d3, mint #77d093, green #5eaa48, sky #58b3d1, green #48873c. The win line and the cell frames are drawn in the same colour (seen on the screens).
- **Lighting:** A highlight at the top of each bead, as from above.
- **Ambience:** A string of coloured gems: the one playful, many-coloured element on a gold board.
- **Materials:** Glass or gemstone in a gold setting.
- **Variants:** 20 colours and one inactive grey; lines not played show grey (inference from the name `Pip_inactive`).
- **Motion:** PipAnim, 30 frames: a white disc fades in over the bead, a streak crosses it and a four-point star flares and fades. On a win the line is drawn from its bead across the reels.
- **Construction:** One atlas of 51 small parts (beads 48x48, sparkle up to 70x63); the sparkle is one white sequence reused over any bead.
- **Notes:** Colour-coding the paylines is the game's whole win language: bead, line, cell frame share one colour. Several of the twenty colours are close to each other (three greens, three pinks).
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 67% · saturation 39% · contrast 58% · warm 43% / cool 22%
- **Palette (measured):** #fbfbfb white 30%, #d9bed9 light magenta 7%, #a97d0f brown 7%, #231b03 black 5%, #ceac32 gold 4%, #5b5324 brown 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### The thirteen reel symbols, base-game set

`symbols` · atlas · 13 parts · largest 244×244 · sheet `sheets/symbols.webp`

- **Role:** The first frame of every symbol as the reels show it at rest: the Sphinx scatter, five picture symbols, six card ranks and the Cleopatra wild.
- **Subject:** Sphinx head (B01, scatter); scarab (S01), lotus fan with a coiled stem (S02), gold cartouche (S03), crook and flail (S04), Eye of Horus (S05); A, K, Q, J, 10 and 9 (S06 to S11); Cleopatra's eyes under a jewelled gold headdress with the game's logo across the lower half (W01, wild).
- **Style:** Two manners in one set. The picture symbols are airbrushed gold-and-enamel objects on a square of torn, woven coloured cloth; the card ranks are gold Art Nouveau letters with lotus buds on plain cream. The Sphinx is flatter and more graphic (banded reds and oranges), and the wild is a tight comic-style crop of a face.
- **Rendering:** Smooth airbrushed gradients inside thin dark outlines, hard-edged (measured soft edge 0.0), with white streak highlights on the gold; the cloth grounds carry a fine weave texture and a ragged edge. Each picture is a full 244x244 opaque cell, ground included.
- **Colour:** Cream cell ground #f8e6bf leads the sheet (30%), with gold #ecbe1a, brown #7d510f and red #a51e0e. Each picture symbol owns one ground colour, measured on its own cell: scarab on green #3a8467, lotus on violet #753e7e, cartouche on blue #3f55b1, crook and flail on yellow #e8ad1e, Eye of Horus on red #b92911; the Sphinx is dark red #9a1f0e and orange #d87f38.
- **Lighting:** No single scene light: each object has its own frontal highlight, with streaks on the gold and a soft dark shadow under it on the cloth. The measure finds the light mostly from the top right.
- **Ambience:** Rich, ornamental and a little dated: a land-based cabinet's symbol set kept as it was, readable at a glance through one colour per symbol.
- **Materials:** Polished gold, blue and turquoise enamel inlay, a red faceted gem on the K, woven linen or papyrus cloth, cream paper.
- **Variants:** Thirteen designs. Every regular symbol also exists in a free-spin ground (symbolsII) and the scatter and wild as frame sequences (symbolsI, symbolsIII to VI).
- **Motion:** None in this sheet: these are stills; the reels spin them with a vertical blur (seen on the screens).
- **Construction:** One TexturePacker atlas of 13 untrimmed 244x244 cells, cut by name. The symbol and its ground are baked into one picture, so nothing is layered: a win is shown by the game around the cell, not inside it.
- **Notes:** The S-numbers follow the paytable order from the scarab down to the 9. This sheet repeats the base-game stills that also sit in symbolsII; inference: it is the set the reels load first.
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged, strong highlights · brightness 59% · saturation 57% · contrast 76% · warm 78% / cool 18% · brighter towards: top-right (2), right (1), top (1)
- **Palette (measured):** #f8e6bf light orange 30%, #7d510f brown 9%, #bb9255 orange 9%, #ecbe1a gold 8%, #d48024 orange 7%, #160f0a black 4%

### Sphinx scatter: trigger and scatter-win sequences

`symbolsI` · atlas · 162 parts · largest 244×244 · sheet `sheets/symbolsI.webp`

- **Role:** The scatter's two animations, each in both grounds: BONUS when three or more trigger the free spins, SCATTER when it pays.
- **Subject:** A front view of a Sphinx head in a striped nemes headdress, in banded red, orange and cream, on an orange desert ground; flames and a word rise over its lower half.
- **Style:** Flat, graphic and poster-like, the least modelled symbol of the set; the lettering is fat cartoon capitals in a red-to-yellow gradient with a dark outline.
- **Rendering:** Hard-edged bands of colour with a soft yellow glow that brightens the face from the centre; flames are flat yellow spikes; the word sits on a solid yellow bar.
- **Colour:** Orange #dc872c (27%), dark red #8a170b, near-black #180c05, yellow #fbee1b for the flames and bar, cream #faebc2; 100% warm by the measure.
- **Lighting:** The light comes from inside: the face glows yellow from its centre while the animation plays, and the measure finds the light from below (the yellow bar and flames).
- **Ambience:** A burst of heat on an otherwise calm board: the loudest thing a normal spin can show.
- **Materials:** Painted stone turned to glowing metal by the light; flat cartoon flame.
- **Variants:** Four 40-frame sequences: B01Bonus and B01Scatter, each for the base-game and the free-spin ground (the cell edge is cream or tan). Plus `glow`, a 244x244 soft overlay, and `glowBaseGame`, a 3x3 placeholder.
- **Motion:** 40 frames: the face brightens, yellow flames rise from the bottom, the word SCATTER or BONUS wipes in over a yellow bar and holds while the flames flicker, then everything fades back to the plain Sphinx (read from every second frame of the sequences). On the screens the cell also gets a red frame from the game.
- **Construction:** One atlas of 162 parts: four full-cell sequences of 40 frames at 244x244, every frame a complete opaque picture. Classic frame-by-frame animation, no parts, no skeleton.
- **Notes:** The only difference between the BONUS and SCATTER sequences is the word; the only difference between base and free-spin copies is the cell's margin. 160 full frames carry two words and two margins.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 49% · saturation 74% · contrast 86% · warm 100% / cool 0% · brighter towards: bottom (30)
- **Palette (measured):** #dc872c orange 27%, #8a170b dark red 16%, #180c05 black 11%, #edcd81 orange 10%, #fbee1b gold 8%, #faebc2 light orange 6%

### Regular symbols in both grounds (base game and free spins)

`symbolsII` · atlas · 22 parts · largest 244×244 · sheet `sheets/symbolsII.webp`

- **Role:** The eleven paying symbols, each drawn twice: for the base-game reels and for the free-spin reels.
- **Subject:** Scarab, lotus fan, cartouche, crook and flail, Eye of Horus, A, K, Q, J, 10, 9; each as BaseGame and FreeSpin.
- **Style:** As the base set: enamelled gold objects on coloured cloth, and gold Art Nouveau letters with lotus buds.
- **Rendering:** Identical drawing in both versions; only the cell ground changes. In the free-spin version the cream paper becomes a darker, mottled tan papyrus with a visible fibre texture.
- **Colour:** Measured on single cells, the ground of the card ranks goes from cream #f9e6bf (53 to 63% of the cell) to tan #e8c684 in the free spins; the cloth colours stay (scarab #3a8467, lotus #753e7e, cartouche #3f55b1, crook and flail #e8ad1e, eye #b92911) and only the paper margin around the cloth darkens (#f5e3bc to #e2c080).
- **Lighting:** Unchanged between the two versions: per-object highlights, no cast scene light.
- **Ambience:** The free-spin set reads warmer and older, matching the crimson sky of that mode; the base set is lighter and cleaner.
- **Materials:** Gold, enamel, a gem, woven cloth; cream paper against aged papyrus.
- **Variants:** 22 pictures: 11 symbols x 2 grounds. The letters differ in inlay so they do not rely on shape alone: A red and blue, K with a red gem and green stone, Q orange, J blue lattice, 10 gold with green stones, 9 orange.
- **Motion:** None: stills.
- **Construction:** One atlas of 22 untrimmed 244x244 cells. A whole second copy of each symbol is shipped for a ground change, where a layered build would have swapped only the ground: simple to run, heavy to make and to alter.
- **Notes:** The mode change is carried by the symbol art itself, not only by the backdrop: a detail worth noticing when planning a feature mode.
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged, strong highlights · brightness 58% · saturation 60% · contrast 72% · warm 79% / cool 17% · brighter towards: top-right (4), right (1)
- **Palette (measured):** #f7e4bc light orange 18%, #e5c17f orange 16%, #7f550f brown 11%, #cc9012 orange 8%, #b98f4d orange 7%, #1c1109 black 4%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Cleopatra wild, DOUBLE animation (base game)

`symbolsIII` · atlas · 80 parts · largest 244×244 · sheet `sheets/symbolsIII.webp`

- **Role:** The wild's win animation when it substitutes in a line win: the logo plate changes to DOUBLE, the wild's doubling rule shown on the symbol itself.
- **Subject:** Cleopatra as a tight crop: green eyes with heavy violet eye shadow under a gold winged headdress set with a red gem and coloured stones, the game's logo across the lower half of the cell; two gold hands with red nails come up over the logo.
- **Style:** Comic-style glamour portrait in hard outlines and saturated flat-to-airbrushed colour, the same drawing as the loading picture; during the animation the whole cell is washed gold.
- **Rendering:** Hard-edged (measured soft edge 0.0), high contrast (0.85 to 0.90), black outlines, smooth gradients on skin and gold; the gold phase is a flat yellow-orange tint over the same drawing.
- **Colour:** Gold #f1cc07 (25%), orange #d78a06, near-black #0a0c02, red-brown #b94006 and cream #f6e4b7 at the cell edge. At rest the first frame adds blue #0528e5 and magenta #ca2a62 from the logo plate and eye shadow; the DOUBLE plate is violet with red letters.
- **Lighting:** At rest a frontal glamour light with white catchlights in the eyes; in the animation the cell lights up as if gilded, with a green glow behind the logo plate.
- **Ambience:** The face of the game: direct eye contact, jewels and gold. The gold flash and the hands make the one theatrical gesture in an otherwise still game.
- **Materials:** Gold headdress with enamel feathers and cabochon stones, skin, lacquered nails; a glossy logo plate.
- **Variants:** This sequence on the base-game ground; the same on the free-spin ground is symbolsIV, and the version that keeps the Cleopatra logo is symbolsV and VI.
- **Motion:** 80 frames: the cell turns gold, two hands rise from the bottom edge and cross over the logo, then open and draw apart to show the plate again, now reading DOUBLE in red on violet, hold, close and open once more to return to the Cleopatra logo, and the colour comes back in the last frames (read from every fourth frame).
- **Construction:** One atlas holding a single 80-frame sequence of full 244x244 opaque cells: frame-by-frame animation, no parts and no skeleton.
- **Notes:** Seen in play on the screens '04-wild-double' and '12-free-spins-double'. The paytable says a win with one or more wilds is doubled; the art states the rule where the player is looking.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 51% · saturation 82% · contrast 89% · warm 92% / cool 5% · brighter towards: top (21)
- **Palette (measured):** #f1cc07 gold 25%, #d78a06 orange 11%, #0a0c02 black 11%, #b94006 brown 10%, #5e3604 brown 9%, #f6e4b7 light orange 9%

### Cleopatra wild, DOUBLE animation (free spins)

`symbolsIV` · atlas · 80 parts · largest 244×244 · sheet `sheets/symbolsIV.webp`

- **Role:** The same DOUBLE animation for the free-spin reels.
- **Subject:** Cleopatra as a tight crop: green eyes with heavy violet eye shadow under a gold winged headdress set with a red gem and coloured stones, the game's logo across the lower half of the cell; two gold hands with red nails come up over the logo.
- **Style:** Comic-style glamour portrait in hard outlines and saturated flat-to-airbrushed colour, the same drawing as the loading picture; during the animation the whole cell is washed gold.
- **Rendering:** Hard-edged (measured soft edge 0.0), high contrast (0.85 to 0.90), black outlines, smooth gradients on skin and gold; the gold phase is a flat yellow-orange tint over the same drawing.
- **Colour:** Gold #efc606 (28%), orange #c67206, near-black #0c0c02, red #b52908, with tan #eac985 at the cell edge in place of cream.
- **Lighting:** At rest a frontal glamour light with white catchlights in the eyes; in the animation the cell lights up as if gilded, with a green glow behind the logo plate.
- **Ambience:** The face of the game: direct eye contact, jewels and gold. The gold flash and the hands make the one theatrical gesture in an otherwise still game.
- **Materials:** Gold headdress with enamel feathers and cabochon stones, skin, lacquered nails; a glossy logo plate.
- **Variants:** Free-spin copy of symbolsIII: the drawing and timing are the same, the cell margin is the tan papyrus.
- **Motion:** 80 frames: the cell turns gold, two hands rise from the bottom edge and cross over the logo, then open and draw apart to show the plate again, now reading DOUBLE in red on violet, hold, close and open once more to return to the Cleopatra logo, and the colour comes back in the last frames (read from every fourth frame).
- **Construction:** One atlas holding a single 80-frame sequence of full 244x244 opaque cells: frame-by-frame animation, no parts and no skeleton.
- **Notes:** A full second copy of 80 frames for a change of margin colour.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 49% · saturation 85% · contrast 86% · warm 92% / cool 5% · brighter towards: top (21)
- **Palette (measured):** #efc606 gold 28%, #c67206 orange 17%, #0c0c02 black 12%, #eac985 orange 9%, #4b3004 brown 6%, #b52908 red 6%

### Cleopatra wild, plain animation (base game)

`symbolsV` · atlas · 80 parts · largest 244×244 · sheet `sheets/symbolsV.webp`

- **Role:** The wild's animation when it wins as itself (inference from the name 'Normal' and from the plate, which keeps the Cleopatra logo): the same hand gesture without the DOUBLE plate.
- **Subject:** Cleopatra as a tight crop: green eyes with heavy violet eye shadow under a gold winged headdress set with a red gem and coloured stones, the game's logo across the lower half of the cell; two gold hands with red nails come up over the logo.
- **Style:** Comic-style glamour portrait in hard outlines and saturated flat-to-airbrushed colour, the same drawing as the loading picture; during the animation the whole cell is washed gold.
- **Rendering:** Hard-edged (measured soft edge 0.0), high contrast (0.85 to 0.90), black outlines, smooth gradients on skin and gold; the gold phase is a flat yellow-orange tint over the same drawing.
- **Colour:** Gold #efc605 (31%), orange #c97504, near-black #0c0e02, brown #6c3d04, red #cd2002 and a dark green #165602 from the glow behind the logo; cream #f7e4b9 at the edge.
- **Lighting:** At rest a frontal glamour light with white catchlights in the eyes; in the animation the cell lights up as if gilded, with a green glow behind the logo plate.
- **Ambience:** The face of the game: direct eye contact, jewels and gold. The gold flash and the hands make the one theatrical gesture in an otherwise still game.
- **Materials:** Gold headdress with enamel feathers and cabochon stones, skin, lacquered nails; a glossy logo plate.
- **Variants:** Base-game copy; symbolsVI is the free-spin copy. Against symbolsIII only the plate differs: here the logo is redrawn in red and gold on green instead of the word DOUBLE.
- **Motion:** 80 frames: the cell turns gold, two hands rise from the bottom edge and cross over the logo, then open and draw apart to show the plate again in a gold and red version on green, hold, close and open once more to return to the Cleopatra logo, and the colour comes back in the last frames (read from every fourth frame).
- **Construction:** One atlas holding a single 80-frame sequence of full 244x244 opaque cells: frame-by-frame animation, no parts and no skeleton.
- **Notes:** Not seen in play: no win made of wilds alone came up in the session, so when it plays is read from the file name.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 52% · saturation 85% · contrast 90% · warm 93% / cool 4% · brighter towards: top (21)
- **Palette (measured):** #efc605 gold 31%, #c97504 orange 16%, #0c0e02 black 13%, #6c3d04 brown 10%, #f7e4b9 light orange 8%, #ad935e orange 5%

### Cleopatra wild, plain animation (free spins)

`symbolsVI` · atlas · 80 parts · largest 244×244 · sheet `sheets/symbolsVI.webp`

- **Role:** The same plain animation for the free-spin reels.
- **Subject:** Cleopatra as a tight crop: green eyes with heavy violet eye shadow under a gold winged headdress set with a red gem and coloured stones, the game's logo across the lower half of the cell; two gold hands with red nails come up over the logo.
- **Style:** Comic-style glamour portrait in hard outlines and saturated flat-to-airbrushed colour, the same drawing as the loading picture; during the animation the whole cell is washed gold.
- **Rendering:** Hard-edged (measured soft edge 0.0), high contrast (0.85 to 0.90), black outlines, smooth gradients on skin and gold; the gold phase is a flat yellow-orange tint over the same drawing.
- **Colour:** Gold #f0c605 (30%), near-black #0e0f02, orange #ce7a04, brown #6d3f05, red #ce2602, with tan #eac884 at the cell edge.
- **Lighting:** At rest a frontal glamour light with white catchlights in the eyes; in the animation the cell lights up as if gilded, with a green glow behind the logo plate.
- **Ambience:** The face of the game: direct eye contact, jewels and gold. The gold flash and the hands make the one theatrical gesture in an otherwise still game.
- **Materials:** Gold headdress with enamel feathers and cabochon stones, skin, lacquered nails; a glossy logo plate.
- **Variants:** Free-spin copy of symbolsV.
- **Motion:** 80 frames: the cell turns gold, two hands rise from the bottom edge and cross over the logo, then open and draw apart to show the plate again in a gold and red version on green, hold, close and open once more to return to the Cleopatra logo, and the colour comes back in the last frames (read from every fourth frame).
- **Construction:** One atlas holding a single 80-frame sequence of full 244x244 opaque cells: frame-by-frame animation, no parts and no skeleton.
- **Notes:** Four atlases, 320 full frames, for one symbol in two states and two margins: the wild is where this game spends its animation.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 50% · saturation 88% · contrast 85% · warm 93% / cool 4% · brighter towards: top (20)
- **Palette (measured):** #f0c605 gold 30%, #0e0f02 black 15%, #ce7a04 orange 15%, #6d3f05 brown 11%, #eac884 orange 8%, #ce2602 red 6%


## Logo and title

The game's own wordmark.

### Loading picture: Cleopatra over the logo

`loading` · atlas · 1 parts · largest 1040×700 · sheet `sheets/loading.webp`

- **Role:** The splash shown while the game loads, and the fullest version of the game's key art.
- **Subject:** Cleopatra's green eyes and gold winged headdress with a red gem rising behind the CLEOPATRA wordmark; pink and violet lotus fans on gold stems at the corners, a dark blue disc behind her, the IGT mark at the lower right.
- **Style:** Comic-style glamour illustration with heavy outlines, in the tradition of casino cabinet glass art.
- **Rendering:** Hard-edged (soft edge 0.0), airbrushed gradients inside outlines, white streak highlights on gold; the letters are red with a yellow inner line, a blue outer band and a gold rim. A 1040x700 picture on black.
- **Colour:** Orange-gold #e8b213 (29%), #c07017, gold #f2cf58, near-black blue #050c34, red #e3260a and blue #0538b0: gold and red against deep blue.
- **Lighting:** Frontal, with the gold lit from above and a blue glow behind the head separating it from the black.
- **Ambience:** Glamorous, direct, a little kitsch; it promises a classic rather than a new game. The copyright line on the loading screen reads 2017.
- **Materials:** Polished gold, enamel, cut gems, skin, lacquer-like lettering.
- **Variants:** The same face is cropped into the wild symbol; the wordmark alone is the cabinet's logo (frameI/logo) with lotus buds instead of the head.
- **Motion:** None: a still; a thin loading bar runs under it on the screen.
- **Construction:** One opaque picture, not layered.
- **Notes:** Key art, wild symbol and logo are one drawing used three ways, which keeps the game's identity tight.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 53% · saturation 77% · contrast 49% · warm 84% / cool 14%
- **Palette (measured):** #e8b213 orange 29%, #c07017 orange 18%, #f2cf58 gold 7%, #050c34 black 5%, #e3260a red 3%, #0538b0 blue 3%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Big Win Sphinx, frames 1 to 20

`bigWinAnimI` · atlas · 20 parts · largest 452×401 · sheet `sheets/bigWinAnimI.webp`

- **Role:** The glowing Sphinx that sits above the Big Win plaque.
- **Subject:** A front view of a Sphinx, head and forepaws on a stepped base, in banded red, orange and yellow, with soft pale rays behind it.
- **Style:** The scatter's flat banded Sphinx redrawn as a full figure, graphic and poster-like.
- **Rendering:** Hard bands of colour under a strong soft glow (soft edge 0.52, strong highlights); the rays are a pale blurred star behind the figure.
- **Colour:** Orange #fdce5d and #f8692b (32% each), red #e32214, pale gold #fff5a5: 100% warm.
- **Lighting:** Self-lit: the figure glows from within and the halo behind it swells and fades.
- **Ambience:** Triumphant and hot, a small sunrise over the reels.
- **Materials:** Stone shown as glowing metal.
- **Variants:** First half of a 40-frame sequence; bigWinAnimII is the second half.
- **Motion:** Over the 20 frames the halo and the inner glow grow, from a faint outline of rays to a full bright star (read from every second frame).
- **Construction:** One atlas of 20 trimmed frames (about 452x401), a frame-by-frame pulse; the sequence is split over two atlases only because of its size.
- **Notes:** Seen in play on '14-big-win-counting' and '15-big-win'. The whole Big Win is this pulse, a plaque and a counting number: no coins, no tiers.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 62% · saturation 70% · contrast 71% · warm 100% / cool 0%
- **Palette (measured):** #fdce5d orange 32%, #f8692b orange 32%, #e32214 red 12%, #fff5a5 light gold 11%, #614220 brown 5%, #916b38 orange 3%

### Big Win Sphinx, frames 21 to 40

`bigWinAnimII` · atlas · 20 parts · largest 452×400 · sheet `sheets/bigWinAnimII.webp`

- **Role:** The second half of the Big Win Sphinx's pulse.
- **Subject:** The same glowing Sphinx with rays.
- **Style:** As bigWinAnimI.
- **Rendering:** As bigWinAnimI (soft edge 0.52).
- **Colour:** Orange #fdce5d and #f86a2b (32% each), red #e12214, pale gold #fff7a3.
- **Lighting:** Self-lit, the glow easing back.
- **Ambience:** As bigWinAnimI.
- **Materials:** Stone as glowing metal.
- **Variants:** Frames 21 to 40 of the sequence begun in bigWinAnimI.
- **Motion:** The halo fades from its brightest back to the faint rays of frame 1, so the 40 frames loop as one slow pulse (read from every second frame).
- **Construction:** One atlas of 20 trimmed frames (about 452x400).
- **Notes:** Inference: the loop repeats while the amount counts up.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 62% · saturation 71% · contrast 71% · warm 100% / cool 0%
- **Palette (measured):** #fdce5d orange 32%, #f86a2b orange 32%, #e12214 red 14%, #fff7a3 light gold 11%, #7e5c2f brown 6%, #472f17 brown 2%

### Plaques and panels: Big Win plaque, free-spin frame, retrigger panel, logo

`frameI` · atlas · 6 parts · largest 1288×748 · sheet `sheets/frameI.webp`

- **Role:** The pieces the celebrations and messages are built from, with the cabinet's logo and the IGT mark.
- **Subject:** `bigWinPlaque`: a sandstone plinth with a dark window, gold winged ends in blue and orange enamel, a winged disc below and a row of magenta lotus fans on top. `transitionFreespin`: half of a gold hieroglyph frame with scarab clasps around a dark panel. `reTrig`: a violet wall of carved hieroglyphs and two Egyptian figures inside a red, blue and yellow striped border. `logo`: the CLEOPATRA wordmark with gold orbs and pale lotus buds at both ends. `bigWinDim`: a black veil for the reels. `IGT`: the company mark.
- **Style:** The plaque and the gold frame are modelled, soft-shaded illustration, closer to the cabinet than to the symbols; the retrigger panel is a flat wall relief in one hue; the logo is the outlined comic lettering of the key art.
- **Rendering:** Smooth gradients and bevels; the sandstone has a light crack texture; the hieroglyphs on the gold frame are embossed, on the violet wall engraved and nearly tone on tone.
- **Colour:** Plaque: dark window #251407, sandstone #c98835 and #7d4c1d, magenta #6c0e3c in the fans. Gold frame: #c88721, #e3bd61, #e8ba1e around #160500. Retrigger panel: violet #1d0c34 and #392c77 with a border of #f8c711, #0966f3 and #f63805. Logo: gold #e2ab18, orange #bf701a, blue #0542bb and #0d1d76, red #db2807.
- **Lighting:** Top light on the plaque and frame, with bevel highlights on the upper edges and a drop shadow under each piece.
- **Ambience:** Ceremonial: a tomb wall, a treasure frame, a temple plinth. The messages themselves are plain yellow or white live text.
- **Materials:** Sandstone, gold, enamel wings, carved painted stone.
- **Variants:** Six parts. The gold frame is drawn as one half and mirrored to make the whole frame (inference from the screens, where it is symmetrical with a scarab at the top and bottom centre). The retrigger panel was not seen in play.
- **Motion:** None in the files: stills. On the screens the gold frame closes over the reels on black, fire plays inside it and the text appears; the plaque sits over the dimmed reels while the amount counts.
- **Construction:** One atlas of 6 trimmed parts (the veil 1288x748, the plaque 823x365, the frame half 649x759, the panel 883x376, the logo 793x177). Text is not in the art: BIG WIN, the amounts and the free-spin messages are drawn by the game in a sans-serif face.
- **Notes:** The atlas mixes components: the logo belongs with the logo and title art, and the rest with celebrations; it is sorted here by its larger share.
- **Measured:** dark, saturated, warm and cool mixed, medium contrast · brightness 16% · saturation 56% · contrast 44% · warm 49% / cool 19% · brighter towards: right (1), bottom (1), left (1)
- **Palette (measured):** #0b0402 black 63%, #cb8c2b orange 12%, #34276d dark blue 11%, #231035 dark purple 3%, #eebd15 gold 3%, #eac763 orange 3%


## Effects

Frame sequences, glows, particles and transitions.

### Fire inside the gold frame (transition into and out of the free spins)

`transitionAnim` · atlas · 32 parts · largest 324×380 · sheet `sheets/transitionAnim.webp`

- **Role:** The 32-frame effect that plays inside the gold frame when the bonus starts and ends.
- **Subject:** Flames and smoke licking inward from a gold hieroglyph frame over a dark centre.
- **Style:** Photographic or simulated fire, the only naturalistic element in the game, against drawn everything else.
- **Rendering:** Soft billowing flame with bright embers, mirrored top to bottom (the same shapes appear above and below a centre line), on an opaque dark ground with the gold frame's edge baked in.
- **Colour:** Pale gold #fce780 (26%), near-black #270c04, brown #743015, orange #f1b350 and #e97a33: 100% warm, contrast 0.92.
- **Lighting:** Self-lit fire, brightest at the frame's left edge and corners (the measure finds the light from the left in all 32 frames).
- **Ambience:** A furnace or a burning scroll: the moment of heat between the purple game and the crimson one.
- **Materials:** Fire and smoke over gold.
- **Variants:** One sequence. Inference: the frames are one half or quarter of the panel, mirrored and stretched to fill the frame, as the mirrored shapes and the 324x380 size against a frame of about 650x380 on screen suggest.
- **Motion:** 32 frames: the fire thickens from the edges toward the centre and the dark middle fills with rolling orange smoke (read from every second frame). On the screen '08-free-spins-welcome' the message sits over it.
- **Construction:** One atlas of 32 opaque frames at 324x380, small and then enlarged on screen, which is why the fire looks soft there.
- **Notes:** Low resolution enlarged and mirrored is an economical way to cover a large panel with fire; the mirror line is visible if looked for.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 50% · saturation 72% · contrast 92% · warm 100% / cool 0% · brighter towards: left (32)
- **Palette (measured):** #fce780 gold 26%, #270c04 black 21%, #743015 brown 19%, #f1b350 orange 14%, #e97a33 orange 12%, #b05324 orange 7%


## Game interface

Buttons, counters and panels drawn for this game.

### Meter bar, buttons and autospin controls

`ui` · atlas · 52 parts · largest 1700×216 · sheet `sheets/ui.webp`

- **Role:** Everything the player presses or reads under the reels.
- **Subject:** A long red-brown bar with dark inset meter windows in gold rims; a gold scarab-arch housing for the round spin button; round glossy buttons for spin (curved arrow), start (play triangle) and skip (play with a bar) in normal, over, pressed and grey inactive states; blue autospin and red stop buttons; small blue triangular plus and minus arrows; a white segmented network spinner.
- **Style:** Two manners: the bar, meter windows and spin housing are in the cabinet's gold-and-lacquer illustration; the autospin, stop and arrow buttons are generic glossy web-style buttons with no Egyptian detail.
- **Rendering:** Glass-dome buttons with a white upper highlight and a darker lower rim; bevelled gold rims on the meter windows; smooth gradients throughout (soft edge 0.22).
- **Colour:** The unit is brown #773f10 (34%) and near-black #150a03 with bronze #a97a39 and orange #eba827. Buttons, measured singly: spin and start yellow-gold #fdc01a, skip orange #fc6c08, autospin blue #047beb, stop red #cd3207, arrows cyan #27d3fd on dark green-black; inactive states are grey #7a7a7a.
- **Lighting:** Top light on every button (a white highlight on the upper half), consistent with the beads.
- **Ambience:** Functional and friendly; the gold spin button is the single brightest control and sits in the centre of the bar, not at the right edge.
- **Materials:** Polished wood or lacquer bar, gold rims, glass buttons.
- **Variants:** 52 parts: spin, start and skip each in four states; autospin and stop each in four; plus and minus each in four; meter windows in several sizes (`Meter`, `betMeter`, `winMeter`, `bonusMeter` with a red glow for the free spins); an autoplay choice panel; a nine-step spinner.
- **Motion:** `startButtonAnim` is a slightly larger gold play button (100x100 against 96x96), inference: used to pulse the button when the bonus waits to be started. `networkActivity` is a 9-frame rotating spinner. Button states are swaps of stills.
- **Construction:** One atlas of 52 trimmed parts. All labels and figures (LINES, LINE BET, TOTAL BET, WIN, BALANCE, FREE SPINS, BONUS WIN) are live text: white figures and orange labels in the meter windows, green for a win amount. The two embedded fonts are Lato Bold and Roboto Regular.
- **Notes:** In the free spins the bar is reduced to two meters and the button (seen on the screens). The blue and red autospin buttons break the palette: they look like a later addition to an older design (inference).
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 36% · saturation 67% · contrast 52% · warm 89% / cool 4% · brighter towards: top (10), bottom-left (3), bottom (2)
- **Palette (measured):** #773f10 brown 34%, #150a03 black 24%, #a97a39 orange 12%, #eba827 orange 6%, #f9f9f5 light yellow 5%, #7a7a7a grey 3%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `stars`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Lato (Bold); Roboto (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 705 components cut from 19 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
