import streamlit as st

from src.persona_detector import PersonaDetector
from src.retriever import SupportRetriever
from src.response_generator import ResponseGenerator
from src.escalation import EscalationEngine
from src.handoff import HandoffGenerator

st.set_page_config(
    page_title="Persona Adaptive Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Persona-Adaptive Customer Support Agent")

st.markdown("""
This AI assistant:

- Detects customer personas
- Retrieves support documentation
- Generates persona-aware responses
- Escalates unresolved issues
- Creates human handoff summaries
""")

query = st.text_area(
    "Enter Customer Message",
    height=150
)

if st.button("Analyze"):

    if not query.strip():
        st.warning("Please enter a message.")
        st.stop()

    detector = PersonaDetector()
    retriever = SupportRetriever()
    generator = ResponseGenerator()
    escalation_engine = EscalationEngine()
    handoff_generator = HandoffGenerator()

    # Persona Detection

    persona_result = detector.detect(query)

    persona = persona_result["persona"]

    st.subheader("Detected Persona")

    st.success(persona)

    # Load Vector Database

    try:
        retriever.load_vector_store()
    except:
        retriever.create_vector_store()

    # Retrieve Documents

    docs = retriever.retrieve(
        query,
        k=3
    )

    st.subheader("Retrieved Sources")

    source_names = []

    if docs:

        for doc in docs:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            source_names.append(source)

            st.write(f"• {source}")

    else:

        st.write("No sources found")

    # Generate Response

    response = generator.generate(
        persona=persona,
        query=query,
        retrieved_docs=docs
    )

    st.subheader("Generated Response")

    st.info(response)

    # Escalation Check

    retrieval_score = 0.90

    if len(docs) == 0:
        retrieval_score = 0.0

    escalation_result = (
        escalation_engine.should_escalate(
            query=query,
            retrieval_score=retrieval_score,
            failed_attempts=0,
            docs_found=len(docs) > 0
        )
    )

    st.subheader("Escalation Status")

    if escalation_result["escalate"]:

        st.error("Escalation Required")

        st.write("Reasons:")

        for reason in escalation_result["reasons"]:
            st.write(f"- {reason}")

        summary = (
            handoff_generator.create_summary(
                persona=persona,
                issue=query,
                conversation_history=[
                    query
                ],
                documents_used=source_names,
                attempted_steps=[
                    "Knowledge Base Retrieval",
                    "AI Response Generation"
                ],
                recommendation=
                    "Escalate to Tier-2 Support"
            )
        )

        st.subheader(
            "Human Handoff Summary"
        )

        st.json(summary)

    else:

        st.success(
            "No Escalation Required"
        )
