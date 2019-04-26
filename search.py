#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://benchmark.pl')

    def test_search_page(self):
        driver = self.driver
        zgoda = driver.find_element_by_xpath('//*[@id="cookies-info"]/div/div[2]/button')
        zgoda.click()
        wyszukaj = driver.find_element_by_name('q')
        wyszukaj.clear()
        wyszukaj.send_keys('RTX 2070')
        wyszukaj.send_keys(Keys.RETURN)
        assert 'Brak wyników.' not in driver.page_source

        pole = driver.find_element_by_xpath('//*[@id="body"]/table[1]/tbody/tr/td[1]/span')
        self.assertTrue(pole.is_displayed)

        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
