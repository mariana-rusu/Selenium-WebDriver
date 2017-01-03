from selenium import webdriver
import unittest
import time

class SecondHeadline(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_Headline_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='top-image']/div/div/h2"))

    def test_Headline_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='top-image']/div/div/h2")
        self.assertEqual(element.text,"Browse jobs, explore the inside of top companies, and meet the people that work there. Get expert advice and connect with a career coach who’ll help give your career a major boost.")


    def tearDown(self):
        self.driver.quit()