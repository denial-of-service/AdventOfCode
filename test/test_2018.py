import unittest

from src.year_2018 import day_01


class Test2018(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(592, day_01.part1())
        self.assertEqual(241, day_01.part2())
