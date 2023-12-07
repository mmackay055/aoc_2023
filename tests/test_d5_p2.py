from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d5 import p2


class D5P2Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 5
        self.puzzle = 2
        self.solver = SolutionRunner(self.day, p2)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_parse_seeds(self):
        self.assertEqual([(79, 93), (55, 68)], p2.parse_seeds("seeds: 79 14 55 13"))
