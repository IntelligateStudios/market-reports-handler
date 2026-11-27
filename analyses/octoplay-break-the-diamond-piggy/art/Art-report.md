# Break The Diamond Piggy: art report

octoplay · run `2026-11-27-0958-octoplay-break-the-diamond-piggy` · captured 2026-11-27

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/break-the-diamond-piggy

**Extracted:** 886 named components from 39 textures in 39 atlases; 64 Spine skeletons; 23 frame sequences (496 frames); 3 fonts. Grouped into 27 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A sunny cruise-ship comedy about two rich pigs: a cream reel board in a thin gold frame on a white pool deck, five golden piggy banks above the reels waiting to crack, a chained blue Diamond Piggy over five enamel jackpot plates, and a night-club lounge kept for the bonus.

**Style.** Bright 3D-look cartoon in the manner of a family animation film, with caricature pigs as the stars (a cigar-and-cocktail tourist and a pin-up in sequins) and polished toy-like objects around them. The world is clean, new and expensive: white ship, blue pools, gold everywhere. One motif brands everything: the pig's snout, on the royals, the coin's back, the padlock, the clock and the flying tokens.

**Rendering.** Smooth airbrushed volumes with hard cut edges for every object (soft edge: reel board 0.034, backdrops 0.034, jackpot plates 0.058, golden piggy banks 0.078, Ms. Piggy 0.086, high symbols 0.089, Mr. Piggy 0.125), flat-faceted crystal for the diamonds and the Diamond Piggy, and soft white light for every effect (bursts 0.909, rays 0.954). Lettering is flat two-tone with a thick outline.

**Colour.** White, cream and pool blue as the ground, gold as the money, and saturated enamel colours for whatever must be told apart. Measured over the art files: near-white #f4f6f2 10% (the ship, the haze and white effect sprites), near-black violet #130616 9% (the lounge and outlines), gold-orange #eeb711 9%, grey #bbb8b6 8%, brown #7e3610 8%, blue #095cb9 5%, cream #f5ddb6 4%, dark blue #0e1557 3%. The board is the lightest large surface (cream #f5dbbd, brightness 0.84), which is rare for a slot: symbols are dark and saturated on a pale ground. Ice blue is reserved for the diamond (Wild, Diamond Piggy: 93% cool); a five-colour scale ranks the royals and, separately, the jackpot plates.

**Lighting.** High daylight: objects are lit from the top, top-left or top-right with warm red-orange core shadows and white glints, and a white haze is painted into the middle of the backdrop behind the board. The bonus lounge reverses it: a dark room with stage spots, pink and gold on the ceiling and cyan light from the crystal pig.

**Ambience.** Carefree, rich and a little cheeky: a luxury holiday where the only job is breaking piggy banks. Day on deck for the base game; a night version of the deck and a casino lounge for the features (the last two read from the files and the intro, not seen in play).

**Shape language.** Round and fat throughout: piggy banks, coins, snouts, bellies, swim ring, fountain bowl, inflated letters. The counter-shapes are the hexagonal jackpot plates and the diamond's facets. Frames are thin and straight; nothing is ornate except the small gold leaf sprigs on the high-symbol tiles and the scrolls on the Wild.

**Materials.** Polished gold, cut crystal, coloured enamel, pink skin, straw, printed cotton, sequins, pearls, leather, glass and liquid, tiled water, white painted steel, velvet and neon in the lounge.

**Typography and lettering.** Four voices. The logo: fat cartoon capitals, one colour per word (green, yellow, ice blue, pink) on a purple strip. Jackpot names and jackpot captions: black slab capitals with a gold rim. Feature captions and WILD: rounded yellow capitals with a dark violet outline. Win tiers: flared two-tone capitals in blue, magenta and yellow. Numbers are the provider's Ultra bitmap font, black with a gold rim on coins, plates and win amounts and cream with a wine outline on the progress counter; the low symbols are inflated letters with a snout. Small interface text is the shell's Poppins (Regular, SemiBold, Bold).

**Motion.** All rigged motion is Spine 4.2.43: 64 skeletons in one bundle file. The largest are Ms. Piggy (144 bones), Mr. Piggy (118), the breakable Diamond Piggy of the Smash & Win (100), the chained Diamond Piggy (93), the intro (81) and the feature splash (75). Beside them 23 frame sequences (496 frames): 232 frames of white glints that run over symbols, frames and the progress bar, 90 of a banknote and two diamonds turning, 83 of white bursts and reel anticipation, 61 of birds and window sparkle, 30 of the snout coin turning. Seen in play: reels of floating letters and framed props on the cream board; Golden Coins flipping on their axis to show a number, then throwing coins and snout tokens up at the golden piggy banks; stacked blue-diamond Wilds; a gold win line and the amount counting up in large black and gold numerals over a white-gold flash; the Piggy Progress number falling with each spin from 10 to 0; then FEATURE UNLOCKED, a golden card opening in a white flash with five reel-high Mr. Piggy figures that fly off it onto the reels, and the counter starting again at 25. No skeleton frame is shown in this report, because the project's renderer is written for Spine 3.7.

**Variants and themes.** Three scenes from three half pictures: the deck by day (normal), the deck by night (special) and the lounge (the Smash & Win and the intro); rigs carry skins normal, special and bonus. Each golden piggy bank exists in 18 paintings (six stages of cracking in three looks). Two pigs as full-reel figures, as portrait tiles in the paytable and as heads on the logo. Five jackpot plates from one shape in five colours; four Jackpot Coin faces from one coin. Landscape and portrait skins for logo, counter and positions (only landscape at 1280x720 was captured).

**How it is built.** Two packed 4096 px atlas pages hold 819 sprites, 496 of them animation frames, with 13 localised lettering files (en-GB), five loose textures and one skeleton bundle. Backdrops ship as the left half of a symmetric scene (1034x1885), with the middle washed to white where the board covers it. Characters and high symbols are layered cut-outs on bones; coins are front, back and side pictures flipped by a rig; the Diamond Piggy of the bonus is literally its 14 breakable pieces. Every glint and burst is a white sprite or sequence tinted in the game. Paytable pictures, the flattened logo, the numeral fonts and the interface come from the provider's shared services.

**Consistency.** High. Gold settings, the snout motif and the same top-lit airbrushed finish run from the backdrop to the smallest token, and the pigs' pink and the diamond's blue are kept off everything else. Seams: the win-tier lettering and the yellow captions are flatter and more generic than the painted world; the white birds are plain silhouettes; and the caricature pigs are drawn with more grit (cigar, stubble, heavy make-up) than the toy-like piggy banks beside them.

**What to take from it.** (1) Put the game's long-term goal on screen as an object. The chained Diamond Piggy, the pocket-watch counter and the five golden banks are the whole top third of the base game: the player sees what is locked, how far it is and what each reel is building towards, before reading a word. (2) Paint anticipation, not only results. One golden piggy bank is painted 18 times (six stages of cracks in three looks) although, as the rules state, the cracks do not change the odds. That is where this game spends its illustration budget, and it is a kind of work image generation does well: one object, many controlled states. (3) A pale board is possible. Cream #f5dbbd under dark, saturated symbols reads cleanly and makes the game look unlike the dark-cabinet slots around it; high symbols bring their own coloured tile, low symbols float. (4) Theme the royals with one detail. A snout worked into 10, J, Q, K and A, plus an 18-frame white glint each, makes the cheapest symbols belong to the game with five pictures. (5) Reserve one colour for the prize. Ice blue appears only on the diamond Wild, the falling diamonds and the Diamond Piggy, so the screen's one cold object is the thing to want. (6) Build breakable things from their pieces. The bonus pig is 14 shell pieces and 10 blurred shards assembled into a whole; breaking it needs no extra drawing. For our packages: when an object must break, generate it whole, then cut it. (7) Half a backdrop is enough when the board sits in the middle: each scene is one 1034x1885 picture for the left side, mirrored (by inference) for the right, with the centre left as haze. (8) Two-sided flat objects flipped by a rig (coin face, snout back, edge disc) give a 3D turn for three pictures; drawn frames are kept for what bones cannot do (a tumbling banknote, a turning gem, glints). (9) Characters double as symbols and presenters: each pig is one large rig (118 and 144 bones) used as the full-reel Collector, in the intro, and, by its animation names, in the big-win scene. Design the character at reel height first. (10) From the same provider and framework as the six earlier Octoplay runs (same shell, Poppins, Double Chance card, Ultra numerals, one skeleton bundle in Spine 4.2.43, packed 4096 px pages), and by the provider's own description a sequel ('The pigs are back'): the framework is constant, and the art budget moves into characters and into a persistent unlock structure, here four levels over 10, 25, 50 and 75 spins.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 53% · saturation 61% · contrast 63% · warm 49% / cool 37% · brighter towards: top (84), top-left (46), top-right (39)

Palette: #f4f6f2 light green 11%, #130616 black 10%, #eeb711 orange 9%, #bbb8b6 grey 9%, #7e3610 brown 8%, #095cb9 blue 6%, #f5ddb6 light orange 4%, #0e1557 dark blue 4%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 2 | 58% | 48% | 68% | 19% / 58% | #b9b8b6 grey 25%, #ebeeea white 15%, #0758bf blue 12% |
| Reel board | 1 | 84% | 26% | 39% | 90% / 0% | #f5dbbd light orange 76%, #ffffff light orange 10%, #be8f4a orange 5% |
| Symbols | 6 | 56% | 72% | 63% | 64% / 21% | #f5c40c gold 18%, #8c3d0d brown 12%, #fdfcfa light orange 11% |
| Characters | 4 | 39% | 72% | 60% | 44% / 50% | #1b081d black 28%, #0b306b dark blue 9%, #0885b8 cyan 7% |
| Logo and title | 2 | 50% | 65% | 58% | 74% / 21% | #8a5b28 brown 28%, #a78d4d orange 13%, #da836a red 11% |
| Win celebrations and banners | 3 | 51% | 75% | 67% | 74% / 23% | #eba30d orange 17%, #5d3829 brown 13%, #f2c854 orange 13% |
| Effects | 3 | 79% | 26% | 22% | 7% / 32% | #fffeff light purple 56%, #854eb8 purple 12%, #cbbcf7 light purple 12% |
| Game interface | 3 | 53% | 78% | 66% | 84% / 10% | #e7b312 gold 23%, #a55a0b brown 22%, #f4de64 gold 14% |
| Typography | 1 | 38% | 57% | 95% | 99% / 0% | #0c0302 black 44%, #fcf3b8 light gold 21%, #510e0e dark red 9% |
| Provider interface (shared) | 2 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backdrops: the cruise ship's pool deck by day and by night

`backgrounds` · atlas · 18 parts · largest 1034×1885 · sheet `sheets/backgrounds.webp`

- **Role:** The scene behind the board: bgNormal (base game), bgSpecial (by the skins named normal, special and bonus, the feature scenes; the special picture was not seen in play) and the loose pieces that move over them: fountain bowl and water, pool surface, a swim ring with its shadow and ripples, a waterfall wave, a pile of coins and a purple curtain.
- **Subject:** The sun deck of a white cruise ship: a round pool and a long tiled pool, rows of orange sun loungers on brown planks, a railing with round lamps, palms in pots, a glass-domed white superstructure, and sea and cloud behind. The night version keeps the layout under a starry dark blue sky with a magenta deck.
- **Style:** Bright, clean holiday cartoon in a 3D look: simplified architecture with rounded corners, no people large enough to read, everything new and polished.
- **Rendering:** Smooth gradient volumes with hard edges (soft edge 0.034 for the unit); pool water is a tile grid under white caustic lines; a white haze is painted into the middle of both pictures, where the board stands.
- **Colour:** Measured: grey #b9b8b6 25% and white #ebeeea 15% (the ship and the haze), pool blue #0758bf 12%, light cyan #94e9f9 6%, night blue #01044b 6%, plank brown #752f0f 4%. Hues are 53% blue and 24% cyan with orange as the accent (the loungers).
- **Lighting:** Day: high sun from the upper left, white bloom on the ship, short shadows. Night: the same forms lit by the deck lamps and the pool from below, with a magenta cast on the planks.
- **Ambience:** A first-class holiday: sunny, rich, spotless and empty, waiting for the two pigs.
- **Materials:** White painted steel, glass, varnished planks, tiled water, canvas loungers, palm leaves, marble (the fountain bowl), satin (the curtain), gold coins.
- **Variants:** Two pictures of 1034x1885 (bgNormal, bgSpecial) and two matching patches for the ship's window (day, night); two fountain bowls (153x122, 152x122); the swim ring in a top and a side view; one curtain half (curtainL, 331x702). The skeletons carry three skins: normal, special and bonus.
- **Motion:** BackgroundEffects (51 bones, 68 slots) has loops of 1.33 s, a 2 s loopLights, a 1 s arcLights and a 49.98 s loopFloat, by its name the swim ring drifting across the pool (inference). The fountain is two water sprites over a marble bowl; a 1024x1024 grey noise picture (seaDisplacement) is, by its name, the map that makes the water shimmer (inference).
- **Construction:** Each backdrop is one tall picture that holds the left half of the scene; in play the scene is symmetric about the board, so the picture is, by inference, mirrored for the right half. The centre is washed out on purpose, so no detail is spent behind the reels. Moving pieces are separate sprites on bones.
- **Notes:** bgPickerBonus, the third scene, is in the unit of the Smash & Win. The night picture and the curtain were not reached in play.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 58% · saturation 48% · contrast 68% · warm 19% / cool 58% · brighter towards: top (2), right (1), bottom-right (1)
- **Palette (measured):** #b9b8b6 grey 25%, #ebeeea white 15%, #0758bf blue 12%, #94e9f9 light cyan 6%, #01044b dark blue 6%, #61a6e6 blue 6%

### Life in the scene: birds, petals and window sparkle

`scene-life` · atlas · 67 parts · largest 122×207 · sheet `sheets/scene-life.webp`

- **Role:** Small moving details that keep the backdrop alive: two flying birds, six flower petals and a 40-frame sparkle for the ship's building.
- **Subject:** White bird silhouettes in two sizes (74x67 and 53x42), petals in violet, yellow and pink of about 20 px, and a sprinkle of white-cyan glitter on a 122x207 field.
- **Style:** Flat silhouettes and tiny soft shapes: stage dressing, not illustration.
- **Rendering:** The birds are plain white shapes meant to be tinted; the sparkle frames are soft points (soft edge 0.723 for the unit); petals have one gradient each.
- **Colour:** Measured: light cyan #effbfe 66%, #a3dcf2 21%, cyan #78cff3 10%. The petals add small violet and yellow accents that the measure does not rank.
- **Lighting:** None of their own: the pieces are light themselves or take the scene's tint.
- **Ambience:** Sea air: gulls far off, petals on the breeze, glass catching the sun.
- **Materials:** Feathers reduced to a silhouette, petals, glitter.
- **Variants:** Two birds, six petals, one sparkle sequence.
- **Motion:** Frame sequences: particleBird1 11 frames and particleBird2 10 frames of a wing beat (the rigs ParticleBird1 and ParticleBird2 loop them in 0.35 s and 0.32 s); bgBuildingMagicEffect 40 frames of glitter rising and fading. Petals are single pictures moved as particles (BackgroundParticles, ForegroundParticles).
- **Construction:** Drawn frames for the two things that change shape (wings, glitter), single sprites scattered by the engine for the petals.
- **Notes:** A cheap layer: 67 small sprites, 61 of them frames of three loops.
- **Measured:** bright, muted, warm and cool mixed, low contrast, glow or soft effect, strong highlights · brightness 91% · saturation 17% · contrast 8% · warm 15% / cool 63%
- **Palette (measured):** #effbfe light cyan 66%, #a3dcf2 light cyan 21%, #78cff3 cyan 10%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board: cream marble in a gold frame

`reel-board` · atlas · 8 parts · largest 1004×619 · sheet `sheets/reel-board.webp`

- **Role:** The 5x3 reel field and its helpers: the board picture, a row divider, the win line and its end cap, and white guide and glow squares the game tints.
- **Subject:** A 1004x619 cream panel with five columns marked by thin vertical lines, inside a narrow polished gold frame.
- **Style:** Plain and bright, the opposite of an ornate cabinet: a sheet of paper for the symbols to sit on.
- **Rendering:** A faint mottled marble or parchment texture, flat lit; the frame is a thin bevel with highlights. Hard-edged (soft edge 0.034).
- **Colour:** Measured: cream #f5dbbd 75%, white 10%, gold-ochre #be8f4a 5% and #8a581f 4%. Brightness 0.84, hues 99% orange: the lightest large surface in the game.
- **Lighting:** Even, with small highlights along the frame's top edge.
- **Ambience:** Sunlit and airy; it lets the saturated symbols carry all the colour.
- **Materials:** Polished gold, pale stone or parchment.
- **Variants:** One board picture; the SlotBackgrounds and SlotFrame rigs carry skins normal, special and bonus, so the board is, by inference, tinted or swapped per scene. Only the normal state was seen in play.
- **Motion:** SlotFrame idles in 1.72 s; ReelEffect (0.67 s) and SpinEffect (1.25 s) flash over the reels; the win line is a 16x25 gold segment stretched across the paying row.
- **Construction:** One picture for the whole field rather than five reel strips; dividers, guides and glows are white or gold primitives.
- **Notes:** The board has no cell boxes: low symbols float on the cream, high symbols bring their own framed tile.
- **Measured:** bright, saturated, warm, medium contrast, hard-edged, strong highlights · brightness 84% · saturation 26% · contrast 39% · warm 90% / cool 0%
- **Palette (measured):** #f5dbbd light orange 76%, #ffffff light orange 10%, #be8f4a orange 5%, #8a581f brown 4%, #dcb289 orange 3%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Paytable pictures of the 15 symbols

`help-symbol-pictures` · atlas · 15 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** One flat 225x225 picture per symbol, served by the provider's asset service for the help pages: 10, J, Q, K, A, hat, passport and glasses, cocktail, suitcase, Wild, Golden Coin, Mr. Piggy, Ms. Piggy, Jackpot Coin and the empty shell.
- **Subject:** The whole symbol set at a glance: five fat letters with a pig's snout worked into each, four framed holiday props, a blue diamond over WILD, a plain gold coin, the two pigs as head-and-shoulders portraits, a black and iridescent JACKPOT coin and a small violet seashell.
- **Style:** The game's own symbols, flattened; the two pigs are cropped to portraits here although on the reels they are full-height figures.
- **Rendering:** Hard-edged and saturated (soft edge 0.038, saturation 0.743, contrast 0.739).
- **Colour:** Measured: brown #8b3c11 16% (outlines and wood), gold #f4c212 14%, orange #c57b1a 10%, pale gold #f8e575 7%, blue #76baea 5%, dark blue #1c1264 4%.
- **Lighting:** Top light on almost every picture (7 of the measured parts).
- **Ambience:** A souvenir stall: bright, tidy, everything on its own card.
- **Materials:** Enamel letters, gold, straw, paper, glass, leather, crystal, pearl shell.
- **Variants:** 15 pictures, named tile1 to tile15 in the asset service's numbering (12 Mr. Piggy, 13 Ms. Piggy, 14 the Jackpot Coin, 15 the shell).
- **Motion:** None; these are stills for the paytable.
- **Construction:** Flattened exports. The game's atlas numbers the same symbols differently in places (its tile13 sprites include the Jackpot Coin's faces).
- **Notes:** The quickest reference for the symbol set; compare the layered versions in the other symbol units.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 50% · saturation 74% · contrast 74% · warm 69% / cool 26% · brighter towards: top (7), top-right (1)
- **Palette (measured):** #8b3c11 brown 16%, #f4c212 gold 14%, #c57b1a orange 10%, #f8e575 gold 7%, #76baea blue 5%, #12050a black 4%

### Low symbols: 10, J, Q, K, A with a snout

`symbols-royals` · atlas · 95 parts · largest 150×132 · sheet `sheets/symbols-royals.webp`

- **Role:** The five low-paying symbols and their win highlights.
- **Subject:** Fat rounded characters, each in its own colour with a gold rim, and each with a pig's snout built into the glyph: the zero of the 10, the bowl of the Q, the serifs of J, K and A.
- **Style:** Toy-like inflated lettering; the snout is the brand mark that makes ordinary royals belong to this game.
- **Rendering:** A quilted or woven pattern on the face, a thick gold bevel around it and a darker gold side; hard outer edge. The unit measures bright and soft (brightness 0.72, soft edge 0.36) because 90 of its 95 parts are white highlight frames.
- **Colour:** By eye from the sheet: 10 blue, J green, Q magenta, K orange-red, A gold. Measured over the unit: white 39% (the highlight frames), brown #9e5218 13%, gold #eab23d 11% and #fbec83 10%, magenta #e30fdc 4%, red #f5420e 4%.
- **Lighting:** Top light with a gloss band across the upper third of each letter.
- **Ambience:** Cheerful and childlike.
- **Materials:** Enamel or padded leather faces in gold settings.
- **Variants:** Five glyphs between 80x147 (J) and 150x132 (10). They sit on the cream board with no tile behind them.
- **Motion:** TileContainerJuniors (5 bones, skins tile1 to tile5): onLand 0.42 s, win 0.6 s. Each glyph has its own 18-frame highlight (juniorHighlightX for the 10, J, Q, K, A): a white glint that crosses the letter and shows its shape in the middle frames.
- **Construction:** One sprite per glyph plus a drawn glint sequence masked to the glyph: 5 pictures and 90 frames.
- **Notes:** A small idea worth copying: one repeated detail (the snout) themes the cheapest symbols without drawing new objects.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 72% · saturation 45% · contrast 47% · warm 48% / cool 9% · brighter towards: top (2), right (1)
- **Palette (measured):** #ffffff light gold 39%, #9e5218 brown 13%, #eab23d orange 11%, #fbec83 gold 10%, #e30fdc magenta 4%, #f5420e red 4%

### Hold & Win symbols: the Jackpot Coin and the empty shell

`symbols-hold-and-win` · atlas · 11 parts · largest 203×209 · sheet `sheets/symbols-hold-and-win.webp`

- **Role:** The symbols that, by the rules, only appear in the Hold & Win: the Jackpot Coin, which reveals one of four jackpot names, and the Empty symbol.
- **Subject:** A black coin with an iridescent mother-of-pearl rim and an octagonal gem in the middle, labelled JACKPOT; four gold coins with a coloured enamel ring (green Major, red Maxi, magenta Mini, violet Minor) and their names in black capitals with a gold rim; a small violet scallop shell.
- **Style:** The coin family extended: same shape as the Golden Coin, with colour doing the naming.
- **Rendering:** Hard-edged and saturated (soft edge 0.038, saturation 0.813); the back coin's rim is painted as a swirl of pink, cyan and violet.
- **Colour:** Measured: gold #ebad05 33%, brown #9e5007 13%, black #090507 10%, yellow #feea15 4%, dark red #700606 3%, green #276f01 2%, red #dd0502 2%.
- **Lighting:** Top light on every coin (7 of the measured parts).
- **Ambience:** The night-time, high-stakes side of the game.
- **Materials:** Gold, coloured enamel, black lacquer, mother-of-pearl, a cut gem, shell.
- **Variants:** One back coin and four named faces (203 px), five words, one shell (63x69). There is no Grand coin: by the rules the Grand is paid when all five Piggy Banks break in one feature.
- **Motion:** TileMystery (16 bones, skins jackpot0 to jackpot3): onLand 0.42 s, loop 2 s, activate 2.17 s, the turn from the black back to the named face (inference from the skins and the two-sided art). TileEmpty lands in 0.42 s.
- **Construction:** A two-sided coin with swappable faces and words: five pictures and five words make four jackpot symbols.
- **Notes:** Not seen in play: the Hold & Win did not come in this run. The help page shows the JACKPOT coin beside a 10x coin and Ms. Piggy.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 48% · saturation 81% · contrast 75% · warm 74% / cool 21% · brighter towards: top (7), top-right (1)
- **Palette (measured):** #ebad05 orange 33%, #9e5007 brown 13%, #090507 black 10%, #feea15 gold 4%, #700606 dark red 3%, #276f01 dark green 2%

### High symbols: hat, passport and glasses, cocktail, suitcase

`symbols-premium` · atlas · 39 parts · largest 191×191 · sheet `sheets/symbols-premium.webp`

- **Role:** The four high-paying symbols, each a holiday prop on a coloured, gold-framed tile.
- **Subject:** A straw hat with a blue band on magenta; a blue passport with boarding passes and gold-rimmed purple sunglasses on green; an orange cocktail with ice, a paper umbrella and a sugar rim on blue; an open leather suitcase with gold coins, a pink cloth, banknotes and a string of pearls on red.
- **Style:** 3D-look props with exaggerated size against a tile they overflow: the hat brim, the glasses and the suitcase all break the frame.
- **Rendering:** Smooth painted volumes, hard edges (soft edge 0.089), a burst of lighter colour in the middle of each tile and two gold leaf sprigs in opposite corners of the frame.
- **Colour:** Measured: orange-red #ef4608 8%, green #01de01 6% and #038b01 4%, cyan #32b1ec 5%, magenta #f431b9 4%, dark red #4a0c02 5%. Saturation 0.807: the tiles are the most saturated flat areas in the game.
- **Lighting:** From the top right on the props (5 of the measured parts); the tile glows from its centre.
- **Ambience:** Packing for a rich holiday.
- **Materials:** Straw, leather, paper, tinted glass, liquid and ice, gold, pearls.
- **Variants:** Four tiles of 191x191 in four colours (magenta, green, blue, red-orange), each prop cut into layers: hat in back, front and cord; passport and glasses; glass back and front, juice back and front, ice, umbrella; suitcase back and front, coin group, two coins, pearls.
- **Motion:** Tile6 to Tile9 (18 to 24 bones each): onLand 0.42 s, win 0.6 s; the layers let the prop lift off its tile. One shared 18-frame highlight runs around the frame (seniorsHighlights). In play the props hang over the tile edge by a few pixels even at rest.
- **Construction:** Frame tile plus two to six prop layers per symbol on a small rig: four symbols from 21 pictures and one shared highlight.
- **Notes:** The coloured tiles sort the high symbols from the letters at a glance; colour, not size, does the ranking.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 47% · saturation 81% · contrast 60% · warm 57% / cool 30% · brighter towards: top-right (5), top (2), bottom-right (1)
- **Palette (measured):** #ef4608 orange 8%, #01de01 green 6%, #32b1ec cyan 5%, #4a0c02 dark red 5%, #038b01 dark green 4%, #f431b9 magenta 4%

### Wild: the blue diamond

`symbol-wild` · atlas · 40 parts · largest 191×191 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol, which substitutes for all paying symbols except Golden Coins and, once the Smash & Win is unlocked, throws a diamond at the Diamond Piggy Bank (the rules).
- **Subject:** A large brilliant-cut blue diamond over the word WILD in yellow with a purple outline, on a golden sunburst tile with scrolled corners and a line of gold coins at its foot.
- **Style:** The jewel of the set: the same faceted blue as the Diamond Piggy.
- **Rendering:** Flat facets in light blue to cyan with violet at the base and white glints; the lettering is flat yellow with a dark violet extrusion; hard edges, strong highlights.
- **Colour:** Measured: gold #f7ba15 18% and #fee560 17%, near-white #fcfbf6 13%, cyan #85daf9 10%, orange #df7d07 9%, blue #1167c9 4%.
- **Lighting:** Top light; the tile radiates from the centre behind the stone.
- **Ambience:** Treasure.
- **Materials:** Cut diamond, gold, enamel lettering.
- **Variants:** One tile (191x191), one diamond (214x167, wider than its tile), one word, one coin row.
- **Motion:** TileWild (12 bones): onLand 0.42 s, win 0.6 s, loop and loopWins 1.33 s. Two 18-frame white highlights: one across the diamond's facets (tile10DiamondHighlight), one across the word (tileWildHighlight). TileWildEffect is a 0.33 s flash.
- **Construction:** Four layers (tile, coins, diamond, word) and two drawn glint sequences.
- **Notes:** Seen in play stacked: seven Wilds on reels 2, 4 and 5 in one spin, each diamond overlapping the tile above it, for a 10.00 line win.
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 69% · saturation 65% · contrast 58% · warm 57% / cool 30% · brighter towards: top (2)
- **Palette (measured):** #f7ba15 orange 18%, #fee560 gold 17%, #fcfbf6 light yellow 13%, #85daf9 cyan 10%, #df7d07 orange 9%, #b36a16 orange 5%

### Golden Coin: the cash symbol

`symbol-golden-coin` · atlas · 24 parts · largest 380×380 · sheet `sheets/symbol-golden-coin.webp`

- **Role:** The symbol that carries a Cash Prize (1x to 10x, the rules) and throws a coin at the golden Piggy Bank above its reel.
- **Subject:** A thick gold coin with a plain face for the number and, on the back, a pig's snout in relief; a white disc for its edge-on view; a small coin for the throw; a 380x380 white burst.
- **Style:** The simplest object in the game, drawn as a polished cartoon coin.
- **Rendering:** Concentric bevels, a soft diagonal sheen on the face; the unit measures bright (0.837) because the burst and highlight frames are white.
- **Colour:** Measured: near-white #fffdfa 44% (burst and highlights), gold #fcda06 34%, orange #e09205 16%, brown #a25605 4%. Hues: 57% yellow, 43% orange, nothing else.
- **Lighting:** Top light with a moving glint.
- **Ambience:** Plain money.
- **Materials:** Gold.
- **Variants:** Face (tile11Coin, 203x209), a brighter copy (tile11CoinAdd), the snout back (tile11BackCoin), the side, and the 60 px thrown coin. The value is written with the provider's numeral font, black with a gold rim.
- **Motion:** TileCash (9 bones): onLand 0.42 s, loop 2 s, collect 0.87 s; an 18-frame highlight sweeps the face (tile11CoinHighlight). Seen in play: landed coins turn on their vertical axis, showing the edge and the snout back before the number, and a coin flies up to the piggy bank above.
- **Construction:** Front, back and side pictures turned by a rig give a 3D flip without drawn frames; only the glint is a sequence.
- **Notes:** The snout on the back ties even the money to the pigs.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 84% · saturation 55% · contrast 30% · warm 57% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #fffdfa light orange 44%, #fcda06 gold 34%, #e09205 orange 16%, #a25605 brown 4%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Smash & Win: the big Diamond Piggy and its lounge

`smash-and-win-diamond-piggy` · atlas · 41 parts · largest 1034×1885 · sheet `sheets/smash-and-win-diamond-piggy.webp`

- **Role:** The art of the Smash & Win bonus (Piggy Progress level 4, the rules: each tap on the Diamond Piggy Bank awards a cash prize) and of the intro screen, which shows the same pig and room: the third backdrop, the large pig in breakable pieces, coins, and a dark figure of Mr. Piggy.
- **Subject:** A night-club lounge inside the ship (round ceiling lamps, a chandelier, an aquarium wall with columns, red armchairs, a stage with a lit arch and a palm in neon); a large blue crystal pig with a captain's cap, built from 14 shell pieces and 10 motion-blurred shards; heaps and stacks of gold coins; Mr. Piggy as a 381x539 dark silhouette.
- **Style:** The game's most theatrical scene: stage light and deep colour against the white daylight of the deck.
- **Rendering:** The room is painted in saturated gradients with bloom on every lamp; the pig's pieces are faceted crystal with thick, pale broken edges; the shards carry painted blur.
- **Colour:** Measured: near-black violet #18081e 36%, dark blue #0a316c 11%, cyan #0686b6 8% and #0adae5 4%, wine #621e30 6%, gold #f0ae10 5%. Brightness 0.314: the darkest unit of the game.
- **Lighting:** Spot and stage light from above (top on 11 of the measured parts), pink and gold on the ceiling, blue from the aquarium; the pig glows cyan from inside.
- **Ambience:** The ship's casino lounge at night: showtime.
- **Materials:** Cut crystal, gold, velvet armchairs, glass, neon.
- **Variants:** One room (bgPickerBonus, 1034x1885); the pig's eyes, brows, ears and cap as separate parts; 14 pieces and 10 'patche' shards; coin pile, coin group and single coins.
- **Motion:** PickerBonus (100 bones, 76 slots) has five hits of 0.33 s, each followed by a 0.58 s break (hit0Break to hit4Break), and a win: the pig breaks apart in five steps (inference from the names). PickerBonusPicker (23 bones) has hit0 to hit2, fsHit and four idles, by its name the thing that strikes (inference). PickerBonusSum flips a prize (0.83 s); the splash shows in 0.95 s. The GameSplash rig (81 bones, loop 4.5 s) animates the intro, where the pig stands on a heap of coins with four golden piggy banks behind it.
- **Construction:** A destructible object made by hand: the whole pig is the sum of its 14 pieces, so breaking it is only a matter of moving them apart, with blurred shards and coins filling the gaps. The room is one half picture like the deck.
- **Notes:** Not reached in play (it needs 160 normal-game spins of progress, by the rules: 10, 25, 50 and 75). The intro screen is the only real frame of this art in the run.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 31% · saturation 77% · contrast 64% · warm 38% / cool 54% · brighter towards: top (11), top-right (6), top-left (4)
- **Palette (measured):** #18081e black 36%, #0a316c dark blue 11%, #0686b6 cyan 8%, #621e30 dark red 6%, #f0ae10 orange 5%, #f5bd94 light orange 5%

### The Diamond Piggy Bank, chained (above the jackpots)

`diamond-piggy-bank` · atlas · 48 parts · largest 283×257 · sheet `sheets/diamond-piggy-bank.webp`

- **Role:** The blue crystal piggy bank at the top left of the base game, bound in a gold chain with a snout-shaped padlock. By the rules it is unlocked at Piggy Progress level 4, after which Wilds throw diamonds at it and it can start the Smash & Win.
- **Subject:** A round piggy bank cut from blue crystal with a coin slot, a faceted snout, small ears and friendly cartoon eyes; a captain's cap for it; a gold chain in whole, shining and broken versions; a gold padlock whose face is a pig's snout.
- **Style:** A toy made precious: the simplest pig shape in the game, with a low-poly gem surface.
- **Rendering:** Flat triangular facets in four or five blues with white edge glints; the unit as a whole measures soft (soft edge 0.665) because 26 of its 48 parts are soft highlight frames. Chain and lock are polished gold with hard highlights.
- **Colour:** Measured: light cyan #e8fefe 31% and #a2fcfd 20%, cyan #65f1fb 13% and #12c3db 12%, blue #0870a9 6%, dark blue #07294f 4%. 93% cool: the one cold object on a warm, golden screen.
- **Lighting:** From the top left (13 of the measured parts); the highlights are drawn as separate white frames.
- **Ambience:** The prize in the display case: desirable, locked, a little smug.
- **Materials:** Cut crystal, gold chain and lock, white cap cloth with a gold anchor badge.
- **Variants:** One body (283x257); chain up, chain bottom, their shine copies and a set of broken links; lock, shackle and shackle piece; the cap in front and back parts.
- **Motion:** SceneCollector (93 bones, 80 slots): six idles from 0.33 s to 1.83 s, activate 0.67 s, activateBonus 0.83 s, collect 0.42 s, move 0.67 s, a 2.67 s loop and four unlock steps (unlock0 to unlock2 0.58 s, unlock3 0.92 s), by their names one per Piggy Progress level (inference). A 26-frame white sequence (sceneCollectorHighlight) sends cracks of light across the crystal. In play it sat still under its chain, blinking.
- **Construction:** A rigged cut-out with face parts (sclera, iris, brows, mouth, nose, ears) on a single body sprite; the glitter is a drawn frame sequence laid over it.
- **Notes:** The same pig is rebuilt much larger, in breakable pieces, for the Smash & Win (its own unit).
- **Measured:** bright, saturated, cool, medium contrast, glow or soft effect, strong highlights · brightness 78% · saturation 48% · contrast 26% · warm 6% / cool 94% · brighter towards: top-left (13), bottom-left (2), left (1)
- **Palette (measured):** #e8fefe light cyan 32%, #a2fcfd light cyan 20%, #65f1fb cyan 13%, #12c3db cyan 12%, #0870a9 blue 7%, #042b4f dark blue 4%

### Mr. Piggy: the tourist Collector (full reel)

`mr-piggy-collector` · atlas · 69 parts · largest 347×631 · sheet `sheets/mr-piggy-collector.webp`

- **Role:** The male pig, the Collector symbol that lands in the normal game once Piggy Progress level 1 is unlocked (the rules) and one of the two figures of the intro. This unit holds his full-height rig parts, his reel-high frame and two reel-high backdrops.
- **Subject:** A grinning pink pig as a rich tourist: straw hat with a blue band, round gold glasses with purple lenses, a moustache, a cigar, a yellow shirt printed with palms, white shorts, a cocktail with a paper umbrella in one hand and a stack of purple banknotes; behind him a strip of beach and sea in a thin gold frame, 193x579.
- **Style:** Caricature in a 3D-animation look: a huge snout and jaw, small eyes behind glasses, a soft round belly; comic and a little sleazy.
- **Rendering:** Painted, airbrushed volumes with warm red shadows and hard cut edges (soft edge 0.125); cloth carries a flat print, glass is a white reflection layer over the drink.
- **Colour:** Measured: orange #c56b0b 17% and #f7b713 11% (shirt, hat, gold), skin red #b34841 10%, dark red #60150a 10%, white #f7f9f3 9%, sky blue #3688e6 9%. Hues: 46% orange, 28% red, 13% blue.
- **Lighting:** From the top right on most parts (10 of the measured parts), with a deep red core shadow.
- **Ambience:** A winner on holiday: loud shirt, drink in hand, money to burn.
- **Materials:** Pink skin, straw, printed cotton, glass, gold, paper money, a leather bag full of coins (tile12WinBigBag).
- **Variants:** One figure in 41 parts; two backdrops (tile12Bg, beach; tile12BgJackpotSplash, a golden hoard); an extra right arm and a coin bag for the big-win pose (tile12ArmRWinBig, tile12WinBigBag); the same head appears small on the logo and in the 225 px help picture.
- **Motion:** TileBig12 is the game's second-largest rig (118 bones, 84 slots): intro 2 s, loop 2.67 s, onLand 0.42 s, win 2 s, collect 2.33 s, and three loops named loopWinBig, loopWinSuper and loopWinMega, so he also presents the big-win tiers (inference from the names; a big win was not reached). The frame has a 28-frame white highlight that runs around it (tile12FrameHighlight). No frame of the rig is drawn in this report (Spine 4.2.43).
- **Construction:** A cut-out rig: body, head in four pieces (head, jaw, back, ears), eyelids, brows, moustache halves, two arms in sleeve, forearm and hand, and props as their own parts (hat, glasses in two sides, cigar, drink in glass, liquid, patch and three straws). The patches (ArmLPatch, CigarPatch, DrinkGlassPatch) cover joints.
- **Notes:** Seen in play on the intro screen, as a pair with Ms. Piggy, and five times side by side on the FEATURE UNLOCKED card of level 1, whole and lit as shipped: reel-high, on his beach strip in the thin gold frame.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 57% · saturation 68% · contrast 62% · warm 79% / cool 17% · brighter towards: top-right (10), bottom-right (2), bottom-left (2)
- **Palette (measured):** #c56b0b orange 17%, #f7b713 orange 11%, #b34841 red 10%, #60150a dark red 10%, #f7f9f3 light green 9%, #3688e6 blue 9%

### Ms. Piggy: the Hold & Win Collector (full reel)

`ms-piggy-collector` · atlas · 28 parts · largest 314×538 · sheet `sheets/ms-piggy-collector.webp`

- **Role:** The female pig. By the rules, a golden Piggy Bank that breaks turns into a Ms. Piggy Collector that covers the whole reel under it in the Hold & Win and collects the coins' prizes. She is also the second figure of the intro.
- **Subject:** A pink sow as a glamorous traveller: long auburn hair with a yellow flower, heavy eyelashes, pearls in her ear, a silver sequin dress, a white clutch bag on a pearl chain, hooves for hands and feet; behind her a strip of night sea and beach, 110x345.
- **Style:** The partner caricature to Mr. Piggy: same snout and jaw, drawn as a pin-up.
- **Rendering:** Painted volumes with red shadow and hard edges (soft edge 0.086); the hair is one large shape with strand lines; the dress is a grey sparkle texture.
- **Colour:** Measured: dark red-brown #421311 29% (hair), skin red #b34534 20% and #e5806a 12%, silver #dacfce 10%, night blue #131a62 6%. Hues: 68% red, 16% blue.
- **Lighting:** From the top and right, softer than his; the backdrop is a night scene, so she reads lighter than her ground.
- **Ambience:** Evening glamour against his daytime leisure.
- **Materials:** Skin, hair, sequins, pearls, quilted leather.
- **Variants:** One figure in 28 parts; two sets of closed eyes; a 238x209 blurred ring (tile13Blur00), by its look the Jackpot Coin spinning (inference).
- **Motion:** TileBig13 is the largest rig in the game (144 bones, 104 slots): show 1.25 s, loop 2.67 s, loopEmpty, loopGs and loopWinMega 2.67 s, win 2 s, collect 2.33 s and a 2.25 s 'trasition'. TileBigEffects (22 bones) and TileBigSum (the collected amount, with multiplierShow and sumMultiply) sit on top. No frame of the rig is drawn in this report.
- **Construction:** A cut-out rig like his: body with dress as one 251x669 piece, hair in back and fringe, head in four pieces, two arms, lids and brows, bag and chain separate.
- **Notes:** Not seen in play beyond the intro: the Hold & Win did not come in this run's session. In the game's files the sprites named tile13 mix her parts with the Jackpot Coin's, which are read in their own unit.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 37% · saturation 59% · contrast 60% · warm 84% / cool 16% · brighter towards: right (3), top (3), top-right (3)
- **Palette (measured):** #421311 dark red 29%, #b34534 red 20%, #e5806a red 12%, #dacfce light red 10%, #131a62 dark blue 6%, #a69a99 grey 5%


## Logo and title

The game's own wordmark.

### Logo for the help pages

`help-logo` · atlas · 1 parts · largest 768×100 · sheet `sheets/help-logo.webp`

- **Role:** The same title at 768x100, served by the provider's asset service for the help pages and lobby.
- **Subject:** The logo strip as in the game: BREAK the DIAMOND PIGGY between the two pigs' heads.
- **Style:** Identical to the game's logo.
- **Rendering:** A smaller export of the same picture.
- **Colour:** Measured: brown #8c5927 28%, ochre #d0ae5e 15%, gold #e6b52d 9%, pink-red #e17a6a 8%, blue #109ff7 5%, green #77ba1c 3%.
- **Lighting:** As the logo.
- **Ambience:** As the logo.
- **Materials:** As the logo.
- **Variants:** One picture.
- **Motion:** None.
- **Construction:** A flat export kept apart from the game's atlas so the shell can show it without loading the game.
- **Notes:** Compared by eye with the game's logo, not pixel for pixel.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 50% · saturation 67% · contrast 61% · warm 76% / cool 20% · brighter towards: top-right (1)
- **Palette (measured):** #8c5927 brown 28%, #d0ae5e orange 15%, #e6b52d orange 9%, #e17a6a red 8%, #545e14 brown 6%, #9e864e orange 5%

### Logo: Break the Diamond Piggy

`logo` · atlas · 1 parts · largest 924×109 · sheet `sheets/logo.webp`

- **Role:** The game's title, a single 924x109 picture in the game atlas. It shows on the intro screen; in the landscape base game no logo was on screen (the Piggy Progress and the piggy banks take the top).
- **Subject:** A long gold-framed strip on a dark purple quilted ground: BREAK in green, 'the' small in yellow, DIAMOND in faceted ice blue, PIGGY in pink, with Ms. Piggy's head at the left end and Mr. Piggy's at the right.
- **Style:** Cartoon display lettering, one colour and one material per word, in a ribbon format made for the top edge of a screen.
- **Rendering:** Fat rounded capitals with a dark outline and a gold rim; DIAMOND carries crystal facets, the other words a soft gradient. The two heads are the characters' own painted heads at small size.
- **Colour:** Measured: brown #895b28 28% and ochre #ab8c4d 20% (frame and outlines), pink-red #de8673 9%, gold #e8b82e 6%, green #6a9719 6%, blue #17a0f2 5%, purple #3c1974 4%.
- **Lighting:** Top light on the letters with a bright upper band.
- **Ambience:** Playful and loud; the title is a row of toys.
- **Materials:** Gold, enamel, cut crystal, pink skin.
- **Variants:** One picture; the Logo rig has skins landscape and portrait with show, idle and hide.
- **Motion:** The Logo rig's animations have no length (0 s): the logo is placed, not animated.
- **Construction:** A flattened picture, not layered letters.
- **Notes:** Each word's colour repeats an element of the game: green and gold for money, ice blue for the Diamond Piggy, pink for the pigs.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 49% · saturation 64% · contrast 56% · warm 72% / cool 22%
- **Palette (measured):** #895b28 brown 28%, #ab8c4d orange 20%, #de8673 red 9%, #e8b82e orange 6%, #6a9719 green 6%, #17a0f2 blue 5%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature captions (en-GB)

`feature-lettering` · atlas · 11 parts · largest 1006×231 · sheet `sheets/feature-lettering.webp`

- **Role:** The localised captions of the splashes and labels: the four unlock messages, FEATURE UNLOCKED, BONUS GAME twice, the Hold & Win and Smash & Win hints, and MORE FOR THE GRAND JACKPOT.
- **Subject:** Heavy rounded capitals in yellow with a dark violet outline: PIGGY COLLECTORS CAN LAND ON THE REELS; X2 MULTIPLIER ON ALL JACKPOTS; PIGGY BANK MULTIPLIERS; SMASH & WIN BONUS; EACH BROKEN PIGGY BANK AWARDS A COLLECTOR; TAP FOR CASH PRIZES; and, in black slab capitals with a gold rim like the jackpot names, MORE FOR THE GRAND JACKPOT and one BONUS GAME.
- **Style:** Two voices: a friendly cartoon caption face for instructions and the jackpot face for jackpot matters.
- **Rendering:** Flat yellow faces with a slight gradient and a thick dark outline; the jackpot-style lines have the gold rim and black face.
- **Colour:** Measured: yellow #f8d10a 27%, near-black violet #190b23 21%, brown #603f2a 15%, gold #ddc064 10% and #9d7124 9%.
- **Lighting:** None beyond the gradient.
- **Ambience:** Clear instructions, no rhyme or joke.
- **Materials:** Print.
- **Variants:** 11 pictures, most on a 1006 px wide canvas; landscape and portrait versions of the jackpot anticipation label.
- **Motion:** Placed by the splash rigs (HoldAndWinSplash show 1 s, PickerBonusSplash show 0.95 s, JackpotAnticipationSplash 4.33 s, PickerBonusHintLabel loop 0.83 s).
- **Construction:** Text is shipped as pictures per language, so every caption is redrawn for each market.
- **Notes:** The captions state the game's structure in the art itself: four unlocks, a bonus where a broken bank awards a Collector, and a tap bonus.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 46% · saturation 75% · contrast 80% · warm 82% / cool 17% · brighter towards: top (1)
- **Palette (measured):** #f8d10a gold 27%, #190b23 black 21%, #603f2a brown 15%, #ddc064 gold 10%, #9d7124 brown 9%, #c79a17 orange 4%

### Win lettering and the big-win window

`win-tiers` · atlas · 13 parts · largest 1006×221 · sheet `sheets/win-tiers.webp`

- **Role:** The three win tiers (BIG WIN, SUPER WIN, MEGA WIN), TOTAL WIN, the win bar with its TAP label, and the props of the big-win scene: an arched window on the sea, its gold frame, a scrolled gold ornament, coin heaps and a diamond.
- **Subject:** Flared display capitals with a two-colour face: BIG WIN in blue and cyan, SUPER WIN in magenta and pink, MEGA WIN in yellow and orange, TOTAL WIN in violet; an orange gold-rimmed bar; a 343x374 arched view of sky, sea and a palm leaf.
- **Style:** Game-show lettering, flatter and more graphic than the painted pigs and props.
- **Rendering:** Each word has a hard horizon between a light upper and a darker lower tone, a thin light rim and a dark outline. The window is painted like the backdrops.
- **Colour:** Measured: orange #ed9a0d 22% (bar, coins), dark purple #381846 9% (outlines), gold #f6d03a 8%, cyan #12bcfb 4%, blue #6ec2f7 4%, magenta #fc0bc0 4%.
- **Lighting:** Top light on the gold; the lettering is self-coloured.
- **Ambience:** A prize show on deck.
- **Materials:** Enamel lettering, gold, glass and sky.
- **Variants:** Three tier words (655, 902 and 851 px wide), TOTAL WIN and TAP as localised en-GB pictures, one bar, one window with half a frame (winBigWindowFrame, 120x446, mirrored by inference), two coin groups, one diamond.
- **Motion:** WinBig (37 bones, 53 slots; skins label1 to label3): labelShow 1.25 s, sumShow 0.58 s, hide 0.58 s. WinTotal (36 bones): show 1.25 s, showGrand 1.43 s. WinBar: sumShow 0.33 s, sumUpgrade 0.33 s. Mr. Piggy's rig has loops named for the three tiers, so he appears in the window (inference). Seen in play: only the ordinary win, counted in large black and gold numerals over a white-gold flash with coins flying.
- **Construction:** A small stage built for the big win: window, frame halves, ornament, coins and the character rig, with the tier word swapped by skin.
- **Notes:** No big win was reached in this run; the tier scene is read from the files.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 49% · saturation 75% · contrast 64% · warm 63% / cool 32% · brighter towards: top (3), top-right (2), top-left (1)
- **Palette (measured):** #ed9a0d orange 22%, #381846 dark purple 9%, #f6d03a gold 8%, #12bcfb cyan 4%, #6ec2f7 blue 4%, #100613 black 4%

### Feature splash card and arrow

`feature-splash` · atlas · 2 parts · largest 407×497 · sheet `sheets/feature-splash.webp`

- **Role:** The card shown when a Piggy Progress level unlocks (FEATURE UNLOCKED, by the lettering files) and a green down arrow.
- **Subject:** A 407x497 golden panel with a soft mottled face and a darker edge; a fat glossy green arrow pointing down (196x184).
- **Style:** Plain carriers for lettering and for a small picture of the feature.
- **Rendering:** The panel is a soft gradient with a hard edge; the arrow has a bevel and a white gloss.
- **Colour:** Measured: orange-gold #fbca4a 67%, yellow #faf850 17%, green #55d532 5%.
- **Lighting:** Even; a gloss on the arrow from the top left.
- **Ambience:** A prize card held up to the player.
- **Materials:** Gold card, green enamel.
- **Variants:** One panel, one arrow; FeatureSplash has skins feature0 to feature3, one per level.
- **Motion:** FeatureSplash (75 bones, 77 slots): show 5 s, a long, staged reveal. Seen in play: a white flash, then the card with five Mr. Piggy figures, then coins bursting from it.
- **Construction:** Two sprites of its own; the rest is borrowed through the rig.
- **Notes:** Seen in play at the first unlock: FEATURE UNLOCKED across the top, the golden card over a dimmed game with five reel-high Mr. Piggy figures side by side and coins flying out, and PIGGY COLLECTORS CAN LAND ON THE REELS below. fsSpecialArrow's use was not identified.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 78% · saturation 72% · contrast 41% · warm 92% / cool 4%
- **Palette (measured):** #fbca4a orange 67%, #faf850 gold 17%, #55d532 green 5%


## Effects

Frame sequences, glows, particles and transitions.

### Bursts, sparks, dust and the reel anticipation

`bursts-and-fireworks` · atlas · 87 parts · largest 526×338 · sheet `sheets/bursts-and-fireworks.webp`

- **Role:** White effect frames the game tints: an explosion, a spark explosion, fireworks, a dust cloud, flying debris, a radial blur, and the glow that runs along a reel's edge in anticipation.
- **Subject:** A white pop that opens into a ring of sparks; a small star burst; twinkling firework points; a cloud; chips of debris; a strip of rising glitter (192x40) and a yellow light bar.
- **Style:** Generic light effects, drawn soft.
- **Rendering:** White on transparency, soft (soft edge 0.909).
- **Colour:** Measured: white #ffffff 99%; one yellow strip (anticipationLightT). Colour comes from tinting in the game.
- **Lighting:** They are the light.
- **Ambience:** Impact and sparkle.
- **Materials:** Light, dust.
- **Variants:** Four sequences: anticipationEffect 36 frames, fireworkEffects 25, sparksExplosionEffect 12, explosionEffect 10; four single sprites.
- **Motion:** The frame sequences are the motion: 83 frames in all. By their names the explosion and debris serve the breaking banks and the Smash & Win (inference).
- **Construction:** Drawn once in white and reused wherever something breaks, lands or wins.
- **Notes:** The same kind of white effect set as in the other Octoplay runs; not compared pixel for pixel.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 1% · contrast 1% · warm 1% / cool 0%
- **Palette (measured):** #ffffff white 99%

### Rays, halos, glints and particles

`light-and-particles` · atlas · 24 parts · largest 562×567 · sheet `sheets/light-and-particles.webp`

- **Role:** The single white light sprites behind symbols, splashes and wins: ray bursts, a halo, a ring wave, an ornamental flower glow, star fields, glints and three small coloured dots.
- **Subject:** Circular ray bursts in three sizes (up to 562x567), speed lines, a round glow, a ring with a corona (magicHalo), a thin ring (whiteWave), a five-petalled ornamental glow with its sparkle cloud, a cone of light, a vertical ray, cross glints, and yellow and blue 23 px particles.
- **Style:** Stock light shapes in white.
- **Rendering:** Soft throughout (soft edge 0.954).
- **Colour:** Measured: white #ffffff 98%. The only colour is in the yellow and blue particle dots.
- **Lighting:** They are the light.
- **Ambience:** Shine and glamour on demand.
- **Materials:** Light.
- **Variants:** 24 single sprites, no sequences.
- **Motion:** Rotated, scaled and faded by the rigs (for example PickerBonusEffects loopLightGlow 4 s, ProgressCollectorMultiplierEffect show 1.92 s). Seen in play: a white-gold flash across the board behind the win amount.
- **Construction:** White sprites tinted and blended by the engine; no drawn frames.
- **Notes:** Several names (circularWhiteRays2, glowSquare, starsEffect) also appear in other Octoplay runs; not compared pixel for pixel.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff white 98%

### Flying money: banknotes and diamonds

`coins-diamonds-and-bills` · atlas · 90 parts · largest 175×150 · sheet `sheets/coins-diamonds-and-bills.webp`

- **Role:** The particles of the celebrations and of the throw towards the Diamond Piggy Bank: a tumbling banknote and a turning diamond in blue and in pink.
- **Subject:** A violet banknote with a white border and round emblem, curling as it falls; a brilliant-cut gem seen turning, in blue and in magenta.
- **Style:** Flat cartoon money and clean faceted gems.
- **Rendering:** The note is flat colour with one fold shadow; the gems are hard facets with a white star glint on some frames.
- **Colour:** Measured: light violet #cdbdf9 26%, violet #854eb8 26%, blue #1f7ec8 14%, magenta #c91fbc 13%, light blue #61abf3 8%.
- **Lighting:** Top light on the gems (12 of the measured frames).
- **Ambience:** Money in the air.
- **Materials:** Paper, cut stone.
- **Variants:** Three 30-frame sequences: billParticle 175x150, blueDiamond and pinkDiamond 100x100.
- **Motion:** Each sequence is one full tumble or turn in 30 drawn (or pre-rendered, by their evenness: inference) frames, looped in 1 s by ParticleDollarBill, ParticleDiamond1 and ParticleDiamond3. Gold coins fly the same way from the coinPiggy sequence.
- **Construction:** 90 frames for three particles: the turning is in the frames, the flight path in the engine.
- **Notes:** The banknotes are violet, not green, which keeps green for the Major jackpot and the J.
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged · brightness 53% · saturation 56% · contrast 48% · warm 14% / cool 71% · brighter towards: top (12), top-right (5), right (2)
- **Palette (measured):** #cdbdf9 light purple 26%, #854eb8 purple 26%, #1f7ec8 blue 14%, #c91fbc magenta 13%, #61abf3 blue 8%, #f480e6 magenta 5%


## Game interface

Buttons, counters and panels drawn for this game.

### Jackpot plates: Mini to Grand

`jackpot-panel` · atlas · 23 parts · largest 1114×193 · sheet `sheets/jackpot-panel.webp`

- **Role:** The five jackpot plates stacked at the left of the board in the base game (Grand 2500x at the top, then Maxi, Major, Minor, Mini), their names, the larger frames and names used when one is won, a rainbow plate and a x2 multiplier disc.
- **Subject:** Shield-like hexagonal plates with a gold frame and a small gold crest on top, filled gold (Grand), red (Maxi), green (Major), violet-blue (Minor) and magenta (Mini); the names in black slab capitals with a gold rim; values in the provider's black and gold numerals.
- **Style:** Casino signage as jewellery: enamel fields in gold settings, matching the reel frame.
- **Rendering:** A faint woven pattern on each field, a bevelled frame with top highlights; hard-edged (soft edge 0.058).
- **Colour:** Measured: brown #6d3114 19% and gold #e1af28 15% (frames), black #0d0806 9% (lettering), pale gold #f1de5d 8%, green #62c109 6%, red #d62516 6%, magenta #ad14cc 6%, violet-blue #6b46de 5%.
- **Lighting:** Top light (9 of the measured parts).
- **Ambience:** The prizes on display, as loud as the symbols.
- **Materials:** Gold and coloured enamel; black lacquer letters.
- **Variants:** Five plates (484x203, the Grand 487x203), five names in two sizes (plate and win), five win frames (347 to 370 px wide, cut as the left half), bgJackpotPlate with a rainbow field (722x224) and bgJackpotTxt, the word JACKPOT at 1114x193, and a 66 px disc (jackpotMultiplierPlate) for the x2 that Piggy Progress level 2 puts on all jackpots (the rules).
- **Motion:** Jackpot (15 bones, skins jackpot0 to jackpot4): idle 1.33 s, win 0.82 s, winLoop 1.5 s, reset 0.5 s. JackpotMultiplier shows in 0.5 s. WinJackpot (34 bones, 62 slots) presents a won jackpot with show, update, multiply (1.17 s) and collect. In play the plates sat still.
- **Construction:** One plate shape recoloured four times plus a wider Grand; names are separate pictures so plate and name can move apart; win frames are half pictures to be mirrored (inference from their cut edge).
- **Notes:** The plate colours repeat on the Jackpot Coin's rings (green Major, red Maxi, magenta Mini, violet Minor), so a coin and its plate match without a legend.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 42% · saturation 74% · contrast 70% · warm 77% / cool 16% · brighter towards: top (9), right (1), top-left (1)
- **Palette (measured):** #6d3114 brown 19%, #e1af28 orange 15%, #0d0806 black 9%, #f1de5d gold 8%, #62c109 green 6%, #d62516 red 6%

### Piggy Progress: the pocket-watch counter

`piggy-progress` · atlas · 32 parts · largest 629×67 · sheet `sheets/piggy-progress.webp`

- **Role:** The counter above the reels that counts down the normal-game spins to the next of four permanent unlocks (10, 25, 50 and 75 spins, the rules), and the portrait layout's spin counter base.
- **Subject:** A gold alarm clock with two bells and a pig's snout on its dial, at the left end of a turquoise bar in a bronze frame; the number of spins left stands on the bar in cream numerals with a wine outline. Also a purple bar labelled SPINS with three cells (counterPortraitBase, 629x67).
- **Style:** A small prop in the game's gold, readable at a glance.
- **Rendering:** The clock is a polished gold volume with a cream dial; the bar is a flat glowing gradient. White flash shapes (a starburst, lightning marks, a clock-shaped glow) bring the unit's soft edge to 0.296.
- **Colour:** Measured: white #fefefe 37% (flash shapes), dark purple #341582 17%, bronze #91551c 16%, cyan #12bdc7 9%, gold #dda010 3%.
- **Lighting:** Top-left on the clock; the bar is self-lit.
- **Ambience:** A promise of more to come; the alarm rings when a level unlocks.
- **Materials:** Gold, enamel, a lit glass bar.
- **Variants:** Clock body with separate hands, bells and snout; plate, end cap and highlight; skins landscape and portrait.
- **Motion:** FeatureProgress (26 bones): loop 1.67 s, decrease 0.33 s on each spin, unlock 1.5 s, an anticipation track of 0.5 s. A 16-frame white highlight crosses the bar (featureProgressPlateHighlight). The ringing uses the starburst and lightning marks (featureProgressClockRinging, RingingMark1 and 2). Seen in play: the number falls by one per spin, from 10.
- **Construction:** A rigged clock of nine small parts on a two-piece bar; all flashes are white sprites.
- **Notes:** The run's session saw the count go from 10 to 0 and the first unlock (Mr. Piggy Collectors) on the next spin.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 61% · saturation 48% · contrast 31% · warm 32% / cool 32% · brighter towards: right (2), top-left (1)
- **Palette (measured):** #fefefe white 37%, #341582 dark purple 17%, #91551c brown 16%, #12bdc7 cyan 9%, #5c3032 dark red 5%, #e6d9bd light orange 3%

### The five golden Piggy Banks above the reels

`golden-piggy-banks` · atlas · 65 parts · largest 393×330 · sheet `sheets/golden-piggy-banks.webp`

- **Role:** One golden piggy bank sits above each reel. A Golden Coin throws a coin at the bank over its reel; each coin may break the bank and start the Hold & Win, and, by the rules, the cracks drawn on a bank are only for show.
- **Subject:** A fat gold piggy bank with a coin slot, in six states of damage from whole to badly cracked, drawn three times over: plain, with small round purple glasses, and with glasses and a wider grin. Around it: shards, a white pig-shaped glow, a 30-frame spinning gold coin with a snout, snout-shaped tokens in pink, red and blue, coin heaps, blue diamonds and a purple top hat.
- **Style:** The mascot as an object: rounder and friendlier than the two pigs, closer to a toy.
- **Rendering:** Polished gold with a soft orange core shadow and a white top glint, hard edges (soft edge 0.078); cracks are dark lines with a pink glow showing inside at the last stages.
- **Colour:** Measured: gold #e8b50d 36%, brown-orange #a95b07 31%, pale gold #f6e066 16%, dark brown #682505 4%. 95% warm, saturation 0.827.
- **Lighting:** From the top left (19 of the measured parts) and top.
- **Ambience:** Anticipation: every coin might be the one.
- **Materials:** Gold, purple glass lenses, velvet (the hat).
- **Variants:** 18 bank pictures: three series (pseudoProgress, pseudoProgress2, pseudoProgress3) of six stages each, growing from 231x207 to 393x330 as the damage grows. By inference the second and third series are the bank with a x2 and a x3 Piggy Multiplier (the rules name those two steps; the help picture shows banks with glasses beside x2 and x3). Six shards; three snout tokens.
- **Motion:** ProgressCollector (39 bones, 44 slots; skins multiplier1 to 3 by progress0 to 5): loop 1.33 s, progressUpdate 0.67 s, activate 1.33 s, reform 1 s, multiplierUpdate 1 s. coinPiggy is a 30-frame turn of the snout coin. Seen in play: coins and snout tokens fly up from the reels to the banks, and a bank hit by a coin jolts.
- **Construction:** Damage is told with whole redrawn pictures per stage, swapped by skin, rather than with crack overlays: 18 paintings of one object. The break itself uses the six shard sprites and white burst frames.
- **Notes:** A large share of the game's hand-painted work goes into an indicator that, as the rules state, does not change the odds: the art buys anticipation.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 62% · saturation 83% · contrast 64% · warm 95% / cool 2% · brighter towards: top-left (19), top (10), top-right (3)
- **Palette (measured):** #e8b50d gold 36%, #a95b07 brown 31%, #f6e066 gold 16%, #682505 brown 4%, #f5fcec light green 4%, #fbf2ae light gold 2%


## Typography

Embedded fonts and lettering.

### Numeral fonts: Ultra in black and gold, and in cream

`font-ultra` · atlas · 32 parts · largest 182×234 · sheet `sheets/font-ultra.webp`

- **Role:** The provider's bitmap numerals: UltraBlack for the values on Golden Coins, the jackpot values and the win count-up; UltraActiveBig for the Piggy Progress counter and small amounts.
- **Subject:** Digits, x, plus, slash, comma, full stop, a question mark and a flower-like asterisk in a very fat slab serif.
- **Style:** Circus-poster numerals, heavier than any lettering in the game's own art.
- **Rendering:** UltraBlack: a black face, a bright gold inner rim and a red-brown drop edge. UltraActiveBig: a glowing cream face with a wine-red outline. Hard-edged, contrast 0.949.
- **Colour:** Measured: black #0c0302 44%, cream #fcf3b8 21%, dark red #510e0e 9%, gold #e7be46 8% and #f2e57b 7%, red #a3141a 4%.
- **Lighting:** Top light on the gold rim.
- **Ambience:** Bold and legible over any background.
- **Materials:** Black enamel in gold; lit cream.
- **Variants:** Two fonts: 17 glyphs up to 182x234 and 15 glyphs up to 105x114 kept by the reader. 95 further glyphs that the font descriptors place on pages this game did not load were cut wrongly and removed.
- **Motion:** None of their own; the win amount scales up as it counts (seen in play: 1.12 rising to 10.00 across the board).
- **Construction:** Bitmap fonts from the provider's shared font service (fonts-v2), not from this game's atlas; other Octoplay games use the same service.
- **Notes:** Black numerals on a gold coin and on a cream board are this game's choice; the earlier Octoplay runs used cream and gold versions of the same face.
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged, strong highlights · brightness 38% · saturation 57% · contrast 95% · warm 99% / cool 0% · brighter towards: top (10), top-left (2), top-right (1)
- **Palette (measured):** #0c0302 black 44%, #fcf3b8 light gold 21%, #510e0e dark red 9%, #e7be46 orange 8%, #f2e57b gold 7%, #a3141a red 4%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts
- `shared-tile0`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 886 components cut from 39 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
