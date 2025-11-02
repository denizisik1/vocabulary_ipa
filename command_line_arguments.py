import argparse
# from random_word import RandomScrape
# from analyze_database import Analyze
# from scrape_online import Scrape
# from revert_back import Revert
# from backup_data import Backup
# from good_only import MarkGood
# from display_clean import Clean
# from clean_data import ConfirmClean
# from input_handler import InputHandler

class ArgumentParsing:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Language Pronunciation Scraper")
        self.parser.add_argument("-r", "--random", action="store_true", help="Scrape random entries")
        self.parser.add_argument("-a", "--analyze", action="store_true", help="Analyze scraped data")
        self.parser.add_argument("-s", "--scrape", action="store_true", help="Scrape data from the web")
        self.parser.add_argument("-R", "--revert", action="store_true", help="Revert to previous data")
        self.parser.add_argument("-b", "--backup", action="store_true", help="Backup current data")
        self.parser.add_argument("-g", "--good", action="store_true", help="Mark data as good")
        self.parser.add_argument("-C", "--clean", action="store_true", help="Clean incomplete data")
        self.parser.add_argument("-c", "--confirm-clean", action="store_true", help="Confirm and clean incomplete data")
        self.parser.add_argument("-i", "--input", type=str, help="Input file for data")

    def parse_arguments(self):
        return self.parser.parse_args()
