# 0x07. Python - Test-driven development

## Description
This repository contains Python scripts and test cases developed as part of the ALX Software Engineering program. The focus of this project is on implementing Test-Driven Development (TDD) principles in Python. The tasks cover various aspects such as integer addition, matrix division, string manipulation, and more.

## Requirements
- Python 3.8.5
- pycodestyle 2.8.*
- Ubuntu 20.04 LTS

## Project Structure
The repository is organized into the following directories and files:

0x07-python-test_driven_development/
├── 0-add_integer.py
├── tests/
│ └── 0-add_integer.txt
├── 2-matrix_divided.py
├── tests/
│ └── 2-matrix_divided.txt
├── 3-say_my_name.py
├── tests/
│ └── 3-say_my_name.txt
├── 4-print_square.py
├── tests/
│ └── 4-print_square.txt
├── 5-text_indentation.py
├── tests/
│ └── 5-text_indentation.txt
└── 6-max_integer.py
└── tests/
└── 6-max_integer_test.py

## Tasks Overview

### 0. Integers Addition
- Prototype: `def add_integer(a, b=98):`
- Requirements: 
  - Add two integers
  - Handle exceptions for invalid inputs

### 1. Divide a Matrix
- Prototype: `def matrix_divided(matrix, div):`
- Requirements: 
  - Divide elements in a matrix
  - Validate matrix dimensions and divisor

### 2. Say My Name
- Prototype: `def say_my_name(first_name, last_name=""):`
- Requirements:
  - Print formatted name string
  - Handle missing last names or non-string inputs

### 3. Print Square
- Prototype: `def print_square(size):`
- Requirements:
  - Print a square pattern with specified size
  - Handle invalid input sizes

### 4. Text Indentation
- Prototype: `def text_indentation(text):`
- Requirements:
  - Format text with specific indentation rules
  - Handle non-string inputs

### 5. Max Integer - Unittest
- Prototype: `def max_integer(list=[]):`
- Requirements:
  - Write unittests for `max_integer` function
  - Test various edge cases

## How to Run Tests
To execute the test cases for each task, navigate to the project directory and run:

```bash
python3 -m doctest ./tests/*
