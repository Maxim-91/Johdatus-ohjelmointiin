# Pyydä tietoja käyttäjältä (min)
minuutit = int(input("Anna minuutit:\n"))

# Lasketaan kokonaisia tunteja ja jäljellä olevia minuutteja
tunnin = 60
tunteja = minuutit // tunnin
minuutteja = minuutit % tunnin

# Tulos
print(f"{tunteja}h {minuutteja}min")