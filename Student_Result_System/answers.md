# Assignment Answers

## 1. What is exception handling?

Exception handling is a way to handle errors in a program without stopping the whole program. In Python, we normally use `try` and `except` for this.

## 2. Why should we use exception handling?

It prevents the program from crashing when something unexpected happens. For example, if the user enters `abc` where a number is expected, the program can show a friendly message instead of crashing.

## 3. Difference between `try` and `except`

The `try` block contains code that may cause an exception.

The `except` block handles the exception if it happens.

## 4. When is the `else` block executed?

The `else` block runs when the code inside `try` finishes without an exception.

## 5. When is the `finally` block executed?

The `finally` block runs whether an exception occurs or not. It is useful for code that should always run, such as cleanup or a final status message.

## 6. What is logging?

Logging means recording useful information about what happens inside an application. It helps us understand normal events, warnings, errors, and serious failures.

## 7. Difference between `print()` and logging

`print()` is mainly used to show information directly to the user.

Logging is used to record application events and errors. Logs can be saved in a file and checked later.

## 8. What happens when the logging level is `ERROR`?

Only `ERROR` and `CRITICAL` messages are recorded.

`DEBUG`, `INFO`, and `WARNING` are ignored at that level.

## 9. What happens if we do not handle `ValueError` with `int()`?

If the user enters something such as `abc`, `int("abc")` raises a `ValueError`. If it is not handled, the program stops with an error message.

## 10. Why avoid `except: pass`?

It hides errors. The program may continue, but we will not know what went wrong.

It is better to catch a specific exception and either show a useful message or record the error in the log.

## 11. Why is logging useful in a production application?

A production application may run without a developer watching it. Logs help developers find problems, understand what happened, and troubleshoot errors later.

## 12. What is the purpose of the `finally` block?

The `finally` block is used for code that must run at the end of processing, whether the operation succeeds or fails.

---

# Logging Level Experiment

The assignment asks us to compare `ERROR` and `DEBUG`.

In `student_result_system.py`, change:

```python
LOG_LEVEL = logging.DEBUG
```

to:

```python
LOG_LEVEL = logging.ERROR
```

Run the program again and check `student_app.log`.

### With `ERROR`

Recorded:

- DEBUG: No
- INFO: No
- WARNING: No
- ERROR: Yes
- CRITICAL: Yes

### With `DEBUG`

All normal levels are recorded:

- DEBUG: Yes
- INFO: Yes
- WARNING: Yes
- ERROR: Yes
- CRITICAL: Yes

The logging level works like a minimum level. Python records that level and more serious levels above it.

---

# How this project meets the assignment

- Student name is accepted.
- Number of subjects is accepted.
- Marks are accepted for each subject.
- Invalid numbers are handled with `ValueError`.
- Marks outside 0 to 100 are rejected.
- Average is calculated using a separate function.
- Result is calculated using a separate function.
- Multiple students can be processed.
- `try`, `except`, `else`, and `finally` are used.
- `ZeroDivisionError` is handled.
- Python's built-in `logging` module is used.
- Logs are written to `student_app.log`.
- DEBUG, INFO, WARNING, ERROR and CRITICAL levels are demonstrated by the logging configuration and experiment.
- Highest mark, lowest mark and average are displayed as the bonus task.

