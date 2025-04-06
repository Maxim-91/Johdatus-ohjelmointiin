# Lisätehtävä №9.7 Aiemmat harjoitukset funktioiden avulla
# Valitse jokin seuraavista aiemmista harjoituksista, ja tee siitä sellainen versio,
# että ohjelman logiikka on sijoitettu joko yhteen tai useampaan funktioon.
# Voit tehdä myös monta aiempaa harjoitusta funktioilla, lisäpisteitä tulee maksimissaan 3:sta aiemmasta tehtävästä.
# Vaihtoehdot:

#  Viikkotehtävä 3 – 3

import functions as f

# Käyttäjän viikon työtuntimäärän ja tuntipalkan
tyotuntia = float(input("Syötä viikon työtunnit: \n"))
tuntipalkkaa = float(input("Syötä tuntipalkkasi: \n"))

# Palkan laskeminen ylitöitä läsnä ollessa
palkka = f.palkkojen_laskeminen(tyotuntia, tuntipalkkaa)

# Tulos
print(f"Viikon ansiosi avat: {palkka:.2f}€")
