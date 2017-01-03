from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException

class SignUp_SignIn(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_SignUp_SignIn_menu_option_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("/html/body/header/nav[2]/a[6]"))

    def test_SignUp_SignIn_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("/html/body/header/nav[2]/a[6]")
        self.assertEqual(element.text,"SIGN UP  /  SIGN IN")


    def test_SignUp_SignIn_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("/html/body/header/nav[2]/a[6]")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()