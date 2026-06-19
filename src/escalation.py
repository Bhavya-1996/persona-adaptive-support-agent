class EscalationEngine:

    def __init__(self):

        self.min_similarity_score = 0.55

        self.billing_keywords = [
            "refund",
            "invoice",
            "chargeback",
            "billing dispute",
            "payment failure"
        ]

        self.legal_keywords = [
            "legal",
            "lawsuit",
            "court",
            "compliance",
            "regulation"
        ]

        self.account_keywords = [
            "account hacked",
            "unauthorized access",
            "security breach",
            "account locked"
        ]

    def should_escalate(
        self,
        query,
        retrieval_score,
        failed_attempts=0,
        docs_found=True
    ):

        query = query.lower()

        reasons = []

        if not docs_found:
            reasons.append(
                "No relevant documentation found"
            )

        if retrieval_score < self.min_similarity_score:
            reasons.append(
                "Low retrieval confidence"
            )

        if failed_attempts >= 2:
            reasons.append(
                "Multiple unsuccessful interactions"
            )

        if any(
            word in query
            for word in self.billing_keywords
        ):
            reasons.append(
                "Billing related issue"
            )

        if any(
            word in query
            for word in self.legal_keywords
        ):
            reasons.append(
                "Legal issue"
            )

        if any(
            word in query
            for word in self.account_keywords
        ):
            reasons.append(
                "Account sensitive issue"
            )

        return {
            "escalate": len(reasons) > 0,
            "reasons": reasons
        }
