from unittest import TestCase
from solutions.d6 import common


class D6P1Test(TestCase):
    def test_calc_wins(self):
        r = common.calc_win_range(7, 9)
        self.assertEqual((2, 5), r)
        self.assertEqual(4, common.calc_range_len(r))

        r = common.calc_win_range(15, 40)
        self.assertEqual((4, 11), r)
        self.assertEqual(8, common.calc_range_len(r))

        r = common.calc_win_range(30, 200)
        self.assertEqual((11, 19), r)
        self.assertEqual(9, common.calc_range_len(r))
