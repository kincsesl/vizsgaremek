from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:1667/#/register")

driver.close()
