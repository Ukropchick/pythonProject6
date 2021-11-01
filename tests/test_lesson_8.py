from Lesson_8 import *
import unittest


class Test(unittest.TestCase):
    def test_roman(self):
        self.assertEqual("I", roman(1))
        self.assertEqual("MMM", roman(3000))
        self.assertEqual("MCMLXXVIII", roman(1978))
        self.assertEqual("DCXCIV", roman(694))
        self.assertEqual("XLIX", roman(49))
        self.assertEqual("VII", roman(7))
        self.assertEqual("V", roman(5))
        self.assertEqual("XIX", roman(19))