import re


def is_valid_email(email: str) -> bool:
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(pattern, email))


def is_non_empty(value: str) -> bool:
    return bool(value and value.strip())