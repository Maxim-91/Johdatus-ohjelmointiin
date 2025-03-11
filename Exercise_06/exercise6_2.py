# Teen ohjelma, jonka avulla käyttäjä voi tulostaa haluamansa luvun kertotaulun väliltä 1 – 10,
# niin monta kertaa kuin hän haluaa ohjelmaa käyttää.
while True:

    # Kysyn aluksi käyttäjältä, minkä luvun kertotaulun hän haluaa nähdä nyt
    number = int(input("Minkä luvun kertotaulun haluat nähdä? (1-10). 0 lopettaa ohjelman.\n"))

    # Ohjelman toiminta loppuu ainoastaan silloin, jos käyttäjä syöttää 0:n
    if number == 0:
        break

    # Kertotaulukosta valitun näyttäminen
    elif 1 <= number <= 10:
        for i in range(10):
            print(f"{number} x {i+1} = {number*(i+1)}")
    else:
        print("Vääränlainen luku.")
