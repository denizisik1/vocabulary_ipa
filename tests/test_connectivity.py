""" This is a test file for checking connectivity to a given URL using Playwright. """
import re
import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))
    print("Title verified successfully.")

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    print("Get started link verified successfully.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        test_has_title(page)
        test_get_started_link(page)
        browser.close()
