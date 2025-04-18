import unittest

from year_2023 import day_01, day_02, day_04, day_06


class Test2023(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(56397, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(55701, day_01.part_2())

    def test_day_02_part_1(self):
        self.assertEqual(2317, day_02.part_1())

    def test_day_02_part_2(self):
        self.assertEqual(74804, day_02.part_2())

    def test_day_04_part_1(self):
        self.assertEqual(27845, day_04.part_1())

    def test_day_06_part_1(self):
        self.assertEqual(1108800, day_06.part_1())

    def test_day_06_part_2(self):
        self.assertEqual(36919753, day_06.part_2())
