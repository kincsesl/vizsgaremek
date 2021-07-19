from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:1667/#/")

def cookies(a):  # 1: nem fogad el, 2: elfogad cookie-t
    kuki = driver.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[" + str(a) + "]/div")
    if len(kuki) > 0:
        kuki[0].click()


cookies(2)

def ide_oda_kattint(): #Vizsgálja a Sign in és a Sign up linkek működését.
    navlinkek = driver.find_elements_by_class_name("nav-link")
    navlinkek[2].click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    navlinkek[1].click()
    time.sleep(2)
    driver.back()

ide_oda_kattint()

driver.close()
