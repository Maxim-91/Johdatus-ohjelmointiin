# Monimutkainen tiedon järjestäminen (custom sort)

import functions as f

# Tee ohjelmassasi seuraava lista (joka koostuu dictionaryistä):
#  0:
    # o city : ”Rovaniemi”
    # o company: ”Sampokeskus”
#  1:
    # o city : ”Oulu”
    # o company: ”Myllyoja”
#  2:
    # o city : ”Rovaniemi”
    # o company: ”Rinteenkulma”
#  3:
    # o city : ”Rovaniemi”
    # o company: ”Revontulikeskus”
#  4:
    # o city : ”Oulu”
    # o company: ”Valkea”
#  5:
    # o city: ”Oulu”
    # o company: ”Ideapark”

data = [
    {'city': 'Rovaniemi', 'company': 'Sampokeskus'},
    {'city': 'Oulu', 'company': 'Myllyoja'},
    {'city': 'Rovaniemi', 'company': 'Rinteenkulma'},
    {'city': 'Rovaniemi', 'company': 'Revontulikeskus'},
    {'city': 'Oulu', 'company': 'Valkea'},
    {'city': 'Oulu', 'company': 'Ideapark'}
]

# Tee Python –ohjelma, jossa on funktio nimeltä city_company_sort(data), joka suodattaa listan siten,
# että tiedot laitetaan aakkosjärjestykseen ensin kaupungin, ja vasta sitten ostoskeskuksen nimen perusteella.
# Tämän voi ratkaista usealla eri tavalla!
#
# Lopputuloksen tulisi olla tässä tapauksessa:
# Oulu: Ideapark
# Oulu: Myllyoja
# Oulu: Valkea
# Rovaniemi: Revontulikeskus
# Rovaniemi: Rinteenkulma
# Rovaniemi: Sampokeskus

sorted_data = f.city_company_sort(data)

# Tulos
for i in sorted_data:
    print(f"{i['city']}: {i['company']}")