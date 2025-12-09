"""
Test execution for Metamorphic Relations Test Set
Tests program correctness through metamorphic properties rather than exact outputs
"""

import pytest
import sys
import csv
import time
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent.parent))
from DateConverter import convert_between_formats

class TestMetamorphicRelations:
    """Execute metamorphic relation test cases"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load test cases from CSV"""
        csv_path = Path(__file__).parent.parent / "MetamorphicTestSet.csv"
        self.test_cases = []
        self.execution_times = []

        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.test_cases = list(reader)
                print(f"\nLoaded {len(self.test_cases)} metamorphic test cases")
        except FileNotFoundError:
            print(f"Warning: {csv_path} not found. Run Generate_Metamorphic_Test_Set.py first.")
            self.test_cases = []

    # ==================== MR1: ROUND-TRIP CONVERSION ====================

    def test_mr1_roundtrip_dash_formats(self):
        """MR1: Converting A→B→A should equal A (dash formats)"""
        test_dates = [
            ("2024-12-07", "D_YYYYMMDD", "S_DDMMYYYY"),
            ("07-12-2024", "D_DDMMYYYY", "S_YYYYMMDD"),
            ("2024-Jan-15", "D_YYYYMMDD_N", "D_YYYYMMDD"),
        ]

        for seed_date, seed_fmt, intermediate_fmt in test_dates:
            start = time.time()

            # Step 1: Convert to intermediate format
            intermediate = convert_between_formats(seed_date, seed_fmt, intermediate_fmt)
            assert intermediate is not None, f"First conversion failed: {seed_date}"

            # Step 2: Convert back to original format
            final = convert_between_formats(intermediate, intermediate_fmt, seed_fmt)
            assert final is not None, f"Second conversion failed: {intermediate}"

            # MR1 Property: Final should equal seed
            assert final == seed_date, \
                f"MR1 violated: {seed_date} -> {intermediate} -> {final}"

            self.execution_times.append(time.time() - start)

    def test_mr1_roundtrip_slash_formats(self):
        """MR1: Round-trip with slash formats"""
        test_dates = [
            ("2024/06/15", "S_YYYYMMDD", "S_DDMMYYYY"),
            ("15/06/2024", "S_DDMMYYYY", "S_YYYYMMDD"),
            ("2024/12/31", "S_YYYYMMDD", "D_YYYYMMDD"),
        ]

        for seed_date, seed_fmt, intermediate_fmt in test_dates:
            start = time.time()

            intermediate = convert_between_formats(seed_date, seed_fmt, intermediate_fmt)
            assert intermediate is not None

            final = convert_between_formats(intermediate, intermediate_fmt, seed_fmt)
            assert final is not None

            assert final == seed_date, f"MR1 violated: Round-trip failed"

            self.execution_times.append(time.time() - start)

    def test_mr1_roundtrip_leap_year(self):
        """MR1: Round-trip with leap year dates"""
        leap_dates = [
            ("2020-02-29", "D_YYYYMMDD", "S_DDMMYYYY"),
            ("29/02/2024", "S_DDMMYYYY", "D_YYYYMMDD"),
            ("2000-02-29", "D_YYYYMMDD", "D_DDMMYYYY"),
        ]

        for seed_date, seed_fmt, intermediate_fmt in leap_dates:
            start = time.time()

            intermediate = convert_between_formats(seed_date, seed_fmt, intermediate_fmt)
            assert intermediate is not None, f"Leap year conversion failed: {seed_date}"

            final = convert_between_formats(intermediate, intermediate_fmt, seed_fmt)
            assert final is not None

            assert final == seed_date, f"MR1 violated for leap year: {seed_date}"

            self.execution_times.append(time.time() - start)

    def test_mr1_roundtrip_two_digit_year(self):
        """MR1: Round-trip with two-digit year formats"""
        test_dates = [
            ("24-06-15", "D_YYMMDD", "D_YYYYMMDD"),
            ("15/06/24", "S_DDMMyy", "S_DDMMYYYY"),
        ]

        for seed_date, seed_fmt, intermediate_fmt in test_dates:
            start = time.time()

            intermediate = convert_between_formats(seed_date, seed_fmt, intermediate_fmt)
            assert intermediate is not None

            final = convert_between_formats(intermediate, intermediate_fmt, seed_fmt)
            assert final is not None

            assert final == seed_date, f"MR1 violated for 2-digit year: {seed_date}"

            self.execution_times.append(time.time() - start)

    # ==================== MR2: IDEMPOTENCY ====================

    def test_mr2_idempotency_same_conversion(self):
        """MR2: Converting same input multiple times yields same result"""
        test_cases = [
            ("2024-03-15", "D_YYYYMMDD", "S_DDMMYYYY"),
            ("15/03/2024", "S_DDMMYYYY", "D_YYYYMMDD"),
            ("2024-Dec-25", "D_YYYYMMDD_N", "D_YYYYMMDD"),
        ]

        for seed_date, in_fmt, out_fmt in test_cases:
            start = time.time()

            # First conversion
            result1 = convert_between_formats(seed_date, in_fmt, out_fmt)
            assert result1 is not None

            # Second conversion of same input
            result2 = convert_between_formats(seed_date, in_fmt, out_fmt)
            assert result2 is not None

            # Third conversion
            result3 = convert_between_formats(seed_date, in_fmt, out_fmt)
            assert result3 is not None

            # MR2 Property: All results should be identical
            assert result1 == result2 == result3, \
                f"MR2 violated: Idempotency failed for {seed_date}"

            self.execution_times.append(time.time() - start)

    def test_mr2_idempotency_converted_result(self):
        """MR2: Converting already converted result maintains consistency"""
        seed_dates = [
            ("2024-06-15", "D_YYYYMMDD", "S_DDMMYYYY"),
            ("2020-Feb-29", "D_YYYYMMDD_N", "D_YYYYMMDD"),
        ]

        for seed_date, in_fmt, out_fmt in seed_dates:
            start = time.time()

            # First conversion
            result1 = convert_between_formats(seed_date, in_fmt, out_fmt)
            assert result1 is not None

            # Convert the result again (same transformation)
            result2 = convert_between_formats(seed_date, in_fmt, out_fmt)
            assert result2 is not None

            # MR2 Property: Results should be identical
            assert result1 == result2, f"MR2 violated: {seed_date}"

            self.execution_times.append(time.time() - start)

    # ==================== MR3: DATE ARITHMETIC ====================

    def test_mr3_consecutive_days(self):
        """MR3: Dates differing by 1 day maintain difference after conversion"""
        date_pairs = [
            ("2024-01-15", "2024-01-16"),
            ("2024-02-28", "2024-02-29"),  # Leap year boundary
            ("2024-12-31", "2025-01-01"),  # Year boundary
        ]

        for date1, date2 in date_pairs:
            start = time.time()

            # Convert both dates
            converted1 = convert_between_formats(date1, "D_YYYYMMDD", "S_DDMMYYYY")
            converted2 = convert_between_formats(date2, "D_YYYYMMDD", "S_DDMMYYYY")

            assert converted1 is not None and converted2 is not None

            # Parse back and check difference
            dt1 = datetime.strptime(converted1, "%d/%m/%Y")
            dt2 = datetime.strptime(converted2, "%d/%m/%Y")

            diff = (dt2 - dt1).days

            # MR3 Property: Should still differ by 1 day
            assert diff == 1, \
                f"MR3 violated: {date1} and {date2} should differ by 1 day, got {diff}"

            self.execution_times.append(time.time() - start)

    def test_mr3_week_difference(self):
        """MR3: Dates differing by 7 days maintain difference"""
        date_pairs = [
            ("2024-01-01", "2024-01-08"),
            ("2024-06-15", "2024-06-22"),
            ("2024-12-25", "2025-01-01"),
        ]

        for date1, date2 in date_pairs:
            start = time.time()

            converted1 = convert_between_formats(date1, "D_YYYYMMDD", "D_DDMMYYYY")
            converted2 = convert_between_formats(date2, "D_YYYYMMDD", "D_DDMMYYYY")

            assert converted1 is not None and converted2 is not None

            dt1 = datetime.strptime(converted1, "%d-%m-%Y")
            dt2 = datetime.strptime(converted2, "%d-%m-%Y")

            diff = abs((dt2 - dt1).days)

            # MR3 Property: Should differ by 7 days
            assert diff == 7, \
                f"MR3 violated: Expected 7 days difference, got {diff}"

            self.execution_times.append(time.time() - start)

    def test_mr3_month_span(self):
        """MR3: Month-spanning dates maintain relative difference"""
        # Test dates at start and end of month
        test_cases = [
            ("2024-01-31", "2024-02-01", 1),
            ("2024-02-28", "2024-03-01", 2),  # Non-leap year (2 days)
            ("2024-02-29", "2024-03-01", 1),  # Leap year (1 day)
        ]

        for date1, date2, expected_diff in test_cases:
            start = time.time()

            converted1 = convert_between_formats(date1, "D_YYYYMMDD", "S_YYYYMMDD")
            converted2 = convert_between_formats(date2, "D_YYYYMMDD", "S_YYYYMMDD")

            # Skip if date is invalid (like Feb 29 in non-leap year)
            if converted1 is None or converted2 is None:
                continue

            dt1 = datetime.strptime(converted1, "%Y/%m/%d")
            dt2 = datetime.strptime(converted2, "%Y/%m/%d")

            diff = (dt2 - dt1).days

            assert diff == expected_diff, \
                f"MR3 violated: Expected {expected_diff} days, got {diff}"

            self.execution_times.append(time.time() - start)

    # ==================== MR4: INVALID REMAINS INVALID ====================

    def test_mr4_invalid_feb_30(self):
        """MR4: February 30 is invalid in any format"""
        invalid_dates = [
            ("2024-02-30", "D_YYYYMMDD"),
            ("30-02-2024", "D_DDMMYYYY"),
            ("2024/02/30", "S_YYYYMMDD"),
            ("30/02/2024", "S_DDMMYYYY"),
        ]

        target_formats = ["D_YYYYMMDD", "S_DDMMYYYY", "D_DDMMYYYY"]

        for invalid_date, in_fmt in invalid_dates:
            for out_fmt in target_formats:
                start = time.time()

                result = convert_between_formats(invalid_date, in_fmt, out_fmt)

                # MR4 Property: Should always return None
                assert result is None, \
                    f"MR4 violated: {invalid_date} should be invalid in any format"

                self.execution_times.append(time.time() - start)

    def test_mr4_invalid_month_13(self):
        """MR4: Month 13 is invalid regardless of conversion"""
        invalid_dates = [
            ("2024-13-01", "D_YYYYMMDD"),
            ("01-13-2024", "D_DDMMYYYY"),
            ("2024/13/01", "S_YYYYMMDD"),
        ]

        for invalid_date, in_fmt in invalid_dates:
            start = time.time()

            result1 = convert_between_formats(invalid_date, in_fmt, "S_DDMMYYYY")
            result2 = convert_between_formats(invalid_date, in_fmt, "D_DDMMYYYY")

            # MR4 Property: Invalid in all formats
            assert result1 is None and result2 is None, \
                f"MR4 violated: Month 13 should always be invalid"

            self.execution_times.append(time.time() - start)

    def test_mr4_invalid_day_32(self):
        """MR4: Day 32 is invalid for any month"""
        invalid_dates = [
            ("2024-01-32", "D_YYYYMMDD"),  # January has 31 days
            ("2024-06-32", "D_YYYYMMDD"),  # June has 30 days
            ("32/01/2024", "S_DDMMYYYY"),
        ]

        for invalid_date, in_fmt in invalid_dates:
            start = time.time()

            result = convert_between_formats(invalid_date, in_fmt, "D_YYYYMMDD")

            assert result is None, f"MR4 violated: Day 32 should be invalid"

            self.execution_times.append(time.time() - start)

    def test_mr4_non_leap_feb_29(self):
        """MR4: Feb 29 in non-leap years is invalid in any format"""
        non_leap_years = [2019, 2021, 2023, 1900, 2100]

        for year in non_leap_years:
            start = time.time()

            # Try different formats
            result1 = convert_between_formats(f"{year}-02-29", "D_YYYYMMDD", "S_DDMMYYYY")
            result2 = convert_between_formats(f"29/02/{year}", "S_DDMMYYYY", "D_YYYYMMDD")

            # MR4 Property: Invalid in all formats
            assert result1 is None and result2 is None, \
                f"MR4 violated: {year} is not a leap year, Feb 29 should be invalid"

            self.execution_times.append(time.time() - start)

    def test_mr4_30_day_month_day_31(self):
        """MR4: Day 31 in 30-day months is invalid"""
        months_30_days = ["04", "06", "09", "11"]

        for month in months_30_days:
            start = time.time()

            result = convert_between_formats(
                f"2024-{month}-31",
                "D_YYYYMMDD",
                "S_DDMMYYYY"
            )

            # MR4 Property: Should be invalid
            assert result is None, \
                f"MR4 violated: Month {month} only has 30 days"

            self.execution_times.append(time.time() - start)

    def test_mr4_malformed_dates(self):
        """MR4: Malformed dates are invalid regardless of target format"""
        malformed = [
            ("", "D_YYYYMMDD"),
            ("invalid", "D_YYYYMMDD"),
            ("2024/01/15", "D_YYYYMMDD"),  # Wrong separator
            ("15-01-2024", "S_DDMMYYYY"),  # Wrong separator
        ]

        for invalid_date, in_fmt in malformed:
            start = time.time()

            result = convert_between_formats(invalid_date, in_fmt, "D_YYYYMMDD")

            assert result is None, f"MR4 violated: Malformed date should be invalid"

            self.execution_times.append(time.time() - start)

    # ==================== MR5: COMPONENT PRESERVATION ====================

    def test_mr5_separator_preservation(self):
        """MR5: Converting between same separator type preserves structure"""
        # Dash to dash
        result = convert_between_formats("2024-06-15", "D_YYYYMMDD", "D_DDMMYYYY")
        assert "-" in result, "MR5: Dash separator should be preserved"

        # Slash to slash
        result = convert_between_formats("2024/06/15", "S_YYYYMMDD", "S_DDMMYYYY")
        assert "/" in result, "MR5: Slash separator should be preserved"

    def test_mr5_year_format_handling(self):
        """MR5: Year format is appropriately converted"""
        # 2-digit to 4-digit
        result = convert_between_formats("24-06-15", "D_YYMMDD", "D_YYYYMMDD")
        assert len(result.split("-")[0]) == 4, "MR5: Should expand to 4-digit year"

        # 4-digit preserved
        result = convert_between_formats("2024-06-15", "D_YYYYMMDD", "S_YYYYMMDD")
        assert len(result.split("/")[0]) == 4, "MR5: Should maintain 4-digit year"

    def test_mr5_component_order_preservation(self):
        """MR5: Date component ordering is correctly transformed"""
        # Year-first to Day-first
        result = convert_between_formats("2024-06-15", "D_YYYYMMDD", "D_DDMMYYYY")
        parts = result.split("-")
        assert len(parts[0]) == 2 and int(parts[0]) == 15, "MR5: Day should be first"

        # Day-first to Year-first
        result = convert_between_formats("15/06/2024", "S_DDMMYYYY", "S_YYYYMMDD")
        parts = result.split("/")
        assert len(parts[0]) == 4 and int(parts[0]) == 2024, "MR5: Year should be first"

@pytest.fixture(scope="session", autouse=True)
def print_execution_summary(request):
    """Print execution summary after all tests"""
    def finalizer():
        print("\n" + "="*60)
        print("METAMORPHIC TEST SET - EXECUTION COMPLETE")
        print("="*60)
        print("\nMetamorphic Relations Tested:")
        print("  MR1: Round-trip conversion")
        print("  MR2: Idempotency")
        print("  MR3: Date arithmetic preservation")
        print("  MR4: Invalid remains invalid")
        print("  MR5: Component preservation")
    request.addfinalizer(finalizer)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])