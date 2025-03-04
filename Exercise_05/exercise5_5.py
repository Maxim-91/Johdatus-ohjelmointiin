# Teen ohjelma, jossa on tuple, joka sisältää suomeksi eri kuukausien nimet
months = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu",
          "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

# Pyydä käyttäjältä kuukauden numero (1-12)
month = int(input("Anna kuukauden numero:\n"))
print(f"{months[month - 1]}")
