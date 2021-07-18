from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:1667/#/login")


def cookies():
    kuki = driver.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[2]/div")
    if len(kuki) > 0:
        kuki[0].click()


time.sleep(2)
cookies()
time.sleep(2)
driver.close()
