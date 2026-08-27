class Invoice:
    def __init__(self, rental, late_fee=0.0):
        self.__rental = rental
        self.__late_fee = late_fee

    @property
    def base_amount(self):
        return self.__rental.base_amount

    @property
    def late_fee(self):
        return self.__late_fee

    @property
    def final_amount(self):
        return self.base_amount + self.late_fee

    def generate_invoice(self):
        payment = self.__rental.payment_result
        transaction_id = payment.transaction_id if payment else "N/A"
        method = payment.method if payment else "N/A"

        return (
            f"Rental ID      : {self.__rental.rental_id}\n"
            f"Customer       : {self.__rental.customer.name}\n"
            f"Vehicle        : {self.__rental.vehicle.vehicle_id}\n"
            f"Rental days    : {self.__rental.days}\n"
            f"Base amount    : Rs. {self.base_amount:.2f}\n"
            f"Late fee       : Rs. {self.late_fee:.2f}\n"
            f"Final amount   : Rs. {self.final_amount:.2f}\n"
            f"Payment method : {method}\n"
            f"Transaction ID : {transaction_id}\n"
            f"Status         : {self.__rental.status}"
        )
