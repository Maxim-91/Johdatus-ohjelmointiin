# Teen ohjelma, joka antaa käyttäjälle satunnaisen mietelauseen!
import os
import random

# Moodlesta löytyviä mietelauseita ohjelmassasi (wisewords.txt).
filename = "wisewords.txt"

# katsotaan onko käsiteltävä tiedosto olemassa: os.path.isfile(filename)
# katsotaan onko meillä käyttöoikeus tähän tiedostoon: os.access(filename, os.R_OK)
# katsotaan ettei tiedosto ole tyhjä: os.path.getsize(filename) > 0
if os.path.isfile(filename) and os.access(filename, os.R_OK) and os.path.getsize(filename) > 0:
    with open(filename, 'r') as file:
        fortunes_list = file.readlines()

# Satunnainen indeksi
# Kaikkien mietelauseiden määrä tiedostossa on juuri tehdyn listan koko (mutta muista - 1,
# koska indeksit alkavat nollasta) esim. max_index = len(fortunes_list) - 1
max_index = len(fortunes_list) - 1
random_index = random.randint(0, max_index)

print("Päivän mielelause:")
print(fortunes_list[random_index])
