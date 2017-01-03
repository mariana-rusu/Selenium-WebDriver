from selenium import webdriver
import unittest
import time

class Paragraph(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        explore_companies = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[1]")
        explore_companies.click()

    def test_Paragraph_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//div/div/div[2]/div[1]/div/div[2]/p"))

    def test_Paragraph_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//div/div/div[2]/div[1]/div/div[2]/p")
        self.assertEqual(element.text,"We think company culture is pretty important. We show you inside offices before you apply to make sure you'll love working there.")


    def tearDown(self):
        self.driver.quit()