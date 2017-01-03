from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException

class Facebook(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_Facebook_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='footer']/div/div[5]/div/a[1]"))

    def test_Facebook_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='footer']/div/div[5]/div/a[1]")

        try:
            element.click()
        except WebDriverException as e:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()