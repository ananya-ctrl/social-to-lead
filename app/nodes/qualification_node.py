import re

from app.utils.validators import is_valid_email, is_non_empty


def extract_email_with_regex(user_message: str) -> str:
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", user_message)
    return match.group(0) if match else ""


def extract_name_with_regex(user_message: str) -> str:
    patterns = [
        r"my name is\s+([A-Za-z][A-Za-z\s]{1,49})",
        r"i am\s+([A-Za-z][A-Za-z\s]{1,49})",
        r"i'm\s+([A-Za-z][A-Za-z\s]{1,49})",
    ]

    for pattern in patterns:
        match = re.search(pattern, user_message, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return ""


def extract_platform_with_regex(user_message: str) -> str:
    platforms = ["YouTube", "Instagram", "TikTok", "Facebook", "LinkedIn", "Twitch"]
    lower_msg = user_message.lower()

    for platform in platforms:
        if platform.lower() in lower_msg:
            return platform

    return ""


def extract_lead_details(user_message: str) -> dict:
    name = extract_name_with_regex(user_message)
    email = extract_email_with_regex(user_message)
    creator_platform = extract_platform_with_regex(user_message)

    if email and not is_valid_email(email):
        email = ""

    if not is_non_empty(name):
        name = ""

    if not is_non_empty(creator_platform):
        creator_platform = ""

    return {
        "name": name,
        "email": email,
        "creator_platform": creator_platform
    }


def find_missing_fields(name: str, email: str, creator_platform: str) -> list[str]:
    missing = []

    if not name:
        missing.append("name")

    if not email:
        missing.append("email")

    if not creator_platform:
        missing.append("creator_platform")

    return missing