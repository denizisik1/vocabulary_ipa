from database import PronunciationDatabase

class RandomWord:
    def __init__(self, language):
        self.language = language
        self.db = PronunciationDatabase()

    def get_random_word(self):
        if not self.db.check_for_language(self.language):
            raise ValueError(f"Language '{self.language}' not found in the database.")
        random_word = self.db.retrieve_random_word(self.language)

        article = (random_word[0] if random_word[0] is not None else "").ljust(40)[:40]
        word = (random_word[1] if random_word[1] is not None else "").ljust(40)[:40]
        meaning = (random_word[2] if random_word[2] is not None else "").ljust(40)[:40]
        pronunciation = (random_word[3] if random_word[3] is not None else "").ljust(40)[:40]

        print(f"{article} {word} {meaning} {pronunciation}")
