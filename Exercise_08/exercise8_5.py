# Pyydä käyttäjältä lista numeroita, ja tee niiden pohjalta tolppadiagrammi
# Voit käyttää haluamaasi Python-graafikirjastoa
# (yleisiä graafikirjastoja ovat seaborn, plotly ja matplotlib)

# Luin netistä, että Matplotlib on yksinkertainen ja universaali, joten päätin valita sen käyttöön.
# Otin tämän sivuston koodin esimerkkinä ja modernisoin sen tehtävää varten:
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/

import matplotlib.pyplot as plt

# Tietojen vastaanottaminen käyttäjältä
# y-akseli
numerot = input("Anna numeroita pilkulla erotettuna: ")
numerot = [int(n) for n in numerot.split(",")]
# x-akseli
sarjanumero = list(range(1, len(numerot) + 1))

plt.bar(sarjanumero, numerot)
plt.title("Tolppadiagrammi")
plt.xlabel("Syötettyjen numeroiden järjestysnumero")
plt.ylabel("Numeron suuruus")
plt.show()
