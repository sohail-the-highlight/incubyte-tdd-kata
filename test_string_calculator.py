import unittest
from string_calculator import add, NegativeNumberException

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers_comma_delimited(self):
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers_comma_delimited(self):
        self.assertEqual(add("1,2,3,4,5"), 15)

    def test_newline_and_comma_delimiters(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_custom_delimiter_with_different_char(self):
        self.assertEqual(add("//|\n2|3|4"), 9)

    def test_negative_number_throws_exception(self):
        with self.assertRaises(NegativeNumberException) as context:
            add("1,-2")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2")

    def test_multiple_negatives_throws_exception(self):
        with self.assertRaises(NegativeNumberException) as context:
            add("2,-4,3,-5")
        self.assertEqual(str(context.exception), "negative numbers not allowed -4,-5")

if __name__ == '__main__':
    unittest.main()
