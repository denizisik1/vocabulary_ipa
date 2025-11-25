# pylint: disable=too-few-public-methods


import logging
from database import PronunciationDatabase


class DataAnalyzer:
    def __init__(self, language):
        self.language = language
        self.db = PronunciationDatabase()

    def analyze_data(self):
        if not self.db.check_for_language(self.language):
            raise ValueError(f"Language '{self.language}' not found in the database.")
        count = self.db.analyze_data(self.language)
        logging.info("Number of rows without pronunciation %s: %d", self.language, count)
        return self.db.analyze_data(self.language)
