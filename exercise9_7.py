# Aiemmat harjoitukset funktioiden avulla
#
# Valitse jokin seuraavista aiemmista harjoituksista, ja tee siitä sellainen versio,
# että ohjelman logiikka on sijoitettu joko yhteen tai useampaan funktioon.
# Voit tehdä myös monta aiempaa harjoitusta funktioilla, lisäpisteitä tulee maksimissaan 3:sta aiemmasta tehtävästä.
# Vaihtoehdot:
#  Viikkotehtävä 3 – 3
#  Viikkotehtävä 4 – 2
#  Viikkotehtävä 6 – 2
#  Viikkotehtävä 6 – 3
#  Viikkotehtävä 7 – 5
#  Lisätehtävä 3 – 7 tai 3 – 8
#  Lisätehtävä 4 – 7
#  Lisätehtävä 5 – 8
#  Lisätehtävä 6 – 8

import functions as f

#  Viikkotehtävä 3 – 3
# Käyttäjän viikon työtuntimäärän ja tuntipalkan
tyotuntia = float(input("Syötä viikon työtunnit: \n"))
tuntipalkkaa = float(input("Syötä tuntipalkkasi: \n"))

# Palkan laskeminen ylitöitä läsnä ollessa
palkka = f.palkkojen_laskeminen(tyotuntia, tuntipalkkaa)

# Tulos
print(f"Viikon ansiosi avat: {palkka:.2f}€")


#-----------------------------------------------------------------------------------
#  Viikkotehtävä 4 – 2
# Kysyn käyttäjältä tekstiä
text = input("Anna jokin teksti:\n")

# Käännän teksti
reversed_text = f.kaannan_teksti(text)
print(reversed_text) #Tulos

#-----------------------------------------------------------------------------------
#  Viikkotehtävä 6 – 2
# Teen ohjelma, jonka avulla käyttäjä voi tulostaa haluamansa luvun kertotaulun väliltä 1 – 10,
# niin monta kertaa kuin hän haluaa ohjelmaa käyttää.
while True:

    # Kysyn aluksi käyttäjältä, minkä luvun kertotaulun hän haluaa nähdä nyt
    number = int(input("Minkä luvun kertotaulun haluat nähdä? (1-10). 0 lopettaa ohjelman.\n"))

    # Ohjelman toiminta loppuu ainoastaan silloin, jos käyttäjä syöttää 0:n
    if number == 0:
        break

    # Kertotaulukosta valitun näyttäminen
    f.tulosta_kertotaulu(number)
