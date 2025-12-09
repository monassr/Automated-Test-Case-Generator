"""
Category-Partition Test Set Generator
Divides input parameters into categories and applies constraints
"""

import sys
import os
import csv
from itertools import product

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_category_partition_tests():
    """
    Generate test cases using category-partition method

    Steps:
    1. Identify parameters
    2. Divide each parameter into categories
    3. Apply constraints
    4. Generate test frames
    """

    test_cases = []
    test_id = 1

    # Define categories for each parameter

    # 1. Format Type Categories
    format_types = {
        "dash_numeric": ["D_YYYYMMDD", "D_DDMMYYYY"],
        "slash_numeric": ["S_YYYYMMDD", "S_DDMMYYYY"],
        "dash_text": ["D_YYYYMMDD_N", "D_DDMMYYYY_N"],
        "two_digit_year": ["D_YYMMDD", "S_YYMMDD"],
        "datetime": ["D_YYYYMMDDHHMMA", "S_DDMMYYYYHHMMA"],
        "datetime_seconds": ["D_YYYYMMDDHHMMSSA", "S_YYYYMMDDHHMMSSA"],
    }

    # 2. Year Categories
    year_categories = {
        "typical": ["2024", "2023", "2022"],
        "leap": ["2020", "2024", "2000"],
        "non_leap": ["2019", "2021", "2023"],
        "century_special": ["1900", "2000", "2100"],  # 1900 not leap, 2000 is leap
        "boundary": ["0001", "9999"],
        "two_digit": ["24", "20", "00", "99"],
    }

    # 3. Month Categories
    month_categories = {
        "31_days": ["01", "03", "05", "07", "08", "10", "12"],
        "30_days": ["04", "06", "09", "11"],
        "february": ["02"],
        "boundary": ["01", "12"],
    }

    # 4. Day Categories
    day_categories = {
        "start": ["01"],
        "mid": ["15"],
        "end_28": ["28"],
        "end_29": ["29"],
        "end_30": ["30"],
        "end_31": ["31"],
    }

    # 5. Validity Categories
    validity_categories = ["valid", "invalid"]

    # Generate test cases with constraints

    # Constraint 1: Valid dates with 31-day months
    for fmt_cat, formats in format_types.items():
        if "datetime" in fmt_cat:
            continue  # Skip datetime for now

        for in_fmt, out_fmt in product(formats[:1], formats):
            if in_fmt == out_fmt:
                continue

            # Test with months having 31 days
            for month in month_categories["31_days"][:2]:  # Limit to 2 months
                for year in year_categories["typical"][:1]:
                    for day in ["01", "15", "31"]:
                        date_str = build_date_string(in_fmt, year, month, day)
                        expected = build_expected(out_fmt, year, month, day)

                        test_cases.append({
                            "test_id": f"CP_{test_id:03d}",
                            "category": f"{fmt_cat}_31days",
                            "date_input": date_str,
                            "input_format": in_fmt,
                            "output_format": out_fmt,
                            "expected_output": expected,
                            "constraint": "31-day months valid",
                            "description": f"Valid date in {month} with {day} day"
                        })
                        test_id += 1

    # Constraint 2: Valid dates with 30-day months
    for fmt_cat in ["dash_numeric", "slash_numeric"]:
        formats = format_types[fmt_cat]
        in_fmt, out_fmt = formats[0], formats[1]

        for month in month_categories["30_days"][:2]:
            for year in year_categories["typical"][:1]:
                for day in ["01", "15", "30"]:
                    date_str = build_date_string(in_fmt, year, month, day)
                    expected = build_expected(out_fmt, year, month, day)

                    test_cases.append({
                        "test_id": f"CP_{test_id:03d}",
                        "category": f"{fmt_cat}_30days",
                        "date_input": date_str,
                        "input_format": in_fmt,
                        "output_format": out_fmt,
                        "expected_output": expected,
                        "constraint": "30-day months valid",
                        "description": f"Valid date in {month} with {day} day"
                    })
                    test_id += 1

    # Constraint 3: February in leap years
    for fmt_cat in ["dash_numeric", "slash_numeric"]:
        formats = format_types[fmt_cat]
        in_fmt, out_fmt = formats[0], formats[1]

        for year in year_categories["leap"][:2]:
            for day in ["01", "15", "28", "29"]:
                date_str = build_date_string(in_fmt, year, "02", day)
                expected = build_expected(out_fmt, year, "02", day)

                test_cases.append({
                    "test_id": f"CP_{test_id:03d}",
                    "category": "february_leap",
                    "date_input": date_str,
                    "input_format": in_fmt,
                    "output_format": out_fmt,
                    "expected_output": expected,
                    "constraint": "Feb in leap year valid",
                    "description": f"Leap year {year} Feb {day}"
                })
                test_id += 1

    # Constraint 4: February in non-leap years (29 invalid)
    for fmt_cat in ["dash_numeric", "slash_numeric"]:
        formats = format_types[fmt_cat]
        in_fmt, out_fmt = formats[0], formats[1]

        for year in year_categories["non_leap"][:1]:
            # Valid days
            for day in ["01", "28"]:
                date_str = build_date_string(in_fmt, year, "02", day)
                expected = build_expected(out_fmt, year, "02", day)

                test_cases.append({
                    "test_id": f"CP_{test_id:03d}",
                    "category": "february_non_leap_valid",
                    "date_input": date_str,
                    "input_format": in_fmt,
                    "output_format": out_fmt,
                    "expected_output": expected,
                    "constraint": "Feb non-leap valid",
                    "description": f"Non-leap year {year} Feb {day}"
                })
                test_id += 1

            # Invalid day 29
            date_str = build_date_string(in_fmt, year, "02", "29")
            test_cases.append({
                "test_id": f"CP_{test_id:03d}",
                "category": "february_non_leap_invalid",
                "date_input": date_str,
                "input_format": in_fmt,
                "output_format": out_fmt,
                "expected_output": None,
                "constraint": "Feb 29 non-leap invalid",
                "description": f"Non-leap year {year} Feb 29 (invalid)"
            })
            test_id += 1

    # Constraint 5: Century year leap year rules
    for fmt_cat in ["dash_numeric", "slash_numeric"]:
        formats = format_types[fmt_cat]
        in_fmt = formats[0]
        out_fmt = formats[1]

        # 2000 is leap (divisible by 400)
        date_str = build_date_string(in_fmt, "2000", "02", "29")
        expected = build_expected(out_fmt, "2000", "02", "29")
        test_cases.append({
            "test_id": f"CP_{test_id:03d}",
            "category": "century_leap",
            "date_input": date_str,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": expected,
            "constraint": "2000 is leap year",
            "description": "Year 2000 Feb 29 (valid)"
        })
        test_id += 1

        # 1900 not leap (divisible by 100 but not 400)
        date_str = build_date_string(in_fmt, "1900", "02", "29")
        test_cases.append({
            "test_id": f"CP_{test_id:03d}",
            "category": "century_non_leap",
            "date_input": date_str,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": None,
            "constraint": "1900 not leap year",
            "description": "Year 1900 Feb 29 (invalid)"
        })
        test_id += 1

    # Constraint 6: Invalid day numbers for each month type
    invalid_tests = [
        ("2024", "02", "30", "dash_numeric", "Feb 30 invalid"),
        ("2024", "04", "31", "dash_numeric", "April 31 invalid"),
        ("2024", "06", "31", "slash_numeric", "June 31 invalid"),
        ("2024", "09", "31", "dash_numeric", "September 31 invalid"),
        ("2024", "11", "31", "slash_numeric", "November 31 invalid"),
    ]

    for year, month, day, fmt_cat, desc in invalid_tests:
        formats = format_types[fmt_cat]
        in_fmt, out_fmt = formats[0], formats[1]
        date_str = build_date_string(in_fmt, year, month, day)

        test_cases.append({
            "test_id": f"CP_{test_id:03d}",
            "category": "invalid_day_for_month",
            "date_input": date_str,
            "input_format": in_fmt,
            "output_format": out_fmt,
            "expected_output": None,
            "constraint": "Invalid day for month",
            "description": desc
        })
        test_id += 1

    # Constraint 7: Text month format conversions
    text_formats = format_types["dash_text"]
    numeric_formats = format_types["dash_numeric"]

    for in_fmt in text_formats:
        for out_fmt in numeric_formats:
            for month_num, month_name in [("01", "Jan"), ("06", "Jun"), ("12", "Dec")]:
                year = "2024"
                day = "15"
                date_str = build_date_string_text_month(in_fmt, year, month_name, day)
                expected = build_expected(out_fmt, year, month_num, day)

                test_cases.append({
                    "test_id": f"CP_{test_id:03d}",
                    "category": "text_month_conversion",
                    "date_input": date_str,
                    "input_format": in_fmt,
                    "output_format": out_fmt,
                    "expected_output": expected,
                    "constraint": "Text to numeric month",
                    "description": f"Convert {month_name} to {month_num}"
                })
                test_id += 1

    # Constraint 8: Two-digit year conversions
    for in_fmt in format_types["two_digit_year"]:
        out_fmt = "D_YYYYMMDD"
        for yy, yyyy in [("24", "2024"), ("20", "2020"), ("00", "2000"), ("99", "1999")]:
            date_str = build_date_string(in_fmt, yy, "06", "15")
            expected = f"{yyyy}-06-15"

            test_cases.append({
                "test_id": f"CP_{test_id:03d}",
                "category": "two_digit_year",
                "date_input": date_str,
                "input_format": in_fmt,
                "output_format": out_fmt,
                "expected_output": expected,
                "constraint": "2-digit to 4-digit year",
                "description": f"Convert {yy} to {yyyy}"
            })
            test_id += 1

    return test_cases

def build_date_string(format_name, year, month, day):
    """Build date string based on format"""
    if "S_" in format_name:
        sep = "/"
    else:
        sep = "-"

    if format_name.startswith(("S_YYYY", "D_YYYY")):
        return f"{year}{sep}{month}{sep}{day}"
    elif format_name.startswith(("S_DD", "D_DD")):
        return f"{day}{sep}{month}{sep}{year}"
    elif format_name.startswith(("S_YY", "D_YY")):
        return f"{year}{sep}{month}{sep}{day}"
    else:
        return f"{year}{sep}{month}{sep}{day}"

def build_date_string_text_month(format_name, year, month_name, day):
    """Build date string with text month"""
    if "S_" in format_name:
        sep = "/"
    else:
        sep = "-"

    if format_name.endswith("_N"):
        if "YYYY" in format_name:
            if format_name.startswith("D_YYYY"):
                return f"{year}{sep}{month_name}{sep}{day}"
            else:
                return f"{day}{sep}{month_name}{sep}{year}"

    return f"{year}{sep}{month_name}{sep}{day}"

def build_expected(format_name, year, month, day):
    """Build expected output based on format"""
    if "S_" in format_name:
        sep = "/"
    else:
        sep = "-"

    if format_name.startswith(("S_YYYY", "D_YYYY")):
        return f"{year}{sep}{month}{sep}{day}"
    elif format_name.startswith(("S_DD", "D_DD")):
        return f"{day}{sep}{month}{sep}{year}"
    else:
        return f"{year}{sep}{month}{sep}{day}"

def save_tests_to_file(test_cases, filename="CategoryPartitionTestSet.csv"):
    """Save test cases to CSV file"""
    if not test_cases:
        return

    fieldnames = ["test_id", "category", "date_input", "input_format",
                  "output_format", "expected_output", "constraint", "description"]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(test_cases)

    print(f"✓ Generated {len(test_cases)} category-partition test cases")
    print(f"✓ Saved to {filename}")

def main():
    """Generate and save category-partition test cases"""
    print("Generating Category-Partition Test Set...")
    test_cases = generate_category_partition_tests()
    save_tests_to_file(test_cases)

    # Print summary by constraint
    constraints = {}
    for tc in test_cases:
        const = tc['constraint']
        constraints[const] = constraints.get(const, 0) + 1

    print("\nTest Cases by Constraint:")
    for const, count in sorted(constraints.items()):
        print(f"  {const}: {count} tests")

    print(f"\nSample test cases:")
    for tc in test_cases[:5]:
        print(f"{tc['test_id']}: {tc['date_input']} -> {tc['expected_output']} ({tc['constraint']})")

if __name__ == "__main__":
    main()