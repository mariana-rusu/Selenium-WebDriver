from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException

class FilterCompanies(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        explore_companies = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[1]")
        explore_companies.click()

    def test_FilterCompanies_menu_option_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/a[2]"))

    def test_FilterCompanies_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/a[2]")
        self.assertEqual(element.text,"Filter Companies")


    def test_FilterCompanies_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/a[2]")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()