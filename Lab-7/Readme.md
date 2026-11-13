# Lab 7 – Fuzz Testing for Input Validation Bugs

This folder contains the assigned movie-ticket input-validation exercise. The handout uses generic filenames (`processor.py` and `test_processor.py`), but the assigned repository uses `movie_tickets.py` and `test_movie_tickets.py`, with three functions: `parse_seat`, `total_price`, and `average_rating`.

## Files
- `movie_tickets_buggy.py` – unmodified starter implementation for the before-fix demonstration.
- `test_movie_tickets_buggy.py` – Hypothesis tests aimed at the buggy implementation; these are expected to find failures.
- `movie_tickets.py` – hardened final application.
- `test_movie_tickets.py` – final Hypothesis fuzz tests and explicit invalid-input tests.
- `requirements.txt` – dependencies.

## Setup
Use Python 3.8 or newer. From this folder:

```bash
python -m pip install -r requirements.txt
```

## Before fixing: reproduce the bugs
Run the original starter application:

```bash
python movie_tickets_buggy.py
```

Then run the fuzz tests against the original functions:

```bash
python -m pytest -v test_movie_tickets_buggy.py
```

These tests are expected to fail and demonstrate edge-case problems such as non-string inputs, empty seat labels, empty CSV fields, and empty rating lists.

## After fixing: run the final application
Run:

```bash
python movie_tickets.py
python -m pytest -v test_movie_tickets.py
```

The final functions validate input and reject invalid values using `ValueError` rather than exposing lower-level exceptions such as `TypeError`, `IndexError`, or `ZeroDivisionError`.

## Screenshots required by the lab handout
Capture screenshots from your terminal for:
1. Original buggy application execution.
2. Failing Hypothesis tests against the buggy starter.
3. Fixed application execution.
4. Passing tests against the fixed application.

Put those screenshots into a PDF and save it in this folder. The code and instructions are in the repository; the screenshot PDF still needs to be generated from your own terminal runs.
