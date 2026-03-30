import os
import logging
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from database import PronunciationDatabase


class RetrievePronunciation:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("BASE_URL")
        self.backup_base_url = os.getenv("BACKUP_BASE_URL")
        self.base_url_element_name = os.getenv("BASE_URL_ELEMENT_NAME")
        self.backup_base_url_element_name = os.getenv("BACKUP_BASE_URL_ELEMENT_NAME")
        self.db = PronunciationDatabase()

    def retrieve_pronunciation(self, word):
        pronunciation = self._retrieve_pronunciation(self.base_url, self.base_url_element_name, word)
        if not pronunciation:
            logging.info(f"Primary source failed for '{word}', trying backup source.")
            pronunciation = self._retrieve_pronunciation(self.backup_base_url, self.backup_base_url_element_name, word)

        if pronunciation:
            logging.info(f"Pronunciation for '{word}': {pronunciation}")
            self.db.store_pronunciation(word, pronunciation)
        else:
            logging.warning(f"Pronunciation for '{word}' not found in both sources.")

    def _retrieve_pronunciation(self, base_url, element_name, word):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"{base_url}{word}")

            try:
                element = page.locator(f".{element_name}")
                pronunciation = element.inner_text().strip()
                browser.close()
                return pronunciation
            except Exception as e:
                logging.error(f"Error scraping pronunciation for '{word}': {e}")
                browser.close()
                return None
