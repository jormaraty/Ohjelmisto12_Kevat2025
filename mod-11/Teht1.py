'''
Mistä luokasta aloitetaan?
Kirja sekä lehti ovat molemmat julkaisuja.
Joten aloitetaan Julkaisu-luokasta.
'''

# määritellään luokka Julkaisu, josta tulee nk. yliluokka
class Julkaisu():
    # jokaisella julkaisulla on 1 yhteinen ominaisuus: nimi
    def __init__(self, nimi):
        self.nimi = nimi


# määritellään aliluokka Kirja, joka periytyy Julkaisu-luokasta.
class Kirja(Julkaisu):
    # Kirja-luokalla on yliluokan ominaisuuden lisäksi 2 lisäominaisuutta
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        # kututaan yliluokan alustajaa, joka asettaa nimi-ominaisuuden arvon.
        super().__init__(nimi)
        # asetetaan kirjalle sen 2 lisäominaisuutta
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    # määritellään luokalle uusi toiminto eli metodi, joka tulostaa luokan kaikki ominaisuudet
    def tulosta_tiedot(self):
        print("\n-- Kirjan tiedot --")          # \n on rivinvaihto
        print(f"Nimi: {self.nimi}")             # aliluokalla on kaikki yliluokan ominaisuudet
        print(f"Kirjailija: {self.kirjoittaja}")
        print(f"Sivuja: {self.sivumäärä}")


# määritellään luokka Lehti, joka perityy Julkaisu-luokasta
class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print("\n-- Lehden tiedot --")
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.päätoimittaja}")


# - pääohjelma alkaa -
# luodaan uusi Lehti-tyyppinen olio, sillä on 2 ominaisuutta
ekaLehti = Lehti("Aku Ankka", "Aki Hyyppä")
# luodaan uusi Kirja-tyyppinen olio, sillä on 3 ominaisuutta
ekaKirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

# tulostetaan kummankin olion kaikki tiedot,
# hyödynnetään niille määriteltyä tulosta_tiedot -metodia
ekaLehti.tulosta_tiedot()
ekaKirja.tulosta_tiedot()

