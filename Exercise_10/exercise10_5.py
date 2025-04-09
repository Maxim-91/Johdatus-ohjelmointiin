import os
import json
from datetime import datetime

# Teen kysytyistä tiedoista dictionary, ja tallenna se JSON-muodossa tiedostoon (esim. maintenance.json) ennen ohjelman päättymistä.
# Kun käynnistät ohjelman uudestaan, ja jos tiedosto on entuudestaan olemassa,
# näytä sen sisältö ennen kuin annat käyttäjälle mahdollisuuden kirjoittaa uudet tiedot sen tilalle.
filename = "maintenance.json"
data = []

# katsotaan onko käsiteltävä tiedosto olemassa: os.path.isfile(filename)
# katsotaan onko meillä käyttöoikeus tähän tiedostoon: os.access(filename, os.R_OK)
# katsotaan ettei tiedosto ole tyhjä: os.path.getsize(filename) > 0
if os.path.isfile(filename) and os.access(filename, os.R_OK) and os.path.getsize(filename) > 0:

    # kaikki ok, luetaan tiedoston sisältö ja tulostetaan!
    with open(filename, 'r') as file:
        try:
            data = json.load(file)
            if data:

                # Näytetään viimeisin huoltokirjaus
                last_entry = data[-1]
                print("Viimeisin kirjaus...")
                print(f"Pvm: {last_entry['date']}")
                print(f"Hlö: {last_entry['name']}")
                print(f"Tilannekoodi: {last_entry['status_code']}")
                print(f"Viesti: {last_entry['description']}")

        except json.JSONDecodeError:
            data = []

# Teen huoltokirjausohjelma, joka kysyy seuraavat tiedot käyttäjältä:
#  Kirjaajan nimi
#  Tilannekoodi
#  Selite

# Kysy käyttäjältä tiedot
nimi = str(input("\nKirjaajan nimi:\n"))
tilannekoodi = input("Tilannekoodi:\n")
selite = input("Selite:\n")

huoltokirjaus = {
                    "name": nimi,
                    "status_code": tilannekoodi,
                    "description": selite,

                    # Lisää tietoihin myös automaattisesti tämän hetkinen päivämäärä
                    "date": datetime.now().strftime("%d.%m.%y")
                }
data.append(huoltokirjaus)

# Lisätehtävä:
# Tallenna kaikki tiedostoon lisätyt huoltokirjaukset (älä kirjoita vanhan yli), ja lisää aina vain perään uusi huoltokirjaus.
# Näytä ohjelman käynnistyessä aina viimeisin huoltokirjaus. JSON on tässä hyödyllinen tallennusmuoto (lista joka koostuu dictionaryistä).

with open(filename, 'w') as file:
    json.dump(data, file)
