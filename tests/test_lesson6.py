import unittest
from Lesson_6 import *


class Test(unittest.TestCase):
    def test_circle_inside(self):
        self.assertEqual(False, circle_inside(0.0, 0.0, 6.0, 0.0, 0.0, 5.0))
        self.assertEqual(False, circle_inside(0.0, 0.0, 1.0, 10.0, 10.0, 9.0))
        self.assertEqual(True, circle_inside(2.0, 2.0, 2.0, 2.0, 2.0, 2.0))
        self.assertEqual(True, circle_inside(-2.0, 3.0, 2.0, -2.0, 0.0, 5.0))
        self.assertEqual(True, circle_inside(1.0, 2.0, 3.0, 4.0, 5.0, 6.0))

    def test_brick_passes(self):
        self.assertEqual(True, brick_passes(2, 10, 5, 6, 3))
        self.assertEqual(True, brick_passes(4, 4, 4, 4, 4))
        self.assertEqual(False, brick_passes(6, 5, 4, 3, 6))
        self.assertEqual(True, brick_passes(3, 2, 1, 1, 2))

    def test_factorial(self):
        self.assertEqual(1.0, factorial(0))
        self.assertEqual(1.0, factorial(1))
        self.assertEqual(6.0, factorial(3))
        self.assertEqual(120.0, factorial(5))
        self.assertEqual(3628800.0, factorial(10))
        self.assertEqual(2.43290200817664E18, factorial(20))

    def test_is_prime(self):
        self.assertEqual(False, is_prime(1))
        self.assertEqual(True, is_prime(2))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))
        self.assertEqual(False, is_prime(4))
        self.assertEqual(False, is_prime(9))
        self.assertEqual(False, is_prime(15))
        count = 0
        for n in range(2, 7919 + 1):
            if is_prime(n):
                count += 1
        self.assertEqual(1000, count)
        count = 0
        for n in range(2, 1000000 + 1):
            if is_prime(n):
                count += 1
        self.assertEqual(78498, count)

    def test_is_perfect(self):
        self.assertEqual(True, is_perfect(6))
        self.assertEqual(True, is_perfect(28))
        self.assertEqual(False, is_perfect(100))

    def test_digit_count_in_number(self):
        self.assertEqual(1, digit_count_in_number(0, 0))
        self.assertEqual(1, digit_count_in_number(7, 7))
        self.assertEqual(0, digit_count_in_number(21, 3))
        self.assertEqual(1, digit_count_in_number(510, 5))
        self.assertEqual(3, digit_count_in_number(4784041, 4))
        self.assertEqual(4, digit_count_in_number(5373393, 3))

    def test_digit_number(self):
        self.assertEqual(1, digit_number(0))
        self.assertEqual(1, digit_number(7))
        self.assertEqual(2, digit_number(10))
        self.assertEqual(2, digit_number(99))
        self.assertEqual(3, digit_number(123))
        self.assertEqual(10, digit_number(1123456789))

    def test_fib(self):
        self.assertEqual(1, fib(1))
        self.assertEqual(1, fib(2))
        self.assertEqual(2, fib(3))
        self.assertEqual(5, fib(5))
        self.assertEqual(21, fib(8))
        self.assertEqual(102334155, fib(40))
        self.assertEqual(1134903170, fib(45))
        self.assertEqual(1836311903, fib(46))
        # Just to calculate it
        fib(50)

    def test_minimal_divisor(self):
        self.assertEqual(2, minimal_divisor(4))
        self.assertEqual(5, minimal_divisor(5))
        self.assertEqual(5, minimal_divisor(5))
        self.assertEqual(173, minimal_divisor(173))
        self.assertEqual(197, minimal_divisor(197))
        self.assertEqual(5, minimal_divisor(25))
        self.assertEqual(17, minimal_divisor(8653))

    def test_is_co_prime(self):
        self.assertEqual(False, is_co_prime(14, 49))
        self.assertEqual(False, is_co_prime(49, 14))
        self.assertEqual(False, is_co_prime(25, 25))
        self.assertEqual(True, is_co_prime(13, 13))
        self.assertEqual(False, is_co_prime(37, 111))



