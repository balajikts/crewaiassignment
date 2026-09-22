from crewai import Crew, Process

from agents.customer_support_agent import create_customer_support_agent
from tasks import create_customer_support_task


# ----------------------------------------
# 1. Create Agent 1
# ----------------------------------------

agent1 = create_customer_support_agent()


# ----------------------------------------
# 2. Create the Task
# ----------------------------------------

customer_query = (
    "My account password is not working. "
    "What should I do?"
)

task1 = create_customer_support_task(
    agent1,
    customer_query
)


# ----------------------------------------
# 3. Create Crew
# ----------------------------------------

crew = Crew(
    agents=[agent1],
    tasks=[task1],
    process=Process.sequential,
    verbose=True
)


# ----------------------------------------
# 4. Execute
# ----------------------------------------

result = crew.kickoff()


# ----------------------------------------
# 5. Display result
# ----------------------------------------

print("\n" + "=" * 60)
print("AGENT 1 FINAL ANSWER")
print("=" * 60)
print(result)