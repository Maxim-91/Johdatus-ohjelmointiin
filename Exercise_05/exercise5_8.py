# Pytän käyttäjältä sanan
sana = str(input("Anna sana:\n"))

# Pytän käyttäjältä salauksessa tarvittava siirtoluku
salaus = int(input("Anna salauksen siirtoluku:\n"))

# Suoritan annetulle sanalle ns. Caesarin salakirjoitus käyttämällä siirtolukua
salattu_teksti = ""
for i in sana:
    if i.isalpha(): # Tarkistan, koostuuko merkkijono vain kirjaimista (ei numeroita, välilyöntejä tai muita merkkejä)
        char = chr((ord(i) - ord('a') + salaus) % 26 + ord('a')) # Turvauduin GPT-chatin apuun
        salattu_teksti += char
    else:
        salattu_teksti += i

print("Salattu teksti:\n" + salattu_teksti)
