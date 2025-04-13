# Lisätehtävä - Luokat ja oliot

# Erillinen lisätehtävä 2:
# Teen Python-ohjelma jolla voi muuntaa aiemmin tehdyn Product-luokan JSONiksi, ja toisinpäin!
import jsonpickle
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

# Tuotteet JSON-muotoon
json_data = jsonpickle.encode(products)
print(json_data + "\n")

# Tallenna tiedostoon
with open("product.json", "w") as file:
    file.write(json_data)

# Lue takaisin tiedostosta
with open("product.json", "r") as f:
    loaded_data = f.read()

# Takaisin tuotteksi
product_restored = jsonpickle.decode(loaded_data)

# Tulos
for i in product_restored:
    i.print_info()
