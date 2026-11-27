# Huff N Lots Of Goals: art report

lnw · run `2026-11-27-0814-lnw-huff-n-lots-of-goals` · captured 2026-11-27

Source: the provider's free-play demo, https://nogs-gl.nyxmalta.com/game/?clienttype=flash&nogscurrency=USD&nogsgameid=72039&nogslang=en_us&nogsmode=demo&nogsoperatorid=961

**Extracted:** 1702 named components from 168 textures in 168 atlases; 12 Spine skeletons; 57 frame sequences (1288 frames); 8 fonts. Grouped into 62 units of art.

What is **measured** is computed from the pixels by `measure.py`. What is **read** is the analyst's reading of the sheets, with inference marked.

## Art direction (read)

The Three Little Pigs as a football match: a glossy cartoon cast in the two team colours, red and blue, on see-through reels cut into a sunlit green pitch, with two goals to fill above the reels, a pennant prize wheel turning behind them and a wolf in a referee's shirt.

**Style.** Family-animation cartoon. Pigs are rounded mascots with big heads (a face-painted fan, a player, a piglet); the wolf is a hand-drawn comic villain dressed as the referee; boots, whistle, ball and trophies are chunky toys. Around them the game uses sports-sticker graphics: halftone dots, torn brush bands, slanted italic titles.

**Rendering.** Smooth digital painting with airbrushed gradients, white gloss, a thin darker outline and a pale rim so pieces lift off the dark reel window. Lettering is fat, bevelled, outlined. The wolf's faces and all smoke, wind and sparkle are flat hand-drawn frames. The stadium is opaque brushwork with a crowd made of dabs.

**Colour.** Green field, red and blue teams, gold prizes. Measured over the game's own captured art: cream-white #f9f7ea 19%, pale orange #ead5bc 10% (smoke and cream fills weigh heavily), grass green #86c70c 9%, black #0a0f0b 5%, wolf blue #565b82 5%, yellow #f4ec13 3%. The background is 61% green hues with a red and pink crowd; the feature balls sit on pure red and royal blue squares; royals are one emerald green (#1c6c38); the coin is 96% warm. Prize tiers keep one colour each on plaque and wedge: magenta Mini, green Minor, blue Major, red Grand, gold Super.

**Lighting.** Daylight, even and shadowless, for the base game; the file named for the free game is the same stadium at night under six floodlights. Objects are top-lit with hard gloss. Glow is kept as separate layers and outline sprites. On screen the reel window is the darkest area and the pitch the brightest.

**Ambience.** Match day with a full house: cheerful, loud, busy. The wheel, two goals, five plaques and an animated logo crowd the top of the screen around a calm dark reel window. The villain is a joke: the wolf's threat is a whistle. A win of ten times the bet was marked by a gold light burst and a one-line caption, no more.

**Shape language.** Round everywhere: balls, coins, cups, domed buttons, bubble letters, puffs of smoke. Points are kept for the wolf's muzzle and ears, the pennant wedges of the wheel and star ornaments.

**Materials.** Stitched leather (ball), brushed steel (whistle), glossy boots, bronze, silver and gold (trophies, coin, frames), mown turf used as a frame material, netting and tube steel (goals), dark glass (plaques), enamel lettering, soap bubbles, riveted wood and hazard tape in the logo, cream cartoon smoke.

**Typography and lettering.** Display lettering is drawn art. The logo gives each word its own material and strikes PUFF out with a black brush stroke in favour of GOALS!. Prize and feature words are heavy rounded or slanted italic capitals with bevel, outline and rim, coloured by tier. Words are swapped as whole pictures for Spanish. Running text on screen is the provider's: Noto Sans as distance-field pages, with Jost and Outfit also shipped and Frutiger Neue in the provider's frame.

**Motion.** Seen in the real frames: the wheel stands at a different wedge in every frame; the logo animates (a ball rolls through GOALS!, PUFF pops under its strike); reels blur on the spin and the spin button becomes a stop square; a win flashes a wide gold burst behind the amount and dims the losing symbols; a collected red ball sends a rope of cream smoke diagonally up the reels to the red goal, with a puff where it leaves and a brighter puff where it arrives; a wheel symbol sends rainbow sparks up to the wheel, where a wedge flares gold. Read from the files only: twelve Spine skeletons (4.1.24, three exported from 4.2.43) with ball landings of 3.25 s, a 1.67 s wolf win, the wolf's pop-up (3.1 s in, 6.8 s loop) and blow (1.5 s in, 4.2 s loop), trophies that build in 1.2 s, feature panels of 1.8 s, a 1.4 s transition and a four-tier big win whose intro grows from 0.7 to 3.1 s. Effects are drawn sequences at the 24 frames a second the sheets state, the longest a 165-frame dust blast. No skeleton frame is shown in this report: the project's drawing tool does not read Spine 4.1 correctly.

**Variants and themes.** Two team colours on shared rigs: blue and red ball, blue and red goal. Three metals on one trophy rig and one frame set. Gold and super versions of the wheel wedges. The red ball as a 1x1, 2x2, 3x3 and 3x5 block. Day and night stadium on one drawing. English and Spanish versions of worded pictures. Landscape and portrait versions of most animations. Two control sets: the provider's grey one, used on the desktop screens, and a game-coloured one not seen in play.

**How it is built.** PixiJS client. In this run: 168 textures, 1,702 named sprites, 12 skeletons, 8 fonts, 57 frame sequences holding 1,288 of the sprites. Sprite sheets are 'Red 7 Exporter' packs; skeletons are Spine 4.1 with few meshes (the wolf symbol has 19, most rigs none). Parts of one rig share a canvas size so colours and grades swap one for one (ball parts 336 to 338 px, trophy parts 278 px, goal parts 517x476). Each background is one square 1920x1920 picture for both orientations. The reel window is a plain see-through dark rectangle. File and animation names are those of the building-site Huff N' Puff games (woodcutter, hardhat, megahat, buzzsaw, houses, toolboxes): inference, this game was built by re-dressing that game's structure piece for piece.

**Consistency.** High: one outline-and-gloss treatment on every object, one lettering system, one colour per prize tier, one cream smoke for every puff, and red against blue carried from the symbols to the goals, the pig's face paint and the transition. The wolf is drawn flatter than the painted symbols, a deliberate cel-cartoon register. The provider's grey controls and help pages are the one part outside the theme.

**What to take from it.** (1) A new theme on an old frame: every piece here answers a piece of the building-site Huff N' Puff games (saw and hard hat became blue and red balls, toolboxes became goals, houses became trophies, caution tape became team-colour bands), and the files keep the old names. The mechanics, rigs and timings were kept; only the pictures changed. That is the cheapest route to a sequel, and a clear brief for an art package: the list of pieces is already known. (2) Let the theme supply the meters: the two collection pots are goals that fill with balls, and each collected ball visibly travels there on a smoke trail. The player sees progress as an object, not a number. (3) Two team colours do the work of a whole palette: red and blue mark the two feature symbols, the two goals, the fan's face and the transition, on a green field that never competes with them. (4) Keep the bonus in sight: the prize wheel turns permanently behind and above see-through reels, and a wheel symbol visibly upgrades a wedge. The plain dark reel window is what keeps the symbols readable in a crowded screen. (5) Give each prize tier one colour and use it on every surface that names it: plaque title, plaque rim, wheel wedge. (6) Rig what moves mechanically and draw what is chaotic: goals, trophies, coins and panels are rigged from parts; the wolf's faces, the logo's letters and all smoke, wind and sparkle are drawn frames. The drawn sequences are where the texture budget goes (22 pages for one dust blast, 11 for the logo). (7) Make the celebration from the cast: the big win stages the wolf and the three trophies, and its particles are the game's coin, star, boot and ball. (8) Small wins are quiet: ten times the bet got a gold burst and a caption. The spectacle is saved for features and tiers. (9) For an AI art package on this model the static pieces are few: two square backgrounds (one a relight of the other), 16 symbol stills at about 300 px, one trophy in three metals with frames and backings, two goals, a coin, 16 wedges, a logo. The cost sits in the drawn sequences, which is where generated art would need the most hand work. (10) Limits of this report: no feature, free spin, big win, wolf pop-up, transition or later paytable page was reached, so those are read from the files alone. The demo is the UK build; that its art matches the US game is inference. No skeleton is drawn here, whatever the method notes below say: the project's drawing tool does not read Spine 4.1 correctly.

## Colour, measured

The game's own art (provider interface left out): bright, saturated, warm and cool mixed, medium contrast, strong highlights · brightness 64% · saturation 49% · contrast 48% · warm 43% / cool 33% · brighter towards: top (102), top-left (39), bottom (37)

Palette: #f9f7ea light gold 20%, #ead5bc light orange 10%, #86c70c green 10%, #b2a789 orange 8%, #0a0f0b black 6%, #565b82 blue 5%, #f4ec13 gold 3%

| Art component | Units | Brightness | Saturation | Contrast | Warm / cool | Leading colours |
| --- | --- | --- | --- | --- | --- | --- |
| Backgrounds and environment | 1 | 54% | 63% | 69% | 27% / 47% | #87ca0b green 23%, #213c50 dark blue 14%, #c4b3a9 orange 8% |
| Reel board | 3 | 62% | 58% | 42% | 4% / 54% | #66c558 green 33%, #a1e211 green 16%, #ebedd0 light yellow 15% |
| Symbols | 7 | 62% | 61% | 56% | 46% / 32% | #fcfbf9 light yellow 20%, #faeb0e gold 11%, #eb6e0b orange 8% |
| Characters | 1 | 65% | 43% | 53% | 2% / 67% | #e2e3d2 light yellow 35%, #85c403 green 21%, #58578a blue 21% |
| Logo and title | 2 | 42% | 46% | 87% | 20% / 40% | #070b07 black 23%, #344233 dark green 18%, #27c11e green 11% |
| Win celebrations and banners | 3 | 61% | 64% | 48% | 32% / 41% | #82c00f green 30%, #e9ead5 light yellow 15%, #555b88 blue 7% |
| Effects | 19 | 84% | 28% | 21% | 87% / 4% | #fef9f1 light orange 40%, #f3d7b8 light orange 24%, #baaa84 orange 13% |
| Game interface | 3 | 42% | 68% | 74% | 54% / 36% | #0f140c black 10%, #a85617 brown 8%, #f8dd60 gold 6% |
| Provider interface (shared) | 23 | 54% | 22% | 18% | 24% / 36% | #848583 grey 40%, #ffffff light blue 18%, #555558 grey 12% |

## Backgrounds and environment

Full-screen scenes and the animated layers that sit on them.

### Stadium backgrounds and the still logo

`background` · atlas · 4 parts · largest 1920×1920 · sheet `sheets/background.webp`

- **Role:** The two full backgrounds, one for the base game and one named for the free game, and a flat copy of the logo. The base-game picture is behind every real screen; the free-game one was not seen in play.
- **Subject:** A football stadium seen from the pitch: striped grass with a centre line running to a touchline wall, two tiers of crowd in red, pink and white, and a glass roof. By day the sky is pale turquoise; the free-game version is the same view at night under a starry sky with six floodlights casting pale beams. The logo sprite reads HUFF N' LOTS OF PUFF GOALS! with PUFF struck through by a black brush stroke.
- **Style:** Simplified painted scenery in a children's-book manner: the crowd is thousands of dabs, not people; the architecture is clean bands.
- **Rendering:** Opaque brushwork with visible grass texture in the foreground, hard edges (soft edge 0.01 measured) and strong one-point perspective that pulls the eye up the centre line.
- **Colour:** Measured: grass green #87ca0b 23%, dark blue #213c50 14%, the crowd's pink-beige #c4b3a9 8%, deeper greens #28963c 7% and #52970e 5%, lime #c8f002 6%. The crowd is red and pink, so the scene is green below and red above, the two halves of the game's palette.
- **Lighting:** Day: even, shadowless light with brighter and darker mown stripes. Night: the stripes turn blue-green and the floodlight cones are laid over the stands.
- **Ambience:** Match day, full house. The day version is fresh and sunny; the night version raises the stakes for the bonus (that it is used for free spins is the file's name, not a seen screen).
- **Materials:** Mown turf, painted concrete, glass and steel, a crowd as confetti.
- **Variants:** Two times of day on one drawing: the same stands, roof and pitch, recoloured and relit.
- **Motion:** None in the pictures themselves.
- **Construction:** 'Red 7 Exporter' sheet: two 1920x1920 square pictures (one square serves landscape and portrait), the 876x581 logo and a 3 px grass swatch.
- **Notes:** The square format is the provider's way to cover both orientations with one painting; the centre of the square is kept empty for the reels.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 54% · saturation 63% · contrast 69% · warm 27% / cool 47% · brighter towards: bottom (1), top-left (1)
- **Palette (measured):** #87ca0b green 23%, #213c50 dark blue 14%, #c4b3a9 orange 8%, #28963c green 7%, #c8f002 green 6%, #52970e green 5%


## Reel board

The frame, the reel backing, dividers, win lines and what holds the symbols.

### The two goals (collection pots)

`pots` · atlas · 17 parts · largest 517×476 · sheet `sheets/pots.webp`

- **Role:** The blue goal and the red goal above the reels, the game's two 'pots': each fills as its ball is collected, as the loading screen's line COLLECT (ball) TO TRIGGER THE KICK BALL FEATURE says. Both are in every base-game screen. After a blue ball was collected the blue goal held one ball and its badge read 1; later stages were not seen.
- **Subject:** A goal with a net on a round island of mown grass, in blue and in red, as layers (ground, net, back frame, side frame), two footballs, a round blue counter badge, and six small numerals 1 to 6.
- **Style:** Chunky toy goal in three-quarter view; the net is drawn as a loose white grid.
- **Rendering:** Painted with soft shading; the net is a semi-transparent layer over a black backing so balls can sit inside it.
- **Colour:** Measured: grass green #8aa747 28%, black #030404 22%, dark green #425837 10%, blue #1d4c8d 7% and #337cc0 3%, white #f6f7ed 5%.
- **Lighting:** Top-left light on the frame; a soft shadow under the island.
- **Ambience:** Playful: the bonus meters are goals to be scored in.
- **Materials:** Painted tube steel, string netting, turf.
- **Variants:** Blue (left) and red (right) on one rig. Animation names keep the older game's words: 'hat_stage_01..06' for one goal and 'saw_stage_01..06' for the other, each with an idle and a trigger.
- **Motion:** 35 animations by the file's key times: a stage change 0.63 s, a trigger 0.37 to 0.40 s, idles up to 1.47 s. Six stages per goal; the first stage put one ball in the net on a real screen; that the later stages add more is inference from the two ball parts and the six numerals. No skeleton frame is shown: the tool twists Spine 4.1 rigs.
- **Construction:** Spine skeleton exported as 4.1 from 4.2.43, 11 bones, 16 slots, 2 meshes; 17 parts on two pages, every part on a shared 517x476 canvas.
- **Notes:** Putting the two collection meters on screen as goals turns the sibling game's pots into the theme's own object.
- **Skeleton (from the file):** Spine 4.1-from-4.2.43 · 11 bones · 16 slots · animations: hat_stage_01 (0 s), hat_stage_01_Idle (0 s), hat_stage_02 (0 s), hat_stage_02_Idle (0 s), hat_stage_03 (0 s), hat_stage_03_Idle (0 s), hat_stage_04 (0 s), hat_stage_04_Idle (0 s), hat_stage_05 (0 s), hat_stage_05_Idle (0 s), hat_stage_06 (0 s), hat_stage_06_Idle (0 s), hat_trig_stage_01 (0 s), hat_trig_stage_02 (0 s), hat_trig_stage_03 (0 s), hat_trig_stage_04 (0 s), hat_trig_stage_05 (0 s), saw_stage_01 (0 s), saw_stage_01_Idle (0 s), saw_stage_02 (0 s), saw_stage_02_Idle (0 s), saw_stage_03 (0 s), saw_stage_03_Idle (0 s), saw_stage_04 (0 s), saw_stage_04_Idle (0 s), saw_stage_05 (0 s), saw_stage_05_Idle (0 s), saw_stage_06 (0 s), saw_stage_06_Idle (0 s), saw_trig_stage_01 (0 s), saw_trig_stage_02 (0 s), saw_trig_stage_03 (0 s), saw_trig_stage_04 (0 s), saw_trig_stage_05 (0 s), saw_trig_stage_06 (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 41% · saturation 47% · contrast 65% · warm 15% / cool 36% · brighter towards: top-left (2), top-right (1), top (1)
- **Palette (measured):** #8aa747 green 28%, #030404 black 22%, #425837 dark green 10%, #1d4c8d blue 7%, #868889 grey 6%, #f6f7ed light yellow 5%

### Free-spins pieces

`freespins` · atlas · 5 parts · largest 844×843 · sheet `sheets/freespins.webp`

- **Role:** A few pieces used only in the bonus rounds. Not seen on a real screen.
- **Subject:** A very large football with a thin gold rim (named megahat), an orange counter plate, and a REEL WAYS label in gold letters on a blue bar, horizontal and vertical.
- **Style:** The big ball is painted in more detail than the reel ball, with stitched panels; the label is arcade-style lettering.
- **Rendering:** Smooth painting with strong gloss on the ball; bevelled gold letters with a dark outline on the label.
- **Colour:** Measured: warm grey #a89a8c 27%, cream #f3ecdd 27%, blue-black #212930 26%, orange #e8894c 5% and #f9970a 4%.
- **Lighting:** Top-left light on the ball.
- **Ambience:** One oversized object for the Mega Ball feature: scale as the spectacle.
- **Materials:** Leather, glossy orange enamel, gold lettering.
- **Variants:** Landscape and portrait REEL WAYS labels.
- **Motion:** None in this unit.
- **Construction:** 'Red 7 Exporter' sheet, 5 frames; the ball is 844x843, more than five reel cells wide at 1280x720.
- **Notes:** The 844 px ball is the 'megahat' of the older game: one symbol large enough to cover a block of the reels.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 57% · saturation 27% · contrast 83% · warm 33% / cool 67% · brighter towards: top-left (1)
- **Palette (measured):** #a89a8c orange 27%, #f3ecdd light orange 27%, #212930 dark blue 26%, #dacab3 light orange 5%, #e8894c orange 5%, #f9970a orange 4%

### Base-game furniture: pitch layers, reel window, jackpot plaques

`basegame` · atlas · 26 parts · largest 1920×1429 · sheet `sheets/basegame.webp`

- **Role:** Everything fixed around the reels in the base game. Seen in every real screen: the pitch strips at the sides, the dark see-through reel window, the five jackpot plaques down the left, and the two goals on grass islands above the reels.
- **Subject:** Four wide pitch and grass layers and a touchline wall, a dark green reel window with a thin grass top edge, five plaque frames outlined in the tier colours with drawn titles (SUPER, GRAND, MAJOR, MINOR, MINI), a blue goal and a red goal each on a round grass island, a white wedge outline for the wheel upgrade, a blue 'click to start' button and a win meter.
- **Style:** The storybook stadium carried into the interface: grass is used as a frame material, and the goals sit above the reels like props.
- **Rendering:** Painted grass with stripes and a soft fade; the plaques are dark glass panels with a thin coloured rim; titles are fat rounded capitals with a white outline and a dark drop.
- **Colour:** 88% green hues by measure: #66c558 36%, lime #a1e211 18%, cream #ebeecf 14%, near-black #071609 10%. The tier titles keep one colour each: red on gold SUPER, red GRAND, blue MAJOR, green MINOR, magenta MINI.
- **Lighting:** Top light on the plaques; the reel window is the darkest area on screen and the grass the brightest.
- **Ambience:** Tidy and bright; the reels are a dark stage cut into a sunny pitch.
- **Materials:** Turf, dark glass, painted steel goal posts and netting, enamel lettering.
- **Variants:** Landscape and portrait versions of the SUPER plaque ('_L', '_P'); base and hover states of the start button.
- **Motion:** None in this unit. On the real screens the plaque amounts are live text: $7,500.00 SUPER, $5,000.00 GRAND, $1,000.00 MAJOR, $100.00 MINOR, $20.00 MINI at a $1.00 bet.
- **Construction:** 'Red 7 Exporter' sheet on two pages, 26 frames: pitch layers 1920 px wide, the reel window 1095x640, plaques 239 to 366 px wide, goals 456 px.
- **Notes:** The reel window is a plain dark rectangle with no drawn frame, as in the sibling game: the wheel shows through it and nothing competes with the symbols. Files still call the goals 'Toolboxes_left' and 'Toolboxes_right'.
- **Measured:** bright, vivid, warm and cool mixed, medium contrast, strong highlights · brightness 63% · saturation 60% · contrast 39% · warm 2% / cool 54% · brighter towards: top (9), bottom (5), top-left (1)
- **Palette (measured):** #66c558 green 36%, #a1e211 green 18%, #ebeecf light yellow 14%, #071609 black 10%, #339170 green 7%, #95e147 green 4%


## Symbols

Every reel symbol: its still picture and its animated skeleton.

### Feature balls (skeleton parts)

`sym12-13` · atlas · 83 parts · largest 338×338 · sheet `sheets/sym12-13.webp`

- **Role:** The parts that animate the two feature symbols: the ball on blue and the ball on red. The stills are on the reels in most real frames; the red ones stack into a full reel, and both colours were seen being collected into their goals. The landing animations were not caught sharp on a screen.
- **Subject:** A black-and-white football in three versions (blue-toned, red set, and blurred spinning frames), square gradient backings in blue, green and red, a diagonal halftone-dot band that cycles, a soft round shadow, a white disc stroke, an orange fire swirl and a few blades of grass.
- **Style:** Flat comic-print graphics behind a painted ball: gradients, halftone dots and a speed band, as on a sports sticker.
- **Rendering:** The ball is painted with soft shading; the spin is done by eight motion-blurred drawings of the ball, not by turning one picture. Backings are plain gradients; the dots are flat white shapes used as light.
- **Colour:** Measured over the parts: white #fdfdfb 66% (balls and dots), orange #e54a0a 5% and #fcb008 4% (the fire swirl), black #0f1a24 4%, green #227928 3%. The backings are sky-to-royal blue, a flat grass green and a pure red.
- **Lighting:** Flat and graphic; the only glow is the fire swirl and the white stroke disc behind the ball.
- **Ambience:** Sporty and punchy, closer to a sticker album than to the storybook of the pigs.
- **Materials:** Stitched leather for the ball; everything else is print: flat colour, gradient and dots.
- **Variants:** Blue and red sets side by side with their own ball, backing, dot cycle and shadow ('bg_blue', 'bg_new', 'ball_blue', 'ball_red_new'); a green backing named 'bg_blue copy'. Animation names keep the older game's words: sym12 (the hard hat, here the red ball) lands in 1x1, 2x2, 3x3 and 3x5 'megahat' sizes, and sym13 (the saw, here the blue ball) has cut, transform and gold versions. Which of these this game uses was not seen.
- **Motion:** 19 animations of 2.5 to 4.2 s by the file's key times (landings 3.25 s, wins 3.04 to 3.25 s, 'sym13_cut_exit' 4.17 s). Drawn sequences inside the rig: ball spin 8 frames in each colour, dot cycle 14 frames (blue) and 24 (red), fire swirl 14, grass 5. No skeleton frame is shown: the tool twists Spine 4.1 rigs.
- **Construction:** Spine 4.1.24, 17 bones, 19 slots, no meshes; 83 parts on three pages, all on a shared 336 to 338 px square canvas so blue and red parts swap one for one.
- **Notes:** The same symbol is a still in the symbols sheet and a kit of layers here; the kit is what allows one ball to be shown in two team colours and in block sizes.
- **Skeleton (from the file):** Spine 4.1.24 · 17 bones · 19 slots · animations: sym12_land (0 s), sym12_land_fs (0 s), sym12_land_megahat (0 s), sym12_land_megahat_2x2 (0 s), sym12_land_megahat_3x3 (0 s), sym12_land_megahat_3x5 (0 s), sym12_win_backup (0 s), sym12_win_bkg_anim (0 s), sym12_win_hat_anim (0 s), sym13_Bigwin_gold (0 s), sym13_cut (0 s), sym13_cut_exit (0 s), sym13_cut_gold (0 s), sym13_landing (0 s), sym13_landing_gold (0 s), sym13_transform (0 s), sym13_win (0 s), sym13_win_gold (0 s), sym_13_blade (0 s)
- **Measured:** bright, muted, warm and cool mixed, medium contrast, strong highlights · brightness 82% · saturation 20% · contrast 28% · warm 12% / cool 31% · brighter towards: bottom (3), top-left (2), top (1)
- **Palette (measured):** #fdfdfb light orange 66%, #e54a0a orange 5%, #0f1a24 black 4%, #919393 grey 4%, #cbc9c1 grey 4%, #fcb008 orange 4%

### Prize coin and meter shine

`coin` · atlas · 31 parts · largest 483×271 · sheet `sheets/coin.webp`

- **Role:** The gold coin that carries a jackpot or wheel prize, with the orange counter plate of the free spins meter and its shine. Not seen on a real screen.
- **Subject:** A gold coin embossed with a football and a ring of stars on both faces, a second front with a spoked wheel, the coin's edge as separate pieces (round and straight), a glow ring, a white stroke ring, a sparkle, a dust texture, and an orange rounded plate with a 21-frame shine.
- **Style:** The same glossy cartoon metal as the trophies: bold emboss, simple star ornament.
- **Rendering:** Painted gold with a warm gradient and a dark brown recess; the edge pieces let the coin be turned in fake 3D by scaling faces and edge.
- **Colour:** 96% warm by measure: orange-gold #efa655 55%, pale gold #f9d392 14%, deep orange #db631e 10%, brown #85461e 6%, red #fe0d01 5%.
- **Lighting:** Top-left light on the faces; a separate starburst sparkle and a soft white shine bar supply the glints.
- **Ambience:** Reward and heat: the warmest unit in the game.
- **Materials:** Cast gold; glossy orange plastic or enamel for the plate.
- **Variants:** Two fronts on one coin body (football for the jackpots, wheel for the wheel prize). The animations name four jackpots (mini, minor, major, grand) and the wheel; how the tier is told on the coin was not seen, and no tier lettering is among the parts.
- **Motion:** 7 animations by the file's key times: the four jackpot coins and the wheel coin 3.33 s each, 'particle_coin' 1.33 s, 'fs_counter_glow_anim' 1.0 s; the shine is 21 drawn frames.
- **Construction:** Spine 4.1.24, 16 bones, 14 slots, no meshes; 31 parts on one page; coin faces 280x289.
- **Notes:** The coin is the football version of the sibling game's coin: same build, new emboss.
- **Skeleton (from the file):** Spine 4.1.24 · 16 bones · 14 slots · animations: fs_counter_glow_anim (0 s), jackpot_grand (0 s), jackpot_major (0 s), jackpot_mini (0 s), jackpot_minor (0 s), jackpot_wheel (0 s), particle_coin (0 s)
- **Measured:** bright, vivid, warm, medium contrast · brightness 65% · saturation 62% · contrast 41% · warm 96% / cool 1% · brighter towards: top-left (3), top (2)
- **Palette (measured):** #efa655 orange 55%, #f9d392 light orange 14%, #db631e orange 10%, #85461e brown 6%, #fe0d01 red 5%, #fdf6e7 light orange 5%

### Wolf symbol (skeleton parts)

`sym00` · atlas · 33 parts · largest 565×559 · sheet `sheets/sym00.webp`

- **Role:** The parts of the wolf symbol's win animation: the referee wolf, his whistle, a ball, a full moon and a night sky inside a gold frame. The wolf still was seen on the reels, and in one win three wolves stood in for other symbols (a wild); his own win animation was not caught.
- **Subject:** A blue-violet wolf head in pieces (head base, upper and lower jaw, two ears, brows, eyes, pupils), a black-and-white striped referee shirt, a steel whistle on a ring, a football, a pale full moon, a starry blue square and a gold square frame. A second, all-black set of body parts (head, torso, arms, legs in striped socks, tail) forms a silhouette of the whole wolf.
- **Style:** The same cartoon wolf as the still, built for squash and stretch: the muzzle is long and pointed, the ears and brows are separate so the expression can change.
- **Rendering:** Soft cel-style painting with a darker contour and airbrushed highlights on the fur; the silhouette parts are flat black with white kit stripes; the moon is a soft photographic-looking disc with a blue halo.
- **Colour:** 91% cool by measure: blue #063895 27%, blue-violet #444382 20%, white #f3f5f6 18%, black #060608 13%, sky blue #62b0fd 4%. The one warm accent is the gold frame.
- **Lighting:** Lit from below and the front (measured: bottom-left 5, bottom 4), with the moon as a back light in the picture. A separate cyan GLOW outline of the whole symbol is kept as its own sprite.
- **Ambience:** A night-match villain: comic rather than frightening, the one cool symbol among warm ones.
- **Materials:** Fur in broad locks, striped jersey cloth, polished steel, a leather ball, gilt frame.
- **Variants:** One rig, one animation. The silhouette set suggests the wolf is shown whole against the moon, kicking the ball, as well as in close-up; that is inference from the parts (Head, torso, L leg, R leg, Ball, ground, Moon), not seen.
- **Motion:** One animation, 'win', 1.67 s by the skeleton file's key times. 44 bones, 35 slots and 19 meshes: the face parts are meshes, so the face deforms rather than swaps. No skeleton frame is shown: the project's drawing tool twists Spine 4.1 rigs.
- **Construction:** Spine 4.1.24 skeleton, 33 parts on one page, the largest 565x559 (the glow outline) around a 504x500 sky and a 524x520 frame.
- **Notes:** The moonlit silhouette is the same change of register the building-site sibling gave its wolf's win; here the howl is replaced by football kit.
- **Skeleton (from the file):** Spine 4.1.24 · 44 bones · 35 slots · animations: win (0 s)
- **Measured:** mid-tone, saturated, cool, medium contrast, hard-edged, strong highlights · brightness 42% · saturation 50% · contrast 48% · warm 4% / cool 91% · brighter towards: bottom-left (5), bottom (4), top-right (3)
- **Palette (measured):** #063895 blue 27%, #444382 blue 20%, #f3f5f6 white 18%, #060608 black 13%, #bdc0d0 light blue 8%, #62b0fd blue 4%

### Trophies and their frames (Cup Feature)

`houses` · atlas · 48 parts · largest 279×282 · sheet `sheets/houses.webp`

- **Role:** Three trophies in bronze, silver and gold with matching square frames and backings: the prize cells of the Cup Feature. The bronze and silver frames appear on the loading screen's sample reels; the trophies were not seen in play.
- **Subject:** A two-handled cup with a star on its bowl in bronze, silver and gold, each also as separate pieces (cup, handles, base, star); three square backings with three shooting stars; three plain metal frames and three glowing frames set with stars; small stars in three metals; white shine and sparkle sprites.
- **Style:** Glossy cartoon trophies, rounded and thick, the same toy-metal as the coin.
- **Rendering:** Painted metal with a strong white gloss and a darker outline; the backings are darker, painterly panels with soft star trails.
- **Colour:** Measured over the parts: dark brown #3c1d0d 21%, bronze #a46934 16%, silver-white #e0e6e6 12%, gold #f3db34 8%, steel blue #8ca7d2 8%, navy #1a2153 8%. Each grade keeps one metal and one backing colour: brown, blue, gold on purple-brown.
- **Lighting:** Top and top-right light (measured 7 and 6); glow frames and sparkle sprites are separate layers.
- **Ambience:** A prize ceremony in miniature; calm compared with the balls.
- **Materials:** Bronze, silver and gold; brushed metal frames.
- **Variants:** Three grades on one rig. File names keep the older game's houses: straw is the bronze cup, stick the silver, brick the gold ('house_straw', 'frame_stick', 'brick_build').
- **Motion:** 10 animations: build 1.21 s, in 1.29 s, out 1.21 s per grade and a 'brick_loop' 1.21 s for gold only, by the file's key times. Drawn inside the rig: a 5-frame build shine, a 9-frame loop shine, 4-frame gold stars.
- **Construction:** Spine 4.1.24, 39 bones, 36 slots, no meshes; 48 parts on one page; cups 278 px, frames 279x282, backings 264 px, so the three grades swap part for part.
- **Notes:** A trophy assembled from cup, handles, base and star can be built piece by piece on screen, as the houses were in the sibling game; that the build animation does this is inference from the parts.
- **Skeleton (from the file):** Spine 4.1.24 · 39 bones · 36 slots · animations: brick_build (0 s), brick_in (0 s), brick_loop (0 s), brick_out (0 s), stick_build (0 s), stick_in (0 s), stick_out (0 s), straw_build (0 s), straw_in (0 s), straw_out (0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 47% · saturation 62% · contrast 65% · warm 64% / cool 33% · brighter towards: top (7), top-right (6)
- **Palette (measured):** #3c1d0d brown 21%, #a46934 orange 16%, #e0e6e6 white 12%, #f3db34 gold 8%, #8ca7d2 blue 8%, #1a2153 dark blue 8%

### Reel symbols (stills)

`symbols` · atlas · 15 parts · largest 366×381 · sheet `sheets/symbols.webp`

- **Role:** The still picture of every reel symbol but the wheel, 15 in one sheet. The real screens show 14 of them on the reels in cells of about 155 px at 1280x720 on a see-through dark window; the green-backed ball (sym_super_woodcutter) was not on a screen.
- **Subject:** A football on three square backings (blue with halftone dots, green, red), the wolf as a referee in a gold frame, three pigs (a fan with his face painted half red and half blue over a GOAL! caption on a yellow tile, a player in a blue shirt with a ball on a navy disc, a piglet in red kit kicking a ball on a green disc), a pair of red boots, a steel whistle, and six royals: 9, 10, J, Q, K, A. The paytable names the pigs PIGGY1 to PIGGY3 and the objects SHOES and WHISTLE.
- **Style:** Cartoon football take on the Three Little Pigs. Pigs and wolf are rounded mascots with big heads and clear expressions; the boots and whistle are chunky and simplified; royals are heavy serif letters, each with one small ornament (a crown on Q and K, a shield on J, a gem on A).
- **Rendering:** Smooth digital painting with airbrushed gradients, a thin dark outline and a pale blue-white rim on the objects so they lift off the dark window. The feature balls sit on a flat graphic backing with a halftone dot fade, a comic-print device the rest of the game repeats.
- **Colour:** Measured over the sheet: black #091516 14%, the royals' dark green #1c6c38 10%, the balls' white #eeeeeb 9%, blue #243c85 and #5d6482 8% each, red #a20504 4%. All six royals are one emerald green, so value is carried by subject and by the red and blue backings, not by letter colour. Saturated (0.51), high contrast (0.87).
- **Lighting:** Top light on most pieces (7 of 10 measured), white gloss on the ball, the whistle and the boots. The wolf is lit cool from the front against a starry blue night.
- **Ambience:** Bright, loud and friendly: match-day mascots. The two team colours, red and blue, are the loudest things on the reels.
- **Materials:** Stitched leather for the ball, brushed steel for the whistle, glossy synthetic leather and rubber studs for the boots, soft matte skin and cloth for the pigs, fur in broad locks for the wolf, enamelled metal for the royals.
- **Variants:** The ball comes on blue, green and red backings, three separate pictures. The file names are those of the building-site Huff N' Puff games (sym_woodcutter, sym_super_woodcutter, sym_hardhat, sym_tape, sym_toolbox): the ball stands where the saws and the hard hat stood, the whistle where the tape measure stood, the boots where the toolbox stood. That this game was made by re-dressing that game's symbol set is inference from the names.
- **Motion:** None in this unit: these are stills. The balls and the wolf have skeletons of their own (sym12-13, sym00) and the wheel symbol has drawn sequences. The client ships no skeleton for the pigs, the boots, the whistle or the royals.
- **Construction:** One 'Red 7 Exporter' sprite sheet on one page, 15 frames stored with their untrimmed size: 264 px square for the low symbols, 290 for the top pig, 317 for the royals, up to 366x381 for the ball on blue.
- **Notes:** The feature symbols are told apart from everything else by a filled square backing in a team colour; pigs sit on a disc or a tile; objects and royals are cut to their silhouette. On the real screens the red-backed balls join into one red column on reel 5.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 46% · saturation 51% · contrast 87% · warm 30% / cool 55% · brighter towards: top (7), top-left (2), bottom-right (1)
- **Palette (measured):** #091516 black 14%, #1c6c38 dark green 10%, #eeeeeb white 9%, #243c85 blue 8%, #5d6482 blue 8%, #a20504 red 4%

### Wheel symbol, landing

`sym_wheel_landing` · atlas · 14 parts · largest 330×330 · sheet `sheets/sym_wheel_landing.webp`

- **Role:** The landing of the wheel scatter: 14 drawn frames. The wheel symbol was seen at rest on reels 2 and 4 in the base-game screens.
- **Subject:** A small prize wheel of ten bright segments with a gold rim and hub on a magenta square.
- **Style:** Toy fairground wheel, flat and glossy.
- **Rendering:** Flat segments with a glass highlight across the top and a thick yellow rim; hard edges (soft edge 0.03 measured).
- **Colour:** The most saturated unit in the game (0.88 measured): yellow #fbf00c 27%, orange #f38c08 14%, cyan #08a9f7 9%, green #0dc902 6%, magenta #f30ac9 5%.
- **Lighting:** No directional light; a white gloss arc only.
- **Ambience:** A rainbow accent that reads as 'bonus' at once against the green and red of the rest.
- **Materials:** Enamel and gold.
- **Variants:** One sequence. The trigger sequence is a unit of its own (sym_wheel_trigger).
- **Motion:** 14 frames in which the wheel overshoots its 254 px cell to 330 px and settles; the sheets state 24 frames a second, about 0.6 s.
- **Construction:** 'Red 7 Exporter' frame sequence on one page, frames 254 to 330 px.
- **Notes:** The only symbol animated purely by drawn frames; the client has no skeleton for it.
- **Measured:** bright, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 63% · saturation 88% · contrast 71% · warm 61% / cool 24%
- **Palette (measured):** #fbf00c gold 27%, #f38c08 orange 14%, #08a9f7 cyan 9%, #0dc902 green 6%, #f7f25e gold 6%, #f30ac9 magenta 5%

### Wheel symbol, trigger

`sym_wheel_trigger` · atlas · 45 parts · largest 312×425 · sheet `sheets/sym_wheel_trigger.webp`

- **Role:** The wheel scatter's trigger animation: 45 drawn frames. Not identified on a real screen: a single wheel symbol was seen upgrading a wedge of the big wheel, but no wheel feature was triggered.
- **Subject:** The same ten-segment wheel spinning, with a magenta chevron rising above it mid-sequence.
- **Style:** Toy fairground wheel, as in the landing.
- **Rendering:** Flat segments, gloss arc, yellow rim; the spin is drawn with turned and blurred segments.
- **Colour:** Yellow #faea0e 23%, orange #eb6f07 12%, blue #047be7 8%, green #0d9803 8%, magenta #bf0892 6% and #f804f8 4% (measured).
- **Lighting:** No directional light.
- **Ambience:** A quick, bright flourish.
- **Materials:** Enamel and gold.
- **Variants:** One sequence.
- **Motion:** 45 frames, about 1.9 s at the 24 frames a second the sheets state; frames grow from 254x260 to 312x425 as the chevron shoots up.
- **Construction:** 'Red 7 Exporter' frame sequence on two pages.
- **Notes:** The chevron points up at the big wheel above the reels; that this is its meaning is inference.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged, strong highlights · brightness 58% · saturation 89% · contrast 72% · warm 62% / cool 25%
- **Palette (measured):** #faea0e gold 23%, #eb6f07 orange 12%, #047be7 blue 8%, #0d9803 green 8%, #e9b208 gold 7%, #bf0892 magenta 6%


## Characters

Mascots and full-figure character art, as skeletons and as painted poses.

### The wolf referee (pop-up and blow)

`wolf` · atlas · 70 parts · largest 3888×1108 · sheet `sheets/wolf.webp`

- **Role:** The game's one character rig: the wolf who rises over a hedge of pitch, blows, and whose tail swishes at the reels. In the real screens he appears only as the reel symbol; the pop-up, the blow and the tail were not seen.
- **Subject:** A blue-violet wolf in a black-and-white striped referee shirt: 19 drawn heads from a sly look to a wide-mouthed blow, a body, paws, blinks, a tongue lick, a whistle in five drawn frames, air streaks, a ball, and two very wide strips ('hedge', 'hedge_dark') that here are mown pitch and a pale touchline wall.
- **Style:** Classic hand-drawn cartoon villain: long muzzle, arched brows, blue eyes, a grin with small fangs. He is drawn flatter and more like cel animation than the painted symbols.
- **Rendering:** Flat colour with one shadow tone and a thin dark line; no airbrush on the heads. The pitch strip is painted with the background's striped grass.
- **Colour:** Measured over the parts: pale cream #e2e3d2 35% and grass green #85c403 21% (the two wide strips), wolf blue-violet #58578a 21% and #aaa9bf 7%, dark navy #191932 4%. The wolf himself is a two-tone violet with light blue eyes.
- **Lighting:** Flat; no cast light on the character. Measured 'light from bottom' comes from the grass strips' gradient.
- **Ambience:** A pantomime villain as match official: the threat is a whistle and a puff of air.
- **Materials:** Fur as flat shapes, jersey cloth, a steel whistle.
- **Variants:** Landscape and portrait versions of pop-up, blow and tail; left and right tails. The sibling building-site game's wolf has the same animation list; here he wears the referee shirt and carries a whistle.
- **Motion:** 26 animations by the file's key times: pop-up in 3.08 s, loop 6.83 s, out 1.38 s; blow in 1.54 s, loop 4.17 s, out 0.92 s, reveal 5.04 s; tail 1.33 s. Faces are drawn frames (19 heads, 25-frame lick, 3 blinks, 4 paws, 5 whistles) placed on a 17-bone rig with 3 meshes. No skeleton frame is shown: the tool twists Spine 4.1 rigs.
- **Construction:** Spine skeleton exported as 4.1 from 4.2.43, 17 bones, 24 slots; 70 parts on five pages; character frames on a 1000x800 canvas, the lick on 1344x756, the pitch strips 3888x1108.
- **Notes:** The body is rigged and the face is drawn, the split the sibling game uses too: expression by hand, movement by rig.
- **Skeleton (from the file):** Spine 4.1-from-4.2.43 · 17 bones · 24 slots · animations: bkg_landscape (0 s), bkg_landscape_FG (0 s), blow_in_landscape (0 s), blow_in_portrait (0 s), blow_loop_landscape (0 s), blow_loop_portrait (0 s), blow_out_landscape (0 s), blow_out_portrait (0 s), blow_reveal_landscape (0 s), blow_reveal_portrait (0 s), popup_in_landscape (0 s), popup_in_landscape_BG (0 s), popup_in_portrait (0 s), popup_loop_landscape (0 s), popup_loop_landscape_BG (0 s), popup_loop_portrait (0 s), popup_out_landscape (0 s), popup_out_landscape_BG (0 s), popup_out_portrait (0 s), tail_left (0 s), tail_left_backup (0 s), tail_left_portrait_backup (0 s), tail_portrait_bkg (0 s), tail_right (0 s), tail_right_backup (0 s), tail_right_portrait_backup (0 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 65% · saturation 43% · contrast 53% · warm 2% / cool 67% · brighter towards: bottom (16), top (1)
- **Palette (measured):** #e2e3d2 light yellow 35%, #85c403 green 21%, #58578a blue 21%, #aaa9bf blue 7%, #aed556 green 4%, #191932 dark blue 4%


## Logo and title

The game's own wordmark.

### Loading screen pieces

`loading` · atlas · 10 parts · largest 1654×1654 · sheet `sheets/loading.webp`

- **Role:** The pictures of the loading screen, which the real screens show: the logo, a sample of the reels with the caption COLLECT (ball) TO TRIGGER THE KICK BALL FEATURE!, the Light & Wonder mark and the load bar over the daytime stadium.
- **Subject:** Three feature teasers (a 5x3 sample of reels full of balls, a sample with empty bronze and silver star frames, the stack of five jackpot titles), a half wheel with a SUPER MEGA BALL wedge in English and Spanish, the provider's mark, a green faceplate, a load bar with orange hazard stripes and a grey ring spinner.
- **Style:** Composed from the game's own symbols and plaques, shrunk; nothing is drawn only for this screen but the bar.
- **Rendering:** As the symbols: glossy painted pieces on dark cells.
- **Colour:** Measured: grey-green #374439 25%, near-black #101910 22%, greys #c8c7c5 16% and #7e7d7e 13%, green #26872e 5%, red #a60907 2%.
- **Lighting:** As the symbols.
- **Ambience:** A quick promise of the features before play.
- **Materials:** As the symbols; flat vector for the provider's mark.
- **Variants:** English and Spanish half wheels ('feature_EN', 'feature_sp').
- **Motion:** On the real loading screen the caption changes between teasers and the orange bar fills; the logo's letters animate.
- **Construction:** 'Red 7 Exporter' sheet, 10 frames, the spinner ring 1654 px, teasers 779 to 955 px wide.
- **Notes:** The loading screen teaches the two collection mechanics with real reel art instead of text panels.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 40% · saturation 40% · contrast 75% · warm 31% / cool 22% · brighter towards: top (3), top-left (2), left (1)
- **Palette (measured):** #374439 grey 25%, #101910 black 22%, #c8c7c5 grey 16%, #7e7d7e grey 13%, #26872e green 5%, #fbfaf7 light yellow 4%

### Animated logo

`game_logo` · atlas · 153 parts · largest 837×595 · sheet `sheets/game_logo.webp`

- **Role:** The logo at the top right of every real screen, on a bank of soap bubbles. It moves: between frames a ball rolls through GOALS!, the letters of PUFF pop and the black stroke crosses them.
- **Subject:** HUFF in riveted yellow planks, a small N' in black-and-yellow hazard stripes, LOTS OF in red, PUFF in glossy blue bubble letters struck out by a black brush stroke, and GOALS! in green with a football for the O over a black halftone shadow; grey-blue bubble clouds behind. A MORE word in red and a 'Text_EVEN' picture (which holds LOTS OF) are also in the set.
- **Style:** Each word in its own material, a sticker-pack logo; the struck-out PUFF is a joke on the series title: this one is about goals.
- **Rendering:** Fat bevelled letters with a white outline and a dark outer line; glass highlights on PUFF; flat comic shadow under GOALS!.
- **Colour:** Measured over the parts: black #050705 25%, green #27c41c 16% and #32492d 14% (72 frames of the GOALS! word dominate), pale green-white #f0f8ee 8%, cyan #70d0f0 3%, gold #e0b70f 3%.
- **Lighting:** Top and top-left light on every letter (measured 17 and 14).
- **Ambience:** Loud, jokey, self-aware.
- **Materials:** Wood with rivets, hazard tape, glossy plastic, soap bubbles, green enamel.
- **Variants:** One idle animation. The words HUFF, N', PUFF and MORE are the sibling games' logo parts reused; LOTS OF, the strike and GOALS! are new.
- **Motion:** One 4.0 s 'idle' by the file's key times, built from drawn sequences: the ball rolling through GOALS! 72 frames, HUFF 21, PUFF 21, MORE 16, N' 13, clouds 6. No skeleton frame is shown.
- **Construction:** Spine skeleton exported as 4.1 from 4.2.43, 16 bones, 22 slots, no meshes; 153 parts on eleven pages, word frames 490x320, the GOALS! frames 837x595.
- **Notes:** Eleven pages for one logo is the cost of animating lettering by redrawing it: the largest texture budget of any single element in the game.
- **Skeleton (from the file):** Spine 4.1-from-4.2.43 · 16 bones · 22 slots · animations: idle (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast · brightness 44% · saturation 50% · contrast 93% · warm 14% / cool 49% · brighter towards: top (17), top-left (14), top-right (3)
- **Palette (measured):** #050705 black 25%, #27c41c green 16%, #32492d dark green 14%, #f0f8ee light green 8%, #c8d9c6 light green 4%, #70d0f0 cyan 3%


## Win celebrations and banners

Big-win tiers, feature intro and outro banners, prize bursts.

### Feature intro panels

`fs_panels` · atlas · 104 parts · largest 1730×1209 · sheet `sheets/fs_panels.webp`

- **Role:** The panels that announce a feature: Kick Ball, Mega Ball, Cup and Wheel. Not seen on a real screen: no feature was triggered in 54 played spins.
- **Subject:** A top view of a football pitch as the panel (in two sizes), a large football, a rainbow prize wheel, a gold laurel wreath with a small gold trophy, a teal glass panel, light rays, and four slanted titles on a red brush stroke: KICK BALL FEATURE, MEGA BALL FEATURE, CUP FEATURE (red) and WHEEL FEATURE (blue). White brush swirls and cyan sparkle clouds are drawn sequences.
- **Style:** Sports-broadcast title cards in cartoon form: slanted italic lettering on a torn brush band.
- **Rendering:** Lettering in two colours with a dark outline and a white edge; objects painted glossy like the symbols; swirls are flat white brush marks.
- **Colour:** Measured: pitch green #77b62a 36%, greys and white #c8c9bb 12% and #ececea 11%, teal #064f73 9%, reds #a82512 and #e71e23 5% together, gold #f8e80f 2%.
- **Lighting:** Flat; a soft gold ring ('panel_glow_wheel') and outline glows are separate layers.
- **Ambience:** Kick-off energy: each feature is introduced like a fixture.
- **Materials:** Turf, leather, enamel, gold leaf.
- **Variants:** Four features on one skeleton; the wheel intro in landscape and portrait with a loop. File names keep the older words: megahat is Mega Ball, buzzsaw is Kick Ball, mansions is Cup.
- **Motion:** 7 animations by the file's key times: each intro 1.83 s (the wheel 1.88 s with a 0.96 s loop). Drawn sequences: two brush swirls of 26 and 20 frames and a 37-frame sparkle cloud.
- **Construction:** Spine 4.1.24, 13 bones, 12 slots, 3 meshes; 104 parts on six pages; the Mega Ball pitch panel is 1730x1209, the others 796 to 894 px.
- **Notes:** One rig serves four intros by swapping panel, object and title, each kept on its own canvas size.
- **Skeleton (from the file):** Spine 4.1.24 · 13 bones · 12 slots · animations: buzzsaw_intro (0 s), mansions_intro (0 s), megahat_intro (0 s), wheel_intro_landscape (0 s), wheel_intro_landscape_loop (0 s), wheel_intro_portrait (0 s), wheel_intro_portrait_loop (0 s)
- **Measured:** mid-tone, saturated, warm and cool mixed, medium contrast · brightness 60% · saturation 58% · contrast 38% · warm 24% / cool 44% · brighter towards: bottom (1), top (1)
- **Palette (measured):** #77b62a green 36%, #c8c9bb grey 12%, #ececea white 11%, #064f73 dark cyan 9%, #89928c grey 5%, #a82512 red 3%

### Big win

`bigwin` · atlas · 142 parts · largest 3888×1108 · sheet `sheets/bigwin.webp`

- **Role:** The big-win celebration in four tiers. Not seen on a real screen: the largest win caught was $10.20 at a $1.00 bet, which showed only the gold burst behind the amount (the 'fx_digits' frames here) and the line '6 ways pays $9.00'.
- **Subject:** The wolf referee again (body, five heads, blinks, whistle frames, air streaks) rising behind a hill of striped pitch, three large trophies in bronze, silver and gold with 29-frame 'out' sequences each, a wide gold light burst in 24 frames, green star and sparkle shapes, and a full-screen dark wolf silhouette with glowing blue eyes.
- **Style:** The same flat-drawn wolf and glossy trophies as elsewhere, staged as a scene.
- **Rendering:** Flat cel wolf, painted trophies, additive-looking light burst on black.
- **Colour:** Measured: pitch green #86c303 29%, cream #eeefd2 14%, wolf violet #565889 8%, black #19151a 7%, gold #f5ea5c 6%.
- **Lighting:** The burst and sparkles are the light; the trophies carry their own gloss.
- **Ambience:** A cup presentation interrupted by the referee: comic, with a short dark beat for the silhouette (inference from the 1920x1080 'wolf' and 'wolf_eyes' parts).
- **Materials:** Turf, fur, polished metal.
- **Variants:** Four tiers (tier_4 to tier_7) in landscape and two portrait layouts; three trophies, which by their names (House_01 to House_03, 'trophies-bronze/silver/gold_out') stand where the three houses stood in the sibling game's big win. That the wolf blows the trophies away tier by tier is inference from those names and sequences.
- **Motion:** 23 animations; intros grow with the tier by the file's key times: tier 5 0.71 s, tier 6 1.08 s with a 2.08 s loop, tier 7 3.08 s with a 4.17 s loop. Drawn sequences: 29 frames for each trophy leaving, a 24-frame light burst, 5 heads, 5 whistles, 3 blinks. No skeleton frame is shown.
- **Construction:** Spine 4.1.24, 43 bones, 43 slots, no meshes; 142 parts on five pages; trophies 324 px, the burst 468x182, the pitch strip 3888x1108.
- **Notes:** The celebration is cast from the game's own characters and prizes rather than generic coins and banners.
- **Skeleton (from the file):** Spine 4.1.24 · 43 bones · 43 slots · animations: effect (0 s), effectloop (0 s), sym13_win_gold (0 s), tier_4_in_landscape (0 s), tier_4_in_portrait (0 s), tier_4_loop_landscape (0 s), tier_4_loop_portrait (0 s), tier_5_in_landscape (0 s), tier_5_in_portrait (0 s), tier_5_loop_landscape (0 s), tier_5_loop_portrait (0 s), tier_6_in_landscape (0 s), tier_6_in_portrait (0 s), tier_6_in_portrait2 (0 s), tier_6_loop_landscape (0 s), tier_6_loop_portrait (0 s), tier_6_loop_portrait2 (0 s), tier_7_in_landscape (0 s), tier_7_in_portrait (0 s), tier_7_in_portrait2 (0 s), tier_7_loop_landscape (0 s), tier_7_loop_portrait (0 s), tier_7_loop_portrait2 (0 s)
- **Measured:** mid-tone, vivid, warm and cool mixed, medium contrast, hard-edged, strong highlights · brightness 61% · saturation 67% · contrast 52% · warm 35% / cool 40% · brighter towards: top (1), bottom (1)
- **Palette (measured):** #86c303 green 29%, #eeefd2 light yellow 14%, #565889 blue 8%, #19151a black 7%, #f5ea5c gold 6%, #a8afc3 blue 4%

### Big-win particles

`bigwin_particles` · atlas · 4 parts · largest 142×142 · sheet `sheets/bigwin_particles.webp`

- **Role:** The four pictures thrown as particles in a big win. Not seen on a real screen.
- **Subject:** A gold football coin, a gold star, a red boot and a football, each with a soft glow rim.
- **Style:** The game's own objects at icon size.
- **Rendering:** Painted, glossy, with a pale outer glow so they read over any background.
- **Colour:** Measured: cream #f6f4ea 18%, pale gold #f5d8a2 15%, gold #f7cf59 8%, dark grey #292c2f 10%, blue #86a3ca 6%.
- **Lighting:** Top-left light.
- **Ambience:** Confetti made of the theme.
- **Materials:** Gold, leather, synthetic boot.
- **Variants:** Four particles.
- **Motion:** Moved by the client's particle system; no frames of their own.
- **Construction:** 'Red 7 Exporter' sheet, four frames of 130 to 142 px.
- **Notes:** Even the particle shower is themed: coin, star, boot and ball instead of generic coins.
- **Measured:** bright, saturated, warm and cool mixed, high contrast, strong highlights · brightness 63% · saturation 42% · contrast 78% · warm 66% / cool 34% · brighter towards: top-left (2)
- **Palette (measured):** #f6f4ea light yellow 18%, #f5d8a2 light orange 15%, #292c2f grey 10%, #f7cf59 gold 8%, #b9bcc2 grey 6%, #86a3ca blue 6%


## Effects

Frame sequences, glows, particles and transitions.

### Wheel particle blast and rim glow

`wheelparticles` · atlas · 35 parts · largest 750×847 · sheet `sheets/wheelparticles.webp`

- **Role:** A burst of coloured sparks behind the wheel and a soft glow ring around it. Not identified on a real screen.
- **Subject:** Scattered green, cyan, magenta and orange sparks along an arc, and a pale gold ring.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Pale gold #f8d77d 18%, cyan #72f7e3 14%, magenta #ed68c8 7%, green #38fa24 6%, orange #f86b20 4% (measured): the wheel's own rainbow.
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Light.
- **Variants:** One sequence.
- **Motion:** Two animations: the blast 1.60 s and the top glow 0.57 s by the file's key times; the blast is 34 drawn frames.
- **Construction:** Spine 4.1.24, 7 bones, 5 slots, all five additive; 35 parts on nine pages, frames 750x847, the ring 795 px.
- **Notes:** The only skeleton in the game whose slots are all additive: pure light.
- **Skeleton (from the file):** Spine 4.1.24 · 7 bones · 5 slots · animations: wheel_bkg_blast_particle_anim (0 s), wheel_top_glow_anim (0 s)
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect, strong highlights · brightness 77% · saturation 51% · contrast 26% · warm 41% / cool 35%
- **Palette (measured):** #f8d77d orange 18%, #72f7e3 cyan 14%, #ed68c8 magenta 7%, #bbf0e6 light cyan 7%, #38fa24 green 6%, #57fa7b green 5%

### Wedge highlight

`superwheelfire` · atlas · 1 parts · largest 668×1170 · sheet `sheets/superwheelfire.webp`

- **Role:** A glowing outline the size of one wheel wedge. On a real screen the MAJOR JACKPOT wedge flared in a yellow glow when a wheel symbol upgraded it; that this outline is part of that flare is inference.
- **Subject:** A yellow wedge outline with a soft glow.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** A blurred vector outline.
- **Colour:** One colour, #ffff05 (measured 100%).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Light.
- **Variants:** One sequence.
- **Motion:** One animation, 'wheel_upgrade_glow_anim', 1.87 s by the file's key times.
- **Construction:** Spine 4.1.24, 2 bones, 1 slot; one 668x1170 picture.
- **Notes:** A whole skeleton for one glowing outline: the pulse is animated by the rig, not drawn.
- **Skeleton (from the file):** Spine 4.1.24 · 2 bones · 1 slots · animations: wheel_upgrade_glow_anim (0 s)
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 93% · saturation 98% · contrast 1% · warm 100% / cool 0%
- **Palette (measured):** #ffff05 gold 100%

### Scene transition

`transition` · atlas · 14 parts · largest 898×382 · sheet `sheets/transition.webp`

- **Role:** The wipe between base game and feature. Not seen on a real screen.
- **Subject:** A torn red band and a torn blue band with a burst of white halftone dots.
- **Style:** Comic-print graphic: torn paper bands and halftone dots.
- **Rendering:** Flat colour with a slight gradient; hard torn edges.
- **Colour:** White #ffffff 57%, red #db2129 27%, blue #0b7dd3 15% (measured): the two team colours.
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Paper and print.
- **Variants:** Landscape and portrait.
- **Motion:** Two animations, landscape and portrait, 1.42 s each by the file's key times; the dot burst is 12 drawn frames.
- **Construction:** Spine 4.1.24, 6 bones, 5 slots; 14 parts; bands 898x382 and 436x361.
- **Notes:** The sibling game wipes with caution tape; this one wipes with team colours and comic dots, the same idea in the new theme.
- **Skeleton (from the file):** Spine 4.1.24 · 6 bones · 5 slots · animations: transition_landscape (0 s), transition_portrait (0 s)
- **Measured:** bright, saturated, warm and cool mixed, low contrast, strong highlights · brightness 72% · saturation 38% · contrast 3% · warm 27% / cool 15% · brighter towards: top-left (1)
- **Palette (measured):** #ffffff white 57%, #db2129 red 27%, #0b7dd3 blue 15%

### Wedge upgrade sparkle

`wedge_upgrade_particle_anim` · atlas · 36 parts · largest 479×793 · sheet `sheets/wedge_upgrade_particle_anim.webp`

- **Role:** Gold sparkles that fill the outline of one wheel wedge when it is upgraded. One upgrade was seen on a real screen (the MAJOR JACKPOT wedge in a yellow flare); the sparkle itself cannot be told apart in that frame.
- **Subject:** A wedge-shaped swarm of small gold stars.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Gold #fded2a 64%, orange #fca41e 33% (measured); 100% warm.
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Light.
- **Variants:** One sequence.
- **Motion:** 36 drawn frames, 1.5 s at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet on five pages, frames up to 479x793.
- **Notes:** The sparkle is shaped to the wedge, so it reads as 'this prize changed'.
- **Measured:** bright, vivid, warm, low contrast, glow or soft effect, strong highlights · brightness 82% · saturation 84% · contrast 18% · warm 100% / cool 0%
- **Palette (measured):** #fded2a gold 64%, #fca41e orange 33%, #fefc72 gold 3%

### Ball smoke trail, short

`box_smoke_tail_s` · atlas · 34 parts · largest 530×167 · sheet `sheets/box_smoke_tail_s.webp`

- **Role:** The trail of smoke a collected ball leaves on its way to a goal; one of three lengths. The long version was seen on a real screen; which length each cell uses is not known.
- **Subject:** A rope of round cream puffs with a white core, and a second 'to reel' sequence of the same trail; grey fading puffs at the end.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Cream-white #fdf5eb about 60%, peach #f3d5bb about 35%, tan #c9ac94 (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke.
- **Variants:** Long, medium and short versions are separate units; each has an out and a 'to reel' sequence.
- **Motion:** Two sequences of 17 frames each (out, and 'to reel'), under a second at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet, 34 frames up to 530x167.
- **Notes:** The trail is the game's main base-game animation: every collected ball draws a line from the reels to its goal.
- **Measured:** bright, muted, warm, low contrast, strong highlights · brightness 89% · saturation 14% · contrast 21% · warm 100% / cool 0% · brighter towards: left (5)
- **Palette (measured):** #fdf6ed light orange 56%, #efd2b8 light orange 31%, #c9ab93 orange 13%

### Wheel rim: fire ring and gold ring

`wheel` · atlas · 18 parts · largest 862×864 · sheet `sheets/wheel.webp`

- **Role:** The rim of the prize wheel: an orange fire ring that animates and a plain gold ring. On the real screens an orange glow sits along the top of the wheel's arc.
- **Subject:** A thin ring of orange flame, and a thin gold circle.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Orange #fab356 48%, red-orange #fd410c 38%, #f98324 10% (measured); 100% warm.
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Fire and gold.
- **Variants:** Fire ring and static gold ring.
- **Motion:** 17 drawn frames of the fire ring, about 0.7 s a loop at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet on five pages, 18 frames; the fire ring 862x864, the gold ring 764x765.
- **Notes:** The file is named 'skeleton-wheel_fire_Orange': inference, a Spine effect baked to frames.
- **Measured:** mid-tone, vivid, warm, medium contrast, glow or soft effect · brightness 59% · saturation 78% · contrast 47% · warm 100% / cool 0%
- **Palette (measured):** #fab356 orange 48%, #fd410c red 38%, #f98324 orange 10%, #fce297 light orange 2%

### Ball smoke trail, long

`box_smoke_tail_l` · atlas · 42 parts · largest 1166×282 · sheet `sheets/box_smoke_tail_l.webp`

- **Role:** The trail of smoke a collected ball leaves on its way to a goal; one of three lengths. Seen on a real screen: a long cream trail runs from the bottom-left red ball diagonally up the reels toward the red goal.
- **Subject:** A rope of round cream puffs with a white core, and a second 'to reel' sequence of the same trail; grey fading puffs at the end.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Cream-white #fdf5eb about 60%, peach #f3d5bb about 35%, tan #c9ac94 (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke.
- **Variants:** Long, medium and short versions are separate units; each has an out and a 'to reel' sequence.
- **Motion:** Two sequences of 21 frames each (out, and 'to reel'), under a second at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet, 42 frames up to 1166x282.
- **Notes:** The trail is the game's main base-game animation: every collected ball draws a line from the reels to its goal.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 91% · saturation 14% · contrast 18% · warm 100% / cool 0% · brighter towards: left (1)
- **Palette (measured):** #fdf5eb light orange 58%, #f3d5bb light orange 35%, #c9ac95 orange 6%

### Wind blast with dust

`windbrickc` · atlas · 165 parts · largest 960×540 · sheet `sheets/windbrickc.webp`

- **Role:** The heavy version of the blow, full of dust clouds. Not seen on a real screen.
- **Subject:** Dozens of tan cartoon dust puffs with a darker underside, crossed by white speed streaks, filling a 960x540 frame and thinning out.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Tan #b8ac88 57%, white #fefefc 33%, darker tan #887d5c 6% (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Dust.
- **Variants:** One sequence.
- **Motion:** 165 drawn frames, about 6.9 s at 24 frames a second: the longest sequence in the game.
- **Construction:** 'Red 7 Exporter' sheet on 22 pages, the largest texture budget of any effect.
- **Notes:** In the sibling game this sheet blows a brick house apart; here the same file name carries dust only. That it plays when the wolf blows the reels is inference.
- **Measured:** bright, muted, warm, medium contrast, glow or soft effect, strong highlights · brightness 78% · saturation 18% · contrast 28% · warm 77% / cool 0% · brighter towards: bottom-left (2), left (1)
- **Palette (measured):** #b8ac88 yellow 57%, #fefefc light gold 33%, #887d5c yellow 6%, #e2daba light yellow 4%

### Reset smoke

`reset_anim` · atlas · 44 parts · largest 1208×650 · sheet `sheets/reset_anim.webp`

- **Role:** A large puff of smoke that covers the wheel when it resets. Not seen on a real screen.
- **Subject:** A dome of cream cartoon smoke that swells into a wide cloud with flying bits and clears.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Cream #f9e2cd 73%, white #fffefa 27% (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke, air or light.
- **Variants:** One sequence.
- **Motion:** 44 drawn frames, about 1.8 s at 24 frames a second, growing from 175x29 to 1208x650.
- **Construction:** 'Red 7 Exporter' sheet on six pages.
- **Notes:** The same cream smoke as the ball trails: one smoke for the whole game.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 93% · saturation 14% · contrast 14% · warm 100% / cool 0%
- **Palette (measured):** #f9e2cd light orange 73%, #fffefa light gold 27%

### Wheel trail, short

`wheel_trail_particle_anim_s` · atlas · 31 parts · largest 836×222 · sheet `sheets/wheel_trail_particle_anim_s.webp`

- **Role:** A streak of coloured sparks that travels from a reel cell toward the wheel; one of three lengths. Seen on a real screen: green, cyan and pink sparks rise from the wheel symbol on reel 4 to the wheel; which length that was is not known.
- **Subject:** A horizontal comet of green, pink, cyan and orange sparks with small white crosses.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Green, magenta, pale gold and orange in near equal parts (measured, for example #32f42d, #ee71be, #e4dbb0, #f46921).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Light.
- **Variants:** Long, medium and short versions are separate units.
- **Motion:** 31 drawn frames, about 1.3 s at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet, frames up to 836x222.
- **Notes:** Three lengths of one effect, for near, middle and far cells: the trail is drawn to length instead of being stretched.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect · brightness 71% · saturation 51% · contrast 41% · warm 48% / cool 24% · brighter towards: left (5), bottom-right (5), bottom-left (3)
- **Palette (measured):** #ee71be magenta 14%, #e5daaf light gold 10%, #2cf227 green 10%, #e4747e red 8%, #f5ede6 light orange 7%, #f5671f orange 6%

### Smoke under the goals

`box_smoke_blast` · atlas · 21 parts · largest 955×370 · sheet `sheets/box_smoke_blast.webp`

- **Role:** A low spread of smoke (the folder is 'cloudunderbox', the box being the goal). Not seen clearly on a real screen.
- **Subject:** A flat bank of beige-grey smoke puffs that spreads sideways and fades.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Beige #c4af88 93% (measured), semi-transparent.
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke, air or light.
- **Variants:** One sequence.
- **Motion:** 21 drawn frames, about 0.9 s.
- **Construction:** 'Red 7 Exporter' sheet on two pages, frames up to 955x370.
- **Notes:** Darker and flatter than the trail smoke, so it sits under the goal as a shadow of dust.
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect · brightness 68% · saturation 31% · contrast 16% · warm 100% / cool 0%
- **Palette (measured):** #c4af88 orange 93%, #978663 orange 7%

### Ball smoke trail, medium

`box_smoke_tail_m` · atlas · 38 parts · largest 722×212 · sheet `sheets/box_smoke_tail_m.webp`

- **Role:** The trail of smoke a collected ball leaves on its way to a goal; one of three lengths. The long version was seen on a real screen; which length each cell uses is not known.
- **Subject:** A rope of round cream puffs with a white core, and a second 'to reel' sequence of the same trail; grey fading puffs at the end.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Cream-white #fdf5eb about 60%, peach #f3d5bb about 35%, tan #c9ac94 (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke.
- **Variants:** Long, medium and short versions are separate units; each has an out and a 'to reel' sequence.
- **Motion:** Two sequences of 19 frames each (out, and 'to reel'), under a second at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet, 38 frames up to 722x212.
- **Notes:** The trail is the game's main base-game animation: every collected ball draws a line from the reels to its goal.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 92% · saturation 13% · contrast 18% · warm 100% / cool 0%
- **Palette (measured):** #fdf5eb light orange 64%, #f3d5bc light orange 34%, #c9ac94 orange 3%

### Smoke burst, white

`box_smoke_blast_hard_hat` · atlas · 16 parts · largest 851×546 · sheet `sheets/box_smoke_blast_hard_hat.webp`

- **Role:** A burst of white puffs and specks; by its name the burst of the red ball (the 'hard hat') being collected. Puffs burst at both goals on a real screen; which sheet each came from is not known.
- **Subject:** Round white puffs flying apart with small specks.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** White #ffffff (measured 100%).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke, air or light.
- **Variants:** One sequence.
- **Motion:** 16 drawn frames, about 0.7 s.
- **Construction:** 'Red 7 Exporter' sheet on two pages, frames up to 851x546.
- **Notes:** Pure white so the client can tint it; that it is tinted is inference.
- **Measured:** bright, muted, neutral, low contrast, glow or soft effect, strong highlights · brightness 100% · saturation 0% · contrast 0% · warm 4% / cool 0%
- **Palette (measured):** #ffffff light green 100%

### Wind (the wolf's blow)

`wind` · atlas · 68 parts · largest 942×525 · sheet `sheets/wind.webp`

- **Role:** The wolf's breath across the screen. Not seen on a real screen.
- **Subject:** White curved air streaks carrying yellow-green flecks, starting as thin vertical lines and widening into a gust.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** White #fffffc 72%, yellow #fed904 22% (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Air and flecks of grass (inference from their colour).
- **Variants:** One sequence.
- **Motion:** 68 drawn frames, about 2.8 s at 24 frames a second, growing from 85x265 to 942x525.
- **Construction:** 'Red 7 Exporter' sheet on eight pages.
- **Notes:** The series' signature action, kept: the wolf still blows, here across a pitch.
- **Measured:** bright, saturated, warm, low contrast, glow or soft effect, strong highlights · brightness 95% · saturation 25% · contrast 11% · warm 82% / cool 0%
- **Palette (measured):** #fffffc light gold 72%, #fed904 gold 22%, #fdf1a3 light gold 4%, #fce763 gold 3%

### Wheel trail, long

`wheel_trail_particle_anim_l` · atlas · 30 parts · largest 1148×244 · sheet `sheets/wheel_trail_particle_anim_l.webp`

- **Role:** A streak of coloured sparks that travels from a reel cell toward the wheel; one of three lengths. Seen on a real screen: green, cyan and pink sparks rise from the wheel symbol on reel 4 to the wheel; which length that was is not known.
- **Subject:** A horizontal comet of green, pink, cyan and orange sparks with small white crosses.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Green, magenta, pale gold and orange in near equal parts (measured, for example #32f42d, #ee71be, #e4dbb0, #f46921).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Light.
- **Variants:** Long, medium and short versions are separate units.
- **Motion:** 30 drawn frames, about 1.3 s at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet, frames up to 1148x244.
- **Notes:** Three lengths of one effect, for near, middle and far cells: the trail is drawn to length instead of being stretched.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect · brightness 73% · saturation 52% · contrast 40% · warm 37% / cool 33% · brighter towards: left (8)
- **Palette (measured):** #31f42e green 14%, #ec72bc magenta 11%, #64f8d8 cyan 9%, #e4d8af light yellow 8%, #a2ebc9 light green 7%, #edeee9 white 7%

### Smoke burst with sparkles

`box_smoke_blast_with_sparkle` · atlas · 16 parts · largest 875×456 · sheet `sheets/box_smoke_blast_with_sparkle.webp`

- **Role:** The burst where a ball's trail arrives at a goal. Seen on real screens: a cream puff at the red goal after red balls were collected, and one with yellow flecks at the blue goal.
- **Subject:** A cream puff with yellow-green flecks shooting outward.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Cream-white #fdf8ef 57%, peach #f7dab7 33%, yellow #fdf362 10% (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke, air or light.
- **Variants:** One sequence.
- **Motion:** 16 drawn frames, about 0.7 s.
- **Construction:** 'Red 7 Exporter' sheet on one page, frames up to 875x456.
- **Notes:** Arrival is marked brighter than departure: the eye is led to the goal.
- **Measured:** bright, muted, warm, low contrast, glow or soft effect, strong highlights · brightness 93% · saturation 18% · contrast 13% · warm 100% / cool 0%
- **Palette (measured):** #fdf8ef light orange 57%, #f7dab7 light orange 33%, #fdf362 gold 10%

### Smoke burst on the reels

`box_smoke_blast_reel` · atlas · 16 parts · largest 328×238 · sheet `sheets/box_smoke_blast_reel.webp`

- **Role:** The puff where a collected ball leaves its cell. Seen on real screens: a cream puff sits on the bottom-left red ball as its trail leaves.
- **Subject:** A compact cream puff with a white core that swells and fades.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Cream-white #fef8f0 65%, peach #f7d7bb 35% (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke, air or light.
- **Variants:** One sequence.
- **Motion:** 16 drawn frames, about 0.7 s.
- **Construction:** 'Red 7 Exporter' sheet on one page, frames 65x54 to 328x238.
- **Notes:** The 'puff' of the title, kept in a game about goals.
- **Measured:** bright, muted, neutral, low contrast, strong highlights · brightness 94% · saturation 12% · contrast 13% · warm 100% / cool 0%
- **Palette (measured):** #fef8f0 light orange 65%, #f7d7bb light orange 35%

### Wheel spin and pointer effects

`wheel_fx` · atlas · 43 parts · largest 810×390 · sheet `sheets/wheel_fx.webp`

- **Role:** A streak of gold smoke that follows the turning wheel and a spark burst at the pointer. Not seen on a real screen.
- **Subject:** A curved gold and grey smoke streak, and a star-shaped orange spark burst around a gold arrowhead.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Muted gold #bba778 34%, orange #fab936 26%, pale yellow #fbf58f 24% (measured).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Smoke and sparks.
- **Variants:** Two sequences.
- **Motion:** Two sequences: 'fx_spin' 31 frames and 'fx_clicker' 12 frames, about 1.3 s and 0.5 s at the sheets' 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet on two pages, 43 frames, up to 810x390.
- **Notes:** The pointer's click gets its own drawn burst: the wheel is treated as a physical thing.
- **Measured:** bright, saturated, warm, medium contrast, glow or soft effect, strong highlights · brightness 75% · saturation 49% · contrast 30% · warm 100% / cool 0% · brighter towards: bottom (2), bottom-right (2), top-right (1)
- **Palette (measured):** #bba778 orange 34%, #fab936 orange 26%, #fbf58f light gold 24%, #8c815f yellow 5%, #fefef1 light gold 5%, #c99c48 orange 3%

### Wheel trail, medium

`wheel_trail_particle_anim_m` · atlas · 32 parts · largest 1015×229 · sheet `sheets/wheel_trail_particle_anim_m.webp`

- **Role:** A streak of coloured sparks that travels from a reel cell toward the wheel; one of three lengths. Seen on a real screen: green, cyan and pink sparks rise from the wheel symbol on reel 4 to the wheel; which length that was is not known.
- **Subject:** A horizontal comet of green, pink, cyan and orange sparks with small white crosses.
- **Style:** Hand-drawn cartoon effect.
- **Rendering:** Flat shapes in two or three tones with soft edges, drawn frame by frame.
- **Colour:** Green, magenta, pale gold and orange in near equal parts (measured, for example #32f42d, #ee71be, #e4dbb0, #f46921).
- **Lighting:** Self-lit; no directional light.
- **Ambience:** A quick accent, not a mood.
- **Materials:** Light.
- **Variants:** Long, medium and short versions are separate units.
- **Motion:** 32 drawn frames, about 1.3 s at 24 frames a second.
- **Construction:** 'Red 7 Exporter' sheet, frames up to 1015x229.
- **Notes:** Three lengths of one effect, for near, middle and far cells: the trail is drawn to length instead of being stretched.
- **Measured:** bright, saturated, warm and cool mixed, medium contrast, glow or soft effect · brightness 72% · saturation 52% · contrast 41% · warm 42% / cool 29% · brighter towards: left (6), bottom-left (3), bottom-right (2)
- **Palette (measured):** #32f42d green 15%, #ee71be magenta 12%, #e4dbb0 light yellow 10%, #f6f0ea light orange 8%, #e5757d red 6%, #f46921 orange 6%


## Game interface

Buttons, counters and panels drawn for this game.

### Game-styled buttons (not seen on screen)

`ui` · atlas · 57 parts · largest 576×105 · sheet `sheets/ui.webp`

- **Role:** A full set of game-coloured controls: spin, stop, skip, fast-forward, autoplay, stake, settings, plus and minus. The real desktop screens do not show them: there the provider's grey round controls are used. Where this set appears (another layout or market) is not known from this run.
- **Subject:** Round buttons with a steel-blue rim: orange with a green arrow for spin, skip and fast-forward, red with a yellow square for stop, green with yellow icons for autoplay, stake and settings; green plus and minus bars; dark green meter and toggle backgrounds; an orange message bar.
- **Style:** Arcade console buttons in the game's green and gold.
- **Rendering:** Glossy domed buttons with a top highlight, a bevelled metal rim and a dark outline; hard edges (soft edge 0.03).
- **Colour:** Measured: dark green #0f3b10 29%, muted orange-brown #796849 18% (the disabled states), grey #849c99 8%, gold #f7c234 6%, orange #d2690e 3%.
- **Lighting:** Top light on every button (41 of 47 measured).
- **Ambience:** Friendly and toy-like, warmer than the provider's glass controls.
- **Materials:** Enamel domes in metal rims.
- **Variants:** Four states of every button: base, hover, down, disabled.
- **Motion:** None in the files beyond the state swaps.
- **Construction:** 'Red 7 Exporter' sheet on one page, 57 frames: large buttons 204 px, small ones 114 px.
- **Notes:** A themed control set exists beside the provider's standard one; a studio can ship both and let the platform choose.
- **Measured:** mid-tone, saturated, warm and cool mixed, high contrast, hard-edged · brightness 42% · saturation 59% · contrast 62% · warm 49% / cool 28% · brighter towards: top (41), top-left (3), top-right (3)
- **Palette (measured):** #0f3b10 dark green 29%, #796849 orange 18%, #849c99 grey 8%, #39503d dark green 7%, #f7c234 orange 6%, #d6f1f1 light cyan 5%

### Paytable pictures

`_paytable` · atlas · 12 parts · largest 379×237 · sheet `sheets/_paytable.webp`

- **Role:** Pictures made for the paytable's feature pages. The real paytable screen reached shows only the first page (the five high symbols with their pays); the pages that use these pictures were not reached.
- **Subject:** A half wheel in English and in Spanish, the three star frames (named brick, stick, straw: gold, silver, bronze) and the three trophies, and the red ball block at three sizes plus the ball on blue.
- **Style:** As the game's own art, reduced for the help pages.
- **Rendering:** As the source pieces.
- **Colour:** Measured: dark red #a10503 11%, silver-blue #abb5c5 10%, black #121012 9%, brown #603312 7%, gold #f4d83a 6%, blue #243f8a 4%.
- **Lighting:** As the source pieces.
- **Ambience:** Explanatory.
- **Materials:** As the source pieces.
- **Variants:** English and Spanish wheel pictures; the red ball in 2x2, 3x3 and 3x5 block shapes ('megahat_two_two', 'megahat_three_three', 'megahat_three_five').
- **Motion:** None.
- **Construction:** 'Red 7 Exporter' sheet, 12 frames, 135 to 379 px.
- **Notes:** The block pictures confirm what the skeleton's names say: the red ball can land as a 2x2, 3x3 or 3x5 block.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast · brightness 45% · saturation 62% · contrast 79% · warm 66% / cool 30% · brighter towards: top-left (3), top-right (1), top (1)
- **Palette (measured):** #a10503 red 11%, #abb5c5 blue 10%, #121012 black 9%, #603312 brown 7%, #eeefea light green 6%, #f4d83a gold 6%

### Prize wheel wedges

`en_us_wheel_2048x2048` · atlas · 21 parts · largest 549×1059 · sheet `sheets/en_us_wheel_2048x2048.webp`

- **Role:** The wedges of the big prize wheel that turns behind and above the reels. The real screens show its top arc with CUP FEATURE, MAJOR JACKPOT, MINI JACKPOT, MINOR JACKPOT, MEGA BALL FEATURE and SUPER JACKPOT wedges passing.
- **Subject:** Sixteen long pennant-shaped wedges with a round medallion and drawn words: the four jackpots, SUPER JACKPOT, KICK BALL FEATURE, CUP FEATURE, MEGA BALL FEATURE, their SUPER versions and a gold UPGRADE wedge with chevrons; two wedge outline frames; and two pointers that are shield-shaped badges holding a football, in gold and in silver.
- **Style:** Fairground wheel crossed with football pennants: each wedge is a club pennant with a crest.
- **Rendering:** Glossy gradients inside a bright rim line, lettering bevelled and outlined; flames painted on the Mega Ball wedges, mown stripes on the Kick Ball wedges.
- **Colour:** Measured: brown-orange #a94b13 10%, black #0e0d0b 8%, dark red #55120a 6%, gold #f7dd61 6%, navy #111b52 5%, blue #0a4eef 3%. One colour per prize: magenta Mini, green Minor, blue Major, red-orange Grand, gold Super, purple Cup, cyan and green Kick Ball, red with fire Mega Ball.
- **Lighting:** Top light on the medallions (9 of 12 measured); each wedge darkens to black at its point.
- **Ambience:** The loudest, most saturated thing on screen, kept half hidden behind the reels so it promises more than it shows.
- **Materials:** Enamel, gold trim, flame, turf.
- **Variants:** A '_g' (gold wheel) and an '_s' (super wheel) version of several wedges, and gold and silver pointers. File names keep the older words: buzz_saw is Kick Ball, megahat is Mega Ball, House is Cup.
- **Motion:** The wedges are stills; the wheel is turned by the client. On the real screens it stands at a different wedge in each frame.
- **Construction:** 'Red 7 Exporter' sheet on six 2048x2048 pages, 21 frames; a wedge is about 548x1059, so the whole wheel is over 2,000 px across at the shipped size.
- **Notes:** The tier colours on the wedges are the same as on the plaques at the left: one colour per prize on every surface.
- **Measured:** mid-tone, vivid, warm and cool mixed, high contrast, hard-edged · brightness 41% · saturation 71% · contrast 76% · warm 53% / cool 39% · brighter towards: top (9), bottom (3)
- **Palette (measured):** #a94b13 brown 10%, #0e0d0b black 8%, #55120a dark red 6%, #f7dd61 gold 6%, #e5e2d8 light yellow 5%, #111b52 dark blue 5%


## Provider interface (shared)

The provider's common controls, lobby and promotion art, the same in all its games. Not this game's art direction.

- `notosans`: 17 parts
- `check`: 1 parts
- `lnw_logo`: 1 parts
- `no_check`: 1 parts
- `progressbar_ninepatch`: 1 parts
- `ui_icon_replay`: 1 parts
- `info`: 1 parts
- `autospins`: 1 parts
- `autospinsrectangle`: 1 parts
- `buypass`: 1 parts
- `buypassclicked`: 1 parts
- `buypassdisabled`: 1 parts
- `buypasshover`: 1 parts
- `turbohover`: 1 parts
- `turboon`: 1 parts
- `eclipse`: 1 parts
- `eclipse_glow`: 1 parts
- `swedish_depositlimit_icon`: 1 parts
- `swedish_selfassessment_icon`: 1 parts
- `swedish_selfexclusion_icon`: 1 parts
- `betautoplayswitchbuttons`: 8 parts
- `settings-menu`: 8 parts
- `basegameui`: 56 parts

## Typography

Typefaces embedded in the bundles (specimen: `sheets/_fonts.webp`): Frutiger Neue LT Pro (Medium); Jost (Black); Jost (Black Italic); Jost (Bold); Noto Sans (Regular); Outfit (Black); Outfit (Bold); icomoon (Regular).

## How this was made, and its limits

- The demo was opened in a browser at 1280×720 and every art file it loaded was kept (capture.mjs). No session key was stored.
- The files were read as the images the game loaded, split where a sprite sheet description was found (extract.py): 1702 components cut from 168 textures, upright and unscaled.
- The art is at the size this client shipped it. Atlases carry a resize percentage (many are 50 to 69% of the source art), so the studio's working files are larger than what is here.
- Only the layout this viewport loaded was captured. A phone in portrait may load other backgrounds and sizes.
- Skeleton pictures are frames of the skeleton's own animations, drawn from the shipped parts (render_spine.py): bones, constraints, mesh deformation, clipping, colour and draw order are applied. Path constraints and two-colour tint are not, so a few effects can sit slightly off.
- Measures (palette, brightness, saturation, contrast, warm and cool, where the light sits) come from the pixels with fixed thresholds (measure.py), so two runs can be compared. Style, mood and technique are a reading by eye.
- The real game screens come from play of the same demo (the Game-GDDs capture of the same day, where one exists); they are the reference for how a character or a scene looks, and the skeleton frames are the reference for what it is built from.
- The blueprint of the whole package, piece by piece, is Art-package.md and art-package.json in the run folder.
- This is a competitor's art, kept for study inside the studio. It is a reference for direction and production method, not material to reuse.
