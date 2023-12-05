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

    def test_process_line(self):
        self.assertEqual(([('0:0:2', 467)], [Item('*', 1, 3, 3)]), p1.process_line('...*......', 1, '467..114..', [Item('467', 0, 0, 2), Item('114', 0, 5, 7)]))
        self.assertEqual(([('2:2:3', 35)], [Item('35', 2, 2, 3), Item('633', 2, 6, 8)]), p1.process_line('..35..633.', 2, '...*......', [Item('*', 0, 3, 3)]))
