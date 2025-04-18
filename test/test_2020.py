import unittest

from year_2020 import day_01


class Test2020(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(927684, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(292093004, day_01.part_2())
