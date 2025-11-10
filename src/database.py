"""Module for interacting with the pronunciation database."""

import sqlite3

# Explicit whitelist of language tables.
# Add new languages by extending these dicts with fully static query strings.
SELECT_RANDOM_SQL = {
    "en": ("SELECT article, word, meaning, pronunciation " "FROM en ORDER BY RANDOM() LIMIT ?"),
    "de": ("SELECT article, word, meaning, pronunciation " "FROM de ORDER BY RANDOM() LIMIT ?"),
}

COUNT_MISSING_SQL = {
    "en": ("SELECT COUNT(*) FROM en " "WHERE pronunciation IS NULL OR pronunciation = ''"),
    "de": ("SELECT COUNT(*) FROM de " "WHERE pronunciation IS NULL OR pronunciation = ''"),
}


class PronunciationDatabase:
    """Class to interact with the pronunciation database."""

    def __init__(self, path="pronunciations.db"):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def check_for_language(self, language):
        """Confirm the table exists AND is whitelisted."""
        if language not in SELECT_RANDOM_SQL:
            return False
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (language,),
        )
        return self.cursor.fetchone() is not None

    def retrieve_random_word(self, language, number=1):
        """Return up to `number` random words for a whitelisted language table."""
        if not self.check_for_language(language):
            raise ValueError("Invalid or missing language table")
        if not isinstance(number, int) or number < 1:
            raise ValueError("number must be a positive integer")

        query = SELECT_RANDOM_SQL[language]
        self.cursor.execute(query, (number,))
        rows = self.cursor.fetchall()
        return rows if rows else None

    def analyze_data(self, language):
        """Count rows lacking pronunciation for a whitelisted language table."""
        if not self.check_for_language(language):
            raise ValueError("Invalid or missing language table")

        query = COUNT_MISSING_SQL[language]
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        return row[0] if row else 0

    def close(self):
        """Close the database connection."""
        try:
            self.cursor.close()
        finally:
            self.connection.close()
