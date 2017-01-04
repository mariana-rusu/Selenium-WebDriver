from selenium import webdriver
import unittest
import time

class SearchJobsByKeywordAndByLocation(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)
        search_jobs = self.driver.find_element_by_xpath("/html/body/header/nav[2]/a[2]")
        search_jobs.click()

    def test_SearchJobsByKeywordAndByLocation(self):

        driver = self.driver
        element1 = driver.find_element_by_id('job_locationautocomplete')
        time.sleep(3)
        element1.send_keys("New York City Metro Area")
        time.sleep(3)
        element11 = driver.find_element_by_xpath("//div/section[1]/div/div/div/div/div[1]/div/form/div/div/ul/li[1]/button")
        element11.click()
        element2 = driver.find_element_by_xpath("//div/section[1]/div/div/div/div/div[2]/div/form/div/input")
        element2.send_keys("QA")
        button = driver.find_element_by_xpath("//div/section[1]/div/div/div/div/a[1]")
        button.click()
        time.sleep(10)

        applied_filter1 = driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div/ul/li[2]/button/span[1]")
        self.assertEqual(applied_filter1.text, "New York City Metro Area")
        applied_filter2 = driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div/ul/li[1]/button/span[1]")
        self.assertEqual(applied_filter2.text,"QA")

        headline = driver.find_element_by_xpath("//*[@id='listing']/div[1]/h1")
        self.assertEqual(headline.text, "QA JOBS IN NEW YORK CITY METRO AREA")



    def tearDown(self):
        self.driver.quit()