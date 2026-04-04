import importlib
import logging
import signal
import sys
from typing import Optional

import typer
from dotenv import load_dotenv

from database import check_for_language

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
    add_help_option=False,
)


def handle_test(language: Optional[str]) -> None:
    result = check_for_language(language)
    print(f"Test check for language '{language}': {result}")


def handle_random(language: Optional[str], number: Optional[int]) -> None:
    if not (language and number):
        return
    try:
        random_word = importlib.import_module("random_word")
        random_word.get_random_word(language, number)
    except ValueError as err:
        logging.error("Value Error: %s", err)


def handle_analyze(language: Optional[str]) -> None:
    if not language:
        return
    try:
        data_analyzer = importlib.import_module("data_analyzer")
        data_analyzer.analyze_data_for_language(language)
    except ImportError as err:
        logging.error("Error importing data analyzer: %s", err)
    except AttributeError as err:
        logging.error("Error during data analysis: %s", err)


def handle_version() -> None:
    try:
        version_info = importlib.import_module("version_info")
        typer.echo(version_info.display_version())
    except ImportError as err:
        logging.error("Error importing version info: %s", err)


def handle_list_languages() -> None:
    try:
        list_languages_module = importlib.import_module("list_languages")
        list_languages_module.list_languages()
    except ImportError as err:
        logging.error("Error importing list_languages: %s", err)


def handle_retrieve(language: Optional[str], word: Optional[str]) -> None:
    if not (language and word):
        return
    try:
        retrieve_module = importlib.import_module("retrieve_pronunciation")
        retrieve_module.retrieve_pronunciation(language, word)
    except ImportError as err:
        logging.error("Error importing retrieve_pronunciation: %s", err)


def validate_flag_dependencies(
    *,
    retrieve: bool,
    random: bool,
    analyze: bool,
    test: bool,
    clean: bool,
    confirm_clean: bool,
    language: Optional[str],
    number: Optional[int],
    word: Optional[str],
) -> list[str]:
    errors: list[str] = []

    if retrieve:
        if not language:
            errors.append("--retrieve requires --language/-l")
        if not word:
            errors.append("--retrieve requires --word/-w")

    if random:
        if not language:
            errors.append("--random requires --language/-l")
        if number is None:
            errors.append("--random requires --number/-n")
        elif number <= 0:
            errors.append("--number/-n must be a positive integer when using --random")

    if analyze and not language:
        errors.append("--analyze requires --language/-l")

    if test and not language:
        errors.append("--test requires --language/-l")

    if confirm_clean and not clean:
        errors.append("--purge/-c requires --clean/-C")

    return errors


@app.callback(invoke_without_command=True)
def main(  # pylint: disable=too-many-arguments, too-many-locals, too-many-positional-arguments
    ctx: typer.Context,
    show_help: bool = typer.Option(
        False, "--help", "-h", help="Show this help message and exit the program."
    ),
    retrieve: bool = typer.Option(
        False, "--retrieve", "-x", help="Retrieve Pronunciation from the web."
    ),
    clean: bool = typer.Option(
        False, "--clean", "-C", help="Clean incomplete data from the database."
    ),
    backup: bool = typer.Option(
        False, "--backup", "-b", help="Backup current data and print its location."
    ),
    analyze: bool = typer.Option(
        False, "--analyze", "-a", help="Analyze retrieved data and show output."
    ),
    good: bool = typer.Option(
        False, "--good", "-g", help="Mark current data as good and ready for use."
    ),
    version: bool = typer.Option(
        False, "--version", "-v", help="Show program version and exit the program."
    ),
    revert: bool = typer.Option(
        False, "--revert", "-R", help="Make another backup and revert to the last good data."
    ),
    test: bool = typer.Option(
        False, "--test", "-t", help="Just a test run. Only used during development."
    ),
    random: bool = typer.Option(
        False, "--random", "-r", help="Retrieve random number of word(s) for a language."
    ),
    language: Optional[str] = typer.Option(
        None, "--language", "-l", help="Specify the language to be used for the operation."
    ),
    number: Optional[int] = typer.Option(
        None, "--number", "-n", help="Specify the number of random words."
    ),
    word: Optional[str] = typer.Option(
        None, "--word", "-w", help="Specify a word to retrieve pronunciation for."
    ),
    confirm_clean: bool = typer.Option(
        False, "--purge", "-c", help="Clean incomplete data from the database."
    ),
    list_langs: bool = typer.Option(
        False, "--list-languages", "-e", help="List all available languages in the database."
    ),
) -> None:
    actions = [
        test,
        random,
        analyze,
        retrieve,
        revert,
        backup,
        good,
        clean,
        confirm_clean,
        version,
        list_langs,
    ]

    if ctx.invoked_subcommand is None and not any(actions):
        typer.echo(ctx.get_help())
        return

    if show_help:
        typer.echo(ctx.get_help())
        raise typer.Exit()

    validation_errors = validate_flag_dependencies(
        retrieve=retrieve,
        random=random,
        analyze=analyze,
        test=test,
        clean=clean,
        confirm_clean=confirm_clean,
        language=language,
        number=number,
        word=word,
    )
    if validation_errors:
        for err in validation_errors:
            typer.echo(f"Error: {err}")
        raise typer.Exit(code=2)

    if test:
        handle_test(language)

    if random:
        handle_random(language, number)

    if analyze:
        handle_analyze(language)

    if version:
        handle_version()

    if list_langs:
        handle_list_languages()

    if retrieve:
        handle_retrieve(language, word)


if __name__ == "__main__":
    app()
