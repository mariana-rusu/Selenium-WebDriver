from selenium import webdriver
import unittest
import time

class SearchJobsByKeywork(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        driver = self.driver
        time.sleep(1)
        search_jobs = driver.find_element_by_xpath("/html/body/header/nav[2]/a[2]")
        search_jobs.click()
        time.sleep(1)
        show_all_jobs = driver.find_element_by_xpath("//div/section[1]/div/div/div/div/a[2]/p")
        show_all_jobs.click()
        time.sleep(1)

    def test_SearchJobsByKeywork(self):

        driver = self.driver
        clear_filter = driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div/div/a/span")
        clear_filter.click()
        all_jobs = driver.find_element_by_xpath("//*[@id='listing']/div[1]/h1")
        self.assertTrue(all_jobs.text, "ALL JOBS")



    def tearDown(self):
        self.driver.quit()