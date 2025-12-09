"""
Pairwise (All-Pairs) Test Case Generator
Uses combinatorial testing to generate test cases efficiently
"""

import csv
import sys
import os
from allpairspy import AllPairs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_pairwise_tests():
    """
    Generate pairwise test cases for date converter
    Uses All-Pairs combinatorial testing technique

    Parameters:
    1. Input Format
    2. Output Format
    3. Year Type
    4. Month Type
    5. Day Type
    6. Separator Type
    """

    # Define parameter values for pairwise testing
    parameters = [
        # Input format categories
        ["YYYY-MM-DD", "DD-MM-YYYY", "YYYY/MM/DD", "DD/MM/YYYY", "YY-MM-DD", "YYYY-MMM-DD"],

        # Output format categories
        ["YYYY-MM-DD", "DD-MM-YYYY", "YYYY/MM/DD", "DD/MM/YYYY", "YY-MM-DD", "DD-MMM-YYYY"],

        # Year types
        ["2024", "2020", "2000", "1900", "0001", "9999", "99", "00"],

        # Month types
        ["01", "02", "04", "06", "12", "00", "13"],

        # Day types
        ["01", "15", "28", "29", "30", "31", "00", "32"],

        # Date validity scenarios
        ["typical", "leap_feb29", "month_end", "invalid_day", "invalid_month", "boundary"]
    ]

    test_cases = []
    test_id = 1

    # Generate all-pairs combinations
    for combination in AllPairs(parameters):
        in_fmt_cat, out_fmt_cat, year, month, day, scenario = combination

        # Map format categories to actual format names
        in_fmt = map_format_category(in_fmt_cat)
        out_fmt = map_format_category(out_fmt_cat)

        # Build date string based on input format and parameters
        date_str = build_date_from_params(in_fmt_cat, year, month, day, scenario)

        # Determine expected validity
        is_valid = determine_validity(year, month, day, scenario)

        # Build expected output if valid
        expected = build_expected_output(out_fmt_cat, year, month, day, scenario) if is_valid else None

        test_case = {
            "test_id": f"PW_{test_id:03d}",
            "date_input": date_str,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "expected_valid": str(is_valid),
            "scenario": scenario,
            "description": f"{scenario}: {year}-{month}-{day}"
        }
        test_cases.append(test_case)
        test_id += 1

    # Add specific edge cases not covered by pairwise
    test_cases.extend(generate_edge_cases(test_id))

    return test_cases

def map_format_category(fmt_category):
    """Map format category to DateFormats enum name"""
    format_map = {
        "YYYY-MM-DD": "D_YYYYMMDD",
        "DD-MM-YYYY": "D_DDMMYYYY",
        "YYYY/MM/DD": "S_YYYYMMDD",
        "DD/MM/YYYY": "S_DDMMYYYY",
        "YY-MM-DD": "D_YYMMDD",
        "DD-MM-YY": "D_DDMMyy",
        "YYYY-MMM-DD": "D_YYYYMMDD_N",
        "DD-MMM-YYYY": "D_DDMMYYYY_N",
    }
    return format_map.get(fmt_category, "D_YYYYMMDD")

def build_date_from_params(fmt_category, year, month, day, scenario):
    """Build date string from parameters"""
    # Handle special scenarios
    if scenario == "leap_feb29":
        month = "02"
        day = "29"
    elif scenario == "month_end":
        if month in ["01", "03", "05", "07", "08", "10", "12"]:
            day = "31"
        elif month in ["04", "06", "09", "11"]:
            day = "30"
        elif month == "02":
            day = "28"
    elif scenario == "invalid_day":
        day = "32"
    elif scenario == "invalid_month":
        month = "13"

    # Adjust year format if needed
    if "YY-" in fmt_category and len(year) == 4:
        year = year[-2:]  # Take last 2 digits
    elif "YYYY" in fmt_category and len(year) == 2:
        if int(year) < 70:
            year = "20" + year
        else:
            year = "19" + year

    # Build date string based on format
    if "/" in fmt_category:
        sep = "/"
    else:
        sep = "-"

    if fmt_category.startswith(("DD", "dd")):
        # Day first
        if "MMM" in fmt_category:
            month_str = get_month_name(int(month)) if month.isdigit() and 1 <= int(month) <= 12 else "Jan"
            return f"{day}{sep}{month_str}{sep}{year}"
        return f"{day}{sep}{month}{sep}{year}"
    else:
        # Year first
        if "MMM" in fmt_category:
            month_str = get_month_name(int(month)) if month.isdigit() and 1 <= int(month) <= 12 else "Jan"
            return f"{year}{sep}{month_str}{sep}{day}"
        return f"{year}{sep}{month}{sep}{day}"

def get_month_name(month_num):
    """Get abbreviated month name"""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[month_num - 1] if 1 <= month_num <= 12 else "Jan"

def build_expected_output(fmt_category, year, month, day, scenario):
    """Build expected output string"""
    # Same logic as build_date_from_params but for output format
    return build_date_from_params(fmt_category, year, month, day, scenario)

def determine_validity(year, month, day, scenario):
    """Determine if date should be valid"""
    if scenario in ["invalid_day", "invalid_month"]:
        return False

    try:
        y = int(year) if len(year) == 4 else (2000 + int(year) if int(year) < 70 else 1900 + int(year))
        m = int(month)
        d = int(day)

        # Basic range checks
        if y < 1 or y > 9999:
            return False
        if m < 1 or m > 12:
            return False
        if d < 1 or d > 31:
            return False

        # Days in month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Check leap year
        if is_leap_year(y):
            days_in_month[1] = 29

        if d > days_in_month[m - 1]:
            return False

        return True
    except:
        return False

def is_leap_year(year):
    """Check if year is leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def generate_edge_cases(start_id):
    """Generate specific edge cases"""
    edge_cases = []
    test_id = start_id

    specific_tests = [
        # Format: (input, in_fmt, out_fmt, expected, valid, desc)
        ("", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "Empty string"),
        ("invalid", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "Malformed date"),
        ("2024/01/15", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "Wrong separator"),
        ("2024-13-01", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "Month 13"),
        ("2024-00-15", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "Month 0"),
        ("2024-06-31", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "June 31"),
        ("2019-02-29", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "Non-leap Feb 29"),
        ("2020-02-29", "D_YYYYMMDD", "S_DDMMYYYY", "29/02/2020", True, "Leap Feb 29"),
        ("2000-02-29", "D_YYYYMMDD", "S_DDMMYYYY", "29/02/2000", True, "Y2K leap"),
        ("1900-02-29", "D_YYYYMMDD", "S_DDMMYYYY", None, False, "1900 not leap"),
    ]

    for date_input, in_fmt, out_fmt, expected, valid, desc in specific_tests:
        edge_cases.append({
            "test_id": f"PW_EDGE_{test_id:03d}",
            "date_input": date_input,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "expected_valid": str(valid),
            "scenario": "edge_case",
            "description": desc
        })
        test_id += 1

    return edge_cases

def save_to_csv(test_cases, filename="PairWiseInputSet.csv"):
    """Save test cases to CSV file"""
    if not test_cases:
        return

    fieldnames = ["test_id", "date_input", "input_format", "output_format",
                  "expected_output", "expected_valid", "scenario", "description"]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(test_cases)

    print(f"✓ Generated {len(test_cases)} pairwise test cases")
    print(f"✓ Saved to {filename}")

def main():
    """Generate and save pairwise test cases"""
    print("Generating Pairwise (All-Pairs) Test Set...")
    print("Using combinatorial testing technique")

    test_cases = generate_pairwise_tests()
    save_to_csv(test_cases)

    # Print summary by scenario
    scenarios = {}
    for tc in test_cases:
        scenario = tc['scenario']
        scenarios[scenario] = scenarios.get(scenario, 0) + 1

    print("\nTest Cases by Scenario:")
    for scenario, count in sorted(scenarios.items()):
        print(f"  {scenario}: {count} tests")

    # Count valid vs invalid
    valid_count = sum(1 for tc in test_cases if tc['expected_valid'] == 'True')
    invalid_count = len(test_cases) - valid_count
    print(f"\nValid cases: {valid_count}")
    print(f"Invalid cases: {invalid_count}")

    print(f"\nSample test cases:")
    for tc in test_cases[:5]:
        print(f"{tc['test_id']}: {tc['date_input']} ({tc['input_format']} -> {tc['output_format']})")

if __name__ == "__main__":
    main()