from database import PronunciationDatabase

class RandomWord:
    def __init__(self, language):
        self.language = language
        self.db = PronunciationDatabase()

    def get_random_word(self):
        if not self.db.check_for_language(self.language):
            raise ValueError(f"Language '{self.language}' not found in the database.")
        random_word = self.db.retrieve_random_word(self.language)

        # Replace this with ncurses like TUI later.
        final_output = ""
        if random_word:
            headers = ["Article", "Word", "Meaning", "Pronunciation"]
            max_lengths = [len(header) for header in headers]

            for i, value in enumerate(random_word):
                if value is not None:
                    max_lengths[i] = max(max_lengths[i], len(str(value)))

            header_line = "\t".join(header.ljust(max_lengths[i]) for i, header in enumerate(headers))
            separator_line = "\t".join("-" * max_lengths[i] for i in range(len(headers)))
            value_line = "\t".join(str(value).ljust(max_lengths[i]) if value is not None else "N/A".ljust(max_lengths[i]) for i, value in enumerate(random_word))

            final_output += header_line + "\n"
            final_output += separator_line + "\n"
            final_output += value_line + "\n"
        print(final_output)

        return self.db.retrieve_random_word(self.language)
