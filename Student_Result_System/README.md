# Student Result Processing System

A small Python project for practicing **Exception Handling and Logging**.

This project is based on the assignment requirements.

## What it does

The program:

1. Takes a student's name.
2. Takes the number of subjects.
3. Takes marks for every subject.
4. Checks invalid input.
5. Calculates the average.
6. Gives the result:
   - 90 - 100: Excellent
   - 75 - 89: Very Good
   - 50 - 74: Pass
   - Below 50: Fail
7. Shows highest, lowest and average marks.
8. Saves application events and errors in `student_app.log`.
9. Allows multiple students.

## Project files

```text
student_result_system/
│
├── student_result_system.py
├── student_app.log
├── answers.md
├── README.md
├── .gitignore
└── screenshots/
    ├── 01_successful_execution.png
    ├── 02_invalid_input.png
    ├── 03_invalid_marks.png
    ├── 04_generated_log.png
    ├── 05_logging_error_level.png
    └── 06_logging_debug_level.png
```

## Requirements

Python 3.10 or newer.

No external packages are required.

## How to run

Open the terminal inside this folder and run:

```bash
python student_result_system.py
```

## Logging level

At the top of `student_result_system.py`:

```python
LOG_LEVEL = logging.DEBUG
```

For the assignment's ERROR experiment, change it to:

```python
LOG_LEVEL = logging.ERROR
```

Run the program and check `student_app.log`.

Then change it back to:

```python
LOG_LEVEL = logging.DEBUG
```

Run it again and compare the log file.

## Git

The project does not contain a virtual environment or unnecessary files.

Basic commands:

```bash
git init
git add .
git commit -m "Add student result system"
```

Then connect your GitHub repository and push it.

## Note

`student_app.log` is included as a sample log file for submission. The program will also create/update this file when you run it.
