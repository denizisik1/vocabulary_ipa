# pylint: disable=broad-exception-caught


import sys
import signal
import logging
from dotenv import load_dotenv
from command_line_arguments import ArgumentParsing
from random_word import RandomWord
from data_analyzer import DataAnalyzer
from version_info import VersionInfo
from list_languages import ListLanguages
from retrieve_pronunciation import RetrievePronunciation


logging.basicConfig(level=logging.INFO)


def signal_handler(_sig, _frame):
    logging.info("Program interrupted. Exiting gracefully...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

load_dotenv()

arg_parser = ArgumentParsing()
args = arg_parser.parse_arguments()
if len(sys.argv) == 1:
    arg_parser.parser.print_help()
    sys.exit(0)

if args.random and args.language and args.number:
    try:
        random_word_generator = RandomWord(args.language, args.number)
        random_word_generator.get_random_word()
    except ValueError as e:
        logging.error("Value Error: %s", e)

if args.analyze and args.language:
    try:
        analyzer = DataAnalyzer(args.language)
        analyzer.analyze_data()
    except Exception as e:
        logging.error("Error during data analysis: %s", e)

if args.version:
    try:
        version_info = VersionInfo()
        print(version_info.version)
    except Exception as e:
        logging.error("Error displaying version info: %s", e)

if args.list_languages:
    try:
        language_lister = ListLanguages()
        language_lister.list_languages()
    except Exception as e:
        logging.error("Error listing languages: %s", e)

if args.retrieve_pronunciation and args.word:
    try:
        retriever = RetrievePronunciation()
        retriever.retrieve_pronunciation(args.word)
    except Exception as e:
        logging.error("Error retrieving pronunciation: %s", e)
