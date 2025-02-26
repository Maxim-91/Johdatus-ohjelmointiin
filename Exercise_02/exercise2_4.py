# Pyydä tietoja käyttäjältä (km)
matka_ajo = float(input("Matka ajon kilometrit:\n"))
kaupunki_ajo = float(input("Kaupunki ajon kilometrit:\n"))

# Käyttäjän polttoaineen kulutus laskenta
polttoaineenkulutus_matka = 5.1
polttoaineenkulutus_kaupunki = 7.5
km = 100

kulutus_matka = matka_ajo / km * polttoaineenkulutus_matka
kulutus_kaupunki = kaupunki_ajo / km * polttoaineenkulutus_kaupunki
kulutus = kulutus_matka + kulutus_kaupunki
kulutus = round(kulutus, 2)

# Tulos
print(f"Kulutus: {kulutus} l")