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
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_parse_items(self):
        self.assertEqual([(True, 1, 1), (True, 4, 4), (True, 7, 7), (True, 9, 9)], p1.parse_items(".*..-..#.="))
        self.assertEqual([(False, 0, 2), (False, 5, 7)], p1.parse_items("467..114.."))
        self.assertEqual([(False, 1, 2), (False, 5, 7)], p1.parse_items(".67..114.."))
        self.assertEqual([(False, 1, 2), (True, 3, 3), (False, 5, 7), (True, 9, 9)], p1.parse_items(".67*.114.-"))
        self.assertEqual([(False, 1, 1), (True, 3, 3), (False, 5, 5), (False, 7, 7), (True, 9, 9)], p1.parse_items(".6.*.1.4.-"))
