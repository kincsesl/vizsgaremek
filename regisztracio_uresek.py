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

navlinkek = driver.find_elements_by_class_name("nav-link")  # Home, Sign in és Sign up
navlinkek[2].click() #Sign up
submit = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/button")
username = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/fieldset[1]/input")
emil = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/fieldset[2]/input")
password = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/fieldset[3]/input")


def hibaellenőrzés(listaelem):
    username.send_keys(listaelem[0])
    emil.send_keys(listaelem[1])
    password.send_keys(listaelem[2])
    submit.click()
    time.sleep(2)
    új_ablak = driver.find_element_by_class_name("swal-modal")
    főszöveg = új_ablak.find_element_by_xpath("//div[@class = 'swal-title']")
    alszöveg = új_ablak.find_element_by_class_name("swal-text")
    okégomb = driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div/button")
    time.sleep(2)
    if főszöveg.text == listaelem[3] and alszöveg.text == listaelem[4]:
        okégomb.click()
        print(listaelem[4], "Oké.")
    else:
        print(listaelem[4], "Nem oké")


cookies(2)

tesztlista = [["", "", "", "Registration failed!", "Username field required."],
              ["abc", "", "", "Registration failed!", "Email field required."],
              ["abc", "abc@abc.hu", "", "Registration failed!", "Password field required."]]

for teszt in tesztlista:
    hibaellenőrzés(teszt)

time.sleep(2)

driver.close()