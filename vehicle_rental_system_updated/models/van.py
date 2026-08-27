from .vehicle import Vehicle


class Van(Vehicle):
    SERVICE_CHARGE_RATE = 0.10

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        normal_amount = self.daily_rate * days
        return normal_amount * (1 + self.SERVICE_CHARGE_RATE)

    def vehicle_type(self):
        return "Van"
