# Date Converter Validation Framework

A complete validation pipeline for testing a date-format conversion module using Base Testing, Category Partition, Pairwise Testing, and Metamorphic Testing. Includes coverage analysis, mutation testing, performance evaluation, and automatic metric collection.

---

## 1. Project Setup

### Install dependencies
pip install -r requirements.txt

### Enter the project directory
cd DateConverterValidation

---

## 2. Generate Test Sets

python Generators/Generate_Base_Test_Set.py  
python Generators/Generate_Category_Partition_Test_Set.py  
python Generators/Generate_Pair_Wise_Test_Set.py  
python Generators/Generate_Metamorphic_Test_Set.py  

---

## 3. Run Tests

### Run all tests
pytest tests/ -v

### Run specific test files
pytest tests/test_Base.py -v  
pytest tests/test_category_partition.py -v  
pytest tests/test_pairwise.py -v  
pytest tests/test_metamorphic.py -v  

### Run tests matching a keyword
pytest tests/ -k "leap"

---

## 4. Coverage Analysis

### HTML Coverage Report
pytest tests/ --cov=DateConverter --cov-report=html

### Terminal Coverage Report
pytest tests/ --cov=DateConverter --cov-report=term

### Show missing lines
coverage report -m

---

## 5. Mutation Testing (mutmut)

mutmut run --paths-to-mutate=DateConverter.py  
mutmut results  
mutmut show survived  
mutmut show 5  
mutmut html  

### Measure mutation execution time (PowerShell)
Measure-Command { mutmut run --paths-to-mutate=DateConverter.py }  
Measure-Command { mutmut run --paths-to-mutate=tests/test_pairwise.py }

---

## 6. Metrics and Analysis

python collect_metrics_for_report.py  
python run_all_tests_with_analysis.py  

---

## 7. Performance / Timing

time pytest tests/test_Base.py -q  
pytest tests/ --durations=10  

---

## Recommended Project Structure

DateConverterValidation/  
│  
├── DateConverter.py  
├── Generators/  
│   ├── Generate_Base_Test_Set.py  
│   ├── Generate_Category_Partition_Test_Set.py  
│   ├── Generate_Pair_Wise_Test_Set.py  
│   └── Generate_Metamorphic_Test_Set.py  
│  
├── tests/  
│   ├── test_Base.py  
│   ├── test_category_partition.py  
│   ├── test_pairwise.py  
│   └── test_metamorphic.py  
│  
├── collect_metrics_for_report.py  
├── run_all_tests_with_analysis.py  
├── requirements.txt  
└── README.md  

