from models import AgentAction

def parse_intent(text: str) -> AgentAction:
    t = text.lower().strip()

    if t.startswith("go to ") or "open " in t or "navigate to" in t:
        return AgentAction(action_type="navigate", target=text)

    if "fill" in t or "enter" in t or "type" in t:
        return AgentAction(action_type="fill_form", target=text)

    if "email" in t or "send mail" in t or "send an email" in t:
        return AgentAction(action_type="email", target=text)

    if "summarize" in t or "summary" in t:
        return AgentAction(action_type="summarize", target=text)

    if "click" in t or "press" in t or "select" in t:
        return AgentAction(action_type="click", target=text)

    return AgentAction(action_type="summarize", target=text)