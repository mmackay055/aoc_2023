from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d5 import p1


class D5P1Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 5
        self.puzzle = 1
        self.solver = SolutionRunner(self.day, p1)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_build_map(self):
        self.assertEqual(p1.Map(98, 50, 2), p1.build_map('50 98 2'))
        self.assertEqual(p1.Map(98, 5, 2), p1.build_map('5 98 2'))
        self.assertEqual(p1.Map(9, 5, 2), p1.build_map(' 5 9 2 '))
        self.assertEqual(p1.Map(9, 5, 2), p1.build_map(' 5 9 2'))
        self.assertEqual(p1.Map(9, 5, 2), p1.build_map('5 9 2 '))

    def test_map_output(self):
        map = p1.Map(98, 50, 2)
        self.assertEqual(50, map.output(98))
        self.assertEqual(51, map.output(99))

    def test_almanac_build(self):
        builder = p1.AlmanacDataParser()
        builder.process_line('seeds: 79 14 55 13')
        builder.process_line('')
        builder.process_line('seed-to-soil map:')
        builder.process_line('50 98 2')
        builder.process_line('52 50 48')
        builder.process_line('')
        builder.process_line('soil-to-fertilizer map')
        builder.process_line('0 15 37')
        builder.process_line('37 52 2')
        builder.process_line('39 0 15')
        builder.process_line('')
        builder.process_line('fertilizer-to-water map:')
        builder.process_line('49 53 8')
        builder.process_line('0 11 42')
        builder.process_line('42 0 7')
        builder.process_line('57 7 4')
        (almanac, seeds) = builder.build()
        self.assertEqual([79, 14, 55, 13], seeds)
        self.assertEqual('seed-to-soil', almanac.mappers[0].name)
        self.assertEqual(p1.Map(98, 50, 2), almanac.mappers[0].maps[0])
        self.assertEqual(p1.Map(50, 52, 48), almanac.mappers[0].maps[1])
        self.assertEqual('soil-to-fertilizer', almanac.mappers[1].name)
        self.assertEqual(p1.Map(15, 0, 37), almanac.mappers[1].maps[0])
        self.assertEqual(p1.Map(52, 37, 2), almanac.mappers[1].maps[1])
        self.assertEqual(p1.Map(0, 39, 15), almanac.mappers[1].maps[2])
        self.assertEqual('fertilizer-to-water', almanac.mappers[2].name)
        self.assertEqual(p1.Map(53, 49, 8), almanac.mappers[2].maps[0])
        self.assertEqual(p1.Map(11, 0, 42), almanac.mappers[2].maps[1])
        self.assertEqual(p1.Map(0, 42, 7), almanac.mappers[2].maps[2])
        self.assertEqual(p1.Map(7, 57, 4), almanac.mappers[2].maps[3])
