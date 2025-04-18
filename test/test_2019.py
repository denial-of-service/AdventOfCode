import unittest

from year_2019 import day_01


class Test2019(unittest.TestCase):
    def test_day_01_part_1(self):
        self.assertEqual(3369286, day_01.part_1())

    def test_day_01_part_2(self):
        self.assertEqual(5051054, day_01.part_2())
