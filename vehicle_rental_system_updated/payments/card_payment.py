from uuid import uuid4
from payments.payment_processor import PaymentProcessor
from payments.payment_result import PaymentResult


class CardPayment(PaymentProcessor):
    def __init__(self, last_four_digits):
        if len(last_four_digits) != 4 or not last_four_digits.isdigit():
            raise ValueError("Enter exactly 4 digits of the card.")
        self.__last_four_digits = last_four_digits

    def process_payment(self, amount):
        transaction_id = f"CARD-{uuid4().hex[:8].upper()}"
        return PaymentResult(
            True,
            transaction_id,
            "Card",
            f"Card payment of Rs. {amount:.2f} successful."
        )
