import asyncio
import json

from playwright.async_api import async_playwright, TimeoutError


async def navigator():

    try:
        async with async_playwright() as p:

            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()

            try:
                await page.goto("https://news.ycombinator.com", timeout=10000)
            except TimeoutError:
                print("Website loading timed out.")
                return

            try:
                await page.wait_for_selector(".titleline", timeout=5000)
            except TimeoutError:
                print("Article titles not found.")
                return

            titles = await page.locator(".titleline").all_inner_texts()

            top5 = titles[:5]

            with open("assignment-2/articles.json", "w") as f:
                json.dump({"articles": top5}, f, indent=4)

            print("Top 5 Articles")

            for i, title in enumerate(top5, start=1):
                print(f"{i}. {title}")

            await browser.close()

    except Exception as e:
        print("Unexpected Error:", e)


asyncio.run(navigator())