"""
Metamorphic Test Set Generator
Generates test cases based on metamorphic relations

Metamorphic Relations (MR):
1. MR1: Round-trip conversion - A→B→A = A
2. MR2: Idempotency - Multiple conversions yield same result
3. MR3: Date arithmetic - Temporal differences preserved
4. MR4: Invalid remains invalid
5. MR5: Format component preservation
"""

import csv
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_metamorphic_tests():
    """Generate all metamorphic test cases"""
    test_cases = []

    # Generate tests for each metamorphic relation
    test_cases.extend(generate_mr1_roundtrip())
    test_cases.extend(generate_mr2_idempotency())
    test_cases.extend(generate_mr3_arithmetic())
    test_cases.extend(generate_mr4_invalid())
    test_cases.extend(generate_mr5_component())

    return test_cases

def generate_mr1_roundtrip():
    """
    MR1: Round-trip conversion
    Property: Converting A→B→A should return original A
    """
    test_cases = []
    test_id = 1

    # Test data: (seed_date, seed_format, intermediate_format)
    test_data = [
        ("2024-12-07", "D_YYYYMMDD", "S_DDMMYYYY"),
        ("07/12/2024", "S_DDMMYYYY", "D_YYYYMMDD"),
        ("2024/12/07", "S_YYYYMMDD", "D_DDMMYYYY"),
        ("07-12-2024", "D_DDMMYYYY", "S_YYYYMMDD"),
        ("2024-Dec-07", "D_YYYYMMDD_N", "S_DDMMYYYY"),
        ("07-Jan-2024", "D_DDMMYYYY_N", "D_YYYYMMDD"),
        ("24-12-07", "D_YYMMDD", "D_YYYYMMDD"),
        ("2020-02-29", "D_YYYYMMDD", "S_DDMMYYYY"),  # Leap year
        ("31/12/2024", "S_DDMMYYYY", "D_YYYYMMDD"),  # Year end
        ("01/01/2000", "S_DDMMYYYY", "D_YYYYMMDD"),  # Y2K
    ]

    for seed_date, seed_fmt, intermediate_fmt in test_data:
        test_case = {
            "test_id": f"MR1_{test_id:03d}",
            "mr_type": "Round-trip",
            "seed_input": seed_date,
            "seed_format": seed_fmt,
            "step1_format": intermediate_fmt,
            "step2_format": seed_fmt,
            "expected_property": "Final equals seed",
            "description": f"{seed_date} through {intermediate_fmt} and back"
        }
        test_cases.append(test_case)
        test_id += 1

    return test_cases

def generate_mr2_idempotency():
    """
    MR2: Idempotency
    Property: f(x) = f(f(x)) - Multiple conversions yield same result
    """
    test_cases = []
    test_id = 1

    test_data = [
        ("2024-03-15", "D_YYYYMMDD", "S_DDMMYYYY"),
        ("15/03/2024", "S_DDMMYYYY", "D_YYYYMMDD"),
        ("2024/06/15", "S_YYYYMMDD", "D_DDMMYYYY"),
        ("2020-Feb-29", "D_YYYYMMDD_N", "D_YYYYMMDD"),
        ("24-06-15", "D_YYMMDD", "D_YYYYMMDD"),
    ]

    for seed_date, seed_fmt, target_fmt in test_data:
        test_case = {
            "test_id": f"MR2_{test_id:03d}",
            "mr_type": "Idempotency",
            "seed_input": seed_date,
            "seed_format": seed_fmt,
            "step1_format": target_fmt,
            "step2_format": target_fmt,
            "expected_property": "Convert(x) = Convert(Convert(x))",
            "description": f"Convert {seed_date} twice to {target_fmt}"
        }
        test_cases.append(test_case)
        test_id += 1

    return test_cases

def generate_mr3_arithmetic():
    """
    MR3: Date arithmetic consistency
    Property: If date1 - date2 = N days, this should hold after conversion
    """
    test_cases = []
    test_id = 1

    # Date pairs with known differences
    date_pairs = [
        ("2024-01-15", "2024-01-16", 1, "Consecutive days"),
        ("2024-02-28", "2024-02-29", 1, "Leap year boundary"),
        ("2024-12-31", "2025-01-01", 1, "Year boundary"),
        ("2024-01-01", "2024-01-08", 7, "One week"),
        ("2024-06-01", "2024-06-30", 29, "Month span"),
        ("2024-01-31", "2024-02-01", 1, "Month transition"),
    ]

    for date1, date2, diff_days, description in date_pairs:
        test_case = {
            "test_id": f"MR3_{test_id:03d}",
            "mr_type": "Date arithmetic",
            "seed_input": f"{date1}|{date2}",
            "seed_format": "D_YYYYMMDD",
            "step1_format": "S_DDMMYYYY",
            "step2_format": "D_YYYYMMDD",
            "expected_property": f"Difference maintained: {diff_days} days",
            "description": description
        }
        test_cases.append(test_case)
        test_id += 1

    return test_cases

def generate_mr4_invalid():
    """
    MR4: Invalid remains invalid
    Property: Invalid dates return None regardless of format conversion
    """
    test_cases = []
    test_id = 1

    invalid_dates = [
        ("2024-02-30", "D_YYYYMMDD", "Feb 30"),
        ("2024-13-01", "D_YYYYMMDD", "Month 13"),
        ("2024-00-15", "D_YYYYMMDD", "Month 0"),
        ("2024-06-31", "D_YYYYMMDD", "June 31 (has 30)"),
        ("2024-04-31", "D_YYYYMMDD", "April 31 (has 30)"),
        ("2024-09-31", "D_YYYYMMDD", "Sep 31 (has 30)"),
        ("2024-11-31", "D_YYYYMMDD", "Nov 31 (has 30)"),
        ("32/01/2024", "S_DDMMYYYY", "Day 32"),
        ("00/01/2024", "S_DDMMYYYY", "Day 0"),
        ("15/13/2024", "S_DDMMYYYY", "Month 13"),
        ("15/00/2024", "S_DDMMYYYY", "Month 0"),
        ("2019-02-29", "D_YYYYMMDD", "Non-leap Feb 29 (2019)"),
        ("2021-02-29", "D_YYYYMMDD", "Non-leap Feb 29 (2021)"),
        ("2023-02-29", "D_YYYYMMDD", "Non-leap Feb 29 (2023)"),
        ("1900-02-29", "D_YYYYMMDD", "1900 not leap (÷100 not ÷400)"),
        ("2100-02-29", "D_YYYYMMDD", "2100 not leap (÷100 not ÷400)"),
        ("", "D_YYYYMMDD", "Empty string"),
        ("invalid-date", "D_YYYYMMDD", "Malformed"),
        ("2024/01/15", "D_YYYYMMDD", "Wrong separator"),
    ]

    for invalid_date, in_fmt, description in invalid_dates:
        # Test conversion to multiple formats
        for out_fmt in ["S_DDMMYYYY", "D_DDMMYYYY", "S_YYYYMMDD"]:
            test_case = {
                "test_id": f"MR4_{test_id:03d}",
                "mr_type": "Invalid remains invalid",
                "seed_input": invalid_date,
                "seed_format": in_fmt,
                "step1_format": out_fmt,
                "step2_format": "N/A",
                "expected_property": "Returns None",
                "description": description
            }
            test_cases.append(test_case)
            test_id += 1

            # Limit to avoid too many tests
            if test_id > 100:
                return test_cases

    return test_cases

def generate_mr5_component():
    """
    MR5: Format component preservation
    Property: Converting between similar formats preserves structure
    """
    test_cases = []
    test_id = 1

    # Test separator preservation concept
    test_data = [
        ("2024-01-15", "D_YYYYMMDD", "D_DDMMYYYY", "Dash separator preserved"),
        ("2024/01/15", "S_YYYYMMDD", "S_DDMMYYYY", "Slash separator preserved"),
        ("2024-Jan-15", "D_YYYYMMDD_N", "D_DDMMYYYY_N", "Text month with dash"),
        ("15-03-2024", "D_DDMMYYYY", "D_YYYYMMDD", "Reorder with dash"),
        ("15/03/2024", "S_DDMMYYYY", "S_YYYYMMDD", "Reorder with slash"),
    ]

    for seed_date, seed_fmt, target_fmt, description in test_data:
        test_case = {
            "test_id": f"MR5_{test_id:03d}",
            "mr_type": "Component preservation",
            "seed_input": seed_date,
            "seed_format": seed_fmt,
            "step1_format": target_fmt,
            "step2_format": seed_fmt,
            "expected_property": "Structure preserved",
            "description": description
        }
        test_cases.append(test_case)
        test_id += 1

    # Test year format preservation
    year_tests = [
        ("24-06-15", "D_YYMMDD", "S_YYMMDD", "2-digit year preserved"),
        ("2024-06-15", "D_YYYYMMDD", "S_YYYYMMDD", "4-digit year preserved"),
        ("24-06-15", "D_YYMMDD", "D_YYYYMMDD", "2-digit to 4-digit"),
        ("2024-06-15", "D_YYYYMMDD", "D_YYMMDD", "4-digit to 2-digit"),
    ]

    for seed_date, seed_fmt, target_fmt, description in year_tests:
        test_case = {
            "test_id": f"MR5_{test_id:03d}",
            "mr_type": "Component preservation",
            "seed_input": seed_date,
            "seed_format": seed_fmt,
            "step1_format": target_fmt,
            "step2_format": seed_fmt,
            "expected_property": "Year format handled",
            "description": description
        }
        test_cases.append(test_case)
        test_id += 1

    return test_cases

def save_to_csv(test_cases, filename="MetamorphicTestSet.csv"):
    """Save metamorphic test cases to CSV"""
    if not test_cases:
        return

    fieldnames = ["test_id", "mr_type", "seed_input", "seed_format",
                  "step1_format", "step2_format", "expected_property", "description"]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(test_cases)

    print(f"✓ Generated {len(test_cases)} metamorphic test cases")
    print(f"✓ Saved to {filename}")

def main():
    """Generate and save metamorphic test cases"""
    print("Generating Metamorphic Test Set...")
    print("Based on 5 metamorphic relations")

    test_cases = generate_metamorphic_tests()
    save_to_csv(test_cases)

    # Print summary by MR type
    mr_counts = {}
    for tc in test_cases:
        mr = tc['mr_type']
        mr_counts[mr] = mr_counts.get(mr, 0) + 1

    print("\nTest Cases by Metamorphic Relation:")
    for mr, count in sorted(mr_counts.items()):
        print(f"  {mr}: {count} tests")

    print(f"\nSample test cases:")
    for mr_type in ["Round-trip", "Idempotency", "Date arithmetic", "Invalid remains invalid"]:
        sample = next((tc for tc in test_cases if tc['mr_type'] == mr_type), None)
        if sample:
            print(f"  {sample['test_id']} ({mr_type}): {sample['description']}")

if __name__ == "__main__":
    main()