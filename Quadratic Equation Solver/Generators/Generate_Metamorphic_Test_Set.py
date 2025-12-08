import sys
import pathlib
import csv
import random
import numpy as np

from pathlib import Path

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from Solver import solve_quadratic

random.seed(101)

f32_min = np.finfo(np.float32).min/10  
f32_max = np.finfo(np.float32).max/10  

block_values = {
    "B1": random.uniform(f32_min, -1),   # < -1
    "B2": random.uniform(-1, 0),         # >= -1 and < 0
    "B3": 0.0,                           # 0
    "B4": random.uniform(0, 1),          # >0 and <=1
    "B5": random.uniform(1, f32_max)     # >1
}
blocks = ["B1", "B2", "B3", "B4", "B5"]

tests = []
scalars = [2.0, 0.5, 10.0, -1.0, -0.1]

for x in range(5):      
    for y in range(5):  
        for z in range(5):
            a = blocks[x]
            b = blocks[y]
            c = blocks[z]
            tests.append((block_values[a], -block_values[b], block_values[c])) 
            for i in scalars:
                tests.append([(i * block_values[a]), i * block_values[b], i * block_values[c]])


OUTPUT_FILE = Path(__file__).parent.parent / "TestSets" / "MetamorphicTestSet.csv"
DELIM = ","

results = []

for test in tests:
    case, root_strs = solve_quadratic(test)
    a_val = test[0]
    b_val = test[1]
    c_val = test[2]
    root1 = root_strs[0]
    root2 = root_strs[1]
    
    results.append([a_val, b_val, c_val, case, root1, root2])
   

#output to CSV
with OUTPUT_FILE.open("w", newline="") as outfh:
    writer = csv.writer(outfh, delimiter=DELIM)
    for row in results:
        while len(row) < 6:
            row.append("N/A")
        writer.writerow(row)
print(f"Wrote results to {OUTPUT_FILE}")
