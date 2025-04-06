import functions as f

# Pyydän laskettavat luvut käyttäjältä, ja tulosta lopputulos.
# hours = int(input("Anna tunnit:\n"))
# inutes = int(input("Anna minuutit:\n"))
# seconds = int(input("Anna sekunnit:\n"))

# full_time = f.count_seconds(hours, minutes, seconds)
# print(f"Yhteensä {full_time} sekuntia.")

# Lisätehtävä: Hyväksy käyttäjän antama formaatti ajasta: “2h 45min 33sek”
time = str(input("Anna aika (esm. 2h 45min 33sek):\n"))
time_pats = time.split(" ")
full_time = f.count_seconds(time_pats[0], time_pats[1], time_pats[2])
print(f"Yhteensä {full_time} sekuntia.")
