import os
import requests

from dotenv import load_dotenv
from crewai.tools import tool


load_dotenv()


@tool("Web Search")
def web_search(query: str) -> str:
    """
    Search the internet using the Serper API.
    Returns relevant search results with titles,
    URLs, and summaries.
    """

    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        return (
            "Web search failed: "
            "SERPER_API_KEY is not configured."
        )

    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "q": query
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        results = []

        for index, item in enumerate(
            data.get("organic", [])[:5],
            start=1
        ):

            title = item.get(
                "title",
                "Untitled"
            )

            link = item.get(
                "link",
                ""
            )

            snippet = item.get(
                "snippet",
                ""
            )

            results.append(
                f"""
SOURCE {index}

Title:
{title}

URL:
{link}

Summary:
{snippet}
"""
            )

        if not results:

            return (
                "No relevant web search results "
                "were found."
            )

        return "\n".join(results)

    except requests.exceptions.RequestException as e:

        return (
            f"Web search request failed: {str(e)}"
        )

    except Exception as e:

        return (
            f"Unexpected web search error: {str(e)}"
        )