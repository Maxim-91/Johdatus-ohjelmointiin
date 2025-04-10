# Teen ohjelma, joka hakee tiedostosta yrityksen tuotteiden nimet

import os
import json

# Lisähaaste 1
# Toiminto nimen, kategorian tai hinnan muokkaamiseen
def muokkaa_tuotetta(products, kentta):
    try:
        choice_number = int(input(f"Anna tuoten numero, jonka {kentta} haluat muokata (0 = Lopeta):\n"))
        if choice_number == 0:
            return False  # Lopeta
        index = choice_number - 1
        if 0 <= index < len(products):
            uusi_arvo = input(f"Syötä uuden tuotteen {kentta}:\n")
            if kentta == "hinta":
                try:
                    uusi_arvo = float(uusi_arvo)
                    uusi_arvo = round(uusi_arvo, 2)
                except ValueError:
                    print("Virheellinen hinta. Syötä numeerinen arvo.")
                    return True
            products[index][kentta] = uusi_arvo
        else:
            print("Virheellinen numero.")
    except ValueError:
        print("Virheellinen tieto, anna numero.")
    return True

# Lisähaaste 2
# Näytä tuotteet valitun kategorian mukaan
def nayta_kategoriat(products):
    kategoriat = sorted(set([product["kategoria"] for product in products])) # sorted - lajittelee aakkosjärjestykseen, set - poistaa kaksoiskappaleet

    print("Saatavilla olevat kategoriat:")
    for i, kategoria in enumerate(kategoriat):
        print(f"{i + 1}. {kategoria}")
    print("0 = Takaisin päävalikkoon")

    try:
        valinta_kat = int(input("Valitse kategoria (numero):\n"))
        if valinta == 0:
            return
        if 1 <= valinta_kat <= len(kategoriat):
            valittu_kategoria = kategoriat[valinta_kat - 1]

            print(f"Tuotteet kategoriassa '{valittu_kategoria}':")

            for i, product in enumerate(products):
                if product["kategoria"] == valittu_kategoria:
                    print(f"{i + 1}. {product['nimi']} - {float(product['hinta']):.2f} €")
        else:
            print("Virheellinen valinta.")
    except ValueError:
        print("Syötä numero.")

def nayta_kaikki_tuotteet(products):
    # Näytä tuotteista numeroitu lista käyttäjälle,
    # ja anna käyttäjälle mahdollisuus valita tuote rivinumerolla, jonka nimeä hän haluaa muokata
    print("Tuotelista:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product['nimi']} (Kategoria: {product['kategoria']}, Hinta: {float(product['hinta']):.2f} €)")




filename = "products.json"

products = []

# Ladataan tuotteet tiedostosta, jos olemassa
if os.path.isfile(filename) and os.access(filename, os.R_OK) and os.path.getsize(filename) > 0:
    with open(filename, 'r') as file:
        products = json.load(file)
else:
    # Voit päättää itse mitä tuotteita kyseinen kuvitteellinen yritys myy
    # Lisähaaste 1:
    # Muuta listaa niin, että se sisältää dictionaryjä eri tuotteista. Yhdestä tuotteesta tulee olla seuraavat tiedot: nimi, kategoria, hinta
    products = [
                {"nimi": "Kahvi", "kategoria": "Juoma", "hinta": 2.50},
                {"nimi": "Tee", "kategoria": "Juoma", "hinta": 2.00},
                {"nimi": "Maito", "kategoria": "Juoma", "hinta": 1.00},
                {"nimi": "Mehu", "kategoria": "Juoma", "hinta": 3.00},
                {"nimi": "Virvoitusjuoma", "kategoria": "Juoma", "hinta": 2.80},
                {"nimi": "Pizza", "kategoria": "Ruoka", "hinta": 5.99},
                {"nimi": "Maksalaatikko", "kategoria": "Ruoka", "hinta": 3.59},
                {"nimi": "Tuoretta Salaattia 100g", "kategoria": "Bistro", "hinta": 2.89}
               ]

# Pääsilmukka
while True:
    print("Valikko:")
    print("1. Näytä kaikki tuotteet") # Päätehtävä
    print("2. Selaa tuotteita kategorian mukaan") # Lisähaaste 2
    print("3. Muokkaa tuotetta") # Päätehtävä + Lisähaaste 1
    print("4. Lisää uusi tuote")  # Lisähaaste 3
    print("5. Poista tuote")  # Lisähaaste 3
    print("0 = Lopeta")
    valinta = int(input("Valitse toiminto (0-3):\n"))

    if valinta == 0:
        break

    elif valinta == 1:
        nayta_kaikki_tuotteet(products)

    # Lisähaaste 2:
    # Luokittele edellisen lisähaasteen tiedot niin, että käyttäjä voi selata yhden kategorian tuotteita aina kerrallaan
    elif valinta == 2:
        nayta_kategoriat(products)

    # Lisähaaste 1:
    # Anna käyttäjälle mahdollisuus muokata minkä tahansa tuotteen mitä tahansa tietoa
    elif valinta == 3:
        print("Mitä haluat muokata?")
        print("1. Nimi")
        print("2. Kategoria")
        print("3. Hinta")
        print("0 = Lopeta")
        field_choice = int(input("Valitse kenttä (0–3):\n"))

        if field_choice == 0:
            break
        elif field_choice == 1:
            kentta = "nimi"
            if not muokkaa_tuotetta(products, kentta):
                break
        elif field_choice == 2:
            kentta = "kategoria"
            if not muokkaa_tuotetta(products, kentta):
                break
        elif field_choice == 3:
            kentta = "hinta"
            if not muokkaa_tuotetta(products, kentta):
                break
        else:
            print("Virheellinen kentän valinta. Hyväksyttäviä numeroita ovat 1, 2 tai 3 ja 0 = Lopettaa")

    # Lisähaaste 3:
    # Anna käyttäjälle mahdollisuus myös lisätä uusia
    # ja poistaa vanhoja tuotteita.
    elif valinta == 4:
        # Uuden tuotteen lisääminen
        uuden_tuotteen_nimi = input("Anna tuotteen nimi:\n")
        uuden_tuotteen_kategoria = input("Anna tuotteen kategoria:\n")
        try:
            uuden_tuotteen_hinta = float(input("Anna tuotteen hinta:\n"))
            uuden_tuotteen_hinta = round(uuden_tuotteen_hinta, 2)
            uusi_tuote = {"nimi": uuden_tuotteen_nimi, "kategoria": uuden_tuotteen_kategoria, "hinta": uuden_tuotteen_hinta}
            products.append(uusi_tuote)
        except ValueError:
            print("Virheellinen hinta. Syötä numeerinen arvo.")

    elif valinta == 5:
        nayta_kaikki_tuotteet(products)

        # Tuotteen poistaminen
        try:
            poistettava = int(input("Anna poistettavan tuotteen numero (0 = Peruuta):\n"))
            if poistettava == 0:
                continue
            elif 1 <= poistettava <= len(products):
                poistettu = products.pop(poistettava - 1) # .pop(index) - palauttaa poistetun elementin
            else:
                print("Virheellinen numero.")
        except ValueError:
            print("Syötä numero.")

    else:
        print("Virheellinen toiminnon valinta. Hyväksyttäviä numeroita ovat 1, 2 tai 3 ja 0 = Lopettaa")

# Kun käyttäjä lopettaa ohjelman käytön, tallenna muutettu lista vanhan tiedoston päälle
with open(filename, 'w') as file:
    json.dump(products, file)
