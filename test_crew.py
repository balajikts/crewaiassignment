print("TEST STARTED")


from crew import run_customer_support_crew


print("CREW IMPORTED")


customer_query = input(
    "\nEnter your customer query: "
)


print(
    "\nQuery received:",
    customer_query
)


result = run_customer_support_crew(
    customer_query
)


print("\n")
print("=" * 70)
print("AGENT 1 - DIRECT ANSWER")
print("=" * 70)

print(
    result["agent1_answer"]
)


print("\n")
print("=" * 70)
print("AGENT 2 - WEB RESEARCH ANSWER")
print("=" * 70)

print(
    result["agent2_answer"]
)


print("\n")
print("=" * 70)
print("AGENT 3 - FILE SAVE RESULT")
print("=" * 70)

print(
    result["agent3_answer"]
)


print("\n")
print("=" * 70)
print("COMPLETE WORKFLOW FINISHED")
print("=" * 70)