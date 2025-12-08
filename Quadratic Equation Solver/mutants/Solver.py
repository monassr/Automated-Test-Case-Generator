import cmath
import math

"""
Solve a*x^2 + b*x + c = 0.

Returns case which can be any of the below
    - 'quadratic_two_real'
    - 'quadratic_one_real' 
    - 'quadratic_two_complex'
    - 'linear' 
    - 'no_solution temp' 
    - 'infinite_solutions' 
    - 'incorrect_type' for error in the inputs

Returns the roots which can be of type complex, float, or "N/A". 
"""
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
def x_solve_quadratic__mutmut_orig(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_1(row):

    
    try:
        a = None
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_2(row):

    
    try:
        a = float(None)
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_3(row):

    
    try:
        a = float(row[1])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_4(row):

    
    try:
        a = float(row[0])
        b = None
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_5(row):

    
    try:
        a = float(row[0])
        b = float(None)
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_6(row):

    
    try:
        a = float(row[0])
        b = float(row[2])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_7(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = None
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_8(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(None)
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_9(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[3])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_10(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "XXincorrect_typeXX", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_11(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "INCORRECT_TYPE", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_12(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["XXN/AXX", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_13(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["n/a", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_14(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "XXN/AXX"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_15(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "n/a"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_16(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a != 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_17(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 1.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_18(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b != 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_19(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 1.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_20(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c != 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_21(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 1.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_22(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "XXinfinite_solutionsXX", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_23(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "INFINITE_SOLUTIONS", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_24(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["XXN/AXX", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_25(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["n/a", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_26(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "XXN/AXX"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_27(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "n/a"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_28(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "XXno_solutionXX", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_29(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "NO_SOLUTION", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_30(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["XXN/AXX", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_31(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["n/a", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_32(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "XXN/AXX"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_33(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "n/a"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_34(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = None
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_35(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c * b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_36(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = +c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_37(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "XXlinearXX", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_38(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "LINEAR", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_39(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "XXN/AXX"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_40(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "n/a"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_41(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = None
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_42(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b + 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_43(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b / b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_44(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a / c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_45(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 / a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_46(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 5 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_47(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc >= 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_48(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 1:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_49(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = None
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_50(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(None)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_51(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = None
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_52(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) * (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_53(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_54(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (+b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_55(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 / a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_56(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (3 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_57(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = None
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_58(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) * (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_59(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_60(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (+b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_61(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 / a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_62(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (3 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_63(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "XXquadratic_two_realXX", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_64(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "QUADRATIC_TWO_REAL", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_65(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc != 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_66(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 1:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_67(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = None
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_68(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b * (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_69(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = +b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_70(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 / a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_71(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (3 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_72(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "XXquadratic_one_realXX", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_73(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "QUADRATIC_ONE_REAL", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_74(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "XXN/AXX"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_75(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "n/a"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_76(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = None
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_77(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(None)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_78(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = None
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_79(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) * (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_80(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_81(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (+b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_82(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 / a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_83(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (3 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_84(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = None
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_85(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) * (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_86(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_87(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (+b - sqrt_d) / (2 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_88(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 / a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_89(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (3 * a)
        return "quadratic_two_complex", [x1, x2]
def x_solve_quadratic__mutmut_90(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "XXquadratic_two_complexXX", [x1, x2]
def x_solve_quadratic__mutmut_91(row):

    
    try:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
    except (ValueError, TypeError):
        return "incorrect_type", ["N/A", "N/A"]


    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "infinite_solutions", ["N/A", "N/A"]
            else:
                return "no_solution", ["N/A", "N/A"]
      
        root = -c / b
        return "linear", [root, "N/A"]

    disc = b * b - 4 * a * c
    if disc > 0:
        
        sqrt_d = math.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "quadratic_two_real", [x1, x2]
    elif disc == 0:
        
        x = -b / (2 * a)
        return "quadratic_one_real", [x, "N/A"]
    else:
        
        sqrt_d = cmath.sqrt(disc)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return "QUADRATIC_TWO_COMPLEX", [x1, x2]

x_solve_quadratic__mutmut_mutants : ClassVar[MutantDict] = {
'x_solve_quadratic__mutmut_1': x_solve_quadratic__mutmut_1, 
    'x_solve_quadratic__mutmut_2': x_solve_quadratic__mutmut_2, 
    'x_solve_quadratic__mutmut_3': x_solve_quadratic__mutmut_3, 
    'x_solve_quadratic__mutmut_4': x_solve_quadratic__mutmut_4, 
    'x_solve_quadratic__mutmut_5': x_solve_quadratic__mutmut_5, 
    'x_solve_quadratic__mutmut_6': x_solve_quadratic__mutmut_6, 
    'x_solve_quadratic__mutmut_7': x_solve_quadratic__mutmut_7, 
    'x_solve_quadratic__mutmut_8': x_solve_quadratic__mutmut_8, 
    'x_solve_quadratic__mutmut_9': x_solve_quadratic__mutmut_9, 
    'x_solve_quadratic__mutmut_10': x_solve_quadratic__mutmut_10, 
    'x_solve_quadratic__mutmut_11': x_solve_quadratic__mutmut_11, 
    'x_solve_quadratic__mutmut_12': x_solve_quadratic__mutmut_12, 
    'x_solve_quadratic__mutmut_13': x_solve_quadratic__mutmut_13, 
    'x_solve_quadratic__mutmut_14': x_solve_quadratic__mutmut_14, 
    'x_solve_quadratic__mutmut_15': x_solve_quadratic__mutmut_15, 
    'x_solve_quadratic__mutmut_16': x_solve_quadratic__mutmut_16, 
    'x_solve_quadratic__mutmut_17': x_solve_quadratic__mutmut_17, 
    'x_solve_quadratic__mutmut_18': x_solve_quadratic__mutmut_18, 
    'x_solve_quadratic__mutmut_19': x_solve_quadratic__mutmut_19, 
    'x_solve_quadratic__mutmut_20': x_solve_quadratic__mutmut_20, 
    'x_solve_quadratic__mutmut_21': x_solve_quadratic__mutmut_21, 
    'x_solve_quadratic__mutmut_22': x_solve_quadratic__mutmut_22, 
    'x_solve_quadratic__mutmut_23': x_solve_quadratic__mutmut_23, 
    'x_solve_quadratic__mutmut_24': x_solve_quadratic__mutmut_24, 
    'x_solve_quadratic__mutmut_25': x_solve_quadratic__mutmut_25, 
    'x_solve_quadratic__mutmut_26': x_solve_quadratic__mutmut_26, 
    'x_solve_quadratic__mutmut_27': x_solve_quadratic__mutmut_27, 
    'x_solve_quadratic__mutmut_28': x_solve_quadratic__mutmut_28, 
    'x_solve_quadratic__mutmut_29': x_solve_quadratic__mutmut_29, 
    'x_solve_quadratic__mutmut_30': x_solve_quadratic__mutmut_30, 
    'x_solve_quadratic__mutmut_31': x_solve_quadratic__mutmut_31, 
    'x_solve_quadratic__mutmut_32': x_solve_quadratic__mutmut_32, 
    'x_solve_quadratic__mutmut_33': x_solve_quadratic__mutmut_33, 
    'x_solve_quadratic__mutmut_34': x_solve_quadratic__mutmut_34, 
    'x_solve_quadratic__mutmut_35': x_solve_quadratic__mutmut_35, 
    'x_solve_quadratic__mutmut_36': x_solve_quadratic__mutmut_36, 
    'x_solve_quadratic__mutmut_37': x_solve_quadratic__mutmut_37, 
    'x_solve_quadratic__mutmut_38': x_solve_quadratic__mutmut_38, 
    'x_solve_quadratic__mutmut_39': x_solve_quadratic__mutmut_39, 
    'x_solve_quadratic__mutmut_40': x_solve_quadratic__mutmut_40, 
    'x_solve_quadratic__mutmut_41': x_solve_quadratic__mutmut_41, 
    'x_solve_quadratic__mutmut_42': x_solve_quadratic__mutmut_42, 
    'x_solve_quadratic__mutmut_43': x_solve_quadratic__mutmut_43, 
    'x_solve_quadratic__mutmut_44': x_solve_quadratic__mutmut_44, 
    'x_solve_quadratic__mutmut_45': x_solve_quadratic__mutmut_45, 
    'x_solve_quadratic__mutmut_46': x_solve_quadratic__mutmut_46, 
    'x_solve_quadratic__mutmut_47': x_solve_quadratic__mutmut_47, 
    'x_solve_quadratic__mutmut_48': x_solve_quadratic__mutmut_48, 
    'x_solve_quadratic__mutmut_49': x_solve_quadratic__mutmut_49, 
    'x_solve_quadratic__mutmut_50': x_solve_quadratic__mutmut_50, 
    'x_solve_quadratic__mutmut_51': x_solve_quadratic__mutmut_51, 
    'x_solve_quadratic__mutmut_52': x_solve_quadratic__mutmut_52, 
    'x_solve_quadratic__mutmut_53': x_solve_quadratic__mutmut_53, 
    'x_solve_quadratic__mutmut_54': x_solve_quadratic__mutmut_54, 
    'x_solve_quadratic__mutmut_55': x_solve_quadratic__mutmut_55, 
    'x_solve_quadratic__mutmut_56': x_solve_quadratic__mutmut_56, 
    'x_solve_quadratic__mutmut_57': x_solve_quadratic__mutmut_57, 
    'x_solve_quadratic__mutmut_58': x_solve_quadratic__mutmut_58, 
    'x_solve_quadratic__mutmut_59': x_solve_quadratic__mutmut_59, 
    'x_solve_quadratic__mutmut_60': x_solve_quadratic__mutmut_60, 
    'x_solve_quadratic__mutmut_61': x_solve_quadratic__mutmut_61, 
    'x_solve_quadratic__mutmut_62': x_solve_quadratic__mutmut_62, 
    'x_solve_quadratic__mutmut_63': x_solve_quadratic__mutmut_63, 
    'x_solve_quadratic__mutmut_64': x_solve_quadratic__mutmut_64, 
    'x_solve_quadratic__mutmut_65': x_solve_quadratic__mutmut_65, 
    'x_solve_quadratic__mutmut_66': x_solve_quadratic__mutmut_66, 
    'x_solve_quadratic__mutmut_67': x_solve_quadratic__mutmut_67, 
    'x_solve_quadratic__mutmut_68': x_solve_quadratic__mutmut_68, 
    'x_solve_quadratic__mutmut_69': x_solve_quadratic__mutmut_69, 
    'x_solve_quadratic__mutmut_70': x_solve_quadratic__mutmut_70, 
    'x_solve_quadratic__mutmut_71': x_solve_quadratic__mutmut_71, 
    'x_solve_quadratic__mutmut_72': x_solve_quadratic__mutmut_72, 
    'x_solve_quadratic__mutmut_73': x_solve_quadratic__mutmut_73, 
    'x_solve_quadratic__mutmut_74': x_solve_quadratic__mutmut_74, 
    'x_solve_quadratic__mutmut_75': x_solve_quadratic__mutmut_75, 
    'x_solve_quadratic__mutmut_76': x_solve_quadratic__mutmut_76, 
    'x_solve_quadratic__mutmut_77': x_solve_quadratic__mutmut_77, 
    'x_solve_quadratic__mutmut_78': x_solve_quadratic__mutmut_78, 
    'x_solve_quadratic__mutmut_79': x_solve_quadratic__mutmut_79, 
    'x_solve_quadratic__mutmut_80': x_solve_quadratic__mutmut_80, 
    'x_solve_quadratic__mutmut_81': x_solve_quadratic__mutmut_81, 
    'x_solve_quadratic__mutmut_82': x_solve_quadratic__mutmut_82, 
    'x_solve_quadratic__mutmut_83': x_solve_quadratic__mutmut_83, 
    'x_solve_quadratic__mutmut_84': x_solve_quadratic__mutmut_84, 
    'x_solve_quadratic__mutmut_85': x_solve_quadratic__mutmut_85, 
    'x_solve_quadratic__mutmut_86': x_solve_quadratic__mutmut_86, 
    'x_solve_quadratic__mutmut_87': x_solve_quadratic__mutmut_87, 
    'x_solve_quadratic__mutmut_88': x_solve_quadratic__mutmut_88, 
    'x_solve_quadratic__mutmut_89': x_solve_quadratic__mutmut_89, 
    'x_solve_quadratic__mutmut_90': x_solve_quadratic__mutmut_90, 
    'x_solve_quadratic__mutmut_91': x_solve_quadratic__mutmut_91
}

def solve_quadratic(*args, **kwargs):
    result = _mutmut_trampoline(x_solve_quadratic__mutmut_orig, x_solve_quadratic__mutmut_mutants, args, kwargs)
    return result 

solve_quadratic.__signature__ = _mutmut_signature(x_solve_quadratic__mutmut_orig)
x_solve_quadratic__mutmut_orig.__name__ = 'x_solve_quadratic'
	


