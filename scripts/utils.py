import logging
import datetime
from typing import Dict, List

def calculate_transaction_fee(amount: float, fee_percentage: float) -> float:
    # Calculate the transaction fee based on the given amount and fee percentage
    return amount * (fee_percentage / 100)

def validate_payment_details(payment_details: Dict) -> bool:
    required_fields = ["card_number", "expiration_date", "cvv"]
    for field in required_fields:
        if field not in payment_details:
            logging.error(f"Missing required field: {field}")
            return False
    return True

def generate_transaction_id() -> str:
    # Generate a unique transaction ID
    return f"TXN-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

def process_payment(payment_details: Dict) -> Dict:
    if not validate_payment_details(payment_details):
        return {"status": "failed", "message": "Invalid payment details"}
    
    transaction_id = generate_transaction_id()
    transaction_fee = calculate_transaction_fee(payment_details["amount"], 2.5)
    
    return {
        "status": "success",
        "transaction_id": transaction_id,
        "transaction_fee": transaction_fee
    }