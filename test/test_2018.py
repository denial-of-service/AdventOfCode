import unittest

from year_2018 import day_01


class Test2018(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(592, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(241, day_01.part_2())
