import argparse
from random_word import RandomWord

# TODO: Add short flags for --list-languages, --set-default-language, --set-default-number.
# TODO: Quiet and verbose should be mutually exclusive.
# TODO: Test what happens if no arguments are provided.

class ArgumentParsing:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                description="Language Pronunciation Scraper")

        self.parser.add_argument("-r",
                                 "--random",
                                 action="store_true",
                                 help="Get a random word from the database.")

        self.parser.add_argument("-l",
                                 "--language",
                                 type=str,
                                 help="Specify the language for the random word.")

        self.parser.add_argument("-n",
                                 "--number",
                                 type=int,
                                 help="Number of random words to retrieve.")

        self.parser.add_argument("-a",
                                 "--analyze",
                                 action="store_true",
                                 help="Analyze scraped data.")

        self.parser.add_argument("-s",
                                 "--scrape",
                                 action="store_true",
                                 help="Scrape data from the web.")

        self.parser.add_argument("-R",
                                 "--revert",
                                 action="store_true",
                                 help="Revert to previous data.")

        self.parser.add_argument("-b",
                                 "--backup",
                                 action="store_true",
                                 help="Backup current data.")

        self.parser.add_argument("-g",
                                 "--good",
                                 action="store_true",
                                 help="Mark data as good.")

        self.parser.add_argument("-C",
                                 "--clean",
                                 action="store_true",
                                 help="Clean incomplete data.")

        self.parser.add_argument("-c",
                                 "--confirm-clean",
                                 action="store_true",
                                 help="Confirm and clean incomplete data.")

        self.parser.add_argument("-f",
                                 "--input",
                                 type=str,
                                 help="Input file for data.")

        self.parser.add_argument("-o",
                                 "--output",
                                 type=str,
                                 help="Output file for data.")

        # Provide reference to https://en.wikipedia.org/wiki/Help:IPA/Standard_German
        self.parser.add_argument("-i",
                                 "--ipa-wikipedia",
                                 action="store_true",
                                 help="Use IPA Wikipedia as the data source.")

        self.parser.add_argument("-v",
                                 "--verbose",
                                 action="store_true",
                                 help="Enable verbose output.")

        self.parser.add_argument("-d",
                                 "--debug",
                                 action="store_true",
                                 help="Enable debug mode.")

        self.parser.add_argument("-q",
                                 "--quiet",
                                 action="store_true",
                                 help="Enable quiet mode.")

        self.parser.add_argument("-V",
                                 "--version",
                                 action="version",
                                 version="Language Pronunciation Scraper 1.0",
                                 help="Show program version and exit.")

        self.parser.add_argument("-h",
                                 "--help",
                                 action="help",
                                 help="Show this help message and exit.")

        self.parser.add_argument("--list-languages",
                                 action="store_true",
                                 help="List all available languages in the database.")

        self.parser.add_argument("--set-default-language",
                                 type=str,
                                 help="Set the default language for operations.")

        self.parser.add_argument("--set-default-number",
                                 type=int,
                                 help="Set the default number of words to retrieve.")

    def parse_arguments(self):
        return self.parser.parse_args()
