from colorama import Back, Style
import random

# Teen ohjelma, jossa käyttäjän pitää arvata tietokoneen arpoma numero väliltä 1-20

# Satunnainen kokonaisluku väliltä 1 ja 20
num = random.randint(1, 20)

# Ohjelma pyytää uutta arvausta niin kauan kunnes käyttäjä arvaa alkuperäisen numeron oikein.
while True:
    number = int(input(Style.RESET_ALL + "Arvaa numero (1-20):\n"))

    # Tarkistan, onko syötetty numero välillä 1-20
    if number < 1 or number > 20:
        print(Style.RESET_ALL + "Virhe! Syötä luku väliltä 1-20.\n")

    # Jos arvaus osuu oikeaan, tulostetaan viesti ”ONNEKSI OLKOON!” vihreällä taustavärillä
    elif number == num:
        print(Back.GREEN + "ONNEKSI OLKOON!")
        break

    # Jos numero on suurempi, tulosta viesti ”Liian korkea” punaisella taustavärillä
    elif number > num:
        print(Back.RED + "Liian korkea")

    # Jos arvaus on pienempi kuin oikea numero, tulosta viesti ”Liian matala” sinisellä taustavärillä
    elif number < num:
        print(Back.BLUE + "Liian matala")
        