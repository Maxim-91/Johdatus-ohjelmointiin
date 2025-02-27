# Pyydetään 2 numeroa käyttäjältä
a = int(input("Anna ensimmäinen luku: \n"))
b = int(input("Anna toinen luku: \n"))

# Vertailen kahta numeroa ja käytän if-funktiota tuloksen tulostamiseen
if a > b:
    print(f"Suurempi luku = {a}")
elif a < b:
    print(f"Suurempi luku = {b}")
else:
    print("Numerot ovat yhtä suuria.")
