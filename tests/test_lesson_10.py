from Lesson_10 import *
import unittest


class Test(unittest.TestCase):
    def test_can_build_from(self):
        self.assertEqual(False, can_build_from([], "foo"))
        self.assertEqual(True, can_build_from(['a', 'b', 'o'], "baobab"))
        self.assertEqual(False, can_build_from(['a', 'm', 'r'], "Marat"))

    def test_has_anagrams(self):
        self.assertEqual(False, has_anagrams([]))
        self.assertEqual(True, has_anagrams(["рот", "свет", "тор"]))
        self.assertEqual(False, has_anagrams(["рот", "свет", "код", "дверь"]))
        self.assertEqual(False, has_anagrams(["поле", "полено"]))
        self.assertEqual(True, has_anagrams(["лунь", "нуль"]))

    def test_find_sum_of_two(self):
        n = 10000000
        my_list = [0] * n
        my_list[1000] = 2
        my_list[n - 1] = 3

        self.assertEqual(
            (1000, n - 1),
            find_sum_of_two(my_list, 5)
        )
        # self.assertEqual(
        #     (-1, -1),
        #     find_sum_of_two([], 1)
        # )
        # self.assertEqual(
        #     (0, 2),
        #     find_sum_of_two([1, 2, 3], 4)
        # )
        # self.assertEqual(
        #     (-1, -1),
        #     find_sum_of_two([1, 2, 3], 6)
        # )
        # self.assertEqual(
        #     (2, 3),
        #     find_sum_of_two([1, 2, 3, 3], 6)
        # )
        # self.assertEqual(
        #     (0, 2),
        #     find_sum_of_two([6, 2, 3, 6], 9)
        # )
        # self.assertEqual(
        #     (0, 3),
        #     find_sum_of_two([6, 2, 3, 6], 12)
        # )