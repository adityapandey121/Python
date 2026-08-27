from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, registration_number, brand, model, daily_rate):
        if not registration_number or not registration_number.strip():
            raise ValueError("Registration number cannot be empty.")
        if daily_rate <= 0:
            raise ValueError("Daily rental rate must be greater than zero.")

        self.__vehicle_id = vehicle_id
        self.__registration_number = registration_number
        self.__brand = brand
        self.__model = model
        self.__daily_rate = daily_rate
        self.__available = True

    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @property
    def registration_number(self):
        return self.__registration_number

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def daily_rate(self):
        return self.__daily_rate

    @property
    def available(self):
        return self.__available

    @abstractmethod
    def calculate_rental_cost(self, days):
        raise NotImplementedError

    @abstractmethod
    def vehicle_type(self):
        raise NotImplementedError

    def display_details(self):
        status = "Available" if self.__available else "Rented"
        return (
            f"{self.vehicle_id} | {self.vehicle_type()} | "
            f"{self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:.2f}/day | {status}"
        )

    def mark_as_rented(self):
        if not self.__available:
            raise ValueError("Vehicle is already rented or reserved.")
        self.__available = False

    def mark_as_available(self):
        self.__available = True
