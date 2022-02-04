# CPE 101-01
# LAB 5: Map Function Tests
# Name: Joshua Smith
# Section: 07

import unittest
from map import *
class TestPoly(unittest.TestCase):
    #do not delete this part, use this to comapre two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2, 3)

    def test_cube_all(self):
        # Test cube_all, which cubes each element in a list
        self.assertListEqual(cube_all([0, 1, 2, 3, 4]), [0, 1, 8, 27, 64])
        self.assertListEqual(cube_all([]), [])
        self.assertListEqual(cube_all([-2, -6, -1]), [-8, -216, -1])
        self.assertListEqual(cube_all([-5, 5, 4]), [-125, 125, 64])

    def test_add_n_to_all(self):
        # Test add_n_to_all, which adds n to each element in a list
        self.assertListEqual(add_n_to_all([0, 1, 2, 3, 4, 5], 10), [10, 11, 12, 13, 14, 15])
        self.assertListEqual(add_n_to_all([-14, 14, 3, 13], -5), [-19, 9, -2, 8])
        self.assertListEqual(add_n_to_all([], 12342354), [])
        self.assertListEqual(add_n_to_all([4, 6, 1], -4), [0, 2, -3])

    def test_div_by_5_all(self):
        # Test div_by_5_all, which checks if each element is divisible by 5
        self.assertListEqual(div_by_5_all([0, -5, 10, -15, 20]), [True] * 5)
        self.assertListEqual(div_by_5_all([]), [])
        self.assertListEqual(div_by_5_all([-4, -3, 154, 2]), [False] * 4)
        self.assertListEqual(div_by_5_all([51, 24, 25, -125, 0]), [False] * 2 + [True] * 3)


if __name__ == '__main__':
    unittest.main()
