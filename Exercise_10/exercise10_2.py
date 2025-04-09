# Teen vieraskirjaohjelma
import os

# Kysyn ensin käyttäjältä, haluaako hän lukea vai kirjoittaa vieraskirjaan (l/k)
kysymys = str(input("Haluatko lukea vai kirjoittaa vieraskirjaan (l/k):\n"))

# Lisätehtävä:
# Käytä JSON-formaattia vieraskirjassa (guestbook.json).
# Tallenna tässä tapauksessa jokaisesta viestistä itse viesti sekä päivämäärä + kellonaika (datetime-moduuli).
import json
from datetime import datetime

filename = "guestbook.json"

# Jos hän haluaa lukea vieraskirjaa, haen tiedostosta rivit, ja tulostan ne näytölle käyttäen silmukkaa
if kysymys == "l":

    # katsotaan onko käsiteltävä tiedosto olemassa: os.path.isfile(filename)
    # katsotaan onko meillä käyttöoikeus tähän tiedostoon: os.access(filename, os.R_OK)
    # katsotaan ettei tiedosto ole tyhjä: os.path.getsize(filename) > 0
    if os.path.isfile(filename) and os.access(filename, os.R_OK) and os.path.getsize(filename) > 0:

        # kaikki ok, luetaan tiedoston sisältö ja tulostetaan!
        with open(filename, 'r') as file:
            entries = json.load(file)
            for entry in entries:
                print(f"{entry['timestamp']}: {entry['message']}")

# Jos käyttäjä haluaa kirjoittaa vieraskirjaan, tallenna rivi tiedoston loppuun
elif kysymys == 'k':

        # Uuden viestin
        message = input("Kirjoita uusi viesti:\n")
        entry = {
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        entries = []

        # Ensin lataan vanhat tiedot lisäämällä uuden viestin
        # katsotaan onko käsiteltävä tiedosto olemassa: os.path.isfile(filename)
        # katsotaan onko meillä käyttöoikeus tähän tiedostoon: os.access(filename, os.R_OK)
        # katsotaan ettei tiedosto ole tyhjä: os.path.getsize(filename) > 0
        if os.path.isfile(filename) and os.access(filename, os.R_OK) and os.path.getsize(filename) > 0:
            with open(filename, 'r') as file:
                entries = json.load(file)
        entries.append(entry)

        # Sitten kirjoitan tiedoston päälle
        with open(filename, 'w') as file:
            json.dump(entries, file)
