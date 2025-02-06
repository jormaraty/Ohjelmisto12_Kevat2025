'''
    Tässä on vähän alkua tehtävään 1, ei hae kaikkia tietoja.
    Testattu 6.12, että toimii PyCarm:lla seuraavalla konfiguraatiolla:
    - python interpreter: 3.13
    - mysql-connector-python: 9.2.0 (uusin)
'''

'''
Suositellaan että mikään sovellus ei käytä tietokannan (root) tunnuksia.
Tosi vaarallista, jos pääkäyttäjän tunnukset leviävät ilkeille tahoille.
Tätä varten tietokantaan on luotu tunnus 'peruskäyttäjä', jolla on vain
oikeudet vain komentoja select, insert ja update.
'''

# Havaittiin, että PyCharm saattaa jotenkin seota, jos alla olevan import lauseen kopioi.
# Kirjoita alla oleva komento käsin, niin sitten pitäisi toimia?!?
import mysql.connector

def hae_kentan_tiedot(icao):
    sql = f"SELECT name FROM airport where ident='{icao}'"
    print(sql)
    # kursorin avulla kommunikoidaan tietokannan kanssa
    kursori = yhteys.cursor()
    # suoritetaan sql-lause kursorin avulla
    kursori.execute(sql)
    # haetaan kursorilta kaikki tulosrivit
    tulos = kursori.fetchall()
    # saatiinko tulosrivejä?
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on: {rivi[0]}")
    else:
        print("ICAO-koodillasi ei löytynyt lentoasemaa.")
    return


# pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',           # tai 'localhost'. Viittaa sinun omaan koneeseen.
    port= 3306,
    database='flight_game',     # tähän sinun tietokannan nimi
    user='perususer',           # vaihda tähän sinun oma käyttäjätunnus
    password='salainen',        # käyttäjän oikea salasana
    autocommit=True
    )

icao_koodi = input("Anna kentän ICAO-koodi: ")
hae_kentan_tiedot(icao_koodi)

