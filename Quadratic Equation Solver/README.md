# Project Testing Guide

## Prerequisites

Make sure you have the required dependencies installed. Install them using:

```bash
pip install -r requirements.txt
```

## Running Tests with Coverage


### Step 1: Run Pytest with Coverage

Run the test suite with coverage reporting, subsitute * with the test type (pairwise, allcombination, base, metamorphic) needed to be run:
```bash
pytest tests/test_*.py --cov=Solver --cov-report=html 
```

### Step 3: View the Coverage Report

Start a local HTTP server to view the report:

```bash
python3 -m http.server 8000 --directory htmlcov
```

Then open your browser and navigate to:

```
http://localhost:8000
```



## Running Mutation Testing with Mutmut

### Clearing Cache for Mutmut Testing

It is recommended to clear cache everytime to ensure accurate results:

```bash
# Clear mutmut cache
rm -rf .mutmut-cache
```

### Step 0: Configure pytest.ini

Before running mutmut, you need to configure `pytest.ini` to specify which test file to run. Open `pytest.ini` and comment/uncomment the appropriate `addopts` line depending on which tests you want to run:

```ini
# to run pairwise mutation tests only
addopts =  --ignore=tests/test_allcombination.py --ignore=tests/test_base.py --ignore=tests/test_mutation_metamorphic.py --ignore=tests/test_metamorphic_relation.py

# to run allcombination mutation tests only
# addopts =  --ignore=tests/test_pairwise.py --ignore=tests/test_base.py --ignore=tests/test_mutation_metamorphic.py --ignore=tests/test_metamorphic_relation.py

# to run base tests only
# addopts =  --ignore=tests/test_pairwise.py --ignore=tests/test_allcombination.py --ignore=tests/test_mutation_metamorphic.py --ignore=tests/test_metamorphic_relation.py

# to run metamorphic mutation tests only
# addopts =  --ignore=tests/test_pairwise.py --ignore=tests/test_allcombination.py --ignore=tests/test_base.py --ignore=tests/test_metamorphic_relation.py
```

**Important**: Only ONE `addopts` line should be uncommented at a time.

### Step 1: Run Mutmut

Run mutation testing with timing information:

```bash
time mutmut run
```

### Step 2: View Mutmut Results

After mutmut completes, view the results in the terminal:

```bash
mutmut results
```

To save results to a text file:

```bash
mutmut results > mutmut_results.txt
```

To view results in an interactive terminal:

```bash
mutmut browse
```

This opens an interactive browser where you can explore the mutation testing results.




## Test Files Available

- `tests/test_base.py` - Base test set mutations
- `tests/test_pairwise.py` - Pairwise test set mutations
- `tests/test_metamorphic.py` - Metamorphic test mutations
- `tests/test_allcombination.py` - All combination test mutations
- `tests/test_relation.py` - Metamorphic relation tests

## Output Files

After running tests:
- `htmlcov/index.html` - Coverage report (main file to view)

