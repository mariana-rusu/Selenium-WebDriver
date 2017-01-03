from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException

class FirstSlide(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        explore_companies = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[1]")
        explore_companies.click()
        first_element = self.driver.find_element_by_xpath("//div/div/div/div/div/a[1]/i")
        first_element.click()

    def test_first_tile_is_found(self):
        driver = self.driver
        driver.find_element_by_xpath("//div/div/div/section/div/div[2]/div[1]/div/div/a/div[1]")

    def test_first_tile_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//div/div/div/section/div/div[2]/div[1]/div/div/a/div[1]")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def test_first_tile_header_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//div/div/div/section/div/div[2]/div[1]/div/div/a/div[2]/h2")
        self.assertEqual(element.text, 'AT&T')


    def tearDown(self):
        self.driver.quit()