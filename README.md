# Social-to-Lead Agentic Workflow

A lightweight conversational AI workflow built for the ServiceHive Machine Learning Intern assignment.

This project simulates a sales-focused conversational agent for **AutoStream**, a fictional SaaS platform for automated video editing tools for content creators. The agent can answer product questions from a local knowledge base, detect high-intent users, collect lead details, and trigger a mock lead capture action.

---

## Features

- Intent detection for:
  - Casual greeting
  - Product or pricing inquiry
  - High-intent lead
- Local knowledge-base answering
- Multi-turn memory across the conversation
- Controlled lead capture workflow
- Mock tool execution only after collecting:
  - Name
  - Email
  - Creator Platform

---

## Project Structure

```text
social-to-lead-agent/
│
├── app/
│   ├── main.py
│   ├── graph.py
│   ├── state.py
│   ├── prompts.py
│   ├── config.py
│   ├── nodes/
│   │   ├── intent_node.py
│   │   ├── rag_node.py
│   │   ├── qualification_node.py
│   │   ├── tool_node.py
│   │   └── response_node.py
│   ├── tools/
│   │   └── lead_capture.py
│   ├── rag/
│   │   ├── kb_loader.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   └── utils/
│       └── validators.py
│
├── data/
│   └── autostream_kb.md
├── demo/
│   └── sample_conversations.txt
├── requirements.txt
├── README.md
└── .env
```

## How to Run Locally
1. Clone the repository
git clone <your-repo-link>
cd social-to-lead-agent

2. Create a virtual environment
python -m venv .venv

3. Activate the virtual environment
PowerShell
.venv\Scripts\Activate.ps1
CMD
.venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run the chatbot
python -m app.main

## Architecture Explanation

I designed this project as a lightweight multi-turn conversational workflow for lead qualification. The system maintains conversation state using a shared state dictionary that stores the detected intent, retrieved context, user details, missing fields, and lead capture status. This allows the chatbot to remember earlier turns and continue a lead-collection flow without losing context.

The workflow is organized into modular nodes: intent detection, knowledge retrieval, lead qualification, tool execution, and response building. Product and pricing questions are answered using a local knowledge base stored in Markdown, which keeps responses grounded in predefined business information. High-intent messages trigger a lead qualification flow where the system collects name, email, and creator platform. The mock lead capture tool is executed only after all required fields are available, preventing premature tool calls.

This design keeps the system simple, explainable, and reliable for a small assignment setting while still reflecting the core structure of a real-world conversational sales agent.

## WhatsApp Webhook Integration

To integrate this workflow with WhatsApp, I would expose the chatbot through a backend API using Flask or FastAPI. Incoming WhatsApp messages would be received through a webhook connected to the WhatsApp Business Cloud API. Each inbound message would be mapped to a user session, and the session state would be stored in memory or a database.

When a message arrives, the backend would pass the text and current session state into the chatbot workflow. The generated response would then be sent back to the user through the WhatsApp API. If the user becomes a qualified lead, the captured details could be stored in a CRM, Google Sheet, or lead management database. This setup would allow the same conversational logic to work across channels while preserving stateful lead qualification.