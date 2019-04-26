#!/usr/bin/python

from selenium import webdriver
import time

#sterownik do Chrome
driver = webdriver.Chrome()

#maksymalizuj okno
driver.maximize_window()

#przejdz do strony www.wsb.pl
driver.get("http://www.wsb.pl")
print(driver.title)
assert "Bankowe" in driver.title
#poczekaj 5 sekund
time.sleep(5)
driver.quit()
