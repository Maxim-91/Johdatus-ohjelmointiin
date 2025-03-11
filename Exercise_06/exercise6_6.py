# Teen uusi ohjelma, ja luo siihen lista nimeltä ”basket”.
# Lisään siihen seuraavat sisältö:
basket = ["omena",
          "banaani",
          "kirsikka",
          "porkkana",
          "peruna",
          "tomaatti",
          "kaali"]

# Kysyn käyttäjältä jokin sana
sana = str(input("Syötä sana:\n"))

# Tulosta basket-listan sisältö allekkain siten, että jätät tulostamatta käyttäjän antaman sanan
if sana in basket:
    for x in basket:
        if x == sana:
            continue
        print(x)
# Lisätehtävä: Jos käyttäjä syöttää sanan sijasta numeron,
# tulosta muutoin kaikki listan sisältö,
# mutta jätä tulostamatta annetulla järjestysnumerolla oleva sana listasta
elif sana.isnumeric() and 0 < int(sana) <= len(basket):
    for i, x in enumerate(basket):
        if i == int(sana) - 1:
            continue
        print(x)
# Jos valittua sanaa ei löydy listasta, ilmoita käyttäjälle
else:
    print("Sanaa ei löytynyt.")
