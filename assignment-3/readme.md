# Assignment 3 - Intent Parser Prototype

## Objective

Build an intent parser that converts natural language browser commands into structured JSON using an LLM.

---

## Features

- Uses OpenAI API
- Converts natural language to JSON
- Supports:
  - navigate
  - fill_form
  - email
  - summarize
  - click
  - search
  - close_tabs
- Handles ambiguous commands using clarification questions.

---

## Install

```bash
pip install -r requirements.txt
```

---

## Set API Key

Create a `.env` file.

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run

Single command

```bash
python intent_parser.py
```

Run all tests

```bash
python test_intent_parser.py
```

---

## JSON Schema

```json
{
  "action": "",
  "target_url": "",
  "data": {},
  "steps": [],
  "question": ""
}
```

---

## Test Commands

1. apply to this job
2. close all tabs
3. email this summary to my boss
4. open youtube
5. search for Python tutorials
6. click the Login button
7. fill registration form with name John age 20
8. summarize this article
9. go to amazon
10. buy a laptop