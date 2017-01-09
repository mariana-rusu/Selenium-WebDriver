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
        assert (driver.find_element_by_xpath("//*[@id='homepage']/section[4]/h3"))

    def test_Headline_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='homepage']/section[4]/h3")
        self.assertEqual(element.text,"No bad apples here. We only work with top companies to make sure you'll have the kick-ass career you deserve.")


    def tearDown(self):
        self.driver.quit()