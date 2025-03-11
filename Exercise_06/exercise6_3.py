# Teen ohjelma, jonka avulla voidaan laskea tilastoa luokan oppilaiden koetuloksista
import statistics
import math

# Kysytään oppilaiden lukumäärä
number = int(input("Opiskelijoiden lukumäärä:\n"))

# Kysytään kunkin oppilaan koearvosana (silmukassa)
arvosanat = []
for i in range(number):
    arvosana = int(input(f"Anna opiskelijan arvosana:\n"))
    # Lisätehtävä: Tallenna arvosanat listaan,
    # ja hyödynnä sitä keskiarvon laskemisessa
    # ja sanallisen arvion tulostamisessa
    arvosanat.append(arvosana)

# Lasketaan keskiarvo arvosanoista ja tulostetaan se näytölle

keskiarvo = math.floor(sum(arvosanat) / number)
print(f"Keskiarvo: {keskiarvo}")

# Lisäksi tulostetaan näytölle keskimääräisestä arvosanasta sanallinen arvio silmukan jälkeen:
# 0 <= keskiarvo < 1 Huono tulos
# 1 <= keskiarvo < 2 Heikko tulos
# 2 <= keskiarvo < 3 Tyydyttävä tulos
# 3 <= keskiarvo < 4 Hyvä tulos
# 4 <= keskiarvo <= 5 Kiitettävä tulos
sana_keskiarvo = ["Huono tulos", "Heikko tulos", "Tyydyttävä tulos", "Hyvä tulos", "Kiitettävä tulos", "Kiitettävä tulos"]
print(f"{sana_keskiarvo[keskiarvo]}\n")

# Toinen lisätehtävä: Laske myös arvojen mediaani
mediaani = statistics.median(arvosanat)
print(f"Mediaani: {mediaani}")

# Kolmas lisätehtävä: Laske myös yleisin arvosana, eli moodi
moodi = statistics.mode(arvosanat)
print(f"Moodi: {moodi}")
