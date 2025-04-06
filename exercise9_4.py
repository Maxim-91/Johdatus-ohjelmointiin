import functions as f

# pyydetään numerot yhtenä tekstinä käyttäjältä
people_string = input("Syötä tapahtuman osallistujat pilkulla eroteltuna:\n")

# muutetaan käyttäjän antama teksti listaksi
people = people_string.split(",")

# otetaan nimistä ylimääräiset välilyönnit pois (nimen alusta ja lopusta)
people = [p.strip() for p in people]

# vaihe 1: kutsutaan show_numbered_list -funktiota, parametreina otsikko ja osallistujalista
f.show_numbered_list("Ilmoittautumisjärjestys", people)

# vaihe 2: järjestetään osallistujat-lista sorted() -funktiolla aakkosjärjestykseen
people = sorted(people)

# vaihe 3: kutsutaan show_numbered_list -funktiota, parametreina otsikko ja osallistujalista
f.show_numbered_list("Aakkosjärjestys etunimen perusteella:", people)

# vaihe 4: järjestetään osallistujat aakkosjärjestykseen sukunimen perusteella
# muutetaan listan henkilöt niin, että sukunimi tulee ennen etunimeä.
# tämä on ns. list comprehension -ominaisuus Pythonissa.
# Logiikka: jokainen nimi vuorollaan muutetaan listaksi
# välilyönnin perusteella, eli tämän vuoksi jokainen nimi on lista,
# jossa on kaksi elementtiä, etunimi ja sukunimi.
# sitten elementtien järjestys muutetaan toisin päin käyttämällä
# reversed-funktiota- lopuksi uusi järjestys muutetaan takaisin
# kokonaiseksi nimeksi .join() -funktion avulla. Lopputuloksena
# people lista koostuu nimistä, joissa sukunimi tulee ensin.
people = [" ".join(reversed(p.split(" "))) for p in people]
people = sorted(people)

# vaihe 5: kutsutaan show_numbered_list -funktiota, parametreina otsikko ja osallistujalista
f.show_numbered_list("Aakkosjärjestys sukunimen perusteella:", people)
