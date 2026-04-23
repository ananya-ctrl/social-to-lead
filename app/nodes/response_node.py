def build_missing_details_response(missing_fields: list[str]) -> str:
    if missing_fields == ["name", "email", "creator_platform"]:
        return "Great, I can help with that. Please share your name, email, and creator platform."

    if missing_fields == ["name", "email"]:
        return "Great choice. Please share your name and email."

    if missing_fields == ["name", "creator_platform"]:
        return "Please share your name and creator platform."

    if missing_fields == ["email", "creator_platform"]:
        return "Please share your email and creator platform."

    if missing_fields == ["name"]:
        return "Please share your name."

    if missing_fields == ["email"]:
        return "Please share your email address."

    if missing_fields == ["creator_platform"]:
        return "Please share your creator platform, like YouTube or Instagram."

    return "Thanks. I have all the details I need."


def build_success_response(name: str, platform: str) -> str:
    return f"Thanks, {name}. Your interest has been recorded for AutoStream on {platform}."


def build_greeting_response() -> str:
    return "Hi! I can help with AutoStream pricing, features, plans, and signup."


def build_fallback_response() -> str:
    return "I can help with AutoStream plans, pricing, features, refunds, support, and signup."