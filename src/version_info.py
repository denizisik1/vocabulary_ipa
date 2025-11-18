"""Module to load and display version information from environment variables."""

import os
import logging
from dotenv import load_dotenv
from environment import select_env_file


class VersionInfo:
    """Class to load and display version information from environment variables."""

    # pylint: disable=too-few-public-methods

    def __init__(self):
        env = select_env_file()  # pylint: disable=invalid-name
        load_dotenv(env)
        self.version = os.getenv("VERSION")

    def display(self):
        """Display the version information."""
        logging.info("Version: %s", self.version)
