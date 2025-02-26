# Pyydä tietoja käyttäjältä (km)
matkan_pituus = float(input("Anna matkan pituus:\n"))

# Käyttäjän polttoaineen kulutus laskenta
polttoaineenkulutus = 6.5
km = 100
kulutus = matkan_pituus / km * polttoaineenkulutus

# 1 desimaalin tarkkuudella
kulutus = round(kulutus, 1)

# Tulos
print(f"Kulutus: {kulutus} l")