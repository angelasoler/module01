import unittest

from array2D import slice_me


class TestBMIFunctions(unittest.TestCase):
    def test_pdf_test(self):
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
            ]
        ret1 = slice_me(family, 0, 2)
        ret2 = slice_me(family, 1, -2)
        expected1 = [[1.8, 78.4], [2.15, 102.7]]
        expected2 = [[2.15, 102.7]]
        self.assertEqual(ret1, expected1)
        self.assertEqual(ret2, expected2)

    def test_invalid_types(self):
        family = [
            [[1.80, 78.4]],
            [[2.15, 102.7]],
            [[2.10, 98.5]],
            [[1.88, 75.2]]
            ]
        with self.assertRaises(Exception):
            slice_me(family, 0, 2)

    def test_invalid_types2(self):
        family = [
            [[1.80, 78.4, ""]],
            [[2.15, 102.7]],
            [[2.10, 98.5]],
            [[1.88, 75.2]]
            ]
        with self.assertRaises(ValueError):
            slice_me(family, 0, 2)


if __name__ == "__main__":
    unittest.main()
