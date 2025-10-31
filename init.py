from environment import select_env_file
import os
from dotenv import load_dotenv
from tests.testing import test_connectivity

env_file = select_env_file()

load_dotenv(env_file)

print(f"Environment variables loaded from {env_file}")

test_connectivity()
