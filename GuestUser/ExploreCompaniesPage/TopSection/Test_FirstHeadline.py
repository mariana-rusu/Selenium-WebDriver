from selenium import webdriver
import unittest
import time

class FirstHeadline(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        explore_companies = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[1]")
        explore_companies.click()

    def test_Headline_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//div/div/div[2]/div[1]/div/div[1]/h1"))

    def test_Headline_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//div/div/div[2]/div[1]/div/div[1]/h1")
        self.assertEqual(element.text,"EXPLORE COMPANIES")


    def tearDown(self):
        self.driver.quit()