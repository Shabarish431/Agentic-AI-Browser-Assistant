from playwright.sync_api import sync_playwright
from langchain.tools import tool

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)

page = browser.new_page()


@tool
def navigate_to(url: str):
    """Navigate browser to a URL."""
    page.goto(url)
    return f"Opened {url}"


@tool
def click_element(selector: str):
    """Click an element using CSS selector."""
    page.click(selector)
    return f"Clicked {selector}"


@tool
def type_text(input: str):
    """
    Input format:
    selector|text
    """

    selector, text = input.split("|", 1)

    page.fill(selector, text)

    return f"Typed '{text}' into {selector}"