import random

random_number = random.randint(1, 10) # palauttaa satunnaisen luvun 1 ja 10 välillä
print(f"Arvottu luku: {random_number}") # Tulos

# Suorakulmion satunnaiset sivut ja sen pinta-ala
number1 = random.randint(2, 10)
number2 = random.randint(2, 10)
pinta_ala = number1 * number2

# Tulos
print(f"Arvottu 1. sivu: {number1}\n"
      f"Arvottu 2. sivu: {number2}\n"
      f"Arvotuista sivuista laskettu pinta-ala: {pinta_ala}")


