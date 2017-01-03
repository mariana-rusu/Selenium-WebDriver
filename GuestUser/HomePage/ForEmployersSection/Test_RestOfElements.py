from selenium import webdriver
import unittest
import time

class Headline(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_LinkText_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='homepage']/section[5]/section/a")
        self.assertEqual(element.text,"LEARN MORE »")

    def test_Video_text_is_found(self):

        driver = self.driver
        self.assertTrue(driver.find_element_by_xpath("//*[@id='homepage']/section[5]/div"))


    def tearDown(self):
        self.driver.quit()