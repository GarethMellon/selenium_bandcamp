import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import env
import os
from selenium.webdriver.common.keys import Keys
import time


class BandcampTest(unittest.TestCase):

    def setUp(self):
        """ run browser and load bandcamp page """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        # Add some settings to try and reduce the overhead on opening the page
        prefs = {
            "profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Set driver to headless mode
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome('drivers/chromedriver.exe', options=chrome_options)  # , options=chrome_options)

        self.driver.maximize_window()
        self.driver.get('https://bandcamp.com/')

    def test_landing_page(self):
        """ tested on landing page to check if it is valid """
        try:
            self.assertEqual(self.driver.title, "Bandcamp")  # assert page title matches
            assert self.driver.find_element_by_link_text('log in').get_attribute(
                'href') == "https://bandcamp.com/login?from=home"  # assert login link is correct
            c = self.driver.find_element_by_css_selector('.carousel-big-item').find_element(By.TAG_NAME,
                                                                                            "a").get_attribute("href")
            self.assertEqual(c,
                             'https://daily.bandcamp.com/2019/04/10/third-man-comes-to-bandcamp-and-the-raconteurs-share-new-song/')  # assert that a link held as a chile of am element is present
            self.assertTrue(self.driver.find_element_by_css_selector('.corp-bclogo').find_element(By.TAG_NAME,
                                                                                                  "svg"))  # assert that an svg tag is there within a class
        except AssertionError:
            raise AssertionError

    def test_login(self):
        """ tests on log in page """
        self.driver.find_element_by_link_text('log in').click()

        try:
            assert self.driver.title == "Log in | Bandcamp"
            assert self.driver.current_url == "https://bandcamp.com/login"
            self.assertTrue(self.driver.find_element_by_id('loginform'))
            assert self.driver.find_element_by_css_selector('.forgot-password').find_element(By.TAG_NAME,
                                                                                             "a").get_attribute(
                'href') == 'https://bandcamp.com/forgot_password'
        except AssertionError:
            raise AssertionError

    def tearDown(self):
        """ driver tear down """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
