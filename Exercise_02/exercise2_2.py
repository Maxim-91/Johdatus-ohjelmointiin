import math

# Käyttäjätiedot suorakulmaisen kolmion jalkojen pituuksista (a ja b)
a = float(input("Anna kolmion ensimmäinen kateetti:\n"))
b = float(input("Anna kolmion toinen kateetti:\n"))

# Hypotennuusan laskelmat kaavan avulla
с = math.sqrt(a**2 + b**2)
с = round(с, 2)

print(f"Hypotennuusan pituus: {с} m\n") # Tulos

