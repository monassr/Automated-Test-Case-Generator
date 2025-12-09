"""
Additional Coverage Tests for DateConverter.py
Targets remaining uncovered lines to push coverage above 85%
Focus: DateTime formats, AM/PM handling, and edge cases
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DateConverter import (
    DateFormats,
    get_python_format,
    convert_between_formats,
    convert_date_format
)


class TestDateTimeFormats(unittest.TestCase):
    """Test DateTime format conversions with time components"""

    def test_datetime_with_am_pm_basic(self):
        """Test basic datetime format with AM/PM"""
        # Test conversion WITH time component
        # This should test the AM/PM handling code around line 155-157
        result = convert_between_formats(
            "2024-12-07, 09:30am",
            "D_YYYYMMDDHHMMA",
            "S_YYYYMMDDHHMMA"
        )
        self.assertEqual(result, "2024/12/07, 09:30am")

    def test_datetime_pm_conversion(self):
        """Test PM time conversion"""
        result = convert_between_formats(
            "2024-12-07, 02:45pm",
            "D_YYYYMMDDHHMMA",
            "S_DDMMYYYYHHMMA"
        )
        self.assertEqual(result, "07/12/2024, 02:45pm")

    def test_datetime_with_seconds_am(self):
        """Test datetime with seconds and AM"""
        result = convert_between_formats(
            "2024-12-07, 08:15:30am",
            "D_YYYYMMDDHHMMSSA",
            "S_YYYYMMDDHHMMSSA"
        )
        self.assertEqual(result, "2024/12/07, 08:15:30am")

    def test_datetime_with_seconds_pm(self):
        """Test datetime with seconds and PM"""
        result = convert_between_formats(
            "07-12-2024, 11:59:59pm",
            "D_DDMMYYYYHHMMSSA",
            "S_DDMMYYYYHHMMSSA"
        )
        self.assertEqual(result, "07/12/2024, 11:59:59pm")

    def test_datetime_midnight(self):
        """Test midnight time (12:00am)"""
        result = convert_between_formats(
            "2024-12-07, 12:00am",
            "D_YYYYMMDDHHMMA",
            "S_YYYYMMDDHHMMA"
        )
        self.assertIsNotNone(result)

    def test_datetime_noon(self):
        """Test noon time (12:00pm)"""
        result = convert_between_formats(
            "2024-12-07, 12:00pm",
            "D_YYYYMMDDHHMMA",
            "S_YYYYMMDDHHMMA"
        )
        self.assertIsNotNone(result)


class TestTextMonthFormats(unittest.TestCase):
    """Test all text month format variations"""

    def test_all_month_names(self):
        """Test conversion with all 12 month names"""
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for i, month in enumerate(months, 1):
            date_str = f"2024-{month}-15"
            result = convert_between_formats(date_str, "D_YYYYMMDD_N", "D_YYYYMMDD")
            self.assertIsNotNone(result, f"Failed for month {month}")
            self.assertIn(f"{i:02d}", result)

    def test_text_month_yy_formats(self):
        """Test 2-digit year with text month"""
        result = convert_between_formats("24-Jan-15", "D_YYMMDD_N", "D_YYYYMMDD")
        self.assertEqual(result, "2024-01-15")

    def test_text_month_dd_first(self):
        """Test day-first format with text month"""
        result = convert_between_formats("15-Dec-24", "D_DDMMyy_N", "D_YYYYMMDD")
        self.assertEqual(result, "2024-12-15")

    def test_slash_text_month_formats(self):
        """Test slash separator with text months"""
        result = convert_between_formats("2024/Nov/05", "S_YYYYMMDD_N", "D_YYYYMMDD")
        self.assertEqual(result, "2024-11-05")

        result = convert_between_formats("05/Nov/2024", "S_DDMMYYYY_N", "S_YYYYMMDD")
        self.assertEqual(result, "2024/11/05")


class TestTwoDigitYearFormats(unittest.TestCase):
    """Test 2-digit year handling across all formats"""

    def test_yy_to_yyyy_conversion(self):
        """Test 2-digit to 4-digit year conversion"""
        result = convert_between_formats("24-12-07", "D_YYMMDD", "D_YYYYMMDD")
        self.assertEqual(result, "2024-12-07")

    def test_yyyy_to_yy_conversion(self):
        """Test 4-digit to 2-digit year conversion"""
        result = convert_between_formats("2024-12-07", "D_YYYYMMDD", "D_YYMMDD")
        self.assertEqual(result, "24-12-07")

    def test_yy_slash_format(self):
        """Test 2-digit year with slash separator"""
        result = convert_between_formats("24/12/07", "S_YYMMDD", "S_YYYYMMDD")
        self.assertEqual(result, "2024/12/07")

    def test_yy_dd_first(self):
        """Test 2-digit year with day-first format"""
        result = convert_between_formats("07-12-24", "D_DDMMyy", "D_YYYYMMDD")
        self.assertEqual(result, "2024-12-07")

    def test_yy_with_text_month(self):
        """Test 2-digit year with text month"""
        result = convert_between_formats("24-Dec-07", "D_YYMMDD_N", "D_YYYYMMDD")
        self.assertEqual(result, "2024-12-07")


class TestFormatCombinations(unittest.TestCase):
    """Test various format combinations"""

    def test_dash_to_slash_all_variants(self):
        """Test conversion from dash to slash formats"""
        test_cases = [
            ("2024-12-07", "D_YYYYMMDD", "S_YYYYMMDD", "2024/12/07"),
            ("07-12-2024", "D_DDMMYYYY", "S_DDMMYYYY", "07/12/2024"),
            ("24-12-07", "D_YYMMDD", "S_YYMMDD", "24/12/07"),
        ]

        for date_str, from_fmt, to_fmt, expected in test_cases:
            result = convert_between_formats(date_str, from_fmt, to_fmt)
            self.assertEqual(result, expected)

    def test_slash_to_dash_all_variants(self):
        """Test conversion from slash to dash formats"""
        test_cases = [
            ("2024/12/07", "S_YYYYMMDD", "D_YYYYMMDD", "2024-12-07"),
            ("07/12/2024", "S_DDMMYYYY", "D_DDMMYYYY", "07-12-2024"),
            ("24/12/07", "S_YYMMDD", "D_YYMMDD", "24-12-07"),
        ]

        for date_str, from_fmt, to_fmt, expected in test_cases:
            result = convert_between_formats(date_str, from_fmt, to_fmt)
            self.assertEqual(result, expected)

    def test_same_format_conversion(self):
        """Test conversion to same format (should work)"""
        result = convert_between_formats("2024-12-07", "D_YYYYMMDD", "D_YYYYMMDD")
        self.assertEqual(result, "2024-12-07")


class TestExceptionPaths(unittest.TestCase):
    """Test exception handling paths"""

    def test_type_error_handling(self):
        """Test TypeError exception path"""
        # Pass integer instead of string
        result = convert_between_formats(20241207, "D_YYYYMMDD", "S_DDMMYYYY")
        self.assertIsNone(result)

    def test_attribute_error_handling(self):
        """Test AttributeError exception path"""
        # Pass object without expected attributes
        result = convert_between_formats("2024-12-07", None, "S_DDMMYYYY")
        self.assertIsNone(result)

    def test_malformed_date_string(self):
        """Test with malformed date strings"""
        malformed_dates = [
            "2024-13-45",  # Invalid month and day
            "abcd-ef-gh",  # Non-numeric
            "2024-12",  # Incomplete
            "2024/12-07",  # Mixed separators
        ]

        for date_str in malformed_dates:
            result = convert_between_formats(date_str, "D_YYYYMMDD", "S_DDMMYYYY")
            self.assertIsNone(result)


class TestBoundaryDates(unittest.TestCase):
    """Test boundary conditions for dates"""

    def test_year_1(self):
        """Test year 1 (minimum valid year)"""
        result = convert_between_formats("0001-01-01", "D_YYYYMMDD", "S_DDMMYYYY")
        self.assertIsNotNone(result)

    def test_year_9999(self):
        """Test year 9999 (maximum valid year)"""
        result = convert_between_formats("9999-12-31", "D_YYYYMMDD", "S_DDMMYYYY")
        self.assertIsNotNone(result)

    def test_all_12_months_last_day(self):
        """Test last day of each month"""
        last_days = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        for month, last_day in last_days.items():
            date_str = f"2023-{month:02d}-{last_day:02d}"
            result = convert_between_formats(date_str, "D_YYYYMMDD", "S_DDMMYYYY")
            self.assertIsNotNone(result)

    def test_leap_year_variations(self):
        """Test various leap year scenarios"""
        leap_years = [2020, 2024, 2000, 1600]
        non_leap_years = [2021, 2023, 1900, 2100]

        for year in leap_years:
            date_str = f"{year}-02-29"
            result = convert_between_formats(date_str, "D_YYYYMMDD", "S_DDMMYYYY")
            self.assertIsNotNone(result, f"Feb 29 should be valid for leap year {year}")

        for year in non_leap_years:
            date_str = f"{year}-02-29"
            result = convert_between_formats(date_str, "D_YYYYMMDD", "S_DDMMYYYY")
            self.assertIsNone(result, f"Feb 29 should be invalid for non-leap year {year}")


class TestConvertDateFormatInterface(unittest.TestCase):
    """Test the alternative convert_date_format interface"""

    def test_both_enums(self):
        """Test with both parameters as enums"""
        result = convert_date_format(
            "2024-12-07",
            DateFormats.D_YYYYMMDD,
            DateFormats.S_DDMMYYYY
        )
        self.assertEqual(result, "07/12/2024")

    def test_both_strings(self):
        """Test with both parameters as strings"""
        result = convert_date_format(
            "2024-12-07",
            "D_YYYYMMDD",
            "S_DDMMYYYY"
        )
        self.assertEqual(result, "07/12/2024")

    def test_first_enum_second_string(self):
        """Test with first as enum, second as string"""
        result = convert_date_format(
            "2024-12-07",
            DateFormats.D_YYYYMMDD,
            "S_DDMMYYYY"
        )
        self.assertEqual(result, "07/12/2024")

    def test_first_string_second_enum(self):
        """Test with first as string, second as enum"""
        result = convert_date_format(
            "2024-12-07",
            "D_YYYYMMDD",
            DateFormats.S_DDMMYYYY
        )
        self.assertEqual(result, "07/12/2024")


class TestAllDateFormatsEnum(unittest.TestCase):
    """Ensure all DateFormats enum values can be used"""

    def test_all_enum_values_work(self):
        """Test that all DateFormats can be used in conversions"""
        # Test a sample from each category
        test_dates = {
            "D_YYYYMMDD": "2024-12-07",
            "D_DDMMYYYY": "07-12-2024",
            "D_YYMMDD": "24-12-07",
            "D_DDMMyy": "07-12-24",
            "S_YYYYMMDD": "2024/12/07",
            "S_DDMMYYYY": "07/12/2024",
            "S_YYMMDD": "24/12/07",
            "S_DDMMyy": "07/12/24",
        }

        for fmt_name, date_str in test_dates.items():
            result = convert_between_formats(date_str, fmt_name, "D_YYYYMMDD")
            self.assertIsNotNone(result, f"Format {fmt_name} should work")


if __name__ == '__main__':
    unittest.main(verbosity=2)