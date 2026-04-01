import logging
from database import list_available_languages


def list_languages():
    languages = list_available_languages() or []

    if not languages:
        logging.info("No languages found in the database.")
        return []

    print("\nAvailable languages in the database:")
    for lang in languages:
        print(lang)

    return languages
