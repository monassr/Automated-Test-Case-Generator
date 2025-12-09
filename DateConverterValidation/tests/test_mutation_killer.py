"""
Mutation Killing Tests for DateConverter.py
"""

import unittest
import sys
import os

# Add parent directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Now import from DateConverter
from DateConverter import (
    DateFormats,
    is_leap_year,
    is_valid_date,
    convert_between_formats,
    convert_date_format,
    find_format_enum,
    get_format_example
)


class TestMutant96_MonthBoundary(unittest.TestCase):
    """
    SURVIVED MUTANT 96: month > 12 changed to month > 13
    Kill it by testing month = 13 specifically
    """

    def test_month_13_is_invalid(self):
        """Month 13 should be invalid - kills mutant 96"""
        self.assertFalse(is_valid_date(2024, 13, 1))

    def test_month_12_is_valid(self):
        """Month 12 should be valid"""
        self.assertTrue(is_valid_date(2024, 12, 1))

    def test_month_13_conversion_fails(self):
        """Conversion with month 13 should return None"""
        result = convert_between_formats("2024-13-01", "D_YYYYMMDD", "S_DDMMYYYY")
        self.assertIsNone(result)


class TestMutant155_159_161_FormatExamples(unittest.TestCase):
    """
    SURVIVED MUTANTS 155, 157, 158, 159, 160, 161
    These mutants modify the examples dictionary with "XX...XX"
    Kill them by asserting exact format of examples
    """

    def test_d_yyyymmdd_n_example_exact(self):
        """Mutant 155: D_YYYYMMDD_N example must not have XX prefix/suffix"""
        example = get_format_example("D_YYYYMMDD_N")
        self.assertEqual(example, "2024-Dec-07")
        self.assertNotIn("XX", example)

    def test_d_ddmmyyyy_n_example_exact(self):
        """Mutant 157: D_DDMMYYYY_N example must not have XX prefix/suffix"""
        example = get_format_example("D_DDMMYYYY_N")
        self.assertEqual(example, "07-Dec-2024")
        self.assertNotIn("XX", example)

    def test_d_yymmdd_example_exact(self):
        """Mutant 159: D_YYMMDD example must not have XX prefix/suffix"""
        example = get_format_example("D_YYMMDD")
        self.assertEqual(example, "24-12-07")
        self.assertNotIn("XX", example)

    def test_s_yymmdd_example_exact(self):
        """Mutant 161: S_YYMMDD example must not have XX prefix/suffix"""
        example = get_format_example("S_YYMMDD")
        self.assertEqual(example, "24/12/07")
        self.assertNotIn("XX", example)

    def test_d_yymmdd_key_not_modified(self):
        """Mutant 158: D_YYMMDD key should exist, not XXD_YYMMDDXX"""
        example = get_format_example("D_YYMMDD")
        self.assertNotEqual(example, "Example not available")

    def test_s_yymmdd_key_not_modified(self):
        """Mutant 160: S_YYMMDD key should exist, not XXS_YYMMDDXX"""
        example = get_format_example("S_YYMMDD")
        self.assertNotEqual(example, "Example not available")

    def test_all_examples_no_xx_markers(self):
        """Ensure all examples don't have XX markers"""
        format_names = ["D_YYYYMMDD", "D_DDMMYYYY", "S_YYYYMMDD",
                       "S_DDMMYYYY", "D_YYYYMMDD_N", "D_DDMMYYYY_N",
                       "D_YYMMDD", "S_YYMMDD"]

        for fmt in format_names:
            example = get_format_example(fmt)
            self.assertNotIn("XX", example,
                           f"Format {fmt} should not have XX markers")


class TestMutant68_LeapYearException(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 68: return False changed to return True
    in is_leap_year exception handler
    Kill it by testing invalid year inputs
    """

    def test_invalid_year_string_not_leap(self):
        """Invalid year string should return False, not True"""
        self.assertFalse(is_leap_year("invalid"))
        self.assertFalse(is_leap_year("abcd"))
        self.assertFalse(is_leap_year(""))

    def test_none_year_not_leap(self):
        """None year should return False"""
        self.assertFalse(is_leap_year(None))

    def test_list_year_not_leap(self):
        """List year should return False"""
        self.assertFalse(is_leap_year([2020]))

    def test_dict_year_not_leap(self):
        """Dict year should return False"""
        self.assertFalse(is_leap_year({"year": 2020}))


class TestMutant77_LeapYearLogic(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 77: 'and' changed to 'or' in leap year logic
    (year % 4 == 0 and year % 100 != 0) changed to (year % 4 == 0 or year % 100 != 0)
    Kill it by testing century years
    """

    def test_century_non_leap_1900(self):
        """1900 is NOT a leap year (divisible by 100 but not 400)"""
        self.assertFalse(is_leap_year(1900))

    def test_century_non_leap_2100(self):
        """2100 is NOT a leap year"""
        self.assertFalse(is_leap_year(2100))

    def test_century_leap_2000(self):
        """2000 IS a leap year (divisible by 400)"""
        self.assertTrue(is_leap_year(2000))

    def test_normal_leap_2020(self):
        """2020 is a leap year (divisible by 4, not 100)"""
        self.assertTrue(is_leap_year(2020))

    def test_non_leap_2019(self):
        """2019 is NOT a leap year"""
        self.assertFalse(is_leap_year(2019))


class TestMutant86_ValidDateException(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 86: return False changed to return True
    in is_valid_date exception handler
    Kill it by testing invalid date inputs
    """

    def test_invalid_year_string(self):
        """Invalid year string should return False"""
        self.assertFalse(is_valid_date("invalid", 6, 15))

    def test_invalid_month_string(self):
        """Invalid month string should return False"""
        self.assertFalse(is_valid_date(2024, "invalid", 15))

    def test_invalid_day_string(self):
        """Invalid day string should return False"""
        self.assertFalse(is_valid_date(2024, 6, "invalid"))

    def test_none_values(self):
        """None values should return False"""
        self.assertFalse(is_valid_date(None, 6, 15))
        self.assertFalse(is_valid_date(2024, None, 15))
        self.assertFalse(is_valid_date(2024, 6, None))


class TestMutant87_YearBoundary(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 87: year < 1 changed to year <= 1
    Kill it by testing year = 1 specifically
    """

    def test_year_1_is_valid(self):
        """Year 1 should be valid"""
        self.assertTrue(is_valid_date(1, 6, 15))

    def test_year_0_is_invalid(self):
        """Year 0 should be invalid"""
        self.assertFalse(is_valid_date(0, 6, 15))

    def test_year_1_conversion_works(self):
        """Conversion with year 1 should work"""
        result = convert_between_formats("0001-06-15", "D_YYYYMMDD", "S_DDMMYYYY")
        self.assertIsNotNone(result)
        self.assertEqual(result, "15/06/0001")


class TestMutant90_YearUpperBoundary(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 90: year > 9999 changed to year > 10000
    Kill it by testing year = 10000 specifically
    """

    def test_year_10000_is_invalid(self):
        """Year 10000 should be invalid"""
        self.assertFalse(is_valid_date(10000, 6, 15))

    def test_year_9999_is_valid(self):
        """Year 9999 should be valid"""
        self.assertTrue(is_valid_date(9999, 6, 15))


class TestMutant91_YearLogic(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 91: year < 1 or year > 9999 changed to year < 1 and year > 9999
    Kill it by testing boundary years
    """

    def test_year_negative_is_invalid(self):
        """Negative year should be invalid"""
        self.assertFalse(is_valid_date(-1, 6, 15))

    def test_year_0_is_invalid(self):
        """Year 0 should be invalid"""
        self.assertFalse(is_valid_date(0, 6, 15))

    def test_year_10000_is_invalid(self):
        """Year 10000 should be invalid"""
        self.assertFalse(is_valid_date(10000, 6, 15))


class TestMutant92_YearReturn(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 92: return False changed to return True
    when year is out of range
    Kill it by testing invalid years
    """

    def test_year_out_of_range_returns_false(self):
        """Out of range year should return False"""
        self.assertFalse(is_valid_date(0, 6, 15))
        self.assertFalse(is_valid_date(10000, 6, 15))
        self.assertFalse(is_valid_date(-100, 6, 15))


class TestMutant143_OutputFormatNone(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 143: output_format.name changed to None
    Kill it by using convert_date_format with enum inputs
    """

    def test_convert_with_both_enums(self):
        """Conversion with both enums should work"""
        result = convert_date_format(
            "2024-12-07",
            DateFormats.D_YYYYMMDD,
            DateFormats.S_DDMMYYYY
        )
        self.assertEqual(result, "07/12/2024")

    def test_convert_with_output_enum(self):
        """Conversion with output format as enum should work"""
        result = convert_date_format(
            "2024-12-07",
            "D_YYYYMMDD",
            DateFormats.S_DDMMYYYY
        )
        self.assertEqual(result, "07/12/2024")


class TestMutant144_FindFormatInvert(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 144: if not format_str changed to if format_str
    Kill it by testing empty string and valid string
    """

    def test_empty_string_returns_none(self):
        """Empty string should return None"""
        self.assertIsNone(find_format_enum(""))

    def test_none_returns_none(self):
        """None should return None"""
        self.assertIsNone(find_format_enum(None))

    def test_valid_string_returns_enum(self):
        """Valid string should return enum"""
        result = find_format_enum("D_YYYYMMDD")
        self.assertEqual(result, DateFormats.D_YYYYMMDD)


class TestMutant145_FindFormatValue(unittest.TestCase):
    """
    SUSPICIOUS MUTANT 145: fmt.value == format_str changed to fmt.value != format_str
    Kill it by searching by value
    """

    def test_find_by_value(self):
        """Finding by value should work correctly"""
        result = find_format_enum("yyyy-MM-dd")
        self.assertEqual(result, DateFormats.D_YYYYMMDD)

    def test_find_by_value_slash(self):
        """Finding slash format by value"""
        result = find_format_enum("dd/MM/yyyy")
        self.assertEqual(result, DateFormats.S_DDMMYYYY)


class TestMutant146_153_KeyValueMutations(unittest.TestCase):
    """
    SUSPICIOUS MUTANTS 146-153: Dictionary key/value mutations with XX
    Kill them by verifying exact examples
    """

    def test_all_standard_examples_exact_match(self):
        """Test all examples match exactly without XX"""
        expected = {
            "D_YYYYMMDD": "2024-12-07",
            "D_DDMMYYYY": "07-12-2024",
            "S_YYYYMMDD": "2024/12/07",
            "S_DDMMYYYY": "07/12/2024",
        }

        for fmt, expected_val in expected.items():
            actual = get_format_example(fmt)
            self.assertEqual(actual, expected_val,
                           f"{fmt} example should be exactly {expected_val}")
            self.assertNotIn("XX", actual)


class TestMutant41_42_43_DateTimeFormats(unittest.TestCase):
    """
    SUSPICIOUS MUTANTS 41, 42, 43: DateTime format strings modified
    Kill them by actually using these formats
    """

    def test_s_yyyymmddhhmmssa_format_exists(self):
        """S_YYYYMMDDHHMMSSA format should exist and work"""
        self.assertEqual(
            DateFormats.S_YYYYMMDDHHMMSSA.value,
            "yyyy/MM/dd, hh:mm:ssa"
        )

    def test_s_ddmmyyyyhhmmssa_format_exists(self):
        """S_DDMMYYYYHHMMSSA format should exist and work"""
        self.assertEqual(
            DateFormats.S_DDMMYYYYHHMMSSA.value,
            "dd/MM/yyyy, hh:mm:ssa"
        )


class TestEdgeCasesToKillMutants(unittest.TestCase):
    """Additional edge cases to ensure high mutation kill rate"""

    def test_month_boundaries_all(self):
        """Test all month boundaries"""
        self.assertFalse(is_valid_date(2024, 0, 15))
        for month in range(1, 13):
            self.assertTrue(is_valid_date(2024, month, 15))
        self.assertFalse(is_valid_date(2024, 13, 15))
        self.assertFalse(is_valid_date(2024, 14, 15))

    def test_day_boundaries(self):
        """Test day boundaries"""
        self.assertFalse(is_valid_date(2024, 6, 0))
        self.assertTrue(is_valid_date(2024, 6, 1))
        self.assertTrue(is_valid_date(2024, 6, 30))
        self.assertFalse(is_valid_date(2024, 6, 31))

    def test_february_boundaries(self):
        """Test February boundaries for leap and non-leap"""
        self.assertTrue(is_valid_date(2020, 2, 29))
        self.assertFalse(is_valid_date(2020, 2, 30))
        self.assertTrue(is_valid_date(2021, 2, 28))
        self.assertFalse(is_valid_date(2021, 2, 29))

    def test_conversion_with_invalid_dates(self):
        """Ensure invalid dates return None"""
        invalid_dates = [
            ("2024-13-01", "D_YYYYMMDD"),
            ("2024-02-30", "D_YYYYMMDD"),
            ("2024-06-31", "D_YYYYMMDD"),
            ("2021-02-29", "D_YYYYMMDD"),
        ]

        for date_str, fmt in invalid_dates:
            result = convert_between_formats(date_str, fmt, "S_DDMMYYYY")
            self.assertIsNone(result, f"{date_str} should be invalid")


if __name__ == '__main__':
    unittest.main(verbosity=2)