# Vaihtoehto 1: Roomalaiset numerot
# Tee ohjelma, jolla voidaan muuntaa arabialaiset kokonaislukuesitykset roomalaisiksi ja päinvastoin.
# Ohjelmassa käyttäjä voi valita kumman muunnoksen hän haluaa suorittaa.
# Ohjelman tulee tarkistaa, että syötetty luku (arabialainen tai roomalainen) on oikeaoppisesti kirjoitettu.
# Tällöin esimerkiksi, jos käyttäjä antaa 4000 tai suuremman luvun, niin se jätetään muuntamatta ja palautetaan käyttäjälle virheilmoitus.

# Словарь для преобразования арабских чисел в римские
roman_numerals = [
    ("I", 1), ("IV", 4), ("V", 5), ("IX", 9),
    ("X", 10), ("XL", 40), ("L", 50), ("XC", 90),
    ("C", 100), ("CD", 400), ("D", 500), ("CM", 900),
    ("M", 1000)
]

# Suurin roomalaisilla numeroilla saatava luku = 3499=MMMCDXCIX
max_value = 3499

# Luon funktion numeroiden muuntamiseksi arabiasta roomalaiseksi
def arabic_to_roman(arabic_number):
    result = ""

    # Jos numero on välillä 1–3499
    if 1 <= arabic_number <= max_value:
        for i, value in reversed(roman_numerals):  # Käydään läpi käänteisessä järjestyksessä

            # Lisätään tarvittava määrä samoja roomalaisia merkkejä
            while arabic_number >= value:
                result += i
                arabic_number -= value

    # Jos luku on pienempi kuin 1 tai suurempi kuin 3499
    else:
        result = "Virhe: vain luvut välillä 1–3499 ovat sallittuja."

    # Palautetaan tulos
    return result

# Luon funktion numeroiden muuntamiseksi roomalaisista arabiaksi
def roman_to_arabic(roman_number):
    roman = roman_number.upper() # Teen kirjaimet isoilla
    index = 0 # Sijainti muuttujassa roman_number
    total = 0 # Arabialaisten numeroiden summa

    symbols = dict(roman_numerals[::-1])  # Käänteinen luettelo roman_numerals

    while index < len(roman):

        # Yritän ottaa kaksi symbolia merkityksen määrittämiseksi
        if roman[index:index+2] in symbols:
            total += symbols[roman[index:index+2]]
            index += 2

        # Jos symbolia 2 ei ole, valitsen yhden
        elif roman[index] in symbols:
            total += symbols[roman[index]]
            index += 1

        # Jos syötetty merkki ei ole luettelossa
        else:
            return "Virhe: virheellinen roomalainen numero!"

    # Muunnan arabian luvun tuloksen takaisin roomalaiseksi
    # ja vertaan sitä syötettyyn roomalaiseen numeroon muuntovirheen poistamiseksi.
    if arabic_to_roman(total) != roman:
        return "Virhe: virheellinen roomalainen numero!"

    return total

# Ohjelman koodi funktioiden avulla
print("1. Arabialainen -> Roomalainen")
print("2. Roomalainen -> Arabialainen")
choice = int(input("Valitse 1 tai 2:\n"))

if choice == 1:
    try:
        number = int(input("Anna arabialainen luku (1–3499):\n"))
        print("Roomalainen:", arabic_to_roman(number))
    except ValueError:
        print("Virhe: syötä kelvollinen kokonaisluku.")

elif choice == 2:
    roman = input("Anna roomalainen luku (esim. MMV):\n").strip().upper()
    result = roman_to_arabic(roman)
    print("Arabialainen:", result)

else:
    print("Virhe: virheellinen valinta.")
    