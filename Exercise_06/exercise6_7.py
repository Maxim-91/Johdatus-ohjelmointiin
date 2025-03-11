# Teen ohjelma, joka etsii käyttäjän määrittelemältä lukualueelta lukua,
# joka on jaollinen viidellä ja seitsemällä


# Käyttäjältä kysytään hakualueen ala- ja yläraja
x = int(input("Anna alueen alaraja: "))
y = int(input("Anna alueen yläraja: "))

# Tulostetaan ohjelmassa jokaisesta luvusta tieto,
# onko se jaollinen 5:lla ja 7:lla vai ei.
a = False # Testimuuttuja, onko luku jaollinen 5:llä ja 7:llä?
for i in range(x, y+1):
    # Tarkistan eiko ole se jaollinen 5:llä
    if i % 5 != 0:
        print(f"{i} ei ole jaollinen viidellä, hylätään.")
    # Tarkistan onko se jaollinen 5:llä ja eiko ole 7:llä
    elif i % 5 == 0 and i % 7 != 0:
        print(f"{i} ei ole jaollinen seitsemällä, hylätään.")
    # Muuten käy ilmi, että se on jaollinen 5:llä ja 7:llä, tämä on haluttu tapaus
    else:
        print(f"Luku {i} on jaollinen 5:llä ja 7:llä.")
        print("Lopetetaan haku.")
        a = True
        break

if a == False:
    print("Alueelta ei löytynyt sopivaa arvoa.")
