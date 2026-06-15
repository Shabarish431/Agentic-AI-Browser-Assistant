import asyncio

from playwright.async_api import async_playwright


async def open_tab(context, url):

    page = await context.new_page()

    try:
        await page.goto(url, timeout=10000)
        title = await page.title()
        return page, title

    except Exception:
        print(f"Failed to open {url}")
        return page, "Unknown"


async def tab_manager():

    urls = [
        "https://google.com",
        "https://github.com",
        "https://news.ycombinator.com",
        "https://bbc.com",
        "https://wikipedia.org",
    ]

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context()

        tasks = [open_tab(context, url) for url in urls]

        results = await asyncio.gather(*tasks)

        print("\nTitles\n")

        for i, (_, title) in enumerate(results, start=1):
            print(f"{i}. {title}")

        for page, _ in results[1:]:
            await page.close()

        print("\nOnly first tab remains open.")

        await asyncio.sleep(5)

        await browser.close()


asyncio.run(tab_manager())
