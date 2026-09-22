from crewai import Agent


def create_customer_support_agent():
    agent = Agent(
        role="Customer Support Agent",
        goal=(
            "Understand the customer's query and provide a clear, "
            "accurate, helpful, and professional answer."
        ),
        backstory=(
            "You are an experienced customer support specialist. "
            "You understand customer questions, identify the main issue, "
            "and provide concise and useful responses. "
            "If you do not know something, clearly say so instead of "
            "inventing information."
        ),
        verbose=True,
        allow_delegation=False
    )

    return agent