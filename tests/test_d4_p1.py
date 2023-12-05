from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d4 import p1


class D4P1Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 4
        self.puzzle = 1
        self.solver = SolutionRunner(self.day, p1)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()
