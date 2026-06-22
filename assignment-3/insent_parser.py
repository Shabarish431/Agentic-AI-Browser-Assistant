import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an Intent Parser.

Your task is to convert browser automation commands into structured JSON.

Return ONLY valid JSON.

Schema:

{
  "action": "fill_form | navigate | email | summarize | click | close_tabs | search | clarifying_question",
  "target_url": "",
  "data": {},
  "steps": [],
  "question": ""
}

Rules:

1. Only output JSON.
2. Never explain anything.
3. If the command is ambiguous, ask a clarification question.

Few-shot Example 1

User:
Open youtube

Assistant:
{
  "action":"navigate",
  "target_url":"https://youtube.com",
  "data":{},
  "steps":["Open https://youtube.com"]
}

Few-shot Example 2

User:
Fill login form with email abc@gmail.com and password 1234

Assistant:
{
  "action":"fill_form",
  "target_url":"",
  "data":{
      "email":"abc@gmail.com",
      "password":"1234"
  },
  "steps":[
      "Locate email field",
      "Enter email",
      "Locate password field",
      "Enter password",
      "Submit form"
  ]
}

Few-shot Example 3

User:
Email this summary to my boss

Assistant:
{
  "action":"email",
  "target_url":"",
  "data":{
      "recipient":"boss",
      "content":"summary"
  },
  "steps":[
      "Compose email",
      "Attach summary",
      "Send email"
  ]
}
"""


def parse_intent(user_command: str) -> dict:

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_command
            }
        ]
    )

    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":

    command = input("Enter command: ")

    result = parse_intent(command)

    print(json.dumps(result, indent=4))