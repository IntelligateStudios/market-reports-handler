# Mega Cash Boost Hold And Win: art report

octoplay · run `2026-11-26-2218-octoplay-mega-cash-boost-hold-and-win` · captured 2026-11-26

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/mega-cash-boost-hold-and-win

**Extracted:** 454 named components from 34 textures in 34 atlases; 54 Spine skeletons; 14 frame sequences (278 frames); 3 fonts. Grouped into 21 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A fruit-and-letters slot rebuilt as a neon scoreboard: no scene and no character, only red laser light, a thin neon reel frame, and fifteen glowing prize plates that lightning keeps charging while three colours of diamond wait to collect them.

**Style.** Flat neon graphic design around glossy 3D-look symbols. The backdrop, the frame and the prize plates are pure light and outline; the fruit, bolts and wild button are airbrushed casino illustration; the diamonds are low-polygon gems. Everything leans: letters, plates and beams share one forward slant.

**Rendering.** Two kinds only. Light: white shapes with feathered edges, tinted and added by the game (backdrop soft edge 0.713, lightning 0.738, glows 0.951). Objects: smooth volumes or flat facets with hard outer edges and a thin blue rim (fruit 0.075, diamonds 0.042, boost 0.1). Lettering has a two-band chrome face with a hard horizon line and a stepped extruded side.

**Colour.** Red field, gold and cyan signs. Measured over the art files: near-white #fafaf8 21% (the white light sprites, which the game tints), gold #f7c030 11%, orange #f08617 10%, red #f2292e 10%, dark red #ab2b0f 3%, dark purple-blue #19083b 2%. On screen the backdrop is set by tints in the skeleton files: near-black wine #1f0014 under red #be1000 and #ff0000 beams. The code is strict: cyan-blue is Cash (plates, Blue Diamond, blue Booster), gold is Jackpot (plates, Gold Diamond, gold Booster), red is both (Red Diamond, the frame, the field), and the logo's three words carry the same three colours. Purple belongs to the Wild alone.

**Lighting.** Self-lit neon everywhere; there is no light source in a scene because there is no scene. Objects are lit from the top or top-left with a blue rim from below, as if standing on a lit sign. Glow circles behind the board make the centre the brightest area.

**Ambience.** High voltage, arcade and motorsport: fast, loud, synthetic. The mood comes from motion of light, not from a place or a story.

**Shape language.** The slanted parallelogram (plates, backplates, frame corners), the chevron (board pattern, meter fill, boost arrows), the lightning zigzag (logo, letters' notches, the container's ends, the effects) and the faceted diamond. Circles appear only on the Wild and the coin.

**Materials.** Neon tube, dark glass, coloured chrome lettering, moulded glossy plastic or glass (bolts, wild button), fruit skin and flesh, cut crystal, polished gold coin, electricity.

**Typography and lettering.** Heavy slanted capitals throughout, in two related faces: a wide italic sans with chrome bands for the logo, WILD and BOOST, and the condensed Anton for numbers, jackpot names, win tiers and captions (gold two-band numerals with a red-brown side; a white set for small counts). The low symbols 10 to A are lettering too, cut by a bolt. Small interface text is the provider shell's Poppins (Regular, SemiBold, Bold).

**Motion.** All motion is Spine 4.2.43: 54 skeletons in one bundle file, moving, scaling and tinting still pictures, plus 14 hand-drawn frame sequences (278 frames), of which eight are lightning (150 frames), three are the diamonds' turn (75), and the rest a coin, a win-line bolt and a plate border. Seen in play: the red beams sweeping behind the board all the time; an opening sequence in which two large Boosters and then a large red diamond appear over the reels and charge the plates; a Booster on the reels growing to cover the board when it fires; plate values jumping with a flash; white-blue lightning crackling along the frame and around locked diamonds; coins flying from a diamond up to a plate; a lightning bolt along a paying line with the amount in gold numerals; in the bonus a yellow flash that turns the stage gold, diamonds blurring through single cells, bolts carrying prizes from the plates to the diamonds, and BIG WIN with a coin shower. No skeleton frame is shown in this report, because the project's renderer is written for Spine 3.7.

**Variants and themes.** Two states of the whole stage from one set of parts (normal and special skins: red for the base game, orange-gold with yellow beams for the Hold & Win, both seen in play); two states of every plate outline (resting and red); cash and jackpot plates as one component in two colours; three diamonds and two Boosters as recolours of one design each; desktop and mobile plate shapes; a brighter Add copy of almost every symbol for win flashes.

**How it is built.** Three 4096 px atlas pages hold 391 sprites, more than half of them animation frames; there is no background picture at all (the backdrop is a 202 px white square and a glow circle, stretched and tinted). Symbols are layered: fruit in two halves, wild as button and word, Booster and Diamond as plate, object and word or bolt. Five localised lettering files (en-GB). The paytable pictures, logo copy, numeral fonts and interface come from the provider's shared services.

**Consistency.** Very high: one slant, three shapes and three prize colours run through backdrop, frame, plates, symbols, lettering and effects. The only seam is between the softly painted fruit and the hard graphic world around it, and the blue rim on the fruit is there to close it.

**What to take from it.** (1) A slot can ship with no background painting and no character: tinted white shapes moved by a rig gave this game its whole stage in eleven sprites, and a second stage for the bonus by changing tint values. For AI art work this moves the effort from illustration to a small kit of clean light shapes. (2) Make the prizes the picture. Fifteen neon plates take more of the screen than the reels' frame, and every Booster visibly changes a number on them; the art direction serves a mechanic of growing prizes rather than a theme. (3) One colour code end to end: blue is Cash, gold is Jackpot, red is both, on plates, diamonds, Boosters, backplates and even the three words of the logo. A player learns the rules from the colours. (4) Spend drawn frames on one effect family and reuse it: 150 of 278 animation frames are white lightning, tinted cyan or gold and placed by rigs on the frame, the plates, the logo and the symbols. (5) Classic fruit made current by cutting, not repainting: each fruit is two small pictures, a cut half and a whole half, which gives depth and a win animation; the letters get the theme from a single bolt-shaped notch. (6) Reserve one hand-animated asset for the symbol players stare at: the three diamonds each have a 25-frame turn, while every other symbol moves by rig only. (7) From the same provider as Fire Rail Express: Hold & Win, and built on the same framework (same file layout, 20 skeleton names in common, the same shell, Poppins and Double Chance card, byte-identical glow, line and lineEnd helpers), yet no picture of the game's own art is shared: same-named sprites such as coin_00 or win1Txt are different drawings. The reuse is in structure and tooling, not in art. (8) A numeral style picked from a provider font library (gold Anton here, purple-and-gold in Fire Rail Express) is enough to tie changing numbers to the game's lettering without drawing digits per game.

## Colour, measured

The game's own art (provider interface left out): bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 63% · saturation 58% · contrast 53% · warm 55% / cool 28% · brighter towards: top (72), top-left (54), top-right (18)

Palette: #fafaf8 light yellow 21%, #f7c030 orange 12%, #f08617 orange 11%, #f2292e red 10%, #d1c9ce grey 4%, #ab2b0f red 4%, #f8656e red 3%, #19083b dark purple 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 66% | 48% | 14% | 30% / 22% | #fffffe light orange 45%, #fb7618 orange 27%, #330663 dark purple 13% |
| Reel board | 1 | 70% | 58% | 19% | 58% / 6% | #ffffff light green 31%, #fbbd26 orange 14%, #db0427 red 11% |
| Symbols | 6 | 59% | 67% | 62% | 63% / 35% | #f5282c red 15%, #3a8bf6 blue 13%, #f8f7f5 light yellow 12% |
| Logo and title | 2 | 46% | 67% | 84% | 65% / 35% | #090a0a black 11%, #62391d brown 8%, #28c2f9 cyan 8% |
| Win celebrations and banners | 3 | 60% | 59% | 61% | 59% / 31% | #faf9f7 light yellow 21%, #d88a2e orange 19%, #f9c510 gold 11% |
| Effects | 2 | 84% | 4% | 20% | 0% / 8% | #f7f8f8 white 60%, #c6c8c8 grey 15%, #9a9a9a grey 11% |
| Game interface | 3 | 74% | 49% | 25% | 59% / 11% | #fefefc light gold 34%, #fc3738 red 21%, #fedf21 gold 12% |
| Typography | 1 | 70% | 74% | 67% | 93% / 7% | #f1c231 gold 55%, #a83803 brown 19%, #f5f36c gold 16% |
| Provider interface (shared) | 2 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backdrop: tinted light beams, no painted picture

`backgrounds` · atlas · 11 parts · largest 1863×347 · sheet `sheets/backgrounds.webp`

- **Role:** Everything behind the reels in the base game (skin normal) and in the Hold & Win bonus (skin special), and the beams of the bonus transition.
- **Subject:** No scene and no picture: white beam shapes (a long fading wedge, a round-ended glowing bar with a solid core, a thin rhombus line with its glow, a short slanted bar), two halftone dot fields and one neon chevron. In play they add up to a dark red space crossed by red and white laser beams that fan out from behind the reels.
- **Style:** Abstract neon graphic, like a light show or a racing title card; nothing is depicted.
- **Rendering:** Soft additive light: every piece is a white or single-colour shape with a feathered edge (soft edge 0.713, the softest picture unit besides the effects), drawn in white to be tinted by the game.
- **Colour:** The sprites are white (#fffffe, 45% of the unit), with one orange wedge (#fb7618) and one purple wedge (#330663 to #d304f2) that are tinted too. The colour is set in the skeleton files, not in the pictures: the base is a white square tinted #1f0014 with a red overlay #be1000 and glow circles #be4000 and #520300; the bonus skin uses #250000 with glows #120400 and #922000. The beams are tinted mostly pure red #ff0000 (45 of 142 slots), gold #ffc60d (30) and yellow #f4fe00 (13).
- **Lighting:** Self-lit; the beams are the light. The brightest area is behind the reel board, where the glow circles sit.
- **Ambience:** Speed and voltage: a dark club or arcade lit by red lasers. Nothing in it competes with the reels or the prize plates.
- **Materials:** Light only: neon tube, laser beam, printed halftone.
- **Variants:** Two skins of the same construction, normal and special, in the three skeletons Backgrounds, BackgroundEffects and SlotFrame. Seen in play: the base game is the red field with red and white beams; the Hold & Win turns the same field orange-gold with yellow beams and yellow outlined rhombuses, after a full-screen yellow flash.
- **Motion:** BackgroundEffects (106 bones, 142 slots) has idle1 3.33 s, idle2 10 s and three loops of 11.68 s, 1.5 s and 8.33 s; seen in play, the beams sweep and cross slowly behind the board, a different arrangement in every frame, and thin outlined rhombuses expand from the centre.
- **Construction:** Eleven sprites, the largest 1863x347, most of them white. The whole backdrop is three skeletons that scale, rotate and tint these few shapes over a 202 px white square stretched 15 times. There is not one background painting in the game's files.
- **Notes:** The cheapest possible backdrop in file size and the most flexible: a new colour scheme is a change of tint values. It is also why the game reads as flat graphic design rather than a place.
- **Measured:** bright, saturated, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 66% · saturation 48% · contrast 14% · warm 30% / cool 22% · brighter towards: bottom-left (1)
- **Palette (measured):** #fffffe light orange 45%, #fb7618 orange 27%, #330663 dark purple 13%, #680796 purple 6%, #9d06c5 purple 3%, #c1c1c1 grey 2%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board: neon frame on black

`reel-board` · atlas · 27 parts · largest 1174×345 · sheet `sheets/reel-board.webp`

- **Role:** The 5x3 reel area, its frame in two states, dividers, the win-line lightning, the empty-cell marker of the bonus and helper shapes.
- **Subject:** A thin neon frame drawn as four pieces (top, bottom, two sides) with stepped, cut corners, in red (Normal) and in gold (Special); hairline dividers in dark red; a white chevron; a soft white square and a hard white square; a small blue diamond-shaped pip (tile15); two tiny gold caps (line, lineEnd); a green guide square; an eleven-frame white lightning line.
- **Style:** Neon sign tubing with motorsport-style cut corners. No texture and no ornament.
- **Rendering:** A bright core line with a wide coloured glow (soft edge 0.503); the chevrons and squares are flat white shapes for tinting.
- **Colour:** Frame red #db0427 and #f7492e with a pale core, or gold #fbbd26 and #f9d963; dividers dark red. The 11% pure green #2bfd01 in the unit's palette is the guide square tileGuide, a layout aid that is not shown in play.
- **Lighting:** Self-lit. In play the red frame throws a soft red glow onto the black board and the backdrop around it.
- **Ambience:** A dark window edged in neon; the symbols sit on near-black with only a faint halftone and chevron pattern, so they keep all the colour.
- **Materials:** Neon tube, black glass.
- **Variants:** Normal (red) for the base game and Special (gold) for the bonus, both seen in play. In the bonus the gold frame holds a grid of fifteen separate cells with horizontal and vertical dividers, and every empty cell shows the small blue pip.
- **Motion:** SlotFrame (15 bones, 42 slots) has idle 5.83 s, win 2.67 s, winLoop 0.75 s and reset 0.83 s and runs the lightningTrail sequence along the frame in pale blue #dcfbff and gold #ffce2f. winLine is an 11-frame lightning line (500x80) that the WinLine skeleton (38 bones) plays for 1 s along a paying line. ReelAnticipation has a 1 s loop.
- **Construction:** 27 sprites. The board has no backing picture: SlotBackgrounds builds it from the white square, twelve copies of the chevron slotArrow, a halftone field and the dividers. The pip tile15 is the picture of the TileEmpty skeleton, the empty cell of the bonus (help picture tile16; seen in play). line and lineEnd are byte-identical to the same files in Fire Rail Express: Hold & Win, so they are the provider's own.
- **Notes:** A frame of four thin strips costs almost nothing in the atlas and can change colour and size per layout.
- **Measured:** bright, saturated, warm and cool mixed, low contrast, strong highlights · brightness 70% · saturation 58% · contrast 19% · warm 58% / cool 6%
- **Palette (measured):** #ffffff light green 31%, #fbbd26 orange 14%, #db0427 red 11%, #2bfd01 green 11%, #f7492e red 10%, #f17e60 red 9%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Paytable pictures of the symbols

`help-symbol-pictures` · atlas · 16 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The sixteen 225x225 pictures the provider's help pages show for the symbols (tile1 to tile16), delivered by the shared paytable service and not cut from the game's atlas.
- **Subject:** 10, J, Q, K, A; cherry, orange, plum, watermelon as assembled two-half symbols; WILD on its button; the blue and gold BOOST symbols; the blue, gold and red diamonds on their plates with a bolt and glints; and a small blue pip (tile16).
- **Style:** The same art as the reels, composed per symbol.
- **Rendering:** As in the game; these are flattened composites at one size.
- **Colour:** The whole symbol palette at once: orange #f2b30b, blue #1556d9, red #f05438, near-white #eeeeef, green #467407. Warm 0.52 against cool 0.419.
- **Lighting:** From the top or top-right on 14 of 15 measured parts.
- **Ambience:** A clean catalogue view of the set.
- **Materials:** As the symbols.
- **Variants:** One picture per symbol.
- **Motion:** None; still pictures.
- **Construction:** Sixteen WebP files of 225x225 from the provider's shared assets folder for this game (`games/<slug>/tiles/`). They show how each layered symbol is meant to be assembled: the diamonds here have the bolt and sparkles in place, which the cut layers alone do not show.
- **Notes:** Useful as the reference for the assembled symbol, since no skeleton frame can be drawn by the project's tools for this client.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 52% · saturation 71% · contrast 73% · warm 52% / cool 42% · brighter towards: top (8), top-right (6), top-left (1)
- **Palette (measured):** #f2b30b orange 10%, #1556d9 blue 9%, #f05438 red 8%, #eeeeef white 7%, #d26907 orange 4%, #467407 dark green 4%

### Boost symbols and the diamond backplates

`symbols-boost` · atlas · 6 parts · largest 550×464 · sheet `sheets/symbols-boost.webp`

- **Role:** The two Booster symbols (tile11 Cash Booster, blue; tile12 Jackpot Booster, gold), which raise the prizes shown around the reels, and the coloured plates that sit behind Boosters and Diamonds.
- **Subject:** A thick lightning bolt, in cyan and in yellow, over a slanted rounded plate printed with chevrons and halftone dots, with the word BOOST. A third plate is red.
- **Style:** Glossy 3D-look icon on a flat graphic plate; chrome italic lettering.
- **Rendering:** The bolts are modelled like moulded glass: a lit front face, darker bevelled sides, a streak highlight and a coloured glow underneath. The plates are flat, with tone-on-tone chevrons, a dot screen in the lower corner and a thin light edge. Hard edges (soft edge 0.1).
- **Colour:** The most saturated unit in the game (saturation 0.837): blue plate #3169fd with a cyan bolt #11eff6, orange plate #ec8d03 with a gold bolt #f8cb06 and #fef511, red plate #c70218. The word is near-white #e8ebeb with a lilac lower half.
- **Lighting:** Bolts are lit from the top-left with a light bounce from below (measured: bottom 2, top-left 2, top 1); the plates are unlit graphics.
- **Ambience:** Power-up signs. When the game is opened, both appear once at about two cells wide over the middle of the board (the Starting Boosters sequence), and a Booster that lands in a cell grows to the same size over the board when it fires (both seen in play), so they read as an event rather than a symbol.
- **Materials:** Coloured glass or candy-gloss plastic for the bolts, printed card or enamel for the plates, chrome for the word.
- **Variants:** Blue for Cash and gold for Jackpots, the game's colour code; the red plate (tile15Backplate) belongs to the Red Diamond. One BOOST word serves both.
- **Motion:** No frame sequence. TileBooster (19 bones, 14 slots, skins tile11 and tile12) has spinStart 0.15 s, onLand 0.5 s, loop 1 s, boost 0.5 s and boostMax 0.5 s; BoosterSplash (11 bones, 16 slots) shows and hides the large opening pair. Seen in play: the word BOOST jumps forward and enlarges when a Booster fires, and a prize plate flashes and changes its number.
- **Construction:** Plates are 540 to 550 px wide and bolts 431 px wide, far larger than the other symbols (about 150 px), because the game shows them large when they fire; at rest on the reels they are scaled down to a cell. Plate, bolt and word are separate layers.
- **Notes:** The atlas names the plates by tile number (11, 12, 15); they were grouped here from those names. The Blue Diamond's plate is tile11Backplate and the Gold Diamond's tile12Backplate in the TileDiamonds skeleton, so Booster and Diamond of one colour share a plate.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 50% · saturation 84% · contrast 48% · warm 58% / cool 41% · brighter towards: bottom (2), top-left (2), top (1)
- **Palette (measured):** #c70218 red 21%, #3169fd blue 20%, #ec8d03 orange 16%, #f8cb06 gold 11%, #e8ebeb white 5%, #11eff6 cyan 4%

### Diamonds: blue, gold and red

`symbols-diamonds` · atlas · 78 parts · largest 365×347 · sheet `sheets/symbols-diamonds.webp`

- **Role:** The feature symbols (tile13 Blue, tile14 Gold, tile15 Red). Diamonds trigger the Hold & Win bonus and take prizes at its end: blue the Cash Prizes, gold the Jackpot Prizes, red either (the game's rules).
- **Subject:** A brilliant-cut gemstone seen from the front and slightly above, in three colours, each as a turning sequence; one more detailed still gold diamond (tile14Diamond); a white lightning-bolt mask; a soft white shape the size of a cell (tileDiamondShadow).
- **Style:** Low-polygon gem with flat facets, cleaner and more graphic than the fruit.
- **Rendering:** Flat-shaded triangular facets in four or five tones, a near-white crown and no outline; the facets change tone from frame to frame as the stone turns. The hardest-edged unit in the game (soft edge 0.042).
- **Colour:** Red #f82c2e with pink #fe6270 and #f9a8a4; blue #4393f5 and #2162d7; gold #fcb240 and #f2830e; crowns near-white #f9f9f6.
- **Lighting:** Lit from the top-left on 41 parts and the top on 14 (measured): the crown catches the light and the lower facets go deep in colour.
- **Ambience:** Cold, clean and valuable; the only objects in the game drawn with straight facets, so they separate at once from fruit and letters.
- **Materials:** Cut glass or crystal.
- **Variants:** Three colours with the same 25-frame turn each (blue and gold 360x281, red 361x281). The still gold diamond is a different, richer drawing with inner reflections (233x186).
- **Motion:** Three frame sequences of 25 frames (diamondBlue, diamondGold, diamondRed): the sheet's three frames show the facet pattern shifting, a turn or shimmer on the spot. TileDiamonds (15 bones, 23 slots, skins tile13, tile14, tile15) has show 0.33 s, onLand 0.5 s, loop 1 s, lock 0.5 s, lockLoop 1 s, activate 0.67 s and burst 1 s, with lightning pieces and glow circles around the stone.
- **Construction:** 75 sequence frames plus three stills. In the skeleton the diamond sits on the coloured backplate of the Boost unit with a tinted glow (#4ea1ff, #fff200, #ff0000 in the file) and the bolt mask behind it. Seen in play: a locked diamond sits on its plate wrapped in white-blue lightning (the Red Diamond with a bolt behind it), blurs like a reel symbol while a bonus cell spins, and at collection carries its prize in gold numerals across the stone.
- **Notes:** A hand-made 25-frame turn per colour is where this game spends its frame budget for symbols; everything else moves by rig. Red Diamonds stay locked on the reels between spins (rules), so this is the picture a player looks at longest. No Gold Diamond took part in the bonus that was played; it was seen on the reels and on the splash.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 62% · saturation 63% · contrast 63% · warm 66% / cool 33% · brighter towards: top-left (41), top (14)
- **Palette (measured):** #f82c2e red 19%, #fcb240 orange 16%, #4393f5 blue 15%, #f9f9f6 light yellow 14%, #f2830e orange 7%, #fe6270 red 7%

### Wild

`symbol-wild` · atlas · 4 parts · largest 235×225 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol (tile10), which substitutes for all symbols except Diamond and Boost symbols (the game's rules).
- **Subject:** A round purple button with a halftone dot face and a polished blue-silver ring, and the word WILD in heavy italic capitals across it.
- **Style:** Arcade push-button; the lettering is the same chrome italic as the BOOST word.
- **Rendering:** The disc is a flat magenta-to-purple gradient covered by a fine dot screen, inside a bevelled ring with a bright upper highlight. The word has a white-to-light-blue face split by a horizon line, a pink rim and a dark extruded shadow.
- **Colour:** Magenta and purple (#ed7af3, #9c40c7) with a blue ring (#574698, #85acee) and near-white lettering (#f7edf9). Measured cool 0.548.
- **Lighting:** Lit from the top (4 of 4 parts); the Add copy is a soft pink disc that makes the button glow from inside.
- **Ambience:** A lit button waiting to be pressed; the one purple object on a red and gold screen.
- **Materials:** Backlit plastic with a printed dot screen, a chrome ring, chrome lettering.
- **Variants:** Disc, disc glow (tile10Add), word, word glow (tile10TxtAdd).
- **Motion:** No frame sequence. TileWild (11 bones, 12 slots) has a loop of 2 s, onLand 0.42 s and win 0.75 s; the separate glow copies are what it can pulse (inference).
- **Construction:** Four sprites: a 235x225 disc, its glow, a 225x91 word and its glow, so the word can move apart from the disc.
- **Notes:** Purple is kept for the Wild alone, so it stands out without any character art.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, strong highlights · brightness 58% · saturation 38% · contrast 69% · warm 23% / cool 55% · brighter towards: top (4)
- **Palette (measured):** #f7edf9 light magenta 26%, #ed7af3 magenta 21%, #9c40c7 purple 18%, #060206 black 8%, #c7beef light blue 7%, #574698 blue 5%

### Low symbols: 10, J, Q, K, A

`symbols-royals` · atlas · 10 parts · largest 190×163 · sheet `sheets/symbols-royals.webp`

- **Role:** The five low-paying symbols (tile1 to tile5), shown bare on the dark board with no tile behind them.
- **Subject:** The characters 10, J, Q, K and A as slanted, extruded letters, each cut through by a lightning-shaped slash or ending in a bolt-like spur.
- **Style:** Racing-stripe or arcade lettering: heavy italic sans capitals with a zigzag notch, in the family of the game's logo.
- **Rendering:** Flat glossy faces with one diagonal band of lighter colour, a thin white bevel line, a darker extruded side and a blue outer rim; outer edges are crisp, the rim is slightly soft (soft edge 0.207 for the unit).
- **Colour:** One colour per character: magenta 10 (#eb12f5 measured in the unit), blue J (#0d5ce3), green Q (#357f08 dark, #68f406 light), red K (#f33108, #a81705) and gold A (#fdf015). Every one has the same blue rim, which is why blue is the unit's largest hue (0.276).
- **Lighting:** Lit from the top (measured on 7 of 9 parts), with the highlight as a hard diagonal band rather than a soft gradient.
- **Ambience:** Fast and electric; the letters lean forward like the beams of the backdrop.
- **Materials:** Lacquered plastic or enamel with a neon-blue edge.
- **Variants:** Each character has a normal picture and an Add copy (tile1Add to tile5Add): the same letter brighter, with a white rim. Inference from the name and the look: the Add copy is drawn additively over the normal one to flash it on a win.
- **Motion:** No frame sequence. The skeleton TileContainerJuniors (3 bones, 5 slots) has onLand 0.42 s and win 0.75 s.
- **Construction:** One picture per character, 145 to 186 px wide, plus its brighter copy; ten sprites in all. The help pages use separate 225 px pictures from the provider's paytable service.
- **Notes:** The lightning cut is the whole theme carried into the cheapest symbols: no extra object, only a notch in the letter.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 55% · saturation 71% · contrast 73% · warm 40% / cool 47% · brighter towards: top (7), top-right (2)
- **Palette (measured):** #0d5ce3 blue 16%, #f8f6f1 light orange 10%, #f33108 red 6%, #fdf015 gold 6%, #357f08 dark green 4%, #eb12f5 magenta 4%

### High symbols: cherry, orange, plum, watermelon

`symbols-fruit` · atlas · 16 parts · largest 153×176 · sheet `sheets/symbols-fruit.webp`

- **Role:** The four high-paying symbols (tile6 to tile9), each a fruit split in two halves.
- **Subject:** A cherry, an orange, a plum and a watermelon, each drawn as two pieces: a cut half showing the flesh and stone or seeds (Back) and a whole or uncut half in front (Front). The cherry, orange and plum keep a stalk with a leaf; the watermelon keeps a curled vine.
- **Style:** Classic fruit-machine subjects painted as glossy, slightly stylised 3D-look illustration, opened up as if struck apart.
- **Rendering:** Smooth airbrushed volumes with texture painted in (orange peel pores, watermelon stripes and seeds, the plum stone's grain), pinpoint highlights and a hard outer edge (soft edge 0.075). A thin blue rim follows the lower edge of each piece.
- **Colour:** Warm unit (warm 0.746): yellows and oranges lead (#f9f711, #f4a60e, #d14e14), with cherry red #eb0722, watermelon green #425103 and the blue rim #0f5bdd. The pure yellow comes mostly from the Add copies.
- **Lighting:** Mixed by piece: measured from the top-left on 4 parts, top-right on 4 and the right on 3; in each pair the highlight sits on the upper curve. The blue rim reads as light from the neon below.
- **Ambience:** Juicy and bright against the near-black board; the halves make a static fruit look caught mid-burst.
- **Materials:** Fruit skin, wet flesh, stone, leaf.
- **Variants:** Per fruit: Back, Front, and a brighter Add copy of each (BackAdd, FrontAdd), recoloured towards yellow and white. On the reels the two halves sit apart with the cut half behind (seen in play).
- **Motion:** No frame sequence. TileContainerSeniors (18 bones, 12 slots, one skin per fruit) has onLand 0.42 s and win 0.75 s and also uses a glint, a spark burst and a lightning trail; with two separate halves the win can move them apart (inference from the construction; a win on a fruit was seen only as still frames).
- **Construction:** Two pictures per fruit, 94 to 153 px wide, plus two brighter copies: sixteen sprites. The skeleton tints its glow per fruit (#ff4646, #ffb200, #a239ff, #47ff47 in the file).
- **Notes:** Splitting each fruit into two layers gives depth and a win animation from two small paintings. The fruit are the high symbols here and the letters the low ones.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 58% · saturation 76% · contrast 65% · warm 75% / cool 20% · brighter towards: top-left (4), top-right (4), right (3)
- **Palette (measured):** #f9f711 gold 12%, #f4a60e orange 9%, #fbf9ed light gold 8%, #d14e14 orange 7%, #425103 dark green 6%, #f9f360 gold 5%


## Logo and title

The game's own wordmark.

### Logo picture of the help pages

`help-logo` · atlas · 1 parts · largest 769×110 · sheet `sheets/help-logo.webp`

- **Role:** The 769x110 logo the provider's shell shows on its own pages, from the shared assets folder for this game.
- **Subject:** The same MEGA CASH BOOST wordmark at a larger size.
- **Style:** As the game's logo.
- **Rendering:** The same chrome letters; at this size the stepped extrusion and the blue outer rim on BOOST are easier to see.
- **Colour:** Red #ec2e0c, gold #f4bf14, cyan #2bb4f8 and blue #094ff1 over brown and near-black sides (#774425, #080b0d).
- **Lighting:** From the top-right (measured).
- **Ambience:** As the game's logo.
- **Materials:** Polished coloured chrome.
- **Variants:** One picture.
- **Motion:** None; a still picture.
- **Construction:** A single WebP (`games/<slug>/logo/default.webp`), separate from the atlas.
- **Notes:** The cleanest copy of the logo in the run.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 42% · saturation 69% · contrast 80% · warm 65% / cool 35% · brighter towards: top-right (1)
- **Palette (measured):** #774425 brown 17%, #080b0d black 11%, #2bb4f8 cyan 8%, #2a3237 dark blue 8%, #ec2e0c red 7%, #f4bf14 gold 6%

### Logo: MEGA CASH BOOST

`logo` · atlas · 2 parts · largest 699×98 · sheet `sheets/logo.webp`

- **Role:** The game's title, sitting on the top edge of the reel frame in the base game and above the three red diamonds on the intro screen.
- **Subject:** The words MEGA CASH BOOST in one line of heavy italic capitals; the S of CASH is replaced by a lightning bolt.
- **Style:** Sports or energy-drink wordmark: wide slanted sans capitals with a hard horizon reflection.
- **Rendering:** Each letter has a chrome-style face split by a horizon line (lighter above, saturated below), a thin light bevel, a dark extruded side stepped down to the lower right and a soft dark shadow. High contrast (0.863).
- **Colour:** One colour per word: MEGA red #f22e08, CASH gold #fded09 over orange #ecab5b, BOOST cyan #29ecfc over blue; near-black sides #0a0a09. The three colours are the game's code: red, gold and blue diamonds.
- **Lighting:** Lit from the top-right (measured on both parts), with the reflection line across the middle of the letters.
- **Ambience:** Loud, fast and confident.
- **Materials:** Polished coloured chrome.
- **Variants:** logo and logoAdd (the same picture, brighter, for an additive flash). The help pages use a larger separate picture.
- **Motion:** Logo (26 bones, 22 slots) has show 0.33 s, hide 0.32 s, collect 0.5 s and win 2 s and uses lightning strikes, the slot lightning and a shock ring; seen in play, white lightning crackles along the top of the frame around the logo when a diamond's coins fly up.
- **Construction:** One 699x98 picture and its bright copy. Small on purpose: on screen it is about 350 px wide, a label on the frame rather than a header.
- **Notes:** The logo's three word colours double as the legend for the three diamond colours.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 48% · saturation 65% · contrast 86% · warm 65% / cool 35% · brighter towards: top-right (2)
- **Palette (measured):** #0a0a09 black 10%, #ecab5b orange 8%, #5a351b brown 8%, #f22e08 red 6%, #29ecfc cyan 5%, #e56647 red 5%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature sentences

`feature-splashes` · atlas · 4 parts · largest 1235×494 · sheet `sheets/feature-splashes.webp`

- **Role:** The localised lettering of the bonus splash and of the moments inside it.
- **Subject:** Four pieces of text: HOLD & WIN; DIAMONDS LOCK ON THE SLOT; MORE FOR THE GRAND JACKPOT!; REWARD COLLECTION TIME!
- **Style:** Condensed italic capitals in the Anton manner.
- **Rendering:** HOLD & WIN has the gold two-band face and red-brown side of the numerals; the three sentences are plain white with a faint blue-grey shade.
- **Colour:** White #fbfcfd (60%) and gold #eebf37 with red-brown #ad3c06.
- **Lighting:** None beyond the gold face's top-lit bands.
- **Ambience:** Announcer's captions: short, capital, exclamatory.
- **Materials:** Gold and white lettering.
- **Variants:** One file per text, en-GB; other languages would replace these four files and TOTAL WIN.
- **Motion:** Shown by FreeSpinsSplash (show 1.5 s, hide 0.33 s), JackpotCounterSplash and RewardSplash (show 1.25 s, hide 0.42 s each), over loop skeletons that use the neon chevron rombNeon. Seen in play: HOLD & WIN over the splash with DIAMONDS LOCK ON THE SLOT under three sample diamonds, and REWARD COLLECTION TIME! across the dimmed board when the respins end. MORE FOR THE GRAND JACKPOT! was not seen.
- **Construction:** Four whole WebP files in the localised folder, up to 1235x494.
- **Notes:** All wording that needs translating is in five files; the rest of the game's lettering (logo, WILD, BOOST, jackpot names, win tiers) is not localised.
- **Measured:** bright, muted, cool, medium contrast, strong highlights · brightness 84% · saturation 23% · contrast 52% · warm 22% / cool 78%
- **Palette (measured):** #fbfcfd light blue 60%, #eebf37 orange 13%, #a8b9c8 blue 11%, #ad3c06 brown 4%, #6a86a0 blue 4%, #113760 dark blue 2%

### Win words, win light and coins

`win-tiers` · atlas · 49 parts · largest 967×590 · sheet `sheets/win-tiers.webp`

- **Role:** The big-win celebration (BIG WIN, SUPER WIN, MEGA WIN), the bonus total (TOTAL WIN), the lightning border of a winning prize plate and the gold coin that flies in showers.
- **Subject:** Four two-line words in heavy condensed italic capitals; a white star-burst of rays; a 12-frame lightning rectangle; a soft directional glow; a 30-frame turning gold coin; a black square used as a screen fade.
- **Style:** Sports-broadcast title lettering, the same family as the jackpot names; the coin is a plain blank disc.
- **Rendering:** Words: a vertical two-tone gradient face with a pale outline and a darker extruded side, slightly arched. Coin: smooth gold with a raised rim and a broad sheen, no emblem. Light pieces are white and soft.
- **Colour:** One colour per tier: BIG WIN purple #b153e9, SUPER WIN blue #527ee8, MEGA WIN red #cd3756 to #9a0d25, TOTAL WIN pink to red with magenta #e945a3; coin gold #fcc408 with orange #d17a07.
- **Lighting:** Words lit from the top; the coin from the top-left (measured: top 8, top-left 6).
- **Ambience:** Loud but brief; the tier colours climb from cool to hot.
- **Materials:** Lacquered lettering, polished gold, light.
- **Variants:** Three tiers and the total from one layout (all four are 967x590). The coin is one sequence.
- **Motion:** coin: 30 frames of a coin turning through edge-on (120x120). payoutWin: 12 frames of lightning running round a rectangle (390x330), used by the prize plates. WinBig (19 bones, 25 slots) has sumShow 0.47 s, labelFinal 0.75 s and hide 0.42 s with a 1 s loop; WinTotal has show, showLabel and bangupEnd of 0.75 s each. Seen in play: coins fly from a diamond on the reels up to a Cash plate; at the end of the bonus BIG WIN stands on a dark slanted plate with a gold lightning border and a purple burst, the amount below it in gold numerals, with a shower of coins. SUPER WIN, MEGA WIN and TOTAL WIN did not appear and are read from the sheet only.
- **Construction:** The three tier words are in the atlas; TOTAL WIN is a localised file (en-GB). Same sprite names as in Fire Rail Express: Hold & Win (win1Txt to win3Txt, winTotalTxt, coin_00 to coin_29, circularWhiteRays2) but different pictures: the provider's framework names the slots and each game paints its own.
- **Notes:** The coin has no face at all, which keeps it usable at 30 px in a shower.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 56% · saturation 61% · contrast 56% · warm 51% / cool 29% · brighter towards: top (8), top-left (6), top-right (2)
- **Palette (measured):** #f9f9fa white 18%, #cd3756 red 15%, #fcc408 gold 14%, #527ee8 blue 9%, #9a0d25 red 6%, #e945a3 magenta 6%

### Jackpot names and the jackpot splash

`jackpot-splash` · atlas · 13 parts · largest 860×439 · sheet `sheets/jackpot-splash.webp`

- **Role:** The names of the six jackpots as they stand on the plates and as they are shown large when a jackpot is won.
- **Subject:** GRAND, MEGA, SUPER, MAJOR, MINOR and MINI twice: a large copy with an orange gradient face (about 210 px tall) and a small copy with a dark blue face and a gold rim (about 111 px tall); and a wide gold neon plate outline (860x439).
- **Style:** Condensed heavy italic capitals, close to the Anton numerals, with a slight arch.
- **Rendering:** Large copies: an orange-to-pale gradient face with a dark red extruded side and a thin light edge. Small copies: a flat dark face with a two-line gold and orange rim. Hard-edged (soft edge 0.145).
- **Colour:** Orange #d98d33 (45%), dark red #a82c0a, pale gold #f8f2ce and gold #fbe02a; the small copies' face is near-black blue #130239, the same value as the plates' fill.
- **Lighting:** From the top (12 parts measured).
- **Ambience:** Gold on dark: the jackpot column's own colour, kept apart from the cyan Cash plates.
- **Materials:** Polished gold lettering; neon.
- **Variants:** Six names in two treatments. The file names spell Grand's as jackporSplashGrandTxt.
- **Motion:** No frame sequence. JackpotSplash (19 bones, 27 slots) has show 0.75 s and hide 0.42 s with a 1 s loop. No jackpot was won in the play, so the large splash is read from the sheet and the file only; the bonus splash shows the six plates with their names as a small block.
- **Construction:** Thirteen sprites. Seen in play, the small dark copies are the names on the plates, each overlapping the plate's top edge in the outline's gap; the large orange copies belong to the splash (inference from the name).
- **Notes:** Unlike Fire Rail Express, the jackpots are not colour-coded one by one: all six are gold and differ only by size and position.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 55% · saturation 72% · contrast 74% · warm 87% / cool 13% · brighter towards: top (12)
- **Palette (measured):** #d98d33 orange 45%, #130239 black 13%, #a82c0a red 11%, #f8f2ce light gold 11%, #fbe02a gold 6%, #f4b352 orange 4%


## Effects

Frame sequences, glows, particles and transitions.

### Lightning

`lightning` · atlas · 151 parts · largest 284×1339 · sheet `sheets/lightning.webp`

- **Role:** The game's one effect family: lightning that connects a symbol to a prize, runs along the frame, strikes, arcs between points and bursts where it lands.
- **Subject:** Seven hand-drawn white lightning animations (a strike, a trail, a wide arc across the slot, small pieces, an arc, a hit burst, a collector crackle), a tall still cyan bolt (bigLightning1, 284x1339) and a set of rising chevron bands.
- **Style:** Cartoon electricity: thin jagged white lines with a soft halo, drawn frame by frame.
- **Rendering:** White cores with a grey-white glow on transparency (saturation 0.041, soft edge 0.738); only the big bolt is coloured, cyan #3be0f6. Everything else is tinted by the game.
- **Colour:** White #f7f8f8 and greys; in the skeletons the lightning is tinted pale cyan (#dcfbff on the frame, #9cf6f7 and #60fcff on the Cash plates) and gold (#ffce2f on the frame, #ffbd2f on the jackpots).
- **Lighting:** Self-lit.
- **Ambience:** The 'boost': the lightning is the visible charge moving from the reels to the prizes.
- **Materials:** Electric light.
- **Variants:** One white set serves cyan and gold by tint. The chevron sequence jackpotArrowEffect (8 frames, 264x200) is the rising-arrows fill shown inside a plate being boosted.
- **Motion:** Eight frame sequences, 150 frames: LightningStrike 10, boltHitEffect3 16, jackpotArrowEffect 8, lightningArk1 20, lightningPice 18, lightningTrail 23, sceneCollectorLightning 31 and slotLightning3 24. The sheet's first, middle and last frames show each one starting as a spark, branching, and breaking into fragments. Seen in play: a jagged white-blue line jumping from the opening Booster to a plate, crackle along the top of the frame and, on the trigger spin, round the whole frame; lightning wrapped around every locked diamond; a thick bolt carrying a prize from a plate to a diamond in the bonus.
- **Construction:** 151 sprites, half of all the animation frames in the game. The lightningTrail sequence alone is used 42 times in the SlotFrame skeleton, so one drawn sequence becomes a whole frame of electricity.
- **Notes:** Drawn once in white, used everywhere in two tints: the effect budget of the game is this one family.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 83% · saturation 4% · contrast 21% · warm 0% / cool 8% · brighter towards: top (2)
- **Palette (measured):** #f7f8f8 white 58%, #c6c8c8 grey 16%, #9a9a9a grey 12%, #363636 grey 4%, #747474 grey 4%, #3be0f6 cyan 4%

### Glows and sparks

`light-and-sparks` · atlas · 5 parts · largest 495×495 · sheet `sheets/light-and-sparks.webp`

- **Role:** The generic light pieces under everything: glow behind symbols and plates, the backdrop's hot spot, a shock ring, a spark cloud and a glint.
- **Subject:** A soft round glow (495x495), a thin elliptical ring, a scatter of small sparks, a four-point glint and a tiny gradient strip.
- **Style:** Standard additive light sprites.
- **Rendering:** Pure white with full feathering (brightness 0.994, soft edge 0.951).
- **Colour:** White #ffffff; all colour comes from tints in the skeletons (the glow circle is the backdrop's red hot spot at #be4000 and the diamonds' glow at #4ea1ff, #fff200 and #ff0000).
- **Lighting:** Self-lit.
- **Ambience:** They make the neon look like it lights the air around it.
- **Materials:** Light.
- **Variants:** Five sprites.
- **Motion:** No sequence; scaled, faded and tinted by the skeletons. The ring is the Logo skeleton's shock wave.
- **Construction:** The glow circle is the most reused picture in the game's skeletons (Jackpot, Payout, the tiles, the backdrop). The strip glow.webp is byte-identical to the one in Fire Rail Express: Hold & Win.
- **Notes:** Five white sprites carry most of the game's atmosphere.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 99% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 98%, #b8b8b8 grey 2%


## Game interface

Buttons, counters and panels drawn for this game.

### Diamond container and respin counter

`diamond-meter` · atlas · 7 parts · largest 816×92 · sheet `sheets/diamond-meter.webp`

- **Role:** The container above the reels that fills as Diamonds land (the rules call its filling purely visual), and the counter of the three free spins of the Hold & Win.
- **Subject:** A wide red outline with zigzag, bolt-like ends; a white arrow-banner shape; a white chevron band; a gold frame with three boxes; the numerals 1, 2 and 3 in white italic.
- **Style:** The same cut, slanted neon vocabulary as the frame, with lightning-shaped ends.
- **Rendering:** Thin glowing outline (the frame) and flat white shapes for tinting; the numerals are white with a dark blue drop edge.
- **Colour:** Mostly white for tinting (#ffffff 69%); the outline is red-orange #fb582f and #f79077, the counter frame gold #fdc025. The SceneCollector skeleton tints the fill dark red #7c0403 and orange #ff9a00.
- **Lighting:** Self-lit.
- **Ambience:** A gauge charging up: the chevrons point upward and inward like a level rising.
- **Materials:** Neon tube; light.
- **Variants:** Counter states 1, 2 and 3. The container is one shape; fifteen chevron slots in the skeleton give its fill levels.
- **Motion:** SceneCollector (28 bones, 43 slots) has show 0.58 s, idle 1 s, progress 1.67 s, collect 0.5 s, win 2 s and loops; in play the container sits behind the logo on the frame's top edge and white lightning runs along it when a diamond lands. ProgressBar (16 bones, 13 slots) has show, hide, anticipation 0.5 s and remove and reset animations for each of the three counts; seen in the bonus, the three-box counter takes the logo's place on the frame's top edge and shows 1 2 3, losing a number with each respin that lands nothing and refilling when a diamond lands.
- **Construction:** Seven sprites. The moving fill is the chevron band repeated and masked inside the banner shape.
- **Notes:** The names in the files are borrowed: the container is SceneCollector and the respin counter is ProgressBar. The unit id here follows the first use.
- **Measured:** bright, muted, warm and cool mixed, low contrast, strong highlights · brightness 86% · saturation 23% · contrast 12% · warm 30% / cool 4%
- **Palette (measured):** #ffffff light cyan 69%, #fb582f red 13%, #f79077 red 9%, #fdc025 orange 4%, #b63002 brown 3%

### Jackpot Prize plates

`jackpot-panel` · atlas · 10 parts · largest 476×242 · sheet `sheets/jackpot-panel.webp`

- **Role:** The six jackpots stacked at the left of the reels: GRAND, MEGA, SUPER, MAJOR, MINOR and MINI.
- **Subject:** A slanted plate outline with a gap in its top edge where the name sits, in gold and in red, for desktop and mobile; and the six jackpot names as outlined italic capitals.
- **Style:** The same neon parallelogram as the Cash plates, in gold; names in a condensed heavy italic.
- **Rendering:** Outlines are a bright line with a wide glow (soft edge 0.731). The names here are the Add copies: yellow outlines of the letters with empty faces, to be laid over the filled name as a glow.
- **Colour:** Gold #fee420 and #f9ab47 with a pale core #fee3b2; the second state red #fd2748. Fully warm (warm 1.0). In the Jackpot skeleton the plate fill is tinted dark blue #120037 and the glow gold #ffbd2f.
- **Lighting:** Self-lit.
- **Ambience:** The gold column is the richest part of the screen; GRAND is the largest plate and sits at the top.
- **Materials:** Neon tube over dark glass.
- **Variants:** Gold resting and a red state (seen in play: the SUPER plate lit and filled red during the Red Diamond's collection), desktop and mobile shapes; six names. One outline is scaled for all six plates (inference from there being a single Grand outline in the atlas and six sizes on screen).
- **Motion:** Jackpot (44 bones, 59 slots, six landscape and six portrait skins) has the same list as Payout: show, boost and its loops, multiplyShow, swap, win 1.33 s, winLoop, and Mega variants of the win animations. Seen in play: a plate flares gold and its value jumps (SUPER from 100X to 160X, GRAND from 1000X to 1600X with x3).
- **Construction:** Ten sprites: four outlines and six name glows. The filled names and the gold numerals are not in this unit: the names are in the jackpot splash unit (the dark blue copies) and the numbers come from the bitmap font.
- **Notes:** Jackpots and Cash Prizes are one component in two colours, gold and cyan, which keeps the growing-prize idea readable.
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 70% · saturation 69% · contrast 30% · warm 100% / cool 0%
- **Palette (measured):** #fee420 gold 28%, #f9ab47 orange 21%, #fd2748 red 20%, #fee3b2 light orange 19%, #fb726b red 9%, #fdda7a orange 3%

### Cash Prize plates

`cash-plates` · atlas · 6 parts · largest 363×295 · sheet `sheets/cash-plates.webp`

- **Role:** The frames of the nine Cash Prizes shown above the reels (1x to 10x), which the Cash Booster raises and Blue Diamonds collect.
- **Subject:** Empty slanted plates outlined in neon: a large one and a small one for the desktop layout and one for the mobile layout, each in cyan and in red.
- **Style:** Neon outline parallelograms, slanted like the lettering.
- **Rendering:** A thin bright line with a wide soft glow and nothing inside (soft edge 0.807, the softest unit of the interface).
- **Colour:** Cyan #1dbdfb with a pale core #92f4fe, and red #fa2020 with #f58498, in equal shares (cyan 0.504, red 0.496).
- **Lighting:** Self-lit.
- **Ambience:** A scoreboard of lit windows; in play the nine plates form a symmetric block above the reels with the 10X plate large in the centre.
- **Materials:** Neon tube over dark glass.
- **Variants:** Cyan is the resting state; the Red copies are the state of a plate while the Red Diamond's prize is being picked at the end of the bonus (seen in play on a jackpot plate, which also fills red; on the Cash plates in passing).
- **Motion:** Payout (37 bones, 57 slots, one skin per plate and layout) has show 0.58 s, boost 0.67 s with three boost loops, multiplyShow 0.83 s, swap 0.33 s, win 1.27 s and winLoop 0.67 s; it adds a lightning border (payoutWin), lightning pieces and arcs and a rising chevron effect. Seen in play: a plate flashes white when boosted, its number changes, and a small x2 or x3 appears beside it. At collection a plate is wrapped in the lightning border and a bolt carries its value down to a diamond.
- **Construction:** Six outline sprites only. The dark blue fill, its halftone and chevrons, and the gold numerals are added by the skeleton from shared shapes (the white square, bgHalftoneCentre) and the bitmap font, so one outline serves every value.
- **Notes:** The prizes are the main picture of this game: they take more screen area than the reels' frame, and they change on every boost.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, glow or soft effect · brightness 57% · saturation 73% · contrast 43% · warm 50% / cool 50%
- **Palette (measured):** #1dbdfb cyan 33%, #fa2020 red 32%, #92f4fe light cyan 14%, #f58498 red 10%, #f7e1ed light magenta 4%, #f24e61 red 3%


## Typography

Embedded fonts and lettering.

### Numeral fonts: gold Anton and white Anton

`font-anton` · atlas · 36 parts · largest 204×512 · sheet `sheets/font-anton.webp`

- **Role:** The bitmap fonts for every changing number: prize values on the plates, multipliers, win amounts and counts.
- **Subject:** Digits 0 to 9, x and X, comma, full stop, plus, minus, slash, question mark and asterisk in gold; a smaller white set of digits and punctuation.
- **Style:** Anton, a condensed heavy grotesque, slanted to match the game's italic lettering.
- **Rendering:** Gold set: a two-band face (light gold over deeper gold with a hard horizon line), a thin pale inner edge and a dark red-brown extruded outline to the lower right; crisp (soft edge 0.052). White set: plain white with a dark blue edge.
- **Colour:** Gold #f1c231 (55%), pale gold #f5f36c, red-brown #a83803 for the side.
- **Lighting:** From the top (16 of 17 measured parts): the upper band of each glyph is the lighter one.
- **Ambience:** Money numerals: the brightest warm thing on the dark blue plates.
- **Materials:** Polished gold.
- **Variants:** Two fonts (Anton and AntonWhite). Each has one page of always-loaded glyphs and single-glyph pages loaded on demand; this game loaded only the capital X of each.
- **Motion:** None of their own; the skeletons scale and flash the numbers.
- **Construction:** Not in the game's atlas: both come from the provider's shared font service (`fonts-v2`), a 2048x1024 page of 18 glyphs up to 252 px tall for gold and a 1024x128 page of 16 for white. The descriptors also list currency signs, letters and whole words (WAY, WAYS, heart, sword) on pages this game never asked for; the 97 entries the reader had cut wrongly from the main page were removed from this run's manifest.
- **Notes:** Fire Rail Express: Hold & Win took a different font from the same service (purple with a gold rim), so the numeral style is chosen per game from a provider library.
- **Measured:** bright, vivid, warm, high contrast, hard-edged, strong highlights · brightness 70% · saturation 74% · contrast 67% · warm 93% / cool 7% · brighter towards: top (16), top-right (1)
- **Palette (measured):** #f1c231 gold 55%, #a83803 brown 19%, #f5f36c gold 16%, #fbfdfa light green 6%, #c78728 orange 2%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts
- `shared-tile0`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 454 components cut from 34 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
