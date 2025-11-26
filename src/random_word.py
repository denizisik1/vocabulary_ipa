import logging
from database import PronunciationDatabase


class RandomWord:
    def __init__(self, language, number):
        self.language = language
        self.number = number
        self.db = PronunciationDatabase()

    def get_random_word(self):
        """
        Replace the existing get_random_word method with this version.

        Behavior:
        - Validates language exists.
        - Retrieves up to `self.number` rows (the DB method may return one
          row or an iterable of rows; we normalize to an iterable).
        - Prints each row with fixed-width columns using ljust and safe None->"".
        """
        if not self.db.check_for_language(self.language):
            raise ValueError(f"Language '{self.language}' not found in the database.")

        rows = self.db.retrieve_random_word(self.language, self.number)

        if rows is None:
            logging.info("No data retrieved from the database.")
            return

        if isinstance(rows, tuple) and (len(rows) == 0 or not isinstance(rows[0], (list, tuple))):
            rows = [rows]

        col_w = 40
        print(
            f"{'article'.ljust(col_w)} {'word'.ljust(col_w)} "
            f"{'meaning'.ljust(col_w)} {'pronunciation'.ljust(col_w)}"
        )
        print("-" * (col_w * 4 + 3))

        for row in rows:
            article = (row[0] or "").ljust(col_w)[:col_w]
            word = (row[1] or "").ljust(col_w)[:col_w]
            meaning = (row[2] or "").ljust(col_w)[:col_w]
            pronunciation = (row[3] or "").ljust(col_w)[:col_w]

            print(f"{article} {word} {meaning} {pronunciation}")
