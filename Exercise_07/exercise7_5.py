# Teen ohjelma, joka lataa ajan tasalla olevat säätiedot internetistä,
# ja ilmoittaa käyttäjälle missä tällä hetkellä tuulee Suomessa eniten ja vähiten.

# Lataan ohjelmassa data tästä osoitteesta (koodiesimerkki alempana):
# https://edu.frostbit.fi/api/weather/

# Aloitan tällä koodilla. Internetistä ladatut tiedot ovat tässä tapauksessa weather –muuttujassa:
import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

# Määrittelen missä tällä hetkellä tuulee Suomessa eniten ja vähiten
vahva = heikko = weather[0]["wind"]
vahva_kaupunki = heikko_kaupunki = weather[0]["location"]

# Sanakirja alueiden kääntämiseen
area_mapping = {
    "lapland": "Lappi",
    "middle": "Maan keskiosa",
    "south": "Etelä-Suomi"
}
# Alustus keskiarvojen laskemista varten
wind_data = {}

# Käsitellään tietoja
for i in weather:
    # Määritä suurin ja pienin tuuli
    if i["wind"] > vahva:
        vahva = i["wind"]
        vahva_kaupunki = i["location"]
    if i["wind"] < heikko:
        heikko = i["wind"]
        heikko_kaupunki = i["location"]

    # Käsitellään keskiarvoja
    area = i["area"]
    if area not in wind_data:
        wind_data[area] = []
    wind_data[area].append(i["wind"])

# Näytä tiedot vahvimmasta ja heikoimmasta tuulesta
print(f"Tänään eniten tuulee sijainnissa: {vahva_kaupunki}, {vahva:.1f} m/s")
print(f"Tänään vähiten tuulee sijainnissa: {heikko_kaupunki}, {heikko:.1f} m/s")

# Laske ja näytä keskimääräiset tuuliarvot alueittain
for area, winds in wind_data.items():
    if winds and area in area_mapping:
        average_wind = sum(winds) / len(winds)
        print(f"Keskimääräinen tuuli, {area_mapping[area]}: {average_wind:.1f} m/s")
