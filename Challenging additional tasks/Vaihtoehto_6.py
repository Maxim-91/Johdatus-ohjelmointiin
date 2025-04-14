# Vaihtoehto 6: Henkilötunnustarkistin

# Tee ohjelma, joka kysyy henkilön nimen ja henkilötunnuksen.
# Tarkista ohjelmassa, että henkilötunnus on oikeassa muodossa.
# Selvitä lisäksi henkilötunnuksesta Python-koodilla henkilön ikä.
# Jos henkilön ikä on 17-64 vuotta, tulosta: ”Oikeus työttömyysetuuteen!”.
# Muussa tapauksessa tulosta ”Ei oikeutta työttömyysetuuteen.”

from datetime import datetime

# Funktio tarkistaa henkilötunnuksen muodon ja palauttaa True/False
def check_format(hetu):
    # Hetun täytyy olla muodossa ppkkvv-xxxx (11 merkkiä)
    # Jos esim. 131052-308T
    if len(hetu) != 11:
        return False
    if hetu[6] not in ['-', 'A', '+']: # Jos esim. 131052-308T: hetu[6] = "-"
        return False
    if not (hetu[:6] + hetu[7:10]).isdigit(): # Jos esim. 131052-308T: hetu[:6] + hetu[7:10] = "131052" + "308" = "131052308"
        return False
    return True

# Funktio laskee iän henkilötunnuksesta
def calculate_age(hetu):
    day = int(hetu[0:2])
    month = int(hetu[2:4])
    year = int(hetu[4:6])
    sign = hetu[6]

    if sign == '+':
        year += 1800
    elif sign == '-':
        year += 1900
    elif sign == 'A':
        year += 2000
    else:
        return None  # virheellinen merkki

    try:
        birthdate = datetime(year, month, day)
    except ValueError:
        return None  # virheellinen päivämäärä

    today = datetime.today()

    # Lasketaan ikä vähentämällä syntymävuosi nykyvuodesta.
    # Jos tämän vuoden syntymäpäivä ei ole vielä ollut, vähennetään yksi.
    # Vertailu palauttaa True (=1) tai False (=0), joten saadaan oikea ikä.
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Pääkoodi
name = input("Anna nimesi:\n")
hetu = input("Anna henkilötunnuksesi (esim. 131052-308T):\n")

if check_format(hetu):
    age = calculate_age(hetu)
    if age is None:
        print("Virheellinen syntymäaika henkilötunnuksessa.")
    else:
        print(f"{name}, ikä: {age} vuotta.")
        if 17 <= age <= 64:
            print("Oikeus työttömyysetuuteen!")
        else:
            print("Ei oikeutta työttömyysetuuteen.")
else:
    print("Henkilötunnus ei ole oikeassa muodossa.")
