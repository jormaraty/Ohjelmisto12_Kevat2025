'''
Ohjelma kysyy käyttäjältä kokonaisluvun ja ilmoittaa
onko se alkuluku vai ei.
'''

# boolean-tyyppinen muuttuja, ilmoittaa onko luku
# alkuluku vai ei. Alkuarvona on True eli
# alkuoletus on että käyttäjältä saadaan alkuluku
onAlku = True

luku = int( input("Anna kokonaisluku: ") )

# logiikka: jaan käyttäjän antamaa lukua arvoilla
# 2, 3, 4, ... (luku-1).
# Jos käyttäjän antama luku on jaollinen yhdelläkin
# muuttujan jakaja arvolla, niin luku EI ole alkuluku.
for jakaja in range(2, luku):
    if luku % jakaja == 0:
        # jakolasku meni tasan -> luku ei ole alkuluku
        onAlku = False
        # nyt tiedetään jo lopputulos, for-toisto voidaan lopettaa heti.
        break

# ilmoitetaan lopputulos.
# boolean-tyyppisillä muuttujilla yhtäsuuruusvertailu voidaan lyhentää seuraavasti.
if (onAlku):
    # if (onAlku == True):    # yläpuolella on lyheempi versio tästä yhtäsuuruusvertailusta
    print("Lukusi ON alkuluku")
else:
    print("Lukusi EI ollut alkuluku")
