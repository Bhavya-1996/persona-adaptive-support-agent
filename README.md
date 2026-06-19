# persona-adaptive-support-agent
Persona-Adaptive Customer Support Agent
Overview

An AI-powered customer support agent that:

Detects customer personas
Retrieves information using RAG
Generates persona-aware responses
Escalates unresolved issues to human agents
Creates structured handoff summaries
Supported Personas
Technical Expert
Uses APIs, logs, configurations
Wants technical explanations
Frustrated User
Uses emotional language
Wants reassurance and quick solutions
Business Executive
Focuses on business impact
Prefers concise communication
Features
Persona Detection
RAG-based Knowledge Retrieval
Adaptive Response Generation
Human Escalation Workflow
Streamlit User Interface
Architecture

User Query
→ Persona Detection
→ RAG Retrieval
→ Response Generation
→ Escalation Check
→ Human Handoff

Tech Stack
Python 3.11
LangChain
ChromaDB
Sentence Transformers
OpenAI GPT-4o-mini
Streamlit
Escalation Rules
No relevant documents found
Low retrieval confidence
Multiple failed attempts
Billing issues
Legal issues
Account-sensitive issues
Installation

pip install -r requirements.txt

streamlit run app.py

Future Improvements
LangGraph workflow
Multi-turn memory
Dashboard analytics
Human approval workflow
