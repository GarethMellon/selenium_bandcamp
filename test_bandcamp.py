import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BandcampTest(unittest.TestCase):
    """ run browser and load bandcamp page """

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()

        # Add some settings to try and reduce the overhead on opening the page
        prefs = {
            "profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Set driver to headless mode
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome('drivers/chromedriver.exe', options=chrome_options)

        self.driver.maximize_window()
        self.driver.get('https://bandcamp.com/')

    def test_landing_page(self):
        self.assertEqual(self.driver.title, "Bandcamp")

    def tearDown(self):
        """ driver tear down """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
