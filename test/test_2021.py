import unittest

from year_2021 import day_01, day_02


class Test2021(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(1624, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(1653, day_01.part_2())

    def test_day_02_part_1(self):
        self.assertEqual(1893605, day_02.part_1())

    def test_day_02_part_2(self):
        self.assertEqual(2120734350, day_02.part_2())