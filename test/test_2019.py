import unittest

from src.year_2019 import day_01


class Test2019(unittest.TestCase):
    def test_day_01(self):
        self.assertEqual(3369286, day_01.part_1())
        self.assertEqual(5051054, day_01.part_2())
