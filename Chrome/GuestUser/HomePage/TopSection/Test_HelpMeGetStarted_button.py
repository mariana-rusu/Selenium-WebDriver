from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException

class HelpMeGetStarted(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_HelpMeGetStarted_button_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='top-image']/div/div/a[1]"))

    def test_HelpMeGetStarted_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='top-image']/div/div/a[1]")
        self.assertEqual(element.text,"HELP ME GET STARTED")


    def test_HelpMeGetStarted_button_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='top-image']/div/div/a[1]")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()