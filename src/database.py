"""Module for interacting with the pronunciation database."""

import sqlite3


class PronunciationDatabase:
    """Class for interacting with the pronunciation database."""

    def __init__(self):
        self.connection = sqlite3.connect("pronunciations.db")
        self.cursor = self.connection.cursor()

    def check_for_language(self, language):
        """Check if the specified language table exists in the database."""
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (language,),
        )

        return self.cursor.fetchone() is not None

    def retrieve_random_word(self, language, number=1):
        """Retrieve a random word along with its meaning and pronunciation."""
        self.cursor.execute(
            "SELECT article, word, meaning, pronunciation "  # nosec
            f"FROM {language} "
            "ORDER BY RANDOM() "
            f"LIMIT {number}"
        )

        result = self.cursor.fetchall()
        return result if result else None

    def analyze_data(self, language):
        """Return the number of rows lacking pronunciation data for the specified language."""
        self.cursor.execute(
            "SELECT COUNT(*) "  # nosec
            f"FROM {language} "
            "WHERE pronunciation IS NULL OR pronunciation = ''"
        )
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def list_available_languages(self):
        """List all available language tables in the database."""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cursor.fetchall()
        return [table[0] for table in tables if table[0].isalpha()]
