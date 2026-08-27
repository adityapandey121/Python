from dataclasses import dataclass


@dataclass(frozen=True)
class PaymentResult:
    success: bool
    transaction_id: str
    method: str
    message: str
