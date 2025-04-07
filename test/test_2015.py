import unittest

from year_2015 import day_01, day_02, day_03, day_04, day_05, day_06


class Test2015(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(232, day_01.part1())
        self.assertEqual(1783, day_01.part2())

    def test_day_02(self):
        self.assertEqual(1598415, day_02.part1())
        self.assertEqual(3812909, day_02.part2())

    def test_day_03(self):
        self.assertEqual(2565, day_03.part1())
        self.assertEqual(2639, day_03.part2())

    def test_day_04(self):
        self.assertEqual(282749, day_04.part1())
        self.assertEqual(9962624, day_04.part2())

    def test_day_05(self):
        self.assertEqual(238, day_05.part1())

    def test_day_06(self):
        self.assertEqual(569999, day_06.part1())
        self.assertEqual(17836115, day_06.part2())
