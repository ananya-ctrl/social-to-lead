def detect_intent(user_message: str) -> str:
    message = user_message.lower().strip()

    greeting_words = ["hi", "hello", "hey", "hii", "good morning", "good evening"]
    acknowledgement_words = ["ok", "okay", "thanks", "thank you", "cool", "great", "nice"]
    inquiry_words = [
        "price", "pricing", "plan", "plans", "feature", "features",
        "refund", "refunds", "support", "policy", "policies",
        "resolution", "captions", "videos", "basic", "pro"
    ]
    high_intent_words = [
        "i want", "sign up", "signup", "get started", "start",
        "try", "interested", "buy", "purchase", "register",
        "use this", "use autostream", "pro plan"
    ]

    if any(word == message or word in message for word in greeting_words):
        return "greeting"

    if any(word == message or word in message for word in acknowledgement_words):
        return "greeting"

    if any(word in message for word in high_intent_words):
        return "high_intent_lead"

    if any(word in message for word in inquiry_words):
        return "product_inquiry"

    return "greeting"