import math

# Selvitä kirsikan merkitys
# 2 kirsikkaa = 2 + 2 * 2 + 2 - 2 - 2
kirsikka = (2 + 2 * 2 + 2 - 2 - 2)/2

# Selvitä omenan merkitys
omena = math.sqrt(3 + 10 - 4) / 3 + (5 ** 3 - 5) / 20 + 3

# Selvitä appelsiinin merkitys, omenan - appelsiini = 9
appelsiini = omena - 9

# Selvitä banaanin merkitys, 2 kirsikkaa - 3 banaania = 10
banaani = (2 * kirsikka - 10) / 3

# Selvitä päärynän merkitys, 3 banaania - päärynä = 8
päärynä = 3 * banaani - 8

# Halutun arvon laskeminen = omena - 2 banaania + 2 appelsiinia * (päärynä + kirsikka)
x = omena - 2 * banaani + 2 * appelsiini * (päärynä + kirsikka)

print(f"Vastaus = {x}") # Tulos