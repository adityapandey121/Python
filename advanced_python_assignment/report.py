from functools import wraps

from employee_processor import employee_generator, create_salary_filter


def log_execution(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"[START] {function.__name__}")
        result = function(*args, **kwargs)
        print(f"[END] {function.__name__}")
        return result

    return wrapper


class ReportFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


@log_execution
def generate_report(employees, department, min_salary):
    salary_filter = create_salary_filter(min_salary)
    selected_employees = []

    for employee in employee_generator(employees):
        if employee["department"].lower() == department.lower():
            if salary_filter(employee):
                selected_employees.append(employee)

    with ReportFile("employee_report.txt") as report:
        report.write("Employee Report\n")
        report.write("===============\n")
        report.write(f"Department: {department}\n")
        report.write(f"Minimum Salary: {min_salary}\n\n")

        for employee in selected_employees:
            report.write(
                f'{employee["id"]} - {employee["name"]} - '
                f'{employee["department"]} - {employee["salary"]}\n'
            )

    print("Report saved successfully.")
    return selected_employees


@log_execution
def calculate_average_salary(employees):
    if not employees:
        return 0

    total = 0
    for employee in employees:
        total += employee["salary"]

    return total / len(employees)
