from unittest import TestCase
from solutions import common


class CommonTest(TestCase):
    def test_parse_game_id(self):
        self.assertEqual((1, "3 blue, 4 red; 6 green, 7 blue"), common.parse_line_id("Game 1: 3 blue, 4 red; 6 green, 7 blue "))
        self.assertEqual((2, "13 32 20 16 61 | 61 30 68 82 17 32 24 19"), common.parse_line_id("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"))
