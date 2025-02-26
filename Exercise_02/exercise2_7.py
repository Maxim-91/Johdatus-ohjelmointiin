import math

# Kysyn käyttäjältä eri muuttujien arvot (a, b ja c)
a = float(input("Anna arvo a: \n"))
b = float(input("Anna arvo b: \n"))
c = float(input("Anna arvo c: \n"))

# Lasken erottimen d=𝑏**2−4*𝑎*𝑐
d = b ** 2 - 4 * a * c

# Jos d>0, sitten kaksi eri arvoa
# Jos d=0, sitten yksi arvo
# Jos d<0, sitten ei arvoa ollenkaan
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Arvot: x1 = {x1}, x2 = {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"arvo: x = {x}")
else:
    print("Ei arvoa ratkaisuja.")

# Käytin GPT-chattia matemaattisen yhtälön ratkaisemiseen
# ja se antoi minulle 3 ratkaisua