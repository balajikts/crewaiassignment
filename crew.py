from crewai import Crew, Process
from typing import Callable, Optional

from agents.customer_support_agent import (
    create_customer_support_agent
)

from agents.web_research_agent import (
    create_web_research_agent
)

from agents.file_save_agent import (
    create_file_save_agent
)

from tasks import (
    create_customer_support_task,
    create_web_research_task,
    create_file_save_task
)


def run_customer_support_crew(
    customer_query,
    progress_callback: Optional[Callable] = None
):

    # ========================================================
    # Helper function for UI progress
    # ========================================================

    def notify(stage, status, message):

        print(message)

        if progress_callback:
            progress_callback(
                stage,
                status,
                message
            )


    # ========================================================
    # CREATE AGENTS
    # ========================================================

    notify(
        "agent1",
        "running",
        "Creating Agent 1..."
    )

    agent1 = create_customer_support_agent()

    notify(
        "agent1",
        "created",
        "Agent 1 created successfully."
    )


    notify(
        "agent2",
        "running",
        "Creating Agent 2..."
    )

    agent2 = create_web_research_agent()

    notify(
        "agent2",
        "created",
        "Agent 2 created successfully."
    )


    notify(
        "agent3",
        "running",
        "Creating Agent 3..."
    )

    agent3 = create_file_save_agent()

    notify(
        "agent3",
        "created",
        "Agent 3 created successfully."
    )


    # ========================================================
    # CREATE TASKS
    # ========================================================

    notify(
        "tasks",
        "running",
        "Creating sequential tasks..."
    )

    task1 = create_customer_support_task(
        agent1,
        customer_query
    )

    task2 = create_web_research_task(
        agent2,
        customer_query,
        task1
    )

    task3 = create_file_save_task(
        agent3,
        customer_query,
        task1,
        task2
    )

    notify(
        "tasks",
        "created",
        "All three tasks created successfully."
    )


    # ========================================================
    # CREATE CREW
    # ========================================================

    notify(
        "crew",
        "running",
        "Creating sequential Crew..."
    )

    crew = Crew(

        agents=[
            agent1,
            agent2,
            agent3
        ],

        tasks=[
            task1,
            task2,
            task3
        ],

        process=Process.sequential,

        verbose=True
    )


    # ========================================================
    # EXECUTE
    # ========================================================

    notify(
        "agent1",
        "running",
        "Agent 1 is processing the customer query..."
    )

    result = crew.kickoff()


    # ========================================================
    # EXECUTION COMPLETE
    # ========================================================

    notify(
        "complete",
        "completed",
        "All three agents completed successfully."
    )


    # ========================================================
    # RETURN RESULTS
    # ========================================================

    return {

        "agent1_answer": task1.output.raw,

        "agent2_answer": task2.output.raw,

        "agent3_answer": task3.output.raw,

        "final_result": result
    }