import tests
import os

SOLUTIONS_DIR = f'{os.path.dirname(tests.__file__)}/data/solutions'
INPUTS_DIR = f'{os.path.dirname(tests.__file__)}/data/inputs'


# Test runner for Advent of Code
class TestRunner():
    def get_puzzle_solution(self):
        return _read_solution(self._build_solution_path('puzzle'))

    def get_example_solution(self):
        return _read_solution(self._build_solution_path('example'))

    def assert_solution_puzzle(self):
        self.assertEqual(self.get_puzzle_solution(),
                         str(self.solver.puzzle_solution()))

    def assert_solution_example(self):
        self.assertEqual(self.get_example_solution(),
                         str(self.solver.example_solution(self.puzzle)))

    def _build_solution_path(self, sol_type):
        return f'{SOLUTIONS_DIR}/d{self.day}/p{self.puzzle}/{sol_type}'


class SolutionRunner():
    def __init__(self, day, solution_calculator):
        self.day = day
        self.solution_calculator = solution_calculator

    def puzzle_solution(self):
        return self.solution_calculator.solve(self._build_path('puzzle'))

    def example_solution(self, puzzle):
        return self.solution_calculator.solve(self._build_path_example(puzzle))

    def _build_path_example(self, puzzle):
        return self._build_path(f'p{puzzle}/example')

    def _build_path(self, input):
        return f'{INPUTS_DIR}/d{self.day}/{input}'


def _read_solution(file):
    with open(file) as f:
        res = f.read().strip()
        return res
