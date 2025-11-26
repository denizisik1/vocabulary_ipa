import logging
from database import PronunciationDatabase


class ListLanguages:
    def __init__(self):
        self.db = PronunciationDatabase()

    def list_languages(self):
        languages = self.db.list_available_languages() or []

        if not languages:
            logging.info("No languages found in the database.")
            return []

        print("\nAvailable languages in the database:")
        for lang in languages:
            print(lang)

        return languages
