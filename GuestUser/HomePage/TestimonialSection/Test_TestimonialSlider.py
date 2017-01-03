from selenium import webdriver
import unittest
import time

class TestimonialSlider(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_first_bullet_is_found(self):
        driver = self.driver
        first_element = driver.find_element_by_xpath("//*[@id='testimonials-slider']/div/div/div/a[1]/i")
        first_element.click()
        self.assertTrue(driver.find_element_by_xpath("//*[@id='testimonial-slide-0']/div[3]"))
        self.assertTrue(driver.find_element_by_xpath("//*[@id='testimonial-slide-0']/div[3]/div"))

    def test_second_bullet_is_found(self):
        driver = self.driver
        first_element = driver.find_element_by_xpath("//*[@id='testimonials-slider']/div/div/div/a[2]/i")
        first_element.click()
        self.assertTrue(driver.find_element_by_xpath("//*[@id='testimonial-slide-0']/div[3]"))
        self.assertTrue(driver.find_element_by_xpath("//*[@id='testimonial-slide-0']/div[3]/div"))

    def test_third_bullet_is_found(self):
        driver = self.driver
        first_element = driver.find_element_by_xpath("//*[@id='testimonials-slider']/div/div/div/a[3]/i")
        first_element.click()
        self.assertTrue(driver.find_element_by_xpath("//*[@id='testimonial-slide-0']/div[3]"))
        self.assertTrue(driver.find_element_by_xpath("//*[@id='testimonial-slide-0']/div[3]/div"))




    def tearDown(self):
        self.driver.quit()