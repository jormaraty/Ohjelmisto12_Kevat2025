class Hissi:
    def __init__(self, alin, ylin):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        # hissin täytyy tietää sen nykyinen kerros,
        # aluksi hissi on alimmassa kerroksessa
        self.nykyinen_kerros = self.alin_kerros
        # TAI: self.nykyinen_kerros = alin

    def siirry_kerrokseen(self, tavoitekerros):
        # Tämä vaatii insinöörin logiikkaa
        # - siirrytäänkä ylös- vai alaspäin?
        # - yritetäänkö mennä maan alle tai katosta läpi?
        print("älä hättäile, kohta toimii, ehkä...")

    def kerros_ylös(self):
        # lisätään ominaisuuden 'nykyinen_kerros' arvoa yhdellä
        self.nykyinen_kerros += 1
        print(f"olen kerroksessa {self.nykyinen_kerros}")


# pääohjelma
testiHissi = Hissi(1, 7)
print(f"hissi on {testiHissi.nykyinen_kerros}. kerroksessa")
# väliaikainen testi
testiHissi.kerros_ylös()
# lopullisessa testissä pääohjelma kutsuu siirry_kerrokseen -metodia.
testiHissi.siirry_kerrokseen(5)






