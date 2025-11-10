"""Module to select environment file based on current Git branch."""

import sys
import os
import logging


branch_name = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()


def select_env_file():
    """Select the appropriate .env file based on the current Git branch."""

    env_file = ""

    if branch_name == "main":
        env_file = ".env.production"

    elif branch_name == "testing":
        env_file = ".env.testing"

    elif branch_name == "development":
        env_file = ".env.development"

    else:
        logging.error("Unrecognized branch name: %s Exiting.", branch_name)
        sys.exit(0)

    return env_file
