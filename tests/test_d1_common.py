from unittest import TestCase
from solutions.d2 import common


class D2CommonTest(TestCase):
    def test_parse_game(self):
        self.assertEqual(["3 blue, 4 red", "10 blue, 11 green, 5 red", "6 green, 7 blue"], common.parse_game("3 blue, 4 red; 10 blue, 11 green, 5 red; 6 green, 7 blue"))

    def test_pasrse_color(self):
        self.assertEqual(("blue", 3), common.parse_color("3 blue"))

    def test_parse_hand(self):
        self.assertEqual({"blue": 3, "red": 4, "green": 0}, common.parse_hand("3 blue, 4 red"))
        self.assertEqual({"blue": 0, "red": 7, "green": 6}, common.parse_hand("6 green, 7 red "))
        self.assertEqual({"blue": 3, "red": 0, "green": 6}, common.parse_hand("3 blue, 6 green"))
        self.assertEqual({"blue": 10, "red": 5, "green": 11}, common.parse_hand("10 blue, 11 green, 5 red"))
