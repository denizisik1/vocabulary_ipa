"""
Collins may be using /ipa/ and not [ipa]
Read selenium-stealth's source code.
Reverse backup and base.
Git main, development, testing branches.
Open wiki page for Help:IPA/Standard German

https://docs.google.com/spreadsheets/d/1r9HwvVpo35MFxnJ_5W6RKlDfx5VzmQVcnpJTgrNUY9I/edit?gid=0#gid=0

"""
import csv
import os
import random
import time

import undetected_chromedriver as uc

from os import listdir
from os.path import isfile, join

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfigLoader:
    def __init__(self):
        load_dotenv()
        self.ENV = os.getenv("ENV", "development")
        self.PATH = os.path.expandvars(os.path.expanduser(os.getenv("CSV_PATH")))
        self.BASE_URL = os.getenv("BASE_URL")
        self.BASE_URL_ELEMENT_NAME = os.getenv("BASE_URL_ELEMENT_NAME")
        self.BACKUP_BASE_URL = os.getenv("BACKUP_BASE_URL")
        self.BACKUP_BASE_URL_ELEMENT_NAME = os.getenv("BACKUP_BASE_URL_ELEMENT_NAME")

        self.user_agents = [
            os.getenv("USER_AGENT_1"),
            os.getenv("USER_AGENT_2"),
            os.getenv("USER_AGENT_3")
        ]


class CSVReader:
    def __init__(self, PATH):
        self.PATH = PATH

    def get_files(self):
        return [f for f in listdir(self.PATH) if isfile(join(self.PATH, f))]

    def read_file(self, file):
        with open(os.path.join(self.PATH, file)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if not row or len(row) < 2:
                    continue
                parts = row[0].split(" ", 1)
                article = parts[0]
                word = parts[1] if len(parts) > 1 else ""
                meaning = row[1]
                yield article, word, meaning


class Scraper:
    def __init__(self, config):
        options = uc.ChromeOptions()
        if config.ENV == "production":
            options.add_argument("--headless=new")
        random_user_agent = random.choice(config.user_agents)
        options.add_argument(f"--user-agent={random_user_agent}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = uc.Chrome(options=options, headless=config.ENV == "production")
        self.BASE_URL = config.BASE_URL
        self.BACKUP_BASE_URL = config.BACKUP_BASE_URL
        self.BASE_URL_ELEMENT_NAME = config.BASE_URL_ELEMENT_NAME
        self.BACKUP_BASE_URL_ELEMENT_NAME = config.BACKUP_BASE_URL_ELEMENT_NAME

    def get_pronunciation(self, word):
        url = self.BASE_URL + word.lower()
        backup_url = self.BACKUP_BASE_URL + word.lower()
        try:
            self.driver.get(url)
            time.sleep(1)
            ipa = self.driver.find_element(By.CLASS_NAME, BASE_URL_ELEMENT_NAME).text # TODO: Decide.
            # ipa = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.BASE_URL_ELEMENT_NAME))).text
            return ipa, url
        except (NoSuchElementException, TimeoutException):
            try:
                self.driver.get(backup_url)
                ipa = self.driver.find_element(By.CLASS_NAME, BACKUP_BASE_URL_ELEMENT_NAME).text # TODO: Decide.
                # ipa = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.BACKUP_BASE_URL_ELEMENT_NAME))).text
                return ipa, backup_url
            except (NoSuchElementException, TimeoutException):
                return None, None

    def close(self):
        self.driver.quit()


class App:
    def __init__(self):
        self.config = ConfigLoader()
        print(f"Running in {self.config.ENV} mode.")
        self.csv_reader = CSVReader(self.config.PATH)
        self.scraper = Scraper(self.config)

    def run(self):
        files = self.csv_reader.get_files()
        for file in files:
            for article, word, meaning in self.csv_reader.read_file(file):
                print(article)
                print(word)
                print(meaning)

                ipa, source_url = self.scraper.get_pronunciation(word)
                if ipa:
                    print(ipa)
                    print(source_url)
                print()
        self.scraper.close()


if __name__ == "__main__":
    app = App()
    app.run()
