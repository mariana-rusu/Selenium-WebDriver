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
        assert (driver.find_element_by_xpath("//*[@id='choose-tile']/div[1]/div[1]/div/div/p"))

    def test_paragraph_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='choose-tile']/div[1]/div[1]/div/div/p")
        self.assertEqual(element.text,"Honest and expert advice for all of your most pressing career questions")


    def tearDown(self):
        self.driver.quit()