#!/usr/bin/env python

from selenium import webdriver
import unittest
from time import sleep

class GoogleCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.pl")
    def tearDown(self):
        self.driver.quit()
    def test_serch(self):
        sleep(3)
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
