# Serpent Gold Hold And Win: art report

octoplay · run `2026-11-27-0430-octoplay-serpent-gold-hold-and-win` · captured 2026-11-27

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/serpent-gold-hold-and-win

**Extracted:** 802 named components from 45 textures in 45 atlases; 57 Spine skeletons; 29 frame sequences (515 frames); 3 fonts. Grouped into 30 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

A lost-temple jungle in which every game mechanic is a snake: a photoreal misty rainforest sits behind hard, glossy, gold-rimmed symbols, three jewel-scaled Snakes in red, green and blue run the features, and a stone serpent above the reels heats from grey to lava as coins are thrown into its mouth.

**Style.** Two registers kept apart on purpose. The world (two jungle scenes, branches, birds) is photoreal painted concept art with soft haze; the game pieces (letters, props, coin, Snakes, plates, frame) are stylised casino art with thick gold rims, enamel colour and Mesoamerican step-fret ornament. The stone serpent and the temple walls sit between the two. Inference: the backgrounds have the look of an image model's picture retouched by hand; the symbols and interface are drawn in the usual production way.

**Rendering.** Backgrounds: soft atmospheric depth, no outlines. Symbols: smooth gradients, hard speculars, a dark outline and a thin yellow-green edge glow that lifts them off the dark panel. Snakes: faceted glossy scales and gold trim. Lettering: two-tone gradient fills with a light inner edge and dark outline. Effects: white sprites tinted by the engine, with fire and lava painted in colour.

**Colour.** Measured over the game's art: near-black brown #18130f 29%, jungle grey-green #526254 14%, dark wine #392d2c 10%, pale grey #b8b7b5 6%, orange-brown #a53b11 5%, near-white #f9f9f7 4%, pale green #83927f 3%, deep red #601a0a 1%. The base game is green haze around a dark brown board with gold; the bonus turns the surround to red stone, violet and orange. Colour carries the rules: red, green and blue for Collect, Clone and Double (heads, frames, gems, side lights, the NEW SNAKE words); purple, blue, green, red-orange and gold for MINI, MINOR, MAJOR, GRAND and ULTIMATE; one hue per letter symbol; gold for anything that pays; jade green for the value on a coin.

**Lighting.** Diffuse daylight from above through mist in the base scene; a low orange sun and coloured haze in the bonus. Game pieces are lit from the top with their own highlights and do not take the scene's light. The statue is lit from above until its mouth and eyes light it from inside.

**Ambience.** An expedition that has found the temple: humid, hushed and green at first, with danger shown as beauty (jewel snakes, a sleeping statue). The bonus is heat and treasure: red walls, gold underfoot, the statue's eyes burning.

**Shape language.** Diamond snake heads and shield-shaped hoods; trapezoid plates in stepped-fret frames; slanted slab letters; round sun coins with spikes; square spiral frets on every frame end, lock plate and letter serif. The fret and the snake are the two repeated marks: the Wild, the win line's end, the win plate's ornament, the frame's corner and the opening wipe are all snakes.

**Materials.** Wet leaf, moss and mist; carved stone, grey when cold and red when lit; gold with turquoise; enamel or gemstone scales; coloured glass letters; lava and ember.

**Typography and lettering.** Drawn words in slanted comic capitals with a dark outline for jackpots, win tiers and feature messages, each in its tier's or snake's colour. The logo is separate: spaced serif capitals in snake skin, gold and red. Numbers come from three bitmap fonts of the provider's shared store: Rubik Mono One in gold with a deep wine extrusion (ladder multipliers, win amounts), Blambot FX Pro Heavy in jade with a gold rim (the value on a Golden Coin, as the screens show), Anton italic in gold (the collector counters). The shell's Poppins sets the help, buttons and balance line.

**Motion.** All motion is Spine: 57 skeletons in one bundle file (47 in 4.2.40, 6 in 4.2.42, 4 in 4.2.43), with 29 frame sequences (515 frames: the coin's turn, a lava flow, fire, white glints fitted to each letter, word and plate, sparks, mist, two shatters). Seen in play: snake bodies wiping the intro away; the three collector frames arriving and the red Snake unlocking under a blue sparkling splash; coins flying from each Golden Coin to the statue, whose mouth and eyes turn red; clusters bound in a gold chain with a 3-2-1 lock disc; win lines in gold with a snake-head end; a gold win amount with a coin shower; the temple walls sliding in for the bonus. Read from the files only: jackpot wins, the big-win tiers, the Clone and Double Snakes in action. No skeleton frame is shown in this report, because the project's renderer cannot draw Spine 4; assembled and motion pictures are absent for that reason only.

**Variants and themes.** Two scenes on one picture (day, and a dusk regrade). Three Snakes on one rig with identical part sizes. Five jackpot plates on one shape, drawn twice (ladder size and win size). Three win tiers and a total on one lettering. Three collector frames told apart by gems and side lights. Two reel backings (five and six reels) and a frame cut in strips so the board grows from 5x4 to 6x6. Numerals in three coloured fonts.

**How it is built.** Three 4096 px atlas pages hold the game: two carry one 2750x2510 scene each with the large pieces, the third some 600 small sprites. Eleven word pictures are localised (en-GB). Characters are few and cheap: the statue is one still with glow layers, a Snake is seven parts, the screen-filling wipe is six 307 px scale strips run along a path. Water moves by a displacement map over a mask, not by frames. White effect sprites are tinted in the engine. Symbol pictures for the help, the flat logo, the numeral fonts, the Extra Chance card, the controls and Poppins come from the provider's shared store outside the game bundle. The artists' green cell guide (tileGuide) ships in the atlas as an anchor.

**Consistency.** Strong inside each register, with one visible seam between them: the soft photoreal jungle and the hard enamel game pieces do not share light or edge quality, and the birds, painted sharper than the scene, sit between. The seam is used rather than hidden: the dark board and gold rims make every symbol read at once against the haze. Colour coding is exact across symbol, frame, word and effect. The comic-capital win words are the least themed element.

**What to take from it.** (1) Let one creature carry every mechanic. Here the snake is the Wild, the three feature symbols, the collectors, the progress statue, the payline's end, the win plate's ornament and the screen wipe, so the theme is restated by play itself and needs no mascot character. (2) Give each feature a colour and never break it: red Collect, green Clone, blue Double hold across head, frame gems, side lights, splash words and effects. A player can read which feature fired from colour alone, and one rig with three skins serves all three. (3) Show locked content as dimmed real art, not as a padlock. The Clone and Double Snakes sit dark in their frames with a counter from the first spin: the goal is visible and the same sprites are reused. (4) Put a progress display where the eye already rests and make it a material change. The stone serpent goes from cold grey to lava mouth and burning eyes with a handful of glow layers and one 40-frame lava loop over a single still picture. (5) A photoreal background can sit behind stylised symbols if the board between them is dark and plain and every symbol has a rim. Decide that separation on purpose; do not try to half-match the two. (6) Make the bonus by regrading and re-dressing, not repainting: the same jungle picture in dusk colours, two temple wall pieces and a coin pile sliding in, and a second reel backing give a scene that feels new. (7) Build big moments from small tiles. The opening wipe fills the screen with snake bodies made of six scale strips on a path; the cluster chain is five 68 px pieces. Plan such pieces as tileable from the start. (8) Fit the highlight to the object. Each letter, word and plate has its own short white glint sequence drawn to its bevels, at small size and scaled up: cheap, and far better than a generic sweep. (9) Keep effect sprites white and tint them in the engine, and keep painted colour for the few effects that are material (fire, lava). (10) For AI-assisted art: backgrounds of this kind are where an image model gives most (two scenes from one picture by regrade); symbols, frames, plates and lettering here depend on exact shape language, rigs in parts and colour codes, and are the part to art-direct tightly and cut for animation.

## Colour, measured

The game's own art (provider interface left out): mid-tone, saturated, warm and cool mixed, medium contrast, hard-edged · brightness 36% · saturation 51% · contrast 57% · warm 50% / cool 28% · brighter towards: top (107), top-left (28), top-right (15)

Palette: #18130f black 30%, #526254 grey 15%, #392d2c dark red 10%, #b8b7b5 grey 7%, #a53b11 brown 5%, #f9f9f7 light yellow 4%, #83927f grey 4%, #601a0a dark red 2%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 3 | 29% | 45% | 65% | 39% / 39% | #121110 black 32%, #516355 grey 23%, #3d282f dark red 16% |
| Reel board | 2 | 20% | 73% | 27% | 91% / 5% | #2a1a0c black 73%, #654329 brown 10% |
| Symbols | 7 | 39% | 70% | 59% | 61% / 26% | #101315 black 29%, #c0832e orange 14%, #56240b brown 9% |
| Characters | 1 | 33% | 72% | 50% | 82% / 15% | #d04418 red 42%, #150f12 black 20%, #961f0b red 11% |
| Logo and title | 2 | 40% | 71% | 58% | 47% / 29% | #0d1b0b black 28%, #d9a430 orange 12%, #876834 brown 9% |
| Win celebrations and banners | 3 | 44% | 72% | 67% | 70% / 20% | #25130a black 22%, #b27b3c orange 12%, #d9940f orange 9% |
| Effects | 6 | 74% | 18% | 28% | 21% / 3% | #b8b8b8 grey 45%, #fbfbfa white 28%, #ec8615 orange 7% |
| Game interface | 2 | 35% | 74% | 47% | 68% / 16% | #40200a brown 35%, #8a4832 red 25%, #5da521 green 15% |
| Typography | 3 | 63% | 76% | 74% | 87% / 10% | #f0c133 orange 45%, #f6e96d gold 14%, #390c09 dark red 11% |
| Provider interface (shared) | 1 | 52% | 96% | 74% | 100% / 0% | #e48305 orange 50%, #b13a02 brown 17%, #fbd812 gold 17% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Two jungle scenes on one composition

`backgrounds` · atlas · 2 parts · largest 2750×2510 · sheet `sheets/backgrounds.webp`

- **Role:** The full-screen backdrop: bgNormal for the base game and bgSpecial for the Hold & Win bonus (the skeleton Backgrounds has the skins normal and special).
- **Subject:** A misty rainforest clearing seen from a low path: a mossy stone slab over a small waterfall in the middle distance, a fallen moss-covered trunk across a still pool, red bromeliads at the left, large banana and monstera leaves framing the top corners. The special version is the same picture at dusk, flooded with orange, pink and violet light, with the foreground leaves turned to black silhouettes and a red-and-blue bird on a stone at the bottom.
- **Style:** Photoreal painted concept art, close to a matte painting; no outlines and no cartoon shapes. Inference: the look, the soft indistinct detail in the distance and the odd leaf joins are typical of an image model's picture retouched by hand.
- **Rendering:** Soft atmospheric depth in three planes: sharp dark leaves in front, mid-ground plants with rim light, and trees dissolving into pale green haze. The special scene is not repainted: it reads as the same picture regraded, with added light rays, purple shadows and a few painted blue fireflies over the water.
- **Colour:** Measured over both: near-black #101011 31%, grey-green #516255 28%, dark violet-grey #342c34 12%, pale green-grey #869483 8%, orange #de8e64 4%, light orange #eed597 3%, purple #572e69 2%. Hue shares: green 46%, purple 19%, red 14%, orange 13%. The base scene is almost all green; the special one carries the purple, orange and red.
- **Lighting:** Base: diffuse daylight falling from the upper centre through the canopy, brightest behind the waterfall. Special: a low warm sun behind the trees at the upper centre, with strong backlight and coloured haze. Measured light position: top and top-right.
- **Ambience:** Humid, quiet and a little secretive in the base game; hot, magical and charged in the bonus.
- **Materials:** Wet leaves, moss, bark, stone, still water, mist.
- **Variants:** Two: normal and special, 2750x2510 px each, both square-ish so one file serves landscape and portrait (the skeletons carry landscape and portrait placements).
- **Motion:** The picture itself does not move. Over it the skeletons BackgroundEffects and ForegroundEffects sway branches and leaves on a 3.67 s loop, two birds perch in the corners, and the textures bgDisplacementMaskNormal and seaDisplacement are, by their names and shapes, a mask over the pool and a ripple map that make the water shimmer (inference from the files; a faint shimmer is seen in play).
- **Construction:** Each scene is one opaque 2750x2510 picture on its own 4096 px atlas page. In landscape at 1280x720 only a band across its middle is on screen.
- **Notes:** The waterfall and the stone slab sit exactly behind the reel board, so in the base game they are hidden; they are seen only on the intro screen.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 31% · saturation 39% · contrast 70% · warm 32% / cool 45% · brighter towards: top-right (1), top (1)
- **Palette (measured):** #101011 black 31%, #516255 grey 28%, #342c34 grey 12%, #869483 grey 8%, #de8e64 orange 4%, #eed597 light orange 3%

### Temple steps and treasure: the bonus foreground

`temple-and-gold` · atlas · 3 parts · largest 1375×1024 · sheet `sheets/temple-and-gold.webp`

- **Role:** The foreground that slides in for the Hold & Win bonus (skeleton SlotTransition: show 2.17 s, hide 2.67 s).
- **Subject:** Two corner pieces of a carved stone temple: an upper wall of blocks with a large half sun-disc relief in gold and a stepped fret border, and a lower flight of stone steps with a small heap of gold coins on a slab; and one large pile of gold coins with stacked columns and a green gem in it.
- **Style:** Painted game-prop stonework in a Mesoamerican manner (step frets, glyph blocks, a calendar-stone half disc), tighter and more designed than the photoreal jungle.
- **Rendering:** Blocks with chipped edges and cracks, gold inlay with a hot rim, a strong red-magenta grade over everything. The coin pile is a dense rendered heap with soft red bounce.
- **Colour:** Measured: dark red #421a1e 57%, red-brown #833926 21%, orange #b65b3a 12%, light orange #d79b59 6%, gold-brown #b87907 3%. Warm share 94%.
- **Lighting:** Lit as if by fire or sunset from the right and below: edges glow orange, recesses fall to dark wine red.
- **Ambience:** A treasure chamber at the mouth of the temple; heat and reward.
- **Materials:** Carved stone, gold inlay, gold coin.
- **Variants:** Top part and bottom part (1375x1024 and 1375x832 px) and the coin pile (978x473 px). By the skeleton they are placed at the screen's sides around the enlarged reel board.
- **Motion:** SlotTransition brings them in with dustCloud and two stone particles (rubble), and takes them out again at the end of the bonus.
- **Construction:** Three sprites on the special scene's atlas page; drawn already graded to the bonus colours, so they are not used in the base game.
- **Notes:** Seen in play: the walls stand at both sides of the 6x6 board as a red band above and below the dusk jungle, and the statue's burning eyes look through an opening at the top.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 25% · saturation 68% · contrast 52% · warm 94% / cool 0% · brighter towards: top-right (1), bottom-right (1), top-left (1)
- **Palette (measured):** #421a1e dark red 57%, #833926 red 21%, #b65b3a orange 12%, #d79b59 orange 6%, #b87907 brown 3%

### Branches, ferns, falling leaves and two birds

`foliage-and-birds` · atlas · 21 parts · largest 552×871 · sheet `sheets/foliage-and-birds.webp`

- **Role:** The moving layer in front of and around the scene: side branches, leaf fringes over the frame, the leaf wipe of the intro, leaves that fall on a spin, and two birds.
- **Subject:** Fern fronds, a palm frond, a broad dark taro-like clump, a bright yellow-green sapling, a bromeliad cluster with orange-red spikes, a hanging vine of small pale leaves, single leaves (sharp and blurred), three white leaf silhouettes, and two red-and-black birds with long yellow-orange bills (one perched upright with a red crest, one crouched in profile).
- **Style:** The same photoreal painted look as the backgrounds; the birds are painted more tightly and brightly than anything around them.
- **Rendering:** Soft-edged cut-outs with real leaf detail; several are deliberately dark, nearly silhouettes, to sit in front of the scene. Four leaf particles are pre-blurred as if out of focus.
- **Colour:** Measured: near-black green #0d1d0a 79% and dark green #2a6020 12%; hue share green 89%. The birds add the only red and yellow, and the bromeliad the only orange.
- **Lighting:** Leaves are lit from above and behind with dark undersides; the birds have a clear top light and a glossy bill.
- **Ambience:** Dense, close and alive: the player looks out through leaves.
- **Materials:** Leaf, frond, feather, bill.
- **Variants:** Four side branches (bgBranchL1, L2, R1, R2), three foreground leaf fringes (fgLeaves1 to 3), two leaf clumps of the intro plate (gsPlateLeaves1, 2), four blurred leaf particles, three white falling-leaf shapes tinted by the engine, one sharp leaf (leaf01), one vine patch, two birds.
- **Motion:** Branches and fringes sway on the 3.67 s loops of BackgroundEffects and ForegroundEffects; GameIntro (show 1.75 s) parts the fgLeaves fringes like a curtain; SpinEffect and ReelEffectNormal throw the sharp leaf (leaf01) across the reels (0.83 to 1.15 s); the blurred and white leaf particles are named in no skeleton, so the engine's particle emitters drop them (inference). In play the birds stay perched at the lower left and the right edge.
- **Construction:** 21 separate sprites up to 552x871 px, placed by Spine skeletons. The falling leaves are white so that the engine can colour them.
- **Notes:** The same fringes are reused under the win bar (WinBar uses fgLeaves3 and gsPlateLeaves), so one set of leaves dresses the scene, the intro and the win plate.
- **Measured:** dark, vivid, warm and cool mixed, low contrast · brightness 16% · saturation 70% · contrast 25% · warm 6% / cool 47% · brighter towards: top-left (4), top (2), bottom-right (2)
- **Palette (measured):** #0d1d0a black 79%, #2a6020 dark green 12%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Five jackpot plates beside the reels

`jackpot-ladder` · atlas · 123 parts · largest 483×159 · sheet `sheets/jackpot-ladder.webp`

- **Role:** The ladder at the left of the reels that names the five jackpots (MINI 25x, MINOR 50x, MAJOR 100x, GRAND 250x, ULTIMATE 5000x, as the screen shows) and, in the bonus, their progress.
- **Subject:** Five trapezoid plates in a gold stepped-fret frame, each filled with one glossy colour; five drawn words in slanted comic capitals; five small coloured discs with a gold rim; and white glint frames for the plate and each word.
- **Style:** Arcade-casino signage: saturated enamel plates and brush-lettered words with a thick dark outline, set in the temple's fret frame.
- **Rendering:** Flat gradients with a soft central sheen on the plates; letters with a two-tone fill, light inner edge and dark offset shadow.
- **Colour:** Measured: gold-orange #ca8f14 17%, orange-brown #a13c06 13%, dark red #491207 9%, blue #0b3aa5 6%, purple #5e1f75 6%, green #09a827 4%. The code is purple MINI, blue MINOR, green MAJOR, red-orange GRAND, gold ULTIMATE; the word colours follow (magenta, blue, green, red, black on gold).
- **Lighting:** Top light on the gold frames (measured: top); a white sweep crosses plate and word.
- **Ambience:** Loud and clear against the dark jungle: the prize list is the brightest fixed thing on screen.
- **Materials:** Polished gold, coloured enamel or glass.
- **Variants:** Five plates on one shape (the ULTIMATE plate is larger, 483x159 against about 398x130), five words, five progress discs, and six 18-frame glint sequences (one for the plate, one per word).
- **Motion:** Jackpot: idle 1.67 s, win and winLoop 0.67 s, collect 0.67 s, with the glint sequences, sparks and small fireworks. JackpotProgress and JackpotProgressEffect (fire pillars rising to the plate in 0.33 to 0.68 s) mark a jackpot coming closer. Seen in the bonus: a disc beside each plate counts the symbols still needed (33, 27, 22, 17, 7 after three coins). A jackpot win was not reached.
- **Construction:** One skeleton with five skins (jackpot0 to 4); the multiplier figures are text over the plate, in the heavy gold numerals (Rubik Mono One, by their look).
- **Notes:** The same five plates are drawn again at larger size for the jackpot win (see the unit jackpot-win).
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 44% · saturation 80% · contrast 70% · warm 64% / cool 25% · brighter towards: top (3)
- **Palette (measured):** #ca8f14 orange 17%, #a13c06 brown 13%, #491207 dark red 9%, #0b3aa5 blue 6%, #5e1f75 dark purple 6%, #09a827 green 4%

### Reel panel and vine-bound frame

`reel-board` · atlas · 25 parts · largest 1032×1034 · sheet `sheets/reel-board.webp`

- **Role:** The 5x4 reel area: its backing, its frame in pieces, the win line and the chain that binds a locked cluster.
- **Subject:** A dark brown stone panel carved with a faint round calendar relief and hung with thin green vines as reel dividers; a narrow frame of carved brown stone with gold fret ornaments at the ends and corners, a small gold snake head on the top left corner, and lianas wound round it; two bracket ornaments (logoD); a gold chain in five pieces; a short red-and-gold striped line with a snake-head end.
- **Style:** Carved temple architecture reduced to a thin border, so the reels stay large; ornament in the stepped-fret language used across the interface.
- **Rendering:** Painted stone with low relief and warm rim light, gold picked out with small hard highlights, vines painted with soft shadows onto the stone.
- **Colour:** Measured: near-black brown #2a1a0c 80%, brown #64442c 10%; hue share orange 93%. It is the darkest and least saturated-looking unit, which is what lets the symbols stand out.
- **Lighting:** Even, from the top; the panel is slightly lighter at its centre.
- **Ambience:** An old wall in shade.
- **Materials:** Stone, gold inlay, vine, chain.
- **Variants:** Two backings: slotBgNormalLandscape (1038x809, four vine dividers for five reels) and slotBgSpecialLandscape (1032x1034, five dividers for the six reels of the bonus). Frame pieces come as D and M sets (by their sizes, the desktop and mobile layouts; inference) and the top right piece as Normal and Special. Chain: middle, inner, outer, crossed and overlap edges, for drawing a chain border round any cluster shape.
- **Motion:** Seen in play: a cluster of Golden Coins is bound by the gold chain with a lock disc at its corner, and winning lines are drawn in gold with the snake-head end at the right. SlotFrame has landscape (1.42 s) and portrait animations; ReelEffectNormal and ReelEffectSpecial flash a soft square glow with leaves on a reel (0.83 s), in three skins named for the three snakes.
- **Construction:** The frame is assembled from about a dozen strips so it can stretch from 5x4 to 6x6. The chain pieces are 68 px tiles meant to be repeated by the engine round a cluster of locked coins. tileGuide is a plain green 202 px square: the artists' cell guide, left in the atlas and used as an invisible anchor in most skeletons.
- **Notes:** The win line's end is a tiny snake head, so even the payline is a snake.
- **Measured:** dark, vivid, warm, low contrast, hard-edged · brightness 17% · saturation 72% · contrast 22% · warm 94% / cool 3% · brighter towards: top-left (3), top-right (2), top (2)
- **Palette (measured):** #2a1a0c black 80%, #64442c brown 10%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Flat symbol pictures for the help pages

`help-symbol-pictures` · atlas · 16 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The pictures of each symbol that the shell's help page shows, served from the provider's asset store and not from the game bundle.
- **Subject:** Sixteen 225x225 px pictures, tile0 to tile15: tile0 is blank; then 10, J, Q, K, A; the map, helmet, chest and open compass; the Wild idol with its word; the Golden Coin; the red, green and blue snakes assembled with open mouths; and the green gem.
- **Style:** The game's own symbols, flattened to one picture each.
- **Rendering:** As in the game; the snakes and the compass are shown assembled (head over body and open mouth; lid raised), which the atlas only holds in parts.
- **Colour:** Measured: near-black #14130f 16%, browns #57240b 13% and #8d4216 12%, tan #cc9847 13%, orange #db7d14 9%, purple #493661 5%, green #196014 4%.
- **Lighting:** As the symbols: top light (measured: top).
- **Ambience:** A catalogue of the set.
- **Materials:** As the symbols.
- **Variants:** One per symbol id.
- **Motion:** None.
- **Construction:** Loose WebP files, one per symbol; they are the only place the full symbol set can be seen assembled without running the game.
- **Notes:** Useful as the reference for how each rigged symbol should look at rest.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 39% · saturation 74% · contrast 73% · warm 73% / cool 20% · brighter towards: top (5)
- **Palette (measured):** #14130f black 16%, #57240b brown 13%, #cc9847 orange 13%, #8d4216 brown 12%, #db7d14 orange 9%, #493661 dark purple 5%

### Wild: the golden double-headed serpent idol

`symbol-wild` · atlas · 38 parts · largest 208×172 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol (tile10), which substitutes for all symbols except the Golden Coin and the Snakes (help text).
- **Subject:** A gold idol of a serpent folded into an M or W shape with a square stylised head at each end, covered in scale texture, set with turquoise stones and crowned with a turquoise diamond; the word WILD in gold slanted capitals lies across its foot.
- **Style:** A Mesoamerican double-headed serpent ornament turned into a slot symbol; the only symbol drawn as jewellery.
- **Rendering:** Dense small scale pattern in gold with strong white speculars and dark brown recesses; the word is a smooth gold gradient with a dark red-brown outline and glow.
- **Colour:** Measured: gold-brown #ae5f0d 26%, dark brown #3a0f01 14%, gold #f4d04c 14%, orange-gold #db9d23 13%, white #fffffe 12% (highlights), with turquoise accents too small to register.
- **Lighting:** Top light with hard highlights (measured: top, strong highlights).
- **Ambience:** The treasure itself.
- **Materials:** Gold, turquoise.
- **Variants:** One idol (208x172 px), one word (206x80 px), and two 18-frame white highlight sequences, one for the idol and one for the word.
- **Motion:** TileWild: loop 1.67 s, onLand 0.42 s, win 0.58 s, with a star blink, sparks and a dust puff on landing.
- **Construction:** Idol and word are separate sprites, so the word can pulse by itself; highlights are tiny sequences (up to 55x84 px) laid over them.
- **Notes:** The same serpent shape, flattened to a silhouette, is the ornament on the win plate (winMaxSnake) and the end of the win line.
- **Measured:** mid-tone, vivid, warm, high contrast, strong highlights · brightness 55% · saturation 73% · contrast 75% · warm 86% / cool 2% · brighter towards: top (1)
- **Palette (measured):** #ae5f0d brown 26%, #3a0f01 black 14%, #f4d04c gold 14%, #db9d23 orange 13%, #fffffe light green 12%, #703507 brown 7%

### The three Snakes: Collect, Clone, Double

`symbols-snakes` · atlas · 67 parts · largest 374×281 · sheet `sheets/symbols-snakes.webp`

- **Role:** The three feature symbols (tile12 red Collect, tile13 green Clone, tile14 blue Double) and the pictures inside the three collector frames at the right of the reels.
- **Subject:** A snake's head seen from the front with its hood or coils raised behind it: a diamond head of large plated scales, two yellow slit eyes rimmed in gold, gold brow ridges and two gold fangs; behind it a dark body with iridescent scales in a gold-edged shield shape, a wide open mouth with a forked gold tongue, and a coil. Each has its word in gold slanted capitals: COLLECT, CLONE, DOUBLE.
- **Style:** Jewel-like fantasy creature art: symmetrical, frontal, more emblem than animal.
- **Rendering:** Glossy faceted scales with bright speculars on the head, soft dark iridescence on the body, gold trim with hard highlights. White shine layers exist for head, mouth, body and eyes of the red snake's rig.
- **Colour:** Measured over the unit: near-black #0f1416 45% (bodies and mouths), gold #c7942f 10%, white #fcfcfb 7% (shine layers), brown #53260b 6%, dark teal #0a3c40 5%. Each head takes one colour, red, green or blue, with the same yellow eyes and gold trim.
- **Lighting:** Heads lit from above; the mouths glow from below (measured: bottom and top almost equally).
- **Ambience:** Threatening but precious: guardians rather than monsters.
- **Materials:** Scale as enamel or gemstone, gold, a wet dark mouth.
- **Variants:** Three snakes on identical part sizes (head about 276x195 px, body 374x281, mouth 270x207, coil 289x104, tongue 67x345), so one rig serves all three by skin. Three words with a highlight sequence each (13 to 16 frames).
- **Motion:** TileFeature: onLand 0.42 s, lock 0.67 s, loop 2.5 s, loopActive 1.67 s, activate 0.83 s, upgrade 0.33 s, collect and win 0.5 s. With separate head, mouth, tongue and coil, the snake can rear, open its mouth and flick its tongue (inference from the parts). Seen in play: the Collect Snake lands with its mouth open, coins pour from it and the red collector frame flares; Clone and Double were still locked (3/25 and 0/25) when the sessions ended.
- **Construction:** Seven parts per snake in Spine with three skins; shine layers are white sprites added on top. The same parts are drawn inside the collector frames by the skeleton FeatureProgress.
- **Notes:** On the intro screen the three snakes appear together, green in the middle, as the game's key art, built from these same parts.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 34% · saturation 73% · contrast 51% · warm 54% / cool 35% · brighter towards: bottom (7), top (6), top-right (1)
- **Palette (measured):** #0f1416 black 45%, #c7942f orange 10%, #fcfcfb light yellow 7%, #53260b brown 6%, #0a3c40 dark cyan 5%

### Low symbols: 10, J, Q, K, A as carved gems

`symbols-letters` · atlas · 81 parts · largest 193×194 · sheet `sheets/symbols-letters.webp`

- **Role:** The five low-paying symbols (tile1 to tile5).
- **Subject:** The numeral 10 and the letters J, Q, K, A, each a thick slanted slab of coloured glass or polished stone in a bronze-gold rim, with a square spiral fret cut into a serif and a few green leaves or a vine growing over it.
- **Style:** Casino card ranks dressed for the temple: chunky italic slab letters, bevelled like cut gems, with the fret motif that runs through the frame.
- **Rendering:** Smooth gradients inside each letter with a bright diagonal sheen, a carved gold border with its own dark outline, tiny painted leaves. Clean and hard-edged against the painted scene.
- **Colour:** One hue each: 10 purple, J blue, Q green, K red, A orange-gold. Measured over the unit: white #ffffff 36% (the glint frames), brown #49240c 14%, tan #d2a25d 8%, orange #c76e16 7%, purple #532966 6%, green #16610c 6%, red #9a1909 5%.
- **Lighting:** Top-left sheen on each face; the rim is lit from above.
- **Ambience:** Bright sweets on a dark wall.
- **Materials:** Coloured glass or jade, bronze-gold, leaf.
- **Variants:** Five letters at about 120 to 200 px wide and 150 to 195 px high; one white highlight sequence per letter (13 to 17 frames).
- **Motion:** TileContainerJuniors: onLand 0.42 s, win 0.58 s. The win plays the letter's own highlight sequence, a white stroke that traces the letter's bevels, with a magicBurstEffect behind.
- **Construction:** One sprite per letter plus a small highlight sequence drawn to fit that letter only; one skeleton with five skins.
- **Notes:** The highlight frames are small (59x87 to 100x76 px) and scaled up over the letter (inference from the sizes).
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 59% · saturation 49% · contrast 40% · warm 44% / cool 14%
- **Palette (measured):** #ffffff light yellow 36%, #49240c brown 14%, #d2a25d orange 8%, #c76e16 orange 7%, #532966 dark purple 6%, #16610c dark green 6%

### High symbols: map, pith helmet, chest, compass

`symbols-explorer` · atlas · 5 parts · largest 198×152 · sheet `sheets/symbols-explorer.webp`

- **Role:** The four high-paying symbols (tile6 to tile9).
- **Subject:** A rolled parchment treasure map with a dotted trail and a red X; a tan explorer's pith helmet with a leather strap; a wooden chest bound in grey steel with a fret-shaped lock plate; an eight-sided gold compass in a dark steel case, drawn as a base and a separate lid with a glass dome.
- **Style:** Adventure-film props in a chunky stylised-realistic manner: slightly inflated, thick rims, simple readable silhouettes.
- **Rendering:** Painted with firm gradients, crisp rim highlights and a thin dark outline; a faint yellow-green edge glow lifts each from the dark panel.
- **Colour:** Measured: orange-tan #ae7028 21%, light gold #f0bc59 16%, near-black #180b0f 15%, steel blue-grey #56596e 10% and #9396ad 5%, dark red #5b1b09 7%. Warm tan and gold for map, helmet and compass; cool steel for the chest and the compass case.
- **Lighting:** From the top (measured: top), with a second green-yellow rim from below as if from the jungle.
- **Ambience:** An expedition's kit laid out: the human side of the story, with no human shown.
- **Materials:** Parchment, felt and leather, wood and steel, gold and glass.
- **Variants:** Four symbols at about 170 to 200 px wide. The compass is two sprites (tile9Base 178x120, tile9Lid 162x93) so that it can open.
- **Motion:** TileContainerSeniors (37 bones): onLand 0.42 s, win 0.58 s, with dust, sparks and stars; the bone count and the two-part compass suggest each prop is bent or opened on a win rather than only scaled (inference from the file).
- **Construction:** Single sprites deformed by a shared rig with four skins; no frame sequence of their own.
- **Notes:** Stacks of the same symbol are common on the reels in play, so each prop is drawn to read when repeated four high.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 44% · saturation 63% · contrast 83% · warm 78% / cool 20% · brighter towards: top (3)
- **Palette (measured):** #ae7028 orange 21%, #f0bc59 orange 16%, #180b0f black 15%, #56596e blue 10%, #5b1b09 dark red 7%, #7d3b14 brown 7%

### Golden Coin: the cash symbol

`symbol-cash-coin` · atlas · 17 parts · largest 217×217 · sheet `sheets/symbol-cash-coin.webp`

- **Role:** The Golden Coin (tile11): carries a cash value of 1x to 10x, forms clusters that lock for three spins, and throws a coin at the statue on every spin (help text).
- **Subject:** A round gold coin with an orange brushed centre, a ring of square glyphs, and eight gold spikes like a sun or compass rose round the rim.
- **Style:** A sun-stone medallion simplified to a bright disc that a number can sit on.
- **Rendering:** Radial brushed-metal centre, flat glyph ring in red-orange, bevelled gold rim with pointed studs; a separate white glyph ring and a 15-frame white sweep for the shine.
- **Colour:** Measured: orange #e6780c 28%, white #ffffff 24% (highlight frames), red-brown #a02a07 16%, gold #edc727 9%, yellow #e4e654 7%.
- **Lighting:** No single direction measured; the face is lit evenly so the value on it stays readable.
- **Ambience:** Hot and sun-like against the dark panel; the brightest symbol.
- **Materials:** Gold, enamel.
- **Variants:** One coin (217x217 px), its inner glyph-ring highlight, and the 15-frame rim sweep. The logo's O and the spinning coin particle are the same design.
- **Motion:** TileCash: onLand 0.42 s, show 0.58 s, lock 0.67 s, loop 1.67 s, activate, collect and win 0.5 s each, with radial shines, sparks and the spinning coin sequence; TileCashSum shows and upgrades the value on it.
- **Construction:** One sprite with overlays; the value is text placed on the plain centre, in the jade comic numerals with a gold rim (Blambot FX Pro Heavy, by their look on the screens).
- **Notes:** Because one design serves the symbol, the particle, the logo and the statue's hoard, gold reads as one object across the whole game.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 62% · saturation 66% · contrast 59% · warm 74% / cool 1%
- **Palette (measured):** #e6780c orange 28%, #ffffff light yellow 24%, #a02a07 red 16%, #edc727 gold 9%, #e4e654 gold 7%, #5a1603 dark red 4%

### Empty marker: a green gem in silver scrolls

`symbol-gem` · atlas · 1 parts · largest 87×118 · sheet `sheets/symbol-gem.webp`

- **Role:** tile15. By the skeleton TileEmpty and the help text ("Golden Coin, Snake, and Empty symbols" in the Hold & Win), it marks an empty position in the bonus (inference from the names).
- **Subject:** A small upright diamond-cut green gem held in a silver setting with four scroll curls.
- **Style:** A quiet ornament, deliberately smaller and greyer than every paying symbol.
- **Rendering:** Faceted green with a light centre, brushed silver with a dark outline.
- **Colour:** Measured: greys #47453c 20% and #848379 20%, near-black #11190b 19%, pale green-grey #bec4b2 17%, dark green #166214 14%, green #35a029 5%.
- **Lighting:** Even; a highlight down the gem's centre.
- **Ambience:** Neutral: it should not be mistaken for a prize.
- **Materials:** Emerald, silver.
- **Variants:** One sprite, 87x118 px, less than half the width of a paying symbol.
- **Motion:** TileEmpty: onLand 0.42 s only.
- **Construction:** A single sprite on a three-slot skeleton.
- **Notes:** Seen in the bonus: one gem on each of the 36 positions until a coin locks there. Not used in the base game.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 41% · saturation 37% · contrast 80% · warm 5% / cool 47%
- **Palette (measured):** #47453c grey 20%, #848379 grey 20%, #11190b black 19%, #bec4b2 green 17%, #166214 dark green 14%, #35a029 green 5%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The stone serpent: statue, lava mouth, burning eyes

`stone-serpent` · atlas · 57 parts · largest 949×457 · sheet `sheets/stone-serpent.webp`

- **Role:** The game's one large figure: a stone snake's head that looks over the top of the reels and takes the coins thrown at it. The help text calls it "the snake statue above the slot" and says its changes are for show only.
- **Subject:** A colossal snake head carved from cracked grey-green stone, jaws wide, two fangs and a forked stone tongue, one pale blank eye, the neck coiling off to the right. Overlays for it: five stages of a glowing lava throat, three stages of a burning red eye for each side, two glow strokes (a pale lightning-like line and a red ember haze), 40 frames of flowing lava, and two heaps of gold coins.
- **Style:** Semi-realistic painted fantasy sculpture; heavy, with chiselled plates for scales. It is the most three-dimensional thing in the game.
- **Rendering:** Broad painted planes with hard cracks, moss-green and violet reflected light in the shadows and a wet highlight on the brow. The overlays are soft, blurred red-orange paintings meant to be blended over the stone.
- **Colour:** Measured over the unit (the lava frames dominate): red-orange #d04418 42%, near-black #150f12 20%, deep red #961f0b 11%, orange #f4982d 8%, stone grey #343331 6%. The statue itself is grey-green with violet shade; everything that wakes it is red and orange.
- **Lighting:** Top light on the stone from the upper right; the throat and eyes light it from inside. Measured light position is split between bottom and top-right for that reason.
- **Ambience:** Dormant menace: a ruin that is slowly heating up.
- **Materials:** Weathered stone, molten lava, ember glow, gold coin.
- **Variants:** One body (949x457 px); mouth glow in five steps (pseudoProgressMouth1 to 5); eye glow in three steps for the left and right eye; two coin heaps (coins1, coins2) for the hoard in front of it.
- **Motion:** Seen in play: each Golden Coin on the reels throws a coin up to the statue on every spin; its mouth and eyes flare red, lava cracks spread over the stone and gold coins heap up on both sides until the bonus starts. By the files: SceneCollector plays collect (0.75 s) when a coin arrives, SceneCollectorProgressBack raises the lava behind a reveal mask through four loop levels (1.67 s down to 0.83 s, so it pulses faster as it fills), SceneCollectorBackEffect runs the 40-frame lava flow on a 2.6 s loop, and activateBonus (0.58 s) with the activatorSkullFire burst opens the bonus.
- **Construction:** A still body with glow layers stacked over it in Spine; the lava is a 100x200 px frame sequence shown through lavaRevealMask. The sprite names (pseudoProgress...) say what the help text says: a progress display that is for show.
- **Notes:** Name of the fire sequence, activatorSkullFire, suggests the rig was first built for a skull in another game and re-dressed (inference from the name only).
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 33% · saturation 72% · contrast 50% · warm 82% / cool 15% · brighter towards: bottom (8), top-right (7), bottom-right (6)
- **Palette (measured):** #d04418 red 42%, #150f12 black 20%, #961f0b red 11%, #f4982d orange 8%, #343331 grey 6%


## Logo and title

The game's own wordmark.

### One-line logo for the help page

`help-logo` · atlas · 1 parts · largest 869×50 · sheet `sheets/help-logo.webp`

- **Role:** The title strip at the top of the shell's help page, from the provider's asset store.
- **Subject:** SERPENT GOLD: HOLD AND WIN on one line, with the coin as the O, in the same three colourings.
- **Style:** As the logo, flattened.
- **Rendering:** A small flat picture, 869x50 px.
- **Colour:** Measured: red #ba4d33 39%, olive #5d5232 13%, dark brown #30190e 10%, red #a11815 8%, gold #cea834 7%, green #348157 7%.
- **Lighting:** As the logo.
- **Ambience:** Plain.
- **Materials:** As the logo.
- **Variants:** One.
- **Motion:** None.
- **Construction:** A single WebP outside the game bundle.
- **Notes:** Shows that the three lines were designed to work in a row as well as stacked.
- **Measured:** mid-tone, vivid, warm, medium contrast · brightness 40% · saturation 69% · contrast 53% · warm 76% / cool 13% · brighter towards: top-left (1)
- **Palette (measured):** #ba4d33 red 39%, #5d5232 brown 13%, #30190e brown 10%, #a11815 red 8%, #cea834 gold 7%, #348157 green 7%

### Logo in three lines

`logo` · atlas · 41 parts · largest 1075×169 · sheet `sheets/logo.webp`

- **Role:** The game's title, large on the intro screen and small at the top left of the reels in play.
- **Subject:** Three stacked lines: SERPENT in green capitals filled with a snake-scale pattern; GOLD: in polished gold slab serif capitals, with a gap where the O is replaced by the sun coin; HOLD AND WIN in small red western-style slab capitals. Behind it a clump of dark ferns.
- **Style:** Adventure-film title lettering: wide spaced capitals with pointed serifs, each line in its own material.
- **Rendering:** SERPENT has a light-to-dark green gradient, a scale texture, a gold inner line and a dark outline; GOLD: is bevelled metal with a top highlight; HOLD AND WIN is flat red with a dark shadow. Two 18-frame white glint sequences cross the first two lines.
- **Colour:** Measured: near-black green #0d1c0b 30% (the ferns), gold #dfb33a 11%, olive-brown #866b33 8%, green #319633 7%, red #a11d14 4%.
- **Lighting:** Top light on the gold (measured: top).
- **Ambience:** A title card for an expedition.
- **Materials:** Snake skin, gold, painted wood.
- **Variants:** Landscape and portrait placements by skin; the three lines and the coin are separate, so the logo can be restacked.
- **Motion:** Logo: show and hide 0.33 s, idle 1.15 s with the glints and the coin turning (the 30-frame coin sequence is in its slots). GameSplash floats it on the intro screen on a 3.67 s loop with leaves and a star blink.
- **Construction:** Four sprites (three lines and logoCoin) with a fern backing and two highlight sequences.
- **Notes:** The coin as the O ties the title to the cash symbol.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 40% · saturation 71% · contrast 59% · warm 45% / cool 30% · brighter towards: top (4)
- **Palette (measured):** #0d1c0b black 30%, #dfb33a orange 11%, #866b33 brown 8%, #319633 green 7%, #a11d14 red 4%, #511c0a brown 4%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature messages

`feature-labels` · atlas · 7 parts · largest 1100×362 · sheet `sheets/feature-labels.webp`

- **Role:** The words of the two splashes: a new Snake unlocked, and the bonus starting.
- **Subject:** NEW SNAKE in three colourings (red-orange, green, steel blue); UNLOCKED in orange-gold; SYMBOL CAN NOW LAND ON THE REELS in small gold capitals; BONUS GAME in pale blue; GOLDEN COIN SYMBOLS LOCK ON THE REELS in small gold capitals.
- **Style:** The same slanted comic capitals as the win words; rule lines in a narrower version.
- **Rendering:** Gradient fills with a light inner edge, dark outline and warm outer glow.
- **Colour:** Measured: orange-tan #b97a3a 28%, gold #ecc646 15%, dark red #812311 15%, light cyan #a2dbf2 6%, blue #3980e1 5%, red #d5250a 4%, green #29c10b 3%. NEW SNAKE takes the colour of the snake that was unlocked.
- **Lighting:** Top (measured).
- **Ambience:** An announcement, read in a second.
- **Materials:** Enamel lettering.
- **Variants:** Seven localised pictures, about 1100 px wide each.
- **Motion:** FeatureSplash: show 5 s, in three skins (feature0 to 2): seen in play, the reels dim under a blue sparkling field, the unlocked snake appears large with its word, and the two lines of text sit above and below. FreeSpinsSplash: show 0.83 s, hide 0.58 s, with a 3.42 s loop of light behind: seen in play with the three Snakes in a row and the shell's START button.
- **Construction:** Text as pictures in imagesLocalized/en-GB, so each language ships its own set.
- **Notes:** The splash's snake is the symbol's own rig enlarged, not a separate illustration.
- **Measured:** mid-tone, vivid, warm, high contrast · brightness 53% · saturation 65% · contrast 63% · warm 78% / cool 19% · brighter towards: top (7)
- **Palette (measured):** #b97a3a orange 28%, #ecc646 gold 15%, #812311 dark red 15%, #a2dbf2 light cyan 6%, #362720 brown 5%, #3980e1 blue 5%

### Jackpot win: large plates and words

`jackpot-win` · atlas · 13 parts · largest 1102×422 · sheet `sheets/jackpot-win.webp`

- **Role:** The presentation of a jackpot in the bonus, and the message that one is close.
- **Subject:** The five jackpot plates redrawn large (about 464x292 px, as left halves) in purple, blue, green, red-orange and gold; the five names large (MINI, MINOR, MAJOR, GRAND, ULTIMATE); and the phrases JACKPOT and CONGRATS! in orange-gold and MORE FOR in green.
- **Style:** As the ladder: enamel plates in gold fret frames and slanted comic capitals.
- **Rendering:** Glossy flat gradients; the gold frame has a sharper bevel at this size.
- **Colour:** Measured: gold-orange #d6920d 16%, dark red #41120e 10%, red #a01305 6%, green #06920f 5%, blue #093cae 4%, purple #5d1d79 4%.
- **Lighting:** Top (measured).
- **Ambience:** A prize board lighting up.
- **Materials:** Gold, enamel.
- **Variants:** Five plates and five names by skin (jackpot0 to 4); three phrases as localised en-GB files.
- **Motion:** WinJackpot: show 0.75 s, hide 0.33 s, with white rays, a radial shine, sparks and stars. JackpotAnticipationSplash: show 2.5 s with coins, the word ULTIMATE and MORE FOR; by its parts it tells the player how many more symbols are needed (inference from the files).
- **Construction:** The same shapes as the ladder at about 1.2 times the size (464 against 398 px wide for the common plates), drawn again rather than scaled.
- **Notes:** Not reached in play on this run; read from the files.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 45% · saturation 78% · contrast 72% · warm 69% / cool 24% · brighter towards: top (7), top-left (2), right (1)
- **Palette (measured):** #d6920d orange 16%, #41120e dark red 10%, #a01305 red 6%, #06920f dark green 5%, #093cae blue 4%, #333d39 grey 4%

### Win words, win plates and the win bar

`win-tiers` · atlas · 11 parts · largest 1100×285 · sheet `sheets/win-tiers.webp`

- **Role:** The big-win presentation (BIG WIN, SUPER WIN, MEGA WIN), the TOTAL WIN of the bonus, and the small bar that shows a win amount under the reels.
- **Subject:** Three phrases in slanted comic capitals, BIG WIN in blue, SUPER WIN in cyan-teal, MEGA WIN in red-orange, and TOTAL WIN in blue to cyan; two dark stone plates in a carved frame with a gold snake head at the corner and gold fret feet (drawn as left halves to be mirrored); a smaller bar plate of the same make; a flat gold double-headed serpent ornament; a white divider line with a flare; and two white spray glows.
- **Style:** The jackpot words' brush lettering, on the frame's temple stonework.
- **Rendering:** Letters with a two-tone gradient, a light inner edge, a dark outline and a soft glow; plates painted like the reel frame, with the panel's calendar relief showing faintly inside.
- **Colour:** Measured: dark brown #211105 40% (plates), white #f6f6f5 14% (glows), blue #097ad9 5%, red #da0903 2%, light blue #a8c1f9 2%. The tiers go cool to hot: blue, cyan, red.
- **Lighting:** Top light on plates and letters (measured: top).
- **Ambience:** A sign raised in front of the temple wall; colour says how big.
- **Materials:** Enamel lettering, stone, gold.
- **Variants:** Three tier words by skin (label1 to 3) on two plate sizes (527x442 and 570x512 as halves); one total; one bar plate (292x241 as a half).
- **Motion:** WinBig: labelShow 1 s, sumShow 0.5 s, hide 0.33 s; WinBigEffects loops 1.67 s of spray glow and light streaks with one more skin (label4) than there are words; WinTotal: show 1 s, bangupEnd 0.83 s; WinBar: show 0.5 s, upgrade 0.33 s, on a 50-bone rig that also carries leaves and dust. Not reached in play: no win of the sessions was large enough for a tier, and the bonus was still running when the session ended, so TOTAL WIN was not seen either.
- **Construction:** Half plates mirrored by the engine; words are separate pictures (the total is a localised en-GB file); amounts are set in a bitmap font.
- **Notes:** The plate hides nothing of the scene: it is dark and sits over the reels, so the words carry all the colour.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, strong highlights · brightness 40% · saturation 66% · contrast 63% · warm 69% / cool 18% · brighter towards: top (5), top-left (1)
- **Palette (measured):** #211105 black 40%, #f6f6f5 white 14%, #097ad9 blue 5%, #da0903 red 2%, #a8c1f9 light blue 2%


## Effects

Frame sequences, glows, particles and transitions.

### Fire: bursts, pillars and embers

`fire` · atlas · 37 parts · largest 391×172 · sheet `sheets/fire.webp`

- **Role:** The heat of the statue and the jackpots: the burst that opens the bonus, fire rings on progress pieces, pillars that rise to a jackpot plate, and ember haze round the statue.
- **Subject:** An 18-frame fire burst (activatorSkullFire), an 11-frame upright fire pillar, an orange fire ring and a green one, four drifting red ember clusters, and two tiny flame particles.
- **Style:** Stylised hand-drawn fire with a white-hot core and a ragged orange edge.
- **Rendering:** Soft glow sprites meant for additive blending; the rings are a jagged outline round a flat hot centre.
- **Colour:** Measured: orange #fe7d21 47%, near-white #fefdef 20%, yellow-orange #fdd15a 18%, red #fc312a 5%, green #6bd501 4% (the green ring). Soft-edge share 80%.
- **Lighting:** Self-lit.
- **Ambience:** Volcanic, sudden.
- **Materials:** Flame, ember.
- **Variants:** Orange and green rings (the green one belongs to the spin counter's pieces, SpinCounterPiece); four ember clusters; pillars placed by eight animations for four ladder heights in landscape and portrait.
- **Motion:** JackpotProgressEffect: 0.33 to 0.73 s per pillar; JackpotProgressPiece and SpinCounterPiece: show 1 s.
- **Construction:** Two frame sequences and single glow sprites; colour is in the sprite here, unlike the white sparks.
- **Notes:** Seen in play: the green ring flying to the spin counter in the bonus. The orange bursts and pillars are read from the files.
- **Measured:** bright, vivid, warm, medium contrast, glow or soft effect, strong highlights · brightness 72% · saturation 64% · contrast 41% · warm 94% / cool 3% · brighter towards: right (1)
- **Palette (measured):** #fe7d21 orange 47%, #fefdef light gold 20%, #fdd15a orange 18%, #fc312a red 5%, #fbf5a8 light gold 4%, #6bd501 green 4%

### Spinning gold coin

`coin` · atlas · 30 parts · largest 144×146 · sheet `sheets/coin.webp`

- **Role:** The coin a Golden Coin symbol throws to the statue on each spin, the coin shower of wins, and the turning O of the logo.
- **Subject:** The sun coin of the cash symbol turning about its upright axis.
- **Style:** As the cash symbol.
- **Rendering:** A rendered 30-frame turn with a visible edge thickness and the highlight travelling across the face.
- **Colour:** Measured: orange-gold #d68c07 61%, gold #efc43c 16%, red-brown #af3802 12%, pale gold #f3d98a 5%.
- **Lighting:** Top and top-left (measured).
- **Ambience:** Bright and constant; there is nearly always a coin in the air.
- **Materials:** Gold.
- **Variants:** 30 frames, up to 144x146 px.
- **Motion:** ParticleCoin loops the turn in 0.97 s; SceneCollectorPiece flies one to the statue in 0.83 s.
- **Construction:** A frame sequence, small enough to be emitted many at a time.
- **Notes:** The frames narrow to 30x145 px edge-on, so the turn is a true rotation, not a squash.
- **Measured:** mid-tone, vivid, warm, medium contrast, hard-edged · brightness 59% · saturation 87% · contrast 51% · warm 100% / cool 0% · brighter towards: top (9), top-left (6), left (6)
- **Palette (measured):** #d68c07 orange 61%, #efc43c gold 16%, #af3802 brown 12%, #f3d98a gold 5%, #fbefd6 light orange 3%

### Wind streaks, dust, steam and rubble

`wind-dust-and-stone` · atlas · 35 parts · largest 629×590 · sheet `sheets/wind-dust-and-stone.webp`

- **Role:** The physical effects: streaks of mist inside the collector frames, dust when something heavy lands or the temple slides in, steam at the statue, and bits of stone.
- **Subject:** A 30-frame sequence of vertical white wind streaks, two white dust clouds (one billowing, one grainy), a soft steam puff, and two small mossy stones.
- **Style:** Painterly white vapour; the stones are painted like the statue.
- **Rendering:** Soft white on transparent (soft-edge share 99%); stones are hard-edged with green moss.
- **Colour:** Measured: white #f6f6f6 78% and #dbdbdb 20%.
- **Lighting:** None of its own.
- **Ambience:** Weight and age: things here are made of stone.
- **Materials:** Dust, vapour, rock.
- **Variants:** Two dust clouds, one steam puff, two stones, one wind sequence (150x300 px frames).
- **Motion:** By the files: windEffect (30 frames) plays inside the three collector frames (FeatureProgress); steamParticle rises behind the statue (SceneCollectorProgressBack); the stones fall with the temple's SlotTransition; the dust clouds serve that transition, symbol landings (TileContainerSeniors, TileWild), the jackpot plates and the win bar.
- **Construction:** White sprites tinted and faded by the engine.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 94% · saturation 0% · contrast 4% · warm 1% / cool 0%
- **Palette (measured):** #f6f6f6 white 78%, #dbdbdb white 20%

### Glows, rays, masks and motes

`light-and-particles` · atlas · 21 parts · largest 1024×1024 · sheet `sheets/light-and-particles.webp`

- **Role:** The light kit under everything: glows behind symbols and words, ray bursts, the drifting motes of the scene, and two technical textures for the water.
- **Subject:** Soft round and square glows, a radial shine and a ring shine, a starburst of rays, an expanding ring (whiteWave), vertical light streaks (splashLights), a snake-shaped soft glow, three small coloured light particles (white, blue, pink), a set of bokeh dots (bgParticles), white squares, a dark gradient strip, a 1024 px ripple map (seaDisplacement) and a black-and-white mask in the shape of the pool (bgDisplacementMaskNormal).
- **Style:** Plain optical effects.
- **Rendering:** White with soft falloff; greyscale for the two maps.
- **Colour:** Measured: greys and white only (#b4b4b4 61%, #fdfdfd 32%); the blue and pink particles are too small to register.
- **Lighting:** Self-lit.
- **Ambience:** Humid air and magic: motes drift in the base scene, and blue ones over the bonus water.
- **Materials:** Light.
- **Variants:** About twenty single sprites.
- **Motion:** BackgroundParticles and ForegroundParticles hold only emitter positions (normal and special skins); the motes, like the leaf, flame and flare particles, are named in no skeleton, so the engine's own particle emitters use them (inference). The ripple map is, by its name and shape, a displacement texture scrolled over the masked pool so the water moves without animation frames (inference).
- **Construction:** Three sprites (circularWhiteRays2, whiteGlow and a square glow) carry the same names as light sprites found pixel for pixel in other Octoplay games on earlier runs; they were not compared again here.
- **Notes:** The water effect costs two small textures and no painting: a cheap way to make a still background live.
- **Measured:** bright, muted, neutral, medium contrast, strong highlights · brightness 77% · saturation 1% · contrast 26% · warm 1% / cool 0%
- **Palette (measured):** #b4b4b4 grey 61%, #fdfdfd white 32%, #808080 grey 5%

### White sparks, stars and magic bursts

`sparks-and-bursts` · atlas · 59 parts · largest 195×219 · sheet `sheets/sparks-and-bursts.webp`

- **Role:** The generic sparkle of landings, wins and unlocks, tinted by the engine.
- **Subject:** A 28-frame smoky ring burst with glittering grains (magicBurstEffect), a 17-frame scatter of four-point stars (fireworkEffects), a 12-frame radial spark pop, a star field, and a four-point lens blink.
- **Style:** Clean motion-graphics sparkle, not themed.
- **Rendering:** White on transparent with soft falloff (soft-edge share 91%), for additive blending.
- **Colour:** Measured: white and light grey only (#dadada 79%, #fbfbfb 21%). Seen in play tinted blue behind the New Snake splash.
- **Lighting:** Self-lit.
- **Ambience:** Magic rather than fire.
- **Materials:** Light.
- **Variants:** Three sequences and two stills; colour comes from tinting.
- **Motion:** Used inside most symbol, counter and splash skeletons; lengths follow those animations (0.4 to 1 s).
- **Construction:** Small frames (up to 195x219 px) scaled up; one white set serves every colour.
- **Notes:** Octoplay's shell shares some light sprites between games; whether these three sequences are shared was not compared on this run.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 88% · saturation 0% · contrast 12% · warm 2% / cool 0%
- **Palette (measured):** #dadada white 79%, #fbfbfb white 21%

### Snake coils: the scale strips of the opening wipe

`snake-coil-transition` · atlas · 6 parts · largest 307×90 · sheet `sheets/snake-coil-transition.webp`

- **Role:** The transition from the intro screen into the game: huge snake bodies slide across the screen and uncover the reels.
- **Subject:** Six short strips of overlapping pointed scales, two each in blue, green and red, with a light spine on each scale and a yellow-green rim on the blue and green ones.
- **Style:** The Snake symbols' enamel scales, as a repeatable tile.
- **Rendering:** Glossy scales with a dark base; each strip tiles sideways.
- **Colour:** Measured: dark teal #183932 46%, dark red #631e08 22%, dark green #437027 7%, dark blue #204772 6%, red #a82511 6%.
- **Lighting:** From the lower left (measured).
- **Ambience:** Being inside the coils for a moment: the one time the snakes are bigger than the screen.
- **Materials:** Snake scale.
- **Variants:** Three colours, two strips each (307x90 px).
- **Motion:** GameIntroLoop (80 bones, 87 slots, skins blue, green, red) runs six coil animations of 1.53 to 2.05 s along a path (snakeCoilPath); seen in play, blue, red and green bodies cross the screen diagonally and part over the logo.
- **Construction:** A 307 px strip repeated along a Spine path into bodies thousands of pixels long: whole-screen snakes from six small sprites.
- **Notes:** The strongest economy in the package: the wipe that fills a 1280x720 screen is built from under 170,000 px of art.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 24% · saturation 73% · contrast 37% · warm 34% / cool 50% · brighter towards: bottom-left (6)
- **Palette (measured):** #183932 dark cyan 46%, #631e08 dark red 22%, #437027 dark green 7%, #204772 dark blue 6%, #a82511 red 6%, #2a63b2 blue 2%


## Game interface

Buttons, counters and panels drawn for this game.

### Three snake collector frames

`snake-collectors` · atlas · 7 parts · largest 305×243 · sheet `sheets/snake-collectors.webp`

- **Role:** The three panels at the right of the reels, one per Snake, each with a progress counter (the screen shows 0/25): the help text's "Snake progress counters".
- **Subject:** A dark red-brown backing panel; a carved stone bar with a square fret at each end and two set gems, in red, green and blue versions; and a thin glowing side strip in the same three colours.
- **Style:** The frame's carved stone language at small scale, colour-keyed by gemstones.
- **Rendering:** Painted stone with soft bevels; the gems are simple glossy cabochons; the side strips are soft light bars.
- **Colour:** Measured: red-brown #8a4734 44%, dark red #52190a 33%, near-black #1e0e04 7%, tan #bc906b 6%, with green #709e3b 2%. The key colours are carried by the gems and strips only.
- **Lighting:** From the top; the strips are self-lit.
- **Ambience:** Three shrines waiting to be woken.
- **Materials:** Stone, gemstone, light.
- **Variants:** Three colourings (0 red, 1 green, 2 blue) of the top bar and side strip on one backing.
- **Motion:** FeatureProgress: locked 2.5 s, unlock 0.83 s, show 0.83 s, loop 1.67 s, collect 0.5 s, activate 0.67 s, and separate loops for the intro screen and the bonus. In play the frames arrive empty, the snakes fade in dark inside them, and the red one unlocks with a burst of light and the word COLLECT.
- **Construction:** A frame of three sprites; the snake inside is the symbol's own parts (tile12 to tile14), drawn dark while locked. The counter is text over a small plate.
- **Notes:** Locked snakes are shown as dim silhouettes of the real art, not as padlocks: the player sees what is coming.
- **Measured:** dark, vivid, warm, medium contrast, hard-edged · brightness 27% · saturation 73% · contrast 41% · warm 91% / cool 6% · brighter towards: top (1)
- **Palette (measured):** #8a4734 red 44%, #52190a dark red 33%, #1e0e04 black 7%, #bc906b orange 6%, #5b6a21 dark green 3%, #709e3b green 2%

### Spin counter and lock counters

`spin-and-lock-counters` · atlas · 26 parts · largest 369×131 · sheet `sheets/spin-and-lock-counters.webp`

- **Role:** The bonus's counter of remaining spins (the help text: 3 free spins, reset whenever a symbol lands) and the small counter on a locked cluster (locked for 3 spins in the base game).
- **Subject:** A low gold arch plate with a fret at each end and a pointed finial; green glass segments that fill it (a middle sector and side pieces), with white shine versions and sequences of the same pieces shattering; the numerals 1, 2, 3 in slanted gold, in two sizes; and a dark red-brown disc with a gold rim.
- **Style:** A temple lintel used as a gauge; the numerals are the game's gold comic italics.
- **Rendering:** Bevelled gold with dark inner field; flat green glass with a lighter edge; the shatter frames are the same shapes cut into shards.
- **Colour:** Measured: green #5ca520 30%, dark olive #322d0a 28%, dark green #3a7216 14%, gold #e3b633 8%.
- **Lighting:** Top light on the gold (measured: top).
- **Ambience:** Clear and game-like: green means a spin is left.
- **Materials:** Gold, green glass.
- **Variants:** Three counter states by skin (spinCounter0 to 2); two shatter sequences (side 9 frames, middle 5 frames); lock counts 1 to 3 on their disc.
- **Motion:** SpinCounter: activate and deactivate 0.5 s, loop 1.17 s; a spent segment breaks in the shatter sequence. TileLockCounter: show, update, reset 0.5 s, hide 0.33 s (from the files).
- **Construction:** A plate with three green inserts and their shine and break overlays; numerals are sprites, not font glyphs.
- **Notes:** Seen in play: the lock disc with 3 or 2 at the corner of a chained cluster, and in the bonus the 1 2 3 arch on top of the Collect frame, with a green fire ring flying to it when a coin lands.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast · brightness 45% · saturation 76% · contrast 55% · warm 41% / cool 28% · brighter towards: top (3), top-left (1)
- **Palette (measured):** #5ca520 green 30%, #322d0a black 28%, #3a7216 dark green 14%, #e3b633 orange 8%, #9dab70 green 4%, #f1ea82 gold 4%


## Typography

Embedded fonts and lettering.

### Blambot FX Pro Heavy in jade: rounded comic numerals

`BlambotFXProHeavy` · atlas · 18 parts · largest 118×181 · sheet `sheets/BlambotFXProHeavy.webp`

- **Role:** A bitmap numeral font from the provider's shared font store, in a green fill with a gold rim. From its look, the value on each Golden Coin is set in it (inference from comparing the glyphs with the screens).
- **Subject:** Fat hand-drawn comic digits with uneven strokes, with x, comma, point, slash, plus, minus, asterisk and question mark.
- **Style:** Comic-book sound-effect lettering.
- **Rendering:** A turquoise-green fill with glassy diagonal facets, a dark green inner line and a thick gold outline.
- **Colour:** Measured: turquoise #4cd2ad 29%, dark olive #37340d 16%, dark green #126040 12%, light cyan #70f6db 9%, gold #dcb741 8% and #f8e77c 8%.
- **Lighting:** Top (measured).
- **Ambience:** Playful; the only cool-coloured numerals in the game.
- **Materials:** Jade or green glass, gold.
- **Variants:** 18 glyphs kept, up to 118x181 px; 92 more are listed as separate files and were not loaded.
- **Motion:** None of its own.
- **Construction:** As Anton: a bitmap font page with a JSON of frames.
- **Notes:** The jade fill matches the green snake and the SERPENT line of the logo.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 56% · saturation 71% · contrast 71% · warm 39% / cool 49% · brighter towards: top (13), top-left (3)
- **Palette (measured):** #4cd2ad cyan 29%, #37340d brown 16%, #126040 dark green 12%, #70f6db cyan 9%, #dcb741 gold 8%, #894c0c brown 8%

### Anton in gold: the tall italic numerals

`Anton` · atlas · 18 parts · largest 178×252 · sheet `sheets/Anton.webp`

- **Role:** A bitmap numeral font from the provider's shared font store. From its look, the slanted gold figures of the collector counters (0/25) are set in it (inference from comparing the glyphs with the screen).
- **Subject:** Tall condensed italic digits with x, comma, point, slash, plus, minus, asterisk and question mark.
- **Style:** A condensed poster face, slanted, coloured as gold.
- **Rendering:** A two-band gold fill, lighter at the top, darker below a hard horizon line, a thin light inner edge and a red-brown outline offset down and right.
- **Colour:** Measured: gold #f1c231 59%, red-brown #a83803 20%, light yellow #f5f36c 17%.
- **Lighting:** Top (measured).
- **Ambience:** Urgent and sporty.
- **Materials:** Polished gold.
- **Variants:** 18 glyphs kept here, up to 180x253 px. The font file lists 94 more glyphs that live in files of their own and load only when a text needs them; those were not loaded in this session and the reader's mis-cuts of them were removed.
- **Motion:** None of its own.
- **Construction:** A bitmap font page with a JSON of frames; glyph names are character codes.
- **Notes:** Shared store, so the face is not this game's own; its gold colouring may be (not established).
- **Measured:** bright, vivid, warm, high contrast, hard-edged, strong highlights · brightness 69% · saturation 78% · contrast 66% · warm 100% / cool 0% · brighter towards: top (16), top-right (1)
- **Palette (measured):** #f1c231 gold 59%, #a83803 brown 20%, #f5f36c gold 17%, #c68727 orange 2%

### Rubik Mono One in gold: the heavy prize numerals

`RubikMonoOneGold` · atlas · 15 parts · largest 192×221 · sheet `sheets/RubikMonoOneGold.webp`

- **Role:** A bitmap numeral font from the provider's shared font store. From its look, the multipliers on the jackpot ladder (25x to 5000x) and the win amounts over the reels are set in it (inference from comparing the glyphs with the screen).
- **Subject:** Very wide, heavy, upright digits with x, plus, minus, comma and point.
- **Style:** A geometric monospaced display face given a deep extruded base.
- **Rendering:** A bright gold face with soft light rays across it, a thin light rim, and a dark wine-red extrusion below with an orange lower edge.
- **Colour:** Measured: gold #f5d052 50%, dark wine #39030a 21%, orange-gold #e3ab1b 21%.
- **Lighting:** Top (measured), with the extrusion in shadow.
- **Ambience:** Solid and valuable: numbers as gold bars.
- **Materials:** Gold.
- **Variants:** 15 glyphs, about 192x220 px each; all are on the page (none listed as separate files).
- **Motion:** None of its own.
- **Construction:** A bitmap font page with a JSON of frames.
- **Notes:** The name carries its colouring (Gold), which suggests the shared store holds coloured variants of one face for several games (inference).
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 61% · saturation 77% · contrast 84% · warm 100% / cool 0% · brighter towards: top (14), top-right (1)
- **Palette (measured):** #f5d052 gold 50%, #39030a black 21%, #e3ab1b orange 21%, #ad731c orange 2%, #fded98 light gold 2%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `buyChances2x`: 1 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 802 components cut from 45 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
