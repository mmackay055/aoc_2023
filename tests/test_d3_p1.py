from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d3 import p1
from solutions.d3.common import Item


class D3P1Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 3
        self.puzzle = 1
        self.solver = SolutionRunner(self.day, p1)

    def test_puzzle(self):
        # latest solution wrong solution is 330744
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_parse_items(self):
        self.assertEqual([Item('467', 0, 0, 2), Item('*', 0, 3, 3), Item('114', 0, 5, 7), Item('123', 0, 10, 12)], p1.parse_items("467*.114..123", 0))
        self.assertEqual([Item('@', 0, 1, 1), Item('-', 0, 4, 4), Item('/', 0, 7, 7), Item('=', 0, 9, 9)], p1.parse_items(".@..-../.=", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7)], p1.parse_items("467..114..", 0))
        self.assertEqual([Item('67', 0, 1, 2), Item('114', 0, 5, 7)], p1.parse_items(".67..114..", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('123', 0, 10, 12)], p1.parse_items("467..114..123", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('*', 0, 8, 8), Item('123', 0, 10, 12)], p1.parse_items("467..114*.123", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('123', 0, 10, 12), Item('*', 0, 13, 13)], p1.parse_items("467..114..123*", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('-', 0, 9, 9), Item('123', 0, 10, 12), Item('*', 0, 13, 13)], p1.parse_items("467..114.-123*", 0))
        self.assertEqual([Item('67', 0, 1, 2), Item('*', 0, 3, 3), Item('114', 0, 5, 7), Item('-', 0, 9, 9)], p1.parse_items(".67*.114.-", 0))
        self.assertEqual([Item('6', 0, 1, 1), Item('*', 0, 3, 3), Item('1', 0, 5, 5), Item('4', 0, 7, 7), Item('-', 0, 9, 9)], p1.parse_items(".6.*.1.4.-", 0))

    def test_is_engnum_diff_line(self):
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 3, 3), 4))
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 2, 2), 3))
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 1, 1), 3))
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 0, 0), 3))
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 3, 3), 3))
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 4, 4), 5))
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 4, 6), Item('*', 1, 3, 3), 4))
        self.assertTrue(p1.is_engnum_diff_line(Item('12', 0, 3, 4), Item('*', 1, 3, 3), 4))
        self.assertTrue(p1.is_engnum_diff_line(Item('123', 0, 2, 4), Item('*', 1, 3, 3), 4))
        self.assertFalse(p1.is_engnum_diff_line(Item('12', 0, 5, 6), Item('*', 1, 3, 3), 6))
        self.assertFalse(p1.is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 5, 5), 6))

    def test_is_engnum_same_line(self):
        self.assertTrue(p1.is_engnum_same_line(Item('123', 0, 1, 3), Item('*', 0, 4, 4)))
        self.assertTrue(p1.is_engnum_same_line(Item('222', 0, 4, 6), Item('#', 0, 3, 3)))
        self.assertFalse(p1.is_engnum_same_line(Item('123', 0, 4, 6), Item('*', 0, 2, 2)))
        self.assertFalse(p1.is_engnum_same_line(Item('123', 0, 1, 3), Item('*', 0, 5, 5)))

    def test_eng_num_same_lines(self):
        self.assertEqual([Item('123', 0, 1, 3), Item('123', 0, 5, 7)], p1.find_eng_num_same_line([Item('123', 0, 1, 3), Item('*', 0, 4, 4), Item('123', 0, 5, 7), Item('123', 0, 8, 9)]))
        self.assertEqual([], p1.find_eng_num_same_line([Item('123', 0, 1, 1), Item('123', 0, 3, 4), Item('123', 0, 5, 7), Item('123', 0, 8, 9)]))
        self.assertEqual([Item('123', 0, 4, 4)], p1.find_eng_num_same_line([Item('123', 0, 1, 3), Item('123', 0, 4, 4), Item('*', 0, 5, 5), Item('123', 0, 8, 9)]))
        self.assertEqual([Item('123', 0, 5, 7)], p1.find_eng_num_same_line([Item('123', 0, 1, 3), Item('123', 0, 4, 4), Item('123', 0, 5, 7), Item('*', 0, 8, 9)]))

    def test_eng_num_diff_line(self):
        self.assertEqual([Item('123', 0, 1, 3), Item('123', 0, 4, 5), Item('123', 0, 8, 8)],
                         p1.find_eng_num_diff_line([Item('123', 0, 1, 3), Item('123', 0, 4, 5), Item('123', 0, 6, 6), Item('123', 0, 8, 8)],
                                                   [Item('123', 0, 1, 1), Item('*', 0, 4, 4), Item('123', 0, 5, 5), Item('*', 0, 8, 8)], 9))

    def test_process_line(self):
        self.assertEqual(([('0:0:2', 467)], [Item('*', 1, 3, 3)]), p1.process_line('...*......', 1, '467..114..', [Item('467', 0, 0, 2), Item('114', 0, 5, 7)]))
        self.assertEqual(([('2:2:3', 35)], [Item('35', 2, 2, 3), Item('633', 2, 6, 8)]), p1.process_line('..35..633.', 2, '...*......', [Item('*', 0, 3, 3)]))
