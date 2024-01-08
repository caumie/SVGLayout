from pathlib import Path
from unittest import TestCase

from src import SvgFileLoader


class TestUsage(TestCase):
    def setUp(self):
        self.current = Path(__file__).parent

    def test_init(self):
        s = SvgFileLoader(self.current / "example1_after.svg")
        print(s)
        print(s.tree)
        pass
