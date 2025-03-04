i = 1

# Tulostaa luvut 1-50 allekkain. Käytä while-toistolausetta
while i <= 50:
    print(f"{i}")
    i += 1

# Tulostaa luvut 1-50 allekkain. Käytä for-toistolausetta
for i in range(1, 51):
    print(f"{i}")

# Teen silmukka, joka laskee kaikkien numeroiden summan väliltä 1 – 30
summa = 0
for i in range(31):
    summa += i
print(f"Summa: {summa}")

# Teen silmukka, joka tulostaa kaikki vuosiluvut väliltä 2005-2010
# välilyönnillä eroteltuna samalle riville
vuodet = []
for i in range(2005, 2011):
    vuodet.append(str(i))
print(" ".join(vuodet))
