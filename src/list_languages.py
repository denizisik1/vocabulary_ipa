import logging
from database import PronunciationDatabase


class ListLanguages:
    def __init__(self):
        self.db = PronunciationDatabase()

    def list_languages(self):
        languages = self.db.list_available_languages()
        if not languages:
            print("No languages found in the database.")
            return

        for lang in languages:
            print(f"{lang}")
        return languages
