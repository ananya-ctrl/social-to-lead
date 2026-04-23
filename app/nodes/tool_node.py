from app.tools.lead_capture import mock_lead_capture


def execute_lead_capture(name: str, email: str, platform: str, lead_captured: bool):
    if lead_captured:
        return {
            "status": "skipped",
            "message": "Lead already captured."
        }

    if not name or not email or not platform:
        return {
            "status": "blocked",
            "message": "Missing required fields. Lead capture not triggered."
        }

    return mock_lead_capture(name, email, platform)