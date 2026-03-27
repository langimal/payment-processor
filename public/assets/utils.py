# utils.py
from typing import Dict, List

def validate_credit_card_number(card_number: str) -> bool:
    """Validates a credit card number using the Luhn algorithm"""
    def digits_of(n: int) -> List[int]:
        return [int(d) for d in str(n)]

    def check_sum(digits: List[int]) -> int:
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        for d in even_digits:
            checksum += sum(digits_of(d))
        for d in odd_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    return check_sum(digits_of(card_number)) == 0

def validate_email(email: str) -> bool:
    """Validates an email address using a simple regular expression"""
    import re
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

class Address:
    """Represents a physical address"""
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def to_dict(self) -> Dict:
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country
        }