import random


def veletlen(s, keveri):  # pl. (0[1-15],a[2],A[1-5],&[3], True)
    szamjegy = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    kisangol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    nagyangol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    kisbetu = ["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "o", "ó", "ö", "ő",
               "p", "q", "r", "s", "t", "u", "ú", "ü", "ű", "v", "w", "x", "y", "z"]
    nagybetu = ["A", "Á", "B", "C", "D", "E", "É", "F", "G", "H", "I", "Í", "J", "K", "L", "M", "N", "O", "Ó", "Ö", "Ő",
                "P", "Q", "R", "S", "T", "U", "Ú", "Ü", "Ű", "V", "W", "X", "Y", "Z"]
    szimbolum = ["-", "_", "+", "*", "/", "!", "?", "&", "#", ">", "<", "%", "="]
    lista = s.split(",")

    def ellenoriz(s):
        def szame(x):
            log = True
            for i in range(len(x)):
                log = log and x[i] in szamjegy
            return log

        log = True
        for elem in lista:
            log = log and elem[0] in {"0", "a", "A", "&", "á", "Á"}
            log = log and elem[1] == "[" and elem[len(elem) - 1] == "]"
            if log:
                alelem = elem[elem.find("[") + 1:elem.find("]")]
                # log = log and alelem.find("[") == -1 and alelem.find("]") == 0
                kotojel = alelem.find("-")
                if kotojel > 0:
                    egyik = alelem[alelem.find("[") + 1:kotojel]
                    masik = alelem[kotojel + 1:elem.find("]")]
                    log = log and szame(egyik)
                    log = log and szame(masik)
                    if log:
                        log = log and int(egyik) < int(masik)
                else:
                    log = log and szame(alelem)

        return log

    def szetszed(a):
        reszek = []
        reszek.append(a[0])
        kotojel = a.find("-")
        if kotojel > -1:
            egyik = a[a.find("[") + 1:kotojel]
            masik = a[kotojel + 1:a.find("]")]
            reszek.append(egyik)
            reszek.append(masik)
        else:
            for i in range(2):
                reszek.append(a[a.find("[") + 1:len(a) - 1])
        return reszek

    def general(a, b, c):
        hany = len(a)
        b = int(b)
        c = int(c)
        x = random.randint(b, c)
        fuzer = ""
        for i in range(0, x):
            fuzer += a[random.randint(0, hany - 1)]
        return fuzer

    def kever(a):
        lista = list(a)
        b = ""
        while len(b) < len(a) - 1:
            betu = str(lista[random.randint(1, len(lista) - 1)])
            b += betu
            lista.remove(betu)
        return b

    if ellenoriz(s):
        kimegy = ""
        for elem in lista:
            darabok = szetszed(elem)
            if darabok[0] == "0":
                kimegy += general(szamjegy, darabok[1], darabok[2])
            elif darabok[0] == "a":
                kimegy += general(kisangol, darabok[1], darabok[2])
            elif darabok[0] == "A":
                kimegy += general(nagyangol, darabok[1], darabok[2])
            elif darabok[0] == "á":
                kimegy += general(kisbetu, darabok[1], darabok[2])
            elif darabok[0] == "Á":
                kimegy += general(nagybetu, darabok[1], darabok[2])
            elif darabok[0] == "&":
                kimegy += general(szimbolum, darabok[1], darabok[2])
        if keveri:
            kimegy = kever(kimegy)
        return kimegy
    else:
        return ("Nem jók a bemenő adatok.")


def emil():
    return veletlen("a[1]", False) + veletlen("a[1-6],0[0-3]", True) + "@" + veletlen("a[4-10],0[0-3]",
                                                                                      False) + "." + veletlen("a[2-3]",
                                                                                                              False)


def nev():
    return veletlen("Á[1],á[1-10]", False)


def name():
    return veletlen("A[1],a[1-10]", False)


def passw():
    return veletlen("A[1-4],a[1-10],0[3],&[1-4]", True)


def jelszo():
    return veletlen("Á[1-4],á[1-10],0[3],&[1-4]", True)
