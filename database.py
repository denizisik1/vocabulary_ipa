import sqlite3

class PronunciationDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('pronunciations.db')
        self.cursor = self.connection.cursor()

    def check_for_language(self, language):
        """ Check if the specified language table exists in the database. """
        self.cursor.execute("SELECT name "
                            "FROM sqlite_master "
                            "WHERE type='table' "
                            "AND name=?",
                            (language,))
        return self.cursor.fetchone() is not None

    def retrieve_random_word(self, language):
        """ Retrieve a random word along with its meaning and pronunciation for the specified language. """
        self.cursor.execute("SELECT article, word, meaning, pronunciation "
                            f"FROM {language} "
                            "ORDER BY RANDOM() "
                            "LIMIT 1")

        result = self.cursor.fetchall()
        return result[0] if result else None

    def analyze_data(self, language):
        """ Return the number of rows lacking pronunciation data for the specified language. """
        self.cursor.execute("SELECT COUNT(*) "
                            f"FROM {language} "
                            "WHERE pronunciation IS NULL OR pronunciation = ''")
        result = self.cursor.fetchone()
        return result[0] if result else 0
