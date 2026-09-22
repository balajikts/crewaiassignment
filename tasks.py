from crewai import Task


# ============================================================
# TASK 1 - Direct Customer Support
# ============================================================

def create_customer_support_task(agent, customer_query):

    return Task(
        description=f"""
        Analyze the following customer query:

        CUSTOMER QUERY:
        {customer_query}

        Your responsibilities:

        1. Understand the customer's question.
        2. Identify what the customer needs.
        3. Provide a clear and helpful answer.
        4. Give practical guidance where appropriate.
        5. Do not perform a web search.
        6. Do not delegate the task.
        7. Do not invent information.

        Answer the customer professionally.
        """,

        expected_output=(
            "A clear, accurate, helpful, and professional "
            "direct answer to the customer's query."
        ),

        agent=agent
    )


# ============================================================
# TASK 2 - Web Research
# ============================================================

def create_web_research_task(
    agent,
    customer_query,
    previous_task
):

    return Task(

        description=f"""
        Research the following customer query:

        CUSTOMER QUERY:
        {customer_query}

        A previous customer support agent has already
        attempted to answer this question.

        Your responsibilities:

        1. Understand the original customer query.
        2. Review the previous agent's answer.
        3. Use the Web Search tool.
        4. Search for current and reliable information.
        5. Verify important facts.
        6. Compare your findings with the previous answer.
        7. Produce your own research-based answer.

        IMPORTANT:

        Structure your final answer using these sections:

        ANSWER:
        Provide a clear customer-friendly answer.

        SOURCES:
        List the important sources used.

        For every source include:
        - Source title
        - URL
        - Brief description of why it is relevant

        Do not invent URLs.
        Only include URLs returned by the Web Search tool.
        """,

        expected_output=(
            "A research-based customer support answer followed "
            "by a SOURCES section containing source titles, "
            "URLs, and brief descriptions."
        ),

        agent=agent,

        context=[
            previous_task
        ]
    )

# ============================================================
# TASK 3 - Save Conversation
# ============================================================

def create_file_save_task(
    agent,
    customer_query,
    agent1_task,
    agent2_task
):

    return Task(
        description=f"""
        Save the complete customer support conversation.

        CUSTOMER QUERY:
        {customer_query}

        The completed answers from Agent 1 and Agent 2 will be
        available to you through the task context.

        Your responsibilities:

        1. Read the customer query.
        2. Read Agent 1's completed answer from the context.
        3. Read Agent 2's completed answer from the context.
        4. Use the Save Customer Support Conversation tool.
        5. Save the customer query and both answers.
        6. Preserve the answers accurately.
        7. Do not invent information.
        8. Confirm that the conversation was saved successfully.
        """,

        expected_output=(
            "A confirmation that the customer query and both "
            "agent answers were successfully saved."
        ),

        agent=agent,

        context=[
            agent1_task,
            agent2_task
        ]
    )