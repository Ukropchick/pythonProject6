import unittest

from Lesson_11 import *


class Test(unittest.TestCase):
    def test_delete_marked(self):
        delete_marked("C:/Users/V/PycharmProjects/pythonProject6/input/delete_in1.txt", "temp.txt")

    def test_count_substrings(self):
        self.assertEqual(
            {"РАЗНЫЕ": 2, "ные": 2, "Неряшливость": 1, "е": 49, "эволюция": 0},
            count_substrings("C:/Users/V/PycharmProjects/pythonProject6/input/substrings_in1.txt", ["РАЗНЫЕ", "ные", "Неряшливость", "е", "эволюция"])
        )
        self.assertEqual(
            {"Карминовый": 2, "Некрасивый": 2, "белоглазый": 1},
            count_substrings("C:/Users/V/PycharmProjects/pythonProject6/input/substrings_in1.txt", ["Карминовый", "Некрасивый", "белоглазый"])
        )
        self.assertEqual(
            {"--": 4, "ее": 2, "животное": 2, ".": 2},
            count_substrings("C:/Users/V/PycharmProjects/pythonProject6/input/substrings_in1.txt", ["--", "ее", "животное", "."])
        )
        self.assertEqual(
            {"Карминовый": 2, "Некрасивый": 2, "белоглазый": 1},
            count_substrings("C:/Users/V/PycharmProjects/pythonProject6/input/substrings_in1.txt", ["Карминовый", "Некрасивый", "белоглазый"])
        )
