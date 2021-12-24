import unittest
from Lesson_12 import *


class Test(unittest.TestCase):
    def test_date_str_to_digit(self):
        self.assertEqual("15.07.2016", date_str_to_digit("15 июля 2016"))
        self.assertEqual("", date_str_to_digit("3 мартобря 1918"))
        self.assertEqual("18.11.2018", date_str_to_digit("18 ноября 2018"))
        # self.assertEqual("", date_str_to_digit("23"))
        # self.assertEqual("03.04.2011", date_str_to_digit("3 апреля 2011"))
        self.assertEqual("", date_str_to_digit("32 сентября 2011"))
        self.assertEqual("", date_str_to_digit("29 февраля 1993"))

    def test_flatten_phone_number(self):
        self.assertEqual("+79211234567", flatten_phone_number("+7 (921) 123-45-67"))
        self.assertEqual("123456798", flatten_phone_number("12 --  34- 5 -- 67 -98"))
        self.assertEqual("+12345", flatten_phone_number("+12 (3) 4-5"))
        self.assertEqual("", flatten_phone_number("+12 () 4-5"))
        self.assertEqual("+425667", flatten_phone_number("+42 56 -- 67"))
        self.assertEqual("+42566789", flatten_phone_number("+42(56 -- 67)89"))
        self.assertEqual("", flatten_phone_number("ab-123"))
        self.assertEqual("", flatten_phone_number("134_+874"))

    def test_best_long_jump(self):
        self.assertEqual(717, best_long_jump("706 % - 717 - 703"))
        self.assertEqual(-1, best_long_jump("% - - % -"))
        self.assertEqual(754, best_long_jump("700 717 707 % 754"))
        self.assertEqual(-1, best_long_jump("700 + 700"))
