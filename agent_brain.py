import os

class SentinelAgent:
    """
    Sentinel-v1: An autonomous operations agent designed for 
    intent classification and communication routing.
    """
    def __init__(self, agent_name="Sentinel-v1"):
        self.agent_name = agent_name
        # Mapping intents to specific operational 'limbs'
        self.routes = {
            "LEAD": "Sales-Slack-Channel",
            "SUPPORT": "Ticketing-System",
            "CONTENT": "Marketing-ClickUp-Board"
        }

    def analyze_intent(self, user_input):
        """
        Logic for identifying the primary goal of an inbound message.
        In production, this module serves as the interface for LLM (Claude/OpenAI) 
        classification based on custom evals.
        """
        input_text = user_input.upper()
        
        if any(keyword in input_text for keyword in ["BUY", "PRICING", "DEMO"]):
            return "LEAD"
        elif any(keyword in input_text for keyword in ["HELP", "ERROR", "BUG", "ISSUE"]):
            return "SUPPORT"
        elif any(keyword in input_text for keyword in ["IDEA", "POST", "VIDEO", "CONTENT"]):
            return "CONTENT"
        else:
            return "GENERAL_INQUIRY"

    def execute_routing(self, message):
        """Processes the message and simulates routing to the target integration."""
        intent = self.analyze_intent(message)
        destination = self.routes.get(intent, "General-Archive")
        
        print(f"[{self.agent_name}] Status: Processing Inbound Message...")
        print(f"[{self.agent_name}] Analysis: Detected Intent -> {intent}")
        print(f"[{self.agent_name}] Action: Routing data to {destination}...")
        return intent

# --- Unit Test ---
if __name__ == "__main__":
    agent = SentinelAgent()
    sample_interaction = "We are interested in a demo and want to know about pricing."
    agent.execute_routing(sample_interaction)
