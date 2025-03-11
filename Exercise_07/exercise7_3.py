# Luon ohjelmaani seuraavanlainen lista:
shopcart = [
    {"name": "Lokki-valaisin", "price": 349.9},
    {"name": "Stockholm-matto", "price": 129.9},
    {"name": "Malm-lipasto", "price": 49.9},
    {"name": "Vienna-divaanisohva", "price": 799.9},
    {"name": "Ritz-nojatuoli", "price": 369.9}
]

# Tulosta ostosten kuitti silmukassa kokonaishinnan kanssa alla olevan esimerkin mukaisesti
print(f"Kuitti ostoksista:")
kuitti = 0
for i in shopcart:
    print(f"- {i['name']}")
    kuitti += i["price"]

print("\n" + f"Yhteensä {kuitti:.2f} €." + "\n" +
      "Tervetuloa uudelleen!")

# Lisätehtävä: Laske kuittiin hinnasta myös ALV –osuus (24%) euroina.
alv = kuitti - (kuitti / 1.24)
print(f"ALV (24 %): {alv:.2f} €.")


