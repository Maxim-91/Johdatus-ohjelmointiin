# Vuosipyyntö käyttäjältä
vuosi = int(input("Anna vuosiluku: \n"))

# Muussa tapauksessa != karkausvuosi
karkausvuosi = False

# Jos vuosiluku on jaollinen 400:lla = karkausvuosi
if vuosi % 400 == 0:
    karkausvuosi = True
# Jos vuosiluku on jaollinen 100:lla != karkausvuosi
elif vuosi % 100 == 0:
    karkausvuosi = False
# Jos vuosiluku on jaollinen 4:llä = karkausvuosi
elif vuosi % 4 == 0:
    karkausvuosi = True

if karkausvuosi:
    print("Karkausvuosi: KYLLÄ")
else:
    print("Karkausvuosi: EI")
