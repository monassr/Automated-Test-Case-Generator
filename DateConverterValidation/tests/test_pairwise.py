"""
Test execution for Pairwise (All-Pairs) Test Set
Tests combinatorial parameter interactions using pairwise testing technique
"""

import pytest
import sys
import csv
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from DateConverter import convert_between_formats

class TestPairwiseSet:
    """Execute pairwise combinatorial test cases"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load test cases from CSV"""
        csv_path = Path(__file__).parent.parent / "PairWiseInputSet.csv"
        self.test_cases = []
        self.execution_times = []

        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.test_cases = list(reader)
                print(f"\nLoaded {len(self.test_cases)} pairwise test cases")
        except FileNotFoundError:
            print(f"Warning: {csv_path} not found. Run Generate_Pair_Wise_Test_Set.py first.")
            self.test_cases = []

    def test_pairwise_typical_dates(self):
        """Test pairwise combinations of typical valid dates"""
        tests = [tc for tc in self.test_cases if tc.get('scenario') == 'typical' and tc.get('expected_valid') == 'True']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            assert result is not None, \
                f"{tc['test_id']} failed: {tc['description']}"

    def test_pairwise_leap_feb29(self):
        """Test pairwise combinations with leap year February 29"""
        tests = [tc for tc in self.test_cases if tc.get('scenario') == 'leap_feb29']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected_valid = tc.get('expected_valid') == 'True'
            if expected_valid:
                assert result is not None, \
                    f"{tc['test_id']} should be valid: {tc['description']}"
            else:
                assert result is None, \
                    f"{tc['test_id']} should be invalid: {tc['description']}"

    def test_pairwise_month_end(self):
        """Test pairwise combinations of month-end dates"""
        tests = [tc for tc in self.test_cases if tc.get('scenario') == 'month_end']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected_valid = tc.get('expected_valid') == 'True'
            if expected_valid:
                assert result is not None, \
                    f"{tc['test_id']} should be valid: {tc['description']}"
            else:
                assert result is None, \
                    f"{tc['test_id']} should be invalid: {tc['description']}"

    def test_pairwise_invalid_day(self):
        """Test pairwise combinations with invalid day values"""
        tests = [tc for tc in self.test_cases if tc.get('scenario') == 'invalid_day']

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

    def test_pairwise_invalid_month(self):
        """Test pairwise combinations with invalid month values"""
        tests = [tc for tc in self.test_cases if tc.get('scenario') == 'invalid_month']

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

    def test_pairwise_boundary_cases(self):
        """Test pairwise combinations of boundary values"""
        tests = [tc for tc in self.test_cases if tc.get('scenario') == 'boundary']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected_valid = tc.get('expected_valid') == 'True'
            if expected_valid:
                assert result is not None, \
                    f"{tc['test_id']} should be valid: {tc['description']}"
            else:
                assert result is None, \
                    f"{tc['test_id']} should be invalid: {tc['description']}"

    def test_pairwise_edge_cases(self):
        """Test specific edge cases from pairwise generation"""
        tests = [tc for tc in self.test_cases if tc.get('scenario') == 'edge_case']

        for tc in tests:
            start = time.time()
            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )
            self.execution_times.append(time.time() - start)

            expected_valid = tc.get('expected_valid') == 'True'
            if expected_valid:
                assert result is not None, \
                    f"{tc['test_id']} should be valid: {tc['description']}"
            else:
                assert result is None, \
                    f"{tc['test_id']} should be invalid: {tc['description']}"

    # Additional pairwise interaction tests

    def test_format_separator_interaction(self):
        """Test interaction between format types and separators"""
        # Dash formats should only work with dash separators
        assert convert_between_formats("2024-06-15", "D_YYYYMMDD", "S_DDMMYYYY") == "15/06/2024"
        assert convert_between_formats("2024/06/15", "D_YYYYMMDD", "S_DDMMYYYY") is None  # Wrong separator

        # Slash formats should only work with slash separators
        assert convert_between_formats("2024/06/15", "S_YYYYMMDD", "D_DDMMYYYY") == "15-06-2024"
        assert convert_between_formats("2024-06-15", "S_YYYYMMDD", "D_DDMMYYYY") is None  # Wrong separator

    def test_year_format_interaction(self):
        """Test interaction between 2-digit and 4-digit year formats"""
        # 2-digit year to 4-digit year
        assert convert_between_formats("24-06-15", "D_YYMMDD", "D_YYYYMMDD") == "2024-06-15"
        assert convert_between_formats("00-01-01", "D_YYMMDD", "D_YYYYMMDD") == "2000-01-01"
        assert convert_between_formats("99-12-31", "D_YYMMDD", "D_YYYYMMDD") == "1999-12-31"

        # Python's datetime: 00-68 -> 2000-2068, 69-99 -> 1969-1999
        assert convert_between_formats("68-01-01", "D_YYMMDD", "D_YYYYMMDD") == "2068-01-01"
        assert convert_between_formats("69-01-01", "D_YYMMDD", "D_YYYYMMDD") == "1969-01-01"
        assert convert_between_formats("70-01-01", "D_YYMMDD", "D_YYYYMMDD") == "1970-01-01"
    def test_month_day_interaction(self):
        """Test interaction between month values and valid day ranges"""
        # Each month type with its boundary days
        test_combinations = [
            # 31-day months with day 31
            ("2024-01-31", True),
            ("2024-03-31", True),
            ("2024-05-31", True),

            # 30-day months with day 30 (valid) and 31 (invalid)
            ("2024-04-30", True),
            ("2024-04-31", False),
            ("2024-06-30", True),
            ("2024-06-31", False),

            # February special cases
            ("2024-02-29", True),   # Leap year
            ("2023-02-29", False),  # Non-leap year
            ("2024-02-30", False),  # Never valid
        ]

        for date_str, should_be_valid in test_combinations:
            result = convert_between_formats(date_str, "D_YYYYMMDD", "S_DDMMYYYY")
            if should_be_valid:
                assert result is not None, f"{date_str} should be valid"
            else:
                assert result is None, f"{date_str} should be invalid"

    def test_year_month_leap_interaction(self):
        """Test interaction between year type (leap/non-leap) and February"""
        # Leap years with Feb 29
        leap_years = [2020, 2024, 2000, 2400]
        for year in leap_years:
            result = convert_between_formats(f"{year}-02-29", "D_YYYYMMDD", "S_DDMMYYYY")
            assert result is not None, f"{year} is leap year"

        # Non-leap years with Feb 29
        non_leap = [2019, 2021, 2023, 1900, 2100]
        for year in non_leap:
            result = convert_between_formats(f"{year}-02-29", "D_YYYYMMDD", "S_DDMMYYYY")
            assert result is None, f"{year} is not leap year"

    def test_format_order_interaction(self):
        """Test interaction between different date component ordering"""
        # YYYY-MM-DD to DD/MM/YYYY
        assert convert_between_formats("2024-06-15", "D_YYYYMMDD", "S_DDMMYYYY") == "15/06/2024"

        # DD-MM-YYYY to YYYY/MM/DD
        assert convert_between_formats("15-06-2024", "D_DDMMYYYY", "S_YYYYMMDD") == "2024/06/15"

        # YY-MM-DD to DD/MM/YYYY
        assert convert_between_formats("24-06-15", "D_YYMMDD", "S_DDMMYYYY") == "15/06/2024"

    def test_text_numeric_month_interaction(self):
        """Test interaction between text and numeric month representations"""
        month_tests = [
            ("2024-Jan-15", "D_YYYYMMDD_N", "2024-01-15", "D_YYYYMMDD"),
            ("15-Feb-2024", "D_DDMMYYYY_N", "15-02-2024", "D_DDMMYYYY"),
            ("2024-Dec-31", "D_YYYYMMDD_N", "31/12/2024", "S_DDMMYYYY"),
        ]

        for date_input, in_fmt, expected, out_fmt in month_tests:
            result = convert_between_formats(date_input, in_fmt, out_fmt)
            assert result == expected, f"{date_input} -> {expected}"

    def test_all_format_pairs(self):
        """Test pairwise coverage of all format type combinations"""
        formats = ["D_YYYYMMDD", "D_DDMMYYYY", "S_YYYYMMDD", "S_DDMMYYYY"]
        test_date_dash = "2024-06-15"
        test_date_slash = "2024/06/15"

        # Test key format pair interactions
        format_pairs = [
            ("D_YYYYMMDD", "D_DDMMYYYY", test_date_dash, "15-06-2024"),
            ("D_YYYYMMDD", "S_DDMMYYYY", test_date_dash, "15/06/2024"),
            ("D_DDMMYYYY", "S_YYYYMMDD", "15-06-2024", "2024/06/15"),
            ("S_YYYYMMDD", "S_DDMMYYYY", test_date_slash, "15/06/2024"),
        ]

        for in_fmt, out_fmt, input_date, expected in format_pairs:
            result = convert_between_formats(input_date, in_fmt, out_fmt)
            assert result == expected, f"{in_fmt} -> {out_fmt}"

    def test_boundary_value_interactions(self):
        """Test interactions at boundary values"""
        boundary_tests = [
            # Year boundaries
            ("0001-01-01", "D_YYYYMMDD", True),
            ("9999-12-31", "D_YYYYMMDD", True),
            ("0000-01-01", "D_YYYYMMDD", False),

            # Month boundaries
            ("2024-01-15", "D_YYYYMMDD", True),
            ("2024-12-15", "D_YYYYMMDD", True),
            ("2024-00-15", "D_YYYYMMDD", False),
            ("2024-13-15", "D_YYYYMMDD", False),

            # Day boundaries
            ("2024-06-01", "D_YYYYMMDD", True),
            ("2024-06-30", "D_YYYYMMDD", True),
            ("2024-06-00", "D_YYYYMMDD", False),
            ("2024-06-31", "D_YYYYMMDD", False),
        ]

        for date_str, fmt, should_be_valid in boundary_tests:
            result = convert_between_formats(date_str, fmt, "S_DDMMYYYY")
            if should_be_valid:
                assert result is not None, f"{date_str} should be valid"
            else:
                assert result is None, f"{date_str} should be invalid"

@pytest.fixture(scope="session", autouse=True)
def print_execution_summary(request):
    """Print execution summary after all tests"""
    def finalizer():
        print("\n" + "="*60)
        print("PAIRWISE TEST SET - EXECUTION COMPLETE")
        print("="*60)
    request.addfinalizer(finalizer)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])