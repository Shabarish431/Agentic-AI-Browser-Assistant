from agent import agent
from profile_store import (
    get_name,
    get_email,
    get_resume,
)

print("Browser Agent")
print("Type 'exit' to quit.\n")

while True:

    command = input("You: ")

    if command.lower() == "exit":
        break

    if "name" in command.lower():
        print(get_name())
        continue

    if "email" in command.lower():
        print(get_email())
        continue

    if "resume" in command.lower():
        print(get_resume())
        continue

    response = agent.invoke(
        {
            "input": command
        }
    )

    print("\nAgent:")
    print(response["output"])