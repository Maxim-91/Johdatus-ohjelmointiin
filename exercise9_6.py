# Lottorivi
import functions as f

# Olen luomassa listaa lottonumeroista
lotto_numbers = []

# Täytän lista 7 numerolla silmukalla
while len(lotto_numbers) < 7:
    number = f.generate_lotto()

    # Tarkistan funktion valitseman numeron yksilöllisyyden
    if number not in lotto_numbers:
        lotto_numbers.append(number)

# Toistan saman esimerkiksi kahdelle bonusnumerolle
bonus_numbers = []
while len(bonus_numbers) < 2:
    number = f.generate_lotto()
    if number not in lotto_numbers and number not in bonus_numbers:
        bonus_numbers.append(number)

# Tulos
print("Lotto numbers:", lotto_numbers)
print("Bonus numbers:", bonus_numbers)
