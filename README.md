\# 🤖 AI Customer Support System



A three-agent sequential customer support system built using \*\*CrewAI, Python, OpenAI, Serper API, and Streamlit\*\*.



The system processes a customer query through three specialized AI agents:



```text

Customer Query

&#x20;     │

&#x20;     ▼

┌──────────────────────────┐

│ Agent 1                  │

│ Customer Support Agent   │

│ Direct Answer            │

└────────────┬─────────────┘

&#x20;            │

&#x20;            ▼

┌──────────────────────────┐

│ Agent 2                  │

│ Web Research Agent       │

│ Search \& Verify          │

└────────────┬─────────────┘

&#x20;            │

&#x20;            ▼

┌──────────────────────────┐

│ Agent 3                  │

│ Documentation Agent      │

│ Save Conversation        │

└────────────┬─────────────┘

&#x20;            │

&#x20;            ▼

customer\_support\_history.txt

