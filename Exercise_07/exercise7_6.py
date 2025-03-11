# Luon ohjelmaasi seuraavanlainen kokoelma,
# jossa on useita ravintoloita (vähintään 5 kpl tai enemmän):

restaurant0 = {
    "name": "North Delish",
    "rating": 4.5,
    "reservations": True,
    "services": ["lunch", "dinner"],
    "price_level": 5,
    "location": "Rovaniemi"
}

restaurant1 = {
    "name": "Food Galore",
    "rating": 3.8,
    "reservations": False,
    "services": ["breakfast", "lunch"],
    "price_level": 3,
    "location": "Tornio"
}

restaurant2 = {
    "name": "Snacksy Oy",
    "rating": 3.2,
    "reservations": False,
    "services": ["lunch", "dinner", "night"],
    "price_level": 2,
    "location": "Oulu"
}

restaurant3 = {
    "name": "Mama's Kitchen & bar",
    "rating": 4.6,
    "reservations": False,
    "services": ["breakfast", "lunch"],
    "price_level": 1,
    "location": "Vaasa"
}

restaurant4 = {
    "name": "Ravintola Poro",
    "rating": 3.7,
    "reservations": True,
    "services": ["dinner", "night"],
    "price_level": 2,
    "location": "Tampere"
}

restaurant5 = {
    "name": "Jufu",
    "rating": 3.9,
    "reservations": False,
    "services": ["lunch", "dinner"],
    "price_level": 1,
    "location": "Espoo"
}

restaurants = [restaurant0, restaurant1, restaurant2, restaurant3, restaurant4, restaurant5]

# Pyydä tämän jälkeen käyttäjältä kysymyksiä, minkälaisen ravintolan hän haluaisi valita (numero- ja kyllä/ei -kysymyksiä).
#
# Esim.
# Tervetuloa ravintolahakuun!
# Monenko tähden ravintolan haluat vähintään? (1-5)
# Minkä hinta-tason ravintolan haluat maksimissaan? (1-5)
# Haluatko tehdä etukäteen varauksen? (k/e)
# Mihin kellonaikaan haluat ruokailla? (0 – 23)

tahti = int(input("Monenko tähden ravintolan haluat vähintään? (1-5):\n"))
hinta = int(input("Minkä hinta-tason ravintolan haluat maksimissaan? (1-5):\n"))

varaus = str(input("Haluatko tehdä etukäteen varauksen? (k/e):\n"))
if varaus == "k" or varaus == "K":
    is_varaus = True
else:
    is_varaus = False

# breakfast = 6-10
# lunch = 11-16
# dinner = 17-24
# night = 0-5
kello = int(input("Mihin kellonaikaan haluat ruokailla? (0 – 23):\n"))
if 6 <= kello <= 10:
    services_time = "breakfast"
elif 11 <= kello <= 16:
    services_time = "lunch"
elif 17 <= kello <= 24:
    services_time = "dinner"
elif 0 <= kello <= 5:
    services_time = "night"

# Näytä lista niiden ravintoloiden nimistä, jotka vastaavat hakua
for restaurant in restaurants:
    if (restaurant["rating"] >= tahti and
        restaurant["price_level"] <= hinta and
        restaurant["reservations"] == is_varaus and
        services_time in restaurant["services"]):
            print(restaurant["name"], restaurant["location"])
