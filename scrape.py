""" There are alternative drivers to seleniumbase e.g. nodriver or zendriver. """
from seleniumbase import Driver

class Scrape:
    pass
    # def __init__(self, url, base_url_element):
    #     self.url = url
    #     self.base_url_element = base_url_element

    # def seleniumbase(self):
    #     driver = Driver(headless=True)
    #     try:
    #         driver.open(self.url)
    #         element_text = driver.get_text(self.base_url_element)
    #         print(f"Element text from {self.url}: {element_text}")
    #         return element_text
    #     finally:
    #         driver.quit()
