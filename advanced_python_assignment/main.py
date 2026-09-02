from employee_processor import (
    employees,
    EmployeeIterator,
    employee_generator,
    filter_by_department,
    create_salary_filter,
)
from report import generate_report, calculate_average_salary


def show_iterator():
    print("----- Iterator Example -----")

    iterator = EmployeeIterator(employees)

    for employee in iterator:
        print(employee["name"])

    print()


def show_generator():
    print("----- Generator Example -----")

    for employee in employee_generator(employees):
        print(employee["name"])

    print()


def show_department_filter():
    print("----- IT Employees -----")

    for employee in filter_by_department(employees, "IT"):
        print(employee["name"])

    print()


def show_closure():
    print("----- Salary Filter Example -----")

    high_salary = create_salary_filter(60000)

    print("John:", high_salary(employees[0]))
    print("David:", high_salary(employees[2]))
    print()


def main():
    show_iterator()
    show_generator()
    show_department_filter()
    show_closure()

    print("----- Employee Report -----")

    department = input("Enter department: ").strip()

    try:
        min_salary = int(input("Enter minimum salary: "))
    except ValueError:
        print("Please enter a valid salary.")
        return

    selected_employees = generate_report(
        employees,
        department,
        min_salary,
    )

    average_salary = calculate_average_salary(selected_employees)

    print()
    print("Selected Employees:")

    for employee in selected_employees:
        print(
            f'{employee["id"]} - {employee["name"]} - '
            f'{employee["department"]} - {employee["salary"]}'
        )

    print(f"Average Salary: {average_salary:.2f}")


if __name__ == "__main__":
    main()
