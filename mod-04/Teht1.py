"""
    Ohjelma tulostaa 3:lla jaolliset luvut
    väliltä 1 ... 1000.
    Käytetään while-toistoa.
"""
import math

'''
    HUOM: koodaa tehtävä itse 'tyhjältä pöydältä',
    jos while-toisto on sinulle uusi asia.
'''

luku = 1

while luku <= 1000:
    # onko luku jaollinen kolmella?
    if luku % 3 == 0:
        print(luku)
    luku += 1       # luku = luku + 1

print("Homma tehty!")


