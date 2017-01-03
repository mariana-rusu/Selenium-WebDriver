from selenium import webdriver
import unittest
import time
import requests
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

class Logo(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_Logo_class_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='homepage']/section[6]/div/div[2]"))


    def test_Logo_image_is_found(self):

        driver = self.driver
        example_images = driver.find_elements(By.XPATH, '//section[6]/div/div[2]/img')

        self.verificationErrors = []
        for image in example_images:
            current_link = image.get_attribute("src")
            r = requests.get(current_link)
            try:
                self.assertEqual(r.status_code, 200)
            except AssertionError:
                self.verificationErrors.append(current_link + ' delivered response code of ' + r.status_code)

    def tearDown(self):
        self.driver.quit()