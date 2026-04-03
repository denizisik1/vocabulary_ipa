import logging
import importlib
from database import check_for_language, retrieve_random_word


def get_random_word(language, number):
    if not check_for_language(language):
        raise ValueError(f"Language '{language}' not found in the database.")

    rows = retrieve_random_word(language, number)

    if rows is None:
        logging.info("No data retrieved from the database.")
        return

    if isinstance(rows, tuple) and (len(rows) == 0 or not isinstance(rows[0], (list, tuple))):
        rows = [rows]

    rich_table = importlib.import_module("rich.table")
    rich_console = importlib.import_module("rich.console")
    console = rich_console.Console()
    table = rich_table.Table(title=f"Random Words for {language.capitalize()}")
    table.add_column("Article", style="cyan", no_wrap=True)
    table.add_column("Word", style="magenta", no_wrap=True)
    table.add_column("Meaning", style="green", no_wrap=True)
    table.add_column("Pronunciation", style="yellow", no_wrap=True)

    for row in rows:
        article = row[0] or ""
        word = row[1] or ""
        meaning = row[2] or ""
        pronunciation = row[3] or ""
        table.add_row(article, word, meaning, pronunciation)

    console.print(table)
