from unittest import TestCase
from solutions.d6 import common


class D6P1Test(TestCase):
    def test_calc_wins(self):
        self.assertEqual([2, 3, 4, 5], common.calc_wins(7, 9))
        self.assertEqual(8, len(common.calc_wins(15, 40)))
        self.assertEqual(9, len(common.calc_wins(30, 200)))
