# Hintapyyntö ilman alv
hinta_ilman_alv = float(input("Anna hinta ilman alv:\n"))

# Lisätään 24%
alv = 1.24
hinta_alvn_kanssa = hinta_ilman_alv * alv

# 2 desimaalin tarkkuudella
hinta_alvn_kanssa = round(hinta_alvn_kanssa, 2)

# Tulos
print(f"Hinta alv:n kanssa: {hinta_alvn_kanssa} €")