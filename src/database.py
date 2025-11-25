import sqlite3


class PronunciationDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("pronunciations.db")
        self.cursor = self.connection.cursor()

    def check_for_language(self, language):
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (language,),
        )

        return self.cursor.fetchone() is not None

    def retrieve_random_word(self, language, number=1):
        self.cursor.execute(
            "SELECT article, word, meaning, pronunciation "  # nosec
            f"FROM {language} "
            "ORDER BY RANDOM() "
            f"LIMIT {number}"
        )

        result = self.cursor.fetchall()
        return result if result else None

    def analyze_data(self, language):
        self.cursor.execute(
            "SELECT COUNT(*) "  # nosec
            f"FROM {language} "
            "WHERE pronunciation IS NULL OR pronunciation = ''"
        )
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def list_available_languages(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cursor.fetchall()
        return [table[0] for table in tables if table[0].isalpha()]
