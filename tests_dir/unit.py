#!/usr/bin/env python

from selenium import webdriver
import unittest
import time

# tworze klase WSBPl check dziedziczona po klasie testcase z modulu unittest
class WsbPlCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.wsb.pl")
    def tearDown(self):
        self.driver.quit()
    def test_page_title(self):
        self.assertIn("Bankowe", self.driver.title)
    def test_Bydgoszcz(self):
        link = self.driver.find_element_by_link_text('Kontakt')
        link.click()
        time.sleep(3)
        link2 = self.driver.find_element_by_partial_link_text('Byd')
        link2.click()
        time.sleep(3)




if __name__ == '__main__':
    unittest.main(verbosity=2)
