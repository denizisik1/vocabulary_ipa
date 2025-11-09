from dotenv import load_dotenv
from environment import select_env_file
import logging
import os

class VersionInfo:
    def __init__(self):
        env_file = select_env_file()
        load_dotenv(env_file)
        self.version = os.getenv("VERSION")

    def display(self):
        logging.info(f"Version: {self.version}")
