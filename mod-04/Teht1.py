"""
    Ohjelma tulostaa 3:lla jaolliset luvut
    väliltä 1 ... 1000.
    Käytetään while-toistoa.
"""

'''
    HUOM: koodaa tehtävä itse 'tyhjältä pöydältä',
    jos while-toisto on sinulle uusi asia.
'''

import math

# tämä muuttuja saa arvot 1, 2, 3, ... 1000
luku = 1

while luku <= 1000:
    # tulostetaan luku, jos se on jaollinen kolmella?
    if luku % 3 == 0:
        print(luku)

    # muista lisätä muuttujan 'luku' arvoa!
    luku += 1       # luku = luku + 1

print("Homma tehty!")


