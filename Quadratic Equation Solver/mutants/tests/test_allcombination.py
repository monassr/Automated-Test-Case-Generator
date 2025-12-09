import sys
import pathlib
import csv
import pytest

from pathlib import Path

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from Solver import solve_quadratic


def load_test_set():
    
    possible_paths = [Path(__file__).resolve().parents[1] / "TestSets" / "AllCombinations.csv", Path(__file__).resolve().parents[2] / "TestSets" / "AllCombinations.csv"]
    
    test_set_path = None
    for path in possible_paths:
        if path.exists():
            test_set_path = path
            break
    
    if test_set_path is None:
        raise FileNotFoundError(f"Could not find PairWiseTestSet.csv in any of: {possible_paths}")
    
    test_cases = []
    
    with open(test_set_path, 'r') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if len(row) == 6:
                test_cases.append(row)
    
    return test_cases


def parse_expected_roots(root1_str, root2_str):
    
    # to parse complex numbers or floats
    roots = []
    
    for root_str in [root1_str, root2_str]:
        if root_str == "N/A":
            roots.append("N/A")  
        else:
            try:
                root = float(root_str)
                roots.append(root)
            except ValueError:
                try:
                    root_str = root_str.replace("(", "").replace(")", "")
                    root = complex(root_str)
                    roots.append(root)
                except ValueError:
                    roots.append("N/A")
    
    return roots


def root_to_comparable(root):
    
    if isinstance(root, complex):
        return f"{root.real:.6g}+{root.imag:.6g}j"
    elif isinstance(root, (float)):
        return f"{root:.6g}"
    
    return root

def assert_pairwise_test_case(row):
  
  
    a_str, b_str, c_str, expected_case, root1_str, root2_str = row[0], row[1], row[2], row[3], row[4], row[5]
    
    
    actual_case, actual_roots = solve_quadratic([a_str, b_str, c_str])
    
    # checking the case first
    assert actual_case == expected_case, \
        f"Case mismatch for ({a_str}, {b_str}, {c_str}): expected {expected_case}, got {actual_case}"

    
    if expected_case in ["quadratic_two_real", "quadratic_two_complex", "linear", "quadratic_one_real"]:
        
        #parsing excel expected outputs
        expected_roots = parse_expected_roots(root1_str, root2_str)
        
        
        if expected_case in ["quadratic_two_real", "quadratic_two_complex"]:
            
            actual_comparable = [root_to_comparable(r) for r in actual_roots]
            expected_comparable = [root_to_comparable(r) for r in expected_roots]
            
            # check if roots match in either order
            if (actual_comparable[0] == expected_comparable[0] and actual_comparable[1] == expected_comparable[1]) or \
                (actual_comparable[0] == expected_comparable[1] and actual_comparable[1] == expected_comparable[0]):
                pass  
            else:
                assert False, \
                    f"Root mismatch for ({a_str}, {b_str}, {c_str}): expected {expected_comparable}, got {actual_comparable}"
                    
        elif expected_case in ["linear", "quadratic_one_real"]:
            
            
            for i, (actual_root, expected_root) in enumerate(zip(actual_roots, expected_roots)):
                if expected_root == "N/A":
                    assert actual_root == "N/A", \
                        f"Root mismatch for ({a_str}, {b_str}, {c_str}), root {i}: expected 'N/A', got {actual_root}"
                else:
                    assert isinstance(actual_root, (float)), \
                        f"Root mismatch for ({a_str}, {b_str}, {c_str}), root {i}: expected numeric root, got {type(actual_root).__name__}"
                    
                    #comparing first 6 digits for simplicity
                    actual_str = f"{actual_root:.6g}"
                    expected_str = f"{expected_root:.6g}"
                    
                    assert actual_str == expected_str, \
                        f"Root mismatch for ({a_str}, {b_str}, {c_str}), root {i}: expected {expected_str}, got {actual_str}"  
                          
    
    elif expected_case in ["no_solution", "infinite_solutions", "incorrect_type", "overflow"]:
        assert actual_roots == ["N/A", "N/A"], \
            f"Expected ['N/A', 'N/A'] for {expected_case}, got {actual_roots}"


@pytest.mark.parametrize("row", load_test_set(), ids=lambda row: f"{row[0]},{row[1]},{row[2]}")
def test_pairwise_quadratic_cases_parametrized(row):

    assert_pairwise_test_case(row)
