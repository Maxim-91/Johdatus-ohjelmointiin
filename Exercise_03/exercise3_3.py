# Käyttäjän viikon työtuntimäärän ja tuntipalkan
tyotuntia = float(input("Syötä viikon työtunnit: \n"))
tuntipalkkaa = float(input("Syötä tuntipalkkasi: \n"))

# Palkan laskeminen ylitöitä läsnä ollessa
if tyotuntia > 40:
    ylituntia = tyotuntia - 40
    palkka = 40 * tuntipalkkaa + ylituntia * tuntipalkkaa * 1.5
else:
    palkka = tyotuntia * tuntipalkkaa

print(f"Viikon ansiosi avat: {palkka:.2f}€")
