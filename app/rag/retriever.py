from app.rag.kb_loader import load_knowledge_base


def get_relevant_context(user_query: str, kb_path: str = "data/autostream_kb.md") -> str:
    raw_text = load_knowledge_base(kb_path)
    query = user_query.lower()

    sections = {
        "basic_plan": (
            "Basic Plan\n"
            "- Price: $29/month\n"
            "- Videos: 10 videos/month\n"
            "- Resolution: 720p"
        ),
        "pro_plan": (
            "Pro Plan\n"
            "- Price: $79/month\n"
            "- Videos: Unlimited videos\n"
            "- Resolution: 4K\n"
            "- Features: AI captions"
        ),
        "policies": (
            "Company Policies\n"
            "- No refunds after 7 days\n"
            "- 24/7 support available only on Pro plan"
        ),
    }

    matched_parts = []

    if any(word in query for word in ["basic", "29", "720p"]):
        matched_parts.append(sections["basic_plan"])

    if any(word in query for word in ["pro", "79", "4k", "captions", "unlimited"]):
        matched_parts.append(sections["pro_plan"])

    if any(word in query for word in ["refund", "refunds", "support", "policy", "policies"]):
        matched_parts.append(sections["policies"])

    if matched_parts:
        return "\n\n".join(matched_parts)

    return raw_text