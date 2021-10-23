import unittest
from Lesson_5 import *


class Test(unittest.TestCase):
    def test_triangle_kind(self):
        self.assertEqual(-1, triangle_kind(3.0, 7.5, 4.0))
        self.assertEqual(1, triangle_kind(5.0, 3.0, 4.0))
        self.assertEqual(2, triangle_kind(4.0, 6.0, 8.0))
        self.assertEqual(0, triangle_kind(1.0, 1.5, 1.5))

    def test_segment_length(self):
        self.assertEqual(-1, segment_length(1, 2, 3, 4))
        self.assertEqual(-1, segment_length(5, 7, 1, 3))
        self.assertEqual(0, segment_length(1, 2, 2, 4))
        self.assertEqual(3, segment_length(3, 6, 0, 9))
        self.assertEqual(2, segment_length(2, 5, 3, 9))
        self.assertEqual(1, segment_length(3, 6, 1, 4))
        self.assertEqual(4, segment_length(1, 15, 10, 14))

    def test_point_inside_circle(self):
        self.assertEqual(True, point_inside_circle(1.0, 1.0, 0.0, 0.0, 2.0))
        self.assertEqual(False, point_inside_circle(2.0, 2.0, 0.0, 0.0, 2.0))

    def test_is_number_happy(self):
        self.assertEqual(True, is_number_happy(1533))
        self.assertEqual(True, is_number_happy(9009))
        self.assertEqual(False, is_number_happy(3644))

    def test_queen_threatens(self):
        self.assertEqual(True, queen_threatens(3, 6, 7, 6))
        self.assertEqual(True, queen_threatens(8, 1, 1, 8))
        self.assertEqual(False, queen_threatens(7, 6, 5, 7))

    def test_days_in_month(self):
        self.assertEqual(31, days_in_month(1, 1990))
        self.assertEqual(28, days_in_month(2, 1990))
        self.assertEqual(31, days_in_month(3, 1990))
        self.assertEqual(30, days_in_month(4, 1990))
        self.assertEqual(31, days_in_month(5, 1990))
        self.assertEqual(30, days_in_month(6, 1990))
        self.assertEqual(31, days_in_month(7, 1990))
        self.assertEqual(31, days_in_month(8, 1990))
        self.assertEqual(29, days_in_month(2, 1992))
        self.assertEqual(29, days_in_month(2, 1996))
        self.assertEqual(28, days_in_month(2, 1900))
        self.assertEqual(29, days_in_month(2, 2000))