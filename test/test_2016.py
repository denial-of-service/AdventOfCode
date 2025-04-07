import unittest

from src.year_2016 import day_01, day_02


class Test2016(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(298, day_01.part1())
        self.assertEqual(158, day_01.part2())

    def test_day_02(self):
        self.assertEqual('45973', day_02.part1())
        self.assertEqual('27CA4', day_02.part2())
