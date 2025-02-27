# Pyydän syöttötietoja: annettu raha ja ostohinta
rahaa = int(input("Anna rahaa: \n"))
hinta = int(input("Ostosten hinta: \n"))

# Tarkistaa, onko rahaa tarpeeksi
if rahaa >= hinta:
    takaisin = rahaa - hinta
    print(f"Kiitos. Annetaan takaisin {takaisin} €")
# Rahat eivät riittäneetkään, käyttäjä lisää rahaa
else:
    lisaa_rahaa = int(input("Rahat eivät riitä, anna lisää rahaa: \n"))
    rahaa += lisaa_rahaa
    # Tapaus, jossa rahaa on nyt tarpeeksi
    if rahaa >= hinta:
        takaisin = rahaa - hinta
        print(f"Kiitos. Annetaan takaisin {takaisin} €")
    # Toinen tapaus, kun rahat eivät vielä riitä
    else:
        print("Sinulla ei ole tarpeeksi rahaa.")
