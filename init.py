import sys
import signal
from dotenv import load_dotenv
from environment import select_env_file
from command_line_arguments import ArgumentParsing
from random_word import RandomWord
from data_analyzer import DataAnalyzer

""" Handle <C-c> gracefully to exit the program. """
def signal_handler(sig, frame):
    print('Captured <C-c>, exiting...')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

""" Load environment variables based on the current Git branch. """
env_file = select_env_file()
load_dotenv(env_file)
# print(f"Environment variables loaded from {env_file}")

""" Parse command-line arguments. """
arg_parser = ArgumentParsing()
args = arg_parser.parse_arguments()
# print("Parsed command-line arguments:", args)

if args.random and args.language and args.number:
    try:
        random_word_generator = RandomWord(args.language, args.number)
        random_word_generator.get_random_word()
    except ValueError as e:
        print(e)

if args.analyze and args.language:
    try:
        analyzer = DataAnalyzer(args.language)
        analyzer.analyze_data()
    except Exception as e:
        print(f"Error during data analysis: {e}")
