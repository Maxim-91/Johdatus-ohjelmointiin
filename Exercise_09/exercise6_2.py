# Lisätehtävä №9.7 Aiemmat harjoitukset funktioiden avulla
# Valitse jokin seuraavista aiemmista harjoituksista, ja tee siitä sellainen versio,
# että ohjelman logiikka on sijoitettu joko yhteen tai useampaan funktioon.
# Voit tehdä myös monta aiempaa harjoitusta funktioilla, lisäpisteitä tulee maksimissaan 3:sta aiemmasta tehtävästä.
# Vaihtoehdot:

#  Viikkotehtävä 6 – 2

import functions as f

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
