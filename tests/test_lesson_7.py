import unittest
from Lesson_7 import *


class Test(unittest.TestCase):
    def test_sq_roots(self):
        self.assertEqual([], sq_roots(-1.0))
        self.assertEqual([0.0], sq_roots(0.0))
        self.assertEqual([-5.0, 5.0], sq_roots(25.0))

    def test_negative_list(self):
        self.assertEqual([], negative_list([1, 2, 3]))
        self.assertEqual([-1, -5], negative_list([-1, 2, 4, -5]))

    def test_mean(self):
        self.assertEqual(0.0, mean([]))
        self.assertEqual(1.0, mean([1.0]))
        self.assertEqual(2.0, mean([3.0, 1.0, 2.0]))
        self.assertEqual(3.0, mean([0.0, 2.0, 7.0, 8.0, -2.0]))

    def test_center(self):
        self.assertEqual([0.0], center([3.14]))
        self.assertEqual([1.0, -1.0, 0.0], center([3.0, 1.0, 2.0]))
        self.assertEqual([-3.0, -1.0, 4.0, 5.0, -5.0], center([0.0, 2.0, 7.0, 8.0, -2.0]))

    def test_polynom(self):
        self.assertEqual(0, polynom([], 1000))
        self.assertEqual(42, polynom([42], -1000))
        self.assertEqual(13, polynom([3, 2], 5))
        self.assertEqual(0, polynom([2, -3, 1], 1))
        self.assertEqual(45, polynom([-7, 6, 4, -4, 1], -2))

    def test_factorize(self):
        self.assertEqual([2], factorize(2))
        self.assertEqual([3, 5, 5], factorize(75))
        self.assertEqual([2, 3, 3, 19], factorize(342))

    def test_convert(self):
        self.assertEqual([1], convert(1, 2))
        self.assertEqual([1, 2, 1, 0], convert(100, 4))
        self.assertEqual([1, 3, 12], convert(250, 14))
        self.assertEqual([2, 14, 12], convert(1000, 19))

