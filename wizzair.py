#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time

# Scenariusz:
# Rejestracja nowego uytkownika na stronie https://wizzair.com/pl-pl#/
#
# Przypadki testowe:
# 1. Rejestracja nowego uytkownika uywajc niepoprawnego adresu e-mail
#
# Kroki:
# 1. Wejdz na strone https://wizzair.com/pl-pl#/
# 2. Kliknij w prawym glownym rogu ZALOGUJ SIe
# 3. Kliknij REJESTRACJA
# 4. Wpisz imie
# 5. Wpisz nazwisko
# 6. Wybierz p
# 7. Wpisz numer telefonu komrkowego
# 8. Wpisz bdny adres e-mail (brak symbolu '@)
# 9. Wpisz haso
# 10. Wybierz narodowo
# 11. Zaznacz "Akceptuj Informacj o polityce prywatnoci"
# 12. Kliknij ZAREJESTRUJ SI
#
# Oczekiwany rezultat:
# Uytkownik otrzymuje informacj, e wprowadzony adres e-mail jest niepoprawny

class WizzairRegistration(unittest.TestCase):
    """
    Klasa będzie zawierała Scenariusz Testowy
    Rejestracja na stronie WizzairRegistration
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.wizzair.com/pl-pl#/")
    def tearDown(self):
        self.driver.quit()

#metody rozpoczynające się od słowa testowe
#są to przypadki testowe

    def test_wrong_email(self):
        """
        przypadek testowy: Rejestracja przy użyciu
        błednego adresu test_wrong_email
        """
        driver = self.driver
        zaloguj_btn = driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button')
        zaloguj_btn.click()
        rejestracja = driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')
        rejestracja.click()
        imie = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-1"]/label[1]/div[1]/input')
        imie.send_keys('Jan')
        nazwisko = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-1"]/label[2]/div[1]/input')
        #xpath napisany: //input[@placeholder='Nazwisko']
        nazwisko.send_keys('Nowak')
        imie.click()
        płeć = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-2"]/div[1]/label[2]/span')
        płeć.click()
        #wymuszenie przyciśnięcia pola
        #driver.execute_script('arguments[0].click()', płeć)
        telefon = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-3"]/input')
        telefon.send_keys('12345678')
        email = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[1]/label/input')
        email.send_keys('adadada-gmail.com')
        hasło = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-5"]/div[1]/label/input')
        hasło.send_keys('QWERTYuiop12345')
        narodowość = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-6"]/div[1]/label/input')
        narodowość.send_keys('Polska')
        pole_1 = driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[9]/span/label[2]')
        pole_1.click()
        self.assertFalse(pole_1.is_selected())
        pole_2 = driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[10]/span/label[1]')
        pole_2.click()
        self.assertFalse(pole_2.is_selected())

        '''nie konieczne do tego testu'''
        #zarejestruj = driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[11]/button')
        #zarejestruj.click()

        '''To jest dopiero właściwy test'''
        zbadaj = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span/span')
        self.assertTrue(zbadaj.is_displayed())
        self.assertEqual('Nieprawidłowy adres e-mail', zbadaj.text)

        time.sleep(10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
