import os
import sys
import logging
from dotenv import load_dotenv

branch_name = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

def select_env_file():

    env_file = ""

    if branch_name == "main":
        env_file = ".env.production"

    elif branch_name == "testing":
        env_file = ".env.testing"

    elif branch_name == "development":
        env_file = ".env.development"

    else:
        logging.error(f"Unrecognized branch name: {branch_name}. Exiting.")
        sys.exit(0)

    return env_file
