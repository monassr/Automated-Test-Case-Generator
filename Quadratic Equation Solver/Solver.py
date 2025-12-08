import cmath
import math

"""
Solve a*x^2 + b*x + c = 0.

Returns case which can be any of the below
    - 'quadratic_two_real'
    - 'quadratic_one_real' 
    - 'quadratic_two_complex'
    - 'linear' 
    - 'no_solution' 
    - 'infinite_solutions' 
    - 'incorrect_type' for error in the inputs

Returns the roots which can be of type complex, float, or "N/A". 
"""
def solve_quadratic(row):

    
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
	


