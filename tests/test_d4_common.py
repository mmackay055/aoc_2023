from unittest import TestCase
from solutions.d4 import common


class D4CommonTest(TestCase):
    def test_parse_card_list(self):
        self.assertEqual([83, 86, 6, 31, 17, 9, 48, 53], common.parse_card_list('83 86  6 31 17  9 48 53'))
        self.assertEqual([3, 86, 6, 31, 17, 9, 48, 53], common.parse_card_list('3 86  6 31 17  9 48 53'))
        self.assertEqual([3, 86, 6, 31, 17, 9, 48, 3], common.parse_card_list('3 86  6 31 17  9 48 3'))

    def test_parse_card(self):
        self.assertEqual(([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]), common.parse_card('41 48 83 86 17 | 83 86  6 31 17  9 48 53'))

    def test_get_match_count(self):
        self.assertEqual(4, common.get_match_count([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]))
