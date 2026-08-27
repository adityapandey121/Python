# Employee Management System

This assignment contains two independent Python applications. Each application has its own `employee_system` package and its own `.venv`.

## Projects

### HR Report Generator

Run it from `hr_report_generator` with `\.venv\Scripts\python.exe app.py`. It loads `templates/employee_report.txt` with Jinja2 and builds the employee table with PrettyTable.

### Employee CLI Application

Run it from `employee_cli` with `\.venv\Scripts\python.exe app.py`. It displays the same employees with Tabulate in grid and simple formats, then displays them with a styled Rich table.

## Documentation Questions

1. **What is a module?** A module is a Python file containing reusable code, such as functions, data, or classes. `employee.py` is a module.
2. **What is a package?** A package is a directory of related Python modules. The `employee_system` directory is a package because it contains `__init__.py` and the three modules.
3. **What is a virtual environment?** It is an isolated Python environment with its own interpreter and installed packages.
4. **Why are two virtual environments used?** The projects are independent and need different libraries. Separate environments prevent their dependencies from affecting one another.
5. **What is Jinja2 used for?** Jinja2 fills placeholders in a template with changing data, which creates the employee report text.
6. **What is PrettyTable used for?** PrettyTable creates an ASCII box-style table without manually drawing table borders.
7. **What is Tabulate used for?** Tabulate converts rows of data into several text table styles, such as `grid` and `simple`.
8. **What is Rich used for?** Rich creates styled terminal output, including colored and aligned tables.
9. **What is `requirements.txt`?** It records the packages and versions a project needs so another environment can install the same dependencies.
10. **Why should package versions be specified?** A pinned version makes installations repeatable and protects a tested application from unexpected library changes.

## Library Comparison

| Library | Purpose | Output |
| --- | --- | --- |
| Jinja2 | Template-based report generation | Dynamic text |
| PrettyTable | Table formatting | ASCII box table |
| Tabulate | CLI table formatting | Multiple table styles |
| Rich | Rich terminal UI | Styled terminal table |

The company should choose Jinja2 when it needs reusable report templates, PrettyTable for a straightforward fixed ASCII table, Tabulate when it wants quick table-format choices, and Rich when the terminal interface should be more readable and visually styled.

## Environment Isolation Demonstration

The HR environment contains Jinja2 and PrettyTable. The CLI environment contains tabulate and rich. From the project root, these checks show the separation:

```powershell
hr_report_generator\.venv\Scripts\python.exe -c "import jinja2, prettytable; print('HR libraries available')"
hr_report_generator\.venv\Scripts\python.exe -c "import rich"
employee_cli\.venv\Scripts\python.exe -c "import tabulate, rich; print('CLI libraries available')"
employee_cli\.venv\Scripts\python.exe -c "import jinja2"
```

The first and third commands succeed. The second and fourth commands fail with `ModuleNotFoundError`, proving that installing a package in one project does not install it in the other.

## Dependency Versions and Recreation

Both `requirements.txt` files contain exact versions captured with `pip freeze`. The HR project pins PrettyTable explicitly because it was tested with that version. To recreate either project in PowerShell:

```powershell
Remove-Item -Recurse -Force .venv
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
deactivate
```

Run those steps inside each project directory, using that project's own `requirements.txt`. The recreated environments produce the same application output.

## Final Concept

Each Python application uses modules. Related modules are grouped into the `employee_system` package. Third-party libraries extend each application, while separate virtual environments keep each project's dependency versions isolated. A global installation of all four libraries could cause version conflicts and make it difficult to reproduce either application reliably.