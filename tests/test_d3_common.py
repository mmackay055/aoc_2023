from unittest import TestCase
from solutions.d3.common import Item, parse_items, is_engnum_same_line, is_engnum_diff_line, find_eng_num_same_line, find_eng_num_diff_line


class D3CommonTest(TestCase):
    def test_parse_items(self):
        self.assertEqual([Item('467', 0, 0, 2), Item('*', 0, 3, 3), Item('114', 0, 5, 7), Item('123', 0, 10, 12)], parse_items("467*.114..123", 0))
        self.assertEqual([Item('@', 0, 1, 1), Item('-', 0, 4, 4), Item('/', 0, 7, 7), Item('=', 0, 9, 9)], parse_items(".@..-../.=", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7)], parse_items("467..114..", 0))
        self.assertEqual([Item('67', 0, 1, 2), Item('114', 0, 5, 7)], parse_items(".67..114..", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('123', 0, 10, 12)], parse_items("467..114..123", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('*', 0, 8, 8), Item('123', 0, 10, 12)], parse_items("467..114*.123", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('123', 0, 10, 12), Item('*', 0, 13, 13)], parse_items("467..114..123*", 0))
        self.assertEqual([Item('467', 0, 0, 2), Item('114', 0, 5, 7), Item('-', 0, 9, 9), Item('123', 0, 10, 12), Item('*', 0, 13, 13)], parse_items("467..114.-123*", 0))
        self.assertEqual([Item('67', 0, 1, 2), Item('*', 0, 3, 3), Item('114', 0, 5, 7), Item('-', 0, 9, 9)], parse_items(".67*.114.-", 0))
        self.assertEqual([Item('6', 0, 1, 1), Item('*', 0, 3, 3), Item('1', 0, 5, 5), Item('4', 0, 7, 7), Item('-', 0, 9, 9)], parse_items(".6.*.1.4.-", 0))

    def test_is_engnum_diff_line(self):
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 3, 3), 4))
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 2, 2), 3))
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 1, 1), 3))
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 0, 0), 3))
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 3, 3), 3))
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 4, 4), 5))
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 4, 6), Item('*', 1, 3, 3), 4))
        self.assertTrue(is_engnum_diff_line(Item('12', 0, 3, 4), Item('*', 1, 3, 3), 4))
        self.assertTrue(is_engnum_diff_line(Item('123', 0, 2, 4), Item('*', 1, 3, 3), 4))
        self.assertFalse(is_engnum_diff_line(Item('12', 0, 5, 6), Item('*', 1, 3, 3), 6))
        self.assertFalse(is_engnum_diff_line(Item('123', 0, 1, 3), Item('*', 1, 5, 5), 6))

    def test_is_engnum_same_line(self):
        self.assertTrue(is_engnum_same_line(Item('123', 0, 1, 3), Item('*', 0, 4, 4)))
        self.assertTrue(is_engnum_same_line(Item('222', 0, 4, 6), Item('#', 0, 3, 3)))
        self.assertFalse(is_engnum_same_line(Item('123', 0, 4, 6), Item('*', 0, 2, 2)))
        self.assertFalse(is_engnum_same_line(Item('123', 0, 1, 3), Item('*', 0, 5, 5)))

    def test_eng_num_same_lines(self):
        self.assertEqual([(Item('*', 0, 4, 4), Item('123', 0, 1, 3)), (Item('*', 0, 4, 4), Item('123', 0, 5, 7))], find_eng_num_same_line([Item('123', 0, 1, 3), Item('*', 0, 4, 4), Item('123', 0, 5, 7), Item('123', 0, 8, 9)]))
        self.assertEqual([], find_eng_num_same_line([Item('123', 0, 1, 1), Item('123', 0, 3, 4), Item('123', 0, 5, 7), Item('123', 0, 8, 9)]))
        self.assertEqual([(Item('*', 0, 5, 5), Item('123', 0, 4, 4))], find_eng_num_same_line([Item('123', 0, 1, 3), Item('123', 0, 4, 4), Item('*', 0, 5, 5), Item('123', 0, 8, 9)]))
        self.assertEqual([(Item('*', 0, 8, 9), Item('123', 0, 5, 7))], find_eng_num_same_line([Item('123', 0, 1, 3), Item('123', 0, 4, 4), Item('123', 0, 5, 7), Item('*', 0, 8, 9)]))

    def test_eng_num_diff_line(self):
        self.assertEqual([(Item('*', 0, 4, 4), Item('123', 0, 1, 3)), (Item('*', 0, 4, 4), Item('123', 0, 4, 5)), (Item('*', 0, 8, 8), Item('123', 0, 8, 8))],
                         find_eng_num_diff_line([Item('123', 0, 1, 3), Item('123', 0, 4, 5), Item('123', 0, 6, 6), Item('123', 0, 8, 8)],
                                                [Item('123', 0, 1, 1), Item('*', 0, 4, 4), Item('123', 0, 5, 5), Item('*', 0, 8, 8)], 9))
