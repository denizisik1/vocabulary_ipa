"""Module to list all available languages in the pronunciation database."""

import logging
from database import PronunciationDatabase


class ListLanguages:
    """Class to list all available languages in the pronunciation database."""

    def __init__(self):
        self.db = PronunciationDatabase()

    def list_languages(self):
        """List all available language tables in the database."""
        languages = self.db.list_available_languages()
        if not languages:
            print("No languages found in the database.")
            return

        for lang in languages:
            print(f"{lang}")
        return languages
