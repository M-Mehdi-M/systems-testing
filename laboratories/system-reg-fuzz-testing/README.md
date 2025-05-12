#  Atheris Fuzzing & Regression Testing

## Overview

This repository contains a simple task manager application and a fuzzing exercise to help you practice **pytest-regtest** and **fuzz testing with atheris**.


## Project Structure

1. `task_manager.py`: implementation of the `TaskManager` class.

    > It contains the implementation you need to test.

2. `test_task_manager.py`: contains empty test function structures.  
   You must complete these functions following the instructions provided in their docstrings.
   Use the command `pytest --regtest-reset` to generate the reference files for testing, then alter the tests and analyze error messages

3. `fuzz_task.py`: a fuzz testing file using **atheris** for discovering edge cases and exceptions in some helper functions.

## Getting Started

1. Clone this repository to your local machine.
2. Install Python and the required packages:
3. Atheris works only on Linux

```bash
pip install pytest pytest-regtest atheris
