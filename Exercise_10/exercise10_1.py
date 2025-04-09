import os

# Pieni lisätehtävä:
# Tee tiedostonkäsittelylle oma funktio, joka palauttaa tiedoston sisällön listana!
# Tulosta lopputulos ohjelmakoodin puolella yllä olevan esimerkkikuvan mukaisesti.

def file_artists(nimi):

    # katsotaan onko käsiteltävä tiedosto olemassa: os.path.isfile(nimi)
    # katsotaan onko meillä käyttöoikeus tähän tiedostoon: os.access(nimi, os.R_OK)
    # katsotaan ettei tiedosto ole tyhjä: os.path.getsize(nimi) > 0
    if os.path.isfile(nimi) and os.access(nimi, os.R_OK) and os.path.getsize(nimi) > 0:

        # kaikki ok, luetaan tiedoston sisältö ja tulostetaan!
        file = open(nimi, 'r')
        rivia = file.readlines()
        file.close()
        return rivia

rivit = file_artists("artists.txt")

print("Kaikkien aikojen myydyimpiä kotimaisia äänitteitä:\n")

# Tulos tiedostosta
for rivi in rivit:
    print("->", rivi.strip())
