# Teen ohjelma, jossa on seuraavanlainen lista tunnisteita:
products = ["K1565_2017_ST7745", "T2432_2019_FE84",
            "T8551_2018_XA413", "T3345_2019_JK142",
            "Y51372_2019_HJ2", "Y76715_2017_AB3",
            "E98144_2018_21T", "T7733_2020_CE55",
            "E7614_2021_XZA784", "E9722_2017_MHE67",
            "Y82018_2020_FI95", "T61287_2021_IA293",
            "E9152_2019_TY5", "T774_2021_OB672"]

# Lista koostuu tilaustunnisteista, joista yksittäinen tunniste noudattaa seuraavaa kaavaa:
# TILAUSKOODI_VUOSILUKU_LISÄTUNNISTE

# Pyydä käyttäjältä vuosiluku
vuosi = int(input("Minkä vuoden koodit haetaan?\n"))

# Tulosta vain ne TILAUSKOODIT listasta, joiden vuosiluku täsmää käyttäjän antaman vuoden kanssa
for i in products:
    parts = i.split("_")
    tilauskoodi = parts[0]
    vuosiluku = int(parts[1])
    # lisatunniste = parts[2]
    if vuosiluku == vuosi:
        print(tilauskoodi)
