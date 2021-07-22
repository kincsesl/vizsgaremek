from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestProba(object):
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("http://localhost:9999/editable-table.html")

    def teardown(self):
        self.driver.close()
    def test_eset(self):
        for i in range(2):  # Két új sort veszünk fel.
            self.driver.find_element_by_xpath("/html/body/div/div/div[2]/button").click()

        def táblátki():  # Kiírja a tábla akt. állapotát.
            global sorsz, oszlopsz
            táblázat = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/table")
            sorok = táblázat.find_elements_by_tag_name("tr")
            sorsz = 0
            oszlopsz = 0
            for sor in sorok:
                cellák = sor.find_elements_by_tag_name("td")
                oszlopsz = 0
                for cella in cellák:
                    # print("sor:", sorsz, "oszlop:", oszlopsz, "érték:", cella.find_element_by_tag_name("input").get_attribute("value"))
                    oszlopsz += 1
                sorsz += 1

        def két_utolsót_ellenőriz(lista):
            igaze = True
            for i in range(sorsz - 2, sorsz):
                sorlista = []
                for j in range(1, oszlopsz):
                    xp = "/html/body/div/div/div[2]/table/tbody/tr[" + str(i) + "]/td[" + str(j) + "]/input"
                    sorlista.append(self.driver.find_element_by_xpath(xp).get_attribute("value"))
                igaze = sorlista == lista[i - sorsz + 2]
                print(sorlista, lista[i - sorsz + 2])
            return igaze

        # Tesztadatok:
        lista = [["Fűnyíró", "11.99", "2", "Hobbi"], ["Tampon", "1.99", "112", "Hobbi"]]  # Hozzáadandók
        szótár = {"name": "", "price": "", "quantity": "", "category": ""}

        # Tesztadatok felvétele a cuccokba.
        cuccok = []
        for i in range(len(lista)):
            m = 0
            for j in szótár.keys():
                szótár[j] = lista[i][m]
                m += 1
            cuccok.append(szótár)
            szótár = {"name": "", "price": "", "quantity": "", "category": ""}

        táblátki()

    # xpath_minta: /html/body/div/div/div[2]/table/tbody/tr[7]/td[1]/input

        for i in range(7, 9):
            for j in range(1, oszlopsz):
                xp = "/html/body/div/div/div[2]/table/tbody/tr[" + str(i) + "]/td[" + str(j) + "]/input"
                self.driver.find_element_by_xpath(xp).clear()
                self.driver.find_element_by_xpath(xp).send_keys(lista[i - 7][j - 1])

        táblátki()

        print(két_utolsót_ellenőriz(lista))