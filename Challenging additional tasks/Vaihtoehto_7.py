# Vaihtoehto 7: Internet-rajapintaa hyödyntävä sähkönkulutusohjelma (haastava)

# Kiitos GPT chatille avusta.

# Tee ohjelma, joka hakee kiinteistön kalenterivuoden sähkönkulutustiedot rajapinnasta,
# ja tulostaa tilaston siitä, minä päivämäärinä (top 5) kyseinen kiinteistö kuluttaa eniten sähköä.
#
# Lisätehtävänä voit tehdä myös arvion siitä mikä viikonpäivä (maanantai – sunnuntai) on
# kyseisessä kiinteistössä yleensä sähkönkulutukseltaan suurin.
#
# Pyydä käyttäjältä rakennuksen nimi ja sen jälkeen tarkasteltava vuosiluku. (esim. väliltä 2010 – 2020).
# Hae näiden tietojen pohjalta tarvittavat tiedot rajapinnasta, ja suorita tarvittavat laskutoimitukset.
#
# Lue tarvittavat sähkönkulutustiedot tästä rajapinnasta.
#
# https://helsinki-openapi.nuuka.cloud/swagger/index.html#/EnergyData/EnergyData_GetHourlyConsumption

import requests
import datetime
from collections import defaultdict

# Ensin haluan näyttää käyttäjälle luettelon rakennusten nimistä, jotka hän voi syöttää suorittaakseen tämän tehtävän.
#
# Törmäsin 1. ongelmaan: kaikissa luettelon rakennuksissa ei ole tietoja.
# Koska se en näyttänyt niitä käyttäjälle.
#
# Sitten 2. ongelma: luettelossa oli rakennuksia, joissa oli tietoja, mutta tietyiltä vuosilta ei ollut tietoja.
# Päätin jättää nämä rakennukset pois luettelosta.
#
# Sitten 3. ongelma: erittäin, hyvin pitkä aika listan käsittelyyn, koska täytyi käsitellä erittäin suuri joukko tietoja.
# Päätin näyttää luettelosta vain ensimmäiset 3 rakennusta, joilla on tietoja vuosilta 2010-2020.

# Saan koko listan rakennuksista
res = requests.get("https://helsinki-openapi.nuuka.cloud/api/v1.0/Property/List")
raw_data = res.json()

unique_names_set = set()
for building in raw_data:
    name = building.get("locationName")
    if name:
        unique_names_set.add(name)

full_buildings_list = list(unique_names_set)

# Toiminto tarkistaa tietojen saatavuus kaikilta vuosilta 2010-2020
def has_full_data(name):
    for year in range(2010, 2021):
        r = requests.get("https://helsinki-openapi.nuuka.cloud/api/v1.0/EnergyData/Daily/ListByProperty",
            params={
                "Record": "LocationName",
                "SearchString": name,
                "ReportingGroup": "Electricity",
                "StartTime": f"{year}-01-01",
                "EndTime": f"{year}-12-31"
            }
        )
        data = r.json()
        if r.status_code != 200 or not data or "errorNote" in data:
            return False
    return True

# Suodatan tiedot full_buildings_list ja jätän ne, joilla on tiedot vuosilta 2010-2020
buildings = []
for name in full_buildings_list:
    if has_full_data(name):
            buildings.append(name)
    # Suodattaminen vaatii monia pyyntöjä, mikä kestää kauan,
    # joten rajoitan suodattimen etsimään luettelosta 3 ensimmäistä sopivaa
    if len(buildings) == 3:
        break
print("Valid buildings (2010–2020):")
print("\n".join(buildings))

# ------------------------------------------------------------------------------------------------------

# Päätehtävän suorittaminen

name = input("\nValitse rakennus listasta:\n").strip()
year = int(input("Syota vuosi (väliltä 2010-2020):\n"))

url = "https://helsinki-openapi.nuuka.cloud/api/v1.0/EnergyData/Daily/ListByProperty"
response = requests.get(
    url,
    params={
            "Record": "LocationName",
            "SearchString": name,
            "ReportingGroup": "Electricity",
            "StartTime": f"{year}-01-01",
            "EndTime": f"{year}-12-31"
            })
data = response.json()

# Lista päivämäärä- ja kulutusparien tallentamiseen
days = []

# Sanakirja, jossa avain on viikonpäivä, arvo on kulutusluettelo
weekdays = defaultdict(list)

# Käydään läpi kaikki saadut tiedot, otetaan talteen päivämäärä ja sähkönkulutusarvo
# ja tallennetaan ne listaan sekä viikonpäivien mukaan ryhmiteltyyn sanakirjaan
for d in data:
    if isinstance(d, dict):
        date = datetime.date.fromisoformat(d["timestamp"][:10])
        val = float(d["value"])
        days.append((date, val))
        weekdays[date.strftime("%A")].append(val)

# Tulostetaan 5 päivää suurimmalla kulutuksella (lajiteltu kulutusarvon mukaan lambda-funktion avulla)
print("\nTop 5 päivät:")
for d, v in sorted(days, key=lambda x: x[1], reverse=True)[:5]:
    print(f"{d}: {v:.2f} kWh")

# Lasketaan viikonpäivien keskimääräinen kulutus ja valitaan suurin (lambda lajittelee kulutusarvon mukaan)
avg = {k: sum(v) / len(v) for k, v in weekdays.items()}
top_day = max(avg.items(), key=lambda x: x[1])
print(f"\nSuurin keskimääräinen:\n{top_day[0]} - {top_day[1]:.2f} kWh")
