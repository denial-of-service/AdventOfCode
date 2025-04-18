import unittest

from year_2024 import day_01, day_02, day_03, day_04, day_05, day_06, day_07


class Test2024(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(1603498, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(25574739, day_01.part_2())

    def test_day_02_part_1(self):
        self.assertEqual(591, day_02.part_1())

    def test_day_02_part_2(self):
        self.assertEqual(621, day_02.part_2())

    def test_day_03_part_1(self):
        self.assertEqual(166357705, day_03.part_1())

    def test_day_03_part_2(self):
        self.assertEqual(88811886, day_03.part_2())

    def test_day_04_part_1(self):
        self.assertEqual(2454, day_04.part_1())

    def test_day_04_part_2(self):
        self.assertEqual(1858, day_04.part_2())

    def test_day_05_part_1(self):
        self.assertEqual(5732, day_05.part_1())

    def test_day_05_part_2(self):
        self.assertEqual(4716, day_05.part_2())

    def test_day_06_part_1(self):
        self.assertEqual(4758, day_06.part_1())

    def test_day_06_part_2(self):
        self.assertEqual(1670, day_06.part_2())

    def test_day_07_part_1(self):
        self.assertEqual(1289579105366, day_07.part_1())

    def test_day_07_part_2(self):
        self.assertEqual(92148721834692, day_07.part_2())
