from selenium import webdriver
import unittest
import time

class Paragraph(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_paragraph_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='homepage']/section[5]/section/p"))

    def test_paragraph_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='homepage']/section[5]/section/p")
        self.assertEqual(element.text,"Let us help you reach all your hiring goals this year. Even the super aggressive ones.")


    def tearDown(self):
        self.driver.quit()