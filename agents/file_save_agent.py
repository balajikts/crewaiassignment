from crewai import Agent

from tools.file_save_tool import (
    save_customer_support_conversation
)


def create_file_save_agent():

    agent = Agent(
        role="Customer Support Documentation Agent",

        goal=(
            "Save the customer support conversation accurately "
            "and ensure the customer's query and both agent answers "
            "are preserved in a text file."
        ),

        backstory=(
            "You are a customer support documentation specialist. "
            "You receive the customer query and the responses produced "
            "by the previous support agents. Your responsibility is "
            "to preserve the complete conversation accurately."
        ),

        tools=[
            save_customer_support_conversation
        ],

        verbose=True,

        allow_delegation=False
    )

    return agent