# import undetected_chromedriver as uc

# opts = uc.ChromeOptions()
# opts.add_argument("--headless")
# opts.add_argument("--no-sandbox")
# opts.add_argument("--disable-dev-shm-usage")

# driver = uc.Chrome(options=opts, use_subprocess=True)

# def visit_google():
#     try:
#         driver.get("https://www.google.com")
#         return driver.title
#     finally:
#         driver.quit()

# def test_connectivity():
#     google_title = visit_google()
#     print("Title:", driver.title)

# nodriver and zendriver are your other options.

import pytest
from seleniumbase import Driver

def test_connectivity():
    driver = Driver(headless=True)
    driver.open("https://seleniumbase.io/")

    title = driver.title

    print("\nPage title:", title)
    assert "SeleniumBa  falskdjflsakdj se" in title

    driver.quit()
