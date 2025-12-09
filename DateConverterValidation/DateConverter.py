"""
Date Format Converter - Complete Working Implementation
For Date Converter Validation Testing Project
"""

from datetime import datetime
from enum import Enum

class DateFormats(Enum):
    """All supported date formats"""
    # Dash separator - numeric month
    D_YYYYMMDD = "yyyy-MM-dd"
    D_DDMMYYYY = "dd-MM-yyyy"
    D_YYMMDD = "yy-MM-dd"
    D_DDMMyy = "dd-MM-yy"

    # Dash separator - text month
    D_YYYYMMDD_N = "yyyy-MMM-dd"
    D_DDMMYYYY_N = "dd-MMM-yyyy"
    D_YYMMDD_N = "yy-MMM-dd"
    D_DDMMyy_N = "dd-MMM-yy"

    # Slash separator - numeric month
    S_YYYYMMDD = "yyyy/MM/dd"
    S_DDMMYYYY = "dd/MM/yyyy"
    S_YYMMDD = "yy/MM/dd"
    S_DDMMyy = "dd/MM/yy"

    # Slash separator - text month
    S_YYYYMMDD_N = "yyyy/MMM/dd"
    S_DDMMYYYY_N = "dd/MMM/yyyy"

    # DateTime formats (basic)
    D_YYYYMMDDHHMMA = "yyyy-MM-dd, hh:mma"
    D_DDMMYYYYHHMMA = "dd-MM-yyyy, hh:mma"
    S_YYYYMMDDHHMMA = "yyyy/MM/dd, hh:mma"
    S_DDMMYYYYHHMMA = "dd/MM/yyyy, hh:mma"

    # DateTime with seconds
    D_YYYYMMDDHHMMSSA = "yyyy-MM-dd, hh:mm:ssa"
    D_DDMMYYYYHHMMSSA = "dd-MM-yyyy, hh:mm:ssa"
    S_YYYYMMDDHHMMSSA = "yyyy/MM/dd, hh:mm:ssa"
    S_DDMMYYYYHHMMSSA = "dd/MM/yyyy, hh:mm:ssa"

def get_python_format(date_format):
    """Convert custom format string to Python strftime format"""
    if isinstance(date_format, DateFormats):
        date_format = date_format.value

    # Map custom format tokens to Python strftime tokens
    # Order matters! Replace longest patterns first
    replacements = [
        ('yyyy', '%Y'),  # 4-digit year
        ('yy', '%y'),    # 2-digit year
        ('MMM', '%b'),   # Abbreviated month name (Jan, Feb, etc.)
        ('MM', '%m'),    # 2-digit month
        ('dd', '%d'),    # 2-digit day
        ('hh', '%I'),    # 12-hour format
        ('mm', '%M'),    # Minutes
        ('ss', '%S'),    # Seconds
        ('a', '%p'),     # AM/PM
    ]

    result = date_format
    for old, new in replacements:
        result = result.replace(old, new)

    return result

def is_leap_year(year):
    """
    Check if a year is a leap year
    Rules:
    1. Divisible by 4 -> leap year
    2. BUT divisible by 100 -> not leap year
    3. BUT divisible by 400 -> leap year
    """
    try:
        year = int(year)
    except (ValueError, TypeError):
        return False

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(year, month, day):
    """
    Validate if date components form a valid date
    """
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except (ValueError, TypeError):
        return False

    # Check year range
    if year < 1 or year > 9999:
        return False

    # Check month range
    if month < 1 or month > 12:
        return False

    # Check day minimum
    if day < 1:
        return False

    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust February for leap year
    if is_leap_year(year):
        days_in_month[1] = 29

    # Check day maximum
    if day > days_in_month[month - 1]:
        return False

    return True

def convert_between_formats(date_str, from_format_name, to_format_name):
    """
    Convert date string from one format to another

    Args:
        date_str: Input date string (e.g., "2024-12-07")
        from_format_name: Name of input format (e.g., "D_YYYYMMDD")
        to_format_name: Name of output format (e.g., "S_DDMMYYYY")

    Returns:
        Converted date string or None if invalid
    """
    # Validate input
    if not date_str or not isinstance(date_str, str):
        return None

    date_str = date_str.strip()
    if not date_str:
        return None

    try:
        # Get format enums
        input_format = DateFormats[from_format_name]
        output_format = DateFormats[to_format_name]

        # Convert to Python format strings
        input_pattern = get_python_format(input_format)
        output_pattern = get_python_format(output_format)

        # Parse the input date
        dt = datetime.strptime(date_str, input_pattern)


        # Format the output date
        result = dt.strftime(output_pattern)

        # Handle AM/PM case (Python uses uppercase, we might want lowercase)
        if 'a' in output_format.value:
            result = result.replace('AM', 'am').replace('PM', 'pm')

        return result

    except (KeyError, ValueError, TypeError, AttributeError) as e:
        # KeyError: Invalid format name
        # ValueError: Date parsing failed
        # TypeError: Invalid input types
        # AttributeError: Missing attributes
        return None

def convert_date_format(date_str, input_format, output_format):
    """
    Alternative interface that accepts DateFormats enum or strings
    For compatibility with different calling patterns
    """
    # Convert enum to name if needed
    if isinstance(input_format, DateFormats):
        input_format = input_format.name
    if isinstance(output_format, DateFormats):
        output_format = output_format.name

    return convert_between_formats(date_str, input_format, output_format)

def find_format_enum(format_str):
    """Find DateFormats enum by name or value"""
    if not format_str:
        return None

    # Try by name first
    try:
        return DateFormats[format_str]
    except (KeyError, TypeError):
        pass

    # Try by value
    for fmt in DateFormats:
        if fmt.value == format_str:
            return fmt

    return None

def get_all_format_names():
    """Return list of all format names"""
    return [fmt.name for fmt in DateFormats]

def get_format_example(format_name):
    """Get an example date string for a given format"""
    examples = {
        "D_YYYYMMDD": "2024-12-07",
        "D_DDMMYYYY": "07-12-2024",
        "S_YYYYMMDD": "2024/12/07",
        "S_DDMMYYYY": "07/12/2024",
        "D_YYYYMMDD_N": "2024-Dec-07",
        "D_DDMMYYYY_N": "07-Dec-2024",
        "D_YYMMDD": "24-12-07",
        "S_YYMMDD": "24/12/07",
    }
    return examples.get(format_name, "Example not available")

# # # Quick test if run directly
# if __name__ == "__main__":
#     print("Testing DateConverter...")
#     print("=" * 60)
#
#     # Test 1: Basic conversion
#     result = convert_between_formats("2024-12-07", "D_YYYYMMDD", "S_DDMMYYYY")
#     print(f"Test 1 (Basic): {result}")
#     assert result == "07/12/2024", f"Test 1 failed: got {result}, expected 07/12/2024"
#     print("  ✓ PASSED")
#
#     # Test 2: Reverse conversion
#     result = convert_between_formats("07/12/2024", "S_DDMMYYYY", "D_YYYYMMDD")
#     print(f"Test 2 (Reverse): {result}")
#     assert result == "2024-12-07", f"Test 2 failed: got {result}, expected 2024-12-07"
#     print("  ✓ PASSED")
#
#     # Test 3: Leap year
#     result = convert_between_formats("2020-02-29", "D_YYYYMMDD", "S_DDMMYYYY")
#     print(f"Test 3 (Leap year): {result}")
#     assert result == "29/02/2020", f"Test 3 failed: got {result}, expected 29/02/2020"
#     print("  ✓ PASSED")
#
#     # Test 4: Invalid date (Feb 30)
#     result = convert_between_formats("2024-02-30", "D_YYYYMMDD", "S_DDMMYYYY")
#     print(f"Test 4 (Invalid Feb 30): {result}")
#     assert result is None, f"Test 4 failed: got {result}, expected None"
#     print("  ✓ PASSED")
#
#     # Test 5: Text month
#     result = convert_between_formats("2024-Jan-15", "D_YYYYMMDD_N", "D_YYYYMMDD")
#     print(f"Test 5 (Text month): {result}")
#     assert result == "2024-01-15", f"Test 5 failed: got {result}, expected 2024-01-15"
#     print("  ✓ PASSED")
#
#     # Test 6: Two-digit year
#     result = convert_between_formats("24-12-07", "D_YYMMDD", "D_YYYYMMDD")
#     print(f"Test 6 (2-digit year): {result}")
#     assert result == "2024-12-07", f"Test 6 failed: got {result}, expected 2024-12-07"
#     print("  ✓ PASSED")
#
#     # Test 7: Invalid month
#     result = convert_between_formats("2024-13-01", "D_YYYYMMDD", "S_DDMMYYYY")
#     print(f"Test 7 (Invalid month 13): {result}")
#     assert result is None, f"Test 7 failed: got {result}, expected None"
#     print("  ✓ PASSED")
#
#     # Test 8: Invalid day
#     result = convert_between_formats("2024-06-31", "D_YYYYMMDD", "S_DDMMYYYY")
#     print(f"Test 8 (Invalid June 31): {result}")
#     assert result is None, f"Test 8 failed: got {result}, expected None"
#     print("  ✓ PASSED")
#
#     # Test 9: Leap year validation
#     print(f"\nTest 9 (Leap year validation):")
#     assert is_leap_year(2020) == True, "2020 should be leap year"
#     print("  ✓ 2020 is leap year")
#     assert is_leap_year(2019) == False, "2019 should not be leap year"
#     print("  ✓ 2019 is not leap year")
#     assert is_leap_year(2000) == True, "2000 should be leap year"
#     print("  ✓ 2000 is leap year (divisible by 400)")
#     assert is_leap_year(1900) == False, "1900 should not be leap year"
#     print("  ✓ 1900 is not leap year (divisible by 100 but not 400)")
#
#     # Test 10: Non-leap year Feb 29
#     result = convert_between_formats("2019-02-29", "D_YYYYMMDD", "S_DDMMYYYY")
#     print(f"\nTest 10 (Non-leap Feb 29): {result}")
#     assert result is None, f"Test 10 failed: got {result}, expected None"
#     print("  ✓ PASSED")
#
#     print("\n" + "=" * 60)
#     print("✓ ALL 10 TESTS PASSED!")
#     print("=" * 60)
#     print("\nDateConverter is working correctly.")
#     print("You can now run your test suites:")
#     print("  pytest tests/test_category_partition.py -v")
#     print("  pytest tests/test_metamorphic.py -v")
#     print("  pytest tests/test_mutation_pairwise.py -v")