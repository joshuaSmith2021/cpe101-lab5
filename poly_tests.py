# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Joshua Smith
# Section: 07

import unittest
from poly import *
class TestPoly(unittest.TestCase):
    #do not delete this part, use this to comapre two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2, 3)

    def test_poly_add2(self):
        # Testing poly_add2, which adds two second-degree polynomials
        self.assertListEqual(poly_add2([1, 5, 6], [4, 2, -7]), [5, 7, -1])
        self.assertListEqual(poly_add2([14, 64, 1], [-6, 13, 4]), [8, 77, 5])
        self.assertListEqual(poly_add2([0, 0, 0], [-1, 1, -1]), [-1, 1, -1])

    def test_poly_mult2(self):
        # Testing poly_mult2, which multiplies two second-degree polynomials
        self.assertListEqual(poly_mult2([2, 5, 2], [-6, 2, 0]), [-12, -26, -2, 4, 0])
        self.assertListEqual(poly_mult2([5, 6, -2], [-7, 0, -7]), [-35, -42, -21, -42, 14])
        self.assertListAlmostEqual(poly_mult2([1/14, 1/7, 4.14], [1, 1, 1]), [0.071428, 0.2142857, 4.35428, 4.28285714, 4.14])


if __name__ == '__main__':
    unittest.main()
