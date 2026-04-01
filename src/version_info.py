import os
import logging
from dotenv import load_dotenv


def display_version():
    load_dotenv()
    version = os.getenv("VERSION")
    logging.info("Version: %s", version)
    return version
