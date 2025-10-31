import os
import sys
from dotenv import load_dotenv

branch_name = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

def select_env_file():

    env_file = ""

    if branch_name == "main":
        env_file = ".env.production"
        print("Loading production environment variables.")

    elif branch_name == "testing":
        env_file = ".env.testing"
        print("Loading testing environment variables.")

    elif branch_name == "development":
        env_file = ".env.development"
        print("Loading development environment variables.")

    else:
        print(f"Unknown branch '{branch_name}'.")
        sys.exit(0)

    return env_file
