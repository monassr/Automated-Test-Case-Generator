import sys
import pathlib
import csv
import pytest
import math
from pathlib import Path

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from Solver import solve_quadratic

def load_test_set():
    
    possible_paths = [
        Path(__file__).resolve().parents[1] / "TestSets" / "AllCombinations.csv", Path(__file__).resolve().parents[2] / "TestSets" / "AllCombinations.csv",
    ]
    
    test_set_path = None
    for path in possible_paths:
        if path.exists():
            test_set_path = path
            break
    
    if test_set_path is None:
        raise FileNotFoundError(f"Could not find file in any of: {possible_paths}")
    
    test_cases = []
    
    with open(test_set_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 6:
                test_cases.append(row)

    return test_cases

# def parse_root(root_str):

#     if root_str == "N/A":
#         return "N/A"
#     try:
#         return float(root_str)
#     except ValueError:
#         try:
#             root_str = root_str.replace("(", "").replace(")", "")
#             return complex(root_str)
#         except ValueError:
#             return "N/A"


def normalize_zero(val):
    
    #to convert -0.0 to 0.0
    if val == 0.0:
        return 0.0
    return val


def roots_equal(root1, root2):
    
    if root1 == "N/A" and root2 == "N/A":
        return True
    if root1 == "N/A" or root2 == "N/A":
        return False
    
    if isinstance(root1, complex) or isinstance(root2, complex) or 'j' in str(root1) or 'j' in str(root2):
        root1_c = complex(root1) if not isinstance(root1, complex) else root1
        root2_c = complex(root2) if not isinstance(root2, complex) else root2
        
        
        root1_real = normalize_zero(root1_c.real)
        root1_imag = normalize_zero(root1_c.imag)
        root2_real = normalize_zero(root2_c.real)
        root2_imag = normalize_zero(root2_c.imag)
        
        #comparing first 6 significant digits
        real_str1 = f"{root1_real:.6g}"
        real_str2 = f"{root2_real:.6g}"
        imag_str1 = f"{root1_imag:.6g}"
        imag_str2 = f"{root2_imag:.6g}"
        return real_str1 == real_str2 and imag_str1 == imag_str2
    
    root1_f = float(root1)
    root2_f = float(root2)
    
    # Normalize -0 to 0
    root1_f = normalize_zero(root1_f)
    root2_f = normalize_zero(root2_f)
    root1_str = f"{root1_f:.6g}"
    root2_str = f"{root2_f:.6g}"
    
    return root1_str == root2_str
    
def negate_root(root):
    
    if root == "N/A":
        return "N/A"
    
    if isinstance(root, complex):
        negated_real = -root.real
        negated_imag = -root.imag
    else:
        negated_real = -float(root)
        negated_imag = 0.0
    

    negated_real = normalize_zero(negated_real)
    negated_imag = normalize_zero(negated_imag)
        
    if isinstance(root, complex):
        
        real_part = float(f"{negated_real:.6g}")
        imag_part = float(f"{negated_imag:.6g}")
        
        real_part = normalize_zero(real_part)
        imag_part = normalize_zero(imag_part)
        
        return complex(real_part, imag_part)
    else:
        result = float(f"{negated_real:.6g}")
        
        return normalize_zero(result)



def _generate_mr1_test_cases():
    """Generate (row, scalar) tuples for all MR1 tests"""
    test_cases = load_test_set()
    scalars = [2.0, 0.5, 10.0, -1.0, -0.1]
    mr1_cases = []
    for row in test_cases:
        for scalar in scalars:
            mr1_cases.append((row, scalar))
    return mr1_cases

"""
MR1: Multiplying all inputs by non-zero scalar k should produce same roots
solve_quadratic(a, b, c) = (case, [x1, x2]) should be same as solve_quadratic(k*a, k*b, k*c) = (case, [x1, x2]) for any k ≠ 0
"""
@pytest.mark.parametrize("row,scalar", _generate_mr1_test_cases())
def test_mr1_scalar_multiplication(row, scalar):
  
    a_str, b_str, c_str, expected_case, root1_str, root2_str = row[0], row[1], row[2], row[3], row[4], row[5]
    k = scalar
    
    # Original test case
    original_case, original_roots = solve_quadratic([a_str, b_str, c_str])
    
    if original_case in ["incorrect_type"]:
        pytest.skip("Skipping MR1 for incorrect_type cases")
    
    # Scale the inputs
    a_scaled = float(a_str) * k
    b_scaled = float(b_str) * k
    c_scaled = float(c_str) * k
    
    scaled_case, scaled_roots = solve_quadratic([str(a_scaled), str(b_scaled), str(c_scaled)])
    
    # checking the case first
    assert scaled_case == original_case, \
        f"MR1 failed: Case changed from {original_case} to {scaled_case} when multiplied by {k}"
    

    if original_case in ["quadratic_two_real", "quadratic_two_complex"]:
    
        match_forward = (roots_equal(original_roots[0], scaled_roots[0]) and roots_equal(original_roots[1], scaled_roots[1]))
        match_reversed = (roots_equal(original_roots[0], scaled_roots[1]) and roots_equal(original_roots[1], scaled_roots[0]))
        
        assert match_forward or match_reversed, \
            f"MR1 failed: Roots changed from {original_roots} to {scaled_roots} when multiplied by {k}"
            
    elif original_case in ["linear", "quadratic_one_real"]:

        for i, (orig_root, scaled_root) in enumerate(zip(original_roots, scaled_roots)):
            
            if orig_root != "N/A" and scaled_root != "N/A":
                assert roots_equal(orig_root, scaled_root), \
                    f"MR1 failed: Root {i} changed from {orig_root} to {scaled_root} when multiplied by {k}"
                    
    elif original_case in ["no_solution", "infinite_solutions"]:
        assert scaled_roots == ["N/A", "N/A"], \
            f"MR1 failed: Expected ['N/A', 'N/A'] for {original_case}, got {scaled_roots}"

"""
MR2: Negating only 'b' should negate the roots (swap their signs)
solve_quadratic(a, b, c) = (case, [x1, x2]) then solve_quadratic(a, -b, c) = (case, [-x1, -x2])
"""
@pytest.mark.parametrize("row", load_test_set())
def test_mr2_negate_b(row):

    a_str, b_str, c_str, expected_case, root1_str, root2_str = row[0], row[1], row[2], row[3], row[4], row[5]
    
   
    original_case, original_roots = solve_quadratic([a_str, b_str, c_str])
    if original_case in ["incorrect_type"]:
        pytest.skip("Skipping MR2 for incorrect_type cases")
    
    # negating b
    b_negated = -float(b_str)
    negated_case, negated_roots = solve_quadratic([a_str, str(b_negated), c_str])
    
    # checking the case first
    assert negated_case == original_case, \
        f"MR2 failed: Case changed from {original_case} to {negated_case} when b is negated"
    

    if original_case in ["quadratic_two_real", "quadratic_two_complex"]:
        expected_negated = [negate_root(r) for r in original_roots]
        
        match_forward = (roots_equal(negated_roots[0], expected_negated[0]) and  roots_equal(negated_roots[1], expected_negated[1]))
        match_reversed = (roots_equal(negated_roots[0], expected_negated[1]) and roots_equal(negated_roots[1], expected_negated[0]))
        
        assert match_forward or match_reversed, \
            f"MR2 failed: Expected negated roots {expected_negated} but got {negated_roots}"
            
    elif original_case in ["linear", "quadratic_one_real"]:
      
        for i, (orig_root, negated_root) in enumerate(zip(original_roots, negated_roots)):
            
            if orig_root != "N/A" and negated_root != "N/A":
                expected_negated = negate_root(orig_root)
                assert roots_equal(negated_root, expected_negated), \
                    f"MR2 failed: Root {i} should be {expected_negated} but got {negated_root}"
                    
    elif original_case in ["no_solution", "infinite_solutions"]:
        assert negated_roots == ["N/A", "N/A"], \
            f"MR2 failed: Expected ['N/A', 'N/A'] for {original_case}, got {negated_roots}"

