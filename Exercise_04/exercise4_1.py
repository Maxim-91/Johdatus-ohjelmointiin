from datetime import datetime

# Muuttujat
paiva = datetime.now().strftime("%d.%m.%Y")
nimi = "Maksym Kotlubaiev"
vuosi = 1991
saldo = 857.99

# Muuttujien yhdistäminen ja tuloksen tulostaminen
tiedot = f"{nimi} ({vuosi}), saldo: {saldo} €, päivitetty {paiva}."
print(tiedot)
