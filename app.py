import streamlit as st

st.title("Persona Adaptive Customer Support Agent")

user_query = st.text_area("Enter Customer Query")

if st.button("Analyze"):

    persona = "Technical Expert"

    if "frustrating" in user_query.lower():
        persona = "Frustrated User"

    elif "business" in user_query.lower():
        persona = "Business Executive"

    st.subheader("Detected Persona")
    st.write(persona)

    st.subheader("Retrieved Sources")
    st.write("api_authentication.md")

    st.subheader("Generated Response")
    st.write("Sample grounded response from knowledge base.")

    st.subheader("Escalation Status")
    st.write("No")
