import unittest

from src.year_2023 import day_04


class Test2023(unittest.TestCase):
    def test_day_04(self):
        self.assertEqual(27845, day_04.part1())
