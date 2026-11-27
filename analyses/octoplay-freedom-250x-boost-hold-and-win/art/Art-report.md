# Freedom 250x Boost Hold And Win: art report

octoplay · run `2026-11-27-0959-octoplay-freedom-250x-boost-hold-and-win` · captured 2026-11-27

Source: the provider's free-play demo, https://lobby-api.octoplay.com/platform/public/launch/freedom-250x-boost-hold-and-win

**Extracted:** 665 named components from 35 textures in 35 atlases; 43 Spine skeletons; 25 frame sequences (426 frames); 3 fonts. Grouped into 20 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

An American-anniversary slot dressed as a prize ceremony: a 3x3 glass board hung with bunting in front of a flag made of light, gold medals for every prize, three smiling presidents as collectors, and a Statue of Liberty that turns to gold coin by coin.

**Style.** Glossy realistic casino illustration with a sticker finish. Objects, medals and portraits are fully painted and idealised; the backdrop is flat graphic design. The portraits are warm caricature, close to animated-film character design, while the emblems and the statue stay realistic.

**Rendering.** Three kinds. Painted objects with smooth blended volume, fine detail and hard outer edges (emblems soft edge 0.147, jackpot coins 0.121, help pictures 0.037), each pay symbol on a thick white outline. Flat gradients for the backdrop and the board panel. White light sprites with feathered edges, tinted and added by the game (glows 0.898, sparks 0.88, fireworks 0.909). Lettering is extruded with a lighter upper band, a gold keyline and a navy or dark red block shadow.

**Colour.** Red, white and blue hold the stage; gold holds everything that pays. Measured over the art files: orange-gold #d7911e 12%, near-white #fbfaf5 11%, dark red #56090a 10%, red #a01c1b 9%, blue #2d78c2 8%, near-black navy #0d1830 8%, gold #f4c64a 4%, light blue #76bae6 3%. The backdrop is half navy, half red (hues blue 0.518, red 0.482); the board is pale sky blue so the warm symbols stand out. A second code names the prizes: purple Unity, blue Justice, green Freedom, red Glory, and the win tiers borrow those colours (magenta BIG, green SUPER, gold MEGA, blue TOTAL). Gold against full colour separates cash from jackpot: the Cash Collector and its coins are all gold, the Jackpot Collectors are in natural colour.

**Lighting.** Bright, even studio light from above and the upper left on every object, with small white hot spots on metal; no cast shadows between pieces except the drop shadows painted into the bunting and scroll. The backdrop glows from its centre behind the board and is the darkest layer (brightness 0.254), the symbols the brightest.

**Ambience.** A Fourth of July parade and an awards ceremony at once: festive, proud, polished, without irony. Fireworks open the game and confetti never stops.

**Shape language.** The five-point star (backdrop, medals, ribbons, the empty cell, the flying coin), the round medal, the scroll ribbon with curled ends, the laurel branch, and the stripe. The board is a plain rounded rectangle so the round and ribboned shapes read against it.

**Materials.** Polished gold above all (coins, medals, ribbons, laurels, the gilded statue), then satin bunting and flags, coloured glass domes, enamel lettering, parchment, feather, brass and wood, plumage, painted skin and cloth in the portraits, and weathered blue-grey metal for the statue before it is gilded.

**Typography and lettering.** Heavy sans capitals throughout. The logo sets FREEDOM upright in red and 250x BOOST and HOLD AND WIN slanted in blue and white, all with a gold keyline and navy block shadow. Jackpot names are arched on ribbons in their own colours. Numbers come from a provider bitmap font (the service calls it MyriadPro): white rounded numerals with a glowing gold keyline and dark red shadow. The words on collectors (CASH, JACKPOT, COLLECTOR) are sprites, the splash sentences are localised picture files, and small interface text is the provider shell's Poppins (Regular, SemiBold, Bold).

**Motion.** All motion is Spine 4.2.43: 43 skeletons in one bundle, moving, scaling, tinting and mesh-bending still pictures, plus 25 hand-drawn frame sequences (426 frames). Twenty-one of the sequences are white highlight sweeps drawn to the shape of one symbol layer; the others are the turning star coin, tumbling confetti and two spark animations. Seen in play: fireworks over the board as the intro gives way to the game; confetti drifting all the time; symbols blurring vertically on the reels; a Golden Coin throwing star coins up to the statue, whose gold rises a band at a time; a Jackpot Coin throwing a coin to the jackpot medallions, which flip; a gold ribbon unrolling across the board with the collected amount and a burst of coins; a thin gold line through a paying row with the winning symbols flaring white; a reel lit by a column of yellow-white light as a coin lands; the Jackpot Hold & Win, where the base game washes red under a BONUS GAME splash, fireworks and puffs of red, white and blue smoke cover the change, the backdrop and board turn red with a gold star in each empty cell and a red 1 2 3 ribbon in place of the logo, and a collected jackpot fills the screen with CONGRATS!, its medal on a purple glow, the amount and a shower of star coins; and the end of that bonus, where the sum leaves the collector, counts up on the gold ribbon over blue rays and MEGA WIN arrives in gold between two laurels under an arc of stars. The collectors' faces are rigged to blink and move (109 bones), read from the file. No skeleton frame is shown in this report, because the project's renderer is written for Spine 3.7.

**Variants and themes.** Three stage states from one set of parts by skin: normal (navy and red backdrop, pale blue board), bonus (all red, seen in the Jackpot Hold & Win) and special (all blue, the cash Hold & Win, seen only in the picture of the help page), each bonus with a respin ribbon in its colour. Four jackpot medals as recolours of one painting, at symbol size and again at win-screen size. One medallion kit for four collectors, gold for cash and full colour for jackpot. The statue in blue-grey and in gold. Every effect in white, tinted per use. Only the 1280x720 landscape layout was captured.

**How it is built.** Two atlas pages (4096x4096 and 4096x2477) hold 615 sprites, 426 of them animation frames; three backdrop pictures take about 30% of the first page. The board panel, the bunting and the flags are half-pieces mirrored by the rig. Symbols are layered (back, front, white outline, star, sweep). The statue's gilding is thirty rising bands of a gold repaint revealed by the rig. Six localised lettering files (en-GB), nineteen help pictures and a help logo from the provider's paytable service, the numeral font from its font service, six small shared helper textures.

**Consistency.** High. One gold, one star, one ribbon shape and one lettering construction run through logo, board, symbols, prizes and win screens, and the statue appears three times (scene figure, gilded figure, Cash Collector). The seams are small: the caricature presidents are in a lighter register than the realistic emblems, and the flat graphic backdrop is a different kind of picture from everything in front of it, which is what lets it sit back.

**What to take from it.** (1) A meter can be the scene's main figure. The Statue of Liberty gilds from the base up as coins land, by revealing thirty bands of one gold repaint; the rules say it changes nothing, and it still gives every coin a visible result. It needs one figure painted twice in exact register, not an animation. (2) Gold for what pays, the theme's colours for the stage. Red, white and blue stay in the backdrop, bunting and lettering; coins, medals, ribbons and collectors are gold, so a prize is found at a glance on a busy patriotic screen. (3) A white sticker outline lets detailed, warm, realistic objects read on a pale board. Each pay symbol ships its outline as a separate silhouette sprite. (4) One medal painting, four colours, two sizes covers the jackpot symbols, the jackpot display and the jackpot win screens; a rosette and a starred ribbon are all that mark the top prize. (5) The frame budget went to highlights, not to character animation: 21 of 25 sequences are white sweeps cut to one symbol or prize layer each, 345 of 426 frames. For AI art work this is a repeatable job: one sweep per finished symbol. (6) Build the board in halves. Panel, bunting and flags are drawn once and mirrored, which works because none of them carries lettering. (7) The theme is a dated national occasion (the 250 in the title, the flag, founding figures, Capitol, Liberty Bell), carried by a kit of emblems rather than a story. The same kit of board, medals, collectors and a gilding figure could carry another occasion with new emblems; that this was the studio's intent is inference. (8) From the same provider and framework as Mega Cash Boost: Hold & Win (same file layout, shell, Poppins, skeleton names such as SlotFrame, SceneCollector, TileWild, WinBig), and again every picture is the game's own. Where that game was neon with no scene and no figure, this one is fully painted: the framework fixes the structure and leaves the art direction free. (9) Real historical figures appear as friendly caricatures on symbols. It suits this market and occasion; a studio taking the idea should pick figures and tone deliberately for its own markets.

## Colour, measured

The game's own art (provider interface left out): mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 47% · saturation 66% · contrast 52% · warm 58% / cool 33% · brighter towards: top (39), left (10), top-right (8)

Palette: #d7911e orange 12%, #fbfaf5 light yellow 12%, #56090a dark red 11%, #a01c1b red 10%, #2d78c2 blue 9%, #0d1830 black 8%, #f4c64a orange 5%, #76bae6 blue 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 25% | 76% | 48% | 47% / 52% | #53090d dark red 20%, #0d1931 dark blue 18%, #9b1e29 red 14% |
| Reel board | 1 | 46% | 68% | 39% | 42% / 52% | #216ebb blue 25%, #640202 dark red 21%, #f3f5f5 light cyan 10% |
| Symbols | 6 | 67% | 49% | 53% | 66% / 7% | #fefcf6 light gold 31%, #eeb333 orange 14%, #7b380c brown 11% |
| Characters | 1 | 68% | 62% | 49% | 83% / 17% | #db921c orange 51%, #f7d578 orange 16%, #f7f6eb light yellow 13% |
| Logo and title | 2 | 43% | 65% | 76% | 62% / 37% | #d60809 red 14%, #5f4535 brown 10%, #0f2153 dark blue 10% |
| Win celebrations and banners | 3 | 50% | 74% | 64% | 69% / 20% | #f1ba3d orange 16%, #faf7ef light orange 8%, #c40805 red 8% |
| Effects | 3 | 87% | 0% | 7% | 10% / 1% | #fefefe light orange 81%, #676767 grey 10%, #0f0f0f black 5% |
| Game interface | 2 | 47% | 70% | 69% | 61% / 29% | #71230a dark red 15%, #f5c83e gold 11%, #cc0b0b red 10% |
| Typography | 1 | 76% | 55% | 90% | 100% / 0% | #fefef5 light gold 36%, #f7d01d gold 30%, #611702 dark red 16% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Backdrop: the flag as a field of light

`backgrounds` · atlas · 3 parts · largest 1375×1255 · sheet `sheets/backgrounds.webp`

- **Role:** The full-screen backdrop behind the board, in three versions the Backgrounds skeleton switches by skin: bgNormal for the base game, bgBonus, all red, for the Jackpot Hold & Win (seen in play), and bgSpecial, all blue, for the cash Hold & Win (not reached in play; the help page's Hold & Win picture shows the blue board and a blue counter ribbon).
- **Subject:** An abstract Stars and Stripes: rows of pale five-point stars on dark navy receding to the upper left, and broad red and white stripes fanning out to the lower right, with a soft pool of light in the middle. No place, no horizon, no object.
- **Style:** Graphic poster design rather than a painted scene: the flag reduced to its two motifs and bent into perspective rays.
- **Rendering:** Smooth vector-like gradients with translucent overlapping bands; the stars are flat shapes at low opacity. The pictures are opaque rectangles (measured soft edge 0.0) and are shipped small, 1375x1255, to be enlarged over the 1280x720 stage.
- **Colour:** Measured over the three: dark red #53090d 20%, dark navy #0d1931 18%, red #9b1e29 14%, blue #154b8d 14%, mid blue #2e78ca 11%, pale blue #71bde8 5%; hues split blue 0.518, red 0.482. bgNormal is half navy and half red; bgSpecial is all blue with a cyan-white centre; bgBonus is all red.
- **Lighting:** A soft glow in the centre of each picture, where the board sits, falling to near-black at the upper left corner; the stripes read as beams coming from the lower left. Brightness 0.254: the darkest unit of the game, so everything in front stands out.
- **Ambience:** Patriotic rally or Fourth of July stage: ceremonial, loud, festive, with no irony.
- **Materials:** Light and printed cloth; nothing has a surface texture.
- **Variants:** Three colour versions of one composition (two-colour, all blue, all red), the same star rows and stripe fan in each.
- **Motion:** The pictures do not move. BackgroundEffects (loopLight 7.58 s) fades white glows over them, and three confetti emitters (ParticleConfettiRed, Blue and White, each a 1 s loop of the 30-frame confetti sprite) drift small red, blue and white discs across the stage, seen in every base-game screen.
- **Construction:** Three sprites on the first atlas page, about 30% of that 4096 px page; one slot in the Backgrounds skeleton whose skin picks the picture.
- **Notes:** The backdrop carries the theme by colour and two shapes only; the recognisable objects are all kept for the board, the statue and the symbols.
- **Measured:** dark, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 25% · saturation 76% · contrast 48% · warm 47% / cool 52% · brighter towards: top-right (1), right (1), bottom-right (1)
- **Palette (measured):** #53090d dark red 20%, #0d1931 dark blue 18%, #9b1e29 red 14%, #154b8d blue 14%, #2e78ca blue 11%, #683d4f magenta 8%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### Reel board: glass panel, gold scroll and bunting

`reel-board` · atlas · 12 parts · largest 492×764 · sheet `sheets/reel-board.webp`

- **Role:** The 3x3 reel area and its dressing, plus the helpers the board uses (cell guides, the glow square behind a landing symbol, the win-line pieces).
- **Subject:** A tall glassy panel with a thin bevelled rim and two faint vertical dividers; a wide gold scroll banner arching over its top; pleated red, white and blue bunting with rosette bows and gold tassels hanging down both sides and across the bottom; a gold star that marks each empty cell of the bonus board (tile19, seen in the Jackpot Hold & Win).
- **Style:** Glossy casino illustration: clean hard shapes for the panel, soft airbrushed cloth and metal for the dressing.
- **Rendering:** The panel is a flat vertical gradient with a lighter centre band and a one-pixel highlight rim; the bunting and scroll are fully modelled with folds, speculars and a dark drop shadow painted into the sprite. Soft edge 0.103.
- **Colour:** Measured: blue #216ebb 25%, dark red #640202 21%, near-white #f3f5f5 10%, light blue #7bbbec 10% and #b3d7f1 9%, red #a40605 5%. The base game panel is pale sky blue; the Jackpot Hold & Win panel is deep red (seen); the third is saturated blue (the cash Hold & Win, seen only in the help page's picture).
- **Lighting:** Panels lit from the top and centre; cloth and scroll lit from the upper left with warm highlights.
- **Ambience:** A decorated stage or parade float: festive, tidy, official.
- **Materials:** Glass or enamel panel, polished gold ribbon, satin bunting, gold cord and tassels.
- **Variants:** Three panels (slotBgNormal, slotBgSpecial, slotBgJackpotBonus): the base one is plain with two dividers, the two bonus ones are ruled into nine cells. The dressing is the same in all three.
- **Motion:** SlotBackgrounds loops 4.67 s (read from the file; no change of the dressing is visible between the still frames taken); SlotFrame idle 1.67 s adds white glows on the ribbon; ReelEffectNormal and ReelEffectSpecial flash the glow square behind a landing coin (0.67 and 0.5 s).
- **Construction:** Everything is built in halves and mirrored: each panel sprite is the left 492 px of the board and the skeleton places it twice (slots slotBg1 and slotBg2); the side bunting (219x829) and the bottom swag (645x380) are also placed left and right. Only the gold scroll (1257x274) is one whole piece. The win line is two shared 25 px gold pieces stretched by code.
- **Notes:** Mirroring halves the texture cost of the largest foreground piece; it works because the board has no lettering and no directional light.
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged · brightness 46% · saturation 68% · contrast 39% · warm 42% / cool 52% · brighter towards: top (2), left (2), top-right (1)
- **Palette (measured):** #216ebb blue 25%, #640202 dark red 21%, #f3f5f5 light cyan 10%, #7bbbec blue 10%, #b3d7f1 light blue 9%, #a40605 red 5%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Help-page symbol pictures

`help-symbol-pictures` · atlas · 19 parts · largest 225×225 · sheet `sheets/help-symbol-pictures.webp`

- **Role:** The nineteen symbol pictures of the help window, one flattened 225 px picture per symbol, served by the provider's help service.
- **Subject:** All symbols as the player meets them, assembled: the eight emblems with their white outline, the Wild seal, the Golden Coin, the Cash Collector, the three Jackpot Collectors with their words, the four Jackpot Coins with their names, and the gold star.
- **Style:** As the symbols.
- **Rendering:** Flattened composites of the layered symbols; hard edges (soft edge 0.037).
- **Colour:** Measured: light gold #f6d98b 18%, brown #79380d 15%, cream #fcf6e8 10%, golds #e8b347 and #b7721d 10% each, red #d3130c 3%; orange 0.669 of the hue. Seen together, the set is overwhelmingly gold, with red, white and blue as accents.
- **Lighting:** Lit from the top.
- **Ambience:** As the symbols.
- **Materials:** As the symbols.
- **Variants:** Nineteen pictures, tile1 to tile19.
- **Motion:** None; stills.
- **Construction:** Nineteen separate WebP files from the provider's paytable service.
- **Notes:** The quickest reference for what each numbered tile is, and for how the layered parts of a collector look when assembled.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 56% · saturation 60% · contrast 81% · warm 89% / cool 10% · brighter towards: top (4), top-left (1)
- **Palette (measured):** #f6d98b light orange 18%, #79380d brown 15%, #fcf6e8 light orange 10%, #e8b347 orange 10%, #b7721d orange 10%, #ca923f orange 7%

### Golden Coin: the cash prize symbol

`symbol-golden-coin` · atlas · 37 parts · largest 238×236 · sheet `sheets/symbol-golden-coin.webp`

- **Role:** The Golden Coin (tile10), which lands on the outer reels carrying a cash value; and the small star coin that flies from it to the statue.
- **Subject:** A gold coin embossed with a waving flag on a pole, a rim of small stars and a ribbon with a star at the bottom; the value is set on it in the numeral font (a white 2 seen in play). The flying coin is a plain gold disc with a five-point star.
- **Style:** Minted-coin relief, tone on tone.
- **Rendering:** Embossed relief in a single hue with bright rim highlights; a ridged edge texture for the coin seen side-on. Soft edge 0.139.
- **Colour:** Gold only. Measured: gold #f3ce4c 25%, brown #8e4b09 24%, orange-gold #dba431 19%, pale gold #fefdee 15%, #be7e1e 8%. No cool colour at all (cool 0.0).
- **Lighting:** Lit from the right and upper right, with a specular arc on the rim.
- **Ambience:** Treasure; the plainest and warmest symbol, so its number reads first.
- **Materials:** Polished gold.
- **Variants:** One face. Side pieces (tileCoinSide1, a ridged disc, and tileCoinSideRectangle, a ridged strip) let the rig show the coin edge-on while it flips.
- **Motion:** Two frame sequences: coinStar, 15 frames of the star coin turning through edge-on, used by ParticleCoin (0.5 s loop) and SpinCounterPiece; tileCashHighlight, an 18-frame sweep. TileCash (20 bones): onLand 0.42 s, collect 0.5 s, collectProgress 0.83 s, loop 2 s. Seen in play: the landed coin throws star coins up to the statue.
- **Construction:** 37 sprites: one face, edge pieces, 15 turn frames, 18 sweep frames.
- **Notes:** The coin face is shared in idea with the jackpot coins (same laurel-and-star rim language), which keeps cash and jackpot prizes in one family.
- **Measured:** bright, vivid, warm, medium contrast, hard-edged, strong highlights · brightness 67% · saturation 66% · contrast 45% · warm 95% / cool 0% · brighter towards: right (1), top-right (1)
- **Palette (measured):** #f3ce4c gold 25%, #8e4b09 brown 24%, #dba431 orange 19%, #fefdee light gold 15%, #be7e1e orange 8%, #f9e99e light gold 8%

### Collectors: Liberty in gold and three presidents' portraits

`symbols-collectors` · atlas · 135 parts · largest 306×232 · sheet `sheets/symbols-collectors.webp`

- **Role:** The four collector symbols of the middle reel. tile11 is the Cash Collector (a gold Statue of Liberty bust), tile12, tile13 and tile14 are the Jackpot Collectors: Abraham Lincoln, George Washington and Benjamin Franklin, as the help pictures and the game's own description name them.
- **Subject:** Round medallions: a bust in front of a waving flag, inside a navy ring of gold stars, with a winged ribbon and gold star below and the words CASH COLLECTOR or JACKPOT COLLECTOR across the lower half. The three men are friendly caricatures with enlarged heads and broad smiles: Lincoln with beard and bow tie, Washington in a blue coat with gold buttons and a white wig, Franklin bald on top with long hair and small round glasses.
- **Style:** Warm caricature portrait painting, close to animated-film character design; the Liberty bust is the scene statue's gold repaint.
- **Rendering:** Soft, fully blended skin and cloth with sharp detail in hair and eyes; the medallion parts are crisp. The unit mixes both (soft edge 0.258).
- **Colour:** Measured: pale gold #fdfaef 32% (shine and highlight sprites), gold #f2b125 22%, #f6cd81 11%, #c87a0e 9%, brown #904712 7%, red #de0e06 2%. The Cash Collector is all gold with a gold-toned flag and blue lettering; the Jackpot Collectors are in natural colour in front of a red, white and blue flag with red JACKPOT lettering. Gold means cash, full colour means jackpot.
- **Lighting:** Portraits lit from the upper left with a soft warm key and a rim on the hair; the gold bust has white hot spots.
- **Ambience:** Affectionate and celebratory; the founding figures are made approachable, not solemn.
- **Materials:** Skin, wool and linen, hair, gold; enamel ring and satin ribbon.
- **Variants:** One medallion kit (plate, ring with stars, flag, ribbon with leaves, text) used by all four; a gold flag for cash and a coloured flag for jackpot; four busts. The word plates are CASH, COLLECTOR and JACKPOT as separate sprites. tileCollectorLock is a gold plaque (306x232) that fills the cell behind a collector locked in the bonus (seen behind Franklin in the Jackpot Hold & Win).
- **Motion:** The most heavily rigged unit: TileCollector has 109 bones and 64 slots, with separate eyes, eyelid patches, hair pieces, Lincoln's curl and Franklin's glasses, so the faces blink and move (idle and loop 2 s, onLand 0.42 s, win 0.58 s, activate 0.58 s). Seven highlight sweeps of 10 to 18 frames cover the bust, the ring, the ribbon, the flag and each word. TileCollectorSum shows the collected amount on the collector (sumShow 0.42 s, sumUpgrade 0.5 s); seen in play as 25 and then 50 in the numeral font over Franklin. Seen as well: the Cash Collector landing beside a Golden Coin and the amount arriving on a gold ribbon.
- **Construction:** 135 sprites: shared medallion parts, four busts with their face parts, 103 highlight frames.
- **Notes:** The only characters with faces in the game, and they are symbols, not a mascot. Likenesses of real historical figures are used; a studio copying the approach should choose its own figures with care.
- **Measured:** bright, saturated, warm, medium contrast, strong highlights · brightness 70% · saturation 52% · contrast 46% · warm 73% / cool 6% · brighter towards: top (2), top-left (2), top-right (2)
- **Palette (measured):** #fdfaef light gold 32%, #f2b125 orange 22%, #f6cd81 orange 11%, #c87a0e orange 9%, #904712 brown 7%, #25120f black 4%

### Jackpot Coins: Unity, Justice, Freedom, Glory

`symbols-jackpot-coins` · atlas · 46 parts · largest 247×239 · sheet `sheets/symbols-jackpot-coins.webp`

- **Role:** The four Jackpot Coin symbols (tile15 to tile18), which land on the outer reels carrying a named jackpot; the same parts build the four jackpot medallions above the reels.
- **Subject:** A gold medal with a laurel wreath, a star at the bottom and a ring of small stars, holding a domed coloured centre like a gem or a button; a gold scroll ribbon across it with the jackpot's name in arched letters.
- **Style:** Glossy award-medal illustration.
- **Rendering:** Polished gold with deep modelling; the centre is a glass dome with a broad top highlight; lettering is extruded with a gold keyline. Hard edges (soft edge 0.121).
- **Colour:** One colour per jackpot on a common gold body: Unity purple, Justice blue, Freedom green, Glory red, each repeated in its lettering. Measured: gold #f3c14d 22%, #b36412 16%, dark red #831703 11%, dark green #1c8003 7%, dark blue #054988 6%, dark magenta #7a0284 6%.
- **Lighting:** Lit from above; the dome highlights sit at the top of each centre.
- **Ambience:** Prize-giving: medals and rosettes.
- **Materials:** Gold, coloured glass or enamel, gold ribbon.
- **Variants:** Four recolours of one medal; two ribbons (tileRibbon, and tile18Ribbon with a star at each end for Glory); four name plates.
- **Motion:** Two 18-frame highlight sweeps (medal and ribbon). The symbol uses the TileCash skeleton with a skin per coin. Seen in play: Unity and Justice coins landing in the base game and throwing a small coin up to the jackpot display, and Unity and Justice coins held on the red bonus board.
- **Construction:** 46 sprites: four medals, two ribbons, four names, 36 sweep frames.
- **Notes:** The four colours are the game's second colour code after red, white and blue, and the only place green and purple appear.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged, strong highlights · brightness 53% · saturation 74% · contrast 64% · warm 71% / cool 12%
- **Palette (measured):** #f3c14d orange 22%, #b36412 orange 16%, #831703 dark red 11%, #fbfaf3 light yellow 8%, #1c8003 dark green 7%, #054988 dark blue 6%

### Wild: the eagle seal

`symbol-wild` · atlas · 28 parts · largest 276×276 · sheet `sheets/symbol-wild.webp`

- **Role:** The Wild symbol (tile9), which substitutes for the pay symbols; seen stacked on a reel in play.
- **Subject:** A round seal modelled on the Great Seal: an eagle with spread wings and a striped shield, olive branch and arrows, a scroll reading E PLURIBUS UNUM, a ring of stars on a navy border and a gold rope rim; the word WILD across the lower part in cream letters.
- **Style:** Engraved-medal illustration, the most detailed drawing among the symbols.
- **Rendering:** Fine line and tone work inside a crisp circle; the letters are flat cream faces with a gold keyline and navy drop edge, each with its own white outline.
- **Colour:** Cream and gold with navy and small reds. The measured palette is led by the white helper shapes (#fefdfa 61%); the picture itself measures cream #ddd3bc, tan #cbb584, brown #543518 and navy #0d205e.
- **Lighting:** Even frontal light; a soft highlight across the upper half of the disc.
- **Ambience:** Official and ceremonial.
- **Materials:** Painted enamel medal with a gold rim.
- **Variants:** One design. The pieces: the seal (tile9Back, 266x266), a white stroke disc, a black lower crescent that darkens the seal under the word, and the four letters W, I, L, D with outlines for W and D.
- **Motion:** A 19-frame highlight sweep over the seal; TileWild (18 bones): onLand 0.42 s, loop 2 s, win 0.58 s. The letters are separate so the rig can bounce them one by one (inference from the separate sprites and bones).
- **Construction:** 28 sprites: seal, strokes, four letters, sweep frames.
- **Notes:** The word is not painted into the seal, so it can be localised or animated without redrawing the medal.
- **Measured:** bright, muted, warm and cool mixed, medium contrast, strong highlights · brightness 76% · saturation 18% · contrast 38% · warm 28% / cool 8%
- **Palette (measured):** #fefdfa light orange 61%, #080403 black 10%, #ddd3bc light orange 6%, #cbb584 orange 5%, #543518 brown 4%, #0d205e dark blue 4%

### Pay symbols: eight American emblems

`symbols-emblems` · atlas · 182 parts · largest 220×228 · sheet `sheets/symbols-emblems.webp`

- **Role:** The eight paying symbols (tile1 to tile8), stacked on the reels. By the help page, from low to high: laurel wreath, quill in an inkwell, striped shield, torch, scroll with quill, the Capitol dome, the Liberty Bell and the bald eagle.
- **Subject:** Single objects on no tile: a gold laurel wreath, an orange feather quill in a blue-and-gold inkwell, a gold-rimmed shield with a blue chief, one star and red and white stripes, a gold torch with flame, a rolled parchment with a quill, the Capitol dome over a star-and-stripes ribbon, the cracked bell on its wooden yoke, and the eagle's head and breast over a ribbon with three gold stars.
- **Style:** Sticker-style casino illustration: realistic objects, slightly idealised, each with a thick white outline that separates it from the pale board.
- **Rendering:** Smoothly painted volumes with fine surface detail (feather barbs, columns, wood grain, the bell's crack) and bright speculars; the outline is a separate white silhouette sprite behind each object. Hard edges (soft edge 0.147).
- **Colour:** Gold, parchment, brown, red and navy on a white outline. The measured palette is dominated by the white outline and highlight sprites (#fefefc 61%); the object colours measured are parchment #e3d4bb, browns #904414 and #5b240a, golds #efce88 and #f4c347. Blue appears only as an accent (hue share 0.071).
- **Lighting:** Lit from the top and upper left (measured on 7 of 9 lit parts), with a warm key and small white hot spots on metal.
- **Ambience:** Museum-shop Americana: dignified objects made friendly and shiny.
- **Materials:** Polished gold and brass, parchment, feather, painted enamel, stone, wood, plumage.
- **Variants:** Eight designs with no colour variants. Most are split into a Back and a Front layer (the bell and its yoke, the dome and its ribbon, the eagle and its ribbon, the scroll and its quill, the quill and its inkwell, the torch and its flame); the dome and eagle ribbons carry a separate gold star.
- **Motion:** Nine white highlight sweeps of 14 to 18 frames each, one per symbol layer, played over the object on a win; TileContainer (27 bones) has one win animation of 0.58 s. Seen in play: a paying line is drawn as a thin gold line with the amount in the numeral font, the winning symbols flare white with small stars around them, and a reel on which a coin lands is lit by a column of yellow-white light.
- **Construction:** 182 sprites, 152 of them highlight frames. Each symbol is two or three colour layers, their white outline silhouettes, and a sweep drawn to that symbol's shape; all in one skeleton with a skin per symbol.
- **Notes:** The white sticker outline is what lets detailed, warm objects read on a pale blue board. The hand-drawn sweep per symbol is the main animation cost of the game.
- **Measured:** bright, muted, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 80% · saturation 24% · contrast 32% · warm 36% / cool 3% · brighter towards: top (4), top-left (3), left (2)
- **Palette (measured):** #fefefc light orange 61%, #e3d4bb light orange 6%, #904414 brown 5%, #efce88 orange 4%, #5b240a brown 4%, #1f0a08 black 3%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The Statue of Liberty: scene character and coin collector

`statue-of-liberty` · atlas · 49 parts · largest 638×859 · sheet `sheets/statue-of-liberty.webp`

- **Role:** The game's one large figure, standing behind the board at the upper right. It is the visible meter of the Golden Coins: every coin that lands flies up to it and the statue turns to gold from the base upward (the help text: "adds a coin to the pile above the slot … purely for visual entertainment").
- **Subject:** The Statue of Liberty from the waist up, three-quarter view, looking up and to the left, crown of seven rays, the tablet in the left arm; the torch arm rises out of the picture. Behind it in the game hang two crossed flags (winTotalFlag, shared with the win screens).
- **Style:** Realistic digital painting, idealised: a smooth youthful face rather than the monument's severe one, with crisp drapery folds.
- **Rendering:** Fully painted volume with fine fold detail; the lower edge fades out softly so the figure can sink behind the board. The gold version repeats the same drawing in polished metal with sharp speculars.
- **Colour:** Two materials of one figure. Measured over the unit: orange-gold #db921c 51%, light gold #f7d578 16%, near-white #f7f6eb 13%, steel blue #466e8c 4%, pale blue-grey #b8c8cb 4%. The resting statue is the cool blue-grey part; the gold pieces dominate the count because there are thirty of them.
- **Lighting:** Lit from the left (measured on 6 parts) with a cool sky light; the gold version carries warm reflected light and white hot spots.
- **Ambience:** Monumental and optimistic; the turn to gold makes it a trophy.
- **Materials:** Weathered copper shown as blue-grey stone-like metal; then polished gold.
- **Variants:** Blue-grey base figure (sceneCollector, 638x859); thirty gold pieces sceneCollectorProgress00 to 29, each a horizontal band of the gold statue higher than the one before, the last being the whole gold bust (631x605); a white shine pass (sceneCollectorShine); and a 17-frame highlight sweep in white.
- **Motion:** Seen in play: gold coins with a star fly from a landed Golden Coin to the statue, and the gold reaches higher after each one (waist after two coins, shoulders later). From the skeleton SceneCollector (81 bones, 73 slots): activate 0.45 s, collect 0.58 s, track-1/progress 5 s stepping two slots of gold bands, track-2/loopSparkles 1.5 s (seven blink stars), track-3/loopOutline 16.67 s moving forty small glows along a path around the figure, loopGs 2.5 s for the intro. No skeleton frame is drawn here (Spine 4.2.43).
- **Construction:** One painted figure, one gold repaint of it cut into thirty rising bands with ragged upper edges, so the rig can reveal the gold step by step without a shader; masks at top and bottom. 49 sprites.
- **Notes:** A progress meter told as a picture: the art carries the anticipation the rules say has no effect on the odds. The gold repaint keeps every fold of the original, so the two register exactly.
- **Measured:** bright, vivid, warm, medium contrast, strong highlights · brightness 68% · saturation 62% · contrast 49% · warm 83% / cool 17% · brighter towards: left (6)
- **Palette (measured):** #db921c orange 51%, #f7d578 orange 16%, #f7f6eb light yellow 13%, #466e8c blue 4%, #b8c8cb light cyan 4%, #eee5c3 light gold 3%


## Logo and title

The game's own wordmark.

### Help-page logo

`help-logo` · atlas · 1 parts · largest 2849×440 · sheet `sheets/help-logo.webp`

- **Role:** The title strip at the top of the help window, served by the provider's help service rather than the game atlas.
- **Subject:** The one-line logo FREEDOM 250x BOOST with laurel and flag ribbon at each end, the same design as the in-game strip.
- **Style:** As the logo.
- **Rendering:** As the logo, at four times the size (2849x440), so the letter construction is easy to study: face, upper band, gold keyline, navy block shadow.
- **Colour:** Measured: red #d50909 14%, brown-gold #604535 11%, dark navy #102355 9%, light cyan #bae4f7 7%, blues #14518f and #0983cb 6% each; hues red 0.38, blue 0.339, orange 0.282.
- **Lighting:** Lit from the top right.
- **Ambience:** As the logo.
- **Materials:** Enamel and gold.
- **Variants:** One picture.
- **Motion:** None; a still.
- **Construction:** A single WebP from the provider's shared paytable service.
- **Notes:** The largest copy of the logo the game ships; a better reference than the 712 px in-game strip.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 42% · saturation 66% · contrast 75% · warm 65% / cool 35% · brighter towards: top-right (1)
- **Palette (measured):** #d50909 red 14%, #604535 brown 11%, #102355 dark blue 9%, #901516 red 8%, #edc465 orange 7%, #bae4f7 light cyan 7%

### Logo: FREEDOM 250x BOOST / HOLD AND WIN

`logo` · atlas · 5 parts · largest 712×119 · sheet `sheets/logo.webp`

- **Role:** The game's title, on the gold scroll above the reels in play and stacked on the intro.
- **Subject:** Three lines of lettering: FREEDOM in red, 250x BOOST in ice blue and blue, HOLD AND WIN in white; a gold laurel branch that sits at each end.
- **Style:** Bold American sports or campaign lettering: heavy sans capitals, the second and third lines slanted forward.
- **Rendering:** Extruded letters with a flat face, a lighter upper band, a gold keyline and a dark navy block shadow; hard edges (soft edge 0.143).
- **Colour:** Measured: dark navy #0d1a4b 15%, red #d50607 13%, near-white #f7f9f7 8%, gold #e8af1f 7%, light cyan #b6e2f6 7%, blue #0880c8 6% and #125092 5%. Red, white and blue in that order down the three lines, tied together by the gold outline.
- **Lighting:** Top-lit faces with a hard horizon line in each letter.
- **Ambience:** Confident and celebratory, in the voice of a sports broadcast title.
- **Materials:** Enamelled metal letters with gold trim; a polished gold laurel.
- **Variants:** One-line version for play (default, 712x119: FREEDOM 250x BOOST with a laurel and a small flag ribbon at each end) and the separate words for the stacked intro logo (default1 FREEDOM, default2 250x BOOST, default3 HOLD AND WIN, defaultLaurent the laurel).
- **Motion:** Logo skeleton: show 0.42 s, idle 1.17 s, hide 0.25 s, with one white glow; on the intro the GameSplash rig (55 bones, loop 2.67 s) holds the stacked words.
- **Construction:** Five sprites; the words are separate so the intro can stack and animate them and the play screen can use a single flat strip.
- **Notes:** The file name defaultLaurent is the studio's spelling of laurel.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 46% · saturation 63% · contrast 81% · warm 52% / cool 48% · brighter towards: top (2), top-right (1), top-left (1)
- **Palette (measured):** #0d1a4b dark blue 15%, #d50607 red 13%, #f7f9f7 light green 8%, #e8af1f orange 7%, #b6e2f6 light cyan 7%, #0880c8 blue 6%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Bonus splash lettering

`feature-splashes` · atlas · 4 parts · largest 926×198 · sheet `sheets/feature-splashes.webp`

- **Role:** The localised words of the two bonus splashes (en-GB): BONUS GAME in blue for the Hold & Win with the caption CASH COLLECTORS COLLECT CASH PRIZES, and BONUS GAME in red for the Jackpot Hold & Win with JACKPOT COLLECTORS COLLECT JACKPOT PRIZES.
- **Subject:** Two title words and two two-line captions.
- **Style:** Condensed heavy capitals.
- **Rendering:** Titles with a fine stripe texture in the face and a dark outline; captions in plain cream-white with a dark outline.
- **Colour:** Measured: blue #364599 20%, red #c90504 19%, cream #eeeee3 18%. Blue title for cash, red title for jackpot.
- **Lighting:** Top-lit.
- **Ambience:** Announcement.
- **Materials:** Printed lettering.
- **Variants:** Two colourways of the same title.
- **Motion:** HoldAndWinSplash and JackpotBonusSplash: show 1 s, hide 0.5 s. Seen in play: the red BONUS GAME over the three Jackpot Collectors and the four medals, with its caption and the START button of the shell, the base game washed red behind it. The blue splash of the cash Hold & Win was not seen.
- **Construction:** Four separate localised picture files, 926 px wide, outside the atlas, so another language replaces only these.
- **Notes:** All text that is not a name or a number is kept in localised files; the atlas holds no sentence.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, strong highlights · brightness 43% · saturation 57% · contrast 62% · warm 58% / cool 42% · brighter towards: top (2)
- **Palette (measured):** #364599 blue 20%, #c90504 red 19%, #eeeee3 light yellow 18%, #8e7154 orange 16%, #7b3321 red 6%, #3b0806 dark red 4%

### Jackpot win screen

`jackpot-win` · atlas · 6 parts · largest 635×343 · sheet `sheets/jackpot-win.webp`

- **Role:** The picture shown when a jackpot is collected (WinJackpot skeleton, one skin per jackpot); seen in play for Unity.
- **Subject:** The jackpot's medal at large size (417x403) in its colour, a gold scroll ribbon, and the word CONGRATS! in red.
- **Style:** As the Jackpot Coins, enlarged.
- **Rendering:** The same medal painting as the symbol at about 1.7 times its size; crisp (soft edge 0.056).
- **Colour:** Measured: gold #f2c04b 20%, #b16314 19%, red #c20404 10%, dark red #771f06 10%, green #1f7502 5%, blue #034784 5%, magenta #770282 5%.
- **Lighting:** Top-lit.
- **Ambience:** Award moment.
- **Materials:** Gold and coloured glass.
- **Variants:** Four large medals (purple, blue, green, red), a starred ribbon for the top prize (jackpot3Ribbon), one CONGRATS! word.
- **Motion:** WinJackpot (32 bones): show 0.92 s, hide 0.5 s; JackpotEffects loops a ray shine 1.33 s. Seen in play: the board dims, CONGRATS! drops in at the top, the purple Unity medal fills the middle on a purple glow with a flag behind it, 25 stands below in the numeral font, and star coins shower outward; once the picture arrived through a yellow-white flash.
- **Construction:** Six sprites; the names come from the jackpot panel's lettering.
- **Notes:** The large medals are separate, sharper paintings of the symbol, not an upscale, so the win screen holds at full size.
- **Measured:** mid-tone, vivid, warm, high contrast, hard-edged · brightness 44% · saturation 83% · contrast 68% · warm 83% / cool 10% · brighter towards: top (1)
- **Palette (measured):** #f2c04b orange 20%, #b16314 orange 19%, #c20404 red 10%, #771f06 dark red 10%, #1f7502 dark green 5%, #fcec9c light gold 5%

### Win celebrations: BIG, SUPER, MEGA and TOTAL WIN

`win-tiers` · atlas · 18 parts · largest 681×761 · sheet `sheets/win-tiers.webp`

- **Role:** The words and dressing of the win screens. By the skeleton skins label1, label2 and label3 the tiers are BIG WIN, SUPER WIN and MEGA WIN; TOTAL WIN closes a bonus.
- **Subject:** Two-word titles in heavy capitals, a large gold star, a gold laurel branch with a ribbon, a wide gold scroll ribbon for the amount, and a large waving Stars and Stripes on a gold-tipped pole.
- **Style:** Game-show title lettering with award dressing.
- **Rendering:** Extruded letters with a gold keyline and a darker side; each word has a blurred white copy for a glow flash. The flag and laurel are fully painted. Soft edge 0.104.
- **Colour:** A colour per tier: BIG WIN magenta, SUPER WIN green, MEGA WIN yellow-gold, TOTAL WIN blue. Measured: gold #f4bc3b 16%, near-white #fdfaf5 11%, green #04c607 7%, blue #0458f1 7%, yellow #f2d202 6%, magenta #d603ca 4%.
- **Lighting:** Top-lit letters; the flag lit from the upper right.
- **Ambience:** Triumphant; a medal ceremony with the flag raised.
- **Materials:** Enamel letters, gold star and laurel, cloth flag.
- **Variants:** Three tier words with one WIN each in the tier colour, their glow copies, one star and its glow, one laurel (placed twice, mirrored, around the words, as seen on MEGA WIN), one ribbon, one flag (a mesh in WinBigEffects).
- **Motion:** WinBig (49 bones): labelShow 0.92 s, sumShow 0.33 s, hide 0.5 s; WinBigEffects: loop 3 s, loopFlag 2 s (the flags wave by mesh); WinTotal: show 0.92 s, bangupEnd 0.58 s. Smaller wins use WinSmall and WinNormal (0.33 s shows). Seen in play: the gold scroll ribbon unrolling across the board with the amount and a burst of star coins when a Cash Collector collects. Seen at the end of the Jackpot Hold & Win: the total counting up on the same ribbon over blue rays, then MEGA WIN in gold between two mirrored laurel branches under an arc of gold stars, 175.00 below it, with star coins and gold confetti. BIG WIN, SUPER WIN and the TOTAL WIN words were not seen; their reading is from the sheet and the files.
- **Construction:** 18 sprites: words are stills, moved and flashed by rig; the flag is the same sprite that hangs behind the statue.
- **Notes:** Tier colours are taken from the jackpot colours (green, magenta, gold, blue), not from the flag, so a big win reads as different from the red, white and blue stage.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 55% · saturation 72% · contrast 62% · warm 62% / cool 22% · brighter towards: top (3), top-right (1)
- **Palette (measured):** #f4bc3b orange 16%, #fdfaf5 light orange 11%, #ae6b24 orange 8%, #04c607 green 7%, #0458f1 blue 7%, #f2d202 gold 6%


## Effects

Frame sequences, glows, particles and transitions.

### Glows, rays and particles

`light-and-particles` · atlas · 23 parts · largest 500×500 · sheet `sheets/light-and-particles.webp`

- **Role:** The general light kit: ray bursts, glows, a ring wave, blink stars, a smoke puff and small particles, used by nearly every skeleton.
- **Subject:** Three ray bursts, a soft glow, a ring, a radial shine, four-point and five-point twinkles, a white smoke cloud, speck fields, and tiny orange and yellow glow dots.
- **Style:** Standard white effect sprites.
- **Rendering:** Soft white shapes (soft edge 0.898); the smoke is the one painted piece.
- **Colour:** Near-white #fefefe 87%; the two glow dots are orange and yellow. Tinted and added by the game.
- **Lighting:** Self-lit.
- **Ambience:** Shine and sparkle.
- **Materials:** Light, smoke.
- **Variants:** One of each.
- **Motion:** No sequences; rigs rotate, scale and fade them (for example SceneCollectorEffects, a 20 s loop of rays behind the statue).
- **Construction:** 23 sprites, four of them separate shared helper textures (glow, glowParticleYellow, emitter_particle_white, RGBAnoise).
- **Notes:** whiteGlow alone is used by more than twenty skeletons.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 90% · saturation 1% · contrast 7% · warm 7% / cool 0%
- **Palette (measured):** #fefefe light orange 87%, #0f0f0f black 6%, #434343 grey 2%, #717171 grey 2%

### Fireworks and confetti

`fireworks-and-confetti` · atlas · 33 parts · largest 662×656 · sheet `sheets/fireworks-and-confetti.webp`

- **Role:** The opening and transition fireworks and the confetti that drifts across the stage all the time.
- **Subject:** Two firework bursts drawn as rings of short streaks (a back and a front layer), a star of motion lines, and a small disc that turns through edge-on.
- **Style:** Light effects drawn in white for tinting.
- **Rendering:** Soft white streaks on transparency (soft edge 0.909); the confetti disc is a flat grey-white shape.
- **Colour:** Shipped in white and grey only (#686868 62%, #fefefe 18%); the game tints them. Seen in play: cyan, white and red bursts on the opening, and red, blue and white confetti.
- **Lighting:** Self-lit.
- **Ambience:** Fourth of July night.
- **Materials:** Light; paper.
- **Variants:** One burst design in two layers, tinted per use; one confetti disc in three tints (the three ParticleConfetti skeletons).
- **Motion:** confettiParticle is a 30-frame tumble. The bursts are scaled and faded by the GameSplash and SlotTransition rigs (show 2 s). Seen in play: three bursts over the board as the intro gives way to the game, and bursts again, with puffs of red, white and blue smoke, as the board changes to the Jackpot Hold & Win.
- **Construction:** 33 sprites: two bursts, motion lines, 30 confetti frames.
- **Notes:** Three tints of one white drawing give the flag's three colours to the effects for the cost of one sprite set.
- **Measured:** mid-tone, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 54% · saturation 0% · contrast 19% · warm 35% / cool 10%
- **Palette (measured):** #686868 grey 62%, #fefefe white 18%, #a3a3a3 grey 12%, #393939 grey 5%, #cacac9 grey 2%

### Sparks

`sparks` · atlas · 36 parts · largest 326×162 · sheet `sheets/sparks.webp`

- **Role:** Two spark animations: a trailing shower for reel anticipation and a small burst for hits and collections.
- **Subject:** A comet-like stream of bright points, and a compact starburst that scatters into specks.
- **Style:** Light effects in white.
- **Rendering:** Pure white with soft falloff (soft edge 0.88).
- **Colour:** White only (#ffffff 100%); tinted by the game.
- **Lighting:** Self-lit.
- **Ambience:** Electric anticipation.
- **Materials:** Light.
- **Variants:** Two sequences, no colour variants in the files.
- **Motion:** anticipationSparks 21 frames (ReelAnticipationFront, 0.67 s loop); sparksExplosion 15 frames, used by the statue, the jackpots and the win screens.
- **Construction:** 36 sprites, all frames.
- **Notes:** The only hand-drawn effect sequences besides the highlight sweeps.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 0% / cool 0%
- **Palette (measured):** #ffffff light gold 100%


## Game interface

Buttons, counters and panels drawn for this game.

### Jackpot display: four medallions above the reels

`jackpot-panel` · atlas · 5 parts · largest 514×170 · sheet `sheets/jackpot-panel.webp`

- **Role:** The four fixed jackpots shown at the upper left of the board in play: GLORY 2500x, FREEDOM 250x, JUSTICE 50x and UNITY 25x (values as the screens and the help text state).
- **Subject:** Each jackpot is a Jackpot Coin medal with its value in the numeral font and its name on the gold ribbon; Glory, the largest, sits on a pleated red, white and blue rosette.
- **Style:** As the Jackpot Coins: award medals and a prize rosette.
- **Rendering:** Arched extruded names with a gold keyline; the rosette is painted satin with a rope-edged cream centre.
- **Colour:** Measured: brown #6f2709 14%, gold #f5c83e 14%, green #0c9804 12%, cream #f3eae2 10%, blue #136ec3 10%, red #cf0606 10%, magenta #b715b9 7%. The names carry the four jackpot colours.
- **Lighting:** No light direction measured; the letters have a lighter upper half.
- **Ambience:** A winners' podium.
- **Materials:** Gold, enamel lettering, satin rosette.
- **Variants:** Four names (jackpot0Txt Unity to jackpot3Txt Glory) and one rosette for the top prize. The medals themselves are the tile15 to tile18 coins.
- **Motion:** Jackpot skeleton (22 bones): activate 0.5 s, activeLoop 0.67 s, collect 0.33 s, win 0.5 s, and tracks for progress (1.67 s) and anticipation (0.83 s). Seen in play: a landed Jackpot Coin throws a small coin up to the display and the Justice and Unity medallions show their bare coloured domes for a moment, the values fading back in.
- **Construction:** Five sprites of its own; everything else is reused from the Jackpot Coin symbol.
- **Notes:** Size and dressing rank the prizes: Glory is larger and has the rosette; the other three differ only in colour and name.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 47% · saturation 74% · contrast 69% · warm 64% / cool 25%
- **Palette (measured):** #6f2709 brown 14%, #f5c83e gold 14%, #0c9804 green 12%, #f3eae2 light orange 10%, #136ec3 blue 10%, #cf0606 red 10%

### Respin counter

`spin-counter` · atlas · 5 parts · largest 415×118 · sheet `sheets/spin-counter.webp`

- **Role:** The 3-2-1 respin counter of the two Hold & Win games (the help text: "starts with 3 Free Spins").
- **Subject:** A small satin scroll ribbon holding the numerals 1, 2 and 3.
- **Style:** As the board dressing.
- **Rendering:** A painted ribbon with folded ends and small leaf tips; plain white heavy numerals.
- **Colour:** Measured: red #bf1b1b 20%, light blue #b6d1e3 16% and #79aed6 14%, dark red #75160d 11%. A light blue ribbon and a red ribbon.
- **Lighting:** Lit from the top.
- **Ambience:** Ceremonial, like a medal bar.
- **Materials:** Satin ribbon.
- **Variants:** Two ribbons: spinCounterPlateSpecial (light blue) and spinCounterPlateJackpotBonus (red), matching the two bonus boards; three numerals.
- **Motion:** SpinCounter: activate 0.42 s, deactivate 0.25 s, loop 0.83 s; SpinCounterPositions show 0.45 s. Seen in play: the red ribbon with 1 2 3 takes the place of the logo on top of the board in the Jackpot Hold & Win, one numeral lit white (3 in the frame kept).
- **Construction:** Five sprites.
- **Notes:** The counter takes the board's bonus colour, so the state of the game is readable from one small ribbon.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 50% · saturation 54% · contrast 68% · warm 52% / cool 44% · brighter towards: top (2)
- **Palette (measured):** #bf1b1b red 20%, #b6d1e3 light blue 16%, #79aed6 blue 14%, #75160d dark red 11%, #397dae blue 8%, #f3f1f0 white 8%


## Typography

Embedded fonts and lettering.

### Numeral font: white with a gold glow line

`font-myriad-pro` · atlas · 18 parts · largest 106×190 · sheet `sheets/font-myriad-pro.webp`

- **Role:** The bitmap font for changing numbers; seen in play on the Golden Coin's value, on the amount a collector holds, on the collection win (2.00 on the gold ribbon) and on the jackpot win (25). That the jackpot values above the reels (2500x, 250x) use it too is inference from their look.
- **Subject:** The digits 0 to 9 and the signs + ? / x * , . and -.
- **Style:** Heavy condensed rounded sans numerals.
- **Rendering:** A white face, a yellow-gold keyline that glows slightly, and a dark red block shadow to the lower right. Hard edges (soft edge 0.117).
- **Colour:** Measured: near-white #fefef5 36%, gold #f7d01d 30%, dark red #611702 16%, yellows #faf35e and #fdfba0 6% each.
- **Lighting:** Top-lit (measured on 17 of 18 glyphs).
- **Ambience:** Bright and loud, like a scoreboard.
- **Materials:** Enamel with a gold edge.
- **Variants:** One set. The descriptor lists 110 glyphs; 18 are on the page this game loaded and 92 are on pages loaded only on demand.
- **Motion:** None of its own; numbers count up by code.
- **Construction:** A provider font service page (fonts-v2/MyriadPro), not part of the game atlas; the 92 glyphs the reader had cut wrongly from this page were removed from the run.
- **Notes:** The name is the provider's; the glyphs are a styled bitmap, not the Myriad Pro typeface as such.
- **Measured:** bright, saturated, warm, high contrast, hard-edged, strong highlights · brightness 76% · saturation 55% · contrast 90% · warm 100% / cool 0% · brighter towards: top (17)
- **Palette (measured):** #fefef5 light gold 36%, #f7d01d gold 30%, #611702 dark red 16%, #faf35e gold 6%, #fdfba0 light gold 6%, #915002 brown 3%


## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Poppins (Bold); Poppins (Regular); Poppins (SemiBold).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 665 components cut from 35 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
