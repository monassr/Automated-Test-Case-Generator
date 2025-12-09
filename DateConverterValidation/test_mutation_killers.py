"""
Additional tests specifically to kill survived mutants
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DateConverter import DateConverter


class TestMutationKillers(unittest.TestCase):
    """Tests designed to kill common mutants"""

    def setUp(self):
        self.converter = DateConverter()

    def test_exact_month_boundaries(self):
        """Kill month boundary mutants (< to <=, > to >=)"""
        # Month = 1 (min valid)
        self.assertEqual(self.converter.convert_date("2024-01-15"), "15/01/2024")

        # Month = 12 (max valid)
        self.assertEqual(self.converter.convert_date("2024-12-15"), "15/12/2024")

        # Month = 0 (invalid)
        with self.assertRaises(ValueError):
            self.converter.convert_date("2024-00-15")

        # Month = 13 (invalid)
        with self.assertRaises(ValueError):
            self.converter.convert_date("2024-13-15")

    def test_exact_day_boundaries(self):
        """Kill day boundary mutants"""
        self.assertEqual(self.converter.convert_date("2024-06-01"), "01/06/2024")
        self.assertEqual(self.converter.convert_date("2024-06-31"), "31/06/2024")

        with self.assertRaises(ValueError):
            self.converter.convert_date("2024-06-00")

        with self.assertRaises(ValueError):
            self.converter.convert_date("2024-06-32")

    def test_logical_operator_mutations(self):
        """Kill OR/AND mutations"""
        # Test each condition independently
        with self.assertRaises(ValueError):
            self.converter.convert_date("2024-00-15")  # month < 1

        with self.assertRaises(ValueError):
            self.converter.convert_date("2024-13-15")  # month > 12

    def test_exact_format_output(self):
        """Kill format string mutations"""
        result = self.converter.convert_date("2024-06-15")

        self.assertEqual(result, "15/06/2024")
        self.assertEqual(result[2], '/')
        self.assertEqual(result[5], '/')
        self.assertEqual(len(result), 10)

        parts = result.split('/')
        self.assertEqual(len(parts), 3)
        self.assertEqual(len(parts[0]), 2)
        self.assertEqual(len(parts[1]), 2)
        self.assertEqual(len(parts[2]), 4)

    def test_strip_functionality(self):
        """Kill strip() mutation"""
        result1 = self.converter.convert_date("2024-06-15")
        result2 = self.converter.convert_date(" 2024-06-15")
        result3 = self.converter.convert_date("2024-06-15 ")
        result4 = self.converter.convert_date(" 2024-06-15 ")

        self.assertEqual(result1, result2)
        self.assertEqual(result1, result3)
        self.assertEqual(result1, result4)

    def test_empty_and_none_inputs(self):
        """Kill None/empty check mutations"""
        with self.assertRaises((ValueError, TypeError)):
            self.converter.convert_date(None)

        with self.assertRaises(ValueError):
            self.converter.convert_date("")

        with self.assertRaises(ValueError):
            self.converter.convert_date("   ")

    def test_regex_pattern_mutations(self):
        """Kill regex pattern mutations"""
        # Valid format
        self.assertIsNotNone(self.converter.convert_date("2024-06-15"))

        # Invalid formats
        with self.assertRaises(ValueError):
            self.converter.convert_date("20240615")  # No separators

        with self.assertRaises(ValueError):
            self.converter.convert_date("2024/06/15")  # Wrong separator

        with self.assertRaises(ValueError):
            self.converter.convert_date("24-06-15")  # Short year

    def test_int_conversion_mutations(self):
        """Kill int() conversion mutations"""
        result = self.converter.convert_date("2024-06-15")
        parts = result.split('/')

        # Verify these are valid integers when extracted
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        self.assertEqual(day, 15)
        self.assertEqual(month, 6)
        self.assertEqual(year, 2024)


if __name__ == '__main__':
    unittest.main(verbosity=2)