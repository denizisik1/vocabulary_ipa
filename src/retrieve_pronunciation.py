import os
import logging
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from database import store_pronunciation

input("Installation is not allowed.")


def retrieve_pronunciation(language, word):
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    backup_base_url = os.getenv("BACKUP_BASE_URL")
    base_url_element_name = os.getenv("BASE_URL_ELEMENT_NAME")
    backup_base_url_element_name = os.getenv("BACKUP_BASE_URL_ELEMENT_NAME")

    pronunciation = _retrieve_pronunciation(base_url, base_url_element_name, word)
    if not pronunciation:
        logging.info(f"Primary source failed for '{word}', trying backup source.")
        pronunciation = _retrieve_pronunciation(backup_base_url, backup_base_url_element_name, word)

    if pronunciation:
        logging.info(f"Pronunciation for '{word}': {pronunciation}")
        store_pronunciation(language, word, pronunciation)
    else:
        logging.warning(f"Pronunciation for '{word}' not found in both sources.")


def _retrieve_pronunciation(base_url, element_name, word):
    with sync_playwright() as p:
        input("Not async still, press Enter to continue...")
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{base_url}{word}")

        try:
            element = page.locator(f".{element_name}")
            pronunciation = element.inner_text().strip()
            browser.close()
            return pronunciation
        except Exception as e:
            logging.error(f"Error retrieving pronunciation for '{word}': {e}")
            browser.close()
            return None
