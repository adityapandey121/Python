from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from prettytable import PrettyTable

from employee_system.employee import get_all_employees


def create_report(employee):
    template_folder = Path(__file__).parent / "templates"
    environment = Environment(loader=FileSystemLoader(template_folder))
    template = environment.get_template("employee_report.txt")
    return template.render(employee=employee)


def create_employee_table(employees):
    table = PrettyTable(["ID", "Name", "Department", "Salary"])
    for employee in employees:
        table.add_row([
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"],
        ])
    return table


def main():
    employees = get_all_employees()

    print("=" * 40)
    print("        HR EMPLOYEE REPORT")
    print("=" * 40)

    for employee in employees:
        print(create_report(employee))

    print("Employee Table")
    print("==============")
    print(create_employee_table(employees))


if __name__ == "__main__":
    main()