# Luodaan Auto-luokka,
# tätä luokkaa kehitetään seuraavissa tehtävissä.

class Auto:
    # määritellään luokan konstruktori eli alustaja.
    # Luokalla on 4 ominaisuutta.
    # Alustaja pyytää nyt käyttäjältä vain 2 ominaisuuden arvot (rekkari, huippunopeus),
    # ja asettaa saamansa arvot luotavalle oliolle.
    # Viimeiset 2 ominaisuutta (nopeus, matka) alustaja asettaa aina nollaksi.

    def __init__(self, rekisteritunnus, maxnopeus):
        self.rekisteritunnus = rekisteritunnus
        # Parametrin nimi (maxnopeus) ei tarvitse olla sama kuin luokan ominaisuus (huippunopeus).
        self.huippunopeus = maxnopeus
        # alustaja asettaa nyt nopeuden ja matkan aina nollaksi.
        self.nopeus = 0
        self.matka = 0


# pääohjelma, joka hyödyntää Auto-luokkaa

# luodaan uusi Auto-tyyppinen olio. Olion nimi on nyt ekaAuto.
ekaAuto = Auto("ABC-123", 142 )

# tulostetaan olion kaikki ominaisuudet, tekniikalla olionNimi.ominaisuus
print("Auto-tyyppisen olion kaikki ominaisuudet")
print(f"rekkari: {ekaAuto.rekisteritunnus}")
print(f"huippunopeus: {ekaAuto.huippunopeus}")
print(f"tämän hetkinen nopeus: {ekaAuto.nopeus}")
print(f"auton kulkema matka: {ekaAuto.matka}")
