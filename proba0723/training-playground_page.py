import locators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    options = Options()
    # options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/todo.html")
    driver.find_element_by_xpath
    def get_imput_1():
        pass
finally:
    driver.close()