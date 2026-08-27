from uuid import uuid4
from payments.payment_processor import PaymentProcessor
from payments.payment_result import PaymentResult


class UPIPayment(PaymentProcessor):
    def __init__(self, upi_id):
        if not upi_id or "@" not in upi_id:
            raise ValueError("Enter a valid UPI ID.")
        self.__upi_id = upi_id

    def process_payment(self, amount):
        transaction_id = f"UPI-{uuid4().hex[:8].upper()}"
        return PaymentResult(
            True,
            transaction_id,
            "UPI",
            f"UPI payment of Rs. {amount:.2f} successful."
        )
