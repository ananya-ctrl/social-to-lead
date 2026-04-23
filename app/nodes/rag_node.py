from app.rag.retriever import get_relevant_context


def answer_with_rag(user_message: str) -> tuple[str, str]:
    context = get_relevant_context(user_message)
    question = user_message.lower()

    if "price" in question or "pricing" in question or "plan" in question:
        answer = (
            "AutoStream offers two plans:\n"
            "- Basic Plan: $29/month, 10 videos/month, 720p resolution\n"
            "- Pro Plan: $79/month, unlimited videos, 4K resolution, AI captions"
        )
    elif "refund" in question:
        answer = "AutoStream offers no refunds after 7 days."
    elif "support" in question:
        answer = "24/7 support is available only on the Pro plan."
    elif "4k" in question or "resolution" in question:
        answer = "The Pro plan supports 4K resolution, while the Basic plan supports 720p."
    elif "captions" in question:
        answer = "AI captions are included in the Pro plan."
    else:
        answer = (
            "Here’s what I found from the AutoStream knowledge base:\n"
            f"{context}"
        )

    return answer, context