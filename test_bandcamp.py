import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import env
import os
from selenium.webdriver.common.keys import Keys


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
            assert "Bandcamp" in self.driver.title  # assert page title matches
            assert self.driver.find_element_by_link_text('log in').get_attribute(
                'href') == "https://bandcamp.com/login?from=home"  # assert login link is correct

            carousel_link = self.driver.find_element_by_css_selector('.carousel-big-item').find_element(By.TAG_NAME,
                                                                                                        "a").get_attribute(
                "href")
            self.assertTrue(carousel_link)  # assert that a link held as a child of am element is present

            self.assertTrue(self.driver.find_element_by_css_selector('.corp-bclogo').find_element(By.TAG_NAME,
                                                                                                  "svg"))  # assert that an svg tag is there within a class
        except AssertionError:
            raise AssertionError

    def test_login(self):
        """ tests on log in page """
        self.driver.find_element_by_link_text('log in').click()

        try:
            assert "Log in | Bandcamp" in self.driver.title
            assert self.driver.current_url == "https://bandcamp.com/login"
            self.assertTrue(self.driver.find_element_by_id('loginform'))
            assert self.driver.find_element_by_css_selector('.forgot-password').find_element(By.TAG_NAME,
                                                                                             "a").get_attribute(
                'href') == 'https://bandcamp.com/forgot_password'
        except AssertionError:
            raise AssertionError

    def test_discover(self):
        """ test all the discover to ensure they are all present on the screen """
        genres = self.driver.find_element_by_css_selector('.discover-genres').find_elements(By.TAG_NAME, "span")
        slices = self.driver.find_element_by_css_selector('.discover-slices').find_elements(By.TAG_NAME, "span")
        formats = self.driver.find_element_by_css_selector('.discover-formats').find_elements(By.TAG_NAME, "span")

        genres_list = ["all", "electronic", "rock", "metal", "alternative", "hip-hop/rap", "experimental", "punk",
                       "folk", "pop", "ambient", "soundtrack", "world", "jazz", "acoustic", "funk", "r&b/soul",
                       "devotional",
                       "classical", "reggae", "podcasts", "country", "spoken word", "comedy", "blues", "kids",
                       "audiobooks",
                       "latin"]
        slices_list = ["best-selling", "new arrivals", "artist-recommended"]
        formats_list = ["any format", "digital", "vinyl", "compact disc", "cassette"]
        try:
            for g in genres:
                assert g.text in genres_list  # check that the genre list are correct
            for s in slices:
                assert s.text in slices_list  # check that the slices list are correct
            for f in formats:
                assert f.text in formats_list  # check that the formats list are correct
        except AssertionError:
            raise AssertionError

    def tearDown(self):
        """ driver tear down """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
