from crewai import Agent

from tools.web_search_tool import web_search


def create_web_research_agent():

    agent = Agent(

        role="Web Research Customer Support Agent",

        goal=(
            "Research the customer's query using reliable web "
            "sources and provide an accurate, current, useful "
            "research-based answer."
        ),

        backstory=(
            "You are an experienced web research and customer "
            "support specialist. You receive a customer question "
            "after another support agent has already attempted "
            "to answer it. You independently research the "
            "question using the web and verify important facts."
        ),

        tools=[
            web_search
        ],

        verbose=True,

        allow_delegation=False
    )

    return agent