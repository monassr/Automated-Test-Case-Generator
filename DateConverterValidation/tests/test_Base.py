"""
Test execution for Base Test Set
Reads test cases from BaseTestSet.csv and executes them
"""

import pytest
import sys
import csv
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from DateConverter import convert_between_formats

class TestBaseTestSet:
    """Execute base test cases"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load test cases from CSV"""
        csv_path = Path(__file__).parent.parent / "BaseTestSet.csv"
        self.test_cases = []

        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.test_cases = list(reader)
        except FileNotFoundError:
            print(f"Warning: {csv_path} not found. Run Generate_Base_Test_Set.py first.")
            self.test_cases = []

        self.execution_times = []

    def test_valid_dates(self):
        """Test all valid date conversions from base set"""
        valid_tests = [tc for tc in self.test_cases if tc['category'] == 'valid']

        for tc in valid_tests:
            start_time = time.time()

            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )

            execution_time = time.time() - start_time
            self.execution_times.append(execution_time)

            assert result == tc['expected_output'], \
                f"Test {tc['test_id']} failed: {tc['date_input']} -> {result} (expected {tc['expected_output']})"

    def test_leap_year_dates(self):
        """Test leap year dates from base set"""
        leap_tests = [tc for tc in self.test_cases if tc['category'] == 'leap_year']

        for tc in leap_tests:
            start_time = time.time()

            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )

            execution_time = time.time() - start_time
            self.execution_times.append(execution_time)

            assert result == tc['expected_output'], \
                f"Leap year test {tc['test_id']} failed: {tc['description']}"

    def test_month_boundaries(self):
        """Test month boundary dates (28, 29, 30, 31)"""
        boundary_tests = [tc for tc in self.test_cases if tc['category'] == 'month_boundary']

        for tc in boundary_tests:
            start_time = time.time()

            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )

            execution_time = time.time() - start_time
            self.execution_times.append(execution_time)

            assert result == tc['expected_output'], \
                f"Boundary test {tc['test_id']} failed: {tc['description']}"

    def test_invalid_dates(self):
        """Test that invalid dates return None"""
        invalid_tests = [tc for tc in self.test_cases if tc['category'] == 'invalid']

        for tc in invalid_tests:
            start_time = time.time()

            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )

            execution_time = time.time() - start_time
            self.execution_times.append(execution_time)

            assert result is None, \
                f"Invalid test {tc['test_id']} should return None: {tc['description']}"

    def test_year_boundaries(self):
        """Test year boundary values"""
        year_tests = [tc for tc in self.test_cases if tc['category'] == 'year_boundary']

        for tc in year_tests:
            start_time = time.time()

            result = convert_between_formats(
                tc['date_input'],
                tc['input_format'],
                tc['output_format']
            )

            execution_time = time.time() - start_time
            self.execution_times.append(execution_time)

            expected = tc['expected_output']
            if expected == 'None' or expected == '' or not expected:
                expected = None

            assert result == expected, \
                f"Year boundary test {tc['test_id']} failed: {tc['description']}"

    def test_01_non_leap_year_feb_29(self):
        """Test non-leap year Feb 29 is invalid"""
        assert convert_between_formats("2019-02-29", "D_YYYYMMDD", "S_DDMMYYYY") is None
        assert convert_between_formats("2021-02-29", "D_YYYYMMDD", "S_DDMMYYYY") is None
        assert convert_between_formats("2023-02-29", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_02_leap_year_feb_29_valid(self):
        """Test leap year Feb 29 is valid"""
        assert convert_between_formats("2020-02-29", "D_YYYYMMDD", "S_DDMMYYYY") == "29/02/2020"
        assert convert_between_formats("2024-02-29", "D_YYYYMMDD", "S_DDMMYYYY") == "29/02/2024"
        assert convert_between_formats("2000-02-29", "D_YYYYMMDD", "S_DDMMYYYY") == "29/02/2000"

    def test_03_century_leap_year_rules(self):
        """Test century year leap year rules"""
        # 2000 is leap (divisible by 400)
        assert convert_between_formats("2000-02-29", "D_YYYYMMDD", "S_DDMMYYYY") == "29/02/2000"

        # 1900 is NOT leap (divisible by 100 but not 400)
        assert convert_between_formats("1900-02-29", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_04_months_with_31_days(self):
        """Test months that have 31 days"""
        months_31 = ["01", "03", "05", "07", "08", "10", "12"]
        for month in months_31:
            assert convert_between_formats(f"2024-{month}-31", "D_YYYYMMDD", "S_DDMMYYYY") is not None

    def test_05_months_with_30_days(self):
        """Test months that have 30 days"""
        months_30 = ["04", "06", "09", "11"]
        for month in months_30:
            # 30th should be valid
            assert convert_between_formats(f"2024-{month}-30", "D_YYYYMMDD", "S_DDMMYYYY") is not None
            # 31st should be invalid
            assert convert_between_formats(f"2024-{month}-31", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_06_february_non_leap(self):
        """Test February in non-leap year"""
        # 28th valid
        assert convert_between_formats("2023-02-28", "D_YYYYMMDD", "S_DDMMYYYY") == "28/02/2023"
        # 29th invalid
        assert convert_between_formats("2023-02-29", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_07_invalid_month_numbers(self):
        """Test invalid month numbers"""
        assert convert_between_formats("2024-00-15", "D_YYYYMMDD", "S_DDMMYYYY") is None
        assert convert_between_formats("2024-13-15", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_08_invalid_day_numbers(self):
        """Test invalid day numbers"""
        assert convert_between_formats("2024-01-00", "D_YYYYMMDD", "S_DDMMYYYY") is None
        assert convert_between_formats("2024-01-32", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_09_year_boundaries_valid(self):
        """Test valid year boundaries"""
        assert convert_between_formats("0001-01-01", "D_YYYYMMDD", "S_DDMMYYYY") == "01/01/0001"
        assert convert_between_formats("9999-12-31", "D_YYYYMMDD", "S_DDMMYYYY") == "31/12/9999"

    def test_10_year_zero_invalid(self):
        """Test year 0 is invalid"""
        assert convert_between_formats("0000-01-01", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_11_empty_and_malformed(self):
        """Test empty and malformed inputs"""
        assert convert_between_formats("", "D_YYYYMMDD", "S_DDMMYYYY") is None
        assert convert_between_formats(None, "D_YYYYMMDD", "S_DDMMYYYY") is None
        assert convert_between_formats("invalid", "D_YYYYMMDD", "S_DDMMYYYY") is None

    def test_12_wrong_separator(self):
        """Test dates with wrong separator"""
        assert convert_between_formats("2024/01/15", "D_YYYYMMDD", "S_DDMMYYYY") is None
        assert convert_between_formats("2024-01-15", "S_YYYYMMDD", "D_DDMMYYYY") is None

@pytest.fixture(scope="session", autouse=True)
def print_execution_summary(request):
    """Print execution time summary after all tests"""
    def finalizer():
        print("\n" + "="*60)
        print("BASE TEST SET - EXECUTION SUMMARY")
        print("="*60)
    request.addfinalizer(finalizer)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short", "-p", "no:warnings"])