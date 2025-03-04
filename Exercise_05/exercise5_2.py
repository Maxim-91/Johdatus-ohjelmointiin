# Kysyn käyttäjältä 12 kertaa kuukauden sademäärä silmukassa
sademaara = []
for i in range(12):
    maara = int(input("Anna kuukauden sademäärä:\n"))
    sademaara.append(maara)
# Sademäärien keskiarvo
keskiarvo = sum(sademaara) / 12
print(f"Vuoden Keskiarvo on n. {keskiarvo:.1f} mm")
