# Tallenna seuraava teksti muuttujaan nimeltä text, ja tulosta se näytölle
text = "The quick brown fox jumps over the lazy dog. That sentence contains every letter in the English alphabet. Neat!"
print(text)

# Muokkaa text-muuttujaa niin, että ”fox” vaihdetaan sanaan ”duck”
text = text.replace("fox", "duck")
print(text)

# Pyydä käyttäjältä jokin sana, joka poistetaan text-muuttujasta
pois = str(input("\nAnna poistettava sana:\n"))
# Jos sanaa ei löydy text-muuttujasta
if pois not in text:
    print("Sanaa ei löytynyt.")
# Sana poistetaan text-muuttujasta
else:
    text = text.replace(pois, "")
    print(text)

# Tulosta text-muuttujassa olevien merkkien ja sanojen lukumäärä.
merkkeja = len(text)
sanoja = len(text.split())
print(f"\nMerkkejä: {merkkeja} \nSanoja: {sanoja}\n")

# Muuta text-muuttujan tekstin pisteet rivinvaihdoiksi
text = text.replace(".", "\n")
print(text)

# Pyydä käyttäjältä jokin lause
usertext = str(input("\nAnna jokin lause:\n"))
# Jos usertext on yli 20 merkkiä pitkä,
# lyhennä se tasan 20 merkkiä pitkäksi,
# sekä lisää perään kolme pistettä "…".
if len(usertext) > 20:
    usertext = usertext[:20] + "..."
    print(usertext)
else:
    print(usertext)
