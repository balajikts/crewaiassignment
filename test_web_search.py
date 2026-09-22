from tools.web_search_tool import create_web_search_tool


search_tool = create_web_search_tool()

result = search_tool.run(
    "What is CrewAI framework?"
)

print("\n" + "=" * 60)
print("WEB SEARCH RESULT")
print("=" * 60)
print(result)