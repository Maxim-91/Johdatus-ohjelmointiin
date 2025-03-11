import datetime

while True: # Silmukka ohjelman työn silmukointiin

    # Haastava lisätehtävä! Tee ohjelma,
    # joka laskee autokaupalle käytetyn auton myyntihinnan seuraavien tietojen perusteella
    # (kysy nämä tiedot käyttäjältä):

    # - Auton alkuperäinen hinta
    hinta = float(input("Alkuperäinen hinta:\n"))

    # - Auton valmistusvuosi
    vuosi = int(input("Valmistusvuosi:\n"))

    # - Ajokilometrit
    kilometrit = int(input("Mittarilukema:\n"))

    # - Auton valmistajan hintakategoria (1 vai 2)
    while True:
         try:
            kategoria = int(input("Hintakategoria (1 tai 2):\n"))
            if kategoria == 1 or kategoria == 2:
                break
         except ValueError:
            print("Syötä 1 tai 2.")

    # - Onko kyseessä tuontiauto (k/e)
    while True:
        try:
            tuontiauto = str(input("Tuontiauto (k/e):\n"))
            if tuontiauto == "k":
                is_tuontiauto = True
                break
            elif tuontiauto == "e":
                is_tuontiauto = False
                break
        except ValueError:
            print("Syötä k tai e.")

    # Luon muuttujan uuden hinnan laskemiseksi
    uusi_hinta = hinta
    current_year = datetime.datetime.now().year
    car_age = current_year - vuosi

    # * Jos kyseessä on hintakategoria 2:
    if kategoria == 2:
        if kilometrit >= 30000:
            if car_age >= 5:
                # 10% per year for the first 5 years, then 7% per year
                for i in range(5):
                    uusi_hinta *= 0.9
                for i in range(car_age - 5):
                    uusi_hinta *= 0.93
            else:
                for i in range(car_age):
                    uusi_hinta *= 0.9
        else:
            if car_age >= 5:
                # 8% per year for the first 5 years, then 5% per year
                for i in range(5):
                    uusi_hinta *= 0.92
                for i in range(car_age - 5):
                    uusi_hinta *= 0.95
            else:
                for i in range(car_age):
                    uusi_hinta *= 0.92
        # * Auton hinta ei koskaan laske kuitenkaan 12%:n alle alkuperäisestä hinnasta
        if uusi_hinta < hinta * 0.88:
            uusi_hinta = hinta * 0.88

    # * Jos kyseessä on hintakategoria 1:
    if kategoria == 1:
        if kilometrit >= 30000:
            if car_age >= 5:
                # 7% per year for the first 5 years, then 4% per year
                for i in range(5):
                    uusi_hinta *= 0.93
                for i in range(car_age - 5):
                    uusi_hinta *= 0.96
            else:
                for i in range(car_age):
                    uusi_hinta *= 0.93
        else:
            if car_age >= 5:
                # 5% per year for the first 5 years, then 3% per year
                for i in range(5):
                    uusi_hinta *= 0.95
                for i in range(car_age - 5):
                    uusi_hinta *= 0.97
            else:
                for i in range(car_age):
                    uusi_hinta *= 0.95
        # * Auton hinta ei koskaan laske kuitenkaan 18%:n alle alkuperäisestä hinnasta
        if uusi_hinta < hinta * 0.82:
            uusi_hinta = hinta * 0.82

    # * Tuontiautojen lopulliseen hintaan lisätään 24% veroa
    if is_tuontiauto:
        uusi_hinta = uusi_hinta * 1.24

    # Tulostetaan lopullinen hinta
    print(f"Lopullinen hinta: {uusi_hinta:.0f} €")

# Kun ohjelma on laskenut myyntihinnan autolle, kysytään käyttäjältä,
# haluaako hän syöttää uuden auton tiedot ohjelmaan.
# Mikäli hän vastaa ’e’, lopetetaan ohjelman suoritus ja kiitetään ohjelman käytöstä.
# Muussa tapauksessa ohjelma aloitetaan alusta.
    continue_input = input("Haluatko syöttää uuden auton tiedot? (k/e):\n").lower()
    if continue_input == "e":
        print("Kiitos ohjelman käytöstä!")
        break  # Sulje ohjelma, jos vastaus on "e"
    else:
        print("Aloitetaan alusta...\n")
