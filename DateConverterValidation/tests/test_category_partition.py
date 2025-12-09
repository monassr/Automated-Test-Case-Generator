"""
Test execution for Category-Partition Test Set
Executes systematically generated test cases based on parameter categories and constraints
"""

import pytest
import sys
import csv
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from DateConverter import convert_between_formats, is_valid_date, is_leap_year

class TestCategoryPartitionSet:
    """Execute category-partition test cases"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load test cases from CSV"""
        csv_path = Path(__file__).parent.parent / "CategoryPartitionTestSet.csv"
        self.test_cases = []
        self.execution_times = []

        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.test_cases = list(reader)
                print(f"\nLoaded {len(self.test_cases)} category-partition test cases")
        except FileNotFoundError:
            print(f"Warning: {csv_path} not found. Run Generate_Category_Partition_Test_Set.py first.")
            self.test_cases = []

    def test_31_day_months_valid(self):
        """Test Category: Months with 31 days (Jan, Mar, May, Jul, Aug, Oct, Dec)"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == '31-day months valid']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected = None if tc['expected_output'] == 'None' else tc['expected_output']
            assert result == expected, \
                f"{tc['test_id']} failed: {tc['description']}"

    def test_30_day_months_valid(self):
        """Test Category: Months with 30 days (Apr, Jun, Sep, Nov)"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == '30-day months valid']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected = None if tc['expected_output'] == 'None' else tc['expected_output']
            assert result == expected, \
                f"{tc['test_id']} failed: {tc['description']}"

    def test_february_leap_year(self):
        """Test Category: February in leap years (29 days valid)"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == 'Feb in leap year valid']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected = None if tc['expected_output'] == 'None' else tc['expected_output']
            assert result == expected, \
                f"{tc['test_id']} failed: Leap year {tc['description']}"

    def test_february_non_leap_valid(self):
        """Test Category: February in non-leap years (28 days valid)"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == 'Feb non-leap valid']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected = None if tc['expected_output'] == 'None' else tc['expected_output']
            assert result == expected, \
                f"{tc['test_id']} failed: {tc['description']}"

    def test_february_non_leap_invalid(self):
        """Test Category: February 29 in non-leap years (invalid)"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == 'Feb 29 non-leap invalid']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            assert result is None, \
                f"{tc['test_id']} should be invalid: {tc['description']}"

    def test_century_leap_year_rules(self):
        """Test Category: Century year leap year rules (divisible by 400)"""
        # Constraint: 2000 is leap year (divisible by 400)
        tests = [tc for tc in self.test_cases if tc.get('constraint') == '2000 is leap year']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            assert result is not None, \
                f"{tc['test_id']} should be valid: 2000 is a leap year"

    def test_century_non_leap_year(self):
        """Test Category: Century years NOT leap (divisible by 100 but not 400)"""
        # Constraint: 1900 is NOT leap year
        tests = [tc for tc in self.test_cases if tc.get('constraint') == '1900 not leap year']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            assert result is None, \
                f"{tc['test_id']} should be invalid: 1900 is not a leap year"

    def test_invalid_day_for_month(self):
        """Test Category: Invalid day numbers for specific months"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == 'Invalid day for month']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            assert result is None, \
                f"{tc['test_id']} should be invalid: {tc['description']}"

    def test_text_month_conversion(self):
        """Test Category: Text month name to numeric month conversion"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == 'Text to numeric month']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected = None if tc['expected_output'] == 'None' else tc['expected_output']
            assert result == expected, \
                f"{tc['test_id']} failed: {tc['description']}"

    def test_two_digit_year_conversion(self):
        """Test Category: Two-digit to four-digit year conversion"""
        tests = [tc for tc in self.test_cases if tc.get('constraint') == '2-digit to 4-digit year']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected = None if tc['expected_output'] == 'None' else tc['expected_output']
            assert result == expected, \
                f"{tc['test_id']} failed: {tc['description']}"

    # Additional specific constraint tests

    def test_constraint_months_31_days_boundary(self):
        """Constraint: All 31-day months should accept day 31"""
        months_31 = ["01", "03", "05", "07", "08", "10", "12"]

        for month in months_31:
            result = convert_between_formats(
                f"2024-{month}-31",
                "D_YYYYMMDD",
                "S_DDMMYYYY"
            )
            assert result is not None, \
                f"Month {month} should have 31 days"

    def test_constraint_months_30_days_boundary(self):
        """Constraint: 30-day months should reject day 31"""
        months_30 = ["04", "06", "09", "11"]

        for month in months_30:
            # Day 30 should be valid
            result = convert_between_formats(
                f"2024-{month}-30",
                "D_YYYYMMDD",
                "S_DDMMYYYY"
            )
            assert result is not None, \
                f"Month {month} should accept day 30"

            # Day 31 should be invalid
            result = convert_between_formats(
                f"2024-{month}-31",
                "D_YYYYMMDD",
                "S_DDMMYYYY"
            )
            assert result is None, \
                f"Month {month} should reject day 31"

    def test_constraint_leap_year_calculation(self):
        """Constraint: Leap year calculation rules"""
        # Rule 1: Divisible by 4 = leap year
        assert is_leap_year(2024) == True
        assert is_leap_year(2020) == True

        # Rule 2: Divisible by 100 = NOT leap year (unless...)
        assert is_leap_year(1900) == False
        assert is_leap_year(2100) == False

        # Rule 3: Divisible by 400 = leap year
        assert is_leap_year(2000) == True
        assert is_leap_year(2400) == True

        # Non-leap years
        assert is_leap_year(2019) == False
        assert is_leap_year(2021) == False
        assert is_leap_year(2023) == False

    def test_constraint_february_leap_vs_nonleap(self):
        """Constraint: February behavior in leap vs non-leap years"""
        # Leap years: Feb 29 valid
        leap_years = [2020, 2024, 2000, 2400]
        for year in leap_years:
            result = convert_between_formats(
                f"{year}-02-29",
                "D_YYYYMMDD",
                "S_DDMMYYYY"
            )
            assert result is not None, \
                f"{year} is leap year, Feb 29 should be valid"

        # Non-leap years: Feb 29 invalid
        non_leap_years = [2019, 2021, 2023, 1900, 2100]
        for year in non_leap_years:
            result = convert_between_formats(
                f"{year}-02-29",
                "D_YYYYMMDD",
                "S_DDMMYYYY"
            )
            assert result is None, \
                f"{year} is not leap year, Feb 29 should be invalid"

    def test_constraint_separator_consistency(self):
        """Constraint: Separator type preserved in format category"""
        # Dash separator formats
        dash_formats = [
            ("2024-06-15", "D_YYYYMMDD", "D_DDMMYYYY", "15-06-2024"),
            ("15-06-2024", "D_DDMMYYYY", "D_YYYYMMDD", "2024-06-15"),
        ]

        for date_input, in_fmt, out_fmt, expected in dash_formats:
            result = convert_between_formats(date_input, in_fmt, out_fmt)
            assert result == expected

        # Slash separator formats
        slash_formats = [
            ("2024/06/15", "S_YYYYMMDD", "S_DDMMYYYY", "15/06/2024"),
            ("15/06/2024", "S_DDMMYYYY", "S_YYYYMMDD", "2024/06/15"),
        ]

        for date_input, in_fmt, out_fmt, expected in slash_formats:
            result = convert_between_formats(date_input, in_fmt, out_fmt)
            assert result == expected

    def test_constraint_month_name_abbreviations(self):
        """Constraint: Standard month name abbreviations"""
        month_mapping = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        for month_name, month_num in month_mapping.items():
            # Text to numeric
            result = convert_between_formats(
                f"2024-{month_name}-15",
                "D_YYYYMMDD_N",
                "D_YYYYMMDD"
            )
            assert result == f"2024-{month_num}-15", \
                f"{month_name} should convert to {month_num}"

    def test_constraint_year_range_boundaries(self):
        """Constraint: Valid year range is 1-9999"""
        # Lower boundary
        assert convert_between_formats("0001-01-01", "D_YYYYMMDD", "S_DDMMYYYY") == "01/01/0001"
        assert convert_between_formats("0000-01-01", "D_YYYYMMDD", "S_DDMMYYYY") is None

        # Upper boundary
        assert convert_between_formats("9999-12-31", "D_YYYYMMDD", "S_DDMMYYYY") == "31/12/9999"
        # Note: 10000 would overflow the format, handled by validation

    def test_constraint_day_range_per_category(self):
        """Constraint: Day range varies by month category"""
        test_cases = [
            # 31-day months
            ("2024-01-31", "D_YYYYMMDD", True, "January has 31 days"),
            ("2024-01-32", "D_YYYYMMDD", False, "January doesn't have 32 days"),

            # 30-day months
            ("2024-04-30", "D_YYYYMMDD", True, "April has 30 days"),
            ("2024-04-31", "D_YYYYMMDD", False, "April doesn't have 31 days"),

            # February special cases
            ("2024-02-29", "D_YYYYMMDD", True, "Leap year Feb has 29 days"),
            ("2023-02-29", "D_YYYYMMDD", False, "Non-leap Feb doesn't have 29 days"),
            ("2024-02-30", "D_YYYYMMDD", False, "February never has 30 days"),
        ]

        for date_input, fmt, should_be_valid, description in test_cases:
            result = convert_between_formats(date_input, fmt, "S_DDMMYYYY")
            if should_be_valid:
                assert result is not None, description
            else:
                assert result is None, description

@pytest.fixture(scope="session", autouse=True)
def print_execution_summary(request):
    """Print execution summary after all tests"""
    def finalizer():
        print("\n" + "="*60)
        print("CATEGORY-PARTITION TEST SET - EXECUTION COMPLETE")
        print("="*60)
    request.addfinalizer(finalizer)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])