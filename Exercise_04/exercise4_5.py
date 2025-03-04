# Ohjelman alkuosa, annetaan special_price:lle alkuarvo,
# voi aloittaa myös arvosta True, jos haluat toimia käänteisellä logiikalla:
special_price = False

# Ohjelman pääosa:
# kysy tässä onko käyttäjä opiskelija vai ei, sekä kuukauden numero (input() jne.)
opiskelija = str(input("Oletko opiskelija? (k/e)\n"))
kuukausi = int(input("Mille kuukaudelle matka varataan? (1-12)\n"))

# Lisää tähän kohtaan kaikki tarvittavat ehtolauseet!
# Ehtolauseiden avulla (vrt. onko opiskelija, onko kesäaika),
# muuta special_price tarvittaessa arvoon True tai False,
# mikäli käyttäjä on tai ei ole kelvollinen alennettuun hintaan
if opiskelija == "k":
    if 6 <= kuukausi <= 8:
        special_price = False
    else:
        special_price = True
else:
    special_price = False

# Tulosta ohjelman lopussa special_price -muuttujan perusteella tieto siitä,
# onko käyttäjä oikeutettu alennukseen
if special_price:
    print("Alennus myönnetty!")
else:
    print("Normaali hinta.")
