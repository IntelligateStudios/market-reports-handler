# Frankensteins Fortune: art report

whitehat · run `2026-11-27-1019-whitehat-frankensteins-fortune` · captured 2026-11-27

Source: the provider's free-play demo, https://contentrgspubst.blueprintgaming.com/Games/BP_FrankensteinsFortune95/1.7.0.0j-pZSE/index.html?playMode=demo&language=EN&currency=USD&bp_jurisdiction=zz&brand=affdemo-affiliate&affiliate=affdemo&bpdemocurrency=USD&customer=CUSTOMERLOBBY&configUrl=https%3a%2f%2ffileservicergspubst.blueprintgaming.com%2fDefault.aspx%3ffileType%3dconfig%26customer%3dCUSTOMERLOBBY%26affiliate%3daffdemo%26platform%3dDesktop%26clientFolder%3dBP_FrankensteinsFortune95%26serverType%3duat%26bp_jurisdiction%3dzz%26launchdomain%3d-1&qBridgeUrlXSS=contentrgspubst%2f%2fcom%2f%2fQBridge%2f1.14.4-pGv3%2fqBridge.js&qBridgeUrl=https%3a%2f%2fcontentrgspubst.blueprintgaming.com%2f%2fQBridge%2f1.14.4-pGv3%2fqBridge.js&serverType=uat&tld=0&game=BP_FrankensteinsFortune95&gameName=BP_FrankensteinsFortune95&assetsName=BP_FrankensteinsFortune95&platform=Desktop

**Extracted:** 1679 named components from 1233 textures in 1233 atlases; 73 Spine skeletons; 61 frame sequences (891 frames); 2 fonts. Grouped into 42 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A cartoon Frankenstein laboratory lit by acid-green electricity: a child-like monster mascot, chunky lab hardware in teal and copper, plasma-ball prizes in neon colours, and gold kept for money.

**Style.** Family-animation cartoon horror with a 3D-look painted finish. Frankie and the Bride have big heads, heavy lids and small bodies; props (hand, ray gun, control box, brain jars, specimen jars) are rounded and toy-like. Nothing is gory: stitches, bolts, brains and eyeballs are played as sweets and toys. Lettering is horror-comic: dripping green words and fat gold slabs.

**Rendering.** Smooth gradients, clean hard silhouettes, no line outlines (measured: 5% soft edge over the game's art). Detail and gloss are spent on the symbols, the jars and Frankie; backgrounds are hazy paintings kept empty in the middle. Every glow, arc and burst is a separate layer on black, added on top.

**Colour.** Measured over the game's own art: vivid (saturation 78%), mid-to-dark (brightness 36%), cool 63% against warm 12%. Black-green #0d1610 26%, dark green #296909 17%, dark blue #112e45 9%, teal #0b887d 8%, bright green #38b512 4%, purple #3b126f 3%; green is 52% of the coloured pixels. The scheme: teal fog and violet shadow for the room, acid green for electricity and light, copper for the frame, and gold with a red edge only for money (cash balls, win numerals, COLLECT). Three bonus games are told apart by colour alone, red, green and blue, and four jackpots by green, blue, magenta and red.

**Lighting.** Light comes from the things in the picture: electrode balls, plasma, liquid in jars, lightning, the storm sky. Objects are top-lit (measured: light from the top on 163 parts, top-left and top-right on about 50 each) with a coloured glow behind them. The reel backing is unlit black, so everything luminous reads against it.

**Ambience.** Spooky but cosy and funny: a Halloween cartoon, with the machine always humming. The base game is the lab at night; Cash Trail goes outside to the stormy hill and castle; Big Money is a shelf of specimen jars; Frankie Spins darkens the lab and lights only the prizes.

**Shape language.** Round and chunky: cylinders, domes, balls and fat letters. The angular shapes are lightning, thorny vines and bare trees, used for energy and for the outdoors. Frames are copper pipe or thin gold; the Collect symbol breaks the grid with a vine border.

**Materials.** Green enamelled metal, copper pipe and brass bolts, glass with coloured liquid and bubbles, plasma behind glass, stitched green skin, cloth, cork, aged wood, gold lettering and coins.

**Typography and lettering.** Display lettering is drawn art: green condensed capitals and a gold slab for the logo, dripping slime letters for WILD and IT'S ALIVE!, green slab words with a blue or dark edge for win tiers and bonus words, fat outlined words for the jackpots. Eight bitmap numeral fonts in one rounded design (gold and red for money, white for counters, teal for totals). Running text is the shell's Roboto.

**Motion.** Spine carries everything: 73 skeletons, 71 of them made in Spine 4.2.43 (six exported as 4.1; the two Power Play rigs are 3.8), from 3-bone symbol pulses (land 0.67 s, win 1.0 s) to Frankie's 138-bone expanded symbol and the 108-bone Mega Frankie. Electricity is hand-made frame sequences played inside the rigs: 61 sequences, 891 frames (arcs of 30 frames, plasma of 21, lightning of 23, win boxes of 30). Hands change pose by swapping numbered pictures. No skeleton frame is drawn in this report: the tools cannot draw Spine 4.2, so motion is read from the files and the screens.

**Variants and themes.** One design, several colours, is the rule: three brain jars, four jackpot balls, four specimen jars, jar counters in red and blue. Each paying symbol ships as a still, a win copy, a painted blur and, for Frankie Spins, a dimmed green copy and its blur at a smaller cell size. Frankie exists as a Collect tile, an expanded three-cell figure, a 2x2 to 5x5 Mega Frankie and a figure for intros. Intro screens and the trail have separate portrait rigs and, for the trail, a separate portrait painting.

**How it is built.** 1,679 named pictures from 1,233 files. Almost all art is loose PNG and JPEG files in folders named by use, with Spine JSON beside them; only the three brain jars, Mega Frankie and the level meter are packed Spine atlases. Files with words in them end in _ml, one set per language (inference from the naming). Effects are JPEG on black for additive slots. The base game loads first; each bonus game's art (373 more files) loads only when that bonus starts.

**Consistency.** Tight: one character design, one hardware family, one green. What sits outside is the Power Play and bonus wheel set, in a chrome blue and gold style with a 'Super Mode' logo placeholder, which looks like a shared template of the provider (inference; listed under the provider's interface and not read), and the big win's coins and gems, which are generic.

**What to take from it.** (1) The build read here is Blueprint Gaming's (BP_FrankensteinsFortune95), not the White Hat Studios US build the market report ranks; treat every finding as about this title's art, with the match between the two builds as inference. (2) One light source idea runs the whole game: green electricity. Arcs on the frame, win boxes, the modifier frame, plasma prizes and lightning in the jars are all the same few hand-made frame sequences, recoloured and reused. (3) Colour is the navigation: red, green and blue name the three bonus games on the meters, the symbols, the counters and the result screens, and gold is reserved for money. An artist's brief for a similar game can fix this palette logic before any asset is drawn. (4) Progress is always a physical object filling up (a brain jar, a glass tube), never an abstract bar. The jar rig, with six liquid levels, is drawn once and coloured three times. (5) The mascot is one set of about 60 body parts reused in five rigs (symbol, expanded symbol, Mega Frankie, modifier walk-on, intros). The cost is in rigging and hand poses, not in new paintings: a generated character still needs to be cut into parts like these. (6) Scene art is not economised: four full paintings at 3200x3200 (the lab, its congratulations copy, the trail in landscape and in portrait) and four more at 1600x1600, each empty where the board or the prizes sit. (7) Dimming losers instead of removing them (the green 'off' symbol set of Frankie Spins) keeps a hold-and-collect board full and on-theme for the price of one recolour per symbol.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 36% · saturation 78% · contrast 50% · warm 12% / cool 62% · brighter towards: top (163), top-right (52), top-left (51)

Palette: #0d1610 black 26%, #296909 dark green 17%, #112e45 dark blue 9%, #0b887d dark cyan 8%, #38b512 green 4%, #f1fbf5 light green 4%, #3b126f dark purple 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 3 | 27% | 81% | 65% | 6% / 82% | #0c1628 black 42%, #0b4e4f dark cyan 21%, #0b9781 cyan 14% |
| Reel board | 8 | 34% | 80% | 50% | 13% / 57% | #0b1606 black 32%, #215c07 dark green 14%, #3ba10b green 12% |
| Symbols | 8 | 43% | 83% | 46% | 41% / 43% | #09110c black 9%, #f3b60d orange 9%, #e84607 orange 6% |
| Characters | 3 | 48% | 53% | 43% | 12% / 61% | #1f4d28 dark green 19%, #131f18 black 16%, #f4fefb light cyan 9% |
| Logo and title | 1 | 56% | 62% | 90% | 21% / 54% | #36abfa blue 12%, #acf7d2 light green 11%, #0a140d black 10% |
| Win celebrations and banners | 7 | 40% | 76% | 51% | 10% / 65% | #0e1713 black 24%, #0a8883 dark cyan 10%, #387f08 dark green 9% |
| Effects | 3 | 26% | 87% | 15% | 2% / 48% | #336306 dark green 62%, #0d1a03 black 33% |
| Game interface | 5 | 37% | 44% | 56% | 28% / 38% | #101012 black 22%, #30352f grey 21%, #5d615a grey 10% |
| Typography | 2 | 67% | 42% | 88% | 29% / 22% | #fffefd light gold 38%, #080503 black 11%, #18f3de cyan 9% |
| Provider interface (shared) | 2 | 44% | 78% | 69% | 48% / 48% | #e2952c orange 18%, #0399fc blue 17%, #020416 black 11% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Big Money

`big-money-pick` · atlas · 22 parts · largest 1600×1600 · sheet `sheets/big-money-pick.webp`

- **Role:** The second stage of Cash Trail: a screen of thirteen specimen jars, each holding a multiplier of the stake from 50x to 1000x.
- **Subject:** Laboratory shelves, darkened and blurred, with cork-stoppered jars in four colours: blue with chattering teeth, red with a heart, green with a thumbs-up hand, gold with an eyeball. Frankie's head sits in the middle over the words BIG MONEY; gold multipliers stand on the jars.
- **Style:** The game's cartoon horror at its most playful: body parts as sweets in a shop.
- **Rendering:** Glossy painted jars with strong rim light and a cork texture; the backdrop is the lab repainted darker and out of focus; multipliers are fat gold numerals with a dark edge.
- **Colour:** Measured: dark teal #094037 53% (the backdrop), black #12110f 17%, brown #72551f 8%, orange #d1770b and gold #e4b71a from the multipliers.
- **Lighting:** Each jar glows in its own colour against the dark shelves; unpicked jars are replaced by a black silhouette (jar_off).
- **Ambience:** A cabinet of curiosities, treats rather than threats.
- **Materials:** Glass, cork, coloured liquid, the specimens, gold lettering.
- **Variants:** Four jars at 442x401, one off silhouette, thirteen multiplier pictures (50x to 1000x), the title, a backdrop 1600x1600 and two masks for Frankie's head.
- **Motion:** Four jar skeletons of 4 bones (active 0.67 s, idle, off) and big_money_jar_bg (81 bones, 60 slots, 3.43 s), which names the Frankie figure's parts for the head in the middle.
- **Construction:** 22 loose files. In the played round the jars went dark one after another until one stayed lit (100x).
- **Notes:** Tier is told by colour and content: gold eyeball jars hold the highest multipliers seen (500x, 1000x), green thumbs the lowest (50x to 80x).
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 27% · saturation 78% · contrast 39% · warm 27% / cool 61% · brighter towards: top (15), bottom (1)
- **Palette (measured):** #094037 dark cyan 53%, #12110f black 17%, #72551f brown 8%, #215d0f dark green 3%, #d1770b orange 3%, #e4b71a gold 2%

### Cash Trail scene

`cash-trail-scene` · atlas · 33 parts · largest 3200×3200 · sheet `sheets/cash-trail-scene.webp`

- **Role:** The first stage of the Cash Trail bonus: a board-game path of multipliers.
- **Subject:** A stone path winding up a mound, with steps from x5 to x40 and BIG MONEY at the top; the castle on a hill at the left with lit windows; bare trees, grave crosses, bats, a crow on a branch; a green storm sky with a moon and lightning.
- **Style:** Storybook horror, flatter and more graphic than the laboratory: strong silhouettes against a bright sky.
- **Rendering:** A painted scene with dark blue-violet silhouettes on a luminous mint-green sky; the multipliers are green slab numerals with a dark extrusion, laid on the path in perspective.
- **Colour:** Measured: dark, 88% cool, high contrast. Blue-black #09162c 46%, dark teal #0a5051 20%, sea green #09986a 10%, purple #310d60 6%, mint #0fd985 5% and #a6f6d6 3%.
- **Lighting:** Back-lit: the sky and the moon are the light, everything else is silhouette with a thin rim. Lightning and the castle's windows are additive layers.
- **Ambience:** Outdoors on the stormy hill, the one scene that leaves the lab.
- **Materials:** Stone, dead wood, mist.
- **Variants:** Two backdrops at 3200x3200 (landscape and portrait compositions), 20 multiplier steps (x5 to x20, x22, x25, x30, x40) at 250x160, START and BIG MONEY labels, a crow in two parts, a back view of Frankie as the playing piece.
- **Motion:** Skeleton trail, 34 bones and 31 slots, with an active and a glow animation per step (1.0 s) and active_big_money (3.0 s); the crow's head is a separate part so it can turn; trail_castle_transition (2.0 s) flashes the castle.
- **Construction:** 33 loose files; the path itself is painted into the backdrop, only the numbers are separate.
- **Notes:** A whole second background painting for one bonus stage, in a different composition for portrait: scene art is not economised here.
- **Measured:** dark, vivid, cool, high contrast, hard-edged · brightness 27% · saturation 82% · contrast 75% · warm 1% / cool 88% · brighter towards: top-right (18), top (7), top-left (1)
- **Palette (measured):** #09162c black 46%, #0a5051 dark cyan 20%, #09986a cyan 10%, #310d60 dark purple 6%, #0fd985 green 5%, #a6f6d6 light green 3%

### The laboratory

`main-background` · atlas · 1 parts · largest 3200×3200 · sheet `sheets/main-background.webp`

- **Role:** The full-screen scene behind the reels in the base game, in Frankie Spins and (blurred) on the congratulations screen. Cash Trail and Big Money have scenes of their own.
- **Subject:** A mad scientist's laboratory seen straight on: a huge teal generator with a lit screen of green lightning, four glowing green electrode balls, chains hanging from the top corners, and in front a wooden workbench with flasks of pink, green and purple liquid, open books, two bolts, a spider, melted candles, a test-tube rack, and under the bench a brain in a jar, a flask, a skull and a blue curtain.
- **Style:** Cartoon horror in a soft painted manner: friendly, rounded props, nothing gory. The machine is simplified to big clear shapes and kept hazy; the bench props are small and crisp.
- **Rendering:** Digital painting with soft airbrushed haze over the upper two thirds and sharper, more finished brushwork on the bench. No outlines. The centre is deliberately empty and low in detail, because the reel board covers it.
- **Colour:** Measured: dark and vivid, 79% cool. Black-violet #181322 39%, teal #0b8d8b 31%, deep teal #0e4b53 14%, green #129442 6% and #23a818 2%, with small warm notes of wood #6f411e and candle gold #caa43b. Teal fog over purple shadow, with acid green as the light.
- **Lighting:** Lit from inside the picture: the green electrode balls and the generator screen glow, a band of green light sits along the back of the bench, and violet falls off into the corners as a vignette. The candle adds one small warm point.
- **Ambience:** Spooky but cosy: a night-time lab humming with green electricity, more Halloween cartoon than horror film.
- **Materials:** Riveted painted metal, glass flasks with coloured liquid, aged wood, paper, wax, iron chain, cloth.
- **Variants:** One picture, 3200x3200, square so that the same file can be cropped for landscape and portrait (inference from the size; only the landscape layout was captured). The congratulations screen ships a second 3200x3200 copy of it.
- **Motion:** A still picture in the files; no animated background layer was loaded. In play the life of the scene comes from what sits on it (the jars, the electric reel frame).
- **Construction:** A single JPEG. No separate layers for the generator, the bench or the props.
- **Notes:** The busiest, warmest detail is put along the bottom edge and in the corners, where the reel board does not cover it.
- **Measured:** dark, vivid, cool, medium contrast, hard-edged · brightness 28% · saturation 81% · contrast 51% · warm 12% / cool 78% · brighter towards: top (1)
- **Palette (measured):** #181322 black 39%, #0b8d8b dark cyan 31%, #0e4b53 dark cyan 14%, #129442 green 6%, #23a818 green 2%, #6f411e brown 2%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Frankie Spins board

`frankie-spins-board` · atlas · 38 parts · largest 1432×1154 · sheet `sheets/frankie-spins-board.webp`

- **Role:** The reel board of the Frankie Spins bonus and its counters.
- **Subject:** A 5x5 grid on a dark panel inside the same copper pipe frame with bulb electrodes, a navy WINNINGS plate, a SPINS LEFT box, and the words SPIN LEFT, SPINS LEFT, ALL and PAYS in green slab letters.
- **Style:** The base board's laboratory plumbing, taller.
- **Rendering:** Smooth 3D-look copper; a near-black backing with a faint green grid; green extruded lettering as in the win tiers.
- **Colour:** Measured: dark. Black-green #06100a 52%, greens #21581f 14%, #3b983f 13%, #90d093 12% (the arc frames).
- **Lighting:** Unlit backing; the green arc and bulb glow are the only lights on it.
- **Ambience:** The lights go down for the bonus.
- **Materials:** Copper pipe, glass bulbs, dark glass, navy enamel plates with a gold edge.
- **Variants:** Board 1432x1154; plates 600x152 and 384x162; a 30-frame arc (fs_sq) and a bulb glow, copies of the base game's.
- **Motion:** Skeleton feature_reel, 8 bones, idle 2.0 s, runs the arcs.
- **Construction:** 38 loose files.
- **Notes:** Cells here are 240x190 against 290x260 in the base game: the same screen holds 25 cells by shrinking them.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 27% · saturation 61% · contrast 42% · warm 45% / cool 29% · brighter towards: top (6)
- **Palette (measured):** #06100a black 52%, #21581f dark green 14%, #3b983f green 13%, #90d093 green 12%

### Win boxes

`win-boxes` · atlas · 120 parts · largest 350×900 · sheet `sheets/win-boxes.webp`

- **Role:** The green electric outline drawn around each winning symbol.
- **Subject:** A square of green lightning tracing the cell's edge; one version three cells tall for a stacked symbol; two versions for the Bride's framed symbol.
- **Style:** Effect art, in the same green electricity as the rest.
- **Rendering:** 30-frame sequences on black for additive blending; the light runs round the edge.
- **Colour:** Measured: all green. #0e2402 42%, #2b7503 25%, #46bc07 15%, #62ea17 8%, #8ef255 7%.
- **Lighting:** Self-lit.
- **Ambience:** Marks a win without covering the symbol.
- **Materials:** Electricity.
- **Variants:** Four sequences of 30: winbox (350x300), winbox_3high (350x900), sym07_winbox and c_sym07_winbox (349x346, the second with an arched top).
- **Motion:** Two skeletons (winbox and sym07_winbox, 5 bones each) with animations winbox and winbox_3high of 1.5 s.
- **Construction:** 120 loose JPEG frames; Spine only places and times them.
- **Notes:** A dedicated three-high box exists because symbols can land stacked.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 37% · saturation 90% · contrast 52% · warm 0% / cool 50%
- **Palette (measured):** #0e2402 black 42%, #2b7503 dark green 25%, #46bc07 green 15%, #62ea17 green 8%, #8ef255 green 7%, #bcfb97 light green 3%

### The reel board

`reel-board` · atlas · 1 parts · largest 1591×936 · sheet `sheets/reel-board.webp`

- **Role:** The frame and backing of the 5x3 reels.
- **Subject:** A dark, almost black panel with four thin copper divider lines, inside a frame of polished copper pipe with flared corner joints. On each side the pipe is broken by a gap between two glass bulb electrodes, where the electric arc of the reel frame runs.
- **Style:** Clean and restrained next to the symbols: laboratory plumbing rather than ornament.
- **Rendering:** Smooth 3D-look rendering of the pipe with soft speculars; the backing is a flat dark gradient from blue-black at the top to green-black at the bottom.
- **Colour:** Measured: very dark (brightness 8%). Black #040b09 86%, copper brown #564025 10%, light copper #e3bf98 2%.
- **Lighting:** Top-lit metal with long highlights along the pipes; the backing has no light of its own, so every symbol and glow reads against it.
- **Ambience:** A dark stage: it makes the neon greens and the gold of the symbols look brighter.
- **Materials:** Polished copper pipe, glass bulbs, a dark glass or void backing.
- **Variants:** One picture, 1591x936, for the 5x3 base game. Frankie Spins has its own 5x5 board (see the Frankie Spins board).
- **Motion:** Still. The arc between the bulbs and the win boxes are separate units.
- **Construction:** One PNG with the backing and the frame together.
- **Notes:** The opaque dark backing is why the laboratory is only seen around the board.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 8% · saturation 72% · contrast 33% · warm 100% / cool 0%
- **Palette (measured):** #040b09 black 86%, #564025 brown 10%, #e3bf98 orange 2%

### Jar labels and sparks

`brain-jar-labels-and-particles` · atlas · 6 parts · largest 254×147 · sheet `sheets/brain-jar-labels-and-particles.webp`

- **Role:** The name under each jar (CASH SPINS, CASH TRAIL, FRANKIE SPINS) and the spark that flies to a jar.
- **Subject:** Three two-line word plates and three star-burst particles in blue, green and red.
- **Style:** Bold cartoon lettering; the particles are plain light bursts.
- **Rendering:** Lettering with a gradient face, a light inner edge, a dark outline and a coloured glow; particles on black for additive blending.
- **Colour:** Measured: orange #faa809 12%, gold #faed49 10%, green #0df53c 5%, dark blue #163a64 4%. CASH is gold on every plate; the second word takes the jar's colour (blue SPINS, green TRAIL), and FRANKIE is green over gold SPINS.
- **Lighting:** Flat, front-lit lettering with a top highlight.
- **Ambience:** Loud and clear, like stickers on the machine.
- **Materials:** None; pure lettering and light.
- **Variants:** Three labels at 254x147; three particles at 100x100. The same three labels are shipped again for the intro screen.
- **Motion:** Still pictures; the particle is moved by code (inference).
- **Construction:** Six loose PNG files. The file names end in _ml, which marks a picture with words in it, to be swapped per language (inference from the naming across the game).
- **Notes:** Colour alone tells the three bonus games apart everywhere in the game.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 58% · saturation 75% · contrast 78% · warm 46% / cool 37%
- **Palette (measured):** #faa809 orange 12%, #0c2b17 black 10%, #faed49 gold 10%, #f7fbee light green 9%, #0df53c green 5%, #163a64 dark blue 4%

### The blue brain jar (Cash Spins)

`brain-jar-blue` · atlas · 94 parts · largest 1008×1027 · sheet `sheets/brain-jar-blue.webp`

- **Role:** One of three feature meters standing at the left of the reels: the blue jar belongs to Cash Spins. It is the game's most elaborate rig.
- **Subject:** A glass cylinder on a green metal base with a control plate, a domed green lid with a lamp, two bolt electrodes with bulb tips, ribbed hoses at both sides, and inside a brain floating in coloured liquid with bubbles.
- **Style:** Chunky cartoon laboratory hardware, the same family as the jar symbols on the reels.
- **Rendering:** Painted parts with clean silhouettes and airbrushed gloss; liquid, bubbles, lightning and glows are separate soft layers.
- **Colour:** Measured: 91% cool. #100711 16% black, #2f0d59 14% dark purple, #39219b 14% and #1a11e1 6% blue, #6a5efe 4%. The jar's own colour is blue-violet with cyan lightning.
- **Lighting:** The brain and the liquid glow from inside; lightning forks and a large coloured halo (1008x1027) are additive layers on top. The metal is top-lit.
- **Ambience:** A specimen being charged: it gets livelier as it fills.
- **Materials:** Green enamelled metal, brass bolts, glass, coloured liquid, rubber hose.
- **Variants:** Six brain and liquid levels (brain_v1 to brain_v6, each with its own water mask, bubbles and electricity), so the jar shows how far it has filled. The blue set has cyan lightning.
- **Motion:** One Spine 4.2.43 skeleton, 68 bones and 86 slots, with hit and idle animations for states 0 to 6 (1.0 s each). A 23-frame lightning sequence (bolt, 433x276) and bubble and spark sets move inside it.
- **Construction:** A Spine atlas of two pages cut into 94 regions (the jars, Mega Frankie and the level meter are the only art the game ships packed; everything else is loose files). No frame is drawn here: the tools cannot draw Spine 4.2.
- **Notes:** The three jars are one rig coloured three times: the same 94 region names with red, green or blue in them.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 30% · saturation 73% · contrast 51% · warm 9% / cool 91% · brighter towards: top (10), top-left (3), bottom (2)
- **Palette (measured):** #100711 black 16%, #2f0d59 dark purple 14%, #39219b blue 14%, #f4fbfd light cyan 8%, #1a11e1 blue 6%, #551d0e dark red 5%

### The green brain jar (Cash Trail)

`brain-jar-green` · atlas · 94 parts · largest 1008×1027 · sheet `sheets/brain-jar-green.webp`

- **Role:** One of three feature meters standing at the left of the reels: the green jar belongs to Cash Trail. It is the game's most elaborate rig.
- **Subject:** A glass cylinder on a green metal base with a control plate, a domed green lid with a lamp, two bolt electrodes with bulb tips, ribbed hoses at both sides, and inside a brain floating in coloured liquid with bubbles.
- **Style:** Chunky cartoon laboratory hardware, the same family as the jar symbols on the reels.
- **Rendering:** Painted parts with clean silhouettes and airbrushed gloss; liquid, bubbles, lightning and glows are separate soft layers.
- **Colour:** Measured: #0e080f 18% black, #300d59 14% dark purple, #47229c 10% purple, #5ca118 5%, #a6f807 5% and #12c208 4% green. The purple comes from the shared lightning frames; the jar's own colour is green with yellow-green lightning.
- **Lighting:** The brain and the liquid glow from inside; lightning forks and a large coloured halo (1008x1027) are additive layers on top. The metal is top-lit.
- **Ambience:** A specimen being charged: it gets livelier as it fills.
- **Materials:** Green enamelled metal, brass bolts, glass, coloured liquid, rubber hose.
- **Variants:** Six brain and liquid levels (brain_v1 to brain_v6, each with its own water mask, bubbles and electricity), so the jar shows how far it has filled. The green set has yellow-green lightning.
- **Motion:** One Spine 4.2.43 skeleton, 68 bones and 86 slots, with hit and idle animations for states 0 to 6 (1.0 s each). A 23-frame lightning sequence (bolt, 433x276) and bubble and spark sets move inside it.
- **Construction:** A Spine atlas of two pages cut into 94 regions (the jars, Mega Frankie and the level meter are the only art the game ships packed; everything else is loose files). No frame is drawn here: the tools cannot draw Spine 4.2.
- **Notes:** The three jars are one rig coloured three times: the same 94 region names with red, green or blue in them.
- **Measured:** mid-tone, vivid, cool, medium contrast, hard-edged · brightness 36% · saturation 74% · contrast 51% · warm 10% / cool 79% · brighter towards: top (9), top-left (4), bottom (2)
- **Palette (measured):** #0e080f black 18%, #300d59 dark purple 14%, #47229c purple 10%, #f4fcfd light cyan 8%, #5ca118 green 5%, #a6f807 green 5%

### The red brain jar (Frankie Spins)

`brain-jar-red` · atlas · 94 parts · largest 1008×1027 · sheet `sheets/brain-jar-red.webp`

- **Role:** One of three feature meters standing at the left of the reels: the red jar belongs to Frankie Spins. It is the game's most elaborate rig.
- **Subject:** A glass cylinder on a green metal base with a control plate, a domed green lid with a lamp, two bolt electrodes with bulb tips, ribbed hoses at both sides, and inside a brain floating in coloured liquid with bubbles.
- **Style:** Chunky cartoon laboratory hardware, the same family as the jar symbols on the reels.
- **Rendering:** Painted parts with clean silhouettes and airbrushed gloss; liquid, bubbles, lightning and glows are separate soft layers.
- **Colour:** Measured: #100811 16% black, #310c59 14% dark purple, #46239e 11% purple, #e41009 10% red, #3852d3 10% blue, #f4fbfd 8%. The purple and blue come from the shared lightning frames; the jar's own colour is red with orange-gold lightning.
- **Lighting:** The brain and the liquid glow from inside; lightning forks and a large coloured halo (1008x1027) are additive layers on top. The metal is top-lit.
- **Ambience:** A specimen being charged: it gets livelier as it fills.
- **Materials:** Green enamelled metal, brass bolts, glass, coloured liquid, rubber hose.
- **Variants:** Six brain and liquid levels (brain_v1 to brain_v6, each with its own water mask, bubbles and electricity), so the jar shows how far it has filled. The red set has orange lightning.
- **Motion:** One Spine 4.2.43 skeleton, 68 bones and 86 slots, with hit and idle animations for states 0 to 6 (1.0 s each). A 23-frame lightning sequence (bolt, 433x276) and bubble and spark sets move inside it.
- **Construction:** A Spine atlas of two pages cut into 94 regions (the jars, Mega Frankie and the level meter are the only art the game ships packed; everything else is loose files). No frame is drawn here: the tools cannot draw Spine 4.2.
- **Notes:** The three jars are one rig coloured three times: the same 94 region names with red, green or blue in them.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 32% · saturation 75% · contrast 52% · warm 31% / cool 68% · brighter towards: top (12), top-left (3), bottom (2)
- **Palette (measured):** #100811 black 16%, #310c59 dark purple 14%, #46239e purple 11%, #e41009 red 10%, #3852d3 blue 10%, #f4fbfd light cyan 8%

### The electric arc on the reel frame

`reel-electric-frame` · atlas · 31 parts · largest 684×77 · sheet `sheets/reel-electric-frame.webp`

- **Role:** The live green arc that runs in the gaps of the copper frame, between the glass bulbs at the left and right of the reels.
- **Subject:** A thin horizontal lightning line, 684x77, in 30 frames, and a round green glow for the bulbs.
- **Style:** Simple, bright effect art.
- **Rendering:** Drawn on black for additive blending: a white-green core with a soft green halo.
- **Colour:** Measured: all green. #0d310e 33%, #2d8231 30%, #90d092 22%, #53b058 11%.
- **Lighting:** Self-lit; it is itself a light source on the board.
- **Ambience:** Says the machine is switched on, all the time.
- **Materials:** Electricity.
- **Variants:** One arc sequence of 30 frames (sq_00 to sq_29) and one glow. Three more arcs of the same size are drawn for other places: m_sq in the modifier intro, fgs_sq and n_fgs_sq with the expanded Frankie.
- **Motion:** The skeleton reel_anim (7 bones, 8 slots, one 4.0 s animation) plays the 30 frames, turned upright for the side gaps (seen in the game screens as vertical arcs at both sides).
- **Construction:** 31 loose JPEG files on black and one Spine 4.2 skeleton that places them with additive slots.
- **Notes:** A cheap way to keep a static frame alive: one small looping strip.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 44% · saturation 58% · contrast 46% · warm 0% / cool 50%
- **Palette (measured):** #0d310e dark green 33%, #2d8231 green 30%, #90d092 green 22%, #53b058 green 11%, #d1f2d2 light green 2%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Wild

`symbol-wild` · atlas · 13 parts · largest 290×260 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol.
- **Subject:** The word WILD in dripping pale-green slime letters over a green brain, in a gold-edged green tile, with the jar's lid, two bolt electrodes and green lightning.
- **Style:** Horror-comic lettering, drippy and uneven.
- **Rendering:** Letters with a pale face, darker green extrusion and a black shadow; the tile behind is a monochrome green painting of a brain.
- **Colour:** Measured: 82% green. Black-green #040e02 27%, dark green #075e07 18%, bright green #70f557 8% and #0da806 7%, pale #f1fbee 6%, brass #b47f09 5%.
- **Lighting:** The word is the brightest thing in the tile; lightning adds additive flashes.
- **Ambience:** Slimy and electric.
- **Materials:** Slime, glass, brass, enamelled metal.
- **Variants:** The still (290x260), the tile, the word, the lid, two bulbs, a shadow and six small lightning frames.
- **Motion:** Skeleton sym10, 12 bones and 15 slots: land 0.67 s, win 1.0 s. The six lightning frames flicker between the electrodes.
- **Construction:** 13 loose PNG parts.
- **Notes:** It reuses the brain-jar hardware, so the Wild looks like part of the same machine.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 43% · saturation 65% · contrast 88% · warm 17% / cool 45% · brighter towards: top (1), top-left (1), top-right (1)
- **Palette (measured):** #040e02 black 27%, #075e07 dark green 18%, #70f557 green 8%, #0da806 green 7%, #f1fbee light green 6%, #b47f09 brown 5%

### Bonus symbols: brain jars

`symbol-brain-jars` · atlas · 32 parts · largest 290×300 · sheet `sheets/symbol-brain-jars.webp`

- **Role:** The bonus scatter symbols. A jar's colour says which bonus game it feeds: green Cash Trail, blue Cash Spins, red Frankie Spins (as the game's rules pages state).
- **Subject:** The brain jar from the side of the reels at symbol size, in a gold-framed tile showing the laboratory: single jars in green, blue and red, three pairs, and all three together.
- **Style:** The same chunky lab hardware as the big jars, simplified.
- **Rendering:** A painted jar with a coloured glow, in a tile with a small blurred painting of the lab behind it.
- **Colour:** Measured: dark teal #12392d 27% and #127764 10%, brown and gold of the frame #5e3d09, #a27010, #ecaa0f, plus yellow-green #d1ef0a and blue #0aa0ef from the jars.
- **Lighting:** The jars glow from inside; top-lit metal (measured on 6 parts).
- **Ambience:** Specimens on display.
- **Materials:** Glass, coloured liquid, green enamelled metal, brass, a gold frame.
- **Variants:** Seven stills at 290x300: sym13 green, sym14 blue, sym15 red, sym16 to sym18 the pairs, sym19 all three. Free-standing jars for the animation and lightning in three colours.
- **Motion:** Seven skeletons (10 bones for a single jar, 19 for a pair, 28 for the triple): land and collect 0.67 s, win 1.0 s. Small 6-frame lightning sequences in the jar's colour.
- **Construction:** Loose PNG parts; the double and triple symbols are built from the same jar pictures.
- **Notes:** Pairs and a triple as symbols of their own are unusual: one cell can feed two or three meters at once.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 41% · saturation 82% · contrast 66% · warm 34% / cool 52% · brighter towards: top (6), top-left (1), top-right (1)
- **Palette (measured):** #12392d dark cyan 27%, #5e3d09 brown 10%, #127764 dark cyan 10%, #a27010 brown 6%, #ecaa0f orange 6%, #149698 cyan 5%

### Cash prize ball

`symbol-cash-ball` · atlas · 27 parts · largest 556×562 · sheet `sheets/symbol-cash-ball.webp`

- **Role:** The symbol that carries a cash value, collected by the Collect symbol.
- **Subject:** A glowing yellow plasma ball with lightning veins running out from its centre, a pale ring edge and an orange outer halo; the value is written on it with the cash numerals.
- **Style:** A plasma globe, the lab's version of a coin.
- **Rendering:** A 21-frame animated plasma texture inside a ring, with a rim shadow and a soft halo.
- **Colour:** Measured: 97% warm. Gold #f4b803 54%, brown-gold #b68600 34%, yellow #ebfa15 4%.
- **Lighting:** Self-lit: the white-hot centre is the light.
- **Ambience:** Warm money against a cold green board.
- **Materials:** Plasma behind glass.
- **Variants:** One colour here; the four jackpot balls are the same design in other colours.
- **Motion:** Skeleton sym08, 10 bones: idle 1.0 s, land 0.67 s, win 0.67 s. The plasma is a 21-frame sequence (ball_00 to ball_20) and a four-point star twinkles on it.
- **Construction:** 27 loose PNG files: 21 plasma frames, the ball, a shadow ring, a star and the outer glow.
- **Notes:** The flat yellow of the still makes a red-outlined number readable on it.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged · brightness 67% · saturation 96% · contrast 40% · warm 97% / cool 1%
- **Palette (measured):** #f4b803 gold 54%, #b68600 brown 34%, #ebfa15 gold 4%, #effa7f gold 3%, #e44700 orange 2%

### High symbols: hand, ray gun, control box, the Bride

`symbols-high` · atlas · 18 parts · largest 290×300 · sheet `sheets/symbols-high.webp`

- **Role:** The four high-paying symbols.
- **Subject:** A stitched green severed hand standing on its fingers; a grey and brass ray-gun apparatus on a stand; an orange control box with a dial, buttons and two green plasma bulbs; and the Bride, a blue-skinned girl with the tall streaked hairdo, a gold tiara, stitches and orange eyes, in a gold frame.
- **Style:** Rounded cartoon props with a toy-like finish; the Bride is a big-headed, cute-but-cross character portrait.
- **Rendering:** Smooth painted 3D-look forms, crisp silhouettes, strong speculars on metal, a soft coloured glow behind each object. The Bride fills a framed tile, the three objects float free.
- **Colour:** Measured: green #20e622 13% (glows and plasma), orange #b5471a 11%, dark blue-grey #2a2837 11%, grey-green #639a77 7%. The hand sits on a red glow, the gun and the box on green, the Bride on a green-to-yellow gradient with a gold border.
- **Lighting:** Top and top-left key light on the objects with a coloured back glow; the Bride is lit from below by green (measured: light from top, top-left and bottom on three parts each).
- **Ambience:** Mad-science toys; the Bride adds attitude.
- **Materials:** Stitched skin, brushed steel and brass, painted orange metal, glass bulbs, hair, gold.
- **Variants:** Per symbol at about 290x260: the still, the win art split into the object and its glow, and a blur. The Bride has a frame, separate eyelids and two small electric arcs.
- **Motion:** Skeletons sym04 to sym06 have 3 bones (land 0.67 s, win 1.0 s: the object and its glow pulse). The Bride, sym07, has 8 bones: she blinks and arcs crackle at her neck.
- **Construction:** Loose PNG parts on small Spine 4.2 rigs.
- **Notes:** Only the Bride gets a frame and a face animation: the top symbol is given more craft than the rest.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 45% · saturation 68% · contrast 61% · warm 38% / cool 42% · brighter towards: top (3), top-left (3), bottom (3)
- **Palette (measured):** #20e622 green 13%, #b5471a orange 11%, #2a2837 dark blue 11%, #639a77 green 7%, #061c04 black 4%, #0d6319 dark green 4%

### Jackpot balls

`symbol-jackpot-balls` · atlas · 128 parts · largest 556×562 · sheet `sheets/symbol-jackpot-balls.webp`

- **Role:** The four jackpot prize symbols: MINI, MINOR, MAJOR, GRAND.
- **Subject:** The cash ball's plasma globe in four colours, each with its jackpot word across it in fat outlined letters.
- **Style:** The same plasma globe, colour-coded.
- **Rendering:** Animated plasma inside a neon ring, the word on top with a white outline and a drop shadow.
- **Colour:** MINI green, MINOR blue, MAJOR magenta, GRAND red. Measured: blue #0575ec 11%, magenta #ee06f2 10%, green #4feb04 10%, orange-red #ea4003 10%.
- **Lighting:** Self-lit, with a neon ring glow of the same colour.
- **Ambience:** Neon signs; the loudest colours in the game.
- **Materials:** Plasma behind glass.
- **Variants:** Four colours of everything: the still (290x315), a 21-frame plasma sequence, a shadow ring, an outer glow, a flat glow disc and the word.
- **Motion:** Four skeletons of 13 bones and 12 slots: idle, collect_idle and fade_off 1.0 s, land and win 0.67 s. A shared 23-frame lightning sequence (electric_bolt, 300x191) plays across the ball.
- **Construction:** 128 loose files, most of them the four 21-frame plasma sequences.
- **Notes:** The words and colours are the ones on the jackpot plates above the reels.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 39% · saturation 86% · contrast 36% · warm 28% / cool 54% · brighter towards: top (4)
- **Palette (measured):** #0575ec blue 11%, #ee06f2 magenta 10%, #4feb04 green 10%, #ea4003 orange 10%, #b201b6 magenta 7%, #08020c black 7%

### Collect symbol: Frankie

`symbol-frankie-collect` · atlas · 24 parts · largest 290×780 · sheet `sheets/symbol-frankie-collect.webp`

- **Role:** The Collect symbol on reel 1, which gathers the cash and jackpot balls in view; it can expand to the whole reel with a multiplier (as the rules pages state).
- **Subject:** Frankie, the monster as a child-like cartoon: square green head, flat black hair, neck bolts, stitches, heavy-lidded orange eyes and a smirk, his hands gripping the bottom of the tile, with COLLECT in gold letters. Behind him a castle under a green storm sky. The expanded version is a three-cell picture of him standing in a graveyard with a gold-edged box for the multiplier.
- **Style:** Family-animation character design: big head, small body, rounded forms, friendly menace.
- **Rendering:** Soft painted 3D-look shading with clean edges; the tile is framed by dark thorny vines instead of a straight border.
- **Colour:** Measured: 58% cool. Black-teal #102224 26%, dark teal #275147 13%, mint cyan #6af7d4 9% and #13f3a5 4%, orange-gold #e39a09 7% for COLLECT and the multipliers.
- **Lighting:** A mint-green rim light from behind and a top key light (measured: from the top on 7 parts).
- **Ambience:** Mischievous rather than frightening.
- **Materials:** Green skin, hair, a brown jacket with a blue bow tie, brass bolts, gold lettering, vines.
- **Variants:** The still (290x304), a copy with an empty value box (1xsym11), the expanded picture (290x780), multipliers x2, x3, x4 and x5 as gold art, head, body, hands and frame pieces for the animation.
- **Motion:** Skeleton sym11, 30 bones and 27 slots: land 0.67 s, collect 0.97 s, collect_idle and win 1.0 s. Head, hands and body are separate parts, so he moves inside the frame.
- **Construction:** 23 loose PNG parts. The expanded, fully rigged Frankie is its own unit under Characters.
- **Notes:** The tile's vine border breaks the grid of square frames and makes this symbol the one the eye finds first.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 49% · saturation 61% · contrast 66% · warm 23% / cool 57% · brighter towards: top (8), bottom (3), right (1)
- **Palette (measured):** #102223 black 26%, #275147 dark cyan 13%, #6af7d4 cyan 9%, #f7fef9 light green 9%, #e49a09 orange 8%, #23bf83 green 6%

### Low symbols: J, Q, K, A

`symbols-royals` · atlas · 12 parts · largest 290×260 · sheet `sheets/symbols-royals.webp`

- **Role:** The four low-paying symbols.
- **Subject:** Slab-serif capital letters, each pierced by a bolt through its side like the monster's neck bolts, with a marbled, veined surface.
- **Style:** Cartoon letters made into monster parts: one idea (the bolt) ties plain royals to the theme.
- **Rendering:** Extruded 3D-look letters with a copper-gold rim, a veined inner face and a soft coloured glow behind; no outline.
- **Colour:** One colour per letter: J teal-cyan, Q purple, K green, A red-orange. Measured over the unit: brown-gold rim #964e10 12% and #ca7a11 6%, dark red #631903 12%, purple #7429ad 8% and #9011ef 4%, green #04fa62, cyan #05faf5.
- **Lighting:** Even front light with a top sheen on the rim; each letter carries a glow of its own colour.
- **Ambience:** Bright and readable; the least spooky things on the board.
- **Materials:** Veined stone or flesh-like enamel inside a copper rim, steel bolts.
- **Variants:** Three pictures per letter at 290x260: the still, a win copy (w_sym) and a vertically smeared blur for the spinning reel.
- **Motion:** Four skeletons of 3 bones and 2 slots: land 0.67 s and win 1.0 s, a pulse of the one picture with an additive copy.
- **Construction:** Loose PNG files; the motion blur is a painted file, not a shader.
- **Notes:** A third, dimmed green copy of each exists for Frankie Spins.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 40% · saturation 80% · contrast 53% · warm 45% / cool 43%
- **Palette (measured):** #964e10 brown 12%, #631903 dark red 12%, #7429ad purple 8%, #ca7a11 orange 6%, #9011ef purple 4%, #f50c02 red 3%

### Frankie Spins symbol set

`frankie-spins-symbols` · atlas · 175 parts · largest 587×508 · sheet `sheets/frankie-spins-symbols.webp`

- **Role:** The symbol set of the Frankie Spins bonus, on its 5x5 board: only prizes, jars, potions and Mega Frankie are live; the paying symbols stay as dimmed decoration (seen in play).
- **Subject:** All the base symbols redrawn at 240x190: the paying symbols and the Wild as dim, dark-green 'off' versions, and the cash ball, four jackpot balls, seven jar symbols, the Collect Frankie and a green potion flask in full colour; potions that carry a jackpot word; plasma frames for the balls; a spill of gold coins.
- **Style:** The same art; state is shown by colour alone.
- **Rendering:** The off versions are the base pictures reduced to one dark green and blurred copies of them; the live symbols keep their glow.
- **Colour:** Measured: black-green #081f04 17%, orange-gold #f5af1a 12%, #c6780f 10% and #f9e446 6% (the cash ball and coins), red #f30303 5%, blue #2137ef 4%.
- **Lighting:** The off symbols have no light of their own; the live ones glow.
- **Ambience:** A darkened board where only the prizes are lit.
- **Materials:** As the base symbols; the flask is glass with green liquid and a cork.
- **Variants:** 175 parts: 9 off and 9 blurred symbols, 14 live symbols, 4 jackpot potions, five 21-frame plasma sequences at 123x124, a 23-frame coin spill (587x508), jackpot backs and words.
- **Motion:** Skeletons sym14_feature_anim (15 bones; idle 2.0 s and land 0.4 s per prize kind), sym_bonuscollect (9 bones, the potion with its prize), sym_bonuscollect_coinspill (1.0 s) and jar_anim.
- **Construction:** Loose PNG files at a smaller cell size than the base game.
- **Notes:** A cheap, clear device: recolour the losers instead of removing them, so the reels still look full.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 41% · saturation 85% · contrast 45% · warm 54% / cool 30% · brighter towards: top (14), bottom (4)
- **Palette (measured):** #081f04 black 17%, #f5af1a orange 12%, #c6780f orange 10%, #f9e446 gold 6%, #6f1106 dark red 6%, #f30303 red 5%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### Frankie, expanded (the full-reel Collect)

`frankie-expanded-collect` · atlas · 156 parts · largest 434×899 · sheet `sheets/frankie-expanded-collect.webp`

- **Role:** The rigged, full-figure Frankie of the expanded Collect symbol, three cells tall, with its setting and effects.
- **Subject:** Frankie as a full figure, cut into parts: face without eyes, hair, ears, eyeballs, irises, eyelids, eyebrows, nose, neck bolts, jacket, shirt, bow tie, legs, shoes and a set of hand poses.
- **Style:** The same family-animation character as the Collect symbol: big square head, small body, chunky hands.
- **Rendering:** Soft painted shading on each part, built to overlap; white-cyan silhouette copies of the head, body, hands and bolts are the glow layers.
- **Colour:** Green skin, dark blue-black hair and shoes, a brown-orange jacket, a yellow-olive shirt and a blue bow tie; glows in mint cyan. Measured: dark green #244f3e 22%, black #111d1e 15%, near-white cyan #f1fefc 13%, cyan #10fff4 10% and #6efde4 9%, brown #54340d 4%.
- **Lighting:** Parts are lit from the top and top-left; the glow copies put a mint rim light around the figure when he powers up.
- **Ambience:** A toy monster come alive.
- **Materials:** Skin, hair, cloth, leather shoes, steel bolts.
- **Variants:** 156 parts: the figure's parts, twelve left-hand and four right-hand poses, a graveyard setting (background 318x798, seven dead branches, fog, shadows, a ten-piece vine frame), a tall glow (434x899), flares, and two 30-frame electric arc sequences.
- **Motion:** Skeleton sym12, 138 bones and 129 slots: collect 3.0 s, three position animations of 3.0 s (pos_1 to pos_3), collect_idle and move_multiplier 1.0 s. A second small rig, sym12_expand_glow, plays the glow.
- **Construction:** Loose PNG parts, one file each, for a Spine 4.2 rig. No frame of the rig is drawn here: the tools cannot draw Spine 4.2, so the game screens are the reference for how he looks whole.
- **Notes:** The most expensive single symbol state in the game: 162 pictures on 138 bones. Seen in play standing the height of reel 1 with a x5 multiplier.
- **Measured:** mid-tone, saturated, cool, medium contrast, strong highlights · brightness 54% · saturation 55% · contrast 41% · warm 10% / cool 72% · brighter towards: top-left (10), top (9), top-right (8)
- **Palette (measured):** #244f3e dark green 22%, #111d1e black 15%, #f1fefc light cyan 13%, #10fff4 cyan 10%, #6efde4 cyan 9%, #a8fcef light cyan 6%

### Mega Frankie (the giant Collect symbol of Frankie Spins)

`frankie-giant-collect` · atlas · 111 parts · largest 559×687 · sheet `sheets/frankie-giant-collect.webp`

- **Role:** The rigged Frankie that sits on the Frankie Spins board as one large symbol and grows from 2x2 cells to 5x5.
- **Subject:** Frankie as a full figure, cut into parts: face without eyes, hair, ears, eyeballs, irises, eyelids, eyebrows, nose, neck bolts, jacket, shirt, bow tie, legs, shoes and a set of hand poses.
- **Style:** The same family-animation character as the Collect symbol: big square head, small body, chunky hands.
- **Rendering:** Soft painted shading on each part, built to overlap; white-cyan silhouette copies of the head, body, hands and bolts are the glow layers.
- **Colour:** Green skin, dark blue-black hair and shoes, a brown-orange jacket, a yellow-olive shirt and a blue bow tie; glows in mint and gold. Measured: dark green #152e18 30%, greens #2b7c33 22% and #85c48d 15% (much of it the 30 arc frames), near-white #f4fbf7 6%, brown #583610 4%.
- **Lighting:** Parts are lit from the top and top-left; the glow copies put a mint rim light around the figure when he powers up.
- **Ambience:** A toy monster come alive.
- **Materials:** Skin, hair, cloth, leather shoes, steel bolts.
- **Variants:** 111 regions: the figure's parts with two ready-made turned heads, arm and hand poses, a golden silhouette of the whole figure, dust and smoke puffs, sparks in orange and green, a potion flask and a 30-frame arc.
- **Motion:** Skeleton frankenstein_giant_symbol, 108 bones and 100 slots: idle, cheer and power_up animations of 2.0 s for each size from 1x1 to 5x5, and a throw. In play he bursts coins when a prize lands on him.
- **Construction:** A Spine atlas of several pages, one of three places where the game packs its art. No frame of the rig is drawn here (Spine 4.2); the game screens show him whole.
- **Notes:** One rig serves five sizes by animation, not by five sets of art.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 44% · saturation 54% · contrast 45% · warm 12% / cool 53% · brighter towards: top-left (10), bottom-right (8), bottom (8)
- **Palette (measured):** #152e18 dark green 30%, #2b7c33 green 22%, #85c48d green 15%, #49ad54 green 6%, #f4fbf7 light green 6%, #583610 brown 4%

### Frankie, in Frankie Spins

`frankie-spins-figure` · atlas · 65 parts · largest 559×687 · sheet `sheets/frankie-spins-figure.webp`

- **Role:** A second copy of the figure's parts, loaded for the Frankie Spins bonus (the folder is fortune_spins).
- **Subject:** Frankie as a full figure, cut into parts: face without eyes, hair, ears, eyeballs, irises, eyelids, eyebrows, nose, neck bolts, jacket, shirt, bow tie, legs, shoes and a set of hand poses.
- **Style:** The same family-animation character as the Collect symbol: big square head, small body, chunky hands.
- **Rendering:** Soft painted shading on each part, built to overlap; white-cyan silhouette copies of the head, body, hands and bolts are the glow layers.
- **Colour:** Green skin, dark blue-black hair and shoes, a brown-orange jacket, a yellow-olive shirt and a blue bow tie; glows in mint cyan. Measured: dark teal #1e2b2c 31%, dark green #326345 14%, near-white #fafffd 13%, brown #53340c 7%, pale cyan #a5f0dc 6%.
- **Lighting:** Parts are lit from the top and top-left; the glow copies put a mint rim light around the figure when he powers up.
- **Ambience:** A toy monster come alive.
- **Materials:** Skin, hair, cloth, leather shoes, steel bolts.
- **Variants:** 65 parts: the same figure, with twelve left-hand and nine right-hand poses, and a potion flask.
- **Motion:** Used by the intro and Big Money rigs of the bonus games (their skeletons name these parts). Swapped hand pictures do the finger movement.
- **Construction:** Loose PNG parts, one file each, for a Spine 4.2 rig. No frame of the rig is drawn here: the tools cannot draw Spine 4.2, so the game screens are the reference for how he looks whole.
- **Notes:** These loose parts duplicate, under an fs_ prefix, what the bonus also ships packed in the Mega Frankie atlas; the bonus intro and Big Money rigs name them.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 45% · saturation 48% · contrast 40% · warm 18% / cool 63% · brighter towards: top-left (9), bottom (8), bottom-left (6)
- **Palette (measured):** #1e2b2c dark cyan 31%, #316344 dark green 14%, #fafffd light cyan 13%, #53340c brown 7%, #a5f0dc light cyan 6%


## Logo and title

The game's own wordmark.

### The logo

`logo` · atlas · 2 parts · largest 2071×618 · sheet `sheets/logo.webp`

- **Role:** The game's wordmark, above the reels in the lobby and intro, and on the loading screen.
- **Subject:** FRANKENSTEIN's in tall green capitals on an arc over FORTUNE in orange-gold slab letters, with blue-white lightning forking out at both sides. The loading version adds Frankie's head above it.
- **Style:** Cartoon horror lettering: the green word is condensed and slightly uneven, like a film poster, the gold word is fat and friendly.
- **Rendering:** Extruded 3D-look letters with a gradient face, a pale rim and a dark drop edge; the lightning is a soft glowing shape with a white core.
- **Colour:** Measured: blue #36abfa 12%, pale green #acf7d2 11%, green #25f72d 7%, orange #eca91b 6%, on black #0a140d 10%. Green for the monster, gold for the money, blue for the electricity.
- **Lighting:** Front-lit with a top highlight on each letter; the lightning throws a blue glow behind the words.
- **Ambience:** Fun and charged.
- **Materials:** Glossy plastic-like letters, electricity.
- **Variants:** Two files: logo_ml 2071x618 (wordmark with long lightning) and preloader_logo_ml 1023x660 (with the head). A third, smaller copy sits in the intro set.
- **Motion:** Still in the files; no logo skeleton.
- **Construction:** Flat PNG files with the lightning baked in.
- **Notes:** The logo is not on the base game screen at 1280x720: the jackpot plates take the top of the board.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 56% · saturation 62% · contrast 90% · warm 21% / cool 54%
- **Palette (measured):** #36abfa blue 12%, #acf7d2 light green 11%, #0a140d black 10%, #25f72d green 7%, #f2fdf1 light green 6%, #eca91b orange 6%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Frankie Spins intro

`frankie-spins-intro` · atlas · 7 parts · largest 1600×1600 · sheet `sheets/frankie-spins-intro.webp`

- **Role:** The intro screen of the Frankie Spins bonus.
- **Subject:** A blurred laboratory backdrop, the FRANKIE SPINS label, two rule panels (Mega Frankie collects what lands on him; potions give extra spins and a bigger Mega Frankie), a red play arrow and yellow-green glows.
- **Style:** The same poster layout as the Cash Trail intro.
- **Rendering:** Panels with a neon edge and baked-in icons; the label is the jar label enlarged.
- **Colour:** Measured: black #121517 30%, teal #0b8984 23% and #103e47 10%, yellow-green #d7f917 5%.
- **Lighting:** A yellow-green glow behind the panel and the play button.
- **Ambience:** Bright and inviting.
- **Materials:** None; lettering and light.
- **Variants:** Seven files; backdrop 1600x1600.
- **Motion:** Skeleton fs_intro_popup, 87 bones, one animation of 6.57 s, with the Frankie rig.
- **Construction:** Loose files.
- **Notes:** The play arrow is red here and on the Cash Trail intro, green on the game's first intro.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 39% · saturation 75% · contrast 66% · warm 26% / cool 59% · brighter towards: top (2), bottom-left (1)
- **Palette (measured):** #121517 black 30%, #0b8984 dark cyan 23%, #103e47 dark cyan 10%, #d7f917 gold 5%, #f7fce6 light green 4%, #4b4616 brown 4%

### Frankie Spins popups

`frankie-spins-popups` · atlas · 14 parts · largest 960×540 · sheet `sheets/frankie-spins-popups.webp`

- **Role:** The words that pop up inside Frankie Spins: +SPIN, +SPINS, BOOST and MEGA BOOST.
- **Subject:** Green slab words with a blue outline, with green lightning in four directions, a green flare and an orange flash.
- **Style:** The win tiers' lettering.
- **Rendering:** Extruded gradient letters; the lightning is 8 frames on black at 960x540.
- **Colour:** Measured: near-white #f2faf6 22%, green #219911 14%, blue #085da8 9%, pale blue #9ad0f1 7%.
- **Lighting:** Lightning shoots out from behind the word.
- **Ambience:** A jolt.
- **Materials:** Glossy lettering, electricity.
- **Variants:** Four words, an 8-frame lightning sequence, three light pictures.
- **Motion:** Skeleton bonus_popups, 11 bones, four animations of 2.33 s.
- **Construction:** 14 loose files and a numeral font for the number of spins.
- **Notes:** None of the four was caught in a screenshot; read from the files.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 58% · saturation 59% · contrast 67% · warm 4% / cool 68% · brighter towards: top (4)
- **Palette (measured):** #f2faf6 light green 22%, #219911 green 14%, #085da8 blue 9%, #04180b black 9%, #9ad0f1 light blue 7%, #b4e5a7 light green 7%

### Cash Trail intro panels

`cash-trail-intro` · atlas · 6 parts · largest 1121×406 · sheet `sheets/cash-trail-intro.webp`

- **Role:** The words of the Cash Trail intro screen.
- **Subject:** The CASH TRAIL label and five panel texts: 'Advance along the Cash Trail, reach the end for Big Money' and four versions of 'Any spin can award …' with different jar icons.
- **Style:** The intro screen's panel style: a dark green plate with a neon edge.
- **Rendering:** White and gold capitals with a dark red outline; small jar icons baked into the text pictures.
- **Colour:** Measured: black-green #052208 50%, white #fbf9f3 8%, green #3ebc52 6%, oranges and gold #cf7a06, #ebb214, #efd744.
- **Lighting:** A soft green glow round each panel (measured: 66% soft edge).
- **Ambience:** Rules told as a poster.
- **Materials:** None; lettering.
- **Variants:** Five panels at 1121x406, the label at 395x235. Four 'any spin can award' versions exist because the list drops a bonus already won (inference).
- **Motion:** Skeleton ct_intro_popup, 87 bones and 80 slots, four animations of 6.57 s; it names the Frankie figure's parts, so the Frankie on this screen is the rig, not a picture.
- **Construction:** Six loose PNG files with the words baked in (_ml).
- **Notes:** Text as pictures: every language needs its own set.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, glow or soft effect · brightness 35% · saturation 74% · contrast 91% · warm 33% / cool 37% · brighter towards: top-right (3), top (2)
- **Palette (measured):** #052208 black 50%, #fbf9f3 light orange 8%, #3ebc52 green 6%, #cf7a06 orange 3%, #ebb214 orange 3%, #efd744 gold 3%

### The intro screen

`intro-popup` · atlas · 27 parts · largest 1600×1600 · sheet `sheets/intro-popup.webp`

- **Role:** The screen shown before play: the logo, the three bonus jars and two panels that explain the Collect multiplier (IT'S ALIVE!) and the random modifiers (FRANKIE TIME).
- **Subject:** A castle on a hill under a green storm sky as the backdrop; two tall dark-green panels with a neon edge, each holding a small picture of the reels; the three brain jars with their labels in the middle under the logo; a walking silhouette of Frankie on the hill; a green play button.
- **Style:** The game's poster: everything at its loudest, in comic-horror lettering.
- **Rendering:** A painted backdrop (1600x1600) kept dark and blurred at the edges; panels are flat with a glowing outline; headings are extruded green letters with drips or a 3D slab; body text is white capitals with a dark red outline.
- **Colour:** Measured: dark and vivid, 68% cool. Black-teal #061518 38%, dark teal #0b4140 19%, green #0c8a59 8% and #0a8b11 4%, purple #300852 4%. Gold is used only for BONUS GAMES and the jar labels.
- **Lighting:** The sky is lit by lightning behind the castle; each jar has a flare of its own colour behind it.
- **Ambience:** A stormy night at the castle, played for fun.
- **Materials:** Painted sky and stone, neon tube edges, the jars' glass and metal.
- **Variants:** 27 parts; a landscape and a portrait skeleton lay out the same parts.
- **Motion:** Skeleton intro_popup, 41 bones and 34 slots, one loop of 33.3 s (a portrait copy has 42 bones). A 30-frame electric border runs round the right panel (seen in the first screen).
- **Construction:** Loose PNG and JPEG files; the two small reel pictures are flat images of the game, not live reels.
- **Notes:** The only place the castle exterior appears with the base game; the laboratory is what the player then sits in.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 28% · saturation 80% · contrast 62% · warm 13% / cool 68% · brighter towards: top (4), bottom (2), top-right (1)
- **Palette (measured):** #061518 black 38%, #0b4140 dark cyan 19%, #0c8a59 dark green 8%, #300852 dark purple 4%, #0a8b11 dark green 4%, #f4faf1 light green 2%

### Big win celebration

`big-win` · atlas · 49 parts · largest 1200×715 · sheet `sheets/big-win.webp`

- **Role:** The win tiers: NICE, BIG, HUGE, MEGA and EPIC WIN, with the amount on a scroll plate.
- **Subject:** Tier words in the logo's green slab letters over a blue-outlined WIN; a dark plate in a thin gold frame for the amount; a green storm cloud with lightning; a blue flare; gold coins with a lightning bolt on them; five cut gems (diamond, red, yellow, green, blue) as particles; a purple-blue lightning sequence.
- **Style:** The game's lettering with a standard coin-and-gem shower.
- **Rendering:** Words are extruded with a gradient face and dark edge; coins and gems are glossy 3D-look renders; cloud, flare and lightning are soft additive layers on black.
- **Colour:** Measured over the unit: 90% cool, dark purple #330f5e 16%, purple #46249d 14%, blue #3756d2 14% (mostly the 23 lightning frames), near-white #f1fbf9 11%. The words are green, WIN is blue and white, coins gold.
- **Lighting:** The cloud and the flare glow behind the words; the coins have a strong top highlight.
- **Ambience:** A thunderclap of money.
- **Materials:** Glossy lettering, gold coins, cut gems, cloud, electricity.
- **Variants:** Five tier words at 962x340, WIN at 569x275, an 11-frame spinning coin (294x293), five gem particles, 23 lightning frames (866x552).
- **Motion:** Skeleton big_win, 7 bones: each tier has an 'in' animation of 2.0 s and a loop of 1.0 s; big_win_bg and big_win_panel bring in the cloud and the plate (0.67 s and 1.0 s). Coins and gems are thrown by a particle system (inference from the file names).
- **Construction:** 49 loose files; the amount uses the big win font.
- **Notes:** Five tiers reuse one layout: only the word picture changes. NICE, HUGE, MEGA and EPIC were seen in play.
- **Measured:** mid-tone, vivid, cool, high contrast, hard-edged, strong highlights · brightness 39% · saturation 70% · contrast 62% · warm 5% / cool 90% · brighter towards: top (10), top-left (3), bottom (2)
- **Palette (measured):** #330f5e dark purple 16%, #130620 black 15%, #46249d purple 14%, #3756d2 blue 14%, #f1fbf9 light cyan 11%, #75c1f8 blue 7%

### IT'S ALIVE! and the modifier intro

`its-alive-modifier` · atlas · 74 parts · largest 1459×976 · sheet `sheets/its-alive-modifier.webp`

- **Role:** The announcement played when Frankie appears to award a modifier (Frankie Time) and when the Collect symbol expands; both were seen in play.
- **Subject:** The words IT'S and ALIVE! in dripping neon-green letters, a rectangle of green lightning that frames the reels (26 frames), a wide green light, yellow-green lightning bolts and a thin cyan arc.
- **Style:** Horror-comic lettering and pure electricity.
- **Rendering:** Letters with a pale face and a strong green outer glow; the frame and bolts are JPEG frames on black for additive blending.
- **Colour:** Measured: 99% green. Dark green #0f4404 24% and #3a7a05 24%, green #099e12 10%; the arcs add cyan.
- **Lighting:** Everything here is a light source; the white_light picture floods the screen green.
- **Ambience:** The famous shout from the film, as a flash of green.
- **Materials:** Slime-like lettering, electricity.
- **Variants:** 74 parts: two word pictures, 26 frame-light frames (878x518), 14 bolt frames (1132x537), a 30-frame arc (684x77), a light and a glow.
- **Motion:** Skeleton its_alive, 13 bones, one animation of 2.0 s. A larger skeleton, modifier_intro (88 bones, 75 slots, 'in' and 'out' of 2.33 s), names 109 pictures, among them the Frankie figure's parts: he walks on for the modifier (inference from the attachment names).
- **Construction:** Loose files; the frame of lightning is the same picture family as the intro panel's border.
- **Notes:** One strong asset announces two features. In play the frame of lightning ran green for Frankie Time and cyan before the Collect symbol expanded.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 49% · saturation 77% · contrast 46% · warm 0% / cool 51%
- **Palette (measured):** #0f4404 dark green 24%, #3a7a05 dark green 24%, #099e12 green 10%

### Congratulations screen

`bonus-congratulations` · atlas · 4 parts · largest 3200×3200 · sheet `sheets/bonus-congratulations.webp`

- **Role:** The total at the end of a bonus.
- **Subject:** CONGRATULATIONS YOU HAVE WON in green and teal slab letters over the laboratory, with drifting gold dust; a second backdrop has Frankie standing at the bench.
- **Style:** Calm after the bonus: the lab, blurred.
- **Rendering:** The base background softened; lettering extruded with a pale rim; the amount in the teal numerals.
- **Colour:** Measured: black #111714 43%, teal #0a8a85 30%, dark teal #0d4444 8%, green #148d36 6%, gold dust #c8a73b 2%.
- **Lighting:** The green light along the bench sits right under the amount.
- **Ambience:** Satisfied, quiet.
- **Materials:** As the laboratory.
- **Variants:** Backdrop 3200x3200, the Frankie version 1600x1600, dust 1600x1600, the words 1521x374.
- **Motion:** Skeleton congrats, 7 bones: congrats_popup and unlucky_congrats_popup, 10 s each; congrats_jars shows which jars paid (seen in play: two small jars with their amounts under the total).
- **Construction:** Four loose files.
- **Notes:** An 'unlucky' version exists for a bonus that pays little or nothing (inference from the animation name).
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 27% · saturation 83% · contrast 30% · warm 25% / cool 65% · brighter towards: top (2)
- **Palette (measured):** #111714 black 43%, #0a8a85 dark cyan 30%, #0d4444 dark cyan 8%, #148d36 green 6%, #55340f brown 2%, #29b515 green 2%


## Effects

Frame sequences, glows, particles and transitions.

### Win light behind symbols

`symbol-win-light` · atlas · 2 parts · largest 4000×4000 · sheet `sheets/symbol-win-light.webp`

- **Role:** Light layers used behind a winning high symbol.
- **Subject:** A dark green radial burst of rays and a cone of green light with sparks rising from a white base.
- **Style:** Plain effect art.
- **Rendering:** JPEG on black for additive blending.
- **Colour:** Measured: all green, #306106 75% and #0c1803 25%.
- **Lighting:** Self-lit.
- **Ambience:** A quick lift under a win.
- **Materials:** Light.
- **Variants:** Two files: light_fx_0002 at 4000x4000, far larger than its use needs, and bean_burst at 260x325.
- **Motion:** Scaled and turned by the symbol skeletons (inference; they are named in the high symbols' folder).
- **Construction:** Two loose JPEG files.
- **Notes:** A 4000x4000 texture for a glow behind a 290 px symbol looks like an oversight rather than a choice (inference).
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 26% · saturation 91% · contrast 13% · warm 0% / cool 50%
- **Palette (measured):** #306106 dark green 75%, #0c1803 black 25%

### Screen transition

`transition` · atlas · 4 parts · largest 400×400 · sheet `sheets/transition.webp`

- **Role:** The wipe between the base game and a bonus game.
- **Subject:** A teal Frankie head with a smirk, an orange lens flare, and black and white fade squares.
- **Style:** The character's head reduced to one colour, like a stamp.
- **Rendering:** The head is painted in teal monochrome with a pale outline; the flare is a JPEG on black.
- **Colour:** Measured: near-white #fefffe 34% (the fade square), dark red #6a1702 20% and orange #b44608 11% (the flare), teal #0b4342 9% and #138078 5% (the head).
- **Lighting:** The flare bursts behind or through the head.
- **Ambience:** A wink from the mascot between scenes.
- **Materials:** None in particular.
- **Variants:** Four files: head 332x346, flare 400x400, two fades 330x330.
- **Motion:** Skeleton transition, 5 bones, one animation of 1.73 s: the head grows over the screen while the fades cover the change (seen in play over the congratulations screen and before a bonus intro).
- **Construction:** Four loose files on a tiny rig.
- **Notes:** Cheap and on-theme: four small files cover every scene change.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 57% · saturation 59% · contrast 42% · warm 47% / cool 21% · brighter towards: bottom (1)
- **Palette (measured):** #fefffe light green 34%, #6a1702 dark red 20%, #b44608 brown 11%, #0b4342 dark cyan 9%, #dc8022 orange 8%, #138078 dark cyan 5%

### Potion throw (Frankie Time)

`potion-modifier` · atlas · 34 parts · largest 340×310 · sheet `sheets/potion-modifier.webp`

- **Role:** The effect of the random modifier: Frankie throws a flask that bursts on the reels (seen in play adding Wild symbols).
- **Subject:** A round glass flask with a blue-white glare, green liquid in six slosh shapes, a 24-frame yellow-green explosion and a square green glow for the cell it changes.
- **Style:** The flask is painted like the symbols; the burst is effect art.
- **Rendering:** Glass with a sharp glare; liquid as separate shapes inside it; explosion frames on black.
- **Colour:** Measured: black #0a0c02 48%, olive green #415203 28%, yellow-green #6d9308 8% and #93e30d 8%.
- **Lighting:** The burst is the light: it whites out the cell for a moment (seen in play).
- **Ambience:** Slapstick chemistry.
- **Materials:** Glass, liquid.
- **Variants:** 34 parts: flask, glare, liquid (7), explosion (24, 340x310), glow. The folder is named modifier_dynamite_blast.
- **Motion:** Skeletons potion_triggers (8 bones, 1.33 s) and symbol_glow (5 bones, 0.77 s).
- **Construction:** Loose files.
- **Notes:** The folder name suggests the effect was taken over from another game's dynamite modifier and redrawn as a potion (inference).
- **Measured:** dark, vivid, warm and cool mixed, low contrast, hard-edged · brightness 26% · saturation 69% · contrast 24% · warm 11% / cool 39% · brighter towards: top (3), right (3), top-right (2)
- **Palette (measured):** #0a0c02 black 48%, #415203 dark green 28%, #6d9308 green 8%, #93e30d green 8%


## Game interface

Buttons, counters and panels drawn for this game.

### Bonus counters and the trail coin

`feature-counters-and-coin` · atlas · 12 parts · largest 173×49 · sheet `sheets/feature-counters-and-coin.webp`

- **Role:** Small counters used inside the bonus games: +1, +2, +3 and SPIN or SPINS in the blue and the red jar's colours, and the Cash Trail token.
- **Subject:** White cartoon numerals with a blue or red edge, and a round teal coin with Frankie's face.
- **Style:** Sticker-like, very simple.
- **Rendering:** White faces with a coloured outline and a small shadow; the coin is a painted head on a disc.
- **Colour:** Measured: white #fdfefe 46%, pale blue #a4d9f2 6%, red #ea6262 4% and #e0a0a0 5%, teal #0e3e4b 4%.
- **Lighting:** Top-lit (measured on 8 parts).
- **Ambience:** Light and quick.
- **Materials:** None in particular; the coin reads as metal.
- **Variants:** Blue and red sets of +1, +2, +3, SPIN, SPINS; one coin at 90x90; one glow particle.
- **Motion:** Two skeletons (blue_jar_feature, red_jar_feature) with on (0.4 s), idle (1.0 s) and off (0.4 s) for each of +1, +2 and +3; coin_trail holds the coin.
- **Construction:** Twelve loose PNG files on three tiny rigs.
- **Notes:** There is no green set here: the green jar's game, Cash Trail, has its own counter.
- **Measured:** bright, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 65% · saturation 25% · contrast 98% · warm 46% / cool 54% · brighter towards: top (8), top-right (2), bottom (1)
- **Palette (measured):** #fdfefe light cyan 46%, #040305 black 18%, #a4d9f2 light cyan 6%, #e0a0a0 light red 5%, #0e3e4b dark cyan 4%, #eb6361 red 4%

### Express Bet panel

`side-bet-panel` · atlas · 4 parts · largest 371×475 · sheet `sheets/side-bet-panel.webp`

- **Role:** The switch at the right of the reels for the game's side bet, which costs half the stake more and raises the chance of a bonus (as the game's rules page states).
- **Subject:** A small dark cabinet with a copper frame, the words EXPRESS BET and INCREASED BONUS CHANCE, two display windows, a green tick and a red cross, a green button and a green glow for the switched-on state.
- **Style:** Built like a piece of the lab, with interface lettering.
- **Rendering:** Flat panel with a copper edge; gold gradient lettering with a dark outline; glossy pill button.
- **Colour:** Measured: pale green #b9efac 33% and green #71fd58 18% (the glow), black #120c14 23%, orange #e19b0b 5%.
- **Lighting:** A green halo marks the active state.
- **Ambience:** Functional; it recedes when off (it is drawn dimmed in the base game screens).
- **Materials:** Painted metal, copper, a plastic button.
- **Variants:** Panel 335x428, glow 371x475, tick and cross, button; an 'inactive' animation file in Lottie format.
- **Motion:** The inactive state is a small Lottie file; no skeleton.
- **Construction:** Four loose PNG files and its own number font.
- **Notes:** This is the game's bonus-chance bet. In this Blueprint build it is called Express Bet; White Hat's page for the US build lists a Side Bet. That they are the same thing is inference.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 57% · saturation 51% · contrast 39% · warm 27% / cool 43% · brighter towards: top-left (1), top (1), bottom-left (1)
- **Palette (measured):** #b9efac light green 33%, #120c14 black 23%, #71fd58 green 18%, #462f16 brown 5%, #e19b0b orange 5%, #85f995 green 3%

### Mega Frankie level meter

`frankie-spins-level-meter` · atlas · 62 parts · largest 457×1045 · sheet `sheets/frankie-spins-level-meter.webp`

- **Role:** The meter at the right of the Frankie Spins board: potions collected fill it, and each level makes Mega Frankie larger, from 2x2 up to 5x5 (as the rules pages state).
- **Subject:** A tall blue glass tube in a copper stand with a hose, a dark scale plate marked 2X2, 3X3, 4X4 and 5X5 with a small Frankie marker, green liquid, bubbles and lightning; and small copies of the cash and jackpot balls.
- **Style:** The brain jars' hardware turned into a thermometer.
- **Rendering:** Painted metal and glass with clean edges; liquid, bubbles, white lightning (30 frames) and flares are separate layers.
- **Colour:** Measured over the unit: greys #393f37 32% and #6f736d 9% (bubble and glass layers), black #171815 26%, brass #826216 4%. In play the tube is blue and the liquid acid green.
- **Lighting:** The liquid glows; lightning strikes the tube on a level up (read from the files: electric_strike).
- **Ambience:** A charge building up.
- **Materials:** Glass, copper, rubber hose, liquid.
- **Variants:** 62 regions in one Spine atlas page: three scale tubes (3x3, 4x4, 5x5), the stand, level labels, five small prize balls (cover_sym), liquid levels.
- **Motion:** Skeleton level_up_meters, 47 bones and 51 slots: for each size an idle per level (4.0 s), a level-up (1.0 s) and an upgrade to the next size (1.0 s).
- **Construction:** The second of the game's two kinds of packed art: a Spine atlas. No frame is drawn here (Spine 4.2).
- **Notes:** Progress is shown as liquid in a tube, the same picture language as the jars: no abstract bar anywhere in the game.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 34% · saturation 40% · contrast 56% · warm 33% / cool 23% · brighter towards: right (1), top (1)
- **Palette (measured):** #393f37 grey 32%, #171815 black 26%, #6f736d grey 9%, #eae9e6 white 6%, #c3c0b6 grey 4%, #826216 brown 4%

### Cash Trail counter

`cash-trail-counter` · atlas · 27 parts · largest 173×2767 · sheet `sheets/cash-trail-counter.webp`

- **Role:** The round window at the left of the Cash Trail that spins and shows each result, with the BONUS WIN box and PRESS TO CONTINUE.
- **Subject:** A black disc in a green neon ring; results +1 to +5 in white numerals with a green edge, BIG MONEY, COLLECT, Frankie's head, and jar icons for Cash Spins, Frankie Spins and both; a tall blurred strip for the spin; a dark box with BONUS WIN in orange.
- **Style:** A one-reel slot inside the bonus, in the game's sticker lettering.
- **Rendering:** Flat results with outlines and a drop shadow; the ring glows; a blue-violet burst plays inside the window (11 frames on black).
- **Colour:** Measured: black #08080c 20%, blue-violet #353a96 18% (the burst), dark blue #192641 12%, white #fbfcfb 11%, green #17ec1d 3%.
- **Lighting:** The neon ring is the light.
- **Ambience:** A fairground wheel reduced to one window.
- **Materials:** Neon tube, enamel plate.
- **Variants:** 27 parts: 13 results at 419x417, the strip 173x2767, the ring, the box, the prompt, 11 burst frames.
- **Motion:** Skeleton trail_counter, 13 bones: full, remove_all, remove_blue and remove_red of 3.0 s (the strip scrolls; jar results are taken off the strip once won, inference from the names).
- **Construction:** Loose PNG and JPEG files.
- **Notes:** The same white numerals with a coloured edge as the jar counters, here edged green for the green jar's game.
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast · brightness 39% · saturation 48% · contrast 57% · warm 13% / cool 68% · brighter towards: top (1), bottom (1), top-left (1)
- **Palette (measured):** #08080c black 20%, #353a96 blue 18%, #192641 dark blue 12%, #fbfcfb light green 11%, #8baf8d green 8%, #506051 grey 6%

### Jackpot plates

`jackpot-plates` · atlas · 13 parts · largest 402×113 · sheet `sheets/jackpot-plates.webp`

- **Role:** The four fixed prizes shown above the reels: MINI, MINOR, MAJOR, GRAND.
- **Subject:** Four copper-framed boxes with ball finials, each filled with its colour, a word label above each, and a flat lightning line that runs along the top.
- **Style:** The copper pipe of the reel frame, with cartoon labels.
- **Rendering:** Smooth 3D-look copper; flat colour fields with a soft top sheen; labels are fat outlined letters with a white stroke and a drop shadow.
- **Colour:** Measured: copper browns #51301e 13% and #190e04 14%, green #076103 and #03f714, red #e91d1d and #af0303, blue #048eee. In play: MINI green, MINOR blue, MAJOR magenta, GRAND red.
- **Lighting:** Top-lit (measured on 8 parts).
- **Ambience:** A scoreboard bolted on top of the machine.
- **Materials:** Copper, enamel colour panels, electricity.
- **Variants:** Four boxes about 401x112, four labels, five lightning lines (one white and one per colour).
- **Motion:** Four skeletons (grand, major, mini, minor, 32 bones each) with a static pose and a 0.67 s win animation; the 32 bones bend the lightning line.
- **Construction:** Loose PNG files, four per plate, on a small Spine rig.
- **Notes:** The same four colours return on the jackpot balls on the reels, so a ball and its plate match.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 33% · saturation 71% · contrast 61% · warm 55% / cool 26% · brighter towards: top (8)
- **Palette (measured):** #190e04 black 14%, #51301e brown 13%, #076103 dark green 7%, #e91d1d red 6%, #fcfbfb light red 6%, #af0303 red 6%


## Typography

Embedded fonts and lettering.

### Prize and bonus numerals

`bonus-fonts` · atlas · 7 parts · largest 723×794 · sheet `sheets/bonus-fonts.webp`

- **Role:** Seven small bitmap fonts: the values on the cash balls, the Express Bet panel, and in the bonus games the spins-left counter, the winnings, the values collected, the +spins popup and the congratulations amount.
- **Subject:** Digits with comma and point (the Express Bet set adds $, the popup set adds +).
- **Style:** One fat, rounded numeral design drawn seven times, each coloured for its place.
- **Rendering:** Gradient faces with a heavy outline: gold with a dark red edge (cash balls, Express Bet), white with a black edge (spins left, +spins), cream with a red edge (winnings, collected values), teal with a pale rim (congratulations).
- **Colour:** Measured over the unit: near-white #fffefe 42%, black #070503 12%, teal-cyan #18f3de 10% and #0fb49f 8% (the two largest pages are the white and the teal sets).
- **Lighting:** Top-lit gloss on every face.
- **Ambience:** Readable first; money is warm, counters are white, the final total is the scene's own teal.
- **Materials:** Gold, enamel white, glowing teal.
- **Variants:** Seven pages from 130x228 to 723x794.
- **Motion:** None of their own.
- **Construction:** Bitmap fonts: one PNG each with an XML table of glyph boxes.
- **Notes:** Seven fonts for digits alone, beside the big win font: every counter gets lettering drawn for its size instead of one font scaled.
- **Measured:** bright, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 68% · saturation 36% · contrast 88% · warm 18% / cool 26% · brighter towards: top (1)
- **Palette (measured):** #fffefe light orange 42%, #070503 black 12%, #18f3de cyan 10%, #0fb49f cyan 8%, #313625 dark green 6%, #2edbac cyan 3%

### Win amount numerals

`big-win-font` · atlas · 1 parts · largest 419×463 · sheet `sheets/big-win-font.webp`

- **Role:** The digits of the amount on the big win screen.
- **Subject:** 0 to 9, comma and point, 156 px high.
- **Style:** Fat rounded numerals.
- **Rendering:** Gold gradient face, bright top, with a red-orange outline and a dark red edge.
- **Colour:** Measured: orange #ec980a 34%, dark red #6d0b01 18%, gold #fde753 16%, cream #fffce6 11%.
- **Lighting:** Top-lit gloss.
- **Ambience:** Hot and rich against the cool green scene.
- **Materials:** Polished gold.
- **Variants:** One page, 419x463, 14 glyphs listed in the font file (12 are drawn on the page).
- **Motion:** None of its own.
- **Construction:** A bitmap font: one PNG with an XML table of glyph boxes.
- **Notes:** Gold with a red edge is kept for money everywhere in the base game; the bonus games add white, teal and cream numerals of their own.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 59% · saturation 79% · contrast 91% · warm 100% / cool 0% · brighter towards: top (1)
- **Palette (measured):** #ec980a orange 34%, #6d0b01 dark red 18%, #fde753 gold 16%, #fffce6 light gold 11%, #b72d05 red 8%, #fdf2a8 light gold 5%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `power-play-and-bonus-wheel`: 34 parts
- `power-play-cash-font`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Roboto (Regular); Roboto Black (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1679 components cut from 1233 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
