from rich.console import Console
from rich.table import Table
from tabulate import tabulate

from employee_system.employee import get_all_employees


def create_rich_table(employees):
    table = Table(title="Employee Details")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Department", style="yellow")
    table.add_column("Salary", style="magenta", justify="right")

    for employee in employees:
        table.add_row(
            employee["id"],
            employee["name"],
            employee["department"],
            str(employee["salary"]),
        )
    return table


def main():
    employees = get_all_employees()

    print("=" * 40)
    print("       EMPLOYEE CLI APPLICATION")
    print("=" * 40)

    print("Employee List - Tabulate")
    print("------------------------")
    print(tabulate(employees, headers="keys", tablefmt="grid"))

    print("\nEmployee List - Tabulate (simple)")
    print("---------------------------------")
    print(tabulate(employees, headers="keys", tablefmt="simple"))

    print("\nEmployee List - Rich")
    print("--------------------")
    Console().print(create_rich_table(employees))


if __name__ == "__main__":
    main()