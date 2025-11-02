import sys
import signal
import argparse
from dotenv import load_dotenv

from environment import select_env_file
from scrape import Scrape

""" Handle <C-c> gracefully to exit the program. """
def signal_handler(sig, frame):
    print('Captured <C-c>, exiting...')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

""" Load environment variables based on the current Git branch. """
env_file = select_env_file()
load_dotenv(env_file)
print(f"Environment variables loaded from {env_file}")

""" Initialize and run the scraper. """
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Scraper")
    parser.add_argument("url", help="The URL to scrape")
    parser.add_argument("base_url_element", help="The CSS selector of the element to scrape")
    args = parser.parse_args()
    print(f"Scraping URL: {args.url} for element: {args.base_url_element}")
    import time; time.sleep(0)

""" Use playwright instead of seleniumbase. """
