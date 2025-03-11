from colorama import Fore, Style
from datetime import datetime

# Kysyn käyttäjältä silmukassa viiden eri henkilön syntymävuosi,
# ja tallenna ne erilliseen listaan
syntymävuodet = []
for i in range(5):
    vuosi = int(input(f"Anna henkilön {i+1} syntymävuosi:\n"))
    syntymävuodet.append(vuosi)

# Päättelen henkilön ikä
kuluva_vuosi = datetime.now().year
iat  = []
for i in range(5):
    ika = kuluva_vuosi - syntymävuodet[i]
    iat.append(ika)

# Annetun iän tulee olla 0:n ja 125:n vuoden välillä
# Jos annettu ikä on oikeanlainen, tulosta ”ikä OK!” vihreällä tekstillä
# Jos ikä ei ole oikeanlainen, tulosta ”ikä ei ole oikeassa muodossa.” punaisella tekstillä
for i in iat:
    if 0 <= i <= 125:
        print(Fore.GREEN + f"{i} vuotta, ikä OK!.")
    else:
        print(Fore.RED + f"{i} vuotta, ikä ei ole oikeassa muodossa.")

# Kun kaikki iät on käsitelty, tulostetaan tavallisella tekstillä ”Valmis!”
print(Style.RESET_ALL + "Valmis!")
