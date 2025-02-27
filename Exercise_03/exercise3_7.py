# Pyydä paketti/kirje ja paino käyttäjältä
tyyppi = int(input("Ilmoita lähetyksen tyyppi:\n1. Jos se on kirje, syötä 1\n2. Jos se on paketti, syötä 2\n"))
paino = int(input("Anna paino:\n"))

# Pitäisikö meidän maksaa 2 euroa
ei_mahdu = 0
k = 0
summa = 0

# Määritän summakertoimen
if paino < 200:
    k = 0
elif 200 <= paino < 500 and tyyppi == 1:
    k = 0.04
elif paino >= 500 and tyyppi == 1:
    k = 0.07
    # Kysyn käyttäjältä mahtuuko kirje postilaatikkoon
    mahtuuko = int(input("Mahtuuko kirje postilaatikkoon?:\n1. Jos kellä, syötä 1\n2. Jos ei, syötä 2\n"))
    if mahtuuko == 2:
        ei_mahdu = 2
elif 200 <= paino < 500 and tyyppi == 2:
    k = 0.08
elif paino >= 500 and tyyppi == 2:
    k = 0.14

if tyyppi  == 1:
    summa = 0.5 + (paino // 100 * k) + ei_mahdu
elif tyyppi  == 2:
    summa = 2 + (paino // 100 * k)

print(f"Lähetyshinta: {summa:.2f}€")
