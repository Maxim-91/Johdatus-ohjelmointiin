# Lisätehtävä - Luokat ja oliot

# Teen uusi Python-tiedosto, joka käyttää Product-luokkaa, esim. store.py.
# Teen 5 oliota Product-luokasta, ja laita ne listaan, ja käy jokainen tuote silmukassa läpi.
# Tulosta tuotteet käyttämällä luokassa olevaa print_info() -metodia.

from product import Product

# Tuotteita
product1 = Product(15, "Mikroaaltouuni 123X", "Kodinkoneet", 99.0)
product2 = Product(35, "Nokia 3310", "Puhelimet", 129, True)
product3 = Product(42, "Lenovo ThinkPad", "Tietokoneet", 899.95)
product4 = Product(8, "Kahvinkeitin", "Kodinkoneet", 49.5, True)

# Käytän oletusarvoja
product5 = Product()

# Tuotteet listassa
products = [product1, product2, product3, product4, product5]

# Lisätehtävä:
# Järjestä tekemäsi oliolista Kategorioittain (helpoin tapa on käyttää lambdaa)
products.sort(key=lambda p: p.category)

# Tulos
for i in products:
    i.print_info()
