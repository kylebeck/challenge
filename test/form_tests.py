#!/usr/bin/python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ComparisonAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost:5000"


    def test_front_page_link(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text('Continue').click()
        assert "String Comparison Form" in driver.page_source


    def test_string1_without_criteria(self):
        driver = self.driver
        driver.get(self.base_url + "/form")
        string2 = driver.find_element_by_name('string2')
        string2.send_keys("unobtanium")
        driver.find_element_by_xpath("//input[@class='submit_button']").click()
        assert "This field is required" in driver.page_source


    def test_string2_without_criteria(self):
        driver = self.driver
        driver.get(self.base_url + "/form")
        string1 = driver.find_element_by_name('string1')
        string1.send_keys("selenium")
        driver.find_element_by_xpath("//input[@class='submit_button']").click()
        assert "This field is required" in driver.page_source


    def test_levenshtein_results(self):
        driver = self.driver
        driver.get(self.base_url + "/form")
        string1 = driver.find_element_by_name('string1')
        string1.send_keys("selenium")
        string2 = driver.find_element_by_name('string2')
        string2.send_keys("unobtanium")
        driver.find_element_by_xpath("//select[@id='metric']/option[text()='Levenshtein Distance']").click()
        driver.find_element_by_xpath("//input[@class='submit_button']").click()
        assert "The Levenshtein Distance between 'selenium' and 'unobtanium' is 6." in driver.page_source


    def test_jaccard_results(self):
        driver = self.driver
        driver.get(self.base_url + "/form")
        string1 = driver.find_element_by_name('string1')
        string1.send_keys("selenium")
        string2 = driver.find_element_by_name('string2')
        string2.send_keys("unobtanium")
        driver.find_element_by_xpath("//select[@id='metric']/option[text()='Jaccard Distance']").click()
        driver.find_element_by_xpath("//input[@class='submit_button']").click()
        assert "The Jaccard Distance between 'selenium' and 'unobtanium' is 0.636363636364." in driver.page_source


    def test_sorensen_results(self):
        driver = self.driver
        driver.get(self.base_url + "/form")
        string1 = driver.find_element_by_name('string1')
        string1.send_keys("selenium")
        string2 = driver.find_element_by_name('string2')
        string2.send_keys("unobtanium")
        driver.find_element_by_xpath("//select[@id='metric']/option[text()='Sorensen Distance']").click()
        driver.find_element_by_xpath("//input[@class='submit_button']").click()
        assert "The Sorensen Distance between 'selenium' and 'unobtanium' is 0.466666666667." in driver.page_source


    def test_return(self):
        driver = self.driver
        driver.get(self.base_url + "/form")
        string1 = driver.find_element_by_name('string1')
        string1.send_keys("selenium")
        string2 = driver.find_element_by_name('string2')
        string2.send_keys("unobtanium")
        driver.find_element_by_xpath("//select[@id='metric']/option[text()='Levenshtein Distance']").click()
        driver.find_element_by_xpath("//input[@class='submit_button']").click()
        driver.find_element_by_link_text('Perform Another Comparison').click()
        assert "String Comparison Form" in driver.page_source


    def test_results_error(self):
        driver = self.driver
        driver.get(self.base_url + "/results")
        assert "Start Over" in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
