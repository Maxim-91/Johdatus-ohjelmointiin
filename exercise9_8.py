# Valuuttamuunnin

import functions as f

print("Offline-pankki\n")
# Käytä näitä valuuttakursseja hyväksi muunnoksessa (voit myös hakea ajantasaiset kurssit internetistä):
#  1 € = 1.1 $ (dollari)
#  1 € = 0.9 £ (punta)
#  1 € = 11.8 kr (Ruotsin kruunu)

# Pyydä ensin käyttäjältä rahasumma sekä valuutan yksikkö
amount = float(input("Syötä rahasumma:\n"))
from_currency = input("Mistä valuutasta (euro, dollari, punta, ruotsin kruunu):\n")

# Kysy tämän jälkeen mihin valuuttaan hän haluaa muuntaa rahasumman
to_currency = input("Mihin valuuttaan (euro, dollari, punta, ruotsin kruunu):\n")

# Tulos
result = f.convert_money(amount, from_currency, to_currency)
print(f"Muunnettu summa: {result} {to_currency}\n\n")

#----------------------------------------------------------------------------------
# Lisätehtävä: Hae päivän valuuttakurssit jostain internet-rajapinnasta!
print("Verkkopankki (Lisätehtävä)\n")

# Valuuttakurssien saaminen
rates = f.fetch_exchange_rates()

# Tiedot käyttäjältä
amount = float(input("Syötä rahasumma:\n"))
from_currency = input("Mistä valuutasta (esim. USD, GBP, SEK):\n").upper()
to_currency = input("Mihin valuuttaan (esim. USD, GBP, SEK):\n'").upper()

# Tulos
result = f.convert_money_verkko(amount, from_currency, to_currency, rates)
print(f"Muunnettu summa: {result} {to_currency}")
