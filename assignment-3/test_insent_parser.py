import json
from intent_parser import parse_intent

test_commands = [

    "apply to this job",

    "close all tabs",

    "email this summary to my boss",

    "open youtube",

    "search for Python tutorials",

    "click the Login button",

    "fill registration form with name John age 20",

    "summarize this article",

    "go to amazon",

    "buy a laptop"

]


for i, command in enumerate(test_commands, start=1):

    print("=" * 60)

    print(f"Test {i}")

    print("Command:", command)

    result = parse_intent(command)

    print(json.dumps(result, indent=4))