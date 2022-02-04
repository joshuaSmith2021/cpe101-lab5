# CPE 101-01
# LAB 5: Filter Function Tests
# Name: Joshua Smith
# Section: 07

import unittest
from filter import *
class TestPoly(unittest.TestCase):
    #do not delete this part, use this to comapre two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2, 3)

    def test_are_even(self):
        # Test are_even, which finds even numbers in list
        self.assertListEqual(are_even(range(10)), [0, 2, 4, 6, 8])
        self.assertListEqual(are_even(range(-10, 0)), [-10, -8, -6, -4, -2])
        self.assertListEqual(are_even([4, 7, 3, 7, 12, -14, -13]), [4, 12, -14])

    def test_remove_duplicates(self):
        # Test remove_duplicates, which removes duplicates from a list
        self.assertListEqual(remove_duplicates([0, 1, 2, 2, 3, 4, 5, 6, 1]), [0, 1, 2, 3, 4, 5, 6])
        self.assertListEqual(remove_duplicates([None, 'wow', 'WOW', 0, None, 1, 2, 'WOW', None]), [None, 'wow', 'WOW', 0, 1, 2])
        self.assertListEqual(remove_duplicates(['abcefgh', 0, 'abcdefgh']))

    def test_are_divisible_by_n(self):
        # Test are_divisible_by_n, which tests if numbers are divisible by n
        self.assertListEqual(are_divisible_by_n(range(100), 27), [0, 27, 54, 81])
        self.assertListEqual(are_divisible_by_n(range(-100, 0), 39), [-78, -39])
        self.assertListEqual(are_divisible_by_n(range(10), 2), [0, 2, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()
