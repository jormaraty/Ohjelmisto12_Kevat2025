# Luodaan Auto-luokka,
# tätä luokkaa kehitetään seuraavissa tehtävissä.

class Auto:
    # määritellään luokan konstruktori eli alustaja.
    # Luokalla on 4 ominaisuutta.
    # Tämä alustaja asettaa luotavan olion ominaisuuksien arvoksi nyt
    # vain 2 ensimmäistä parametreina saamaansa arvoa (rekkari, huippunopeus).
    # Viimeiset 2 ominaisuutta (nopeus, matka) saavat arvoksi 0.
    # def __init__(self, rekisteritunnus, maxnopeus, nopeus = 0, matka = 0):
    def __init__(self, rekisteritunnus, maxnopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = maxnopeus
        # alustaja asettaa nyt nopeuden ja matkan aina nollaksi.
        self.nopeus = 0
        self.matka = 0


# pääohjelma, joka hyödyntää Auto-luokkaa

# luodaan uusi Auto-tyyppinen olio. Olion nimi on ekaAuto.
ekaAuto = Auto("ABC-123", 142 )

# tulostetaan olion kaikki ominaisuudet
print("Auto-tyyppisen olion kaikki ominaisuudet")
print(f"rekkari: {ekaAuto.rekisteritunnus}")
print(f"huippunopeus: {ekaAuto.huippunopeus}")
print(f"tämän hetkinen nopeus: {ekaAuto.nopeus}")
print(f"auton kulkema matka: {ekaAuto.matka}")
