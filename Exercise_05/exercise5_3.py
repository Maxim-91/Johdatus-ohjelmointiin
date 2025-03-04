import math

running = True
while running:
    # Kysyn käyttäjältä ympyrän säteen
    r = int(input("Anna säde:\n"))

    # Lasken ympyrän pinta-alan
    s = math.pi * r ** 2
    print(f"Ympyrän pinta-alan {s:.2f}")

    # Kysyn käyttäjältä haluaako jatkaa
    jatkaa = str(input("Haluatko jatkaa? (k/e)\n"))
    if jatkaa == "e":
        running = False
        