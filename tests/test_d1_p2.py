from unittest import TestCase
from tests.util.runner import TestRunner
from tests.util.runner import SolutionRunner
from solutions.d1 import p2


class D1P2Test(TestRunner, TestCase):
    @classmethod
    def setUpClass(self):
        self.day = 1
        self.puzzle = 2
        self.solver = SolutionRunner(self.day, p2)

    def test_puzzle(self):
        self.assert_solution_puzzle()

    def test_example(self):
        self.assert_solution_example()

    def test_line_forward(self):
        self.assertEqual('3', p2.find_forward('z3two'))
        self.assertEqual('1', p2.find_forward('onetwo'))
        self.assertEqual('1', p2.find_forward('zonetwo'))
        self.assertEqual('1', p2.find_forward('zononetwo'))
        self.assertEqual('2', p2.find_forward('zon2onetwo'))
        self.assertEqual('3', p2.find_forward('3zon2onetwo'))
        self.assertEqual('8', p2.find_forward('threight2onetwo'))
        self.assertEqual('3', p2.find_forward('zthreeight2onetwo'))
        self.assertEqual('7', p2.find_forward('zseveneight2onetwo'))

    def test_line_reverse(self):
        self.assertEqual('3', p2.find_reverse('ztwo3'))
        self.assertEqual('2', p2.find_reverse('z3two'))
        self.assertEqual('2', p2.find_reverse('onetwo'))
        self.assertEqual('2', p2.find_reverse('zonetwozz'))
        self.assertEqual('2', p2.find_reverse('zononetwoz'))
        self.assertEqual('2', p2.find_reverse('zon2onetwoee'))
        self.assertEqual('1', p2.find_reverse('3zon2onetw'))
        self.assertEqual('2', p2.find_reverse('threight2on'))
        self.assertEqual('8', p2.find_reverse('zthreeightoewo'))

    def test_line_full(self):
        self.assertEqual(19, p2.process_line('eone39six55ninenhhdd'))
        self.assertEqual(18, p2.process_line('zzesz1threeight'))
        self.assertEqual(12, p2.process_line('onenetwo'))
        self.assertEqual(11, p2.process_line('onenetwone'))
        self.assertEqual(11, p2.process_line('onenet3wone'))
        self.assertEqual(28, p2.process_line('2328'))
        self.assertEqual(31, p2.process_line('nenet3wone'))
        self.assertEqual(22, p2.process_line('2eightnin2three2'))
        self.assertEqual(44, p2.process_line('44kmn'))
        self.assertEqual(11, p2.process_line('1onenetwone'))
        self.assertEqual(15, p2.process_line('1onenefiveour'))
        self.assertEqual(11, p2.process_line('asdfasdfoneneddd'))
        self.assertEqual(97, p2.process_line('zeronine7'))
        self.assertEqual(58, p2.process_line('five1nine78888'))
        self.assertEqual(55, p2.process_line('5'))
        self.assertEqual(55, p2.process_line('five'))
        self.assertEqual(32, p2.process_line('threeightwo'))
