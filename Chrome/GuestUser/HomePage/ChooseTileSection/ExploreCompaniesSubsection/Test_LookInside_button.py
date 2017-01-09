from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException

class LookInside(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_LookInside_button_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='choose-tile']/div[2]/div[1]/div/div/a[2]"))

    def test_LookInside_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='choose-tile']/div[2]/div[1]/div/div/a[2]")
        self.assertEqual(element.text,"LOOK INSIDE")


    def test_LookInside_button_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='choose-tile']/div[2]/div[1]/div/div/a[2]")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()