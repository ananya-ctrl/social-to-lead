from app.graph import process_user_message
from app.state import AgentState


def create_initial_state() -> AgentState:
    return {
        "messages": [],
        "intent": "",
        "retrieved_context": "",
        "user_name": "",
        "user_email": "",
        "creator_platform": "",
        "missing_fields": [],
        "lead_ready": False,
        "lead_captured": False,
        "last_user_message": "",
        "last_agent_response": ""
    }


def main():
    print("AutoStream Agent is running. Type 'exit' to stop.\n")

    state = create_initial_state()

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() in {"exit", "quit"}:
            print("Agent: Goodbye!")
            break

        state = process_user_message(state, user_message)
        print(f"Agent: {state['last_agent_response']}\n")


if __name__ == "__main__":
    main()