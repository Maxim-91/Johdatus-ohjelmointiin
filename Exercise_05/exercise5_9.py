# Teen ohjelmassa lista, jossa on vähintään 10 eri suomalaista etunimeä
nimet = ["Matti", "Mikka", "Juho", "Aino", "Eero", "Johanna", "Mattias", "Oskari", "Päivi", "Hertta"]

# Suodatetaan nimet list comprehensionilla:
# 1. Nimet joissa ei ole s-kirjainta
# 2. Nimet joissa ei ole e-kirjainta
# 3. Nimet jotka ovat alle 8 merkkiä pitkiä
suodatetut_nimet = [x for x in nimet
                    if "s" not in x and "e" not in x and len(x) < 8]
print(suodatetut_nimet)

# Lisätehtävä: Nimet joissa on maksimissaan 2 vokaalia (haastava!)
vokaalit = "aäeioöuy" # vokaalia
lopullinen_lista = [nimi for nimi in suodatetut_nimet
                    if sum(1 for kirjain in nimi.lower()
                           if kirjain in vokaalit) <= 2]
print(lopullinen_lista)
