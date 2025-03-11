# Teen ohjelma, joka tuottaa halutun mittaisia turvallisia salasanoja

import random
import string

special_chars = "-_~?*$#!+%@" # Erikoismerkki

# string.ascii_letters - sisältää kaikki latinalaiset kirjaimet (isot ja pienet kirjaimet)
# string.digits - sisältää kaikki numerot (0123456789)
all_chars = string.ascii_letters + string.digits + special_chars

# Pyydän käyttäjältä merkkimäärä, kuinka pitkän salasanan hän haluaa,
# mutta täyttää seuraavat ehdot:
# a) Salasanassa on vähintään yksi pieni kirjain
# b) Salasanassa on vähintään yksi iso kirjain
# c) Salasanassa on vähintään yksi numero
# d) Salasanassa on vähintään jokin seuraavista erikoismerkeistä: - _ ~ ? * $ # ! + % @

# Jotta 4 sääntöä vastaavat, salasanan pituuden on oltava vähintään 4 merkkiä,
# joten luon tarkistuksen
while True:
     try:
         pas_length = int(input("Anna salasanan pituus (yli 4 merkkiä): "))
         if pas_length < 4:
             print("Salasanan on oltava vähintään 4 merkkiä pitkä.")
         else:
             break
     except ValueError:
         print("Syötä vain numeroita.")

# Generoidaan salasana, joka täyttää kaikki ehdot - GPT-chat auttoi luomaan tämän osan ja ehdotti myös tuontimerkkijonoa
while True:
    password = "".join(random.choices(all_chars, k=pas_length))
    if (any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in special_chars for c in password)):
        break

print("Salasana:", password)