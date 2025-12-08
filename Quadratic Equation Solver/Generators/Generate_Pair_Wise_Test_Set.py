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

# OA(25,3,5,2)
OA = [
    [0,0,0], [0,1,1], [0,2,2], [0,3,3], [0,4,4],
    [1,0,1], [1,1,2], [1,2,3], [1,3,4], [1,4,0],
    [2,0,2], [2,1,3], [2,2,4], [2,3,0], [2,4,1],
    [3,0,3], [3,1,4], [3,2,0], [3,3,1], [3,4,2],
    [4,0,4], [4,1,0], [4,2,1], [4,3,2], [4,4,3]
]

tests = []

for row in OA:
    a = blocks[row[0]]
    b = blocks[row[1]]
    c = blocks[row[2]]
    tests.append((
        block_values[a],
        block_values[b],
        block_values[c]
    ))


OUTPUT_FILE = Path(__file__).parent.parent / "TestSets/PairWiseTestSet.csv"
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
        writer.writerow(row)
print(f"Wrote results to {OUTPUT_FILE}")