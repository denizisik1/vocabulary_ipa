import pytest
from seleniumbase import Driver

def test_connectivity():
    driver = Driver(headless=True)
    driver.open("https://seleniumbase.io/")

    title = driver.title

    print("\nPage title:", title)
    assert "Selenium" in title

    driver.quit()
