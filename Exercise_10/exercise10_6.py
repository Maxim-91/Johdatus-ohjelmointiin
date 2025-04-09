import os
import csv

# Käytä Pythonin CSV-moduulia, ja lataa tiedoston sisältö kokoelmaan. Tulosta sisältö silmukoimalla Pythonissa
input_file = "serialtest.csv"
data = []

# Luetaan CSV-tiedosto

# katsotaan onko käsiteltävä tiedosto olemassa: os.path.isfile(filename)
# katsotaan onko meillä käyttöoikeus tähän tiedostoon: os.access(filename, os.R_OK)
# katsotaan ettei tiedosto ole tyhjä: os.path.getsize(filename) > 0
if os.path.isfile(input_file) and os.access(input_file, os.R_OK) and os.path.getsize(input_file) > 0:

    # kaikki ok, luetaan tiedoston sisältö ja tulostetaan!
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row)  # Tulos

            # Lisähaaste:
            # Muokkaa lataamaasi sisältöä Pythonissa siten, että nostat jokaista palkkaa 100 €:lla,
            # ja tallenna lopputulos toiseen CSV-tiedostoon, ja avaa se lopuksi Excelissä.
            if 'Salary' in row:
                    row['Salary'] = str(int(row['Salary']) + 100)
            data.append(row)

# Kirjoitetaan uusi CSV-tiedosto
output_file = "updated_salaries.csv"
with open(output_file, 'w', newline='') as file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(data)

# Avataan uusi CSV-tiedosto Excelissä
import webbrowser
full_path = os.path.abspath(output_file)
webbrowser.open(full_path)
