from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d4 import p2


class D4P2Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 4
        self.puzzle = 2
        self.solver = SolutionRunner(self.day, p2)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()
