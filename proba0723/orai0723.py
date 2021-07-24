from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    options = Options()
    # options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/todo.html")
    input_1_xpath = '//*@id = "ipt1"]'
    def ipt1_empty_by_default_test():
        #Az ipt1 mező nem lehet üres.
        driver.find_element_by_xpath("input_1_xpath").text == ""
    def ipt1_fill_with_text():
        #Az ipt1 mező nem lehet üres.
        testing_string = "dslfkjpoierj"
        ipt1_element = driver.find_element_by_xpath("input_1_xpath")
except:
    pass
finally:
    driver.close()