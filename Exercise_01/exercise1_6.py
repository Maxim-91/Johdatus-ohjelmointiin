# Pyydä tietoja käyttäjältä (senttiä)
senttia = int(input("Anna 1-100 senttiä:\n"))

# Määritä, kuinka monta 50 sentin kolikkoa tarvitset
snt50 = senttia // 50
print(f"50 snt kolikoita {snt50} kpl")

# Määritän sentin loput
senttia -= snt50 * 50

# Toistan operaation jokaiselle sentin nimellisarvolle
snt20 = senttia // 20
senttia -= snt20 * 20
print(f"20 snt kolikoita {snt20} kpl")

snt10 = senttia // 10
senttia -= snt10 * 10
print(f"10 snt kolikoita {snt10} kpl")

snt5 = senttia // 5
senttia -= snt5 * 5
print(f"5 snt kolikoita {snt5} kpl")

snt2 = senttia // 2
senttia -= snt2 * 2
print(f"2 snt kolikoita {snt2} kpl")
print(f"1 snt kolikoita {senttia} kpl")

# Koodi voidaan muuntaa for-silmukaksi
