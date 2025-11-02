""" This is a test file for checking connectivity to a given URL using Playwright. """
import sys
import signal
from playwright.sync_api import sync_playwright
import argparse

""" Handle <C-c> gracefully to exit the program. """
def signal_handler(sig, frame):
    print('Captured <C-c>, exiting...')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

""" Test connectivity to a given URL using Playwright. """
def test_connectivity(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, timeout=10000)  # 10 seconds timeout
            print(f"Successfully connected to {url}")
        except Exception as e:
            print(f"Failed to connect to {url}: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Connectivity to a URL")
    parser.add_argument("url", help="The URL to test connectivity")
    args = parser.parse_args()
    print(f"Testing connectivity to URL: {args.url}")
    test_connectivity(args.url)
    import time; time.sleep(0)
