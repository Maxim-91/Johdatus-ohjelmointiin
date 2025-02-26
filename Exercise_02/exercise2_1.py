import math

# Käyttäjä syöttää särmiön sivujen pituudet
a = float(input("Anna särmiön ensimmäisen sivun pituus:\n"))
b = float(input("Anna särmiön toisen sivun pituus:\n"))
c = float(input("Anna särmiön kolmannen sivun pituus:\n"))

# Kuvion tilavuuden laskeminen kaavalla V = a * b * c
v = a * b * c
v = round(v, 2)
print(f"Särmiön tilavuus: {v} m3\n") # Tulos

# Pallon säteen pyyntö käyttäjältä
r = float(input("Anna pallon säde:\n"))

# Pallon laskelmat kaavan avulla
pi = math.pi
v_pallon = 4 / 3 * pi * r ** 3
v_pallon = round(v_pallon, 2)

print(f"Pallon tilavuus: {v_pallon} m3\n") # Tulos