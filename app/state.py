from typing import TypedDict, List


class AgentState(TypedDict):
    messages: List[str]
    intent: str
    retrieved_context: str
    user_name: str
    user_email: str
    creator_platform: str
    missing_fields: List[str]
    lead_ready: bool
    lead_captured: bool
    last_user_message: str
    last_agent_response: str