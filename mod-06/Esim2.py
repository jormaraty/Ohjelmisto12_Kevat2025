# Funktio, joka saa alkuarvon eli parametrin.
# Funktio ei palauta mitään.
def tuplaus(luku):
    print(f"Sain alkuarvoksi luvun {luku}")
    tulos = 2 * luku
    print(f"Alkuarvo eli parametrin arvo "
          f"tuplana {tulos} ")

print("Pääohjelma alkaa")
# kutsutaan funktiota
tuplaus(3)

print("Ollaan takaisin pääohjelmassa")
