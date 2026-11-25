"""Tests of the ledger's matching, the leaders rule, unify and the site's Markdown reader.

Run: python3 -I -m unittest discover tests   (from the repository's root)
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import build_site  # noqa: E402
import ledger as L  # noqa: E402


class Names(unittest.TestCase):
    def test_spellings_compare_equal(self):
        self.assertEqual(L.norm("Gates of Olympus™"), L.norm("GATES OF OLYMPUS"))
        self.assertEqual(L.norm("Huff N’ Puff"), L.norm("Huff N' Puff"))
        self.assertEqual(L.norm("Rich Wilde & the Book of Dead"), L.norm("Rich Wilde and the Book of Dead"))
        self.assertEqual(L.norm("Sweet Bonanza Slot"), L.norm("Sweet Bonanza"))

    def test_a_version_is_another_game(self):
        self.assertNotEqual(L.norm("Gates of Olympus 1000"), L.norm("Gates of Olympus"))

    def test_provider_spellings(self):
        _, lookup = L.load_providers()
        self.assertEqual(L.provider_key("Pragmatic Play", lookup), ("pragmatic", True))
        self.assertEqual(L.provider_key("Light and Wonder", lookup), ("lnw", True))
        self.assertEqual(L.provider_key("Nobody Games", lookup), ("nobodygames", False))


class Placing(unittest.TestCase):
    def setUp(self):
        self.ledger = {"games": [L.new_game("Gates of Olympus", "Pragmatic Play", "pragmatic"), L.new_game("Plinko", "Stake Originals", "stake")]}

    def test_same_title_same_provider(self):
        self.assertEqual(L.place(self.ledger, "GATES OF OLYMPUS™", "pragmatic")[0], "match")

    def test_no_provider_and_one_title(self):
        self.assertEqual(L.place(self.ledger, "Gates of Olympus", None)[0], "match")

    def test_version_is_asked_not_merged(self):
        self.assertEqual(L.place(self.ledger, "Gates of Olympus 1000", "pragmatic")[0], "ask")

    def test_same_title_other_provider_is_asked(self):
        self.assertEqual(L.place(self.ledger, "Plinko", "spribe")[0], "ask")

    def test_unknown_is_new(self):
        self.assertEqual(L.place(self.ledger, "Book of Dead", "playngo")[0], "new")


class Leaders(unittest.TestCase):
    def test_one_list_keeps_its_order(self):
        rows = {f"g{i}": [{"list": "a", "rank": i}] for i in range(1, 31)}
        order = L.leaders_of(rows, {"a": 1}, 20)
        self.assertEqual([r["game"] for r in order], [f"g{i}" for i in range(1, 21)])

    def test_lists_sum_and_ties_break_on_best_rank(self):
        rows = {"both": [{"list": "a", "rank": 3}, {"list": "b", "rank": 3}], "top": [{"list": "a", "rank": 1}], "tie": [{"list": "b", "rank": 1}], "unranked": [{"list": "a", "rank": None}]}
        order = L.leaders_of(rows, {"a": 1, "b": 1}, 20)
        self.assertEqual([r["game"] for r in order], ["both", "tie", "top"])
        self.assertEqual(order[0]["points"], 36)


class Unify(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.old = (L.REGISTRY, L.REPORTS)
        L.REGISTRY, L.REPORTS = root / "registry" / "games.json", root / "reports"
        folder = L.REPORTS / "2026-01-01-test"
        folder.mkdir(parents=True)
        (folder / "report.json").write_text(json.dumps({"id": "2026-01-01-test", "file": "t.pdf", "pages": 1, "received": "2026-01-01", "status": "taken"}))
        self.rankings = folder / "rankings.json"
        ledger = {"version": 1, "games": [L.new_game("Sweet Bonanza", "Pragmatic Play", "pragmatic")]}
        ledger["games"][0]["analysis"]["art"] = {"status": "complete", "report": "https://claude.ai/artifact/x"}
        L.save(ledger)

    def tearDown(self):
        L.REGISTRY, L.REPORTS = self.old
        self.tmp.cleanup()

    def write(self, entries):
        self.rankings.write_text(json.dumps({"title": "Test", "lists": [{"id": "top", "title": "Top", "entries": entries}]}))

    def unify(self):
        L.cmd_unify(SimpleNamespace(report="2026-01-01-test", top=20, dry_run=False))

    def test_known_game_is_found_and_not_queued_again(self):
        self.write([{"rank": 1, "game": "SWEET BONANZA", "provider": "Pragmatic"}, {"rank": 2, "game": "Book of Dead", "provider": "Play'n GO"}, {"rank": 3, "game": "Aviator", "provider": "Spribe", "type": "crash"}])
        self.unify()
        self.unify()  # a second time changes nothing
        ledger = L.load()
        self.assertEqual(len(ledger["games"]), 3)
        sweet = L.by_id(ledger, "pragmatic-sweet-bonanza")
        self.assertEqual(len(sweet["appearances"]), 1)
        header = json.loads((L.REPORTS / "2026-01-01-test" / "report.json").read_text())
        self.assertEqual([r["game"] for r in header["leaders"]], ["pragmatic-sweet-bonanza", "playngo-book-of-dead"])
        self.assertEqual([r["game"] for r in L.queue(ledger)], ["playngo-book-of-dead"])

    def test_a_doubtful_name_stops_and_writes_nothing(self):
        self.write([{"rank": 1, "game": "Sweet Bonanza 1000", "provider": "Pragmatic Play"}])
        with self.assertRaises(SystemExit):
            self.unify()
        self.assertEqual(len(L.load()["games"]), 1)
        self.write([{"rank": 1, "game": "Sweet Bonanza 1000", "provider": "Pragmatic Play", "new": True}])
        self.unify()
        self.assertEqual(len(L.load()["games"]), 2)

    def test_a_session_key_is_refused(self):
        with self.assertRaises(SystemExit):
            L.clean_url("https://demo.example/openGame.do?gameSymbol=x&mgckey=AUTHTOKEN@abc")


class Markdown(unittest.TestCase):
    def test_table_list_and_escape(self):
        out = build_site.markdown("# T\n\nA **b** <script>.\n\n| a | b |\n| --- | --- |\n| 1 | [x](https://e.x) |\n\n- one\n- two\n")
        self.assertIn("<h2>T</h2>", out)
        self.assertIn("&lt;script&gt;", out)
        self.assertIn('<a href="https://e.x" target="_blank" rel="noopener">x</a>', out)
        self.assertIn("<li>two</li>", out)


if __name__ == "__main__":
    unittest.main()
