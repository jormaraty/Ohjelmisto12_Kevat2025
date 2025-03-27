'''
Näytetään käytäjälle satunnainen Chuck Norris vitsi.
Rajapinnan määrittely löytyy osoitteesta: https://api.chucknorris.io/
'''

# asenna tarvittaessa tämä paketti Python-kehittimeesi
import requests

# tämä rajapinta ei vaadi mitään hakuehtoja,
# nyt ohjelma odottaa tässä vain käyttäjältä käynnistyslupaa.
kaynnistys = input("Paina Enter, niin saat Chuck Norris vitsin ")

# Haetaan json-data palvelun api-rajapinnan ohjeiden mukaan
# datan hakulause
pyyntö = "https://api.chucknorris.io/jokes/random"

# Varaudutaan mahdollisiin virheisiin try-except rakenteella.
# Virheherkkä koodi laitetaan try-osan sisään.
# Jos ei tapahdu virheitä try-osion koodissa -> except-osiota ei suoriteta ollenkaan.
# Jos try-osiossa tulee virhetilanne:
#    - try-osion suoritus lopetetaan heti ja siirrytään except-osioon
#    - try-osion koodiin ei enää palata
try:
    # lähetetään pyyntö nettiin ja otetaan saatu data talteen 'vastaus' -olioon.
    vastaus = requests.get(pyyntö)

    # testataan oliko vastauksen status koodi OK (=200)
    if vastaus.status_code == 200:
        # muutetaan saatu data ns. json-dataksi,
        # joka muistuttaa Pythonin sanakirja-tietorakennetta.
        json_vastaus = vastaus.json()

        print("Tässä vitsisi, ole hyvä! \n")     # \n tekee rivinvaihdon
        # 'json_vastaus' sisältää kaiken netistä saadun datan.
        # tulostetaan nyt vain sen 'value' avaimen arvo
        print(json_vastaus["value"])

except requests.exceptions.RequestException as e:
    # tähän tullaan, jos tapahtui request-paketin havaitsema virhe
    print ("Hakua ei voitu suorittaa.")
except Exception as ex:
    # tänne tullaan kaikissa muissa virhetilanteissa
    print("Tapahtui odottamaton virhe")

print("\nToivottavasti pidit vitsistä!")
