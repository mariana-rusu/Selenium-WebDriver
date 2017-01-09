from selenium import webdriver
import unittest
import time

class SearchJobsByKeyword(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        search_jobs = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[2]")
        search_jobs.click()
        time.sleep(1)

    def test_SearchJobsByKeyword(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//div/section[1]/div/div/div/div/div[2]/div/form/div/input")
        element.send_keys("QA")
        button = driver.find_element_by_xpath("//div/section[1]/div/div/div/div/a[1]")
        button.click()
        applied_filter = driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div/ul/li/button/span[1]")
        self.assertEqual(applied_filter.text,"QA")
        self.assertTrue(driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div/div/a/span"))
        headline = driver.find_element_by_xpath("//*[@id='listing']/div[1]/h1")
        self.assertEqual(headline.text, "QA JOBS")



    def tearDown(self):
        self.driver.quit()