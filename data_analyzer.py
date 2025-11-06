import logging
from database import PronunciationDatabase

class DataAnalyzer:
    def __init__(self, language):
        self.language = language
        self.db = PronunciationDatabase()

    def analyze_data(self):
        """ Return the number of rows lacking pronunciation data for the specified language. """
        if not self.db.check_for_language(self.language):
            raise ValueError(f"Language '{self.language}' not found in the database.")
        count = self.db.analyze_data(self.language)
        logging.info(f"Number of entries without pronunciation data for '{self.language}': {count}")
        return self.db.analyze_data(self.language)
