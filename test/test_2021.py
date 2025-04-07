import unittest

from src.year_2021 import day_01


class Test2021(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(1624, day_01.part1())
        self.assertEqual(1653, day_01.part2())
