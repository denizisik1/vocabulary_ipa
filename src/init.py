# pylint: disable=broad-exception-caught

"""Main entry point for the application."""

import sys
import signal
import logging
from dotenv import load_dotenv
from environment import select_env_file
from command_line_arguments import ArgumentParsing
from random_word import RandomWord
from data_analyzer import DataAnalyzer
from version_info import VersionInfo


logging.basicConfig(level=logging.INFO)


def signal_handler(_sig, _frame):
    """Handle <C-c> gracefully to exit the program."""
    logging.info("Program interrupted. Exiting gracefully...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


env = select_env_file()  # pylint: disable=invalid-name
load_dotenv(env)

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
