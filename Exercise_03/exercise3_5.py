# Pisteet pyyntö käyttäjältä
pistetta = int(input("Anna pistemäärä: \n"))

# Arvosana tuotos pistemäärästä riippuen
if 0 <= pistetta <= 50:
    print("Arvosana: 0")
elif 51 <= pistetta <= 60:
    print("Arvosana: 1")
elif 61 <= pistetta <= 70:
    print("Arvosana: 2")
elif 71 <= pistetta <= 80:
    print("Arvosana: 3")
elif 81 <= pistetta <= 90:
    print("Arvosana: 4")
elif 91 <= pistetta <= 100:
    print("Arvosana: 5")
else:
    print("Pistemäärä ei ole mahdollinen.")
