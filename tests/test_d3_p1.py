from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d3 import p1


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
        self.assertEqual([(False, 0, 2), (True, 3, 3), (False, 5, 7), (False, 10, 12)], p1.parse_items("467*.114..123"))
        self.assertEqual([(True, 1, 1), (True, 4, 4), (True, 7, 7), (True, 9, 9)], p1.parse_items(".@..-../.="))
        self.assertEqual([(False, 0, 2), (False, 5, 7)], p1.parse_items("467..114.."))
        self.assertEqual([(False, 1, 2), (False, 5, 7)], p1.parse_items(".67..114.."))
        self.assertEqual([(False, 0, 2), (False, 5, 7), (False, 10, 12)], p1.parse_items("467..114..123"))
        self.assertEqual([(False, 0, 2), (False, 5, 7), (True, 8, 8), (False, 10, 12)], p1.parse_items("467..114*.123"))
        self.assertEqual([(False, 0, 2), (False, 5, 7), (False, 10, 12), (True, 13, 13)], p1.parse_items("467..114..123*"))
        self.assertEqual([(False, 0, 2), (False, 5, 7), (True, 9, 9), (False, 10, 12), (True, 13, 13)], p1.parse_items("467..114.-123*"))
        self.assertEqual([(False, 1, 2), (True, 3, 3), (False, 5, 7), (True, 9, 9)], p1.parse_items(".67*.114.-"))
        self.assertEqual([(False, 1, 1), (True, 3, 3), (False, 5, 5), (False, 7, 7), (True, 9, 9)], p1.parse_items(".6.*.1.4.-"))

    def test_is_engnum_diff_line(self):
        self.assertTrue(p1.is_engnum_diff_line((False, 1, 3), (True, 3, 3), 4))
        self.assertTrue(p1.is_engnum_diff_line((False, 1, 3), (True, 2, 2), 3))
        self.assertTrue(p1.is_engnum_diff_line((False, 1, 3), (True, 1, 1), 3))
        self.assertTrue(p1.is_engnum_diff_line((False, 1, 3), (True, 0, 0), 3))
        self.assertTrue(p1.is_engnum_diff_line((False, 1, 3), (True, 3, 3), 3))
        self.assertTrue(p1.is_engnum_diff_line((False, 1, 3), (True, 4, 4), 5))
        self.assertTrue(p1.is_engnum_diff_line((False, 4, 6), (True, 3, 3), 4))
        self.assertTrue(p1.is_engnum_diff_line((False, 3, 4), (True, 3, 3), 4))
        self.assertTrue(p1.is_engnum_diff_line((False, 2, 4), (True, 3, 3), 4))
        self.assertFalse(p1.is_engnum_diff_line((False, 5, 6), (True, 3, 3), 6))
        self.assertFalse(p1.is_engnum_diff_line((False, 1, 3), (True, 5, 5), 6))

    def test_is_engnum_same_line(self):
        self.assertTrue(p1.is_engnum_same_line((False, 1, 3), (True, 4, 4)))
        self.assertTrue(p1.is_engnum_same_line((False, 4, 6), (True, 3, 3)))
        self.assertFalse(p1.is_engnum_same_line((False, 4, 6), (True, 2, 2)))
        self.assertFalse(p1.is_engnum_same_line((False, 1, 3), (True, 5, 5)))

    def test_eng_num_same_lines(self):
        self.assertEqual([(False, 1, 3), (False, 5, 7)], p1.find_eng_num_same_line([(False, 1, 3), (True, 4, 4), (False, 5, 7), (False, 8, 9)]))
        self.assertEqual([], p1.find_eng_num_same_line([(False, 1, 1), (False, 3, 4), (False, 5, 7), (False, 8, 9)]))
        self.assertEqual([(False, 4, 4)], p1.find_eng_num_same_line([(False, 1, 3), (False, 4, 4), (True, 5, 5), (False, 8, 9)]))
        self.assertEqual([(False, 5, 7)], p1.find_eng_num_same_line([(False, 1, 3), (False, 4, 4), (False, 5, 7), (True, 8, 9)]))

    def test_eng_num_diff_line(self):
        self.assertEqual([(False, 1, 3), (False, 4, 5), (False, 8, 8)],
                         p1.find_eng_num_diff_line([(False, 1, 3), (False, 4, 5), (False, 6, 6), (False, 8, 8)],
                                                   [(False, 1, 1), (True, 4, 4), (False, 5, 5), (True, 8, 8)], 9))
