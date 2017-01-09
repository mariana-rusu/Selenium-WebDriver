from selenium import webdriver
import unittest
import time

class FirstHeadline(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        #self.driver.get("localhost:5000/test")
        time.sleep(1)

    def test_Headline_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='choose-tile']/header/h2"))

    def t1est_Headline_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='choose-tile']/header/h2")
        self.assertEqual(element.text,"Let’s do this. What would you like to take a look at first?")


    def tearDown(self):
        self.driver.quit()