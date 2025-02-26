# Pyydä tietoja käyttäjältä (senttiä)
senttiä = int(input("Anna 1-100 senttiä:\n"))

# Määritä, kuinka monta 50 sentin kolikkoa tarvitset
snt50 = senttiä // 50

# Määritän sentin loput
senttiä -= snt50 * 50

# Toistan operaation jokaiselle sentin nimellisarvolle
snt20 = senttiä // 20
senttiä -= snt20 * 20

snt10 = senttiä // 10
senttiä -= snt10 * 10

snt5 = senttiä // 5
senttiä -= snt5 * 5

snt2 = senttiä // 2
senttiä -= snt2 * 2

snt1 = senttiä // 1
senttiä -= snt1 * 1

# Tulos
print(f"50 snt kolikoita {snt50} kpl\n"
      f"20 snt kolikoita {snt20} kpl\n"
      f"10 snt kolikoita {snt10} kpl\n"
      f"5 snt kolikoita {snt5} kpl\n"
      f"2 snt kolikoita {snt2} kpl\n"
      f"1 snt kolikoita {snt1} kpl")

# Koodi voidaan muuntaa for-silmukaksi