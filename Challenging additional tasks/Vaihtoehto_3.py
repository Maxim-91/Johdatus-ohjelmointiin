# Vaihtoehto 3: Tekstiruudukot
# Toteuta ohjelma, joka sisältää funktion (joka voi koostua muista funktioista),
# ja joka tulostaa seuraavanlaisia tekstimuotoisia taulukoita
#
# + - - - + - - - + - - - + - - - +
# |       |       |       |       |
# |       |       |       |       |
# + - - - + - - - + - - - + - - - +
# |       |       |       |       |
# |       |       |       |       |
# + - - - + - - - + - - - + - - - +
# |       |       |       |       |
# |       |       |       |       |
# + - - - + - - - + - - - + - - - +
#
# Pyydä ohjelman alussa käyttäjältä kaksi tietoa: rivien ja sarakkaiden lukumäärä.
# Yllä oleva esimerkki olisi lopputulos siinä tapauksessa, jos käyttäjä syöttäisi 3 ja 4.

# Taulukon yläosa - malli
def top_btm (top):
    print('+ - - - ' * top + '+')

# Taulukon puolella - malli
def wall_side (wall):
    print('|       ' * wall + '|')
    print('|       ' * wall + '|')

# Taulukon piirtäminen kahdella mallilla
def draw_grid(rows, columns):
    for i in range(rows):
        top_btm(columns)
        wall_side(columns)
    top_btm(columns)  # Viimeinen rivi on erotin

try:
    rows = int(input("Anna rivien lukumäärä:\n"))
    columns = int(input("Anna sarakkeiden lukumäärä:\n"))
    draw_grid(rows, columns)
except ValueError:
    print("Syötäthän kokonaisluvun.")
