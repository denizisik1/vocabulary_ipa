import typer
import sys
import signal
import logging
from typing import Optional
from dotenv import load_dotenv
from random_word import get_random_word
from data_analyzer import analyze_data_for_language
from version_info import display_version
from list_languages import list_languages
from retrieve_pronunciation import retrieve_pronunciation

logging.basicConfig(level=logging.INFO)

def signal_handler(_sig, _frame):
    logging.info("Program interrupted. Exiting gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

load_dotenv()

app = typer.Typer(
    name="LanguagePronunciationRetriever",
    help="Language Pronunciation Retriever",
    add_completion=False,
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    test: bool = typer.Option(False, "--test", "-t", help="Just a test run."),
    random: bool = typer.Option(False, "--random", "-r", help="Retrieve random word(s) with pronunciation. (Requires --language and --number)"),
    language: Optional[str] = typer.Option(None, "--language", "-l", help="[String] Specify the language for the random word."),
    number: Optional[int] = typer.Option(None, "--number", "-n", help="[Number] Number of random words to retrieve."),
    analyze: bool = typer.Option(False, "--analyze", "-a", help="Analyze retrieved data. (Requires --language)"),
    retrieve: bool = typer.Option(False, "--retrieve", "-x", help="Retrieve data from the web. (Requires --language)"),
    word: Optional[str] = typer.Option(None, "--word", "-w", help="[String] Specify a word to retrieve pronunciation for. (Requires --language)"),
    revert: bool = typer.Option(False, "--revert", "-R", help="Revert to previous data. (Requires --language)"),
    backup: bool = typer.Option(False, "--backup", "-b", help="Backup current data."),
    good: bool = typer.Option(False, "--good", "-g", help="Mark data as good. (Requires --language)"),
    clean: bool = typer.Option(False, "--clean", "-C", help="Clean incomplete data. (Requires --language)"),
    confirm_clean: bool = typer.Option(False, "--confirm-clean", "-c", help="Confirm and clean incomplete data. (Requires --language)"),
    input_file: Optional[str] = typer.Option(None, "--input", "-f", help="[String] Input file for data. (Requires --language)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="[String] Output file for data. (Requires --language)"),
    ipa_wikipedia: bool = typer.Option(False, "--ipa-wikipedia", "-i", help="Use IPA Wikipedia as the data source."),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode."),
    version: bool = typer.Option(False, "--version", "-v", help="Show program version and exit."),
    list_languages: bool = typer.Option(False, "--list-languages", "-e", help="List all available languages in the database."),
    set_language: Optional[str] = typer.Option(None, "--set-language", "-k", help="[String] Set the default language for operations."),
    set_number: Optional[int] = typer.Option(None, "--set-number", "-m", help="[Number] Set the default number of words to retrieve."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress output messages."),
    verbose: bool = typer.Option(False, "--verbose", "-V", help="Enable verbose output messages."),
):
    # If no arguments provided, show help
    if ctx.invoked_subcommand is None and not any([test, random, analyze, retrieve, revert, backup, good, clean, confirm_clean, version, list_languages]):
        typer.echo(ctx.get_help())
        return
    
    if test:
        logging.info("This is a test run. No operations will be performed.")

    if random and language and number:
        try:
            get_random_word(language, number)
        except ValueError as e:
            logging.error("Value Error: %s", e)

    if analyze and language:
        try:
            analyze_data_for_language(language)
        except Exception as e:
            logging.error("Error during data analysis: %s", e)

    if version:
        try:
            typer.echo(display_version())
        except Exception as e:
            logging.error("Error displaying version info: %s", e)

    if list_languages:
        try:
            list_languages()
        except Exception as e:
            logging.error("Error listing languages: %s", e)

    if retrieve and word and language:
        try:
            retrieve_pronunciation(language, word)
        except Exception as e:
            logging.error("Error retrieving pronunciation: %s", e)


if __name__ == "__main__":
    app()
