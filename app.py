import streamlit as st

st.set_page_config(
    page_title="Persona Adaptive Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Persona-Adaptive Customer Support Agent")

st.markdown("""
This AI support assistant:
- Detects customer persona
- Retrieves support information
- Generates persona-aware responses
- Escalates unresolved issues
""")

user_query = st.text_area(
    "Enter Customer Query",
    placeholder="Describe your issue here..."
)

if st.button("Analyze Query"):

    persona = "Technical Expert"

    query = user_query.lower()

    if any(word in query for word in [
        "frustrating",
        "angry",
        "nothing works",
        "terrible",
        "urgent"
    ]):
        persona = "Frustrated User"

    elif any(word in query for word in [
        "business",
        "revenue",
        "operations",
        "customers",
        "impact"
    ]):
        persona = "Business Executive"

    st.subheader("Detected Persona")
    st.success(persona)

    st.subheader("Retrieved Sources")

    retrieved_sources = [
        "api_authentication.md",
        "login_troubleshooting.md"
    ]

    for source in retrieved_sources:
        st.write(f"• {source}")

    st.subheader("Generated Response")

    if persona == "Technical Expert":
        st.info("""
Root Cause Analysis:

The issue may be related to authentication
token expiration or configuration mismatch.

Troubleshooting Steps:

1. Verify API token validity
2. Check request headers
3. Review application logs
4. Retry authentication
        """)

    elif persona == "Frustrated User":
        st.info("""
I understand how frustrating this can be.

Let's try the following:

1. Log out
2. Clear browser cache
3. Log in again

If the issue continues,
we can escalate it to support.
        """)

    else:
        st.info("""
Business Impact:

The issue may affect normal operations.

Recommended Action:

Review system access and restore service.

Estimated Resolution Time:

15-30 minutes.
        """)

    st.subheader("Escalation Status")

    escalation = False

    escalation_keywords = [
        "refund",
        "legal",
        "lawsuit",
        "hacked",
        "unauthorized"
    ]

    if any(word in query for word in escalation_keywords):
        escalation = True

    if escalation:
        st.error("Escalated to Human Support")
    else:
        st.success("No Escalation Required")

    st.subheader("Human Handoff Summary")

    if escalation:
        summary = {
            "persona": persona,
            "issue": user_query,
            "documents_used": retrieved_sources,
            "recommended_action":
                "Review case by Tier-2 Support"
        }

        st.json(summary)
