from Lesson_9 import *
import unittest


class Test(unittest.TestCase):
    def test_merge_phone_books(self):
        self.assertEqual(
            {"Emergency": "112"},
            merge_phone_books({"Emergency": "112"}, {"Emergency": "112"})
        )
        self.assertEqual(
            {"Emergency": "112", "Police": "02"},
            merge_phone_books({"Emergency": "112"}, {"Emergency": "112", "Police": "02"})
        )
        self.assertEqual(
            {"Emergency": "112, 911", "Police": "02"},
            merge_phone_books({"Emergency": "112"}, {"Emergency": "911", "Police": "02"})
        )
        self.assertEqual(
            {"Emergency": "112, 911", "Fire department": "01", "Police": "02"},
            merge_phone_books(
                {"Emergency": "112", "Fire department": "01"},
                {"Emergency": "911", "Police": "02"}
            )
        )

    def test_find_cheapest_stuff(self):
        self.assertEqual(
            None,
            find_cheapest_stuff(
                {"Мария": ["печенье", 20.0], "Орео": ["печенье", 100.0]},
                "торт"
            )
        )
        self.assertEqual(
            "Мария",
            find_cheapest_stuff(
                {"Мария": ["печенье", 20.0], "Орео": ["печенье", 100.0]},
                "печенье"
            )
        )

    def test_extract_repeats(self):
        self.assertEqual(
            {},
            extract_repeats([])
        )
        self.assertEqual(
            {"a": 2},
            extract_repeats(["a", "b", "a"])
        )
        self.assertEqual(
            {},
            extract_repeats(["a", "b", "c"])
        )
