import time
import locators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Sign_upLap():
    def __init__(self):
        self.options = Options()
        # self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(locators.signuplap)
        self.username = self.driver.find_element_by_xpath(locators.username)
        self.emil = self.driver.find_element_by_xpath(locators.emil)
        self.password = self.driver.find_element_by_xpath(locators.password)
        self.submit = self.driver.find_element_by_xpath(locators.submit)  # Sign up felirat.

    def hibaablak(self):
        self.felirat = self.driver.find_element_by_xpath(locators.failed)
        self.reszlet = self.driver.find_element_by_xpath(locators.reszlet)
        self.failed_okgomb = self.driver.find_element_by_xpath(locators.failed_okgomb)
        #self.userhiba = locators.userhiba  # 4 elemű lista.

    def sikerablak(self):
        self.welcome = self.driver.find_element_by_xpath(locators.welcome)
        self.successful = self.driver.find_element_by_xpath(locators.successful)
        self.successful_okgomb = self.driver.find_element_by_xpath(locators.successful_okgomb)

    def test_01_rossz_mezok(self, a, b, c, d):
        if a == "":
            self.submit.click()
        elif b == "":
            self.username.send_keys(a)
            self.submit.click()
        elif c == "":
            self.username.send_keys(a)
            self.emil.send_keys(b)
            self.submit.click()
        else:
            self.username.send_keys(a)
            self.emil.send_keys(b)
            self.password.send_keys(c)
            self.submit.click()
        time.sleep(1)
        self.hibaablak()
        log = self.reszlet.text == d
        self.failed_okgomb
        self.driver.close()
        #return self.reszlet.text ==
        return log
