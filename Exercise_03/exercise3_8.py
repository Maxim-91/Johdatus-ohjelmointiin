# Pyydän käyttäjältä ostosten kokonaissumman euroina
ostosumma = float(input("Anna ostosten kokonaissumman euroina:\n"))

# Onko asiakas opiskelija (K / E)
is_opiskelija = str(input("Oletko opiskelija (K / E)?:\n")) == "K"

# Onko asiakas kanta-asiakas (K / E)
is_kanta_asiakas = str(input("Oletko kanta-asiakas (K / E)?:\n")) == "K"

# Kysytään kuinka paljon kanta-asiakaspisteitä asiakkaalla on entuudestaan
if is_kanta_asiakas:
    pisteita = int(input("Syötä kanta-asiakaspistein määrä:\n"))

# Kysyn alennuskoodit
alennuskoodit = str(input("Syötä alennuskoodit, jos sinulla on:\n"))

# Alennuskoodi: FALL24 ja BK2SCHOOL
if alennuskoodit == "FALL24":
    ostosumma *= 0.90
elif alennuskoodit == "BK2SCHOOL" and is_opiskelija:
    ostosumma *= 0.8

# 100 asiakaspistettä per tilauksen jokaista alkavaa 10€
if is_kanta_asiakas:
    lisaa_pisteita = ostosumma // 10 * 100
    pisteita += lisaa_pisteita
# -5€ jokaista täyttä 1000:tta kanta-asiakaspistettä
    ostosumma -= pisteita // 1000 * 5

# postimaksut, jos kokonaissumma tässä vaiheessa ylittää 99€, postimaksu on 0€
if ostosumma <= 99:
    ostosumma += 7.95

print(f"Tilauksen loppusumma = {ostosumma:.2f} €")
