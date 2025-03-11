from colorama import Fore

# Teen ohjelma, joka etsii alkuluvut väliltä 2-100. Tulosta jokainen numero siten,
# että alkuluvut tulostetaan vihreällä taustavärillä,
# ja muut luvut punaisella taustavärillä.
#
# Huom: alkuluku on kokonaisluku joka on ainoastaan jaollinen itsellään ja 1:llä.
# Esim. 7 on alkuluku, 9 ei. (koska yhdeksän on jaollinen myös kolmella.)

a = 0 # Lasken jakojen lukumäärän
for i in range(2, 101):
    for j in range(2, 101):
        if i % j == 0:
            a += 1
    if a == 1: # Jos a = 1, se tarkoittaa, että luku on jaollinen vain itsellään.
        a = 0
        print(Fore.GREEN + f"{i}")
    else: # Muissa tapauksissa luku ei voi olla alkuluku
        a = 0
        print(Fore.RED + f"{i}")
