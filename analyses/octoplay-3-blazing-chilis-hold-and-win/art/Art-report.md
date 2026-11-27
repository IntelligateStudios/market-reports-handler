# 3 Blazing Chilis Hold And Win: art report

octoplay · run `2026-11-27-0953-octoplay-3-blazing-chilis-hold-and-win` · captured 2026-11-27

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/3-blazing-chilis-hold-and-win

**Extracted:** 433 named components from 41 textures in 41 atlases; 37 Spine skeletons; 12 frame sequences (204 frames); 3 fonts. Grouped into 24 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A sunny Mexican market stall run by one beaming chef, where the whole game is a grill: three chilis in traffic-light colours sit on three plates above the reels, catch fire to start the Hold & Win, and turn the day street into a lantern-lit fiesta night.

**Style.** Family animated-feature illustration throughout: a storybook street, a soft caricature chef, plump glossy food symbols and comic poster lettering. Unlike many games of this kind there is no gap between a realistic world and stylised game pieces; background, character and symbols share one rounded, friendly manner, the symbols only more saturated and glossier. Inference: the two street pictures and the chef have the look of an image model's work finished by hand (the night street repeats the day street object for object); frame, boards, lettering and effects are drawn in the usual production way.

**Rendering.** Backgrounds: painted gradients with brush texture and no outlines. Chef: smooth 3D-like shading with a warm rim. Symbols: strong gradients, long white speculars, a dark outline, each on the dark plank board. Lettering: two-tone gradients with a top bevel, dark outline and lower extrusion. Fire: cel-painted licks in two or three tones with a soft glow. Smoke and light: white sprites tinted by the engine.

**Colour.** Measured over the game's art: dusty wine #60373f 12%, dark wine #371819 12%, terracotta #b45832 11%, sand #ca996b 10%, near-white #f5f7f5 9%, mauve #7e5966 8%, pale sand #eac596 8%, gold #fbd945 2%. A warm palette of cream, terracotta and red with green as the foil. Colour carries the rules: green, yellow and red for the three chilis, in value order (1x, 2x, 5x the stake), repeated on their words, their effect marks and the logo; red and gold, orange, cyan and purple for GRAND, MAJOR, MINOR and MINI; cyan, orange and red for BIG, SUPER and MEGA WIN; one hue per letter symbol. The bonus keeps every game piece and changes the world to violet and deep blue with orange lights.

**Lighting.** Base game: high sun from the upper right, soft short shadows. Bonus: moonlight with warm pools from windows, a lantern and strings of bulbs. Game pieces carry their own top light and do not take the scene's; fire lights itself and gives the chilis a rim.

**Ambience.** A holiday lunch at a street grill: sunny, generous, a little comic (the deadpan hen, the chef who breathes fire and coins when the chilis ignite). The bonus is the same street at fiesta time, hotter and more intimate.

**Shape language.** Round and plump everywhere: curved chilis, barrel cacti, a domed sombrero, a round-faced chef, rounded slab letters. The chili silhouette is the game's mark and is reused as a shape: the logo sign and win plate are a chili-shaped wooden board, a glow has a chili-shaped hole, the coin is embossed with a chili. Zigzag bands (poncho, sombrero, letters) are the second repeated motif.

**Materials.** Stucco, terracotta and clay tile; bleached and red-painted wood, rope; steel grill plates, cold and red-hot; waxy pepper skin, straw, feathers, glass; flame, smoke, gold coin.

**Typography and lettering.** Drawn words in rounded comic capitals with a double outline for the logo, the jackpots, the win tiers, the chili words (SPICY, HOT, BURNS) and the headings BONUS GAME, JACKPOT, TOTAL WIN and CONGRATS!, each in its rule colour. Rules on the bonus splash are a condensed italic sans in white with a red edge. Numbers come from three bitmap fonts of the provider's shared store: Tsiyugunsini in gold with a wine-red edge (jackpot values, the value on every Chili symbol, win amounts), Ultra in black with a gold rim (the +1 and x2 effect marks), Contrail One in white (the jackpot counters); which font sets which number is an inference from comparing glyphs with the screens. The shell's Poppins sets the help, buttons and balance line.

**Motion.** All character and layout motion is Spine: 37 skeletons in one bundle file (35 in 4.2.43, one in 4.1.24, one in 4.3.26), with 12 frame sequences (204 frames) that are almost all fire and smoke: a 31-frame fire burst, an 18-frame flame behind each Chili symbol, flame splashes, fire lines and streaks, a 28-frame cloud, puffs, an 18-frame smoke wisp, sparkles and a 10-frame coin. Seen in play: flames behind the three chilis on the intro; win lines as a thin gold line; a win amount on the wooden pepper plate with coins; the grill chilis lifting and flaring as their symbols land; on the bonus trigger all three ignite, the chef claps his hands to his mouth and blows fire and coins, the words turn into +1, x2 and an up-arrow; the Bonus Game splash on a tall red board; a red-orange fire screen with the grill and the three chilis as the change of scene; a golden flash with the chef giving two thumbs up as the game opens; then, in the bonus, the night street, a row of red chilis added on top inside a gold outline, values growing as +1 and x2 marks fly down, and empty positions burning as a reel nears full. When a reel fills, its chilis fly up to the wooden pepper plate, which counts the win; the MINI jackpot came with the gold JACKPOT word, the tier word large over the reels, coins and streamers; TOTAL WIN closes the bonus on the tall red board. Read from the files only: BIG, SUPER and MEGA WIN and the three higher jackpots. No skeleton frame is shown in this report, because the project's renderer cannot draw Spine 4; assembled and motion pictures are absent for that reason only.

**Variants and themes.** Two scenes on one composition (day and night). Three chilis on one rig with three skins, in symbol, grill and splash sizes. Three collectors on one rig with three skins. Four jackpot boards on one plank. Three win tiers on one lettering. Two reel backings (three rows, and four with the bonus row) and a frame cut in mirrored strips so the board can grow. One chef with three pairs of hands. One wooden pepper board used as logo sign, bonus counter panel and win plate.

**How it is built.** Two 4096 px atlas pages hold the whole game: each carries one 2750x2582 scene, and the rest is some 340 small sprites, more than half of them fire and smoke frames. Twelve word pictures are localised files (en-GB loaded). The chef is a bust of 19 parts with one painted face; the Wild hen is 12 parts; every other symbol is one to three sprites on a shared rig with skins. Effects are reused across skeletons by name (the symbol flame is also the grill flame, tinted red for a second version; the Wild's smoke is also the grill's). White effect sprites are tinted in the engine. The symbol pictures for the help, the flat logo, the numeral fonts, the Buy Feature cards, the controls and Poppins come from the provider's shared store outside the game bundle. The artists' white cell guide (tileGuide) and green container guide ship in the atlas as anchors.

**Consistency.** High. One manner runs from street to chef to symbols, and the three chili colours tie logo, symbols, grill, words, effect marks and poncho stripes together. The seams are small: the black-and-gold slab numerals of the effect marks and the condensed italic rule text are stock type beside hand-drawn comic capitals, and the Buy Feature cards are denser and hotter than anything in play.

**What to take from it.** (1) Turn the mechanic into a place in the scene. The three persistent bonus modifiers are three chilis on a grill above the reels, each with a plate that heats, a word and a dial; the player reads the state of the game from a picture of cooking, not from meters. (2) Use an order people already know for value. Green, yellow, red is 1x, 2x, 5x and nobody needs it explained; the same three colours then pay for the logo, the words, the effect marks and the costume. (3) One host character, cut cheaply, gives a game a face. The chef is a bust with one painted face, separate brows, eyelids and moustache, and three pairs of forearms; his big moment (hands to mouth, fire and coins) is hand swaps and particles, not a new drawing. (4) Keep background, character and symbols in one style when the theme is warm and comic. Here nothing is photoreal, so no dark board trick is needed to separate symbols from the world: saturation and gloss do it. (5) Make the bonus by changing the time of day. The night street is the same composition relit, with every game piece unchanged; it reads as a new place for the cost of one picture. (6) Spend the frame budget where the theme lives. More than half of the sprites are fire and smoke frames, painted in a cel style that matches the illustration, and each loop is reused by several rigs and tinted for variants. (7) Reuse one themed silhouette as a container. The chili-shaped wooden board is the logo sign, the bonus panel and the win plate; the same shape is cut into a glow and embossed on the coin. (8) Draw the short words, set the numbers. SPICY, HOT, BURNS, the jackpots and win tiers are drawn pictures in the rule colour; every amount is a bitmap font, so one pepper carries any value and the +1 and x2 marks can fly as text. (9) Plan localisation of drawn text early: twelve word pictures ship per language here, while the chili words are English inside the art and are not localised. (10) For AI-assisted art: the two street scenes and a host bust are where an image model gives most (a relit copy of one composition is exactly its strength); the symbols must then be pushed to the same manner at higher gloss, and the grill states, the frame in strips, the lettering and the effect loops are production work to plan as parts and frames from the start.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 49% · saturation 52% · contrast 50% · warm 69% / cool 21% · brighter towards: top (46), top-left (18), right (12)

Palette: #60373f dark red 13%, #371819 dark red 12%, #b45832 orange 12%, #ca996b orange 10%, #f5f7f5 light green 9%, #7e5966 red 9%, #eac596 light orange 8%, #fbd945 gold 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 44% | 51% | 52% | 70% / 21% | #784f5d red 20%, #cfa274 orange 19%, #42272d dark red 18% |
| Reel board | 2 | 48% | 68% | 36% | 80% / 11% | #34090b dark red 26%, #f4c6a3 light orange 25%, #b34b2d red 7% |
| Symbols | 5 | 60% | 75% | 50% | 86% / 8% | #f48e0d orange 26%, #fccf50 orange 22%, #e7dbc3 light orange 11% |
| Characters | 1 | 41% | 55% | 54% | 83% / 16% | #a65d3b orange 32%, #291a2a dark magenta 21%, #ecb291 orange 15% |
| Logo and title | 2 | 50% | 79% | 68% | 60% / 20% | #21611c dark green 20%, #fbca2e gold 16%, #35b126 green 13% |
| Win celebrations and banners | 2 | 45% | 72% | 59% | 88% / 6% | #4b180d dark red 30%, #ea2e19 red 11%, #a8210f red 10% |
| Effects | 4 | 85% | 21% | 26% | 26% / 51% | #f8f9f7 light green 66%, #fc640a orange 11%, #c0d5dd light cyan 5% |
| Game interface | 3 | 45% | 65% | 63% | 80% / 15% | #ad3118 red 17%, #ebae82 orange 16%, #372e2c grey 10% |
| Typography | 3 | 44% | 52% | 96% | 88% / 0% | #0c0302 black 39%, #fefcee light gold 16%, #f9f0a0 light gold 11% |
| Provider interface (shared) | 1 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backgrounds: the market street by day and by night

`backgrounds` · atlas · 2 parts · largest 2750×2582 · sheet `sheets/backgrounds.webp`

- **Role:** The scene behind everything: bgNormal for the base game and bgSpecial for the Hold & Win bonus (the two skins of the Backgrounds skeleton, "normal" and "special").
- **Subject:** A narrow Mexican village street looking downhill: stucco houses with red tile roofs and arched windows, a striped awning with hanging dried chilis, strings of flags, a yellow market umbrella over tables with checked cloths and vegetables, a tomato bush, terracotta planters, palms, two cloth bags with flowers, and a pavement of large coloured stone slabs in the foreground. The night picture is the same street under a full moon and stars, with lit windows, a lantern and light bulbs along the flag strings.
- **Style:** Storybook illustration with the finish of an animated feature: rounded, slightly leaning buildings, simplified foliage, everything clean and friendly. Inference: both pictures have the look of an image model's picture finished by hand; the night scene repeats the day composition object for object.
- **Rendering:** Soft painted gradients with visible brush texture on walls and stones, no outlines, mild depth haze down the street. Measured hard-edged (soft-edge share 0.0), mid-tone, medium contrast.
- **Colour:** Measured over both: dusty mauve #784f5d 20%, sand #cfa274 19%, dark wine #42272d 18%, terracotta #c66133 13%, brick red #893729 5%, sky blue #a7d8eb 4%, night blue #162362 3%. Day is cream, terracotta and green under a pale blue sky; night turns the walls violet and the sky deep blue and keeps the warm notes as lights.
- **Lighting:** Day: high sun from the upper right (measured: top-right), short soft shadows. Night: cool moonlight from above with warm pools from windows, the lantern, the doorway at the right and the bulbs, so the pavement glows orange down the middle.
- **Ambience:** A small-town food market on a festival day, sunny and unhurried; at night the same street becomes a fiesta, warmer and more intimate.
- **Materials:** Stucco, terracotta, clay roof tiles, painted wood, cloth, leaves, worn stone.
- **Variants:** Two full pictures of 2750x2582 px, one composition in two times of day. They take most of the two 4096 px atlas pages.
- **Motion:** The pictures do not move. The BackgroundEffects skeleton lays glows over them (six "lightsGlow" slots, two gradients and two white glows, with idle and loop animations of 4 to 8 s and the same "normal" and "special" skins); read from the file, these are light pulses, which fit the bulbs and windows (inference).
- **Construction:** One still per scene, far larger than the 1280x720 view, so the game can crop and shift it; the reel cabinet covers the middle. No separate foreground layers: the Foregrounds skeleton holds only a black fade square.
- **Notes:** The lower middle of both pictures is kept empty of detail (plain slabs), where the reels and controls sit.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 44% · saturation 51% · contrast 52% · warm 70% / cool 21% · brighter towards: top-right (1)
- **Palette (measured):** #784f5d red 20%, #cfa274 orange 19%, #42272d dark red 18%, #c66133 orange 13%, #893729 red 5%, #a7d8eb light cyan 4%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Jackpot boards: GRAND, MAJOR, MINOR, MINI

`jackpot-ladder` · atlas · 15 parts · largest 413×292 · sheet `sheets/jackpot-ladder.webp`

- **Role:** The four fixed jackpots shown as a stack of boards at the upper left of the board in every screen, and their large versions for a jackpot win (the Jackpot and WinJackpot skeletons, skins jackpot0 to jackpot3).
- **Subject:** Four pale wooden planks (643x160; the MINI plate 571x142), each with an edge line in its tier colour, a drawn word (GRAND red on a gold oval coin 413x292, MAJOR orange, MINOR cyan, MINI purple), a white outline shape used to flash a plate, and four 57 px round counters in red, orange, purple and cyan.
- **Style:** Hand-painted signboards: chunky comic capitals leaning on rough planks, as on a market price board.
- **Rendering:** Words in a two-tone vertical gradient with a light top bevel, dark drop edge and thick outline; planks with soft grain. Measured bright, vivid, hard-edged.
- **Colour:** Measured: pale wood #f5c6a4 40%, orange #f87a0f 8%, gold #fad603 8%, #b35933 6%, cyan #1bc4e5 6%, red #f82b19 6%, dark red #651408 4%. One colour per tier: red and gold, orange, cyan, purple.
- **Lighting:** From the top (measured: top on four parts): a light band on the upper half of each letter.
- **Ambience:** Prizes chalked up at a stall: plain, loud and legible.
- **Materials:** Bleached wood, glossy enamel letters, a gold coin.
- **Variants:** Four tiers on one plank shape; each word once at 357 to 557 px wide, reused small on the ladder and large on the win. Four round counters, one per tier: the help text says each jackpot needs a number of Chili symbols (15, 25, 35, 40), and in the bonus a round counter in the tier's colour sits at the left end of each board with a white number that falls as Chili symbols lock (seen: 5, 10, 10 and 4 beside GRAND, MAJOR, MINOR and MINI at one moment).
- **Motion:** Read from the file: Jackpot idle 1.5 s, select 0.58 s, win 0.95 s, a loop 1.2 s and counter show, hide and collect of 0.3 to 0.6 s; WinJackpot show 1.0 s and hide 0.58 s. Seen in play: at the end of the bought bonus the MINI was awarded: the gold word JACKPOT across the top of the board, the purple MINI word large and translucent over the reels, 15 in gold numerals flying up to the win plate, with coins and paper streamers; the MINI board flashed white-purple before it.
- **Construction:** One plank sprite tinted or swapped per tier plus a colour overlay (jackpotPlateColor); the number beside each word is set in a bitmap font, not drawn. The boards hang on the rope that belongs to the reel frame.
- **Notes:** On the intro screen the same four boards are shown larger with "x" after each value.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged · brightness 63% · saturation 62% · contrast 48% · warm 80% / cool 17% · brighter towards: top (4)
- **Palette (measured):** #f5c6a4 light orange 40%, #f87a0f orange 8%, #fad603 gold 8%, #b35933 orange 6%, #1bc4e5 cyan 6%, #f82b19 red 6%

### Reel board: the market-stall cabinet

`reel-board` · atlas · 23 parts · largest 599×285 · sheet `sheets/reel-board.webp`

- **Role:** The 5x3 reel area and its frame, the bonus version with an added row, the lock frame of held positions, the win line and the artists' guides.
- **Subject:** A red-painted wooden market stall: a dark mahogany plank backing (slotBg 512x251, slotBgSpecial 512x333 for the taller bonus board), thin red and cream trim strips, curved red side posts, a clay-tile roof corner (599x285), a rope (75x555) from which the jackpot boards hang, a glowing gold-orange outline (lockedEdge, lockedSide), seen in the bonus around the added row of locked red chilis, a brown diamond for an empty bonus position (tile14 43x64), soft shadows and a 16x25 gold win-line segment with its end cap.
- **Style:** Simplified painted props in the same storybook manner as the street, flatter and darker so that symbols stand out.
- **Rendering:** Flat colour with a light bevel line on the trims and a wood grain on the backing; shadows are separate soft sprites. Measured dark, vivid, low contrast.
- **Colour:** Measured: near-black wine #31080b 60%, red #ad2216 16%, white guides 11%, cream #e9b185 5%, deep red #790a03 2%. The board is a dark red-brown field framed in bright red.
- **Lighting:** Little modelling: a top-left highlight on the trims (measured: left and top). The locked-reel outline is the only light source drawn in.
- **Ambience:** A street-food stand; the reels are its counter front. In the bonus every empty position shows the brown diamond on the dark planks, and the empty positions of a reel that is nearly full burn with a panel of flame (seen; that it marks a reel close to a collect is an inference).
- **Materials:** Painted wood, clay tile, rope.
- **Variants:** Two backings (three rows and four rows) and one frame cut in pieces: roof corner, upper side, back post, top, bottom and side strips. Right-hand pieces only: the left side is the mirror.
- **Motion:** Read from the file: SlotFrame has idle 2.0 s, react 1.0 s, activate 0.5 s and upgrade 1.0 s, and SlotBackgrounds upgrade 1.0 s and reset 0.8 s, which is the board growing by a row; SlotFrameLock shows, loops (3.0 s) and hides the gold outline; WinLine draws the line along a 37-bone path in 0.67 s.
- **Construction:** The frame is assembled from strips and mirrored, so it can stretch when the bonus row is added. tileGuide (200x164 white) and containerGuide (50x50 green) are artists' anchors shipped in the atlas; tileGuide is referenced by 18 skeletons as a placeholder.
- **Notes:** One symbol cell is about 200x164 px in the atlas (tileGuide).
- **Measured:** dark, vivid, warm, low contrast · brightness 26% · saturation 76% · contrast 18% · warm 78% / cool 1% · brighter towards: left (3), top (1), top-left (1)
- **Palette (measured):** #31080b black 60%, #ad2216 red 16%, #ffffff light orange 11%, #e9b185 orange 5%, #790a03 dark red 2%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Help pictures of the 14 symbols

`help-symbol-pictures` · atlas · 14 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The flat pictures the provider's help page and paytable show, one per symbol (tile1 to tile14), from the shared store outside the game bundle.
- **Subject:** Each symbol composed whole on a 225x225 square: the five letters, cactus, taco with its bowl, tequila with its glass, sombrero, the hen on her nest with WILD, the three chilis in flames with their words, and the brown diamond of an empty bonus position.
- **Style:** The game's own symbol art, flattened.
- **Rendering:** As the symbols; the chili pictures include the flame and the hen her nest, so they show how the layered pieces look together.
- **Colour:** Measured: gold #f9cc1f 16%, brown #a1390e 15%, orange #e87d1a 14%, #f1c671 9%, cream #f4e2bc 6%, red #d82a23 4%, purple #a51fce 4%.
- **Lighting:** Top-left and top (measured).
- **Ambience:** A plain catalogue.
- **Materials:** As the symbols.
- **Variants:** 14 pictures of 225x225 px.
- **Motion:** None: stills.
- **Construction:** One WebP per symbol in the provider's asset store, named by tile number.
- **Notes:** These are the quickest reference for each symbol assembled, since no skeleton frame is drawn in this report.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 54% · saturation 76% · contrast 64% · warm 75% / cool 16% · brighter towards: top-left (3), top (2), right (1)
- **Palette (measured):** #f9cc1f gold 16%, #a1390e brown 15%, #e87d1a orange 14%, #f1c671 orange 9%, #f4e2bc light orange 6%, #d82a23 red 4%

### Wild: the hen on her nest

`symbol-wild` · atlas · 30 parts · largest 471×462 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol (tile10), which substitutes for all symbols except the Chilis (help text).
- **Subject:** A plump cream-white hen with a red comb and wattles and half-closed, unimpressed eyes, sitting on a straw nest, with a gold WILD word across the front; a white feather, an orange radial glow behind and a rising wisp of smoke.
- **Style:** Cartoon mascot in the family-animation manner of the chef, with a deadpan expression that gives the set its one joke.
- **Rendering:** Soft rounded shading with few details; straw as flat orange strokes; WILD in bevelled yellow gold with a dark brown outline. The unit measures bright and soft (soft-edge 0.68) because the glow and the smoke frames dominate it.
- **Colour:** Measured: cream #e4dac5 53%, orange glow #fdae21 39%, brown #98480d 4%, #c68b54 2%. White and straw against the dark board, with red only on comb and wattles.
- **Lighting:** Lit from the front and above; the orange disc (radialShineY 471x462) backlights her.
- **Ambience:** Comic calm in the middle of the heat.
- **Materials:** Feathers, straw, gold lettering, smoke.
- **Variants:** One symbol in parts: body 159x182, wing, tail, beak, wattles, eyelid and pupil, two nest pieces (back 211x55, front 146x40), a feather 163x45, the WILD word 122x53, and 18 frames of smoke (about 90x222).
- **Motion:** TileWild (27 bones, 19 slots): a 2.0 s idle loop, onLand 0.50 s, win 0.67 s (read from the file). The smoke is an 18-frame painted loop; eyelid, beak, wing and tail are separate so she can blink and ruffle (inference).
- **Construction:** The only symbol with a rig of its own. The smoke sequence is reused by the grill above the reels (the SceneCollector skeleton names it).
- **Notes:** The help page shows three hens side by side as the example of a Wild line.
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect · brightness 77% · saturation 48% · contrast 19% · warm 98% / cool 2%
- **Palette (measured):** #e4dac5 light orange 53%, #fdae21 orange 39%, #98480d brown 4%, #c68b54 orange 2%

### Low symbols: 10, J, Q, K, A

`symbols-letters` · atlas · 5 parts · largest 153×146 · sheet `sheets/symbols-letters.webp`

- **Role:** The five low-paying symbols (tile1 to tile5).
- **Subject:** A purple 10, blue J, teal Q, orange K and red A, each cut as if from a painted wooden board, with a zigzag or tooth pattern in a darker tone down one side and a cream-gold rim.
- **Style:** Chunky slab capitals in a folk-craft manner; the zigzag borrows the poncho and sombrero pattern.
- **Rendering:** Flat saturated fill with a faint wood grain, a thick bevelled cream rim, a dark outline and a soft drop shadow. Measured hard-edged, high contrast.
- **Colour:** Measured: brown #a33b11 18%, orange #ee8124 16%, cream-gold #f7cb7e 16%, purple #a51fcf 10%, teal #2d9770 8%, red #d33331 5%, blue #176bab 5%. One hue per letter.
- **Lighting:** From the top (measured: top on four of five): a light upper rim.
- **Ambience:** Painted market signage: cheerful and secondary.
- **Materials:** Painted wood with a gilt edge.
- **Variants:** Five symbols 92 to 153 px wide and 137 to 156 px high, one hue each.
- **Motion:** TileContainerJuniors (4 bones, five skins): onLand 0.48 s and win 0.50 s, so a letter is moved and scaled whole (read from the file).
- **Construction:** One sprite each, on a shared four-bone rig with a skin per letter.
- **Notes:** The rims are the same cream-gold on all five, which ties them to the frame trims.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 47% · saturation 75% · contrast 63% · warm 70% / cool 24% · brighter towards: top (4)
- **Palette (measured):** #a33b11 brown 18%, #ee8124 orange 16%, #f7cb7e orange 16%, #a51fcf purple 10%, #2d9770 green 8%, #d33331 red 5%

### High symbols: cactus, taco, tequila, sombrero

`symbols-high` · atlas · 8 parts · largest 199×183 · sheet `sheets/symbols-high.webp`

- **Role:** The four high-paying symbols (tile6 to tile9).
- **Subject:** A cluster of three round barrel cacti with pink flowers; a filled taco with a small clay bowl of white sauce; a square amber tequila bottle with a round stopper and a shot glass with a lime wedge; a yellow sombrero with a red, green and yellow zigzag brim.
- **Style:** Plump, glossy food-and-fiesta icons, rounder and more saturated than the street behind them.
- **Rendering:** Painted with strong gradients, crisp white speculars, a dark outline and a thin warm rim light; each has its own soft shadow sprite. Measured hard-edged, vivid, high contrast.
- **Colour:** Measured: gold-orange #e5a71d 22%, orange-brown #c1600c 14%, dark green #1f5f13 13%, brown #91320b 11%, leaf green #618f24 9%, near-black #2a0e04 7%, light gold #f6d95a 4%.
- **Lighting:** From the upper left (measured: top-left on four parts) with a yellow rim from behind.
- **Ambience:** A festive table: appetite and holiday.
- **Materials:** Cactus skin, fried tortilla, glass and liquid, woven straw.
- **Variants:** Four symbols 129 to 208 px wide. The taco is three sprites (taco 159x133, sauce bowl 73x72, shadow), the tequila three (bottle 129x187, glass 64x88, shadow); cactus and sombrero are one each.
- **Motion:** TileContainerSeniors (14 bones, four skins): onLand 0.50 s and win 0.67 s. The separate bowl and glass let the two parts of a symbol move against each other on a win (inference from the parts; not seen frame by frame).
- **Construction:** Single sprites or two-part groups on one shared rig with a skin per symbol; no frame sequence of their own.
- **Notes:** The sombrero symbol repeats the chef's hat band, and the cactus brings the only pink in the set.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 50% · saturation 78% · contrast 67% · warm 69% / cool 17% · brighter towards: top-left (4), top (1)
- **Palette (measured):** #e5a71d orange 22%, #c1600c orange 14%, #1f5f13 dark green 13%, #91320b brown 11%, #618f24 green 9%, #2a0e04 black 7%

### Chili symbols: green SPICY, yellow HOT, red BURNS

`symbols-chili` · atlas · 25 parts · largest 270×227 · sheet `sheets/symbols-chili.webp`

- **Role:** The three cash symbols (tile11 to tile13) that feed the three chilis above the reels and are the only symbols of the Hold & Win bonus. Help text: green pays 1x the stake, yellow 2x, red 5x, collected only in the bonus.
- **Subject:** Three glossy curved chili peppers, green, yellow and red, each with a slanted word on its tail (SPICY, HOT, BURNS) and its value in gold numerals with a dark red edge on the body; an 18-frame flame burns behind each.
- **Style:** The same plump glossy icon manner as the high symbols, pushed further: these are the largest and most saturated pieces on the reels.
- **Rendering:** Strong gradients from a dark underside to a bright top, long white speculars, a dark outline; words in bevelled capitals in the pepper's own colour. The flame is cel-painted in three flat tones with a soft orange glow. Measured vivid (saturation 0.86), half soft-edged because of the flames.
- **Colour:** Measured (flame frames included): orange #f78c08 40%, yellow #fed757 30%, #c05202 12%, brown #884f01 4%, reds #a20c04 3% and #e81612 2%. The three peppers are a pure green, a yellow-gold and a signal red: the traffic-light order is the value order.
- **Lighting:** From above (measured: top and bottom), with a rim from the flame behind.
- **Ambience:** Heat as reward: the hotter the colour, the bigger the prize.
- **Materials:** Waxy pepper skin, green stalks, flame.
- **Variants:** Three peppers on one rig (TileCash skins tile11, tile12, tile13): 202x148, 197x153, 270x227. Three word sprites. One flame loop of 18 frames (about 220x270) shared by all three, and a small white dotted cloud used when a pepper lands.
- **Motion:** TileCash (14 bones): onLand 0.50 s, loops of 0.90 s (plain, active, splash), collect 0.67 s, and separate tracks for updating the value and resetting the counter (read from the file). The help text says a landed Chili symbol flies to the chili of its colour above the reels; in the played frames the grill pepper of that colour lifts off its plate and flares when its symbol lands. In the bonus the values grow in place (5 became 10 and 32 on the bonus row) as +1 and x2 marks fly down from the grill.
- **Construction:** One rig, three skins; the value is a bitmap-font number set on the pepper, so the same art carries any amount. The peppers are also used at large size in the opening transition (SlotTransition names tile11Pepper and tile13Pepper) and on the grill.
- **Notes:** The words are English drawn into the art, not localised text: SPICY, HOT and BURNS ship only as pictures.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 61% · saturation 86% · contrast 49% · warm 95% / cool 2% · brighter towards: bottom (3), top (2)
- **Palette (measured):** #f78c08 orange 40%, #fed757 gold 30%, #c05202 orange 12%, #884f01 brown 4%, #a20c04 red 3%, #e81612 red 2%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The chef: the game's host behind the grill

`chef` · atlas · 19 parts · largest 570×475 · sheet `sheets/chef.webp`

- **Role:** The one character, standing behind the grill above the reels in the base game and bonus, and large on the intro screen. The Character skeleton: 40 bones, 20 slots, 14 animations.
- **Subject:** A stout, smiling man with a round face, rosy cheeks, brown side-parted hair, a handlebar moustache and a small chin beard, in a wide straw sombrero with a red, green and yellow zigzag band, a navy poncho with striped borders in red, orange, yellow and blue over a white open-collared shirt with rolled sleeves.
- **Style:** Family animated-feature caricature: large head, small features, soft volumes, no hard outline. Friendly rather than comic.
- **Rendering:** Smoothly shaded like a 3D render painted over: soft skin gradients with a warm rim, fine fabric pattern on the poncho, woven texture on the hat. Measured hard-edged, mid-tone, medium contrast.
- **Colour:** Measured: skin and straw orange-brown #a65d3b 32%, dark navy-plum #291a2a 21%, light skin #ecb291 15%, dark red-brown #6f2b1a 11%, #c58b71 7%, shirt white #f4eadd 4%. The poncho's stripes repeat the three chili colours on navy.
- **Lighting:** From the upper left (measured: top-left on five parts), with a warm bounce on the forearms as if from the grill below.
- **Ambience:** A proud cook showing his food: welcoming, a little theatrical.
- **Materials:** Skin, hair, straw, wool, cotton.
- **Variants:** One character, one skin. Three pairs of forearms for three gestures (cooking hands 288x164, clapping hands 347x143, thumbs up 195x271), a body 570x475, a hat 477x313, a face 212x252 with eye, eyelid, eyebrow, nose, two moustache halves and two hair pieces as separate parts, and two poncho shoulders.
- **Motion:** Read from the file: idle 2.0 s and loop 8.3 s, collect 2.4 s, activate 2.7 s, win 3.0 s, winJackpot 1.3 s, upgrade 1.2 s, gameSplash 3.7 s. The separate brows, eyelids and moustache halves and the swapped hand pairs mean expression and gesture changes rather than whole-body movement (inference). Seen in play: on the intro he stands large behind the three flaming chilis with his hands low, and gives two thumbs up inside a golden flash as the game opens; in the base game his forearms rest at the grill; when the bought bonus triggers he brings both hands to his mouth with wide eyes and a burst of fire and gold coins comes out between them; in the bonus he stands with raised brows behind the flames. No skeleton frame is drawn here (Spine 4.2).
- **Construction:** 19 sprites; mirrored parts ship once (one eye, one eyebrow, one sclera). The face is a single painted piece with holes for the eyes, so the head does not turn. He is cut off at the chest: the grill and the reel cabinet hide the rest, and no lower body exists.
- **Notes:** The character is cheap for the presence he has: a bust, one face, three hand pairs.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 41% · saturation 55% · contrast 54% · warm 83% / cool 16% · brighter towards: top-left (5), top (2), top-right (1)
- **Palette (measured):** #a65d3b orange 32%, #291a2a dark magenta 21%, #ecb291 orange 15%, #6f2b1a dark red 11%, #c58b71 orange 7%, #f4eadd light orange 4%


## Logo and title

The game's own wordmark.

### Flat logo for the help page

`help-logo` · atlas · 1 parts · largest 615×126 · sheet `sheets/help-logo.webp`

- **Role:** The one-line logo the provider's help page shows at its top.
- **Subject:** 3 BLAZING CHILIS with HOLD & WIN set under the last word, on one line, without the pepper.
- **Style:** As the logo.
- **Rendering:** As the logo, flattened to one 615x126 picture.
- **Colour:** Measured: dark green #3d721c 22%, red #fa2d10 17%, gold #f9d03b 16%, orange #f56821 15%, dark red #5f1c0a 8%.
- **Lighting:** As the logo.
- **Ambience:** As the logo.
- **Materials:** As the logo.
- **Variants:** One picture.
- **Motion:** None.
- **Construction:** A single WebP in the provider's asset store.
- **Notes:** Seen at the top of the help page in the played session.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 47% · saturation 81% · contrast 68% · warm 77% / cool 12% · brighter towards: bottom-left (1)
- **Palette (measured):** #3d721c dark green 22%, #fa2d10 red 17%, #f9d03b gold 16%, #f56821 orange 15%, #5f1c0a dark red 8%, #a44423 orange 6%

### Logo: 3 BLAZING CHILIS HOLD & WIN

`logo` · atlas · 4 parts · largest 414×346 · sheet `sheets/logo.webp`

- **Role:** The game's title, large on the intro screen and small on a wooden sign at the top right of the cabinet in play (the Logo and GameSplash skeletons).
- **Subject:** A fat gold 3 with a green outline, BLAZING CHILIS in arched capitals that run from yellow at the foot through orange to red, HOLD & WIN in yellow, and a large glossy green chili that lies under the words on the intro screen.
- **Style:** Comic poster lettering: heavy rounded capitals on a rising arc, outlined twice, in dark red-brown and then green.
- **Rendering:** Vertical gradient fills with a light upper bevel; a green outer contour like a pepper skin. Measured hard-edged, vivid, high contrast.
- **Colour:** Measured: dark green #1d611d 22%, gold #fbcd30 15%, green #35b226 15%, red #f92d10 9%, light gold #f7ea75 7%, dark red #5a1205 6%. The title is in the three chili colours.
- **Lighting:** A top bevel on the letters; the pepper has long speculars from above.
- **Ambience:** Loud, hot and friendly: a fairground sign.
- **Materials:** Glossy enamel lettering, pepper skin.
- **Variants:** Four sprites: the 3 (125x204), BLAZING CHILIS (781x172), HOLD & WIN (492x114) and the intro pepper (414x346). The same words serve both sizes; the in-play sign adds a pepper-shaped wooden plate (logoPlate, sorted with the spin counter, which shares it).
- **Motion:** Logo: show 1.0 s and hide 0.5 s; GameSplash: a 6.0 s loop and a 3.7 s hide (read from the file). Seen: the intro logo over the green pepper, then the small sign in play.
- **Construction:** Words as separate sprites so they can arrive one after another and be re-laid for the small sign.
- **Notes:** The digit and the two word lines are drawn pictures, not a font.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 50% · saturation 78% · contrast 69% · warm 56% / cool 22% · brighter towards: top (1), bottom-left (1), bottom-right (1)
- **Palette (measured):** #1d611d dark green 22%, #fbcd30 gold 15%, #35b226 green 15%, #f92d10 red 9%, #f7ea75 gold 7%, #5a1205 dark red 6%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature messages: BONUS GAME, JACKPOT and the three chili rules

`feature-labels` · atlas · 6 parts · largest 1036×184 · sheet `sheets/feature-labels.webp`

- **Role:** The localised word pictures of the bonus splash (FreeSpinsSplash) and the jackpot win.
- **Subject:** BONUS GAME and JACKPOT in fat yellow-gold capitals; the line FILL A REEL WITH CHILI SYMBOLS TO COLLECT THEIR CASH PRIZES; and three short rules, one per chili: TO ALL CASH PRIZES ON EACH SPIN (green), DOUBLES THE CASH PRIZE OF A CHILI (yellow), BONUS ROW OF LOCKED RED CHILI SYMBOLS (red).
- **Style:** Two letterings: the rounded comic capitals for the headings and a condensed italic sans in white with a red edge for the rules.
- **Rendering:** Headings with a gold gradient, white band and brown outline; rules flat white with a red outline and dark drop edge. Measured vivid, high contrast.
- **Colour:** Measured: gold #f6d32a 27%, dark red #601e10 15%, white #f8f4f4 10%, #c5924b 9%, #f7e170 7%.
- **Lighting:** A top band on the gold headings.
- **Ambience:** Clear instruction at a loud moment.
- **Materials:** Gold lettering; flat ink.
- **Variants:** Six pictures, each a separate localised file (en-GB loaded): headings 1036 px wide, rules about 340 px wide.
- **Motion:** FreeSpinsSplash show 0.83 s and hide 0.67 s (read from the file). Seen in play: BONUS GAME on the tall red board with +1, x2 and the up-arrow over the three rules and the three flaming chilis, the FILL A REEL line across the bottom; and JACKPOT across the board at the MINI win.
- **Construction:** Text is shipped as pictures per language, so every language needs these six redrawn or re-rendered.
- **Notes:** The rule lines use the same condensed italic as the Contrail One numerals.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 60% · saturation 61% · contrast 77% · warm 100% / cool 0%
- **Palette (measured):** #f6d32a gold 27%, #601e10 dark red 15%, #f8f4f4 light red 10%, #c5924b orange 9%, #f7e170 gold 7%, #d0b9b9 light red 6%

### Win tiers: BIG WIN, SUPER WIN, MEGA WIN, TOTAL WIN

`win-tiers` · atlas · 10 parts · largest 450×711 · sheet `sheets/win-tiers.webp`

- **Role:** The big-win words (WinBig, skins label1 to label3), the total at the end of the bonus (WinTotal), CONGRATS!, the tall board they stand on and the lights behind (WinBigEffects, WinSmall).
- **Subject:** BIG WIN in cyan, SUPER WIN in orange, MEGA WIN in red, each as two stacked words; TOTAL WIN in red and CONGRATS! in yellow as wide one-line pictures; a tall dark-red plank board with a clay-tile roof (winPlate 450x711, half of a mirrored sign); a white ray burst; a white glow with a chili-shaped hole (pepperGlow 497x487); a thin orange line.
- **Style:** The logo's comic capitals, wobbling slightly off the baseline.
- **Rendering:** Two-tone gradient with a bright top bevel, dark inner shade and thick dark outline with a lower extrusion. Measured hard-edged, vivid.
- **Colour:** Measured: dark red #4a170d 35%, red #ec3019 13%, #ad200d 11%, orange #f4731f 8%, white 7%, #eba270 6%, gold #f4cb19 4%, cyan #2ff9f2 3%. The tiers climb from cool to hot: cyan, orange, red.
- **Lighting:** From the top (measured: top on five parts).
- **Ambience:** A fiesta announcement.
- **Materials:** Glossy enamel letters on a painted wooden sign.
- **Variants:** Three tier words on one lettering (305 to 486 px wide), two wide localised words (1036 px), one board, three light sprites.
- **Motion:** Read from the file: WinBig sumShow 1.0 s, bangupEnd 0.5 s, hide 0.5 s; WinBigEffects a 2.5 s loop with a skin per tier and a "labelMax"; WinTotal show 0.65 s; WinSmall and WinNormal show a sum in 0.5 to 0.6 s. Coins and confetti are attached as particles. Seen in play: the small win (an amount in gold numerals on the wooden pepper plate with coins), and TOTAL WIN at the end of the bonus: the tall red board with its tile roof fills the middle of the screen, the three chilis in flames sit over a thin gold line, the red TOTAL WIN word under it and 138.00 in gold numerals, with coins falling. BIG, SUPER and MEGA WIN were not reached.
- **Construction:** The words are single sprites scaled by the rig; the board is one half, mirrored. The chili-shaped glow shows the theme's silhouette even in a plain light effect.
- **Notes:** Colour by tier follows the same cool-to-hot idea as the chilis.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 41% · saturation 75% · contrast 54% · warm 85% / cool 8% · brighter towards: top (5), top-right (1)
- **Palette (measured):** #4a170d dark red 35%, #ec3019 red 13%, #ad200d red 11%, #f4731f orange 8%, #feffff light cyan 7%, #eba270 orange 6%


## Effects

Frame sequences, glows, particles and transitions.

### Glows, rays, sparkles and engine textures

`light-and-particles` · atlas · 28 parts · largest 494×494 · sheet `sheets/light-and-particles.webp`

- **Role:** Generic light sprites used by almost every skeleton, and the engine's particle and displacement textures.
- **Subject:** A soft white glow (494 px), a white ray burst (497x487), a soft white square (the highlight of a symbol cell), a four-point glint, a 19-frame sparkle cluster (stars), small dots, an orange ember dot, and a grey gradient strip used as a displacement map.
- **Style:** Neutral effect stock.
- **Rendering:** White on transparent with soft falloff. Measured bright, saturation 0.001, soft-edge 0.44.
- **Colour:** Measured: white #fbfbfb 67%, greys 31%. Colour comes from tint at run time.
- **Lighting:** Self-lit.
- **Ambience:** Shine and emphasis.
- **Materials:** Light.
- **Variants:** 9 single sprites and one 19-frame sequence.
- **Motion:** whiteGlow is named by 13 skeletons and glowSquare by four; stars is a frame sequence. The displacement strip suggests a heat-haze distortion over the grill (inference; not confirmed in the frames).
- **Construction:** Shared white sprites tinted per use; three of them (glow, emitter_particle, displacement) are loose files outside the atlas.
- **Notes:** Nothing here is specific to the theme except how it is tinted.
- **Measured:** bright, muted, neutral, medium contrast, strong highlights · brightness 81% · saturation 0% · contrast 30% · warm 0% / cool 0%
- **Palette (measured):** #fbfbfb white 67%, #4c4c4c grey 19%, #cbcbcb grey 7%, #878787 grey 5%

### Smoke, clouds and puffs

`smoke-and-clouds` · atlas · 66 parts · largest 297×272 · sheet `sheets/smoke-and-clouds.webp`

- **Role:** Transition and landing effects in white.
- **Subject:** A cartoon cloud that swells and breaks into a ring in 28 frames (gameIntroCloud, up to 297x272); a flower-shaped smoke puff in 11 frames (tileSpawnSmokeEffect); a spark explosion in 10 frames; a pair of air puffs in 16 frames (bulletAir, about 120x45); a soft dust cloud.
- **Style:** Cartoon smoke with scalloped edges and a pale blue shade, in the manner of hand-drawn animation effects.
- **Rendering:** Flat white with one cool shadow tone and a clean edge; the dust cloud alone is soft. Measured bright, low contrast.
- **Colour:** Measured: white #f7f9f7 85%, pale blue #c0d8e0 7%, greys 7%.
- **Lighting:** A faint shade on the lower side.
- **Ambience:** Comic impact: puff, pop, whoosh.
- **Materials:** Smoke, dust.
- **Variants:** Four sequences (28, 11, 10 and 16 frames) and one dust sprite.
- **Motion:** Frame sequences. Seen in play: smoke drifts over the grill in the change to the bonus. The rest is read from names and files: a puff when a symbol spawns, air puffs behind a flying pepper (inference from "bulletAir").
- **Construction:** 65 of 66 parts are frames, white so that the engine can tint them.
- **Notes:** The cloud that breaks into a ring is named for the game intro (gameIntroCloud); it was not caught in a frame.
- **Measured:** bright, muted, neutral, low contrast, hard-edged, strong highlights · brightness 93% · saturation 2% · contrast 18% · warm 4% / cool 86%
- **Palette (measured):** #f7f9f7 light green 85%, #c0d8e0 light cyan 7%, #939393 grey 4%, #5f5f5f grey 3%

### Coins and confetti

`coins-and-confetti` · atlas · 22 parts · largest 166×166 · sheet `sheets/coins-and-confetti.webp`

- **Role:** Particles for wins: a turning gold coin (ParticleCoin) and paper streamers (ParticleConfetti).
- **Subject:** A gold coin embossed with a chili, in 10 frames of a turn from face-on to edge-on; twelve confetti pieces, long spirals in orange, red, purple, green and blue with white undersides, and small folded scraps.
- **Style:** Clean casino-style coin; flat paper confetti.
- **Rendering:** The coin has a hard gradient with a white glint and a darker rim; confetti is flat two-tone. Measured bright, vivid, hard-edged.
- **Colour:** Measured: gold #f8d024 41%, pale gold #fef29c 23%, orange #de890d 12%, #fbe55f 10%, brown #ad5807 4%.
- **Lighting:** Glints on the coin from the lower right and left (measured).
- **Ambience:** A payout and a party.
- **Materials:** Gold; paper.
- **Variants:** One coin in 10 frames (166 px), 12 confetti shapes of 15 to 154 px.
- **Motion:** The coin turn is a 10-frame sequence looped in 1.0 s by ParticleCoin; the confetti skeletons loop in 0.78 s (read from the file).
- **Construction:** Emitted by the engine as particles; only the coin has drawn frames. Seen in play at the jackpot and the total win: coins of several sizes tumbling across the whole screen with orange and red streamers.
- **Notes:** The chili on the coin is the only place the theme marks money itself.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 78% · saturation 70% · contrast 54% · warm 98% / cool 1% · brighter towards: bottom-right (2), left (1)
- **Palette (measured):** #f8d024 gold 41%, #fef29c light gold 23%, #de890d orange 12%, #fbe55f gold 10%, #ad5807 brown 4%, #fcfbf1 light gold 4%

### Fire: bursts, flame splashes, fire lines and streaks

`fire` · atlas · 75 parts · largest 349×201 · sheet `sheets/fire.webp`

- **Role:** The heat effects of the grill, the locked symbols and the transitions.
- **Subject:** A curling orange fire burst in 31 frames (up to 349x201); a white flame-shaped splash in 18 frames (flamesLighting, about 290x140), tinted by the engine (inference: it ships white); a tall thin fire line in 14 frames (straightFireLoop, about 60x400); a horizontal fire streak in 11 frames (effectTileLock 261x80); and an ember particle.
- **Style:** Cel-style cartoon fire: hard-edged licks in two or three tones with a soft outer glow, not photographic flame.
- **Rendering:** Painted frames with a yellow-white core and orange edge; the unit measures soft (soft-edge 0.77) because of the glows.
- **Colour:** Measured: orange #fd630a 50%, near-white #fffffb 29%, #f8a834 10%, pale gold #fdefa1 3%, #fbe265 3%, red #b31102 3%.
- **Lighting:** Self-lit.
- **Ambience:** Heat, speed, a kitchen flaring up.
- **Materials:** Flame and ember.
- **Variants:** Four sequences (31, 18, 14 and 11 frames) and one ember sprite.
- **Motion:** Frame sequences played by the skeletons: the burst on the collector's progress and upgrade, the streak when a symbol locks (its name, effectTileLock); a diagonal fire streak was seen crossing the board in the bonus, and empty positions of a reel that is nearly full burn with a panel of flame. Where the tall fire line is used was not settled.
- **Construction:** 74 of the 75 parts are frames. Colour fire is painted; the white splash is tinted at run time.
- **Notes:** This is the largest group of the atlas after the backgrounds: the game spends its frame budget on fire.
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 67% · saturation 64% · contrast 36% · warm 73% / cool 0% · brighter towards: right (11), bottom-right (4), top-left (1)
- **Palette (measured):** #fd630a orange 50%, #fffffb light gold 29%, #f8a834 orange 10%, #fdefa1 light gold 3%, #fbe265 gold 3%, #b31102 red 3%


## Game interface

Buttons, counters and panels drawn for this game.

### Buy Feature cards

`buy-feature-cards` · atlas · 2 parts · largest 490×190 · sheet `sheets/buy-feature-cards.webp`

- **Role:** The two pictures in the provider's Buy Feature window: "Hold & Win" and "All Chilis Hold & Win" (titles from the help text).
- **Subject:** First card: a whirl of green, yellow and red chilis with 1x, 2x and 5x and their words, spiralling into fire. Second card: the chef wide-eyed behind the grill with the three flaming chilis marked +1x, x2 and an up-arrow, the three bonus effects.
- **Style:** Promotional key art composed from the game's own pieces, denser and hotter than anything in play.
- **Rendering:** Painted, with motion blur on the spiral and heavy glow. Measured vivid, high contrast.
- **Colour:** Measured: brown-orange #9c4410 22%, gold #f3cb26 15%, dark red #300f0d 12%, #ce7437 10%, orange #ec730f 8%.
- **Lighting:** Lit by fire from below and behind.
- **Ambience:** Excitement turned up: the bonus as a blaze.
- **Materials:** Pepper skin, flame.
- **Variants:** Two cards of 490x190 px.
- **Motion:** None: stills.
- **Construction:** Two WebP pictures in the provider's asset store.
- **Notes:** The second card is the only place where the chef's face shows a different expression as a finished picture.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 46% · saturation 77% · contrast 82% · warm 85% / cool 9% · brighter towards: bottom (1)
- **Palette (measured):** #9c4410 brown 22%, #f3cb26 gold 15%, #300f0d dark red 12%, #ce7437 orange 10%, #ec730f orange 8%, #424443 grey 3%

### The grill: three chili collectors with heat dials

`grill-collectors` · atlas · 15 parts · largest 352×102 · sheet `sheets/grill-collectors.webp`

- **Role:** The display above the reels: a three-plate grill, one plate per chili colour, each with its pepper, its word (SPICY, HOT, BURNS) and a small heat dial. Chili symbols that land fly to the plate of their colour, and a chili that is "activated" brings its effect into the Hold & Win (help text). The SceneCollector skeleton: 51 bones, 58 slots, 24 animations, skins skin0 to skin2.
- **Subject:** Steel grill grates drawn in perspective, cold blue-grey (metal plate) and glowing red-orange (hot plate), each in a middle and a right-hand version; the three words as drawn capitals in green, yellow and red; a round gauge with a green-to-red scale and a black needle; a white ring halo; a black up-arrow with a gold edge (the added bonus row); and a red pepper with a face, horns and a moustache with a green stalk piece, which sits on the logo sign.
- **Style:** The same painted-prop manner as the cabinet, with the words in the comic capitals of the logo.
- **Rendering:** Grates in flat tones with a light edge; the hot plate is the same drawing with a red-orange glow painted in. Words with gradient, bevel and dark outline. Measured mid-tone, saturated, hard-edged.
- **Colour:** Measured: grey-brown #362e2c 22%, black 13%, red #dd3a2e 13%, steel blue #69798b 13%, dark red #721f0f 11%, green #5fda38 6%, gold #f5cc33 5%. Cold steel against red heat, with the three chili colours as labels.
- **Lighting:** The plates light themselves when hot; the dial and words have a top highlight.
- **Ambience:** A street grill heating up: progress is shown as temperature.
- **Materials:** Steel, embers, enamel lettering, a plastic gauge.
- **Variants:** One plate drawn twice per state (middle and right; the left is the mirror of the right) in two states, cold and hot. Three words. One dial with separate needle. Skins skin0, skin1 and skin2 dress the same rig as the green, yellow or red collector; the yellow skin alone has a second hot plate and metal plate.
- **Motion:** Read from the file: five progress steps (progress0 to progress4, 0.33 s each) with five loops, activate 1.67 s, collect 0.42 s, upgrade 0.77 s, reset 0.67 s. Seen in play: flames on the grill behind each pepper on the intro; the peppers resting on cold plates with their words and dials in the base game; when the bonus triggers, all three catch fire, the words swell and are replaced by the effect marks +1, x2 and an up-arrow, and the plates glow red through the bonus. The change of scene into the bonus is the grill alone on a red-orange fire screen with the three chilis jumping on it.
- **Construction:** The collector reuses the game's effect sequences by name (the symbol flame loop, a red version of it made by tint, the white flame splashes, smoke puffs, the Wild's smoke). Two attachments are keyed under an artist's folder name in the skeleton; the keys are kept as shipped and not shown.
- **Notes:** The help text says the peppers' graphical changes are for entertainment and do not change the chance of the feature: the dial is theatre.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 35% · saturation 57% · contrast 50% · warm 62% / cool 32% · brighter towards: top (1), bottom (1), top-left (1)
- **Palette (measured):** #362e2c grey 22%, #0b0b0c black 13%, #dd3a2e red 13%, #69798b blue 13%, #721f0f dark red 11%, #5fda38 green 6%

### Respin counter and win plates

`spin-counter` · atlas · 10 parts · largest 357×267 · sheet `sheets/spin-counter.webp`

- **Role:** The 1 2 3 respin counter of the Hold & Win bonus (SpinCounter), the pepper-shaped wooden plate that carries the small logo and the win amount (logoPlate, used by SpinCounter and WinNormal), and the WIN strip.
- **Subject:** A three-cell wooden frame hung on a short rope with two peg holes, the white italic digits 1, 2 and 3, a chili-shaped pale wood board with a red edge (357x267), a soft red strip and the white word WIN.
- **Style:** The signboard manner of the jackpot boards.
- **Rendering:** Pale wood with painted grain and a red rim; digits flat white with a dark edge. Measured hard-edged, medium contrast.
- **Colour:** Measured: pale wood #ecaf89 52%, red #a9311e 30%, #b4603d 10%, #f7d6bd 5%, white 2%.
- **Lighting:** A top-left highlight on the board.
- **Ambience:** Hand-made stall fittings.
- **Materials:** Wood, rope.
- **Variants:** Three digit sprites, one frame, one board, one strip, one word picture (localised).
- **Motion:** Read from the file: show 1.0 s, hide 1.4 s, remove0 to remove2 (0.33 s) as a respin is used, reset0 to reset2 (0.8 to 1.2 s) when a Chili lands, and a sum that shows, collects and hides.
- **Construction:** Digits are sprites, not font glyphs. The board shape is shared by three uses: the logo sign, the bonus counter and the base-game win amount.
- **Notes:** One wooden pepper silhouette, reused, does the work of three panels.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 57% · saturation 55% · contrast 48% · warm 98% / cool 0% · brighter towards: top (1), top-left (1)
- **Palette (measured):** #ecaf89 orange 52%, #a9311e red 30%, #b4603d orange 10%, #f7d6bd light orange 5%, #fefefe light orange 2%


## Typography

Embedded fonts and lettering.

### Numerals: Ultra in black with a gold rim

`UltraBlack` · atlas · 18 parts · largest 182×234 · sheet `sheets/UltraBlack.webp`

- **Role:** A bitmap font of digits and signs from the provider's font store (fonts-v2/UltraBlack). Seen in the bonus: it sets the effect marks +1 and x2, on the grill and flying down onto the symbols.
- **Subject:** Fat slab-serif digits 0 to 9, +, /, x, *, comma, minus, full stop and a question mark, about 234 px high.
- **Style:** Circus or wanted-poster slab serif, very heavy.
- **Rendering:** Black fill, a double gold rim with a bright inner line, and a thin red outer edge. Measured hard-edged, contrast 0.95.
- **Colour:** Measured: black #0c0302 52%, light gold #fbf1b1 13%, #e7be46 9%, #f2e67b 9%, dark red #4c1309 8%, red #c01f17 2%.
- **Lighting:** A light upper edge on the rim (measured: top).
- **Ambience:** Showy, a little Western.
- **Materials:** Black enamel with gilt edging.
- **Variants:** 18 glyphs kept here; 94 more that the font lists live in files of their own and were not loaded.
- **Motion:** None in the font.
- **Construction:** One 2048x512 page with a glyph table.
- **Notes:** The up-arrow of the red chili's effect (extraRow) is drawn to match it: black with a gold edge.
- **Measured:** mid-tone, saturated, warm, high contrast, hard-edged, strong highlights · brightness 33% · saturation 58% · contrast 95% · warm 100% / cool 0% · brighter towards: top (10), top-left (2), top-right (1)
- **Palette (measured):** #0c0302 black 52%, #fbf1b1 light gold 13%, #e7be46 orange 9%, #f2e67b gold 9%, #4c1309 dark red 8%, #c01f17 red 2%

### Numerals: Contrail One in white

`ContrailOneActiveWhite` · atlas · 18 parts · largest 62×166 · sheet `sheets/ContrailOneActiveWhite.webp`

- **Role:** A bitmap font of digits and signs from the provider's font store. Inference from comparing glyphs with the screens: it sets the white numbers in the round jackpot counters of the bonus.
- **Subject:** Condensed italic digits 0 to 9, x, +, -, *, /, comma, full stop and question mark, about 127 px high.
- **Style:** Sporty condensed italic sans.
- **Rendering:** Flat white with a black outline and a small dark drop edge. Measured saturation 0.0.
- **Colour:** Measured: white #fefefe 80%, black #050505 13%, greys 4%. It is left white on the coloured counters.
- **Lighting:** None drawn.
- **Ambience:** Neutral, fast.
- **Materials:** Flat ink.
- **Variants:** 18 glyphs kept; 92 more listed by the font live in files of their own and were not loaded.
- **Motion:** None in the font.
- **Construction:** One 2048x256 page with a glyph table.
- **Notes:** The three digit sprites of the respin counter are in the same style.
- **Measured:** bright, muted, neutral, high contrast, hard-edged, strong highlights · brightness 84% · saturation 0% · contrast 99% · warm 0% / cool 0%
- **Palette (measured):** #fefefe white 80%, #050505 black 13%, #c8c8c8 grey 2%, #999899 grey 2%

### Numerals: Tsiyugunsini in gold

`TsiyugunsiniWhiteGold` · atlas · 16 parts · largest 92×139 · sheet `sheets/TsiyugunsiniWhiteGold.webp`

- **Role:** A bitmap font of digits and signs from the provider's font store. Inference from comparing glyphs with the screens: it sets the jackpot values on the boards, the value on every Chili symbol and the win amounts (gold digits with a wine-red edge).
- **Subject:** Wide, heavy rounded digits 0 to 9, x, +, -, /, comma and full stop, about 134 px high.
- **Style:** Heavy rounded display sans, slightly squared.
- **Rendering:** A gold gradient from pale yellow at the top through a white band to deep yellow, with a dark wine-red outline and lower extrusion. Measured hard-edged, contrast 0.95.
- **Colour:** Measured: wine red #6b0c0d 28%, pale gold #fefbdd 26%, gold #f8de33 26%, near-black #170203 7%, #fdf79c 6%, #faca64 3%.
- **Lighting:** A white band across the upper middle of each digit (measured: top).
- **Ambience:** Prize money.
- **Materials:** Polished gold.
- **Variants:** 16 glyphs, all on the page.
- **Motion:** None in the font.
- **Construction:** One 2048x256 page with a glyph table.
- **Notes:** Its red edge matches the cabinet's red, so numbers sit naturally on the boards.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 61% · saturation 63% · contrast 95% · warm 100% / cool 0% · brighter towards: top (12), top-right (1)
- **Palette (measured):** #6b0c0d dark red 28%, #fefbdd light gold 26%, #f8de33 gold 26%, #170203 black 7%, #fdf79c light gold 6%, #faca64 orange 3%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 433 components cut from 41 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
