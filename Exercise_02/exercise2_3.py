# Pyydä käyttäjäpalkka ja heidän veroprosenttinsa
palkka = float(input("Anna kuukausipalkkasi:\n"))
vero_prosentti = float(input("Anna veroprosenttisi:\n"))

# Nettopalkan ja veron määrän laskeminen
palkka_netto = palkka - palkka * (vero_prosentti / 100)
vero = palkka - palkka_netto

palkka_netto = round(palkka_netto, 2)
vero = round(vero, 2)

print(f"Käteenjäävä osuus: {palkka_netto} €\n"
      f"Verot: {vero} €\n") # Tulos