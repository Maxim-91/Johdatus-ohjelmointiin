# Lämpötilaa pyydetään
t = int(input("Syötä päivän lämpötila: \n"))

# Vastauksen lähtö määritetystä lämpötilasta riippuen
if 0 <= t <= 10:
    print("KYLMÄÄ")
elif 11 <= t <= 15:
    print("KOLEAA")
elif 16 <= t <= 20:
    print("NORMAALI LÄMPÖTILA")
elif 21 <= t <= 25:
    print("LÄMMINTÄ")
elif 26 <= t <= 30:
    print("HELLETTÄ")
