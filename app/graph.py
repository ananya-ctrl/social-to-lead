from app.state import AgentState
from app.nodes.intent_node import detect_intent
from app.nodes.rag_node import answer_with_rag
from app.nodes.qualification_node import extract_lead_details, find_missing_fields
from app.nodes.tool_node import execute_lead_capture
from app.nodes.response_node import (
    build_missing_details_response,
    build_success_response,
    build_greeting_response,
    build_fallback_response,
)


def process_user_message(state: AgentState, user_message: str) -> AgentState:
    state["last_user_message"] = user_message
    state["messages"].append(f"User: {user_message}")

    if state["missing_fields"] and not state["lead_captured"]:
        extracted = extract_lead_details(user_message)

        if extracted["name"]:
            state["user_name"] = extracted["name"]

        if extracted["email"]:
            state["user_email"] = extracted["email"]

        if extracted["creator_platform"]:
            state["creator_platform"] = extracted["creator_platform"]

        missing_fields = find_missing_fields(
            state["user_name"],
            state["user_email"],
            state["creator_platform"]
        )
        state["missing_fields"] = missing_fields
        state["intent"] = "high_intent_lead"

        if missing_fields:
            response = build_missing_details_response(missing_fields)
            state["last_agent_response"] = response
            state["messages"].append(f"Agent: {response}")
            return state

        tool_result = execute_lead_capture(
            state["user_name"],
            state["user_email"],
            state["creator_platform"],
            state["lead_captured"]
        )

        if tool_result["status"] == "success":
            state["lead_captured"] = True
            state["lead_ready"] = True
            response = build_success_response(
                state["user_name"],
                state["creator_platform"]
            )
        else:
            response = tool_result["message"]

        state["last_agent_response"] = response
        state["messages"].append(f"Agent: {response}")
        return state

    intent = detect_intent(user_message)
    state["intent"] = intent

    if intent == "greeting":
        response = build_greeting_response()
        state["last_agent_response"] = response
        state["messages"].append(f"Agent: {response}")
        return state

    if intent == "product_inquiry":
        answer, context = answer_with_rag(user_message)
        state["retrieved_context"] = context
        state["last_agent_response"] = answer
        state["messages"].append(f"Agent: {answer}")
        return state

    if intent == "high_intent_lead":
        extracted = extract_lead_details(user_message)

        if extracted["name"]:
            state["user_name"] = extracted["name"]

        if extracted["email"]:
            state["user_email"] = extracted["email"]

        if extracted["creator_platform"]:
            state["creator_platform"] = extracted["creator_platform"]

        missing_fields = find_missing_fields(
            state["user_name"],
            state["user_email"],
            state["creator_platform"]
        )
        state["missing_fields"] = missing_fields

        if missing_fields:
            response = build_missing_details_response(missing_fields)
            state["last_agent_response"] = response
            state["messages"].append(f"Agent: {response}")
            return state

        tool_result = execute_lead_capture(
            state["user_name"],
            state["user_email"],
            state["creator_platform"],
            state["lead_captured"]
        )

        if tool_result["status"] == "success":
            state["lead_captured"] = True
            state["lead_ready"] = True
            response = build_success_response(
                state["user_name"],
                state["creator_platform"]
            )
        else:
            response = tool_result["message"]

        state["last_agent_response"] = response
        state["messages"].append(f"Agent: {response}")
        return state

    response = build_fallback_response()
    state["last_agent_response"] = response
    state["messages"].append(f"Agent: {response}")
    return state