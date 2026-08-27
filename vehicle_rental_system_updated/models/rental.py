from datetime import date, timedelta
from models.invoice import Invoice


class Rental:
    LATE_FEE_RATE = 0.20

    def __init__(self, rental_id, customer, vehicle, days, rental_date=None):
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        self.__rental_id = rental_id
        self.__customer = customer
        self.__vehicle = vehicle
        self.__days = days
        self.__rental_date = rental_date or date.today()
        self.__due_date = self.__rental_date + timedelta(days=days)
        self.__base_amount = vehicle.calculate_rental_cost(days)
        self.__late_fee = 0.0
        self.__invoice = None
        self.__payment_result = None

        self.__vehicle.mark_as_rented()
        self.__status = "Payment Pending"

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def customer(self):
        return self.__customer

    @property
    def vehicle(self):
        return self.__vehicle

    @property
    def days(self):
        return self.__days

    @property
    def rental_date(self):
        return self.__rental_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def base_amount(self):
        return self.__base_amount

    @property
    def late_fee(self):
        return self.__late_fee

    @property
    def invoice(self):
        return self.__invoice

    @property
    def payment_result(self):
        return self.__payment_result

    @property
    def status(self):
        return self.__status

    def confirm_payment(self, payment_result):
        if self.__status != "Payment Pending":
            raise ValueError("This rental is not waiting for payment.")

        if not payment_result.success:
            self.__vehicle.mark_as_available()
            self.__status = "Payment Failed"
            raise ValueError(payment_result.message)

        self.__payment_result = payment_result
        self.__status = "Confirmed"

    def complete_payment_failure(self):
        if self.__status == "Payment Pending":
            self.__vehicle.mark_as_available()
            self.__status = "Payment Failed"

    def complete_rental(self, return_date):
        if self.__status != "Confirmed":
            raise ValueError("Only confirmed rentals can be completed.")

        if return_date < self.__rental_date:
            raise ValueError("Return date cannot be before rental date.")

        late_days = max(0, (return_date - self.__due_date).days)
        self.__late_fee = (
            late_days * self.__vehicle.daily_rate * self.LATE_FEE_RATE
        )

        self.__invoice = Invoice(self, self.__late_fee)
        self.__status = "Returned"
        self.__vehicle.mark_as_available()
        self.__customer.add_rental(self)

        return self.__invoice

    def display_summary(self):
        return (
            f"{self.rental_id} | {self.vehicle.vehicle_type()} | "
            f"{self.vehicle.vehicle_id} | {self.days} days | "
            f"Rs. {self.base_amount:.2f} | {self.status}"
        )
