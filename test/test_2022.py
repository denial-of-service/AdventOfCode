import unittest

from src.year_2022 import day_01


class Test2022(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(70698, day_01.part_1())
        self.assertEqual(206643, day_01.part_2())
