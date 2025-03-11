# Pyydä silmukassa käyttäjältä 5 positiivista lukua
max_number = 0
i = 0

while i < 5:
    number = int(input("Anna numero:\n"))
    # Lisätehtävä: Tarkista että käyttäjä syöttää datan oikeassa muodossa (positiivinen kokonaisluku)
    if number >= 0:
        max_number = max(max_number, number)
        i += 1
    else:
        print("Numeron on oltava positiivinen (eli >= 0)")

# Näytä ainoastaan suurin käyttäjän syöttämä luku
print(f"Suurin käyttäjän luku: {max_number}")