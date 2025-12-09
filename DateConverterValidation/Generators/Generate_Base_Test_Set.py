"""
Base Test Set Generator
Generates fundamental test cases covering basic functionality
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_base_tests():
    """Generate base test cases"""
    test_cases = []

    # Valid dates - typical cases
    valid_cases = [
        ("2024-01-15", "D_YYYYMMDD", "S_DDMMYYYY", "15/01/2024", "Typical date"),
        ("15/01/2024", "S_DDMMYYYY", "D_YYYYMMDD", "2024-01-15", "Reverse typical"),
        ("2024-12-31", "D_YYYYMMDD", "S_YYYYMMDD", "2024/12/31", "Year end"),
        ("01/01/2024", "S_DDMMYYYY", "D_DDMMYYYY", "01-01-2024", "Year start"),
        ("2024-06-15", "D_YYYYMMDD", "S_DDMMYYYY", "15/06/2024", "Mid year"),

        # Text month formats
        ("2024-Dec-07", "D_YYYYMMDD_N", "D_YYYYMMDD", "2024-12-07", "Text to numeric month"),
        ("07-Jan-2024", "D_DDMMYYYY_N", "S_DDMMYYYY", "07/01/2024", "Text month conversion"),
        ("2024-Mar-31", "D_YYYYMMDD_N", "D_DDMMYYYY", "31-03-2024", "Text month end"),

        # Two-digit year formats
        ("24-12-07", "D_YYMMDD", "D_YYYYMMDD", "2024-12-07", "2-digit to 4-digit year"),
        ("07/12/24", "S_DDMMyy", "S_DDMMYYYY", "07/12/2024", "2-digit year slash format"),
        ("00-01-01", "D_YYMMDD", "D_YYYYMMDD", "2000-01-01", "Y2K year"),

        # DateTime formats
        ("2024-12-07, 03:30pm", "D_YYYYMMDDHHMMA", "D_DDMMYYYYHHMMA", "07-12-2024, 03:30pm", "DateTime with AM/PM"),
        ("2024/12/07, 11:45am", "S_YYYYMMDDHHMMA", "S_DDMMYYYYHHMMA", "07/12/2024, 11:45am", "DateTime slash format"),
        ("2024-12-07, 03:30:45pm", "D_YYYYMMDDHHMMSSA", "D_DDMMYYYYHHMMSSA", "07-12-2024, 03:30:45pm", "DateTime with seconds"),
    ]

    for i, (input_date, in_fmt, out_fmt, expected, description) in enumerate(valid_cases, 1):
        test_cases.append({
            "test_id": f"BASE_{i:03d}",
            "category": "valid",
            "date_input": input_date,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "description": description
        })

    # Leap year cases
    leap_year_cases = [
        ("2020-02-29", "D_YYYYMMDD", "S_DDMMYYYY", "29/02/2020", "Leap year Feb 29 - 2020"),
        ("29/02/2024", "S_DDMMYYYY", "D_YYYYMMDD", "2024-02-29", "Leap year Feb 29 - 2024"),
        ("2000-02-29", "D_YYYYMMDD", "D_DDMMYYYY", "29-02-2000", "Leap year - century divisible by 400"),
        ("20-02-29", "D_YYMMDD", "D_YYYYMMDD", "2020-02-29", "Leap year 2-digit format"),
    ]

    test_id = len(test_cases) + 1
    for input_date, in_fmt, out_fmt, expected, description in leap_year_cases:
        test_cases.append({
            "test_id": f"BASE_{test_id:03d}",
            "category": "leap_year",
            "date_input": input_date,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "description": description
        })
        test_id += 1

    # Month boundary cases
    month_boundaries = [
        ("2024-01-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/01/2024", "January - 31 days"),
        ("2024-02-28", "D_YYYYMMDD", "S_DDMMYYYY", "28/02/2024", "February - 28 days (non-leap)"),
        ("2024-03-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/03/2024", "March - 31 days"),
        ("2024-04-30", "D_YYYYMMDD", "S_DDMMYYYY", "30/04/2024", "April - 30 days"),
        ("2024-05-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/05/2024", "May - 31 days"),
        ("2024-06-30", "D_YYYYMMDD", "S_DDMMYYYY", "30/06/2024", "June - 30 days"),
        ("2024-07-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/07/2024", "July - 31 days"),
        ("2024-08-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/08/2024", "August - 31 days"),
        ("2024-09-30", "D_YYYYMMDD", "S_DDMMYYYY", "30/09/2024", "September - 30 days"),
        ("2024-10-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/10/2024", "October - 31 days"),
        ("2024-11-30", "D_YYYYMMDD", "S_DDMMYYYY", "30/11/2024", "November - 30 days"),
        ("2024-12-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/12/2024", "December - 31 days"),
    ]

    for input_date, in_fmt, out_fmt, expected, description in month_boundaries:
        test_cases.append({
            "test_id": f"BASE_{test_id:03d}",
            "category": "month_boundary",
            "date_input": input_date,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "description": description
        })
        test_id += 1

    # Invalid dates
    invalid_cases = [
        ("2024-02-30", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - Feb 30"),
        ("2024-13-01", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - Month 13"),
        ("2024-00-15", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - Month 0"),
        ("2024-06-31", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - June 31"),
        ("32/01/2024", "S_DDMMYYYY", "D_YYYYMMDD", None, "Invalid - Day 32"),
        ("00/01/2024", "S_DDMMYYYY", "D_YYYYMMDD", None, "Invalid - Day 0"),
        ("15/13/2024", "S_DDMMYYYY", "D_YYYYMMDD", None, "Invalid - Month 13"),
        ("2019-02-29", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - Non-leap year Feb 29"),
        ("1900-02-29", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - 1900 not leap year"),
        ("", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - Empty string"),
        ("invalid", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - Malformed date"),
    ]

    for input_date, in_fmt, out_fmt, expected, description in invalid_cases:
        test_cases.append({
            "test_id": f"BASE_{test_id:03d}",
            "category": "invalid",
            "date_input": input_date,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "description": description
        })
        test_id += 1

    # Year boundary cases
    year_boundaries = [
        ("0001-01-01", "D_YYYYMMDD", "S_DDMMYYYY", "01/01/0001", "Year boundary - Year 1"),
        ("9999-12-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/12/9999", "Year boundary - Year 9999"),
        ("0000-01-01", "D_YYYYMMDD", "S_DDMMYYYY", None, "Invalid - Year 0"),
        ("2000-01-01", "D_YYYYMMDD", "S_DDMMYYYY", "01/01/2000", "Year 2000"),
        ("1999-12-31", "D_YYYYMMDD", "S_DDMMYYYY", "31/12/1999", "Pre-Y2K"),
    ]

    for input_date, in_fmt, out_fmt, expected, description in year_boundaries:
        test_cases.append({
            "test_id": f"BASE_{test_id:03d}",
            "category": "year_boundary",
            "date_input": input_date,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "description": description
        })
        test_id += 1

    return test_cases

def save_tests_to_file(test_cases, filename="BaseTestSet.csv"):
    """Save test cases to CSV file"""
    import csv

    if not test_cases:
        return

    fieldnames = ["test_id", "category", "date_input", "input_format",
                  "output_format", "expected_output", "description"]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(test_cases)

    print(f"✓ Generated {len(test_cases)} base test cases")
    print(f"✓ Saved to {filename}")

    # Print summary by category
    categories = {}
    for tc in test_cases:
        cat = tc['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\nTest Cases by Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} tests")

def main():
    """Generate and save base test cases"""
    print("Generating Base Test Set...")
    test_cases = generate_base_tests()
    save_tests_to_file(test_cases)

    print(f"\nSample test cases:")
    for tc in test_cases[:5]:
        print(f"{tc['test_id']}: {tc['date_input']} ({tc['input_format']} -> {tc['output_format']}) = {tc['expected_output']}")

if __name__ == "__main__":
    main()