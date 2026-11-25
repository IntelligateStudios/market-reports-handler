#!/usr/bin/env python3
"""The game ledger: one entry per game, however many reports name it, with where its analysis stands.

Reads:  registry/games.json, registry/providers.json, reports/<id>/rankings.json and report.json;
        for `seed`, the sibling repositories (Games-AI-art runs, Intelligate HQ competitor GDDs and market research);
        for `complete`, the finished art run's folder in Games-AI-art.
Writes: registry/games.json; reports/<id>/report.json (the report's leaders) and reports/<id>/unify.json (what
        each ranked name was taken as); analyses/<game id>/art/ (the digest of a finished art run: digest.json,
        Art-report.md and a few small game screens), so this repository can build its pages alone.

Commands (python3 -I tools/ledger.py <command> …):
  seed [--hq <dir>] [--art <dir>]      take in what the studio already has on record
  unify <report id> [--top 20] [--dry-run]
                                       match the report's ranked games to the ledger, add the new ones, and fix
                                       the report's leaders; stops, writing nothing, on a name it cannot place
  queue [--json]                       leaders of any report whose art analysis is not complete, best first
  start <game id> [--run <run id>]     an art run has begun
  complete <game id> --run <run dir> --report <url> [--drive <url>] [--miro <url>] [--commit <sha>]
  block <game id> --reason "<why>"     the analysis cannot run (no public demo, a client the tools cannot read…)
  set <game id> <key>=<value> …        demo, name, provider, type, family, notes; alias+=<another spelling>
  status                               the whole ledger in one table

A game's id is <provider key>-<name slug>, the same as its art run's folder name without the date.
"""
import argparse
import datetime
import difflib
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry" / "games.json"
PROVIDERS = ROOT / "registry" / "providers.json"
REPORTS = ROOT / "reports"
ANALYSES = ROOT / "analyses"
SECRET = re.compile(r"(mgckey|token|session|sessionid|sid|key)=", re.I)
TOP = 20


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── names ────────────────────────────────────────────────────────────────────


def norm(text):
    """A name as it is compared: no accents, marks, case or punctuation; '&' is 'and'."""
    text = (text or "").replace("™", " ").replace("®", " ").replace("©", " ")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower().replace("&", " and ").replace("™", " ").replace("®", " ")
    text = re.sub(r"[’'`]", "", text)
    text = re.sub(r"[^a-z0-9]+", " ", text).strip()
    text = re.sub(r"\s+(slot|slots|online slot|video slot)$", "", text)
    return text


def slug(text):
    return norm(text).replace(" ", "-")


def load_providers():
    table = json.loads(PROVIDERS.read_text())["providers"]
    lookup = {}
    for key, spellings in table.items():
        lookup[norm(key)] = key
        for s in spellings:
            lookup[norm(s)] = key
    return table, lookup


def provider_key(name, lookup):
    """The provider's key, and whether registry/providers.json knows the spelling."""
    if not name:
        return None, True
    n = norm(name)
    if n in lookup:
        return lookup[n], True
    return n.replace(" ", ""), False


# ── the ledger file ──────────────────────────────────────────────────────────


def load():
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text())
    return {"version": 1, "updated": None, "games": []}


def save(ledger):
    ledger["games"].sort(key=lambda g: g["id"])
    ledger["updated"] = now()
    REGISTRY.parent.mkdir(exist_ok=True)
    REGISTRY.write_text(json.dumps(ledger, ensure_ascii=False, indent=1) + "\n")


def by_id(ledger, game_id):
    for g in ledger["games"]:
        if g["id"] == game_id:
            return g
    sys.exit(f"No game '{game_id}' in the ledger. `ledger.py status` lists them.")


def new_game(name, provider, key, kind="slot"):
    return {
        "id": f"{key or 'unknown'}-{slug(name)}",
        "name": name,
        "provider": provider,
        "providerKey": key,
        "type": kind,
        "aliases": [],
        "demo": None,
        "appearances": [],
        "existing": [],
        "analysis": {"art": {"status": "none"}},
        "added": now(),
    }


def names_of(game):
    return {norm(game["name"])} | {norm(a) for a in game.get("aliases", [])}


def place(ledger, name, key):
    """Where a ranked name belongs: ('match', game), ('new', None) or ('ask', [candidates])."""
    n = norm(name)
    exact = [g for g in ledger["games"] if n in names_of(g)]
    if key:
        same = [g for g in exact if g["providerKey"] == key]
        if len(same) == 1:
            return "match", same[0]
        open_provider = [g for g in exact if not g["providerKey"]]
        if len(open_provider) == 1 and not same:
            return "match", open_provider[0]
        if exact:  # the same title under another provider: a clone, or one of the two is wrong
            return "ask", exact
    elif len(exact) == 1:
        return "match", exact[0]
    elif exact:
        return "ask", exact
    close = []
    for g in ledger["games"]:
        if key and g["providerKey"] and g["providerKey"] != key:
            continue
        ratio = max(difflib.SequenceMatcher(None, n, m).ratio() for m in names_of(g))
        # A title that only adds words to another ("… 1000", "… Megaways") is a version: a game of its own,
        # but close enough to a slip of the pen that a person decides.
        version = any(n.startswith(m + " ") or m.startswith(n + " ") for m in names_of(g))
        if ratio >= 0.88 or version:
            close.append(g)
    if close:
        return "ask", close
    return "new", None


# ── seed ─────────────────────────────────────────────────────────────────────


def clean_url(url):
    if url and SECRET.search(url):
        sys.exit(f"The link carries a session parameter and is not written: {url.split('?')[0]}?…")
    return url


def upsert(ledger, lookup, name, provider, kind="slot"):
    key, _ = provider_key(provider, lookup)
    verdict, game = place(ledger, name, key)
    if verdict == "match":
        return game
    game = new_game(name, provider, key, kind)
    ledger["games"].append(game)
    return game


def add_existing(game, entry):
    if entry not in game["existing"]:
        game["existing"].append(entry)


def cmd_seed(args):
    ledger = load()
    _, lookup = load_providers()
    hq, art = Path(args.hq), Path(args.art)

    research = sorted(hq.glob("records/market-research/*/run.json"))
    for path in research:
        run = json.loads(path.read_text())
        for position, g in enumerate(run["games"], 1):
            series = re.search(r"\s+(and the .* series|series)$", g["name"])
            name = g["name"][: series.start()] if series else g["name"]
            kind = "slot" if g.get("type") == "Video slot" else (g.get("type") or "other").lower()
            game = upsert(ledger, lookup, name, g["provider"], kind)
            entry = {"kind": "research", "repo": "IntelligateStudios/intelligate-ai", "run": run["id"], "position": position}
            if series:
                entry["as"] = g["name"]
            add_existing(game, entry)

    for path in sorted(hq.glob("records/competitor-gdds/*/run.json")):
        run = json.loads(path.read_text())
        game = upsert(ledger, lookup, run["game"], run["provider"])
        add_existing(game, {"kind": "gdd", "repo": "IntelligateStudios/intelligate-ai", "run": path.parent.name})
        url = (run.get("source") or {}).get("url")
        if url and not game["demo"]:
            game["demo"] = {"url": clean_url(url), "from": f"intelligate-ai records/competitor-gdds/{path.parent.name}"}

    for path in sorted(art.glob("runs/*/run.json")):
        run = json.loads(path.read_text())
        game = upsert(ledger, lookup, run["game"], run["provider"])
        add_existing(game, {"kind": "art", "repo": "IntelligateStudios/Games-AI-art", "run": run["id"]})
        url = (run.get("source") or {}).get("url")
        if url and not game["demo"]:
            game["demo"] = {"url": clean_url(url), "from": f"Games-AI-art runs/{run['id']}"}
        if game["analysis"]["art"]["status"] == "none":
            game["analysis"]["art"] = {"status": "found", "run": run["id"], "note": "A run exists in Games-AI-art. Close it with `ledger.py complete`."}

    save(ledger)
    print(f"{len(ledger['games'])} games in the ledger.")


# ── unify ────────────────────────────────────────────────────────────────────


def leaders_of(appearances, weights, top):
    """The report's leading slot games. Points: weight × (21 − rank) for ranks 1–20, summed over its lists.

    This is the handler's rule for putting several lists into one order, not a figure of the report.
    Ties: the better best rank, then the name.
    """
    table = {}
    for game, rows in appearances.items():
        points = sum(weights.get(r["list"], 1) * max(0, TOP + 1 - r["rank"]) for r in rows if r.get("rank"))
        ranked = [r for r in rows if r.get("rank")]
        if not points or not ranked:
            continue
        best = min(ranked, key=lambda r: r["rank"])
        table[game] = {"game": game, "points": round(points, 2), "best": {"list": best["list"], "rank": best["rank"]}, "lists": len(ranked)}
    order = sorted(table.values(), key=lambda t: (-t["points"], t["best"]["rank"], t["game"]))[:top]
    for position, row in enumerate(order, 1):
        row["position"] = position
    return order


def cmd_unify(args):
    folder = REPORTS / args.report
    header_path, rankings_path = folder / "report.json", folder / "rankings.json"
    if not rankings_path.exists():
        sys.exit(f"reports/{args.report}/rankings.json is not written yet (schema in README.md).")
    header = json.loads(header_path.read_text())
    rankings = json.loads(rankings_path.read_text())
    ledger = load()
    _, lookup = load_providers()

    for g in ledger["games"]:  # a second unify of the same report replaces its first
        g["appearances"] = [a for a in g["appearances"] if a["report"] != args.report]

    log, asks, unknown_providers, per_game, weights = [], [], set(), {}, {}
    seen_lists = set()
    for lst in rankings.get("lists", []):
        if lst["id"] in seen_lists:
            sys.exit(f"Two lists share the id '{lst['id']}'.")
        seen_lists.add(lst["id"])
        weights[lst["id"]] = lst.get("weight", 1)
        for e in lst["entries"]:
            key, known = provider_key(e.get("provider"), lookup)
            if not known:
                unknown_providers.add(e["provider"])
            if e.get("is"):
                verdict, game = "match", by_id(ledger, e["is"])
            elif e.get("new"):
                verdict, game = "new", None
            else:
                verdict, game = place(ledger, e["game"], key)
            if verdict == "ask":
                asks.append((lst["id"], e, game))
                continue
            if verdict == "new":
                game = new_game(e["game"], e.get("provider"), key, e.get("type", "slot"))
                if any(g["id"] == game["id"] for g in ledger["games"]):
                    sys.exit(f"'{e['game']}' is marked new but {game['id']} exists. Use \"is\": \"{game['id']}\".")
                ledger["games"].append(game)
            elif norm(e["game"]) not in names_of(game):
                game["aliases"].append(e["game"])
            if key and not game["providerKey"]:
                game["provider"], game["providerKey"] = e.get("provider"), key
            row = {"report": args.report, "list": lst["id"], "rank": e.get("rank"), "value": e.get("value"), "page": e.get("page", lst.get("page"))}
            if norm(e["game"]) != norm(game["name"]):
                row["as"] = e["game"]
            game["appearances"].append(row)
            if game["type"] == "slot":
                per_game.setdefault(game["id"], []).append(row)
            log.append({"list": lst["id"], "rank": e.get("rank"), "written": e["game"], "provider": e.get("provider"), "game": game["id"], "how": verdict})

    if asks:
        print(f"{len(asks)} name(s) could not be placed. In rankings.json give each entry \"is\": \"<game id>\" or \"new\": true:")
        for list_id, e, candidates in asks:
            options = ", ".join(f"{c['id']} ({c['name']}, {c['provider']})" for c in candidates)
            print(f"  [{list_id} #{e.get('rank')}] {e['game']} ({e.get('provider') or 'no provider'})  →  {options}")
        sys.exit(1)

    leaders = leaders_of(per_game, weights, args.top)
    new = sorted({r["game"] for r in log if r["how"] == "new"})
    for key in ("title", "publisher", "period", "published", "markets"):
        if rankings.get(key):
            header[key] = rankings[key]
    header.update({"status": "unified", "unified": now(), "leaders": leaders, "lists": len(rankings.get("lists", [])), "games": len({r["game"] for r in log}), "newGames": new})

    print(f"{args.report}: {len(log)} ranked names, {header['games']} games, {len(new)} new to the ledger.")
    if unknown_providers:
        print("Providers not in registry/providers.json (add their spellings, then unify again): " + ", ".join(sorted(unknown_providers)))
    print(f"Leaders (top {args.top} slot games):")
    for row in leaders:
        g = by_id(ledger, row["game"])
        print(f"  {row['position']:>2}. {g['name']} ({g['provider']})  {row['points']} points  art: {g['analysis']['art']['status']}")
    if args.dry_run:
        print("Dry run: nothing written.")
        return
    save(ledger)
    header_path.write_text(json.dumps(header, ensure_ascii=False, indent=1) + "\n")
    (folder / "unify.json").write_text(json.dumps(log, ensure_ascii=False, indent=1) + "\n")


# ── the queue and an analysis's state ────────────────────────────────────────


def queue(ledger):
    """Every report's leaders whose art analysis is not complete: each game once, by its best position."""
    best = {}
    for header in sorted(REPORTS.glob("*/report.json")):
        report = json.loads(header.read_text())
        for row in report.get("leaders", []):
            if row["game"] not in best or row["position"] < best[row["game"]]["position"]:
                best[row["game"]] = {"position": row["position"], "report": report["id"]}
    rows = []
    for game_id, where in best.items():
        g = by_id(ledger, game_id)
        status = g["analysis"]["art"]["status"]
        if status != "complete":
            rows.append({"game": game_id, "name": g["name"], "provider": g["provider"], "status": status, "demo": (g["demo"] or {}).get("url"), **where})
    return sorted(rows, key=lambda r: (r["position"], r["game"]))


def cmd_queue(args):
    rows = queue(load())
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return
    if not rows:
        print("Nothing waiting: every leader's art analysis is complete.")
    for r in rows:
        print(f"{r['position']:>2}  {r['game']:<44} {r['status']:<8} demo: {'yes' if r['demo'] else 'to find'}   ({r['report']})")


def cmd_start(args):
    ledger = load()
    g = by_id(ledger, args.game)
    if g["analysis"]["art"]["status"] == "complete":
        sys.exit(f"{args.game} is complete already ({g['analysis']['art'].get('report')}). A game is analysed once.")
    g["analysis"]["art"] = {"status": "running", "started": now(), "run": args.run}
    save(ledger)
    print(f"{args.game}: running.")


def cmd_block(args):
    ledger = load()
    g = by_id(ledger, args.game)
    g["analysis"]["art"] = {"status": "blocked", "reason": args.reason, "at": now(), "run": g["analysis"]["art"].get("run")}
    save(ledger)
    print(f"{args.game}: blocked. {args.reason}")


def digest_of(run_dir, out):
    """The part of an art run this repository keeps: what its pages are built from."""
    from PIL import Image

    run = json.loads((run_dir / "run.json").read_text())
    art = json.loads((run_dir / "art.json").read_text())
    manifest = json.loads((run_dir / "manifest.json").read_text())
    direction_path = run_dir / "analysis" / "game.json"
    if not direction_path.exists():
        sys.exit(f"{run_dir.name} has no analysis/game.json: the art is not read yet, so the run is not complete.")
    titles = {c["id"]: c["title"] for c in art["categories"]}
    units = {}
    for u in art["units"]:
        units[u["category"]] = units.get(u["category"], 0) + 1
    out.mkdir(parents=True, exist_ok=True)

    screens = []
    index = run_dir / "game-screens" / "index.json"
    if index.exists():
        every = json.loads(index.read_text())["screens"]
        chosen = []
        for stage in ("main", "base", "feature", "celebration", "intro", "trigger"):
            pick = next((s for s in every if s.get("stage") == stage and s not in chosen), None)
            if pick:
                chosen.append(pick)
        for s in chosen[:4]:
            src = run_dir / s["file"]
            if not src.exists() or src.stat().st_size < 1000:  # a Git LFS pointer, not the picture
                continue
            image = Image.open(src).convert("RGB")
            image.thumbnail((420, 420))
            name = f"{s['id']}.webp"
            image.save(out / name, "WEBP", quality=72)
            screens.append({"file": name, "width": image.width, "height": image.height, "stage": s.get("stage"), "screen": s.get("screen"), "caption": s.get("caption")})

    digest = {
        "run": run["id"],
        "game": run["game"],
        "started": run.get("started"),
        "reader": manifest.get("reader"),
        "counts": {k: len(manifest.get(k, [])) for k in ("textures", "components", "spines", "fonts")},
        "units": [{"id": c, "title": titles.get(c, c), "units": n} for c, n in units.items()],
        "measured": art["game"]["overall"],
        "byComponent": {titles.get(c, c): {k: v.get(k) for k in ("brightness", "saturation", "contrast", "warm", "cool", "palette")} for c, v in art["game"]["byCategory"].items()},
        "direction": json.loads(direction_path.read_text()),
        "screens": screens,
    }
    (out / "digest.json").write_text(json.dumps(digest, ensure_ascii=False, indent=1) + "\n")
    if (run_dir / "Art-report.md").exists():
        shutil.copyfile(run_dir / "Art-report.md", out / "Art-report.md")
    return digest


def cmd_complete(args):
    ledger = load()
    g = by_id(ledger, args.game)
    run_dir = Path(args.run)
    if not (run_dir / "run.json").exists():
        sys.exit(f"{run_dir} is not an art run folder (no run.json).")
    if not re.match(r"https://claude\.ai/(code/)?artifact/", args.report):
        sys.exit("--report is the published art report's address (https://claude.ai/artifact/…).")
    digest = digest_of(run_dir, ANALYSES / g["id"] / "art")
    if not digest["screens"]:
        print("No game screen was copied (none in the run, or Git LFS pointers: `git lfs pull` there first).")
    art = {"status": "complete", "run": digest["run"], "repo": "IntelligateStudios/Games-AI-art", "report": args.report, "completed": now()}
    for key in ("drive", "miro", "commit"):
        if getattr(args, key):
            art[key] = getattr(args, key)
    started = g["analysis"]["art"].get("started")
    if started:
        art["started"] = started
    g["analysis"]["art"] = art
    entry = {"kind": "art", "repo": art["repo"], "run": digest["run"]}
    add_existing(g, entry)
    save(ledger)
    print(f"{g['id']}: complete. analyses/{g['id']}/art/ holds its digest ({len(digest['screens'])} screens).")


def cmd_set(args):
    ledger = load()
    g = by_id(ledger, args.game)
    _, lookup = load_providers()
    for pair in args.pairs:
        key, _, value = pair.partition("=")
        if key == "alias+":
            if norm(value) not in names_of(g):
                g["aliases"].append(value)
        elif key == "demo":
            g["demo"] = {"url": clean_url(value), "from": "set by hand", "at": now()}
        elif key == "provider":
            g["provider"], g["providerKey"] = value, provider_key(value, lookup)[0]
        elif key in ("name", "type", "family", "notes"):
            g[key] = value
        else:
            sys.exit(f"Unknown key '{key}'. Keys: demo, name, provider, type, family, notes, alias+.")
    save(ledger)
    print(f"{g['id']}: set.")


def cmd_status(_):
    ledger = load()
    waiting = {r["game"]: r for r in queue(ledger)}
    counts = {}
    for g in sorted(ledger["games"], key=lambda g: (g["id"] not in waiting, g["id"])):
        status = g["analysis"]["art"]["status"]
        counts[status] = counts.get(status, 0) + 1
        reports = sorted({a["report"] for a in g["appearances"]})
        mark = f"leader #{waiting[g['id']]['position']}" if g["id"] in waiting else ""
        print(f"{g['id']:<46} {g['type']:<10} art: {status:<9} reports: {len(reports)}  existing: {','.join(sorted({e['kind'] for e in g['existing']})) or '-':<16} {mark}")
    print(f"\n{len(ledger['games'])} games. " + ", ".join(f"{n} {s}" for s, n in sorted(counts.items())) + f". {len(waiting)} waiting in the queue.")


def main():
    ap = argparse.ArgumentParser(description="The game ledger.")
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("seed")
    p.add_argument("--hq", default=str(ROOT.parent / "intelligate-ai"))
    p.add_argument("--art", default=str(ROOT.parent / "Games-AI-art"))
    p.set_defaults(func=cmd_seed)
    p = sub.add_parser("unify")
    p.add_argument("report")
    p.add_argument("--top", type=int, default=TOP)
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_unify)
    p = sub.add_parser("queue")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_queue)
    p = sub.add_parser("start")
    p.add_argument("game")
    p.add_argument("--run")
    p.set_defaults(func=cmd_start)
    p = sub.add_parser("block")
    p.add_argument("game")
    p.add_argument("--reason", required=True)
    p.set_defaults(func=cmd_block)
    p = sub.add_parser("complete")
    p.add_argument("game")
    p.add_argument("--run", required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--drive")
    p.add_argument("--miro")
    p.add_argument("--commit")
    p.set_defaults(func=cmd_complete)
    p = sub.add_parser("set")
    p.add_argument("game")
    p.add_argument("pairs", nargs="+")
    p.set_defaults(func=cmd_set)
    p = sub.add_parser("status")
    p.set_defaults(func=cmd_status)
    args = ap.parse_args()
    handler = args.func
    handler(args)


if __name__ == "__main__":
    main()
