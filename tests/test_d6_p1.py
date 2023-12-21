from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d6 import p1


class D6P1Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 6
        self.puzzle = 1
        self.solver = SolutionRunner(self.day, p1)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_parse_line(self):
        self.assertEqual([7, 15, 30], p1.parse_line("Time:      7  15   30"))
        self.assertEqual([9, 40, 200], p1.parse_line("Distance:  9  40  200"))
