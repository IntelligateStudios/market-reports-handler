#!/usr/bin/env python3
"""Build the summary report: one HTML file with every page inside it.

Reads:  registry/games.json; reports/*/report.json, rankings.json and unify.json; analyses/<game id>/art/
        (digest.json and the small screens); documents/art-report.md and documents/next-steps.md (the two
        written documents, when they exist).
Writes: site/index.html, self-contained (the pictures are inside it), and site/site.json (what it holds).

Pages, each at its own plain #address: summary, reports, report-<id>, games, game-<id>, art-report,
next-steps, method. Every figure on a page is either copied from a report (with its page), measured by
Games-AI-art from pixels, or a reading; the page says which.

Usage: python3 -I tools/build_site.py
"""
import base64
import datetime
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ledger as L  # noqa: E402

ROOT = L.ROOT
SITE = ROOT / "site"
DOCS = ROOT / "documents"
esc = html.escape

STATUS = {
    "complete": ("Analysed", "good"),
    "running": ("Running", "warn"),
    "blocked": ("Blocked", "bad"),
    "found": ("Run found", "warn"),
    "none": ("Not analysed", "idle"),
}
DIRECTION = ["style", "rendering", "colour", "lighting", "ambience", "shapes", "materials", "typography", "motion", "variants", "construction", "consistency"]
MEASURES = [("brightness", "Brightness"), ("saturation", "Saturation"), ("contrast", "Contrast"), ("warm", "Warm share"), ("cool", "Cool share"), ("softEdge", "Soft edges")]


def day(stamp):
    if not stamp:
        return ""
    d = datetime.date.fromisoformat(stamp[:10])
    return f"{d.day} {d.strftime('%b %Y')}"


def link(href, text, cls=""):
    out = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{esc(href)}"{out}{c}>{text}</a>'


def pill(status):
    label, tone = STATUS.get(status, (status, "idle"))
    return f'<span class="pill {tone}">{label}</span>'


def kv(rows):
    body = "".join(f"<tr><th scope=\"row\">{k}</th><td>{v}</td></tr>" for k, v in rows if v)
    return f'<div class="scroll"><table class="kv">{body}</table></div>'


def table(head, rows, cls=""):
    h = "".join(f"<th scope=\"col\">{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="scroll"><table class="grid {cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


# ── a small Markdown reader, for the two written documents ───────────────────


def inline(text):
    text = esc(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<em>\1</em>", text)
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: link(m.group(2), m.group(1)), text)


def markdown(text):
    out, lines, i = [], text.splitlines(), 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif m := re.match(r"(#{1,4})\s+(.*)", line):
            level = min(len(m.group(1)) + 1, 5)  # the page's own title is the h1 and h2
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
        elif line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            cells = lambda row: [c.strip() for c in row.strip().strip("|").split("|")]
            head, rows = cells(line), []
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([inline(c) for c in cells(lines[i])])
                i += 1
            out.append(table([inline(c) for c in head], rows))
        elif m := re.match(r"\s*([-*]|\d+\.)\s+", line):
            tag = "ol" if m.group(1)[0].isdigit() else "ul"
            items = []
            while i < len(lines) and (n := re.match(r"\s*([-*]|\d+\.)\s+(.*)", lines[i])):
                items.append(n.group(2))
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() and not re.match(r"\s*([-*]|\d+\.)\s+", lines[i]):
                    items[-1] += " " + lines[i].strip()
                    i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
        elif line.startswith(">"):
            out.append(f"<blockquote>{inline(line.lstrip('> '))}</blockquote>")
            i += 1
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"(#{1,4}\s|\s*([-*]|\d+\.)\s+|\s*\||>)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


# ── what the pages are made from ─────────────────────────────────────────────


def gather():
    ledger = L.load()
    games = {g["id"]: g for g in ledger["games"]}
    reports = []
    for header in sorted(L.REPORTS.glob("*/report.json"), reverse=True):
        r = json.loads(header.read_text())
        rk = header.parent / "rankings.json"
        r["rankings"] = json.loads(rk.read_text()) if rk.exists() else None
        un = header.parent / "unify.json"
        r["log"] = json.loads(un.read_text()) if un.exists() else []
        reports.append(r)
    digests = {}
    for path in sorted(L.ANALYSES.glob("*/art/digest.json")):
        d = json.loads(path.read_text())
        for s in d["screens"]:
            s["data"] = "data:image/webp;base64," + base64.b64encode((path.parent / s["file"]).read_bytes()).decode()
        digests[path.parent.parent.name] = d
    leaders = {}  # game id → its best position in any report, and the reports that rank it a leader
    for r in reports:
        for row in r.get("leaders", []):
            cur = leaders.setdefault(row["game"], {"position": row["position"], "reports": []})
            cur["position"] = min(cur["position"], row["position"])
            cur["reports"].append((r["id"], row["position"]))
    return ledger, games, reports, digests, leaders


def game_link(g):
    return link(f"#game-{g['id']}", esc(g["name"]))


def report_title(r):
    return esc(r.get("title") or r["file"])


def art_links(g):
    art = g["analysis"]["art"]
    out = []
    if art.get("report"):
        out.append(link(art["report"], "Art report", "ext"))
    if art.get("drive"):
        out.append(link(art["drive"], "Drive", "ext"))
    if art.get("miro"):
        out.append(link(art["miro"], "Miro", "ext"))
    return " ".join(out)


def palette_strip(palette, labels=True):
    total = sum(p["share"] for p in palette) or 1
    bars = "".join(
        f'<span style="flex:{p["share"] / total:.4f} 1 0;background:{esc(p["hex"])}" title="{esc(p["name"])} {esc(p["hex"])}, {p["share"] * 100:.1f}% of the art"></span>'
        for p in palette
    )
    out = f'<div class="strip" role="img" aria-label="Measured palette: {esc(", ".join(p["name"] for p in palette))}">{bars}</div>'
    if labels:
        out += '<ul class="swatches">' + "".join(
            f'<li><i style="background:{esc(p["hex"])}"></i><code>{esc(p["hex"])}</code> {esc(p["name"])} <span class="num">{p["share"] * 100:.1f}%</span></li>' for p in palette
        ) + "</ul>"
    return out


def meter(value):
    if value is None:
        return ""
    return f'<span class="meter"><span style="width:{max(0, min(1, value)) * 100:.0f}%"></span></span><span class="num">{value:.2f}</span>'


# ── pages ────────────────────────────────────────────────────────────────────


def page_summary(ledger, games, reports, digests, leaders):
    done = [g for g in leaders if games[g]["analysis"]["art"]["status"] == "complete"]
    analysed_all = [g for g in games.values() if g["analysis"]["art"]["status"] == "complete"]
    facts = [
        (len(reports), "market reports taken"),
        (len(games), "games on record"),
        (len(leaders), "leading slot games"),
        (f"{len(done)} of {len(leaders)}" if leaders else len(analysed_all), "leaders with an art analysis" if leaders else "games with an art analysis"),
    ]
    out = ['<p class="lede">Which slot games lead the market reports the studio receives, and what their art is made of. Each game is analysed once, however many reports name it.</p>']
    out.append('<dl class="facts">' + "".join(f"<div><dt>{label}</dt><dd>{n}</dd></div>" for n, label in facts) + "</dl>")
    if leaders:
        rows = []
        for gid, info in sorted(leaders.items(), key=lambda kv: (kv[1]["position"], kv[0])):
            g = games[gid]
            named = sorted({a["report"] for a in g["appearances"]})
            rows.append([f'<span class="num">{info["position"]}</span>', game_link(g), esc(g["provider"] or ""), " ".join(link(f"#report-{r}", f"#{p}", "chip") for r, p in info["reports"]) + (f' <span class="muted">in {len(named)} reports</span>' if len(named) > 1 else ""), pill(g["analysis"]["art"]["status"]), art_links(g) or '<span class="muted">—</span>'])
        out.append("<h3>The leading games</h3>")
        out.append('<p class="note">Position is the game\'s best place among any report\'s 20 leaders. A report\'s own order is on its page.</p>')
        out.append(table(["Best", "Game", "Provider", "Leader in", "Art analysis", "Open"], rows, "summary"))
    else:
        out.append('<div class="empty"><strong>No market report has been taken yet.</strong> When a PDF arrives its ranked games are read, joined to the games below, and the 20 leading slot games that have no art analysis are analysed.</div>')
    others = [g for g in games.values() if g["id"] not in leaders and (g["existing"] or g["analysis"]["art"]["status"] != "none")]
    if others:
        rows = []
        for g in sorted(others, key=lambda g: (g["analysis"]["art"]["status"] != "complete", g["name"])):
            kinds = sorted({e["kind"] for e in g["existing"]})
            words = {"gdd": "PRD and GDD in Intelligate HQ", "research": "Our web research, 21 Nov 2026", "art": "Art run"}
            rows.append([game_link(g), esc(g["provider"] or ""), esc(g["type"]), "; ".join(words[k] for k in kinds), pill(g["analysis"]["art"]["status"]), art_links(g) or '<span class="muted">—</span>'])
        out.append("<h3>Already on the studio's record</h3>")
        out.append('<p class="note">Games known before any report named them. A report that ranks one of them finds it here and does not analyse it a second time.</p>')
        out.append(table(["Game", "Provider", "Type", "On record as", "Art analysis", "Open"], rows))
    return "Summary", "".join(out)


def page_reports(reports, games):
    if not reports:
        return "Reports", '<div class="empty"><strong>No report yet.</strong> Each PDF gets a page here: what it is, its lists as it prints them, and its 20 leading slot games.</div>'
    rows = [[link(f"#report-{r['id']}", report_title(r)), esc(r.get("publisher", "")), esc(r.get("period", "")), day(r["received"]), f'<span class="num">{r.get("games", "")}</span>', f'<span class="num">{len(r.get("newGames", []))}</span>', esc(r["status"])] for r in reports]
    return "Reports", table(["Report", "Publisher", "Period", "Received", "Games", "New to the record", "State"], rows)


def page_report(r, games):
    out = [kv([("File", f'<code>{esc(r["file"])}</code>, {r["pages"]} pages'), ("Publisher", esc(r.get("publisher", ""))), ("Period", esc(r.get("period", ""))), ("Markets", esc(", ".join(r.get("markets", [])) if isinstance(r.get("markets"), list) else r.get("markets", ""))), ("Received", day(r["received"])), ("In the repository", f'<code>reports/{esc(r["id"])}/</code>'), ("Notes", esc((r.get("rankings") or {}).get("notes", "")))])]
    if r.get("leaders"):
        rows = []
        for row in r["leaders"]:
            g = games[row["game"]]
            rows.append([f'<span class="num">{row["position"]}</span>', game_link(g), esc(g["provider"] or ""), f'<span class="num">{row["points"]:g}</span>', f'#{row["best"]["rank"]} in {esc(row["best"]["list"])}', "New" if g["id"] in r.get("newGames", []) else "Known", pill(g["analysis"]["art"]["status"])])
        out.append("<h3>Its 20 leading slot games</h3>")
        out.append('<p class="note">Order by the handler\'s rule (Method): 21 − rank points for each list a game is ranked in, summed. It is our way of joining the report\'s lists, not a figure of the report.</p>')
        out.append(table(["Position", "Game", "Provider", "Points", "Best rank", "Record", "Art analysis"], rows))
    taken = {(e["list"], e["rank"], e["written"]): e["game"] for e in r.get("log", [])}
    for lst in (r.get("rankings") or {}).get("lists", []):
        out.append(f"<h3>{esc(lst['title'])}</h3>")
        meta = " · ".join(x for x in [esc(lst.get("metric", "")), esc(lst.get("market", "")), f"page {lst['page']}" if lst.get("page") else ""] if x)
        if meta:
            out.append(f'<p class="note">As the report prints it. {meta}</p>')
        rows = []
        for e in lst["entries"]:
            gid = taken.get((lst["id"], e.get("rank"), e["game"]))
            rows.append([f'<span class="num">{e.get("rank") or ""}</span>', esc(e["game"]), esc(e.get("provider") or ""), esc(str(e.get("value") or "")), game_link(games[gid]) if gid in games else ""])
        out.append(table(["Rank", "Game as written", "Provider", "Value as stated", "On our record as"], rows))
    return report_title(r), "".join(out)


def page_games(games, leaders):
    rows = []
    for g in sorted(games.values(), key=lambda g: (leaders.get(g["id"], {}).get("position", 999), g["name"])):
        reports = sorted({a["report"] for a in g["appearances"]})
        rows.append([game_link(g), esc(g["provider"] or ""), esc(g["type"]), f'<span class="num">{leaders[g["id"]]["position"]}</span>' if g["id"] in leaders else "", f'<span class="num">{len(reports)}</span>', pill(g["analysis"]["art"]["status"]), art_links(g)])
    control = '<label class="filter" for="game-filter">Find a game or provider <input id="game-filter" type="search" autocomplete="off"></label>'
    return "Games", control + table(["Game", "Provider", "Type", "Best position", "Reports", "Art analysis", "Open"], rows, "filterable")


def page_game(g, digests, reports):
    art = g["analysis"]["art"]
    titles = {r["id"]: report_title(r) for r in reports}
    existing = []
    for e in g["existing"]:
        where = {"gdd": "PRD and GDD run", "research": "Web research run", "art": "Art run"}[e["kind"]]
        existing.append(f'{where} <code>{esc(e["run"])}</code> in {esc(e["repo"])}' + (f' (as "{esc(e["as"])}")' if e.get("as") else ""))
    demo = (g.get("demo") or {}).get("url")
    out = [kv([("Provider", esc(g["provider"] or "")), ("Type", esc(g["type"])), ("Also written", esc(", ".join(g.get("aliases", [])))), ("Ledger id", f'<code>{esc(g["id"])}</code>'), ("Demo", link(demo, "The provider's free-play demo", "ext") if demo else ""), ("On record", "<br>".join(existing)), ("Notes", esc(g.get("notes", "")))])]
    out.append("<h3>In the market reports</h3>")
    if g["appearances"]:
        rows = [[link(f"#report-{a['report']}", titles.get(a["report"], esc(a["report"]))), esc(a["list"]), f'<span class="num">{a.get("rank") or ""}</span>', esc(str(a.get("value") or "")), esc(a.get("as", "")), f'{a["page"]}' if a.get("page") else ""] for a in g["appearances"]]
        out.append(table(["Report", "List", "Rank", "Value as stated", "Written as", "Page"], rows))
    else:
        out.append('<p class="note">No report taken so far names this game.</p>')
    out.append(f"<h3>Art analysis {pill(art['status'])}</h3>")
    d = digests.get(g["id"])
    if art["status"] == "complete" and d:
        out.append(kv([("Full art report", link(art["report"], esc(art["report"]), "ext")), ("Google Drive", link(art["drive"], "The run's folder", "ext") if art.get("drive") else ""), ("Miro", link(art["miro"], "The run's board", "ext") if art.get("miro") else ""), ("Run", f'<code>{esc(art["run"])}</code> in {esc(art["repo"])}'), ("Completed", day(art.get("completed"))), ("Extracted", f'{d["counts"]["components"]:,} named sprites on {d["counts"]["textures"]:,} textures, {d["counts"]["spines"]} skeletons, {d["counts"]["fonts"]} fonts'), ("Kept here", f'<code>analyses/{esc(g["id"])}/art/</code>')]))
        out.append(f'<p class="lead">{esc(d["direction"].get("summary", ""))}</p>')
        if d["screens"]:
            out.append('<div class="screens">' + "".join(f'<figure><img src="{s["data"]}" width="{s["width"]}" height="{s["height"]}" alt="{esc(s.get("caption") or s.get("screen") or "")}" loading="lazy"><figcaption>{esc(s.get("screen") or s.get("stage") or "")}</figcaption></figure>' for s in d["screens"]) + "</div>")
        out.append('<h4>Palette <span class="tag">Measured</span></h4>' + palette_strip(d["measured"]["palette"]))
        out.append('<h4>Tone <span class="tag">Measured</span></h4>' + kv([(label, meter(d["measured"].get(key))) for key, label in MEASURES] + [("In words", esc(", ".join(d["measured"].get("words", []))))]))
        out.append('<h4>Art components</h4>' + table(["Component", "Units"], [[esc(u["title"]), f'<span class="num">{u["units"]}</span>'] for u in sorted(d["units"], key=lambda u: -u["units"])]))
        out.append('<h4>Art direction <span class="tag read">Read</span></h4>' + kv([(f.capitalize(), esc(d["direction"].get(f, ""))) for f in DIRECTION]))
        if d["direction"].get("takeaways"):
            out.append('<h4>What to take from it <span class="tag read">Read</span></h4><ul>' + "".join(f"<li>{esc(t)}</li>" for t in d["direction"]["takeaways"]) + "</ul>")
    elif art["status"] == "blocked":
        out.append(f'<p>{esc(art.get("reason", ""))}</p>')
    elif art["status"] == "running":
        out.append(f'<p>Started {day(art.get("started"))}.</p>')
    else:
        out.append('<p class="note">Not analysed. It is analysed when a report ranks it among its 20 leading slot games.</p>')
    return g["name"], "".join(out)


def page_art_report(games, digests, leaders):
    wanted = sorted(leaders, key=lambda g: leaders[g]["position"])
    have = [g for g in (wanted or sorted(digests)) if g in digests] + [g for g in sorted(digests) if wanted and g not in wanted]
    out = []
    if wanted:
        missing = [games[g]["name"] for g in wanted if g not in digests]
        out.append(f'<p class="lede">The art of the market\'s leading slot games, side by side. {len(wanted) - len(missing)} of {len(wanted)} leaders are analysed.</p>')
        if missing:
            status = lambda g: ((games[g].get("analysis") or {}).get("art") or {}).get("status")
            blocked = [games[g]["name"] for g in wanted if g not in digests and status(g) == "blocked"]
            waiting = [n for n in missing if n not in blocked]
            if waiting:
                out.append(f'<p class="note">Still to analyse: {esc(", ".join(waiting))}.</p>')
            if blocked:
                out.append(f'<p class="note">Blocked, each with its reason on its own page: {esc(", ".join(blocked))}. The comparison below covers only the analysed games and is not a view of the whole market.</p>')
    else:
        out.append(f'<p class="lede">The art of the games analysed so far, side by side. No report has named its leaders yet, so this is {len(have)} game{"s" if len(have) != 1 else ""}, not the market.</p>')
    written = DOCS / "art-report.md"
    if written.exists():
        out.append('<div class="doc">' + markdown(written.read_text()) + "</div>")
    if not have:
        return "Art of the leaders", "".join(out)
    out.append('<h3>Palettes <span class="tag">Measured</span></h3><div class="palettes">')
    for gid in have:
        out.append(f'<div><div class="pal-name">{game_link(games[gid])}</div>{palette_strip(digests[gid]["measured"]["palette"], labels=False)}</div>')
    out.append("</div>")
    rows = [[game_link(games[g])] + [meter(digests[g]["measured"].get(k)) for k, _ in MEASURES] for g in have]
    out.append('<h3>Tone <span class="tag">Measured</span></h3>' + table(["Game"] + [label for _, label in MEASURES], rows, "tone"))
    rows = [[game_link(games[g]), *(f'<span class="num">{digests[g]["counts"][k]:,}</span>' for k in ("components", "textures", "spines", "fonts"))] for g in have]
    out.append('<h3>Size of the art package <span class="tag">Measured</span></h3>' + table(["Game", "Named sprites", "Textures", "Skeletons", "Fonts"], rows))
    out.append('<h3>Art direction, game by game <span class="tag read">Read</span></h3>')
    for field in DIRECTION:
        rows = [[game_link(games[g]), esc(digests[g]["direction"].get(field, ""))] for g in have]
        out.append(f'<details data-key="dir-{field}"{" open" if field == "style" else ""}><summary>{field.capitalize()}</summary>' + table(["Game", field.capitalize()], rows, "read") + "</details>")
    out.append('<h3>The full reports</h3>' + table(["Game", "Art report", "Files"], [[game_link(games[g]), link(games[g]["analysis"]["art"]["report"], esc(games[g]["analysis"]["art"]["report"]), "ext"), art_links(games[g])] for g in have]))
    return "Art of the leaders", "".join(out)


def page_next_steps(games, digests, leaders):
    written = DOCS / "next-steps.md"
    if written.exists():
        return "Next steps in art", '<div class="doc">' + markdown(written.read_text()) + "</div>"
    done = len([g for g in leaders if g in digests])
    state = f"{done} of {len(leaders)} leaders are analysed." if leaders else "No report has named its leaders yet."
    return "Next steps in art", f'<div class="empty"><strong>Not written yet.</strong> The recommendation for Intelligate\'s next steps in art is written from the finished analyses of all the leading games, so that it rests on the whole set. {state}</div>'


def page_method():
    return "Method", markdown((ROOT / "documents" / "method.md").read_text())


CSS = (Path(__file__).resolve().parent / "site.css")
JS = (Path(__file__).resolve().parent / "site.js")


def main():
    ledger, games, reports, digests, leaders = gather()
    pages = [("summary", *page_summary(ledger, games, reports, digests, leaders), "nav"), ("reports", *page_reports(reports, games), "nav")]
    for r in reports:
        pages.append((f"report-{r['id']}", *page_report(r, games), "reports"))
    pages.append(("games", *page_games(games, leaders), "nav"))
    for g in sorted(games.values(), key=lambda g: g["name"]):
        pages.append((f"game-{g['id']}", *page_game(g, digests, reports), "games"))
    pages += [("art-report", *page_art_report(games, digests, leaders), "nav"), ("next-steps", *page_next_steps(games, digests, leaders), "nav"), ("method", *page_method(), "nav")]

    built = datetime.datetime.now(datetime.timezone.utc)
    nav = "".join(f'<a href="#{pid}" data-nav="{pid}">{esc(title)}</a>' for pid, title, _, parent in pages if parent == "nav")
    sections = []
    for pid, title, body, parent in pages:
        crumb = "" if parent == "nav" else f'<a class="crumb" href="#{parent}">← {parent.capitalize()}</a>'
        sections.append(f'<section data-page="{pid}" data-parent="{parent}" hidden>{crumb}<h2>{esc(title)}</h2>{body}</section>')
    doc = f"""<title>Slot Market Art Ledger</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
{CSS.read_text()}</style>
<div class="shell">
<header class="side">
<h1><a href="#summary">Slot Market <br>Art Ledger</a></h1>
<nav aria-label="Pages">{nav}</nav>
<p class="built">Intelligate Studios, internal.<br>Built {built.day} {built.strftime('%b %Y, %H:%M')} UTC.</p>
</header>
<main id="main">
{''.join(sections)}
</main>
</div>
<script>
{JS.read_text()}</script>
"""
    SITE.mkdir(exist_ok=True)
    (SITE / "index.html").write_text(doc)
    info = {"built": built.strftime("%Y-%m-%dT%H:%M:%SZ"), "pages": len(pages), "reports": len(reports), "games": len(games), "leaders": len(leaders), "analysed": len(digests), "bytes": len(doc.encode())}
    (SITE / "site.json").write_text(json.dumps(info, indent=1) + "\n")
    print(f"site/index.html: {info['pages']} pages, {info['bytes'] / 1024:.0f} KB. {info['reports']} reports, {info['games']} games, {info['analysed']} analysed.")


if __name__ == "__main__":
    main()
