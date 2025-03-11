# Teen ohjelma, joka pyytää käyttäjältä vuosiluvun (2017 – 2020)
# ja laskee Oulun alueen terveyspalveluiden keskimääräisen jonotusajan kyseiseltä vuodelta.
#
# Data löytyy seuraavasta osoitteesta:
# https://api.ouka.fi/v1/chc_waiting_times_monthly_stats?order=year.desc,month.desc

import json
import urllib.request


url = "https://api.ouka.fi/v1/chc_waiting_times_monthly_stats?order=year.desc,month.desc"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
odottaa = json.loads(raw_data)

# Pyydän käyttäjältä vuosiluvun (2017 – 2020)
vuosi = int(input("Syötä vuosi (2017 - 2020): "))

# Luon muuttujan laskelmien tallentamista varten
keski = 0
keskiarvo = 0
keskinumero = 0
yleinen_keskiarvo = 0

# Lasken keskiarvon tehtävän suorittamiseksi
for i in odottaa:
    if (i["time"] is not None and i["year"] == vuosi) and i["doctor_queue"] is not None and i["nurse_queue"] is not None:
            keski = (float(i["doctor_queue"]) + float(i["nurse_queue"])) / 2
            keskiarvo += keski
            keskinumero += 1

# Tarkistetaan jakoa 0:lla
if keskinumero != 0:
    yleinen_keskiarvo = keskiarvo / keskinumero

# Tulos
print(f"Oulun alueen terveyspalveluiden keskimääräisen jonotusajan kyseiseltä {vuosi}: {yleinen_keskiarvo:.0f} päivää.")
