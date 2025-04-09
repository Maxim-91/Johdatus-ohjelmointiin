# Lataa Moodlesta tiedosto nimeltä ”countries.json”, ja lisää se samaan kansioon jossa Python-tiedostosi ovat.
# Lataa tiedosto Pythonilla omaan muuttujaansa, ja tulosta listan sisältö allekkain alla olevan esimerkin mukaisesti.

import os
import json

filename = "countries.json"

# katsotaan onko käsiteltävä tiedosto olemassa: os.path.isfile(filename)
# katsotaan onko meillä käyttöoikeus tähän tiedostoon: os.access(filename, os.R_OK)
# katsotaan ettei tiedosto ole tyhjä: os.path.getsize(filename) > 0
if os.path.isfile(filename) and os.access(filename, os.R_OK) and os.path.getsize(filename) > 0:

    # kaikki ok, luetaan tiedoston sisältö ja tulostetaan!
    with open(filename, 'r') as file:
        countries_list = json.load(file)

# Tulos
for country in countries_list:
    print(f"{country['country']}: {country['capital']}")

# Lisätehtävä:
# Kysy käyttäjältä listan tulostamisen jälkeen kirjain A-Z, ja tulosta vain sillä kirjaimella alkavien maiden tiedot.
kirjain = str(input("\nMinkä alkukirjaimen maat ja pääkaupungit tulostetaan?\n")).upper()

# Tulos
for country in countries_list:
    if country['country'].startswith(kirjain):
        print(f"{country['country']}: {country['capital']}")
