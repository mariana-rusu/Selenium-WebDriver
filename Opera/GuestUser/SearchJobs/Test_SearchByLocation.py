from selenium import webdriver
import unittest
import time

class SearchJobsByLocation(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Opera()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        search_jobs = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[2]")
        search_jobs.click()
        time.sleep(1)

    def test_SearchJobsByLocation(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='job_locationautocomplete']")
        element.send_keys("New York")
        button = driver.find_element_by_xpath("//div/section[1]/div/div/div/div/a[1]")
        button.click()
        applied_filter = driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div/ul/li/button/span[1]")
        self.assertEqual(applied_filter.text,"New York")
        self.assertTrue(driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div/div/a/span"))
        headline = driver.find_element_by_xpath("//*[@id='listing']/div[1]/h1")
        self.assertEqual(headline.text, "NEW YORK JOBS")



    def tearDown(self):
        self.driver.quit()