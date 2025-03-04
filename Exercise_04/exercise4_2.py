# Kysyn käyttäjältä tekstiä
text = input("Anna jokin teksti:\n")

# Käännän teksti
reversed_text = text[::-1]
print(reversed_text) #Tulos

# Määritän, onko testi tehty vai ei
if text == "":
    print("Antamasi teksti on tyhjä.")

# Määritän, onko teksti palindromi
elif text == reversed_text:
    print("Palindromi: KYLLÄ")
else:
    print("Palindromi: EI")
    