from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
import requests
from selenium.common.exceptions import WebDriverException

class Search(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        explore_companies = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[1]")
        explore_companies.click()

    def test_Search_class_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("/html/body/header/div/div/i"))

    def test_Search_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("/html/body/header/div/div/i")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()