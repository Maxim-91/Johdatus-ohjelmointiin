# Edistyneemmät funktiotekniikat

import functions as f # Ulkoista toimintoa ei tarvinnut käyttää
import random

#  Tee lambda, joka palauttaa Booleanin riippuen siitä, onko annettu kokonaisluku parillinen
# o Vinkki: Lambdan voi tallentaa muuttujaan!
is_lambda_true = lambda x: x % 2 == 0

#  Tee seuraavaksi kokoelma, jossa on satunnaisesti parittomia ja parillisia lukuja
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print("Satunnaisesti parittomia ja parillisia lukuja:", numbers)

#  Käytä filter():ä siten, että suodatat kokoelmasta parittomat luvut käyttämällä aiemmin tekemääsi lamdbaa
# o filter() palauttaa ns. filter objectin, joka pitää kääntää vielä listaksi käyttämällä list() -funktiota
is_lambda_false = lambda x: x % 2 != 0
filter_numbers = list(filter(is_lambda_false, numbers))
print("Parittomat luvut:", filter_numbers)

#  Käytä map()- funktiota siten, että käsittelet kokoelman aiemmin tekemälläsi lambdalla
# o map() –palauttaa ns. map objectin, joka pitää kääntää vielä listaksi käyttämällä list() -funktiota
is_map_true = list(map(is_lambda_true, numbers))
print("True ja False –arvoja:", is_map_true)
