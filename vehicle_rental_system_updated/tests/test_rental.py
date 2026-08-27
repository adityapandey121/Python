import unittest
from datetime import date, timedelta

from models.car import Car
from models.bike import Bike
from models.customer import Customer
from payments.card_payment import CardPayment
from services.rental_service import RentalService


class TestVehicleRentalSystem(unittest.TestCase):
    def setUp(self):
        self.service = RentalService()
        self.car = Car("V101", "KA01AB1234", "Toyota", "Innova", 2000)
        self.bike = Bike("V102", "KA01CD5678", "Yamaha", "FZ", 700)
        self.customer = Customer(
            "C101", "Ananya Sharma",
            "ananya@example.com", "DL123456"
        )
        self.service.add_vehicle(self.car)
        self.service.add_vehicle(self.bike)
        self.service.add_customer(self.customer)

    def test_car_cost(self):
        self.assertEqual(self.car.calculate_rental_cost(3), 6000)

    def test_bike_discount(self):
        self.assertEqual(self.bike.calculate_rental_cost(6), 3990)

    def test_double_rental_blocked(self):
        rental = self.service.create_rental(self.customer, self.car, 3)
        self.service.make_payment(rental.rental_id, CardPayment("1234"))

        other = Customer("C102", "Rahul", "rahul@example.com", "DL654321")
        self.service.add_customer(other)

        with self.assertRaises(ValueError):
            self.service.create_rental(other, self.car, 2)

    def test_late_fee(self):
        rental = self.service.create_rental(self.customer, self.car, 3)
        self.service.make_payment(rental.rental_id, CardPayment("1234"))

        invoice = self.service.return_vehicle(
            rental.rental_id,
            date.today() + timedelta(days=4)
        )

        self.assertEqual(invoice.late_fee, 400)
        self.assertEqual(invoice.final_amount, 6400)

    def test_invalid_days(self):
        with self.assertRaises(ValueError):
            self.service.create_rental(self.customer, self.car, 0)


if __name__ == "__main__":
    unittest.main()
