class ResponseGenerator:

    def generate(
        self,
        persona,
        query,
        retrieved_docs
    ):

        if not retrieved_docs:
            return (
                "I could not find sufficient "
                "information in the knowledge base."
            )

        context = "\n".join([
            doc.page_content
            for doc in retrieved_docs
        ])

        if persona == "Technical Expert":
            return self._technical_response(
                query,
                context
            )

        elif persona == "Frustrated User":
            return self._frustrated_response(
                query,
                context
            )

        elif persona == "Business Executive":
            return self._business_response(
                query,
                context
            )

        return context

    def _technical_response(
        self,
        query,
        context
    ):

        return f"""
Detected Persona: Technical Expert

Issue Analysis:
Based on the retrieved documentation.

Relevant Information:
{context}

Recommended Troubleshooting:

1. Review configuration settings.
2. Verify authentication details.
3. Check application logs.
4. Retry affected operation.
5. Validate system connectivity.

Root Cause:
Refer to retrieved documentation above.
"""

    def _frustrated_response(
        self,
        query,
        context
    ):

        return f"""
Detected Persona: Frustrated User

I understand how frustrating this situation can be.

Based on the support documentation:

{context}

Recommended Steps:

1. Follow the documented resolution steps.
2. Verify account and login details.
3. Retry the operation.

If the issue continues, we can escalate
this to a support specialist.
"""

    def _business_response(
        self,
        query,
        context
    ):

        return f"""
Detected Persona: Business Executive

Business Impact:
The issue may affect normal operations.

Recommended Action:
Review the following documented guidance:

{context}

Estimated Resolution:
Please follow the documented procedure.
If the issue persists, escalation may
be required.

Next Step:
Apply the recommended resolution process.
"""
