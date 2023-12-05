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
        self.assertEqual([('467', 0, 2), (None, 3, 3), ('114', 5, 7), ('123', 10, 12)], p1.parse_items("467*.114..123"))
        self.assertEqual([(None, 1, 1), (None, 4, 4), (None, 7, 7), (None, 9, 9)], p1.parse_items(".@..-../.="))
        self.assertEqual([('467', 0, 2), ('114', 5, 7)], p1.parse_items("467..114.."))
        self.assertEqual([('67', 1, 2), ('114', 5, 7)], p1.parse_items(".67..114.."))
        self.assertEqual([('467', 0, 2), ('114', 5, 7), ('123', 10, 12)], p1.parse_items("467..114..123"))
        self.assertEqual([('467', 0, 2), ('114', 5, 7), (None, 8, 8), ('123', 10, 12)], p1.parse_items("467..114*.123"))
        self.assertEqual([('467', 0, 2), ('114', 5, 7), ('123', 10, 12), (None, 13, 13)], p1.parse_items("467..114..123*"))
        self.assertEqual([('467', 0, 2), ('114', 5, 7), (None, 9, 9), ('123', 10, 12), (None, 13, 13)], p1.parse_items("467..114.-123*"))
        self.assertEqual([('67', 1, 2), (None, 3, 3), ('114', 5, 7), (None, 9, 9)], p1.parse_items(".67*.114.-"))
        self.assertEqual([('6', 1, 1), (None, 3, 3), ('1', 5, 5), ('4', 7, 7), (None, 9, 9)], p1.parse_items(".6.*.1.4.-"))

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
        self.assertEqual([('', 1, 3), ('', 5, 7)], p1.find_eng_num_same_line([('', 1, 3), (None, 4, 4), ('', 5, 7), ('', 8, 9)]))
        self.assertEqual([], p1.find_eng_num_same_line([('', 1, 1), ('', 3, 4), ('', 5, 7), ('', 8, 9)]))
        self.assertEqual([('', 4, 4)], p1.find_eng_num_same_line([('', 1, 3), ('', 4, 4), (None, 5, 5), ('', 8, 9)]))
        self.assertEqual([('', 5, 7)], p1.find_eng_num_same_line([('', 1, 3), ('', 4, 4), ('', 5, 7), (None, 8, 9)]))

    def test_eng_num_diff_line(self):
        self.assertEqual([('', 1, 3), ('', 4, 5), ('', 8, 8)],
                         p1.find_eng_num_diff_line([('', 1, 3), ('', 4, 5), ('', 6, 6), ('', 8, 8)],
                                                   [('', 1, 1), (None, 4, 4), ('', 5, 5), (None, 8, 8)], 9))

    def test_process_line(self):
        self.assertEqual(([('0:0:2', 467)], [(None, 3, 3)]), p1.process_line('...*......', 1, '467..114..', [('467', 0, 2), ('114', 5, 7)]))
        self.assertEqual(([('2:2:3', 35)], [('35', 2, 3), ('633', 6, 8)]), p1.process_line('..35..633.', 2, '...*......', [(None, 3, 3)]))
