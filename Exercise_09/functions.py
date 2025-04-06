# Task №9.1
# Teen funktio nimeltä show_personal_info(), joka tulostaa henkilötiedot (nimi, kotipaikka, ammatti)
def show_personal_info(nimi, kotipaikka, ammatti):
    print(f"{nimi}")
    print(f"{kotipaikka}")
    print(f"{ammatti}")

#---------------------------------------------------------------------------------------------------------------

# Task №9.2
# Teen funktio count_seconds(hours, minutes, seconds),
# joka ottaa vastaan parametrit: tunnit, minuutit ja sekunnit.
# Funktion tulee palauttaa (eli return) vastauksena yksi kokonaisluku siitä,
# kuinka monta sekuntia annetut parametrit ovat yhteensä.

# Lisätehtävä: Hyväksy käyttäjän antama formaatti ajasta: “2h 45min 33sek”
def count_seconds(hours, minutes, seconds):
    if isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
        return hours * (60 * 60) + minutes * 60 + seconds
    elif isinstance(hours, str) and isinstance(minutes, str) and isinstance(seconds, str):
        hours = int(hours.replace("h", ""))
        minutes = int(minutes.replace("min", ""))
        seconds = int(seconds.replace("sek", ""))
        return hours * (60 * 60) + minutes * 60 + seconds
    else:
        return 0

#---------------------------------------------------------------------------------------------------------------

# Task №9.3
# Tee funktio nimeltä magazine_serial_check(serial)
# Pieni lisätehtävä: Palauta (return) funktiosta Boolean,
# joka ilmoittaa onko annettu ISSN-numero oikeassa muodossa (True/False).
# Tässä tapauksessa älä tulosta lopputulosta itse funktiossa, vaan vasta ohjelmakoodissa.
def magazine_serial_check(serial):
# Tarkistan pituuden ja viivojen olemassaolon.
    if len(serial) == 9 and serial[4] == '-':
        # Poistan viiva
        serial = serial.replace('-', '')
        # Tarkistan onko tämä numero
        if len(serial) == 8 and serial.isdigit():
            return True
    else:
        return False

#---------------------------------------------------------------------------------------------------------------

# Task №9.4
# Funktion tulee ensin tulostaa annettu otsikko,
# sekä sen jälkeen numeroitu lista osallistujista
def show_numbered_list(title, data):

    # Tulosta sisennyksen / tyhjän rivin
    print()

    # Tulosta otsikkotekstin
    print(title)

    # Tulosta listan tapahtuman osallistujien nimistä
    n = 1
    for i in data:
        print(f"{n}. {i}")
        n += 1

#---------------------------------------------------------------------------------------------------------------

# Task №9.5
# Tilavuuslaskuri
import math

# 1. laatikon tilavuus -> tee uusi funktio: box_volume(width, height, depth)
    # • kaava = leveys * korkeus * syvyys
    # • palauta funktiossa laskutoimituksen tulos pyöristettynä kahteen desimaaliin (return). Älä tulosta funktiossa mitään.
def box_volume(width, height, depth):
    return round(width * height * depth, 2)

# 2. pallon tilavuus -> tee uusi funktio: ball_volume(radius)
    # • kaava = (4 * π * säde**3) / 3
    # • palauta funktiossa laskutoimituksen tulos pyöristettynä kahteen desimaaliin (return). Älä tulosta funktiossa mitään.
def ball_volume(radius):
    return round((4 * math.pi * radius**3) / 3, 2)

# 3. putken tilavuus -> tee uusi funktio: pipe_volume(radius, length)
    # • kaava = π * säde**22 * pituus
    # • palauta funktiossa laskutoimituksen tulos pyöristettynä kahteen desimaaliin (return). Älä tulosta funktiossa mitään.
def pipe_volume(radius, length):
    return round(math.pi * radius**2 * length, 2)

#---------------------------------------------------------------------------------------------------------------

# Lisätehtävä №9.6 Lottorivi
# Teen funktio, joka tuottaa satunnaisen lottorivin. Lottorivissä on 7 eri numeroa väliltä 1-40.
import random
def generate_lotto():
    return random.randint(1, 40)

#---------------------------------------------------------------------------------------------------------------

# Lisätehtävä №9.7 Aiemmat harjoitukset funktioiden avulla
# Valitse jokin seuraavista aiemmista harjoituksista, ja tee siitä sellainen versio,
# että ohjelman logiikka on sijoitettu joko yhteen tai useampaan funktioon.
# Voit tehdä myös monta aiempaa harjoitusta funktioilla, lisäpisteitä tulee maksimissaan 3:sta aiemmasta tehtävästä.
# Vaihtoehdot:

#  Viikkotehtävä 3 – 3
def palkkojen_laskeminen(tyotuntia, tuntipalkkaa):
    if tyotuntia > 40:
        ylituntia = tyotuntia - 40
        palkka = 40 * tuntipalkkaa + ylituntia * tuntipalkkaa * 1.5
        return palkka
    else:
        palkka = tyotuntia * tuntipalkkaa
        return palkka

#-----------------------------------------------------------------------------------
#  Viikkotehtävä 4 – 2

def kaannan_teksti(text1):
    # Käännän teksti
    text2 = text1[::-1]

    # Määritän, onko testi tehty vai ei
    if text1 == "":
        text3 = "Antamasi teksti on tyhjä."

    # Määritän, onko teksti palindromi
    elif text1 == text2:
        text3 = "Palindromi: KYLLÄ"
    else:
        text3 = "Palindromi: EI"

    return text2, text3

#-----------------------------------------------------------------------------------
#  Viikkotehtävä 6 – 2
def tulosta_kertotaulu(number):
    if 1 <= number <= 10:
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    else:
        print("Vääränlainen luku.")

#---------------------------------------------------------------------------------------------------------------

# Lisätehtävä №9.8 Valuuttamuunnin
# Tee funktio nimeltä "convert_money", joka ottaa vastaan muunnettavan summan, alkuperäisen valuutan sekä valuutan johon summa muutetaan.
# Hyväksyttävät valuutat ovat € (euro), $ (dollari), £ (punta) sekä kr (Ruotsin kruunu).
# Funktion tehtävä on muuntaa annettu rahasumma haluttuun valuuttaan valuuttakurssien mukaisesti.

def convert_money(amount, from_currency, to_currency):
# Käytä näitä valuuttakursseja hyväksi muunnoksessa (voit myös hakea ajantasaiset kurssit internetistä):
#  1 € = 1.1 $ (dollari)
#  1 € = 0.9 £ (punta)
#  1 € = 11.8 kr (Ruotsin kruunu)
    rates = {
        "euro": 1,
        "dollari": 1.1,
        "punta": 0.9,
        "ruotsin kruunu": 11.8
        }

    # Tarkistan, onko tällaisia valuuttoja listassa
    if from_currency not in rates or to_currency not in rates:
        return "Valuuttaa ei löydy."

    # Muunna ensin euroiksi ja sitten kohdevaluuttaan
    amount_in_euros = amount / rates[from_currency]
    converted_amount = amount_in_euros * rates[to_currency]
    return round(converted_amount, 2)


# Lisätehtävä: Hae päivän valuuttakurssit jostain internet-rajapinnasta!
import json
import urllib.request

# Käytin GPT-chat-apua saadakseni API-tuloksen
def fetch_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    req = urllib.request.Request(url)
    raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
    data = json.loads(raw_data)

    # Luon sanakirjan valuuttakurssien tallentamiseksi
    rates = {"EUR": 1.0}

    # Haetaan valuuttakurssit ja tallennetaan ne sanakirjaan
    for currency, rate in data['rates'].items():
        rates[currency] = rate

    return rates

# Kopioin toiminnon verkko-käyttäjäksi
def convert_money_verkko(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return "Valuuttaa ei löydy."

    amount_in_euros = amount / rates[from_currency]
    converted_amount = amount_in_euros * rates[to_currency]

    return round(converted_amount, 2)

#---------------------------------------------------------------------------------------------------------------

# Task №9.9 Rekursiot

import os

def list_files(path, level=0): # Olen luomassa funktiota "listdir":n käyttöä varten

    # Silmukka käy läpi kaikki määritetyn polun kansiot ja tiedostot
    for item in os.listdir(path):
        indent = "  " * level # Sisennyksen lisääminen (syvyystasojen luominen)
        if os.path.isdir(os.path.join(path, item)): # Jos tämä taso on kansio
            print(f"{indent}{item} …") # Teen tälle tasolle sopivan sisennyksen + nimi + kolme pistettä
            list_files(os.path.join(path, item), level + 1) # Siirryn seuraavalle tasolle käyttämällä samaa toimintoa
        else: # Jos tämä taso ei ole kansio
            print(f"{indent}- {item}") # Teen tälle tasolle sopivan sisennyksen + viiva + nimi

#---------------------------------------------------------------------------------------------------------------

# Task №9.10 Edistyneemmät funktiotekniikat
# Ulkoista toimintoa ei tarvinnut käyttää

#---------------------------------------------------------------------------------------------------------------

# Task №9.11 Monimutkainen tiedon järjestäminen (custom sort)

# Tee Python –ohjelma, jossa on funktio nimeltä city_company_sort(data), joka suodattaa listan siten,
# että tiedot laitetaan aakkosjärjestykseen ensin kaupungin, ja vasta sitten ostoskeskuksen nimen perusteella.
# Tämän voi ratkaista usealla eri tavalla!

def city_company_sort(data):
    return sorted(data, key=lambda x: (x['city'], x['company']))
