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


cookies(2)  # Engedélyezi.

navlinkek = driver.find_elements_by_class_name("nav-link")  # Home, Sign in és Sign up
navlinkek[2].click()  # A Sign up oldalra lép

submit = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/button")
username = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/fieldset[1]/input")
emil = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/fieldset[2]/input")
password = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/fieldset[3]/input")


def ellenőrzi(név, email, jelszó):
    username.send_keys(név)
    emil.send_keys(email)
    password.send_keys(jelszó)
    submit.click()
    time.sleep(5)
    welcome = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]")
    success = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]")
    okégomb = driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div/button")
    if welcome.text == "Welcome!" and success.text == "Your registration was successful!":
        okégomb.click()
        s = név + "-" + email + "-" + jelszó + ": oké."
# Logout, ha van
        driver.back()
        navlinkek = driver.find_elements_by_class_name("nav-link")  # Home, Sign in és Sign up
        navlinkek[2].click()  # A Sign up oldalra lép
    else:
        s = név + "-" + email + "-" + jelszó + ": nem oké."
    return s


ellenőrzőlista = []

with open("adatok.csv", "r") as csvfájl:
    for sor in csvfájl:
        sor = sor[:-1:]
        ellenőrzőlista.append(sor.split(";"))

for listaelem in ellenőrzőlista:
    print(ellenőrzi(listaelem[0], listaelem[1], listaelem[2]))
    time.sleep(2)

driver.close()
