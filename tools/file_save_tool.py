import os
from datetime import datetime

from crewai.tools import tool


@tool("Save Customer Support Conversation")
def save_customer_support_conversation(
    customer_query: str,
    agent1_answer: str,
    agent2_answer: str
) -> str:
    """
    Save the customer query and both agent answers
    into a text file.
    """

    output_directory = "output"

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    file_path = os.path.join(
        output_directory,
        "customer_support_history.txt"
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    content = f"""
============================================================
CUSTOMER SUPPORT CONVERSATION
============================================================

Timestamp:
{timestamp}

------------------------------------------------------------
CUSTOMER QUERY
------------------------------------------------------------

{customer_query}

------------------------------------------------------------
AGENT 1 - DIRECT ANSWER
------------------------------------------------------------

{agent1_answer}

------------------------------------------------------------
AGENT 2 - WEB RESEARCH ANSWER
------------------------------------------------------------

{agent2_answer}

============================================================
END OF CONVERSATION
============================================================

"""

    try:

        with open(
            file_path,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return (
            f"Conversation successfully saved to: "
            f"{file_path}"
        )

    except Exception as e:

        return (
            f"Failed to save conversation: {str(e)}"
        )