class HandoffGenerator:

    def create_summary(
        self,
        persona,
        issue,
        conversation_history,
        documents_used,
        attempted_steps,
        recommendation
    ):

        summary = {
            "persona": persona,
            "issue": issue,
            "conversation_history":
                conversation_history,
            "documents_used":
                documents_used,
            "attempted_steps":
                attempted_steps,
            "recommendation":
                recommendation
        }

        return summary
