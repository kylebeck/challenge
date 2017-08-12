import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ComparisonAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/kylebeck/Desktop/challenge/chromedriver')
        self.base_url = "http://localhost:5000/form"        


    def test_comparison_form_without_criteria(self):
        driver = self.driver
        driver.get(self.base_url)
        string2 = driver.find_element_by_name('string2')
        string2.send_keys(Keys.RETURN)
        assert "This field is required" in driver.page_source


    def test_comparison_results(self):
        driver = self.driver
        driver.get(self.base_url)
        string1 = driver.find_element_by_name('string1')
        string1.send_keys("selenium")
        string2 = driver.find_element_by_name('string2')
        string2.send_keys("unobtanium")
        string2.send_keys(Keys.RETURN)
        assert "Comparison Results" in driver.page_source


    def tearDown(self):
        self.driver.close()
