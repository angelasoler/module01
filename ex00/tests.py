import unittest

from give_bmi import give_bmi, apply_limit

class TestBMIFunctions(unittest.TestCase):
    def test_valid_input(self):
        # Testa com listas válidas de mesmo tamanho
        weights = [70, 50, 90]
        heights = [1.75, 1.60, 1.80]
        expected_bmi = [22.86, 19.53, 27.78]
        result = give_bmi(weights, heights)
        self.assertEqual([round(b, 2) for b in result], expected_bmi)

    def test_apply_limit(self):
        # Testa valores acima e abaixo do limite
        values = [18.5, 22.0, 30.0]
        limit = 25
        expected = [False, False, True]
        result = apply_limit(values, limit)
        self.assertEqual(result, expected)

    def test_mismatched_list_sizes(self):
        # Testa listas de tamanhos diferentes
        weights = [70, 50]
        heights = [1.75]
        with self.assertRaises(AssertionError):
            give_bmi(weights, heights)

    def test_invalid_types(self):
        # Testa inputs com tipos inválidos
        weights = [70, "fifty", 90]
        heights = [1.75, 1.60, 1.80]
        with self.assertRaises(AssertionError):
            give_bmi(weights, heights)

    def test_empty_lists(self):
        # Testa listas vazias
        weights = []
        heights = []
        result = give_bmi(weights, heights)
        self.assertEqual(result, [])

    def test_apply_limit_empty_list(self):
        # Testa apply_limit com lista vazia
        values = []
        limit = 25
        result = apply_limit(values, limit)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
