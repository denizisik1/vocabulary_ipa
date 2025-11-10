import os
import logging

from dotenv import load_dotenv

from environment import select_env_file


class VersionInfo:
    def __init__(self):
        ENV_FILE = select_env_file()
        load_dotenv(ENV_FILE)
        self.version = os.getenv("VERSION")

    def display(self):
        logging.info(f"Version: {self.version}")
