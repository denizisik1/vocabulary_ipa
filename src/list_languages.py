import logging
import importlib
from database import list_available_languages


def list_languages():
    languages = list_available_languages() or []

    if not languages:
        logging.info("No languages found in the database.")
        return []

    rich_table = importlib.import_module('rich.table')
    rich_console = importlib.import_module('rich.console')
    console = rich_console.Console()
    table = rich_table.Table(title="Available Languages in the Database")
    table.add_column("Language", style="cyan", no_wrap=True)

    for lang in languages:
        table.add_row(lang)

    console.print(table)

    return languages
