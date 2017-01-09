from selenium import webdriver
import unittest
import time

class FirstHeadline(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_Headline_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='top-image']/div/h1"))

    def test_Headline_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='top-image']/div/h1")
        self.assertEqual(element.text,"We've helped over 50 million people with their careers")


    def tearDown(self):
        self.driver.quit()