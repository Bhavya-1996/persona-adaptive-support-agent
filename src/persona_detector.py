class PersonaDetector:

    def __init__(self):
        self.technical_keywords = [
            "api",
            "endpoint",
            "logs",
            "stack trace",
            "token",
            "authentication",
            "configuration",
            "database",
            "server",
            "error code"
        ]

        self.frustrated_keywords = [
            "frustrating",
            "angry",
            "nothing works",
            "terrible",
            "worst",
            "urgent",
            "issue again",
            "still not working",
            "disappointed"
        ]

        self.business_keywords = [
            "business",
            "operations",
            "revenue",
            "customers",
            "impact",
            "downtime",
            "sla",
            "executive",
            "timeline",
            "resolution"
        ]

    def detect(self, message):

        text = message.lower()

        technical_score = sum(
            keyword in text
            for keyword in self.technical_keywords
        )

        frustrated_score = sum(
            keyword in text
            for keyword in self.frustrated_keywords
        )

        business_score = sum(
            keyword in text
            for keyword in self.business_keywords
        )

        scores = {
            "Technical Expert": technical_score,
            "Frustrated User": frustrated_score,
            "Business Executive": business_score
        }

        persona = max(scores, key=scores.get)

        if scores[persona] == 0:
            persona = "Technical Expert"

        return {
            "persona": persona,
            "scores": scores
        }
