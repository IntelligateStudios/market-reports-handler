# The Goonies Quest For Treasure 2: art report

whitehat · run `2026-11-27-1045-whitehat-the-goonies-quest-for-treasure-2` · captured 2026-11-27

Source: the provider's free-play demo, https://contentrgspubst.blueprintgaming.com/Games/BP_TheGooniesQuestForTreasure295/1.7.0.1_hotfix_3-OaiaJ/index.html?playMode=demo&language=ENG&bp_jurisdiction=zz&brand=affdemo-affiliate&affiliate=affdemo&currency=USD&bpdemocurrency=GBP&customer=CUSTOMERLOBBY&configUrl=https%3a%2f%2ffileservicergspubst.blueprintgaming.com%2fDefault.aspx%3ffileType%3dconfig%26customer%3dCUSTOMERLOBBY%26affiliate%3daffdemo%26platform%3dDesktop%26clientFolder%3dBP_TheGooniesQuestForTreasure295%26serverType%3duat%26bp_jurisdiction%3dzz%26launchdomain%3d-1&qBridgeUrlXSS=contentrgspubst%2f%2fcom%2f%2fQBridge%2f1.14.1-hotfix1-E4yf2%2fqBridge.js&qBridgeUrl=https%3a%2f%2fcontentrgspubst.blueprintgaming.com%2f%2fQBridge%2f1.14.1-hotfix1-E4yf2%2fqBridge.js&serverType=uat&tld=0&game=BP_TheGooniesQuestForTreasure295&gameName=BP_TheGooniesQuestForTreasure295&assetsName=BP_TheGooniesQuestForTreasure295&platform=Desktop

**Extracted:** 726 named components from 726 textures in 726 atlases; 68 Spine skeletons; 8 frame sequences (205 frames); 1 fonts. Grouped into 59 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A licensed film adventure staged as a lantern-lit pirate cave: realistic painted portraits of the film's characters and a skeleton pirate host set among cartoon-bold gold lettering and jewel-bright treasure, almost entirely warm orange and gold against one navy reel board, with cyan and acid green kept as signal colours.

**Style.** Two registers side by side. Likeness art (four portrait symbols and one full-length figure) is semi-realistic film-poster painting. Everything else is stylised painted cartoon realism: props such as chests, coins, a ship's wheel, scrolls and chains painted with full materials, and a faceted, animation-background cave. One-Eyed Willy, a skull in a green tricorn hat with a gold eye patch, is the mascot and appears as symbol, map icon, intro host and transition mark.

**Rendering.** Fully painted, no line outlines on objects; heavy dark outlines only on lettering. Props carry real material detail (wood grain, rust, hammered metal) at small sizes with hard top-left highlights. The cave is flat faceted planes with soft gradients only in light. Light effects are separate soft additive pictures (the files sit on black or are plain glows), so glow is a layer, not paint.

**Colour.** Measured over the game's own art: black-brown #1c0c0c 19%, brown #572817 18% and #8e4b23 15%, then light gold #f8eb87 3% and one dark blue #273145 2%. Almost every unit measures 80 to 100% warm. The reel board is the exception (dark blue #152035, 94% of its unit) and is what the gold symbols are read against. Identity colours are used as codes, not decoration: blue, red and green for the three chests and their bonus symbols; gold, green, red and blue for the four collectors; yellow, green, blue and red for the four jackpot plates; cyan (#0cceff) for anticipation and One-Eyed Willy Spins; acid green (#53ff60, #78ff0b) for the Mystery Symbol and the lock.

**Lighting.** The scene has three lights by colour: orange from the skull-shaped cave mouth and two lanterns, teal-green daylight behind the stair, purple in the shadowed rock, with a warm pool on the floor under the reels. Objects are lit from the top left. Prizes glow from inside (coin heaps, the ruby, the chests), and every win or feature state is an added coloured light in the object's own shape.

**Ambience.** Adventure, not horror: a treasure hunt by lantern light, with skeletons played for fun and the film's catchphrases (NEVER SAY DIE!, HEY YOU GUYS!) used as art. The board always shows the long game: the trail map above and the three chests beside the reels.

**Shape language.** Chunky and irregular: hand-cut slab letters, torn parchment, hammered coins with uneven rims, faceted rock. The reel cell is a wide 215x180 rectangle, 6 reels by 4 rows; the collector grows from one cell to a 215x720 column. Round medallions and rectangles with value plates repeat across the prize symbols.

**Materials.** Parchment and turned wood with brass caps (scrolls, map), dark ship planks (board, panels), gold in three finishes (hammered doubloon, stamped skull coin, plain cartoon disc), ruby and cut gems, rusted iron (chains, the Treasure Wheel), bone, cobweb, lantern glass.

**Typography and lettering.** Four lettering families, all as pictures or bitmap fonts (nine font pages with BMFont .xml files; the only embedded web font is the shell's Roboto Black). A curly storybook pirate serif for values and counters; fat comic block capitals with gradient, extrusion and dark outline for feature names, each in its identity colour; angular faceted slab numerals in gold for win amounts and in silver for free-spin counts; and wide serif capitals that look cut from rusted copper for the big-win tiers. The logo is the film's own lettering.

**Motion.** 68 Spine skeletons, 62 of them version 4.1.24 (three 4.1.17 for the max-win notice, one 4.1.23, and two 3.8 for the shared Power Play art), plus 8 frame sequences of 19 to 30 frames (fire-line win boxes, win blast, dynamite, coin spin, coin burst, burning plate). The rigs are small (most under 35 bones; the unlock pop-up has 66) and move whole pictures: symbols land in 0.3 s and play a 1.0 s win, the collector grows in 1.1 s, the chests have 45 short state animations each, the background runs one 233 s loop of light. No character is rigged limb by limb: the one full figure is a still swung on a rope. None of the skeletons is drawn in this run, because the project's renderer does not draw Spine 4.x; the real game screens show the motion's key states.

**Variants and themes.** Variation is by recolour and by swap. One bonus chest in four colours; one collector in four colours and two heights; three chests from one drawing; four jackpot plates from one frame; five big-win tiers that differ only in the word; eight unlock screens from one scroll. Every reel symbol up to the portraits has a blurred twin for the spinning reel. A landscape and a portrait skeleton exist for the intro, chests, pots and pop-ups, over the same pictures.

**How it is built.** 726 loose pictures in named folders, no atlas pages at all, at one scale (folder 100). Each feature is a folder with its skeletons and an images folder, and the client loads a feature's folder when it first needs it: 77 pictures and 5 skeletons arrived only during play. Backgrounds are single 3200x3200 squares cropped by the viewport. Text that carries language is baked into pictures marked _ml. Several pictures are shipped twice under different folders (the trail icons, the rope figure, the explosion).

**Consistency.** Strong in colour and material: almost nothing leaves the orange-gold-brown family except by rule. Weaker in drawing hands: the realistic portraits, the cartoon props and a flat vector max-win notice are three styles, and there are three different coin designs. Leftover names from other Blueprint games (banana_trail, kong, genie_hammer_hit) and a ruby coin that reads SUPER for every pot show a shared production kit under the licensed skin (inference).

**What to take from it.** (1) Read this as Blueprint Gaming's build BP_TheGooniesQuestForTreasure295. The market report ranks White Hat Studios' US build (WHS_TheGooniesQuestForTreasure2US94); the two share a title, and that they share their art is inference. It is not the Jackpot Royale version. (2) The licence carries the faces, the logo and two catchphrases; everything else is ordinary pirate-treasure art that a studio could make for its own theme: a cave, chests, coins, a map, a skeleton host. The lesson is how little likeness art (four portraits and one still figure) is needed to make a licensed game feel like the film. (3) One cool surface in a warm game: the navy reel board (#152035) is the only large cool area, so gold and orange symbols read without outlines. Worth copying as a layout rule. (4) Colour as code: three chest colours, four collector colours and four pot colours are each used the same way everywhere they appear (symbol, title, glow, pop-up), and cyan and acid green are reserved for anticipation and for the mystery and lock states. (5) Persistent progress drawn as objects, not meters: a parchment map of 20 steps above the reels and three physical chests beside them, each step paying off with its own titled unlock screen. For AI art work this is a set of small, flat, high-contrast icons plus one reusable scroll. (6) Variants by recolour and swap: one drawing per idea (chest, collector, plate, banner), then colour sets and word pictures. An art package planned this way needs few masters and many cheap derivatives, which suits generating a master and deriving variants. (7) Motion is cheap here: small Spine 4.1 rigs that move whole pictures, additive glow layers and a handful of short frame sequences; no rigged character. A studio can match this level of animation without character rigging. (8) Production notes for our own packages: lazy loading by feature folder keeps the first load light (649 pictures at start, 77 more in play); square 3200 px backgrounds serve both orientations; baked-in language pictures (_ml) make every language a new set of files. (9) Not seen in this run, so not to be relied on from it: free spins (Treasure Spins and One-Eyed Willy Spins), the Treasure Wheel, a big win and Power Play in play. Their art is in the package and read from the sheets only.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm, medium contrast, hard-edged · brightness 39% · saturation 68% · contrast 50% · warm 78% / cool 14% · brighter towards: top (142), top-left (56), top-right (32)

Palette: #1c0c0c black 19%, #572817 brown 18%, #8e4b23 brown 15%, #fafdf5 light green 6%, #f8eb87 light gold 4%, #273145 dark blue 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 2 | 37% | 49% | 57% | 69% / 23% | #281a2a dark magenta 28%, #513d3d dark red 20%, #c47d41 orange 14% |
| Reel board | 5 | 29% | 77% | 47% | 92% / 7% | #240e08 black 39%, #722c11 brown 20%, #ba5422 orange 14% |
| Symbols | 10 | 53% | 68% | 62% | 65% / 26% | #f5fae8 light green 12%, #59250f brown 10%, #17120b black 8% |
| Characters | 2 | 39% | 46% | 56% | 41% / 43% | #2a427c blue 28%, #493228 brown 15%, #0f0b08 black 12% |
| Logo and title | 1 | 43% | 82% | 78% | 91% / 9% | #f2b819 orange 33%, #b00101 red 13%, #f76a07 orange 13% |
| Win celebrations and banners | 11 | 36% | 74% | 45% | 85% / 8% | #7e401d brown 31%, #1d0d0b black 23%, #4c1f0f brown 8% |
| Effects | 11 | 54% | 68% | 38% | 67% / 16% | #fffffa light gold 20%, #d4770c orange 17%, #6e2d07 brown 16% |
| Game interface | 6 | 34% | 74% | 68% | 88% / 11% | #3e1b0d brown 47%, #824521 brown 16%, #f55a06 orange 5% |
| Typography | 9 | 57% | 54% | 92% | 61% / 34% | #fcda5e gold 15%, #ef971d orange 15%, #f7f7f7 white 13% |
| Provider interface (shared) | 2 | 44% | 78% | 69% | 48% / 48% | #e2952c orange 18%, #0399fc blue 17%, #020416 black 11% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### The cave behind the intro

`intro-background` · atlas · 4 parts · largest 3200×3200 · sheet `sheets/intro-background.webp`

- **Role:** The scene behind the opening scroll.
- **Subject:** The same cave painting, with the stair rock and the glowing skull also supplied as separate cut-outs.
- **Style:** As the main background.
- **Rendering:** As the main background. In the intro screens the cave is shown blurred and tinted teal-blue behind the scroll; the files are not tinted, so the tint is applied by the client (inference).
- **Colour:** Measured: mid-tone, saturated, 67% warm and 25% cool. Dark magenta #281b2a 30%, dark red-brown #503d3d 21%, brown #855438 18%, orange #c88042 11%, light green #c5f5d9 4%.
- **Lighting:** As the main background; the skull cut-out carries its own orange inner glow.
- **Ambience:** The cave before the adventure starts: cooler and dimmer on screen than in play.
- **Materials:** Rock, timber, glowing bone.
- **Variants:** intro_popup_bg (3200x3200), intro_popup_bg_stairs (1071x1037), intro_popup_bg_skull (529x494), a black fill (400x400).
- **Motion:** Skeleton intro_popup_bg (Spine 4.1.24, 9 bones, 7 slots): one animation of 18.8 s, the length of the intro. Not drawn here.
- **Construction:** The backdrop with two cut-outs that can move apart from it (a slow push-in is the likely use: inference).
- **Notes:** The second 3200x3200 file is the same painting as bg_main as far as the sheet shows.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 36% · saturation 48% · contrast 57% · warm 67% / cool 25% · brighter towards: top (1)
- **Palette (measured):** #281b2a dark magenta 30%, #503d3d dark red 21%, #855438 brown 18%, #c88042 orange 11%, #c5f5d9 light green 4%, #9ec973 green 3%

### The cave: main background

`main-background` · atlas · 4 parts · largest 3200×3200 · sheet `sheets/main-background.webp`

- **Role:** The scene behind the reels in the base game.
- **Subject:** A cavern seen straight on: a stone stair with a broken wooden rail climbs to a cave mouth shaped like a skull that glows orange from inside; two lanterns hang on chains from the rock; teal-green daylight falls through gaps either side of the stair; a cracked flagstone floor in front; cobwebs in the corners.
- **Style:** Stylised painted environment, between animation background and concept art: big faceted rock shapes, strong colour zones, little fine texture.
- **Rendering:** Hard-edged planes of rock with flat colour and a second, lighter plane for the lit side; soft gradients only in the light shafts and the floor's pool of light. The painting fades to black at an irregular edge, so it sits on any screen shape.
- **Colour:** Measured: mid-tone, saturated, 71% warm and 22% cool. Dark magenta #281a2a 26%, dark red-brown #513d3d 19%, brown #824b2f 14%, orange #be753e 14% and #ecb653 7%, light green #c6f5da 4%, green #a2cc75 4%.
- **Lighting:** Three lights by colour: orange from the skull mouth and the lanterns (top and sides), teal-green from behind the stair, and purple in the shadowed rock. The floor carries a warm pool that sits under the reels.
- **Ambience:** A lit stage set of the film's cave: adventure, not horror. The reels sit where the stair is, so the skull crowns the board.
- **Materials:** Faceted rock, old timber, iron lanterns, cobweb, flagstones.
- **Variants:** bg_main (3200x3200, one square painting for landscape and portrait), bg1_highlights (2283x1694, the orange rims of the skull and chains alone), bg_dust (1600x1600), bg_lantern_glow (415x423).
- **Motion:** Skeleton bg_main (Spine 4.1.24, 8 bones, 6 slots): one animation of 233.3 s, additive slots. From the parts: the lantern glows and the orange highlights pulse and dust drifts (inference; not drawn here).
- **Construction:** One opaque painting plus three additive light layers; nothing in the scene is cut out to move.
- **Notes:** A square 3200 px master cropped by the viewport is a cheap way to serve both orientations.
- **Measured:** mid-tone, saturated, warm, medium contrast, hard-edged · brightness 38% · saturation 51% · contrast 57% · warm 71% / cool 22%
- **Palette (measured):** #281a2a dark magenta 26%, #513d3d dark red 19%, #824b2f brown 14%, #be753e orange 14%, #ecb653 orange 7%, #c6f5da light green 4%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Win box (three rows)

`win-box-3-high` · atlas · 30 parts · largest 350×900 · sheet `sheets/win-box-3-high.webp`

- **Role:** The same highlight for a symbol three rows tall.
- **Subject:** The fire line round a tall cell.
- **Style:** As the one-row win box.
- **Rendering:** As the one-row win box.
- **Colour:** Measured: dark, vivid, 100% warm. Black-brown #250d05 43%, brown #742b0f 21%, orange #bc5423 16% and #dc8d48 12%, light orange #eec275 8%.
- **Lighting:** It is the light.
- **Ambience:** Embers on the board.
- **Materials:** Fire.
- **Variants:** 30 frames, 350x900.
- **Motion:** Frame sequence `winbox_3high`, 30 frames in 1.0 s (skeleton winbox).
- **Construction:** A frame sequence on a rig.
- **Notes:** A three-row box exists although the collector symbol grows to four rows; where it is used was not seen.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 28% · saturation 80% · contrast 47% · warm 100% / cool 0%
- **Palette (measured):** #250d05 black 43%, #742b0f brown 21%, #bc5423 orange 16%, #dc8d48 orange 12%, #eec275 orange 8%

### Win box (one row)

`win-box` · atlas · 30 parts · largest 350×300 · sheet `sheets/win-box.webp`

- **Role:** The highlight drawn round a winning symbol.
- **Subject:** A line of fire running round the edge of one cell.
- **Style:** Effect animation, hand-finished fire.
- **Rendering:** A thin white-hot line with an orange bloom on black, for additive blending.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Black-brown #270e05 38%, brown #742b0f 21%, orange #be5222 16% and #dd8d49 14%, light orange #f4cc7b 10%.
- **Lighting:** It is the light.
- **Ambience:** Embers on the board.
- **Materials:** Fire.
- **Variants:** 30 frames, 350x300 (a 215x180 cell plus bloom).
- **Motion:** Frame sequence `winbox`, 30 frames played in 1.0 s by skeleton winbox (Spine 4.1.24): the lit part of the line travels once round the cell.
- **Construction:** A frame sequence on a rig that only places it.
- **Notes:** Shipped as 30 loose files rather than one sheet.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 31% · saturation 79% · contrast 52% · warm 100% / cool 0%
- **Palette (measured):** #270e05 black 38%, #742b0f brown 21%, #be5222 orange 16%, #dd8d49 orange 14%, #f4cc7b orange 10%

### Reel board

`reel-board` · atlas · 2 parts · largest 1364×772 · sheet `sheets/reel-board.webp`

- **Role:** The frame and backing of the 6-reel, 4-row board (cells of 215x180).
- **Subject:** Six columns of dark navy planks, and a thin frame around them drawn as a gold line with small ornaments at the corners.
- **Style:** Deliberately plain: the board gets out of the way of the symbols.
- **Rendering:** Flat dark planks with a faint grain and a thin lighter edge between reels; the frame is a fine painted gold cord.
- **Colour:** Measured: dark, vivid, 92% cool. One colour, dark blue #152035, is 94% of the unit.
- **Lighting:** None of its own; the board is the dark hole the symbols glow out of.
- **Ambience:** Ship timber at night. The only large cool area in a warm game, which is what makes the gold symbols read.
- **Materials:** Painted planks, gold cord.
- **Variants:** apps (1364x772, the frame) and app_back (1312x722, the planks).
- **Motion:** No skeleton names them: static.
- **Construction:** Two full-size layers, backing under the symbols and frame over them.
- **Notes:** Complementary contrast as a layout tool: navy board, orange world.
- **Measured:** dark, vivid, cool, low contrast, hard-edged · brightness 14% · saturation 62% · contrast 11% · warm 8% / cool 92%
- **Palette (measured):** #152035 dark blue 94%

### The three treasure chests

`treasure-chests` · atlas · 37 parts · largest 766×510 · sheet `sheets/treasure-chests.webp`

- **Role:** The side feature left of the reels: three chests named REEL ATTACK (blue), COLLECT EXPAND (red) and TRAIL BOOST (green); the intro reads OPEN A CHEST ON ANY SPIN TO TRIGGER ENHANCED BONUSES.
- **Subject:** Three wooden chests with gold bands and a skull crest, in blue, red and green, each on a stone pedestal with a carved skull. At the start they are bound in rusty chains; open, they are heaped with coins and carry their title across the front.
- **Style:** Painted cartoon realism, the same hand as the bonus symbol.
- **Rendering:** Each chest is painted in parts (lid, lid inside, base, base front) with wood grain, gold trim and a coloured lacquer panel. Titles are two-line lockups: a fat gradient block word over a gold serif word, heavy dark outline.
- **Colour:** Measured: mid-tone, vivid, 81% warm. Black-brown #160b07 24%, dark red #562111 19%, brown #88471f 10%, orange #f89b09 9% and #ba6b26 6%, gold #ffe00e 3%. Blue, red and green appear only as the three identity colours.
- **Lighting:** Gold light from inside the open chest (cf_chest_glow, cf_chest_rays, sparkles); the key and each title have a soft glow in the chest's colour.
- **Ambience:** The hoard, always on screen; the chains make the first unlock a small event.
- **Materials:** Wood, gold, rusty iron chain, stone, coin heaps.
- **Variants:** 37 pictures: per colour a lid (452x148), lid inside (616x207), base and base front (421x175), a title (495x247), a key glow; shared: 4 coin heaps of rising size (cf_coins_1 to 4), 3 chains, the skull key (92x126), pillar (376x329) and its shadow, a dark closed silhouette (chest_off1), glow, rays, sparkles, smoke, a coin burst, an anticipation ring.
- **Motion:** Skeletons chest1, chest2, chest3 (Spine 4.1.24, 33 bones, 27 slots, 45 animations each: `stage0` to later stages with `_anticipation` 0.1 s, `_hit` 0.7 s, `_reset` 1.0 s, and `empty` 1.2 s) and portrait copies with 35 bones; chest_reveal (`*_activate` 1.3 s, `*_reveal` 2.0 s per colour), chest_key, chest_anticipation. Not drawn here; the chests are in the game screens closed, chained and open.
- **Construction:** A chest is five layers so the lid can swing and coins can sit between base and front; the fill level is four swapped coin heaps, not animation.
- **Notes:** Three persistent pots as physical objects, not meters: the state reads from across the room.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 35% · saturation 71% · contrast 52% · warm 81% / cool 10% · brighter towards: top (14), top-right (1)
- **Palette (measured):** #160b07 black 24%, #562111 dark red 19%, #88471f brown 10%, #f89b09 orange 9%, #ba6b26 orange 6%, #ffe00e gold 3%

### The Upgrade Trail map

`upgrade-trail-map` · atlas · 32 parts · largest 1484×226 · sheet `sheets/upgrade-trail-map.webp`

- **Role:** The progress meter across the top of the reels: a ship moves along a trail of 20 steps and unlocks seven upgrades.
- **Subject:** A long parchment map rolled on two gold-capped wooden rods. On it, seven stations: three round medallions of Willy over treasure (green, red, blue), a skull in a bandana, a ship's wheel with a skull hub, Willy at half length, and a skull-shaped key of copper bones. Between them, 13 small gold bars as steps; a galleon is the marker; a gold skull coin is the token that flies to it.
- **Style:** Treasure-map illustration: the locked state is drawn as brown engraving on the parchment, the unlocked state as a full-colour painted icon laid on top.
- **Rendering:** Icons are small, fully painted and sharply lit, each with a gold outline glow as its highlight; the map is a sepia wash with faint route lines.
- **Colour:** Measured: mid-tone, vivid, 98% warm. Brown #764223 46%, orange-tan #b77e48 12%, black-brown #30150a 10%, gold #fce957 8%.
- **Lighting:** Icons lit from the top left; unlocking adds a star flare (unlock_flare, 288x288) and an outline glow in the icon's own shape.
- **Ambience:** The film's map as the game's long-term goal: always in view above the reels.
- **Materials:** Parchment, turned wood and brass (the rods), gold, bone, coloured gems behind the medallions.
- **Variants:** 32 pictures: map (1484x226), 2 rod ends, 7 station icons (108x110 to 202x222) and 5 outline highlights, 13 pips (about 43x30), ship (126x158), 2 flares, the coin (90x90).
- **Motion:** Skeleton unlock_map (Spine 4.1.24, 34 bones, 33 slots, 28 animations): `intro` 0.7 s, then `pos_1` to `pos_20` of 0.5 to 0.7 s with an `_idle` for each station. Skeleton banana_trail (8 bones, 0.7 s) throws the coin; its name looks carried over from another game (inference). Not drawn here.
- **Construction:** A static map with every icon and pip as its own slot, switched on step by step.
- **Notes:** A whole persistent meta-feature drawn in a 1484x226 strip: icons this small need the flat, high-contrast painting they have.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 43% · saturation 69% · contrast 55% · warm 98% / cool 2% · brighter towards: bottom-left (2), top (2), top-right (2)
- **Palette (measured):** #764223 brown 46%, #b77e48 orange 12%, #30150a black 10%, #fce957 gold 8%, #fdfdeb light gold 2%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Royals: 9, 10, J, Q, K, A

`symbols-royals` · atlas · 12 parts · largest 215×180 · sheet `sheets/symbols-royals.webp`

- **Role:** The six low symbols (files sym00 to sym05).
- **Subject:** One chunky capital or numeral per tile, leaning a little, on a dark navy plank tile with a thin lighter frame line.
- **Style:** Adventure-cartoon lettering: fat slab shapes with uneven, hand-cut edges, the same family as the logo's letters.
- **Rendering:** Each glyph is an orange, cracked, weathered face (it reads as old painted wood or hammered copper) with a bevel, a coloured outline and a dark drop shadow; fully painted, no flat fills.
- **Colour:** Measured: mid-tone, vivid, 79% warm. Black-brown #0e0804 26%, brown #75491d 25%, orange #f6a644 12%, #c8641d 6%. The outline is the only thing that tells the six apart by colour: blue on 9 and J, green on 10 and Q, red on K, gold on A (read from the sheet).
- **Lighting:** Light from the top left on every glyph; a soft warm highlight on the upper bevel.
- **Ambience:** Worn treasure-map lettering, kept quiet so the portraits and coins stand out.
- **Materials:** Cracked wood or copper (the face), enamel-like coloured rim, navy planks (the tile).
- **Variants:** 6 symbols, each with a `_blur` twin (the same tile smeared vertically for the spinning reel): 12 pictures, all 215x180.
- **Motion:** No skeleton names these files. In play a win is shown by the shared win box and win blast over the tile (seen in the game screens); the blur twin replaces the still while the reel turns.
- **Construction:** One opaque 215x180 tile per symbol with its background painted in; nothing is layered.
- **Notes:** The tile background is part of the picture, so a royal cannot be lifted off its tile without repainting.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 30% · saturation 69% · contrast 62% · warm 79% / cool 16% · brighter towards: top (10), top-left (2)
- **Palette (measured):** #0e0804 black 26%, #75491d brown 25%, #f6a644 orange 12%, #4c230e brown 11%, #c8641d orange 6%

### Character portraits (four high symbols)

`symbols-characters` · atlas · 8 parts · largest 215×180 · sheet `sheets/symbols-characters.webp`

- **Role:** The four high symbols (files sym06 to sym09): painted head-and-shoulders portraits of the film's characters.
- **Subject:** Three boys and, on sym09, the character the client's own files call Sloth (`intro_sloth` is the same figure at full length). Each fills the tile from the chest up, facing the player or three-quarters, with a different coloured scene behind: green jungle (sym06), blue ship rigging (sym07), orange glow (sym08), red (sym09). The files do not name the three boys, so they are not named here.
- **Style:** Semi-realistic digital portrait painting, in the manner of a film poster: likeness first, with smoothed skin and sharpened eyes and hair. That they are painted over film stills is inference.
- **Rendering:** Soft painterly modelling on the faces, crisper strokes in hair and collars, a coloured rim light taken from the background, and a loose, slightly blurred backdrop. No outline.
- **Colour:** Measured: dark, saturated, 68% warm and 26% cool. Dark red-brown #2b2121 40%, brown #5f3a29 28%, skin #f0ae90 4% and #c88669 2%, red #8e120e 4%, dark blue #314b60 4%. Each portrait owns one background hue (green, blue, orange, red), which is how the four are told apart at reel size.
- **Lighting:** A key light from the upper left on the face and a rim light in the background's colour on the far side.
- **Ambience:** Warm and friendly on the boys, comic-grotesque on sym09; the film's faces are the selling point of the symbol set.
- **Materials:** Skin, hair and cloth painted naturally; no metal or gem treatment, unlike every other symbol.
- **Variants:** 4 symbols, each with a `_blur` twin: 8 pictures, all 215x180.
- **Motion:** No skeleton names these files, so the portraits do not move on their own (inference from the files; in the game screens a win shows the win box and blast over a still portrait).
- **Construction:** One opaque 215x180 tile per portrait, background painted in.
- **Notes:** This is licensed likeness art: the one part of the package a studio cannot make without the licence. The art direction lesson is the contrast: realistic faces against cartoon lettering and jewel-like prize symbols.
- **Measured:** dark, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 28% · saturation 54% · contrast 51% · warm 68% / cool 26% · brighter towards: bottom-left (4), bottom-right (2), right (2)
- **Palette (measured):** #2b2121 dark red 40%, #5f3a29 brown 28%, #846a51 orange 9%, #8e120e red 4%, #314b60 dark blue 4%, #c26633 orange 4%

### The pirate flag symbol

`symbol-flag` · atlas · 4 parts · largest 290×193 · sheet `sheets/symbol-flag.webp`

- **Role:** A reel symbol (sym10) that lands stacked, several to a reel, in the game screens.
- **Subject:** A black flag stretched in a frame with gold studs at the corners: a white skull over two crossed cutlasses and a ribbon reading NEVER SAY DIE!
- **Style:** Graphic and flat compared with the rest: a white-on-black emblem, like a printed flag.
- **Rendering:** Clean vector-like skull and blades with light grey shading, a faint cloth ripple in the black, small painted gold corner studs.
- **Colour:** Measured over the unit: mid-tone, 48% warm and 52% cool. Black #0c0f11 38%, then the glow layers' dark cyan #034a6d 15%, cyan #3dd2fe 9% and #078acb 9%, white #f2fafb 8%. The tile itself is black and white; all the colour is in the win glow.
- **Lighting:** The emblem is evenly lit; the win state adds a cyan neon copy of the skull (sym10_glow, 224x210) and a blue flare (sym10_flare, 290x193).
- **Ambience:** The film's motto as a symbol; the only black tile on the board, so stacks of it read at once.
- **Materials:** Cloth, bone-white print, gold studs; neon light for the win.
- **Variants:** sym10 and sym10_flag (the same picture, the second used as the moving layer), one glow, one flare.
- **Motion:** Skeleton sym10_anim (Spine 4.1.24, 6 bones, 3 slots): `215x180_sym10_land` 0.3 s and `215x180_sym10_win` 1.0 s. Not drawn here: the project's renderer does not draw Spine 4.x.
- **Construction:** A still tile plus two additive light layers moved by a small rig.
- **Notes:** The four pictures are 215x180 to 290x193.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 35% · saturation 51% · contrast 74% · warm 48% / cool 52%
- **Palette (measured):** #0c0f11 black 38%, #034a6d dark cyan 15%, #3dd2fe cyan 9%, #078acb cyan 9%, #f2fafb light cyan 8%, #044eff blue 4%

### Wild: the silver doubloon

`symbol-wild` · atlas · 4 parts · largest 215×180 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol (sym11).
- **Subject:** An irregular, hand-struck silver coin with a cross and worn lettering, the word WILD laid across it in gold; on a navy plank tile with a thin frame.
- **Style:** Painted prop realism: an old coin as a museum piece, with cartoon-bold gold lettering on top.
- **Rendering:** Hammered, uneven rim, pitted grey metal with dark creases, a hard highlight on the upper edge; WILD is a bevelled gold slab word with a dark outline.
- **Colour:** Measured: mid-tone, saturated (the least vivid symbol, saturation 0.37). Grey #6f7676 36% and #a5abad 15%, black-brown #110a05 14%, gold lettering #e9bc50 7%; the glow layer adds orange #ff5300 3%.
- **Lighting:** Top-left light on the metal; an orange outline glow (sym11_glow) for the win.
- **Ambience:** Old Spanish treasure; cooler and quieter than the gold prize coins, so Wild and prize are not confused.
- **Materials:** Worn silver, gold lettering, navy wood.
- **Variants:** sym11 (whole tile), sym11_coin (the coin alone), sym11_border (the empty tile frame), sym11_glow.
- **Motion:** Skeleton sym11_anim (Spine 4.1.24, 7 bones, 3 slots): `215x180_sym11_land` 0.3 s, `215x180_sym11_anim` 1.0 s. Not drawn here.
- **Construction:** Coin, frame and glow as three 215x180 layers over the still.
- **Notes:** The only grey object among the symbols.
- **Measured:** mid-tone, saturated, warm, high contrast · brightness 45% · saturation 37% · contrast 72% · warm 88% / cool 12% · brighter towards: top-left (2), top (1)
- **Palette (measured):** #6f7676 grey 36%, #a5abad grey 15%, #110a05 black 14%, #464035 brown 11%, #e9bc50 orange 7%, #582c0a brown 4%

### Bonus: the treasure chest

`symbol-bonus-chest` · atlas · 31 parts · largest 297×344 · sheet `sheets/symbol-bonus-chest.webp`

- **Role:** The bonus (scatter) symbol (sym12), in four colours.
- **Subject:** An open wooden chest heaped with gold coins, a skull crest on its front, the word BONUS across the bottom, in a gold-framed tile. A stone pedestal with a carved skull (sym12_pillar) and a blue glass copy of Willy's head (map_willy_blue_glow) belong to its win animation.
- **Style:** Rich painted cartoon realism, the house style of the prize symbols.
- **Rendering:** Painted wood grain, gold bands and rivets, a glowing coin heap with white-hot centre; BONUS is a fat serif word with bevel, gradient and dark outline.
- **Colour:** Measured: mid-tone, vivid, 54% warm and 36% cool. Brown #72360e 16%, black-green #122309 16%, orange #cc791b 10%, gold #f6c749 8%, blue #1384c9 5%, dark blue #0f1a48 5%. The four variants change the chest panels, the tile background and the word: plain brown (sym12), red (sym12_1), blue (sym12_2), green (sym12_3).
- **Lighting:** The gold lights the lid from inside; each colour has its own shaft of light (chest_*_shaft), star flare and smoky wisp.
- **Ambience:** The promise of the feature; the three colours tie each bonus symbol to one of the three chests beside the reels.
- **Materials:** Wood, gold, coin heap, coloured lacquer panels, stone (the pillar).
- **Variants:** 4 whole tiles, 4 backgrounds (sym12_bg1 to 4), 4 chests (204x152), 4 BONUS words (197x66), 4 light shafts, 3 flares, 3 wisps, a coin heap, 2 glows, the pillar: 31 pictures.
- **Motion:** Skeletons sym12_anim and sym12_1/2/3_anim (Spine 4.1.24, 16 bones, 12 slots each): `1_bonus_lands_in` 0.3 s, `2_bonus_anticipation` 1.3 s, `2_bonus_idle` 3.0 s, `3_bonus_win` 1.0 s. `sym12_last_bonus_effect` has four sizes named 156, 195, 260 and 390. Not drawn here.
- **Construction:** Each colour is assembled from the same layer stack (background, chest, coins, word, shaft, flare, wisp), so a new colour is five recoloured pictures, not a new symbol.
- **Notes:** A clear lesson in variants by recolour: one drawing, four states.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 42% · saturation 79% · contrast 64% · warm 54% / cool 36% · brighter towards: top (12), bottom (3), right (1)
- **Palette (measured):** #72360e brown 16%, #122309 black 16%, #cc791b orange 10%, #f6c749 orange 8%, #1384c9 blue 5%, #0f1a48 dark blue 5%

### Cash coin: One-Eyed Willy's gold doubloon

`symbol-cash-coin` · atlas · 7 parts · largest 271×236 · sheet `sheets/symbol-cash-coin.webp`

- **Role:** The cash prize symbol (sym13): a coin that carries a money value on a plate under it.
- **Subject:** A round gold coin stamped with a pirate skull in a tricorn hat, a red gem for the one eye, a rope border; behind it a hot orange tile that looks like a sunlit treasure map, and a dark brown lozenge plate with a gold rim for the value.
- **Style:** Jewel-bright slot prize art: polished, saturated, readable at a glance.
- **Rendering:** Smooth airbrushed gold with crisp engraved lines, a red faceted gem, a glossy plate; the map background is painted with cracks and a bright centre.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Brown #4b1b05 32% and #99480f 17%, orange #e68315 17%, gold #f6cd2d 15%, light gold #fef18b 5%.
- **Lighting:** The coin is lit from the top; the tile glows from its centre as if the coin were lit from behind. Win layers: a round shine (242x242) and a ring of rays (coins_glow, 197x196).
- **Ambience:** Found treasure, warm and loud; the game's main prize object.
- **Materials:** Polished gold, ruby, lacquered wood plate, parchment.
- **Variants:** sym13 (whole tile), sym13_bg, coin13a (205x215), sym13_losenge (210x75), shine, coins_glow, and a gold border for the max-collect state (sym13_max_collect_border, loaded during play). The value is typeset with the ticket font.
- **Motion:** Skeleton sym13_anim (Spine 4.1.24, 17 bones, 12 slots): `sym13_anim_landin` 0.3 s, `sym13_anim` 1.0 s, and `max_collect_intro` 0.3 s, `max_collect_loop` 2.2 s, `max_collect_end` 0.2 s. Not drawn here.
- **Construction:** Background, coin, plate and two light layers, stacked; the number is live text.
- **Notes:** The same coin, 90x90, is the token that flies to the upgrade trail.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 43% · saturation 85% · contrast 59% · warm 100% / cool 0% · brighter towards: top (1), top-left (1)
- **Palette (measured):** #4b1b05 brown 32%, #e68315 orange 17%, #99480f brown 17%, #f6cd2d gold 15%, #bc691c orange 8%, #fef18b light gold 5%

### Jackpot coin: the ruby medallion

`symbol-jackpot-coins` · atlas · 22 parts · largest 758×370 · sheet `sheets/symbol-jackpot-coins.webp`

- **Role:** The jackpot prize symbol (sym14), one tile per pot: mini, minor, major, mega.
- **Subject:** A large faceted red gem set in a round gold coin with a braided rim, on the same hot orange map tile as the cash coin, with a plate or a word under it.
- **Style:** Jewel-bright prize art, the loudest symbol on the reels.
- **Rendering:** Hard-edged gem facets with white glints, smooth gold, a glossy plate; the word is a fat red-orange slab with a dark extrusion.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Dark red #521a08 31%, brown #a14010 22%, orange #df771d 17%, red #eb2b08 10%, gold-orange #f4b52d 10%.
- **Lighting:** The gem glows from inside; a wide orange flash (sym14_flash, 758x370) and a ring of rays for the win.
- **Ambience:** The top prize, treated as a film MacGuffin jewel.
- **Materials:** Ruby, gold, lacquered plate, parchment.
- **Variants:** 8 tiles (mini, minor, major, mega, each `_blank` with an empty plate and `_ml` with a word), 4 coins (coin_sym14, _blue, _green, _yellow), 4 word pictures, background, plate, 3 light layers, a max-collect border: 22 pictures. In this build all four `_ml` tiles and all four word pictures read SUPER, and the four coins look the same red at sheet size; what each pot shows in play was not seen.
- **Motion:** Skeleton sym14_anim (Spine 4.1.24, 19 bones, 14 slots): per pot `_anim1` 0.3 s and `_anim2` 1.0 s, plus the `max_collect` intro, loop and end. Not drawn here.
- **Construction:** The same layer stack as the cash coin with a gem instead of a skull.
- **Notes:** The file names promise four pot colours that the pictures do not show: worth a look by whoever plays the bonus.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 38% · saturation 86% · contrast 62% · warm 100% / cool 0% · brighter towards: top-left (13), top (4)
- **Palette (measured):** #521a08 dark red 30%, #a14010 brown 21%, #ed9325 orange 20%, #eb2b08 red 10%, #d3671a orange 6%, #080203 black 2%

### The ship's wheel symbol

`symbol-wheel` · atlas · 9 parts · largest 315×287 · sheet `sheets/symbol-wheel.webp`

- **Role:** A feature symbol (sym20 to sym22); the client's free spins pop-up shows it beside the coins as something that is collected.
- **Subject:** A wooden ship's wheel with a small skull in a green tricorn hat at the hub, on the orange map tile; sym21 adds the value plate; sym22 is the skull-and-swords emblem alone in an empty frame.
- **Style:** Painted prop, same family as the coins.
- **Rendering:** Brown wood with brass caps and a painted grain, a dark hub; glow layers are plain white-yellow shapes of the wheel and of its six gaps.
- **Colour:** Measured: mid-tone, vivid, 99% warm. Brown #4a210e 28%, light gold #ffffeb 17% (the glow layers), orange #ee8114 10%, gold #fdef80 5%.
- **Lighting:** Lit from the front; the win fills the wheel's shape and its gaps with white-gold light.
- **Ambience:** The ship as a prize: it points to the Treasure Wheel feature (inference from the shared wheel shape).
- **Materials:** Wood, brass, parchment.
- **Variants:** sym20, sym21, sym22, background, plate, the skull emblem, wheel (315x280), wheel_glow, segs_glow: 9 pictures.
- **Motion:** Skeletons sym20_anim and sym21_anim (Spine 4.1.24, 11 bones, 8 slots): `_land` 0.3 s and `_anim` 1.0 s. Not drawn here.
- **Construction:** Background, wheel, emblem and plate as layers, with two additive glows.
- **Notes:** What sym22 does in play was not seen.
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 51% · saturation 64% · contrast 56% · warm 99% / cool 1% · brighter towards: top-left (3), top (1)
- **Palette (measured):** #4a210e brown 28%, #ffffeb light gold 17%, #ee8114 orange 10%, #fdef80 gold 5%

### Mystery Symbol: the skeleton

`symbol-mystery` · atlas · 5 parts · largest 382×352 · sheet `sheets/symbol-mystery.webp`

- **Role:** The Mystery Symbol (sym23), switched on by the Upgrade Trail: the unlock pop-up shows this tile over the words MYSTERY SYMBOL NOW ACTIVE! WHAT RICHES WILL THEY REVEAL? Its effect files are named `organ_`.
- **Subject:** A pirate skeleton from the ribs up, bandana on the skull, arms spread, in a frame made of bones, on a dark carved-wood ground.
- **Style:** The darkest and most detailed of the prize symbols: painted like a film prop.
- **Rendering:** Brown-orange bone with deep shadow between the ribs, fine highlights, a bone frame with knuckle corners.
- **Colour:** Measured over the unit: 31% warm and 36% cool, because two of its five pictures are green light: black-green #101a0a 25%, dark green #05631c 11%, green #78ff0b 9%, light green #f3fee7 8%. The tile itself is brown and orange (read from the sheet).
- **Lighting:** Warm light from the upper left on the bones; the effect is a flat acid-green square (organ_cover_glow, 382x352) and a green ring (organ_sym_effect, 320x320).
- **Ambience:** Booby-trap menace; the one place the game uses sickly green.
- **Materials:** Bone, dark wood; green light.
- **Variants:** sym23 twice (the still and the animated copy), the skeleton cut out alone, two green effects.
- **Motion:** Skeleton sym23 (Spine 4.1.24, 5 bones, 4 slots): `land` 0.3 s, `win` 1.0 s. Not drawn here.
- **Construction:** Tile, cut-out figure and two additive lights.
- **Notes:** In the game screens the mystery positions flash as acid-green squares and turn into one symbol. The same green square is the lock effect's glow.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 49% · saturation 69% · contrast 49% · warm 30% / cool 36% · brighter towards: top (2), top-right (1)
- **Palette (measured):** #101a0a black 25%, #05631c dark green 11%, #78ff0b green 9%, #f3fee7 light green 8%, #cefca6 light green 7%, #a2ff4f green 5%

### One-Eyed Willy: the expanding collect symbol

`symbol-one-eyed-willy` · atlas · 49 parts · largest 388×948 · sheet `sheets/symbol-one-eyed-willy.webp`

- **Role:** The collector symbols (sym15 to sym18): Willy's head lands on a reel, grows to the full four rows and collects the coins; four kinds with different words.
- **Subject:** A skull in a wide green tricorn hat with a gold eye patch, over a heap of coins and gems, with a scroll banner under it: COLLECT on gold (sym15), CASCADE on green (sym16), BOOST on red (sym17), X COLLECT on blue (sym18). The tall form shows a beam of coloured light rising from a mound of treasure.
- **Style:** The game's mascot treatment: the richest painting in the symbol set, with comic-book lettering on scrolls.
- **Rendering:** The head is fully painted with leather, bone and gold; backgrounds are saturated gradients with painted treasure; banners are parchment scrolls with fat outlined words; multipliers are glossy gold 3D numerals set on a slant.
- **Colour:** Measured: bright, vivid, 59% warm and 30% cool. Light green-white #f4fae8 19% (glow layers), gold #efc74e 8%, orange #ee7d0a 7%, red #d21510 6%, green #419808 6% and #65e90c 4%, cyan #a9f0fb 3% and #08baff 2%. Four full colour sets: gold, green, red, blue.
- **Lighting:** Each kind is lit by its own colour from below and behind: a tall neon slab (sym15_expand_glow_*, 388x948), a shorter one (sym15_390_*), a smoky wisp, and mist from the skull's mouth (head_mouth_mist).
- **Ambience:** The dead pirate as the game's host: menacing in shape, playful in colour.
- **Materials:** Bone, leather, gold, gems, parchment scrolls, coloured light.
- **Variants:** 49 pictures: 4 one-row tiles (215x180), 4 four-row tiles (215x720), 4 tall backgrounds (324x780), 4 heads (217x169), 8 expand glows, 4 wisps, 4 scroll titles (220x91), 8 multipliers x2 x3 x4 x5 x6 x8 x10 x20 (204x142), 2 borders, plate, flare, mist, and 4 COLLECT word pictures loaded during play.
- **Motion:** Skeletons (Spine 4.1.24): sym_expand_anim (15 bones, 12 slots; `top`, `top_mid`, `bottom_mid`, `bottom` for each of the 4 kinds, 1.1 s each: the symbol grows from whichever row it landed on), syms_15_16_17_static_idles (`idle` 1.7 s and `land` 0.8 s per kind; sym18_land runs 5.5 s), sym_expand_extra_anims (19 bones; animations named `kong_1` to `kong_3`, 1.4 to 1.7 s with loops; the name looks carried over from another game: inference), multiplier_anims (one 1.3 s animation per multiplier). Not drawn here; an expanded Willy is in the game screens.
- **Construction:** One head, one treasure mound and one banner, recoloured four times and stretched by a rig between a 1-row and a 4-row frame.
- **Notes:** The most reusable idea in the package: an expanding symbol built as layers, so one rig serves every colour and every landing row.
- **Measured:** bright, vivid, warm and cool mixed, high contrast, strong highlights · brightness 64% · saturation 62% · contrast 63% · warm 59% / cool 30% · brighter towards: top (21)
- **Palette (measured):** #f4fae8 light green 19%, #efc74e gold 8%, #ee7d0a orange 7%, #d21510 red 6%, #409808 green 6%, #65e90c green 4%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Sloth on the rope: the respin multiplier

`sloth-multiplier-figure` · atlas · 5 parts · largest 745×937 · sheet `sheets/sloth-multiplier-figure.webp`

- **Role:** The same figure for another feature (folder `respin_collect_sloth_multiplier`, loaded during play).
- **Subject:** The rope-swinging figure again, with a second pose in which the rope has snapped (sloth_fall), a cloud of grey smoke for the landing and an orange star burst.
- **Style:** As the modifier intro figure: painted film-poster realism.
- **Rendering:** The two poses are the same painting with the rope cut short; smoke is a soft painted cloud.
- **Colour:** Measured: 50% warm and 50% cool. Blue #2a427c 30% and #5576ac 9% (the blur copy and the shirt), brown #483128 16%, black #0f0a08 13%, orange #cf5e11 5%.
- **Lighting:** Lit from the upper left; the snap is marked by an orange burst (sloth_snap_glow, 350x294).
- **Ambience:** Slapstick: he swings in, the rope breaks, he lands in smoke.
- **Materials:** Skin, cloth, rope, smoke.
- **Variants:** 5 pictures: sloth and sloth_fall (389x1370), blur (745x937), sloth_fall_smoke (563x326), sloth_snap_glow.
- **Motion:** Skeletons sloth_left and portrait_sloth_left (Spine 4.1). One picture swung as a whole, then swapped for the fall pose: not rigged limb by limb. Not drawn here.
- **Construction:** Two poses, a blur twin and two effects.
- **Notes:** The same painting is shipped in two folders (here and under modifier_intro).
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast · brightness 35% · saturation 53% · contrast 51% · warm 50% / cool 50% · brighter towards: top (2), top-right (1)
- **Palette (measured):** #2a427c blue 30%, #483128 brown 16%, #0f0a08 black 13%, #5576ac blue 9%, #f6f7f8 light blue 6%, #cf5e11 orange 5%

### Sloth on the rope: HEY YOU GUYS!

`modifier-intro-figure` · atlas · 6 parts · largest 745×937 · sheet `sheets/modifier-intro-figure.webp`

- **Role:** The figure that swings across the screen to announce a random modifier.
- **Subject:** The character the files name Sloth, at full length, hanging from a red rope by one hand: pirate hat, blue sleeveless shirt, red braces, grey trousers, boots. With it the three words HEY, YOU and GUYS! and a motion-blurred blue copy of the figure.
- **Style:** Painted film-poster realism for the figure (likeness art, like the portrait symbols); the words are chunky 3D slab letters.
- **Rendering:** The figure is painted with photographic shading and no outline; the words are white-to-grey bevelled blocks with a dark extrusion and cracks.
- **Colour:** Measured: 33% warm and 36% cool, high contrast. Blue #2a417d 26% and #5473aa 7% (the blur copy and the shirt), brown #4d3425 15%, white #f7f6f6 13%, black #100c08 11%, greys #cbcac9 8% and #959497 7%.
- **Lighting:** Lit from the upper left; a warm star flare (intro_hyg_flare1, 358x348) behind the words.
- **Ambience:** The film's most quoted line as the game's surprise moment.
- **Materials:** Skin, cloth, rope; stone-like lettering.
- **Variants:** 6 pictures: intro_sloth (389x1370, the rope makes it tall), intro_blur (745x937), hey (503x225), you (452x220), guys (685x233), a flare.
- **Motion:** Skeletons intro_hey_you_guys (Spine 4.1.24, 6 bones, 4 slots; `animation` and `near_miss`, 2.5 s each) and intro_sloth_left (5 bones, 3 slots, 1.2 s). The figure is one picture swung as a whole with a blur copy trailing it: it is not rigged limb by limb. Not drawn here.
- **Construction:** A single painted pose, a blur twin and three word pictures.
- **Notes:** A full-figure character that is a still, swung. It came up once in the played session (spin 80): the figure swings in from the left, far larger than the reels, in front of the board.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, strong highlights · brightness 42% · saturation 40% · contrast 61% · warm 33% / cool 36% · brighter towards: top (4), top-right (1)
- **Palette (measured):** #2a417d blue 26%, #4d3425 brown 15%, #f7f6f6 white 13%, #100c08 black 11%, #cbcac9 grey 8%, #959497 grey 7%


## Logo and title

The game's own wordmark.

### Logo

`logo` · atlas · 4 parts · largest 1477×871 · sheet `sheets/logo.webp`

- **Role:** The game's wordmark.
- **Subject:** THE GOONIES in uneven, hand-cut capitals with a small i, golden yellow to orange, over a red ribbon reading QUEST FOR TREASURE and a large gold 2.
- **Style:** The film's own logo lettering with a slot-game finish.
- **Rendering:** Bevelled gradient letters with a dark outline and a navy drop shadow; a folded red ribbon with white serif text.
- **Colour:** Measured: mid-tone, vivid, 91% warm, high contrast. Orange-gold #f2b819 33%, red #b00101 13%, orange #f76a07 13%, black #0e0808 9%, dark blue #103b54 8%, dark red #640703 7%.
- **Lighting:** Top light on the letter faces (the measure puts the light at the top).
- **Ambience:** Loud, cheerful, 1980s adventure.
- **Materials:** Glossy enamel letters, cloth ribbon.
- **Variants:** 4 sizes of one design: intro_logo_ml 1477x871, preloader_logo_ml 1040x535 (with a line of legal text under it), portrait_logo_ml 649x388, logo_ml 269x167.
- **Motion:** No skeleton of its own; it is a slot of the intro skeleton.
- **Construction:** One flat picture per size.
- **Notes:** A licensed wordmark: not something to imitate, only to note how little else on screen uses its yellow-red pair.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 43% · saturation 82% · contrast 78% · warm 91% / cool 9% · brighter towards: top (3)
- **Palette (measured):** #f2b819 orange 33%, #b00101 red 13%, #f76a07 orange 13%, #0e0808 black 9%, #103b54 dark blue 8%, #640703 dark red 7%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Bonus choice cards

`bonus-activation` · atlas · 4 parts · largest 689×807 · sheet `sheets/bonus-activation.webp`

- **Role:** The screen where the player picks one of the two bonuses.
- **Subject:** Two upright scrolls on carved rods: TREASURE SPINS and ONE-EYED WILLY SPINS, each with its title, the words COLLECTS ANY over small pictures of symbols, and a line of small text.
- **Style:** The intro scroll, upright and small.
- **Rendering:** Parchment and rods as on the intro; lettering in the bonus's own title style.
- **Colour:** Measured: 69% warm and 30% cool, high contrast. Light green-white #f5fbf5 22% and brown #3a1d0f 20%, gold #ffe8a0 6% and #fdd95f 6%, cyan #a1f5fe 6%, #01bbff 4%. The left card glows orange-gold, the right one cyan.
- **Lighting:** Each card has a glow in the card's shape (689x807): warm for Treasure Spins, cold for One-Eyed Willy Spins.
- **Ambience:** A fork in the map.
- **Materials:** Parchment, wood, brass.
- **Variants:** 2 cards (615x736) and 2 glows.
- **Motion:** Skeleton bonus_activation (Spine 4.1.24, 7 bones, 4 slots): `intro` 1.0 s, `idle`, `free_spins1_picked` and `free_spins2_picked` 1.0 s. Not drawn here.
- **Construction:** Two flat cards with the text painted in, each with an additive glow.
- **Notes:** Warm against cold is used to make a choice legible: the same pairing as the two transition colours.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 60% · saturation 56% · contrast 61% · warm 69% / cool 30%
- **Palette (measured):** #f5fbf5 light green 22%, #3a1d0f brown 20%, #ffe8a0 light gold 6%, #fdd95f gold 6%, #a1f5fe light cyan 6%, #01bbff cyan 4%

### Upgrade unlocked pop-ups

`upgrade-unlock-popup` · atlas · 52 parts · largest 3200×3200 · sheet `sheets/upgrade-unlock-popup.webp`

- **Role:** The full-screen notice each time the Upgrade Trail unlocks something (folder `unlock_collects`, loaded during play): seen three times in the played session.
- **Subject:** A small scroll on rods over a wall of dark planks. On it the red word UNLOCKED!, the name of the upgrade in its own colour (CASCADE COLLECT green, MATCH COLLECT magenta, BOOST COLLECT orange, X COLLECT cyan, MYSTERY SYMBOL teal serif, TREASURE WHEEL, ONE-EYED WILLY SPINS, POWER PLAY, the three chest titles), NOW ACTIVE! in white, and one teasing line in yellow (CASH FALLS AWAIT!, WATCH YOUR BOUNTY GROW, WHAT RICHES WILL THEY REVEAL?). Beside it, the thing unlocked: a tall Willy tile in the upgrade's colour, the Mystery Symbol tile, the wheel, the skull key or the three chests in chains.
- **Style:** The intro scroll's poster style, reused as a reward screen.
- **Rendering:** Parchment and rods as on the intro; each upgrade name is a fat outlined word with a gradient in its identity colour; teasing lines are small yellow block capitals with a dark outline.
- **Colour:** Measured: mid-tone, vivid, 92% warm, low contrast, because the plank wall dominates: brown #7a3e1e 44%, black-brown #2e140a 36%. The identity colours (green, magenta, orange, cyan) are small accents.
- **Lighting:** A warm glow behind the scroll (up_bg_glow) and a cyan flare as it opens; in the game screens the backdrop behind the scroll is tinted teal-blue, as on the intro.
- **Ambience:** A page of the map turning: progress made visible as an event.
- **Materials:** Parchment, wood, brass, iron chain.
- **Variants:** 52 pictures: plank wall (up_full_wood_bg, 3200x3200), scroll and rod (778x428, 227x834), UNLOCKED! (867x204), NOW ACTIVE!, 6 upgrade names, 3 chest titles, 9 teasing lines, 4 tall Willy tiles (267x624: green, blue, red and a purple one the reels do not ship), Mystery tile (356x320), Willy at half length (240x456), wheel, skull key, chests open and chained (1497x415), 3 chains, a green play button, glows, sparkles, smoke.
- **Motion:** Skeletons popup_unlocked and portrait_popup_unlocked (Spine 4.1). Not drawn here; three of its states are in the game screens.
- **Construction:** One scroll and one rig; every upgrade is a swap of a name picture, a line picture and an object picture.
- **Notes:** The purple tile and MATCH COLLECT suggest a fourth collector colour that the reel symbols in the capture do not have (inference). A good pattern to copy: a long-term meter whose every step pays off with its own titled screen.
- **Measured:** mid-tone, vivid, warm, low contrast, hard-edged · brightness 28% · saturation 75% · contrast 25% · warm 92% / cool 5% · brighter towards: top (24), top-right (5), top-left (3)
- **Palette (measured):** #7a3e1e brown 44%, #2e140a black 36%

### Max win pop-up

`max-win-popup` · atlas · 21 parts · largest 1922×1082 · sheet `sheets/max-win-popup.webp`

- **Role:** The notice shown when a round reaches the maximum win.
- **Subject:** A flat red panel under a red ribbon reading MAX WIN REACHED!, with GAME ROUND COMPLETE and CONGRATULATIONS!, a diamond in a laurel wreath on top, flat gold coins and blue and purple gems, and a yellow pill button with OK.
- **Style:** Flat vector illustration: none of the game's painting. It looks like a shared Blueprint notice shipped inside the game's folder (inference: its skeletons are Spine 4.1.17, the game's are 4.1.24, and the style matches nothing else here).
- **Rendering:** Flat fills with one tone of shading, white sans-serif text.
- **Colour:** Measured: dark, 81% of it the overlay's black-purple #0c0014; red #a70a08 9% and #700a09 3%, yellow #ffef05 2%.
- **Lighting:** None.
- **Ambience:** A compliance notice, not a celebration.
- **Materials:** None represented.
- **Variants:** 21 pictures: overlay (1922x1082), frame (968x693), button and OK text, 14 coins, 2 gems, a sparkle.
- **Motion:** Skeletons maxwin_popup (20 bones, 27 slots; `in` 1.3 s, `loop` 2.3 s, `out` 0.3 s), btn and overlay. Not drawn here.
- **Construction:** A layered pop-up with loose coin and gem pieces.
- **Notes:** Read here because it ships in the game's own asset folder; it says nothing about the game's art direction.
- **Measured:** dark, vivid, warm and cool mixed, low contrast, glow or soft effect · brightness 8% · saturation 96% · contrast 13% · warm 18% / cool 2% · brighter towards: top (2), top-right (1)
- **Palette (measured):** #0c0014 black 81%, #a70a08 red 9%, #700a09 dark red 3%, #ffef05 gold 2%

### The intro scroll

`intro-scroll` · atlas · 10 parts · largest 1917×1020 · sheet `sheets/intro-scroll.webp`

- **Role:** The opening screen: a scroll that shows four feature messages in turn.
- **Subject:** A wide parchment scroll on two carved wooden rods with gold caps. Painted on it, faintly, the cave with its skull; at the left stands One-Eyed Willy, a skeleton in a green tricorn hat, eye patch and long brown coat. The four messages: TREASURE CHEST BONUS, UPGRADE TRAIL, TREASURE SPINS, ONE-EYED WILLY SPINS, each with small pictures of the symbols they talk about.
- **Style:** The game's poster style: painted props with comic-book lettering.
- **Rendering:** Parchment with torn edges, stains and a soft inner shadow; the rods are turned wood with painted brass. Message lettering is fat yellow-to-orange gradient capitals with a brown extrusion and dark outline, with white and blue words for contrast.
- **Colour:** Measured: mid-tone, vivid, 91% warm, high contrast. Brown #5e3723 41%, orange-tan #9b602a 13%, gold #ecb40e 11%, black-brown #180a06 4%, cyan #05c3ff 3%.
- **Lighting:** Warm, from the top; a cyan flare (popup_flare2, 800x700) and orange sparks mark the change of message.
- **Ambience:** A map unrolled for the player: the film's premise in one prop.
- **Materials:** Parchment, wood, brass, bone, old cloth.
- **Variants:** intro_scroll (1917x1020), 4 message layers of the same size with only lettering on them, 2 effects, 3 small bonus tiles (215x180).
- **Motion:** Skeleton intro_popup, and portrait_intro_popup (Spine 4.1.24, 34 and 35 bones, 32 slots): one animation of 18.8 s that cycles the messages and lights the trail icons. Not drawn here; three of the four messages are in the game screens.
- **Construction:** A scroll picture with full-size transparent lettering layers swapped over it.
- **Notes:** Full-screen layers that are mostly empty are simple to author and heavy to ship; the client loads them anyway.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 41% · saturation 72% · contrast 62% · warm 91% / cool 8% · brighter towards: top (3), bottom-left (2), bottom-right (1)
- **Palette (measured):** #5e3723 brown 41%, #9b602a orange 13%, #ecb40e gold 11%, #180a06 black 4%, #05c3ff cyan 3%, #f7f71b gold 2%

### The trail map on the intro

`intro-trail-map` · atlas · 22 parts · largest 1327×190 · sheet `sheets/intro-trail-map.webp`

- **Role:** The intro's own copy of the Upgrade Trail: shown on the UPGRADE TRAIL message.
- **Subject:** The seven station icons and 13 gold bars of the trail, with the map strip in its locked, engraved state.
- **Style:** As the Upgrade Trail map.
- **Rendering:** As the Upgrade Trail map: small painted icons with hard highlights.
- **Colour:** Measured: dark, vivid, 97% warm. Brown #562d16 35%, black #0a0402 34%, tan #91582c 12%, orange-gold #f8b718 3%.
- **Lighting:** Top-left light on the icons; one star flare (map_flare, 368x383).
- **Ambience:** A preview of the long game.
- **Materials:** Parchment, gold, bone.
- **Variants:** 22 pictures: map_off (1327x190), map_flare, pos_1 to pos_20 (the same icons and pips as the trail, under intro names).
- **Motion:** Slots of the intro skeleton (18.8 s).
- **Construction:** The trail's parts shipped a second time for the intro.
- **Notes:** Duplicate files: the intro could have reused the trail's pictures.
- **Measured:** dark, vivid, warm, high contrast · brightness 24% · saturation 68% · contrast 67% · warm 97% / cool 2% · brighter towards: bottom-left (1), top (1), top-right (1)
- **Palette (measured):** #562d16 brown 35%, #0a0402 black 34%, #91582c brown 12%, #f8b718 orange 3%

### Coin burst from a chest

`chest-coin-burst` · atlas · 23 parts · largest 587×508 · sheet `sheets/chest-coin-burst.webp`

- **Role:** The coins that fly out when a chest is hit.
- **Subject:** A fountain of round gold coins rising and scattering.
- **Style:** Clean cartoon coins, simpler than the hammered doubloon.
- **Rendering:** Smooth yellow-orange discs with one highlight and one shadow tone, slight motion blur.
- **Colour:** Measured: bright, vivid, 100% warm. Orange-gold #f6b32b 62%, orange #d56d15 22%, gold #fef650 10%, brown #a34b0f 5%.
- **Lighting:** Self-lit.
- **Ambience:** A quick payout sparkle.
- **Materials:** Gold.
- **Variants:** 23 frames, 587x508.
- **Motion:** Frame sequence `cf_chestcoins`, 23 frames, played inside the chest skeletons' `hit` animations (0.7 s).
- **Construction:** A frame sequence placed by the chest rig.
- **Notes:** A third coin design in one game (hammered doubloon, stamped skull coin, plain disc).
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 67% · saturation 83% · contrast 53% · warm 100% / cool 0%
- **Palette (measured):** #f6b32b orange 62%, #d56d15 orange 22%, #fef650 gold 10%, #a34b0f brown 5%

### Big win banner

`big-win` · atlas · 15 parts · largest 1260×840 · sheet `sheets/big-win.webp`

- **Role:** The win celebration: five tiers named NICE, BIG, HUGE, MEGA and EPIC, each followed by WIN.
- **Subject:** A tier word in wide serif capitals that look cut from rusted copper or burnt wood, over a rolled red cloth banner that holds the amount; five cut gems as particles: a white diamond, a red hexagon, a yellow oval, a green emerald cut and a blue pear.
- **Style:** Painted, textured lettering rather than glossy enamel: the most restrained celebration type in the game.
- **Rendering:** Letters have a pitted orange-brown face, a thin bright edge and a deep dark-red extrusion; the banner is painted cloth with rolled ends; gems are crisp facets with white glints.
- **Colour:** Measured: mid-tone, vivid, 96% warm. Dark red #3a0c05 23%, orange #cf701b 20%, brown #882f0b 19%, light gold #fefdf5 10%, orange #f8a82a 8%, red #e73a27 5%. The gems are the only cool colours.
- **Lighting:** Two additive flares behind the words (bw_flare1 894x894, bw_flare2 1260x840) and a white-hot glow in the banner's shape.
- **Ambience:** Treasure dug up: heavy and warm.
- **Materials:** Copper or wood lettering, red cloth, cut gems.
- **Variants:** 15 pictures: 5 tier words (1519x454), WIN (667x266), banner and its glow (1570x419), 2 flares, 5 gems (242 to 370 px).
- **Motion:** Skeleton big_win (Spine 4.1.24, 6 bones, 5 slots): an `_in` of 2.0 s and a `_loop` of 0.7 s per tier; big_win_panel `intro` 1.0 s. Not drawn here. No big win came in the played session.
- **Construction:** Word pictures swapped on one small rig; gems and the spinning coin are thrown as particles.
- **Notes:** All tiers share one banner and one colour: the tier is told by the word alone.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 45% · saturation 76% · contrast 57% · warm 96% / cool 3% · brighter towards: top (6), bottom (2), bottom-left (1)
- **Palette (measured):** #3a0c05 dark red 23%, #cf701b orange 20%, #882f0b brown 19%, #fefdf5 light gold 10%, #f8a82a orange 8%, #e73a27 red 5%

### Spinning doubloon

`big-win-coin` · atlas · 25 parts · largest 256×256 · sheet `sheets/big-win-coin.webp`

- **Role:** The coin thrown about during a big win.
- **Subject:** A hammered, irregular gold-copper coin with a worn cross, turning.
- **Style:** Rendered or painted to look real: the most photographic object in the effects.
- **Rendering:** Pitted metal with hard specular glints, an uneven rim, full shading on every frame.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Orange-brown #a64e1c 29%, orange #eb8933 26%, brown #63230b 23%, light orange #fccd60 10%, light gold #fff88f 6%.
- **Lighting:** A fixed light from the upper left while the coin turns.
- **Ambience:** Real pirate gold, not arcade tokens.
- **Materials:** Hammered gold.
- **Variants:** 25 frames, 256x256.
- **Motion:** Frame sequence `coin_spin`, 25 frames: one full turn.
- **Construction:** A frame sequence used as a particle.
- **Notes:** It contrasts with the flat vector coins of the max win pop-up.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 48% · saturation 77% · contrast 70% · warm 100% / cool 0% · brighter towards: top-left (12), left (9), right (1)
- **Palette (measured):** #a64e1c orange 29%, #eb8933 orange 26%, #63230b brown 23%, #fccd60 orange 10%, #fff88f light gold 6%, #c37231 orange 3%

### Modifier titles

`modifier-titles` · atlas · 5 parts · largest 1081×491 · sheet `sheets/modifier-titles.webp`

- **Role:** The titles of the five random modifiers.
- **Subject:** DYNAMITE BLAST, HIDDEN TREASURE, BONUS BOOST, COLLECT BOOST and CAVE IN, each a two-line lockup in its own lettering.
- **Style:** Five small logos, each dressed as its subject: fire, jungle green, treasure copper, cracked stone.
- **Rendering:** DYNAMITE BLAST: a white script word over orange block letters with a red glow. HIDDEN TREASURE: bright green block capitals with a dark green extrusion. BONUS BOOST: copper-gold serif capitals with a heavy dark outline. COLLECT BOOST: the same with COLLECT in green. CAVE IN: blue-grey stone letters with cracks and falling rocks, IN in gold.
- **Colour:** Measured: mid-tone, vivid, 60% warm and 26% cool, high contrast. Orange #f47008 13%, black #0d0d03 10%, green #a5f802 10%, brown #67280b 9%, gold #f7d058 8%, dark green #116703 6%.
- **Lighting:** Top light on all four; the dynamite title glows.
- **Ambience:** A comic-book sound effect for each surprise.
- **Materials:** Fire, enamel, copper, stone.
- **Variants:** 5 pictures, 651x459 to 1081x491. The file names are title_dynamite_wilds, title_hidden_tresures, title_bonus_boost, title_collect_boost (loaded during play), title_cave_in.
- **Motion:** Skeleton modifier_title_intros (Spine 4.1.24, 2 bones, 1 slot): five 1.5 s animations, one per title. Not drawn here.
- **Construction:** One picture per title, popped in on one bone.
- **Notes:** One modifier came up in the played session (the rope swing at spin 80); no frame caught its title.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 49% · saturation 78% · contrast 80% · warm 60% / cool 26% · brighter towards: top (3)
- **Palette (measured):** #f47008 orange 13%, #0d0d03 black 10%, #a5f802 green 10%, #67280b brown 9%, #f7d058 gold 8%, #116703 dark green 6%

### The Treasure Wheel

`treasure-wheel` · atlas · 18 parts · largest 1277×1278 · sheet `sheets/treasure-wheel.webp`

- **Role:** A bonus wheel that awards a jackpot or a mystery win.
- **Subject:** A large rusted iron ship's wheel with a riveted hub. Between its spokes sit wedges painted with a cave of treasure: MAJOR in blue light, MEGA in red, MINI in yellow, MINOR in green, and a dark green MYSTERY WIN wedge with a sunken wreck. A faceted red-and-gold arrowhead is the pointer; PRESS TO SPIN! in red.
- **Style:** Painted prop realism at the largest scale in the game.
- **Rendering:** Thick rust and pitting on the iron, bolt heads on the hub; wedges are small full paintings with a coloured light source each; labels are fat block capitals in the pot colours.
- **Colour:** Measured: mid-tone, vivid, 85% warm, high contrast. Brown #4f341c 22%, orange-brown #a05729 19%, black #1b130c 13%, orange #f1a116 10%, light gold #fbec8c 6%, red #f43b09 4%.
- **Lighting:** Each wedge is lit from its outer edge in its own colour; a white-gold wedge shape and a red outline mark the winning segment; a ring of sparks (treasure_wheel_effect).
- **Ambience:** The ship's helm as a prize wheel.
- **Materials:** Rusted iron, gold, painted treasure.
- **Variants:** 18 pictures: wheel (1277x1278), 5 wedges each with a `_blank` twin without its word (474x475), hub (346x345), arrow (233x322), 2 segment lights (497x385), an effect ring, PRESS TO SPIN (1070x134), a COLLECT ALL line loaded during play.
- **Motion:** Skeleton treasure_wheel_effects (Spine 4.1.24, 5 bones, 4 slots): `segment_win` and `mystery_win`, 1.3 s. The wheel's turn itself is not in a skeleton, so the client's code turns it (inference). Not reached in play.
- **Construction:** A wheel picture with wedges placed by code, so the layout of segments can change without new art.
- **Notes:** The blank twins let a wedge show a number instead of its word.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 43% · saturation 67% · contrast 63% · warm 85% / cool 9% · brighter towards: right (10), top (2), top-right (2)
- **Palette (measured):** #4f341c brown 22%, #a05729 orange 19%, #1b130c black 13%, #f1a116 orange 10%, #fbec8c light gold 6%, #fbf5e8 light orange 4%

### Free spins pop-ups

`free-spins-popups` · atlas · 26 parts · largest 1370×780 · sheet `sheets/free-spins-popups.webp`

- **Role:** The award screens of the two bonuses: Treasure Spins and One-Eyed Willy Spins, each in a plain, SUPER, MEGA and ULTRA tier.
- **Subject:** A wide painted scene of a ship's hold with Willy's skeleton seated at the left among barrels and treasure, kept dark and blurred as a backdrop. Over it, title lockups: TREASURE in gold block letters with a heap of coins and SPINS in red script; ONE-EYED WILLY in teal serif with SPINS in orange block letters; the tier on a red ribbon. Small pictures pair the collected symbols (cash coin with ruby coin; wheel with coins).
- **Style:** The intro's poster style, turned up.
- **Rendering:** The backdrop is a soft, almost photographic painting; lettering is bevelled, outlined and extruded like the intro's.
- **Colour:** Measured: mid-tone, vivid, 83% warm, high contrast. Black-brown #160f0a 24%, brown #552610 16% and #974710 10%, orange #d06f15 10% and #f7a509 5%, gold #f9ea0d 5%.
- **Lighting:** A warm flare behind the title (fs_popup_flare, 878x1079) and a cyan burst (screen_flare) as the pop-up opens.
- **Ambience:** Arrival in the treasure ship: the reward scene of the film.
- **Materials:** Timber, gold, cloth ribbon.
- **Variants:** 26 pictures: oew_popup (1370x780), 8 tier titles (690x371), 2 large titles with 10 FREE SPINS (1291x549 and 1413x450), 2 lines of small text, 2 symbol pairs, 3 chest titles (297x148), ACTIVE, a plus sign, 2 flares, black and white fades.
- **Motion:** Skeletons 10_free_spins and 10_oew_free_spins (Spine 4.1.24, 21 and 22 bones, 18 and 19 slots, 16 animations: `collect_0`, `collect_6` to higher numbers, each also as `_wheel_inactive`, 1.7 s). Not drawn here. Free spins were not reached in the played session.
- **Construction:** One backdrop and one rig serve every tier and both bonuses by swapping title pictures.
- **Notes:** No separate free-spins background was loaded in the capture; whether the bonus plays in another scene is not known.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 38% · saturation 71% · contrast 67% · warm 82% / cool 15% · brighter towards: top-right (9), top (7), top-left (1)
- **Palette (measured):** #160f0a black 24%, #552610 brown 16%, #d06f15 orange 10%, #974710 brown 10%, #f9ea0d gold 5%, #f7a509 orange 5%


## Effects

Frame sequences, glows, particles and transitions.

### Reel anticipation and landing effects

`reel-anticipation` · atlas · 4 parts · largest 238×483 · sheet `sheets/reel-anticipation.webp`

- **Role:** The light on a reel that may complete a feature, and the puff when a bonus lands.
- **Subject:** A cyan neon frame the height of a reel, its blurred twin, a white vertical light streak, and a small spray of gold coins.
- **Style:** Plain glow effects.
- **Rendering:** Soft-edged light shapes (the measure counts 91% soft edges); the coins are tiny painted discs.
- **Colour:** Measured: bright, vivid, 72% cool. Cyan #0cceff 68% and #42daff 4%, white #e5e5e5 9%, orange #f6a022 6%.
- **Lighting:** It is the light: cold blue against the warm board.
- **Ambience:** Tension: the one moment the board turns cold.
- **Materials:** Neon light.
- **Variants:** 4 pictures: anticipation_border_full and _glow (238x483), light (123x338), bonus_land_leaf (97x251; coins, despite the name).
- **Motion:** Skeletons anticipation (Spine 4.1.24; `during_spin` 0.7 s, `lands` 1.7 s), anticipation_sym_anim (1.0 s) and bonus_land_effect (31 bones, 24 slots, 0.7 s: the coin spray). Seen in the game screens as a cyan frame round the last reel.
- **Construction:** Two stacked glow layers on a small rig; the coin spray is one picture on many bones.
- **Notes:** Cyan is reserved for anticipation and for One-Eyed Willy Spins: a consistent signal colour.
- **Measured:** bright, vivid, cool, medium contrast, glow or soft effect · brightness 66% · saturation 77% · contrast 30% · warm 11% / cool 72%
- **Palette (measured):** #0cceff cyan 68%, #e5e5e5 white 9%, #f6a022 orange 6%, #42daff cyan 4%, #232323 grey 4%, #fee840 gold 3%

### Transition

`transition` · atlas · 5 parts · largest 1600×1600 · sheet `sheets/transition.webp`

- **Role:** The wipe between the base game and the bonuses.
- **Subject:** A full-screen colour frame in cyan and in orange with a darker middle, a white flash, and Willy's head in his hat as a glass-like figure in blue and in gold.
- **Style:** Flat colour and one emblem: the simplest pictures in the game.
- **Rendering:** Soft-edged colour fields; the head is a monochrome version of the painted head with a glow.
- **Colour:** Measured: 34% warm and 34% cool. White #ffffff 33%, cyan #07b0d4 21%, orange #d47807 21%, brown #743501 12%, dark cyan #016870 10%.
- **Lighting:** The screen floods with one colour.
- **Ambience:** Cold for one direction, warm for the other.
- **Materials:** Light, glass.
- **Variants:** transition_bg1 and transition_bg2 (1600x1600), white (1600x1600), transition_skull and map_willy_glow (297x344).
- **Motion:** Skeleton transition (Spine 4.1.24, 4 bones, 3 slots): `freespins` and `main`, 1.8 s each. Not drawn here; not reached in play.
- **Construction:** Three stretched layers and one emblem.
- **Notes:** The mascot's head doubles as the transition mark.
- **Measured:** bright, vivid, warm and cool mixed, low contrast, hard-edged, strong highlights · brightness 63% · saturation 66% · contrast 24% · warm 34% / cool 34%
- **Palette (measured):** #ffffff light green 33%, #07b0d4 cyan 21%, #d47807 orange 21%, #743501 brown 12%, #016870 dark cyan 10%, #018799 cyan 2%

### Win blast

`win-blast` · atlas · 26 parts · largest 572×540 · sheet `sheets/win-blast.webp`

- **Role:** The burst over a winning symbol.
- **Subject:** A red-orange explosion of shards from the middle of a cell, a field of orange sparks, and a white-gold glow in the shape of a cell.
- **Style:** Flat cartoon explosion.
- **Rendering:** Hard-edged red shapes with no shading; soft sparks and glow for additive blending.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Red #ff3503 29%, black-brown #290b01 25%, brown #6c2f06 12%, gold #fec915 12%, light gold #fffdf4 8%.
- **Lighting:** It is the light.
- **Ambience:** A firecracker on each win.
- **Materials:** Fire.
- **Variants:** 26 pictures: 24 frames of `explosion` (340x310), winblast_particles (572x540), winblast_sym_glow1 (320x300).
- **Motion:** Frame sequence `explosion`, 24 frames in 1.0 s, in skeleton winblast_symbol_explosion (Spine 4.1.24). Its animation is named `genie_hammer_hit`, which looks carried over from another game (inference).
- **Construction:** A frame sequence with a glow under it.
- **Notes:** The dynamite explosion looks like the same 24 shapes on black.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 41% · saturation 84% · contrast 43% · warm 100% / cool 0%
- **Palette (measured):** #ff3503 red 29%, #290b01 black 25%, #6c2f06 brown 12%, #fec915 gold 12%, #fffdf4 light gold 8%, #9d6224 brown 4%

### Collect Boost glows

`modifier-collect-boost` · atlas · 4 parts · largest 1536×946 · sheet `sheets/modifier-collect-boost.webp`

- **Role:** The light that marks a symbol being upgraded, and the tall tile it turns into (folders `modifier_collect_boost` and `modifier_add_collect_expand`, loaded during play).
- **Subject:** Three pale gold glows: the size of a cell, of a tall four-row reel, and of the whole board; and a four-row gold Willy tile without its banner.
- **Style:** Plain light.
- **Rendering:** Soft-edged pale yellow with an orange rim.
- **Colour:** Measured: bright, 100% warm, high contrast. Light gold #fff894 41% and #feffeb 28%, black #190c01 10%, orange #edb744 6% and #b87116 6%.
- **Lighting:** It is the light: the game's gold at its brightest.
- **Ambience:** A flash of fortune.
- **Materials:** Light.
- **Variants:** sym_upgrade_glow (388x363), sym_upgrade_glow_expanded (383x867), sym_upgrade_glow_full_reel (1536x946), modifier_collect_expand_sym (215x720).
- **Motion:** Skeleton symbol_upgrade_effect (Spine 4.1). Not drawn here. A gold flash of this shape is in the game screens where Willy expands.
- **Construction:** One glow in three sizes.
- **Notes:** Three sizes of one glow rather than one stretched picture: sharper edges at each size.
- **Measured:** bright, saturated, warm, high contrast, hard-edged, strong highlights · brightness 78% · saturation 46% · contrast 86% · warm 100% / cool 0%
- **Palette (measured):** #fff894 light gold 41%, #feffeb light gold 28%, #190c01 black 10%, #edb744 orange 6%, #b87116 orange 6%, #723603 brown 5%

### Count-up lights

`count-up` · atlas · 3 parts · largest 1260×840 · sheet `sheets/count-up.webp`

- **Role:** The flares behind the win amount as it counts up.
- **Subject:** A wide field of orange sparks, a ring of beads round a soft sun, and a star flare.
- **Style:** Plain glow effects.
- **Rendering:** Soft additive light on black.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Brown #6d270d 28%, black-brown #280c07 24%, orange-brown #a94711 19%, orange #df7619 14% and #faad2b 8%.
- **Lighting:** It is the light.
- **Ambience:** Gold catching the lantern.
- **Materials:** Light.
- **Variants:** countup_sparkles (1260x840), countup_flare (395x395), intro_flare (382x382).
- **Motion:** Skeleton count_up (Spine 4.1.24, 5 bones, 4 slots): `intro` 0.7 s, `loop` 1.0 s.
- **Construction:** Three additive layers.
- **Notes:** The spark field looks the same as the big win's bw_flare2 (both 1260x840) at sheet size.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 32% · saturation 84% · contrast 53% · warm 100% / cool 0%
- **Palette (measured):** #6d270d brown 28%, #280c07 black 24%, #a94711 brown 19%, #df7619 orange 14%, #faad2b orange 8%, #fefae9 light gold 2%

### Burning value plate

`symbol-anticipation-flame` · atlas · 30 parts · largest 334×188 · sheet `sheets/symbol-anticipation-flame.webp`

- **Role:** The flame round a coin symbol's value plate.
- **Subject:** A rectangle of yellow fire, slightly wider than the plate.
- **Style:** Hand-finished fire line.
- **Rendering:** A bright yellow line with a flicker and an orange bloom on black.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Orange-gold #c39627 32%, gold #f4ed60 22%, black-brown #331d07 22%, brown #7d4b12 16%.
- **Lighting:** It is the light.
- **Ambience:** The prize heating up.
- **Materials:** Fire.
- **Variants:** 30 frames, 334x188 (files numbered 000 to 058 in twos).
- **Motion:** Frame sequence `bttn2_anticipation`, 30 frames in 1.0 s, in skeleton sym_pot_anim (`sym_pot_anim` and a loop).
- **Construction:** A frame sequence on one bone.
- **Notes:** Every second frame of a 60-frame render was shipped.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 52% · saturation 76% · contrast 61% · warm 100% / cool 0%
- **Palette (measured):** #c39627 orange 32%, #f4ed60 gold 22%, #331d07 black 22%, #7d4b12 brown 16%, #fefeb5 light gold 3%, #9a6518 brown 3%

### Collect lock and cracks

`collect-lock` · atlas · 3 parts · largest 296×271 · sheet `sheets/collect-lock.webp`

- **Role:** Effects on a prize cell that is held: chains across it, a green flash, cracks (folder `sym_lock`, loaded during play).
- **Subject:** A cell-sized frame of rusty chain crossed corner to corner over a mossy edge, a bright green square glow, and white cracks like lightning.
- **Style:** Painted prop for the chain; plain light for the rest.
- **Rendering:** The chain is fully painted iron with orange rust and highlights; glow and cracks are soft white-green shapes.
- **Colour:** Measured: bright, 21% warm and 39% cool. Green #53ff60 29%, light green #e6ffd9 20%, green #00ff29 13%, brown #4c3d1d 8% and #825b31 6% (the chain).
- **Lighting:** The green glow is the light; the chain is lit from the top left.
- **Ambience:** A cursed lock on the treasure.
- **Materials:** Rusted iron, moss, green light.
- **Variants:** streak_collect_chain (215x180), stack_collect_glow (296x271), stack_collect_cracks (242x212).
- **Motion:** Skeleton sym_lock_effect (Spine 4.1.24, 4 bones, 3 slots): one animation of 1.3 s. Seen in the game screens as chains over coin cells while Willy collects.
- **Construction:** A cell overlay with two additive layers.
- **Notes:** Acid green is kept for this and the Mystery Symbol: the colour of the curse.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 71% · saturation 56% · contrast 37% · warm 21% / cool 39%
- **Palette (measured):** #53ff60 green 29%, #e6ffd9 light green 20%, #00ff29 green 13%, #98ff9a light green 12%, #4c3d1d brown 8%, #825b31 brown 6%

### One-Eyed Willy anticipation

`willy-reel-anticipation` · atlas · 3 parts · largest 406×899 · sheet `sheets/willy-reel-anticipation.webp`

- **Role:** The frame that lights a reel when the collector symbol may land.
- **Subject:** A tall red-orange neon frame in two sizes and an orange smoky wisp.
- **Style:** Plain glow effects.
- **Rendering:** Soft additive light.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Red #ff0b00 37%, orange #ff913a 35%, light orange #ffc253 12%, #ff6004 9%.
- **Lighting:** It is the light.
- **Ambience:** Heat and danger: the warm counterpart of the cyan anticipation frame.
- **Materials:** Fire light.
- **Variants:** 3 pictures: sym15_willy_ant (306x806), sym15_willy_ant2 (406x899), sym15_willy_ant_wisp (218x316).
- **Motion:** Skeleton willy_ant (Spine 4.1.24, 4 bones, 3 slots): `animation` 1.0 s, `animation_collect` 1.3 s. Not drawn here.
- **Construction:** Two frames and a wisp on a small rig.
- **Notes:** First sorted under characters by its name; it is an effect.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 51% · saturation 83% · contrast 43% · warm 100% / cool 0%
- **Palette (measured):** #ff0b00 red 37%, #ff913a orange 35%, #ffc253 orange 12%, #ff6004 orange 9%, #ffe5cc light orange 5%, #ffd292 light orange 2%

### Cave-in rocks

`modifier-cave-in-rocks` · atlas · 7 parts · largest 107×113 · sheet `sheets/modifier-cave-in-rocks.webp`

- **Role:** The rocks that fall in the Cave In modifier.
- **Subject:** Seven brown stones, each already smeared by motion blur.
- **Style:** Painted rocks, kept dull.
- **Rendering:** Soft blurred edges, two or three tones.
- **Colour:** Measured: dark, saturated, 100% warm. Dark red-brown #342520 70%, brown #614d45 16%, grey #9d8b83 12%.
- **Lighting:** None of their own.
- **Ambience:** Dust and danger.
- **Materials:** Stone.
- **Variants:** 7 pictures, 38x49 to 107x113.
- **Motion:** No skeleton names them: particles thrown by the client (inference).
- **Construction:** Loose particle pictures.
- **Notes:** Not seen in play.
- **Measured:** dark, saturated, warm, medium contrast · brightness 24% · saturation 34% · contrast 52% · warm 100% / cool 0% · brighter towards: top-right (3), bottom-right (1)
- **Palette (measured):** #342520 dark red 70%, #614d45 brown 16%, #9d8b83 grey 12%, #cdb09c orange 2%

### Dynamite

`modifier-dynamite` · atlas · 21 parts · largest 831×508 · sheet `sheets/modifier-dynamite.webp`

- **Role:** The stick thrown onto the reels in the Dynamite modifier.
- **Subject:** A red dynamite stick with faint lettering and a burning fuse, turning end over end; a cloud of tan dust; a white-orange glow in the shape of a cell.
- **Style:** Painted prop with a white-hot spark.
- **Rendering:** The stick has a paper-wrap texture and one highlight; the spark is a plain white disc with an orange halo.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Light orange #fad689 30%, dark red #762819 21%, orange #f98217 17%, tan #bf8146 11%, red #dc461a 6%.
- **Lighting:** The spark and the cell glow.
- **Ambience:** Slapstick danger.
- **Materials:** Paper, fuse, dust.
- **Variants:** 21 pictures: 19 frames of the stick (58x188 to 99x161), dyn_falling_dust (831x508), dynamite_sym_glow (323x324).
- **Motion:** Frame sequence `dynamite`, 19 frames. Skeletons dynamite_symbol (0.8 s), dynamite_triggers (1.3 s) and modifier_dynamite_falling_dust (17 bones, 3.7 s). Not drawn here; not seen in play.
- **Construction:** A frame sequence for the tumbling stick, a rig for the dust.
- **Notes:** Trimmed frames of different sizes: the turn is in the frames, the flight in the rig.
- **Measured:** mid-tone, vivid, warm, medium contrast, strong highlights · brightness 57% · saturation 66% · contrast 51% · warm 100% / cool 0% · brighter towards: top-left (14), top-right (4), top (2)
- **Palette (measured):** #fad689 light orange 30%, #762819 dark red 21%, #f98217 orange 17%, #bf8146 orange 11%, #dc461a red 6%, #f6a350 orange 4%

### Dynamite explosion

`dynamite-explosion` · atlas · 24 parts · largest 340×310 · sheet `sheets/dynamite-explosion.webp`

- **Role:** The blast where a stick lands.
- **Subject:** The win blast's red-orange burst on a black ground.
- **Style:** Flat cartoon explosion.
- **Rendering:** Hard red shapes on black, for additive blending.
- **Colour:** Measured: dark, vivid, 92% warm. Black #0d0301 44%, dark red #6e1903 22%, red #be2f05 13%, orange-gold #febe14 11%.
- **Lighting:** It is the light.
- **Ambience:** A bang.
- **Materials:** Fire.
- **Variants:** 24 frames, 340x310.
- **Motion:** Frame sequence `dynamite_explosion`, 24 frames, used by the two dynamite skeletons.
- **Construction:** A frame sequence.
- **Notes:** The shapes look the same as the win blast's at sheet size: shipped a second time, on black.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 21% · saturation 70% · contrast 16% · warm 92% / cool 0%
- **Palette (measured):** #0d0301 black 44%, #6e1903 dark red 22%, #be2f05 red 13%, #febe14 orange 11%, #ed4b07 orange 7%, #f7830e orange 4%


## Game interface

Buttons, counters and panels drawn for this game.

### Expand Collect stepper

`expand-collect-stepper` · atlas · 3 parts · largest 270×825 · sheet `sheets/expand-collect-stepper.webp`

- **Role:** A marker on a reel for the Collect Expand feature (folder `win_stepper`, loaded during play).
- **Subject:** A tall cyan neon frame, a ghostly cyan Willy head trailing downward like a comet, and three cyan chevrons pointing down.
- **Style:** Neon interface light.
- **Rendering:** Soft additive glow; the head is the mascot's silhouette in one colour.
- **Colour:** Measured: bright, vivid, 100% cool. Cyan #22f2ff 51%, light cyan #bbf4f8 15%, #40b6c6 12%, dark cyan #0c5c76 10%.
- **Lighting:** It is the light.
- **Ambience:** A cold ghost passing down the reel.
- **Materials:** Light.
- **Variants:** expand_collect_frame (270x825), expand_collect_willy (236x743), expand_collect_arrows (270x613).
- **Motion:** Skeleton win_stepper (Spine 4.1.24, 5 bones, 3 slots): `step_up` and `step_down`, 0.7 s. Not drawn here; not seen in play.
- **Construction:** Three additive layers on a small rig.
- **Notes:** Cyan again as the signal colour for something about to happen.
- **Measured:** bright, vivid, cool, medium contrast, glow or soft effect, strong highlights · brightness 71% · saturation 72% · contrast 35% · warm 0% / cool 100% · brighter towards: bottom (1)
- **Palette (measured):** #22f2ff cyan 51%, #bbf4f8 light cyan 15%, #40b6c6 cyan 12%, #0c5c76 dark cyan 10%, #7ce9f1 cyan 8%

### Top messages

`top-messages` · atlas · 3 parts · largest 351×196 · sheet `sheets/top-messages.webp`

- **Role:** Three small promotional cards the game rotates on screen.
- **Subject:** 3 OR MORE AWARDS TREASURE SPINS over three bonus tiles; WIN UP TO 10,000x; COLLECTS ALL PRIZES beside the Willy symbol.
- **Style:** Miniature posters in the game's lettering styles.
- **Rendering:** Fat outlined gradient words (gold, orange, blue, silver-white) mixed with tiny copies of the symbols.
- **Colour:** Measured: mid-tone, vivid, 73% warm and 27% cool. Orange #f39005 20%, black #070608 10%, gold #f8df06 9%, blue #0396f3 8%, brown #6b280e 8%.
- **Lighting:** Flat.
- **Ambience:** Selling the features while the reels idle.
- **Materials:** Enamel lettering.
- **Variants:** 3 cards, 351x196 each.
- **Motion:** No skeleton names them.
- **Construction:** Each card is one flat picture with the text painted in.
- **Notes:** The figure 10,000x is as the card states it.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 49% · saturation 73% · contrast 91% · warm 73% / cool 27% · brighter towards: top-left (1), top-right (1)
- **Palette (measured):** #f39005 orange 20%, #070608 black 10%, #f8df06 gold 9%, #0396f3 blue 8%, #6b280e brown 8%, #bf550b orange 7%

### Power Play: the game's own panels

`power-play-panel` · atlas · 6 parts · largest 1310×720 · sheet `sheets/power-play-panel.webp`

- **Role:** The pop-ups and buttons of the Power Play side bet as dressed for this game.
- **Subject:** Two boards of dark wooden planks with gold italic headings: POWER PLAY UNLOCKED! ACTIVATE FOR MORE WAYS TO WIN BIG! with the skull key, and POWER PLAY ONLY ... ACTIVE, POWER STAKE, GUARANTEED UPGRADE EVERY BONUS with the bonus tiles, Willy and the three chests. Round green minus and plus buttons with gold rims, lit and unlit.
- **Style:** Game art in the cave's palette, wrapped round Blueprint's shared Power Play feature.
- **Rendering:** Painted plank texture with a vignette; headings are slanted gold-gradient capitals with a dark outline; buttons are glossy domes.
- **Colour:** Measured: dark, vivid, 98% warm. Brown #3f1b0d 57% and #824521 19%. Green appears only on the buttons.
- **Lighting:** Even; the gold lettering is the brightest thing on each board.
- **Ambience:** A notice nailed to the ship's planking.
- **Materials:** Wood, gold lettering, enamel buttons.
- **Variants:** popup_unlock_powerplay_ml and popup_power_play_ml (1310x720 each), 4 buttons (188x152: minus and plus, on and off).
- **Motion:** No skeleton of the game names them; the shared Power Play skeletons (Spine 3.8) animate the feature's own art, which is listed under the provider's interface.
- **Construction:** Whole-screen panels with the text painted in (`_ml` in the name marks a picture that carries language).
- **Notes:** The switch on the reel screen itself was not captured as a picture.
- **Measured:** dark, vivid, warm, high contrast, hard-edged · brightness 28% · saturation 74% · contrast 70% · warm 98% / cool 1% · brighter towards: top (4)
- **Palette (measured):** #3f1b0d brown 57%, #824521 brown 19%

### Jackpot plates: MINI, MINOR, MAJOR, MEGA

`jackpot-pots` · atlas · 12 parts · largest 388×217 · sheet `sheets/jackpot-pots.webp`

- **Role:** The four jackpot value plates.
- **Subject:** Four wooden-framed plates of rising size with a coloured, worn metal face (yellow, green, blue-grey, orange), four words in matching colours and four neon outlines.
- **Style:** Painted game interface in the cave's materials.
- **Rendering:** A rough timber frame with nail heads around a brushed, scratched coloured plate; words are fat bevelled block capitals, each in its pot colour; highlights are single-colour neon rectangles.
- **Colour:** Measured: mid-tone, vivid, 74% warm and 20% cool. Brown #542f1b 20%, orange #d8711d 8%, gold #fcbc03 7%, cyan #02b8ff 6%, red #ff0f00 6%, green #30fd00 4%. One colour per pot: MINI yellow, MINOR green, MAJOR blue, MEGA red-orange.
- **Lighting:** Flat front light; the neon outline is the win state.
- **Ambience:** Prize boards on a ship's wall.
- **Materials:** Timber, painted metal, neon.
- **Variants:** 4 plates (panel_1 247x131 to panel_4 330x171), 4 words (266x82), 4 highlights: 12 pictures.
- **Motion:** Skeleton pots, and portrait_pots (Spine 4.1.24, 22 and 21 bones, 16 slots): one 0.6 s animation per pot and `all_anim`. Not drawn here.
- **Construction:** Plate, word and highlight as three layers per pot; the values are live text in the pot font.
- **Notes:** The plates were not on the base-game screen in the played session; where they appear was not seen.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 46% · saturation 72% · contrast 55% · warm 74% / cool 20% · brighter towards: top (5), top-left (2)
- **Palette (measured):** #542f1b brown 20%, #160d06 black 8%, #d8711d orange 8%, #fcbc03 orange 7%, #02b8ff cyan 6%, #ff0f00 red 6%

### WAYS

`ways-counter` · atlas · 1 parts · largest 245×118 · sheet `sheets/ways-counter.webp`

- **Role:** The label of the ways-to-win counter.
- **Subject:** The word WAYS in gold pirate lettering.
- **Style:** Storybook pirate serif with curled, pointed terminals.
- **Rendering:** Glossy yellow-gold faces with a brown bevel and a dark outline.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Gold #f8eb0c 31%, brown #bf7201 22% and #6c2800 19%, black #040100 10%, light gold #fdfb75 10%.
- **Lighting:** Top light, strong highlights.
- **Ambience:** Treasure-map heading.
- **Materials:** Polished gold.
- **Variants:** One picture, 245x118.
- **Motion:** Skeleton ways_counter_anim (Spine 4.1.24, 8 bones, 5 slots) only sets the layout for 1 to 4 digits; no timed motion.
- **Construction:** A word picture beside live digits in the ways font.
- **Notes:** The counter was not seen in the played session.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 57% · saturation 85% · contrast 96% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #f8eb0c gold 31%, #bf7201 brown 22%, #6c2800 brown 19%, #040100 black 10%, #fdfb75 gold 10%, #ecaf04 orange 6%

### SPIN

`free-spins-counter` · atlas · 1 parts · largest 199×89 · sheet `sheets/free-spins-counter.webp`

- **Role:** The label of the free spins counter.
- **Subject:** The word SPIN in fat gold block capitals.
- **Style:** Comic block lettering, the same family as the chest titles.
- **Rendering:** Yellow-to-orange gradient faces, brown extrusion, dark outline.
- **Colour:** Measured: mid-tone, vivid, 100% warm. Gold #f8da00 37%, orange #fc8f00 31%, brown #bc6b00 18% and #6a2600 12%.
- **Lighting:** Top light.
- **Ambience:** Arcade-bright.
- **Materials:** Enamel.
- **Variants:** One picture, 199x89.
- **Motion:** None.
- **Construction:** A word picture beside live digits in the free spins counter font.
- **Notes:** Free spins were not reached, so the counter was not seen in place.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 60% · saturation 98% · contrast 74% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #f8da00 gold 37%, #fc8f00 orange 31%, #bc6b00 brown 18%, #6a2600 brown 12%, #040100 black 2%


## Typography

Embedded fonts and lettering.

### Pot font

`pot-font` · atlas · 1 parts · largest 512×256 · sheet `sheets/pot-font.webp`

- **Role:** Digits for the jackpot plates.
- **Subject:** 0 to 9, x, a full stop and a comma in a curly pirate serif.
- **Style:** Storybook pirate serif.
- **Rendering:** Orange faces with a lighter inner bevel and a dark brown outline.
- **Colour:** Measured: 100% warm. Orange #f5a937 33%, black-brown #271200 25%, orange-brown #b8590b 24%, #e47b19 9%.
- **Lighting:** Soft top light.
- **Ambience:** Treasure-map numerals.
- **Materials:** Carved, painted wood.
- **Variants:** One bitmap font page, 512x256, with a BMFont .xml beside it.
- **Motion:** None.
- **Construction:** A bitmap font: glyphs on one page, placed by the .xml.
- **Notes:** Same family as the ways font and the ticket font.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 44% · saturation 85% · contrast 77% · warm 100% / cool 0%
- **Palette (measured):** #f5a937 orange 33%, #271200 black 25%, #b8590b orange 24%, #e47b19 orange 9%, #6f3200 brown 5%, #fedf7e gold 4%

### Ways font

`ways-font` · atlas · 1 parts · largest 283×367 · sheet `sheets/ways-font.webp`

- **Role:** Digits for the ways counter.
- **Subject:** 0 to 9, comma and full stop in the pirate serif.
- **Style:** Storybook pirate serif with sharp, split terminals.
- **Rendering:** Glossy yellow-gold with a white top glint, brown bevel and dark outline.
- **Colour:** Measured: 100% warm. Gold #f8e70b 30%, brown #6d2a00 20% and #c07502 20%, light gold #fdfb75 10%.
- **Lighting:** Top light, strong highlights.
- **Ambience:** Polished treasure.
- **Materials:** Gold.
- **Variants:** One page, 283x367, with its .xml.
- **Motion:** None.
- **Construction:** A bitmap font.
- **Notes:** Matches the WAYS word picture.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 56% · saturation 86% · contrast 96% · warm 100% / cool 0%
- **Palette (measured):** #f8e70b gold 30%, #6d2a00 brown 20%, #c07502 brown 20%, #fdfb75 gold 10%, #060200 black 10%, #e4ae09 gold 7%

### Count-up font

`count-up-font` · atlas · 1 parts · largest 853×958 · sheet `sheets/count-up-font.webp`

- **Role:** Digits of the win amount as it counts up.
- **Subject:** 0 to 9, comma and full stop as heavy, angular slab numerals.
- **Style:** Blocky faceted numerals, cut like stone or cast metal; a different family from the pirate serif.
- **Rendering:** A gold gradient face with a fine hatched edge texture, a bright bevel, a red-brown extrusion below and a dark outline.
- **Colour:** Measured: 100% warm. Gold #fcd95e 28%, orange #ee9a22 22%, black-brown #180300 16%, brown #a15114 13%, dark red #631504 13%.
- **Lighting:** Top light; the extrusion is in shadow.
- **Ambience:** Weight and money.
- **Materials:** Cast gold.
- **Variants:** One page, 853x958 (glyphs about 200 px tall), with its .xml.
- **Motion:** None of its own; skeleton count_up brings the number in.
- **Construction:** A bitmap font.
- **Notes:** The largest type in the game.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 50% · saturation 78% · contrast 90% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #fcd95e gold 28%, #ee9a22 orange 22%, #180300 black 16%, #a15114 brown 13%, #631504 dark red 13%, #d09e5e orange 5%

### Big win font

`big-win-font` · atlas · 1 parts · largest 512×512 · sheet `sheets/big-win-font.webp`

- **Role:** Digits of the amount on the big win banner.
- **Subject:** 0 to 9, comma and full stop: the count-up numerals at a smaller size.
- **Style:** As the count-up font.
- **Rendering:** As the count-up font.
- **Colour:** Measured: 100% warm. Gold #fcd95b 31%, orange #ee9b22 25%, black-brown #360801 19%, brown #97350a 11%.
- **Lighting:** Top light.
- **Ambience:** Weight and money.
- **Materials:** Cast gold.
- **Variants:** One page, 512x512, with its .xml.
- **Motion:** None.
- **Construction:** A bitmap font.
- **Notes:** One design at two sizes rather than one scaled page.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 54% · saturation 80% · contrast 86% · warm 100% / cool 0%
- **Palette (measured):** #fcd95b gold 31%, #ee9b22 orange 25%, #360801 black 19%, #97350a brown 11%, #cf9e57 orange 6%, #a96d24 orange 4%

### Ticket font

`ticket-font` · atlas · 1 parts · largest 186×203 · sheet `sheets/ticket-font.webp`

- **Role:** Digits of the money values on the coin symbols.
- **Subject:** 0 to 9, comma and full stop in the pirate serif, small.
- **Style:** Storybook pirate serif.
- **Rendering:** Orange-gold faces with a light bevel and dark outline, drawn to hold at about 40 px tall.
- **Colour:** Measured: 100% warm. Orange #f6770b 36% and #f5b23d 24%, black-brown #1e0e00 17%, gold #fde276 10%.
- **Lighting:** Top light.
- **Ambience:** Engraved value.
- **Materials:** Gold.
- **Variants:** One page, 186x203, with its .xml.
- **Motion:** None.
- **Construction:** A bitmap font.
- **Notes:** The values on the cash coins in the game screens are set in it.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 52% · saturation 83% · contrast 85% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #f6770b orange 36%, #f5b23d orange 24%, #1e0e00 black 17%, #fde276 gold 10%, #c1601b orange 9%, #7d3800 brown 3%

### Power Play feature font

`power-play-feature-font` · atlas · 1 parts · largest 297×334 · sheet `sheets/power-play-feature-font.webp`

- **Role:** Digits and the currency sign for the Power Play stake.
- **Subject:** 0 to 9, $, X, comma and full stop in a rounded italic sans.
- **Style:** Rounded, glossy, modern: the shared feature's look, not the cave's.
- **Rendering:** Orange gradient with a pale top glint, a light inner line and a brown outline.
- **Colour:** Measured: 100% warm. Orange #f6910f 33% and #f9c43a 24%, brown #582004 14%, light gold #fefcb0 11%.
- **Lighting:** Top light, strong highlights.
- **Ambience:** Arcade.
- **Materials:** Enamel.
- **Variants:** One page, 297x334, with its .xml.
- **Motion:** None.
- **Construction:** A bitmap font.
- **Notes:** It ships a dollar sign although the demo played in pounds.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 61% · saturation 77% · contrast 83% · warm 100% / cool 0%
- **Palette (measured):** #f6910f orange 33%, #f9c43a orange 24%, #582004 brown 14%, #fefcb0 light gold 11%, #a95f1a orange 7%, #fcea71 gold 6%

### Treasure Wheel mystery win font

`treasure-wheel-font` · atlas · 1 parts · largest 306×366 · sheet `sheets/treasure-wheel-font.webp`

- **Role:** Digits of the mystery win on the Treasure Wheel.
- **Subject:** 0 to 9, comma and full stop as angular block numerals.
- **Style:** The count-up family, flatter.
- **Rendering:** A red-to-yellow vertical gradient with a thin white edge, a dark red extrusion and black outline.
- **Colour:** Measured: 100% warm. Gold #fecb01 29%, orange #fe6a02 26%, black #0f0b0a 17%, brown #772305 11%.
- **Lighting:** From below: the yellow is at the bottom of each glyph.
- **Ambience:** Fire.
- **Materials:** Enamel.
- **Variants:** One page, 306x366, with its .xml.
- **Motion:** None.
- **Construction:** A bitmap font.
- **Notes:** The wheel was not reached in play.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 48% · saturation 78% · contrast 85% · warm 100% / cool 0%
- **Palette (measured):** #fecb01 gold 29%, #fe6a02 orange 26%, #0f0b0a black 17%, #772305 brown 11%, #442b19 brown 4%

### Free spins pop-up font

`free-spins-popup-font` · atlas · 1 parts · largest 716×1175 · sheet `sheets/free-spins-popup-font.webp`

- **Role:** The number of spins on the free spins pop-ups.
- **Subject:** 0 to 9 as angular block numerals.
- **Style:** The count-up family in silver.
- **Rendering:** A white-to-grey gradient face with a white bevel, black extrusion and a cyan outer glow.
- **Colour:** Measured: bright, muted, 100% cool. White #f7f7f7 32%, greys #cacbcb 19% and #9ea0a0 13%, black #040a0b 9%, cyan #03b0ca 9%.
- **Lighting:** Top light; cyan glow all round.
- **Ambience:** Cold steel against the warm pop-up: the number is the one cool thing on it.
- **Materials:** Brushed steel.
- **Variants:** One page, 716x1175 (glyphs about 180 px tall), with its .xml.
- **Motion:** None.
- **Construction:** A bitmap font.
- **Notes:** The only cool-coloured type in the game.
- **Measured:** bright, muted, cool, high contrast, strong highlights · brightness 66% · saturation 19% · contrast 98% · warm 0% / cool 100%
- **Palette (measured):** #f7f7f7 white 32%, #cacbcb grey 19%, #9ea0a0 grey 13%, #040a0b black 9%, #03b0ca cyan 9%, #27393c dark cyan 7%

### Free spins counter font

`free-spins-counter-font` · atlas · 1 parts · largest 352×406 · sheet `sheets/free-spins-counter-font.webp`

- **Role:** Digits of the spins counter during free spins.
- **Subject:** 0 to 9, a slash, comma and full stop as angular block numerals.
- **Style:** The count-up family in silver, smaller.
- **Rendering:** White-to-grey gradient, white bevel, black extrusion; no glow.
- **Colour:** Measured: bright, muted, neutral. White #f8f8f8 35%, greys #9a9a9a 25% and #d0d0d0 13%, black #050505 16%.
- **Lighting:** Top light.
- **Ambience:** Neutral, readable.
- **Materials:** Brushed steel.
- **Variants:** One page, 352x406, with its .xml.
- **Motion:** None.
- **Construction:** A bitmap font.
- **Notes:** The slash is for a count such as 3/10 (inference).
- **Measured:** bright, muted, neutral, high contrast, strong highlights · brightness 64% · saturation 0% · contrast 100% · warm 0% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #f8f8f8 white 35%, #9a9a9a grey 25%, #050505 black 16%, #d0d0d0 grey 13%, #5e5e5e grey 8%, #2f2f2f grey 3%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `power-play-shared`: 34 parts
- `power-play-cash-font`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Roboto Black (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 726 components cut from 726 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
