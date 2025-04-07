import unittest

from src.year_2020 import day_01


class Test2020(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(927684, day_01.part1())
        self.assertEqual(292093004, day_01.part2())
