# Lab 7 – Fuzz Testing for Input Validation Bugs

This folder contains the movie-ticket input validation exercise adapted from the assigned Lab 7 repository.

## Files
- `movie_tickets.py` – hardened application containing `parse_seat`, `total_price`, and `average_rating`.
- `test_movie_tickets.py` – Hypothesis property-based fuzz tests and explicit invalid-input tests.
- `requirements.txt` – Python test dependencies.

## Setup
Use Python 3.8 or newer. From this folder, install the test dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the application
```bash
python movie_tickets.py
```

Try valid values first (for example, `H12`, `150,250,400`, and `4 5 3`). Also try malformed values to observe the input-validation messages.

## Run the fuzz tests
```bash
python -m pytest -v test_movie_tickets.py
```

The functions reject invalid input with `ValueError` rather than leaking lower-level exceptions such as `TypeError`, `IndexError`, or `ZeroDivisionError`.

## Important submission evidence
The lab handout asks for screenshots of:
1. Running the original buggy application.
2. Hypothesis finding failures against the original buggy functions.
3. Running the fixed application.
4. All fuzz tests passing against the fixed application.

Capture these screenshots from your own terminal after running the commands. The initial-bug screenshots must be taken before replacing the starter implementation with the fixed file. The repository contains the hardened final application and updated tests; screenshots have not been captured.
