from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d6 import p2


class D6P2Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 6
        self.puzzle = 2
        self.solver = SolutionRunner(self.day, p2)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_parse_line(self):
        self.assertEqual(71530, p2.parse_line("Time:      7  15   30"))
        self.assertEqual(940200, p2.parse_line("Distance:  9  40  200"))
