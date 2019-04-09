import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BandcampTest(unittest.TestCase):
    """ run browser and load bandcamp page """
    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://bandcamp.com/')
        self.driver.implicitly_wait(1)

    def test_basic(self):
        assert "1" == "2"

    def tearDown(self):
        """ driver tear down """
        self.driver.close()

if __name__ =="__main__":
    unittest.main()