import asyncio
import json

from playwright.async_api import async_playwright, TimeoutError


async def form_filler():

    try:

        with open("assignment-2/form_data.json") as f:
            data = json.load(f)

    except FileNotFoundError:
        print("JSON file not found.")
        return

    except json.JSONDecodeError:
        print("Invalid JSON.")
        return

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        try:
            await page.goto(
                "https://demoqa.com/automation-practice-form",
                timeout=10000,
            )
        except TimeoutError:
            print("Website timeout.")
            return

        try:

            await page.locator("#firstName").fill(data["first_name"])
            await page.locator("#lastName").fill(data["last_name"])
            await page.locator("#userEmail").fill(data["email"])

            await page.get_by_text(data["gender"], exact=True).click()

            await page.locator("#userNumber").fill(data["mobile"])

            await page.locator("#dateOfBirthInput").click()

            await page.locator(".react-datepicker__month-select").select_option(
                label=data["dob_month"]
            )

            await page.locator(".react-datepicker__year-select").select_option(
                label=data["dob_year"]
            )

            await page.locator(
                f".react-datepicker__day--0{int(data['dob_day']):02d}"
            ).first.click()

            for subject in data["subjects"]:
                await page.locator("#subjectsInput").fill(subject)
                await page.keyboard.press("Enter")

            for hobby in data["hobbies"]:
                await page.get_by_text(hobby).click()

            await page.locator("#currentAddress").fill(data["address"])

            await page.screenshot(path="before_submit.png")

            print("Screenshot saved.")

        except Exception as e:
            print("Element not found:", e)

        finally:
            await browser.close()


asyncio.run(form_filler())
