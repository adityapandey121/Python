from models.car import Car
from models.bike import Bike
from models.van import Van
from models.customer import Customer
from payments.card_payment import CardPayment
from payments.upi_payment import UPIPayment
from services.rental_service import RentalService


def menu():
    print("\n" + "=" * 50)
    print("       VEHICLE RENTAL MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Vehicle")
    print("2. Add Customer")
    print("3. Show Available Vehicles")
    print("4. Show Customers")
    print("5. Search Vehicles")
    print("6. Rent Vehicle")
    print("7. Make Payment")
    print("8. Return Vehicle & Print Invoice")
    print("9. Show Rental History")
    print("10. Exit")
    print("=" * 50)


def add_vehicle(service):
    print("\n--- ADD VEHICLE ---")
    kind = input("Vehicle type (Car/Bike/Van): ").strip().lower()
    try:
        vehicle_id = input("Vehicle ID: ").strip()
        registration = input("Registration number: ").strip()
        brand = input("Brand: ").strip()
        model = input("Model: ").strip()
        rate = float(input("Daily rental rate: "))

        classes = {"car": Car, "bike": Bike, "van": Van}
        if kind not in classes:
            print("Invalid vehicle type.")
            return

        vehicle = classes[kind](
            vehicle_id, registration, brand, model, rate
        )
        service.add_vehicle(vehicle)
        print("Vehicle added successfully.")
    except ValueError as error:
        print(f"Error: {error}")


def add_customer(service):
    print("\n--- ADD CUSTOMER ---")
    try:
        customer = Customer(
            input("Customer ID: ").strip(),
            input("Name: ").strip(),
            input("Email: ").strip(),
            input("Driving licence number: ").strip()
        )
        service.add_customer(customer)
        print("Customer added successfully.")
    except ValueError as error:
        print(f"Error: {error}")


def show_customers(service):
    print("\n--- CUSTOMERS ---")
    if not service.customers:
        print("No customers found.")
        return
    for customer in service.customers:
        print(customer.display_details())


def show_available_vehicles(service):
    print("\n--- AVAILABLE VEHICLES ---")
    output = service.display_available_vehicles()
    print(output if output else "No vehicles are currently available.")


def search_vehicles(service):
    print("\n--- SEARCH VEHICLES ---")
    print("1. By Vehicle ID")
    print("2. By Vehicle Type")
    print("3. By Maximum Daily Rate")
    choice = input("Choice: ").strip()

    try:
        if choice == "1":
            results = service.search_vehicles(
                vehicle_id=input("Vehicle ID: ").strip()
            )
        elif choice == "2":
            results = service.search_vehicles(
                vehicle_type=input("Vehicle type: ").strip()
            )
        elif choice == "3":
            results = service.search_vehicles(
                max_daily_rate=float(input("Maximum daily rate: "))
            )
        else:
            print("Invalid choice.")
            return
    except ValueError:
        print("Enter a valid value.")
        return

    if not results:
        print("No matching vehicles found.")
        return
    for vehicle in results:
        print(vehicle.display_details())


def rent_vehicle(service):
    print("\n--- RENT VEHICLE ---")
    customer = service.find_customer(input("Customer ID: ").strip())
    if customer is None:
        print("Customer not found.")
        return

    vehicle = service.find_vehicle(input("Vehicle ID: ").strip())
    if vehicle is None:
        print("Vehicle not found.")
        return

    try:
        days = int(input("Rental days: "))
        rental = service.create_rental(customer, vehicle, days)

        print("\nRental created.")
        print(f"Rental ID: {rental.rental_id}")
        print(f"Base amount: Rs. {rental.base_amount:.2f}")
        print("Status: Payment Pending")
        print("Use option 7 to make payment.")
    except ValueError as error:
        print(f"Error: {error}")


def make_payment(service):
    print("\n--- MAKE PAYMENT ---")
    pending = service.pending_rentals

    if not pending:
        print("No payment-pending rentals.")
        return

    for rental in pending:
        print(
            f"{rental.rental_id} | {rental.customer.name} | "
            f"{rental.vehicle.vehicle_id} | "
            f"Rs. {rental.base_amount:.2f}"
        )

    rental_id = input("Rental ID: ").strip()
    rental = service.find_rental(rental_id)

    if rental is None or rental.status != "Payment Pending":
        print("Payment-pending rental not found.")
        return

    print("1. Card")
    print("2. UPI")
    choice = input("Payment method: ").strip()

    try:
        if choice == "1":
            processor = CardPayment(
                input("Last 4 card digits: ").strip()
            )
        elif choice == "2":
            processor = UPIPayment(
                input("UPI ID: ").strip()
            )
        else:
            print("Invalid payment method.")
            return

        service.make_payment(rental_id, processor)
        print("Payment successful.")
        print(f"Transaction ID: {rental.payment_result.transaction_id}")
        print(f"Rental status: {rental.status}")
    except ValueError as error:
        print(f"Payment failed: {error}")


def return_vehicle(service):
    print("\n--- RETURN VEHICLE ---")
    active = service.active_rentals

    if not active:
        print("No active rentals.")
        return

    for rental in active:
        print(
            f"{rental.rental_id} | {rental.customer.name} | "
            f"{rental.vehicle.vehicle_id} | Due: {rental.due_date}"
        )

    rental_id = input("Rental ID: ").strip()
    rental = service.find_rental(rental_id)

    if rental is None:
        print("Rental not found.")
        return

    try:
        raw_date = input(
            "Return date YYYY-MM-DD (Enter for today): "
        ).strip()

        from datetime import date
        return_date = date.fromisoformat(raw_date) if raw_date else date.today()

        invoice = service.return_vehicle(rental_id, return_date)

        print("\n" + "=" * 45)
        print("              FINAL INVOICE")
        print("=" * 45)
        print(invoice.generate_invoice())
        print("=" * 45)
    except ValueError as error:
        print(f"Error: {error}")


def show_history(service):
    print("\n--- RENTAL HISTORY ---")
    if not service.rentals:
        print("No rental records.")
        return
    for rental in service.rentals:
        print(rental.display_summary())


def main():
    service = RentalService()

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_vehicle(service)
        elif choice == "2":
            add_customer(service)
        elif choice == "3":
            show_available_vehicles(service)
        elif choice == "4":
            show_customers(service)
        elif choice == "5":
            search_vehicles(service)
        elif choice == "6":
            rent_vehicle(service)
        elif choice == "7":
            make_payment(service)
        elif choice == "8":
            return_vehicle(service)
        elif choice == "9":
            show_history(service)
        elif choice == "10":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please select 1-10.")


if __name__ == "__main__":
    main()
