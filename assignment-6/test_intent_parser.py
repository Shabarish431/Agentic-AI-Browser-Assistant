from intent_parser import parse_intent

def test_navigate():
    action = parse_intent("navigate to google.com")
    assert action.action_type == "navigate"

def test_fill_form():
    action = parse_intent("fill the name field with John")
    assert action.action_type == "fill_form"

def test_email():
    action = parse_intent("send an email to alice@example.com")
    assert action.action_type == "email"

def test_summarize():
    action = parse_intent("summarize this page")
    assert action.action_type == "summarize"

def test_click():
    action = parse_intent("click the submit button")
    assert action.action_type == "click"