from selenium import webdriver
import unittest
import time

class Headline(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_Headline_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='choose-tile']/div[2]/div[1]/div/div/h2"))

    def test_Headline_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='choose-tile']/div[2]/div[1]/div/div/h2")
        self.assertEqual(element.text,"EXPLORE COMPANIES")


    def tearDown(self):
        self.driver.quit()