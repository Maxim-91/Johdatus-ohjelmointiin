# Teen tilavuuslaskuri
import functions as f

# While-operaattori: Aja ohjelmaa kunnes käyttäjä ei halua enää jatkaa (valitsemalla vaihtoehdon 0)
while True:
    print("Tilavuuslaskuri:\n"
            "1 = Laatikko\n"
            "2 = Pallo\n"
            "3 = Putki\n"
            "0 = Lopeta\n")

    # Pyydä aluksi käyttäjältä numero
    choice = input("Valitse toimenpide (1-3), 0 lopettaa ohjelman:\n")

    # 1 = laatikon tilavuus, funktio: box_volume(width, height, depth)
    if choice == "1":
        width = float(input("Anna laatikon leveys:\n"))
        height = float(input("Anna laatikon korkeus:\n"))
        depth = float(input("Anna laatikon syvyys:\n"))
        print(f"Laatikon tilavuus: {f.box_volume(width, height, depth)} m3\n")

    # 2 = pallon tilavuus, funktio: ball_volume(radius)
    elif choice == "2":
        radius = float(input("Anna pallon säde:\n"))
        print(f"Pallon tilavuus: {f.ball_volume(radius)} m3\n")

    # 3 = putken tilavuus, funktio: pipe_volume(radius, length)
    elif choice == "3":
        radius = float(input("Anna putken säde:\n"))
        length = float(input("Anna putken pituus:\n"))
        print(f"Putken tilavuus: {f.pipe_volume(radius, length)} m3\n")

    # 0 = Lopeta
    elif choice == "0":
        print("Kiitos ohjelman käytöstä!")
        break

    # Virhe
    else:
        print("Virheellinen valinta, yritä uudelleen.")
