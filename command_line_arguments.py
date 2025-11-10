import argparse

from random_word import RandomWord
from argparse import RawTextHelpFormatter


class ArgumentParsing:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                prog="LanguagePronunciationScraper",
                add_help=False,
                description="Language Pronunciation Scraper",
                formatter_class=RawTextHelpFormatter)

        self.parser.add_argument("-r",
                                 "--random",
                                 action="store_true",
                                 help="         Retrieve random word(s) with pronunciation. (Requires -l and -n)")

        self.parser.add_argument("-l",
                                 "--language",
                                 type=str,
                                 metavar="",
                                 help="[String] Specify the language for the random word.")

        self.parser.add_argument("-n",
                                 "--number",
                                 type=int,
                                 metavar="",
                                 help="[Number] Number of random words to retrieve.")

        self.parser.add_argument("-a",
                                 "--analyze",
                                 action="store_true",
                                 help="         Analyze scraped data.                       (Requires -l)")

        self.parser.add_argument("-s",
                                 "--scrape",
                                 action="store_true",
                                 help="         Scrape data from the web.                   (Requires -l)")

        self.parser.add_argument("-R",
                                 "--revert",
                                 action="store_true",
                                 help="         Revert to previous data.                    (Requires -l)")

        self.parser.add_argument("-b",
                                 "--backup",
                                 action="store_true",
                                 help="         Backup current data.")

        self.parser.add_argument("-g",
                                 "--good",
                                 action="store_true",
                                 help="         Mark data as good.                          (Requires -l)")

        self.parser.add_argument("-C",
                                 "--clean",
                                 action="store_true",
                                 help="         Clean incomplete data.                      (Requires -l)")

        self.parser.add_argument("-c",
                                 "--confirm-clean",
                                 action="store_true",
                                 help="         Confirm and clean incomplete data.          (Requires -l)")

        self.parser.add_argument("-f",
                                 "--input",
                                 type=str,
                                 metavar="",
                                 help="[String] Input file for data.                        (Requires -l)")

        self.parser.add_argument("-o",
                                 "--output",
                                 type=str,
                                 metavar="",
                                 help="[String] Output file for data.                       (Requires -l)")

        # Provide reference to https://en.wikipedia.org/wiki/Help:IPA/Standard_German
        self.parser.add_argument("-i",
                                 "--ipa-wikipedia",
                                 action="store_true",
                                 help="         Use IPA Wikipedia as the data source.")

        self.parser.add_argument("-d",
                                 "--debug",
                                 action="store_true",
                                 help="         Enable debug mode.")

        self.parser.add_argument("-V",
                                 "--version",
                                 action="store_true",
                                 help="         Show program version and exit.")

        self.parser.add_argument("-e",
                                 "--list-languages",
                                 action="store_true",
                                 help="         List all available languages in the database.")

        self.parser.add_argument("-k",
                                 "--set-language",
                                 type=str,
                                 metavar="",
                                 help="[String] Set the default language for operations.")

        self.parser.add_argument("-m",
                                 "--set-number",
                                 type=int,
                                 metavar="",
                                 help="[Number] Set the default number of words to retrieve.")

        group = self.parser.add_mutually_exclusive_group()

        group.add_argument("-q",
                           "--quiet",
                           action="store_true",
                           help="         Suppress output messages.")

        group.add_argument("-v",
                           "--verbose",
                           action="store_true",
                           help="         Enable verbose output messages.")

    def parse_arguments(self):
        return self.parser.parse_args()
