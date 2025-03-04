# Teen ohjelma, jossa on seuraavanlainen yksinkertainen lista (list):
cities = ['Rooma', 'Ateena', 'Tukholma', 'Lontoo', 'Dublin', 'Pariisi']

# Listan laittaminen aakkosjärjestykseen (tai numerojärjestykseen)
cities.sort()

# Tulosen lista käyttämällä silmukkaa
amount = len(cities)
for i in range(amount):
    print(f"{i + 1}: {cities[i]}")
    