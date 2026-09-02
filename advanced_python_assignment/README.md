# Advanced Python Assignment

## Employee Data Processing System

This project demonstrates five advanced Python concepts:

1. Iterator
2. Generator
3. Closure
4. Decorator
5. Context Manager

The program uses the employee data given in the assignment and creates an employee report based on department and minimum salary.

---

## Project Structure

```text
advanced_python_assignment/
│
├── main.py
├── employee_processor.py
├── report.py
├── employee_report.txt
└── README.md
```

---

## How to Run

Make sure Python is installed.

Open the terminal inside this folder and run:

```bash
python main.py
```

Example:

```text
Enter department: IT
Enter minimum salary: 60000
```

The program will create/update:

```text
employee_report.txt
```

---

# Concepts Used

## 1. Iterator

`EmployeeIterator` controls how employees are returned one by one.

It implements:

```python
__iter__()
__next__()
```

When there are no more employees, `__next__()` raises `StopIteration`.

### Difference between iter() and next()

`iter(employees)` gets an iterator from an iterable.

`next(iterator)` asks that iterator for the next value.

---

## 2. Generator

`employee_generator()` uses `yield`.

```python
def employee_generator(employees):
    for employee in employees:
        yield employee
```

A generator gives one value at a time instead of creating a complete result list at once.

This is useful when working with a very large amount of data because it can save memory.

---

## 3. Generator vs Iterator

Yes, a generator is an iterator.

A generator automatically provides the iterator behavior needed by `next()` and keeps track of where it stopped.

---

## 4. Closure

`create_salary_filter()` creates an inner function.

```python
def create_salary_filter(min_salary):
    def check(employee):
        return employee["salary"] >= min_salary

    return check
```

The inner `check()` function remembers `min_salary`.

For example:

```python
high_salary = create_salary_filter(60000)
```

Now `high_salary` remembers that the minimum salary is `60000`.

This happens because the inner function keeps access to the value from the outer function.

---

## 5. Decorator

`@log_execution` adds extra behavior to a function.

It prints when the function starts and when it finishes.

Example:

```python
@log_execution
def generate_report():
    ...
```

The decorator allows us to add this behavior without changing the main work done by the function.

In this project it is used on:

- `generate_report()`
- `calculate_average_salary()`

---

## 6. Context Manager

`ReportFile` is a custom context manager.

It uses:

```python
__enter__()
__exit__()
```

Example:

```python
with ReportFile("employee_report.txt") as report:
    report.write("Employee Report")
```

The file is opened in `__enter__()` and closed in `__exit__()`.

This is better than manually opening and closing the file because the cleanup happens automatically.

---

# Final Processing Flow

```text
Employee List
     |
     v
Generator
     |
     v
Filter by Department
     |
     v
Closure
     |
     v
Filter by Salary
     |
     v
Context Manager
     |
     v
Write Report
     ^
     |
Decorator logs execution
```

---

# Example

Input:

```text
Enter department: IT
Enter minimum salary: 60000
```

Output:

```text
103 - David - IT - 65000
105 - Alex - IT - 75000
```

The generated report contains:

```text
Employee Report
===============
Department: IT
Minimum Salary: 60000

103 - David - IT - 65000
105 - Alex - IT - 75000
```

---

# Bonus

The program also accepts the department and minimum salary from the user, so the report is generated dynamically.

This covers the bonus requirement from the assignment.

---

## Note

Only Python's standard library is used. No external package is required.
