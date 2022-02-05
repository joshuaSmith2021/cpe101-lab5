# CPE 101-01
# LAB 5: Nested Function Tests
# Name: Joshua Smith
# Section: 07

import unittest
from nested import product


class TestPoly(unittest.TestCase):
    # do not delete this part, use this to comapre two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2, 3)

    def test_product(self):
        # Testing product, which multiplies inner lists
        self.assertListEqual(product([[1, 2], [2, 3, 4], [-2, 5]]),
                             [2, 24, -10])

        self.assertListEqual(product([[0, 1, 4, 6, 2, 5, 2, 6, 2],
                                      [-1, 100], [14]]),
                             [0, -100, 14])

        self.assertListEqual(product([[-3] * 3, [5] * 3, [14] * 2]),
                             [-27, 125, 196])


if __name__ == '__main__':
    unittest.main()
