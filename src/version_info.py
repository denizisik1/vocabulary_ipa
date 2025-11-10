"""Module to load and display version information from environment variables."""

import os
import logging

from dotenv import load_dotenv

from environment import select_env_file


class VersionInfo:
    """Class to load and display version information from environment variables."""
    # pylint: disable=too-few-public-methods

    def __init__(self):
        # pylint: disable-next=invalid-name
        ENV = select_env_file()
        # pylint: disable-next=invalid-name
        load_dotenv(ENV)
        self.version = os.getenv("VERSION")

    def display(self):
        """Display the version information."""
        logging.info("Version: %s", self.version)
