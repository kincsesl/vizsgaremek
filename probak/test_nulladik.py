from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import randomstring


def test_proba():
    assert True

def test_proba1():
    assert True

def test_proba2():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/todo.html")

    class Todooldal:
        def __init__(self):
            self.beolvasás()

        def beolvasás(self):
            self.tartalmazó_konténer = driver.find_element_by_xpath("/html/body/div/div/div")
            self.teendőlista_ul = self.tartalmazó_konténer.find_element_by_xpath("//ul[@class = 'unstyled']")
            # A todok listája, egyelőre nem használom.
            self.teendőlista = self.teendőlista_ul.find_elements_by_xpath("//li[@class = 'ng-scope']")
            # A meglevő todok, elsőre 5
            self.a_teendők_száma = self.tartalmazó_konténer.find_element_by_xpath("//span['@class = ng-binding']")
            self.archive_link = self.tartalmazó_konténer.find_element_by_xpath("/html/body/div/div/div/a")
            self.új_todószöveg = self.tartalmazó_konténer.find_element_by_xpath("/html/body/div/div/div/form/input[1]")
            self.addgomb = self.tartalmazó_konténer.find_element_by_xpath("/html/body/div/div/div/form/input[2]")

        def teardown(self):  # Lerombolás.
            self.driver.close()

        def mennyi(self):
            self.a = self.a_teendők_száma.text.find(" ")  # Megkeresi az első szóközt az x of y... mezőben
            s = ""
            for i in range(self.a):
                s += self.a_teendők_száma.text[i]
            return s  # A mező elejéről kiírja a sztringet (x) a szóközig.

        def összes(self):
            a = self.a_teendők_száma.text.find("of ")  # Megkeresi az of szócskát az x of y... mezőben.
            b = self.a_teendők_száma.text.find(" ", a + 3)  # Innen továbbkeres a következő szóközig.
            s = ""
            for i in range(a + 3, b):
                s += self.a_teendők_száma.text[i]
            return s  # visszaadja y-t.

        def rákatt(self, x):
            self.teendőlista[x].find_element_by_tag_name("input").click()
            # time.sleep(2)

        def listát_frissít(self):
            self.archive_link.click()
            # Újra feltérképezi az oldalt.
            self.beolvasás()

        def új_todo(self, szöveg):
            self.új_todószöveg.send_keys(szöveg)
            self.addgomb.click()
            self.beolvasás()

    oldal = Todooldal()

    oldal.rákatt(2)
    oldal.rákatt(0)
    oldal.rákatt(2)
    oldal.listát_frissít()
    oldal.új_todo("Új feladat.")
    oldal.új_todo("Még egy.")
    oldal.új_todo("Meg egy harmadik.")

    számlista = []  # Véletlenszámlista lesz.
    for i in range(100):
        a = randomstring.randint(0, len(oldal.teendőlista) - 1)  # Véletlenszám 0-utolsó között, erre az elelmre kattintok.
        számlista.append(a)
        oldal.rákatt(a)  # Rákattint az a-adik listaelemre.

    print(számlista)

    kipipálatlan = 0  # Egyelőre nincs ilyen.
    for i in range(len(oldal.teendőlista)):
        if számlista.count(i) % 2 == 0:  # Ha páros sokszor kattintottam, akkor pipás, tehát nő a pipások száma.
            kipipálatlan += 1
    # A kipipáltban megkap
    # Kiírja, az X of Y mezőből az értékeket + a kipipáltan maradtak számát.
    print(oldal.mennyi(), "/", oldal.összes(), ":", kipipálatlan)

    if int(oldal.mennyi()) == kipipálatlan:  # Ha stimmel, akkor "minden oké".
        print("Minden oké.")
    else:
        print("Valami nem oké.")
    driver.close()
