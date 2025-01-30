# Funktio saa parametrin eli alkuarvon.
# Funktio tekee laskutoimituksia ja palauttaa
# kutsujalle arvon.
# Huom: kutsujan eli pääohjelman täytyy ottaa funktion
# palauttama arvo talteen.
import math

def nelio(luku):
    tulos = luku ** 2
    # tulos = math.pow(luku, 2)
    # funktio palauttaa laskemansa arvon
    return tulos

# pääohjelma näkee vain vain omat muuttujansa
arvo = float( input("Anna luku: ") )

# kutsutaan funktiota, muista ottaa
# funktion palauttama arvo talteen!
vastaus = nelio(arvo)

print(f"Lukusi neliö on: {vastaus:.2f}")