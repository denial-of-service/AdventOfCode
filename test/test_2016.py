import unittest

from year_2016 import day_01, day_02


class Test2016(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(298, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(158, day_01.part_2())

    def test_day_02_part_1(self):
        self.assertEqual('45973', day_02.part_1())

    def test_day_02_part_2(self):
        self.assertEqual('27CA4', day_02.part_2())
