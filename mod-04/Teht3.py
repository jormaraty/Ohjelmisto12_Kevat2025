"""
Kysytään käyttäjältä lukuja, kunnes käyttäjä antaa
tyhjän merkkijonon.
Lopuksi tulostetaan käyttäjän antamista luvuista
suurin ja pienin arvo.
"""
import math

# Annetaan alkuarvor suurimmalle ja pienimmälle arvolle.
pienin = math.inf       # mahdollisimman iso luku
suurin = -math.inf

# Ahaa, luvut on pakko lukea sisään tekstinä,
# jotta havaitaan lopetusmerkki "".
luku_str = input("Anna eka luku, tyhjä lopettaa: ")

# while-toisto loppuu vain tyhjällä merkkijonolla
while luku_str != "":
    # muunnetaan luettu merkkijono numeroksi
    luku = float(luku_str)

    # jos käyttäjä antoi vielä pienemmän arvon, kuin muuttujan 'pienin' nykyinen arvo on, niin
    if luku < pienin:
        # sijoitetaan muuttujan 'pienin' uudeksi arvoksi käyttäjän antama arvo
        pienin = luku

    # vastaavasti, jos käyttäjä antoi isomman luvun kuin muuttujan 'suurin' arvo
    if luku > suurin:
        suurin = luku

    # HUOM: muista kysyä käyttäjältä uusi arvo!!!
    luku_str = input("Anna seuraava luku, tyhjä lopettaa: ")

# tulostetaan suurin ja pienin saaduista luvuista
print(f"Suurin antamasi luku oli: {suurin}")
print(f"Pienin antamasi luku oli: {pienin}")
