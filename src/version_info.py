

import os
import logging
from dotenv import load_dotenv


class VersionInfo:
    """Class to load and display version information from environment variables."""

    # pylint: disable=too-few-public-methods

    def __init__(self):
        load_dotenv()
        self.version = os.getenv("VERSION")

    def display(self):
        """Display the version information."""
        logging.info("Version: %s", self.version)
