import randomstring
import locators
import classok

lap = classok.Sign_upLap()
"""
print(lap.test_01_rossz_mezok("", "", "", locators.userhiba[0]))
lap = classok.Sign_upLap()
print(lap.test_01_rossz_mezok(randomstring.nev(), "", "", locators.userhiba[1]))
lap = classok.Sign_upLap()
print(lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", locators.userhiba[2]))
lap = classok.Sign_upLap()
print(lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", locators.userhiba[2]))
"""
print(lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), randomstring.name(), locators.userhiba[3]))


