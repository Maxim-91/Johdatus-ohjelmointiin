# Teen ohjelma, joka selvittää missä kaupungissa on
# Suomessa tilastollisesti ollut eniten liukastumisvaroituksia.
#
# Liukastumisvaroituksia voi ladata seuraavasta internet-rajapinnasta (API):
# https://liukastumisvaroitus-api.beze.io/api/v1/warnings

import json
import urllib.request
from datetime import datetime

url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
liukastumisvaroitusta = json.loads(raw_data)

# Näytä lisäksi myös 5 viimeisintä liukastumisvaroitusta aikaleiman perusteella
# (kaupunki + päivämäärä + kellonaika)

# Ensin lajittelen tiedot ajan mukaan (uusimmasta vanhimpaan)
liukastumisvaroitusta.sort(key=lambda x:
    datetime.strptime(x['created_at'], "%Y-%m-%d %H:%M:%S"), reverse=True)

# Näytän 5 viimeisintä liukastumisvaroitusta
for i in liukastumisvaroitusta[:5]:
    created_at = datetime.strptime(i['created_at'], "%Y-%m-%d %H:%M:%S")  # Muutan merkkijonon päivämääräksi
    print(f"Kaupunki: {i['city']}, Päivämäärä: {created_at.date().strftime("%d.%m.%Y")}, Kellonaika: {created_at.time().strftime("%H:%M")}")
