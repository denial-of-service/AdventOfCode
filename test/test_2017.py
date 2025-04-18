import unittest

from year_2017 import day_01


class Test2017(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(995, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(1130, day_01.part_2())
