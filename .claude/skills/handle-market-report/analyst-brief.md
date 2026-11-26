# Brief for the analyst of one game

You analyse the art of **one** leading slot game with the Games AI art project, from finding its public demo to a published art report. Other analysts are doing other games at the same time in the same folders, so the limits below matter.

Your prompt gives: the game's ledger id, its title and provider as the market report prints them, the provider key, and Roei's request to quote.

## Read first

- `/home/user/Games-AI-art/CLAUDE.md`, `README.md` and `.claude/skills/extract-game-art/SKILL.md`: the rules and the procedure. You follow that skill, with the changes below.
- One finished example to match in depth and voice: `/home/user/Games-AI-art/runs/2026-11-24-1733-pragmatic-zeus-vs-hades-pop/analysis/game.json` and one of its `analysis/*.json` unit files.

## Limits (several analysts share the machine)

- **Touch only your own run folder** `/home/user/Games-AI-art/runs/<your run id>/` and your own record `/home/user/Games-AI-art/records/2026-11-25-<provider key>-<game slug>.md`. Scratch files go in a folder of your own under the scratchpad directory.
- **No git**: no add, commit, push, checkout or lfs command, in any repository. The caller commits.
- **Do not edit** `README.md`, `tools/`, `categories.json` or anything in `/home/user/market-reports-handler/` (the ledger is the caller's). A rule you think belongs in `tools/categories.json` goes in your run's `classification.json` and in your final message as a suggestion.
- **No Drive and no Miro** in this batch, and nothing posted or sent anywhere. The only thing you publish is the art report, as a private artifact.
- Public pages only: no login, no account, no real-money play. Never write a session key anywhere (`mgckey=`, `token=`, `session=`, `key=`, `jwt=`); a `securetoken=null` or empty parameter is not a secret.
- The capture names itself as desktop Chrome (Roei, 26 Nov 2026: "yes it may identify itself as it needs to make it work"); that is built into `tools/capture.mjs`, and your own play script may use the same user agent. It is the only allowance: still no proxy or VPN, no age or consent gate, no account.
- Three other browsers may be running: give a game time to load (`--wait 60`) before deciding it is broken.

## Steps

1. **Find the demo.** The studio's product team uses slotslaunch.com, and its Free Play opens the provider's own free-play client.
   - Find the game's page there: try `https://slotslaunch.com/<provider>/<game-slug>` (provider slugs such as `igt`, `light-and-wonder`, `games-global`, `aristocrat`, `white-hat-studios`, `octoplay`, `netent`, `evolution`, `reelplay`, `ags`), the provider's listing page, or a web search for the title with "slotslaunch". US titles are sometimes listed under a slightly different name (the studio's name instead of the parent's, "&" for "And"): make sure it is this exact game and version, not a sibling ("Cash Eruption" is not "Triple Cash Eruption").
   - `node /home/user/market-reports-handler/tools/find_demo.js "<page>" 25000 <screenshot.png>` presses Free Play and prints the frames. The provider's frame (not `slotslaunch.com/...`) is the demo link; if it carries a session key that cannot be dropped, use the `https://slotslaunch.com/game/<n>` frame instead.
   - If Slotslaunch does not have it, try the provider's own site and other public demo hosts. If no public free-play demo of this exact game opens after a fair search, stop and report **blocked** with what you tried.

2. **Record first**: your record file, with the request quoted, the link, and what you decide.

3. **Run the pipeline** from `/home/user/Games-AI-art`:
   ```bash
   NODE_PATH=/opt/node-tools/node_modules node tools/run.mjs "<demo link>" --provider <provider key> --game "<Title>" --requested "<the request>" --wait 60 [--viewport 1280x720] [--clicks "x,y x,y"] [--spin "x,y"] [--spin-wait 5]
   ```
   These are not Pragmatic Play games, so the reader is `generic` and the capture's default clicks often stop at an intro or a sound question. Do a first try with `tools/capture.mjs "<link>" <scratch folder>` alone, look at `screens/01-loaded.png` and `02-main.png`, work out the click points that reach the reels and where the spin button is, then do the real run with `--clicks` and `--spin`. Only the real run lives in `runs/`.
   - Check the output as the skill says: the counts, the sheets, and that the screens show the game in play.
   - Skeletons: the `generic` reader may draw none (other Spine versions, binary skeletons, or sprite-sheet animation instead). Say what the game uses for motion from the files you see; do not present an empty `assembled/` as a finding about the game.

4. **Real game screens.** Play the demo in your own short Playwright script (same link, same viewport): the base game at rest, spins, a win, the paytable or info pages, and a feature or bonus if it comes within about 60 spins or a free-play buy. Save PNG or WebP frames with a `screens.json` in the shape `tools/add_game_screens.py` reads (look at the tool and at the example run's `game-screens/index.json`), then add them. Say in the record which stages you did not reach.

5. **Sort.** Open sheets from each art component; the `generic` reader leaves much in "Other". Put every unit you can place into its component through `<run>/classification.json`, then run `measure.py` and `sheets.py` again.

6. **Read every unit** outside `provider-ui`, yourself (you have no sub-reviewers): `python3 -I tools/brief.py <run> <categories>` names each unit's sheet and measured facts; open every sheet before writing its unit. Write `analysis/<group>.json` files keyed by unit id with exactly the skill's fields, then `analysis/game.json` with the art direction and `takeaways`. Only what is seen or measured; inference marked as inference; measured hex values cited for colour; no invented figure.

7. **Build and look**: `build_package.py`, `build_report.py`; every unit outside `provider-ui` read. Look at `report.html` once at desktop and phone width (a Playwright screenshot of the local file).

8. **Publish** `report.html` as its own private artifact with the Artifact tool: `root` the run folder, `files` the paths in `report-files.json`, `icon` "palette". Put the address in your record.

9. **Check for secrets**: `grep -rIl -E "mgckey=|token=[A-Za-z0-9]|session=[A-Za-z0-9]|jwt=" runs/<run id> --exclude-dir=raw` prints nothing.

## Your final message (the caller reads only this)

Plain lines, nothing else:

```
STATUS: complete | blocked
GAME: <ledger id>
RUN: <run id>
REPORT: <artifact address>
DEMO: <the demo link used, no session key>
COUNTS: <textures, named sprites, skeletons, fonts, units read / units>
SCREENS: <which stages have real screens; which were not reached>
DIRECTION: <the art direction in three sentences>
OPEN: <what stays open or was skipped>
SUGGESTIONS: <tool or rule changes worth making, if any>
```

For blocked: `STATUS`, `GAME`, and `REASON: <what was tried and what failed>`.
