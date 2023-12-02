from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d2 import p1


class D2P1Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 2
        self.puzzle = 1
        self.solver = SolutionRunner(self.day, p1)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_process_line(self):
        self.assertEqual(1, p1.process_line("Game 1: 3 blue, 4 red; 6 green, 7 blue "))
        self.assertEqual(20, p1.process_line("Game 20: 3 blue, 4 red; 6 green, 7 blue "))
        self.assertEqual(20, p1.process_line("Game 20: 3 blue, 4 red; 6 green, 12 red, 7 blue "))
        self.assertEqual(0, p1.process_line("Game 20: 3 blue, 4 red; 13 green, 13 red, 14 blue "))
        self.assertEqual(0, p1.process_line("Game 20: 3 blue, 4 red; 14 green, 12 red, 14 blue "))
        self.assertEqual(0, p1.process_line("Game 20: 3 blue, 4 red; 13 green, 12 red, 15 blue "))
