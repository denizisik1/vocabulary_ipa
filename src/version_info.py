import os
import logging
from dotenv import load_dotenv


class VersionInfo:
    def __init__(self):
        load_dotenv()
        self.version = os.getenv("VERSION")

    def display(self):
        logging.info("Version: %s", self.version)
