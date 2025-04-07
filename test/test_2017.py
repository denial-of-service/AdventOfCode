import unittest

from src.year_2017 import day_01


class Test2017(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(995, day_01.part1())
        self.assertEqual(1130, day_01.part2())
