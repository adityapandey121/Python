from models.rental import Rental


class RentalService:
    def __init__(self):
        self.__vehicles = []
        self.__customers = []
        self.__rentals = []
        self.__rental_counter = 1000

    @property
    def vehicles(self):
        return tuple(self.__vehicles)

    @property
    def customers(self):
        return tuple(self.__customers)

    @property
    def rentals(self):
        return tuple(self.__rentals)

    @property
    def pending_rentals(self):
        return tuple(
            r for r in self.__rentals if r.status == "Payment Pending"
        )

    @property
    def active_rentals(self):
        return tuple(
            r for r in self.__rentals if r.status == "Confirmed"
        )

    def add_vehicle(self, vehicle):
        if self.find_vehicle(vehicle.vehicle_id):
            raise ValueError("Vehicle ID already exists.")
        if any(
            v.registration_number == vehicle.registration_number
            for v in self.__vehicles
        ):
            raise ValueError("Registration number already exists.")
        self.__vehicles.append(vehicle)

    def add_customer(self, customer):
        if self.find_customer(customer.customer_id):
            raise ValueError("Customer ID already exists.")
        self.__customers.append(customer)

    def find_vehicle(self, vehicle_id):
        for vehicle in self.__vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def find_customer(self, customer_id):
        for customer in self.__customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def find_rental(self, rental_id):
        for rental in self.__rentals:
            if rental.rental_id == rental_id:
                return rental
        return None

    def display_available_vehicles(self):
        return "\n".join(
            v.display_details()
            for v in self.__vehicles
            if v.available
        )

    def search_vehicles(self, vehicle_id=None, vehicle_type=None, max_daily_rate=None):
        results = self.__vehicles

        if vehicle_id:
            results = [
                v for v in results
                if v.vehicle_id.lower() == vehicle_id.lower()
            ]
        if vehicle_type:
            results = [
                v for v in results
                if v.vehicle_type().lower() == vehicle_type.lower()
            ]
        if max_daily_rate is not None:
            results = [
                v for v in results if v.daily_rate <= max_daily_rate
            ]
        return tuple(results)

    def create_rental(self, customer, vehicle, days):
        if self.find_customer(customer.customer_id) is None:
            raise ValueError("Customer is not registered.")
        if self.find_vehicle(vehicle.vehicle_id) is None:
            raise ValueError("Vehicle is not registered.")
        if not vehicle.available:
            raise ValueError(
                "Vehicle unavailable. Please select another vehicle."
            )

        self.__rental_counter += 1
        rental = Rental(
            f"R{self.__rental_counter}",
            customer,
            vehicle,
            days
        )
        self.__rentals.append(rental)
        return rental

    def make_payment(self, rental_id, payment_processor):
        rental = self.find_rental(rental_id)
        if rental is None:
            raise ValueError("Rental not found.")

        result = payment_processor.process_payment(rental.base_amount)

        if not result.success:
            rental.complete_payment_failure()
            raise ValueError(result.message)

        rental.confirm_payment(result)

    def return_vehicle(self, rental_id, return_date):
        rental = self.find_rental(rental_id)
        if rental is None:
            raise ValueError("Rental not found.")
        return rental.complete_rental(return_date)
