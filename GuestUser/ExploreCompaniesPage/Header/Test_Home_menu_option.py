from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
import requests
from selenium.common.exceptions import WebDriverException

class Home(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        explore_companies = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[1]")
        explore_companies.click()

    def test_Home_class_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("/html/body/header/div/nav[2]/a[1]"))

    def test_Home_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("/html/body/header/div/nav[2]/a[1]")
        self.assertEqual(element.text,"HOME")


    def test_Home_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("/html/body/header/div/nav[2]/a[1]")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()