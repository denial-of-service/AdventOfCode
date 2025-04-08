import unittest

from year_2023 import day_01, day_04


class Test2023(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(56397, day_01.part1())
        self.assertEqual(55701, day_01.part2())

    def test_day_04(self):
        self.assertEqual(27845, day_04.part1())
