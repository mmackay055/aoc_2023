from unittest import TestCase
from solutions.d5 import common


class D5CommonTest(TestCase):
    def test_build_map(self):
        self.assertEqual(common.Map(98, 50, 2), common.build_map('50 98 2'))
        self.assertEqual(common.Map(98, 5, 2), common.build_map('5 98 2'))
        self.assertEqual(common.Map(9, 5, 2), common.build_map(' 5 9 2 '))
        self.assertEqual(common.Map(9, 5, 2), common.build_map(' 5 9 2'))
        self.assertEqual(common.Map(9, 5, 2), common.build_map('5 9 2 '))

    def test_map_output(self):
        map = common.Map(98, 50, 2)
        self.assertEqual(50, map.output(98))
        self.assertEqual(51, map.output(99))

    def test_almanac_build(self):
        builder = common.AlmanacDataParser()
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
        almanac = builder.build()
        self.assertEqual('seed-to-soil', almanac.mappers[0].name)
        self.assertEqual(common.Map(98, 50, 2), almanac.mappers[0].maps[0])
        self.assertEqual(common.Map(50, 52, 48), almanac.mappers[0].maps[1])
        self.assertEqual('soil-to-fertilizer', almanac.mappers[1].name)
        self.assertEqual(common.Map(15, 0, 37), almanac.mappers[1].maps[0])
        self.assertEqual(common.Map(52, 37, 2), almanac.mappers[1].maps[1])
        self.assertEqual(common.Map(0, 39, 15), almanac.mappers[1].maps[2])
        self.assertEqual('fertilizer-to-water', almanac.mappers[2].name)
        self.assertEqual(common.Map(53, 49, 8), almanac.mappers[2].maps[0])
        self.assertEqual(common.Map(11, 0, 42), almanac.mappers[2].maps[1])
        self.assertEqual(common.Map(0, 42, 7), almanac.mappers[2].maps[2])
        self.assertEqual(common.Map(7, 57, 4), almanac.mappers[2].maps[3])
