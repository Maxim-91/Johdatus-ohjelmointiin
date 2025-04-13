# Vaihtoehto 2: Ventti Vaihtoehto 2: Ventti.
# Teen venttipeli, jossa kone arpoo pelikortteja (käytännössä luvun väliltä 1-13, ässä on siis tässä aina ykkönen).
# Kortin arvottuaan kone ilmoittaa arvotun kortin numeron ja tähänastisen korttien numeroiden summan
# sekä kysyy haluaako käyttäjä lopettaa vai ottaa lisää kortteja.
#  Jos summa menee yli 21, tulostetaan näytölle "JAKAJAN VOITTO".
#  Jos summaksi tulee 21, tulostetaan näytölle "VENTTI, PELAAJAN VOITTO".
#  Jos summa jää alle 21 ja käyttäjä lopettaa arpomisen, kone arpoo omat pelikortit.

import random

# Toiminto = satunnainen kortti (numerot 1-13)
def draw_card():
    return random.randint(1, 13)

# Pelaaja-käyttäjä asettaa vedon
def player_turn():
    total_player = 0

    while True:
        card = draw_card()
        total_player += card
        print(f"Sait kortin {card}. Kokonaissumma: {total_player}")

        # Jos summa menee yli 21, tulostetaan näytölle "JAKAJAN VOITTO".
        if total_player == 21:
            print("VENTTI, PELAAJAN VOITTO.")  # Pelaaja sai 21
            return total_player
        elif total_player > 21:
            print("JAKAJAN VOITTO.")  # Pelaaja häviää, jos summa yli 21
            return None

        # Käyttäjältä kysytään, haluaako lisää kortteja
        choice = input("Haluatko lisää kortteja? (k/e):\n").lower()
        if choice == 'e':
            return total_player  # Pelaaja lopettaa vuoron
        elif choice == 'k':
            continue  # Pelaaja jatkaa korttien ottamista
        else:
            print("Syötä vain k tai e.")
            continue

# Kone arpoo uuden pelikortin aina, kun korttien summa on alle 17.
# Jos koneen lopullinen summa on pienempi kuin käyttäjän lopullinen summa
# tai summa menee yli 21, kone häviää. Samalla tuloksella kone voittaa.
def dealer_turn(player_total):
    total_dealer = 0
    print("\n----- Jakajan vuoro -----")

    while total_dealer < 17:
        card = draw_card()
        total_dealer += card
        print(f"Jakaja sai kortin {card}. Kokonaissumma: {total_dealer}")

    print(f"\nPelaajan summa: {player_total} | Jakajan summa: {total_dealer}")

    if total_dealer > 21 or total_dealer < player_total:
        print("Pelaajan voitto!")
        return "player"
    else:
        print("Jakajan voitto!")
        return "dealer"

# Pelin pääsilmukka, joka käsittelee panokset, kierrokset ja voitot.
# Lisäpisteitä tulee, jos lisäät ohjelmaa panoksien sijoittamisen.
# Ohjelma kysyy aina ennen peliä, mikä on pelaajan panos. Ohjelma kirjaa peleissä tulleet voitot
# ja tappiot ja ilmoittaa lopuksi pelaajalle voittojen tai tappioiden suuruuden.
def play_round():
    balance = 0  # Lisätehtävä: pelaajan nettovoitot/tappiot

    while True:
        try:
            bet = int(input("Anna panos (€):\n"))  # Panoksen kysyminen
            if bet <= 0:
                print("Panos pitää olla positiivinen.")
                continue
        except ValueError:
            print("Anna kelvollinen luku.")
            continue

        # Pelaajan vuoro
        player_result = player_turn()

        # Tarkistetaan tulos
        if player_result is None:
            balance -= bet  # Pelaaja hävisi
        elif player_result == 21:
            balance += bet  # Pelaaja sai VENTTI
        else:
            # Jakajan vuoro
            winner = dealer_turn(player_result)
            if winner == "player":
                balance += bet
            else:
                balance -= bet

        print(f"Nettovoittosi: {balance} €")  # Näytetään pelaajan tilanne

        # Uusi kierros?
        again = input("\nHaluatko pelata uudelleen? (k/e):\n").lower()
        if again == 'e':
            print(f"\nKiitos pelaamisesta! Kokonaisvoittosi: {balance} €")
            break
        elif again == 'k':
            continue
        else:
            print("Syötä vain k tai e.")
            continue

# Käynnistetään peli
play_round()
