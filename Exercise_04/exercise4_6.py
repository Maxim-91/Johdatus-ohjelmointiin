# Kysyn käyttäjältä ulkolämpötila ja kosteusprosentti
lämpötila = float(input("Anna ulkolämpötila (°C):\n"))
kosteus = float(input("Anna kosteusprosentti (%):\n"))

# Teen ohjelmaasi Boolean-muuttujat:
freezing = False
heatwave = False
raining = False
hailstorm = False

# Jos annettu lämpötila on alle 0 astetta, aseta freezing-muuttuja todeksi.
if lämpötila < 0:
    freezing = True

# Jos kosteusprosentti on yli 80, aseta raining-muuttuja todeksi,
# paitsi jos pakkasta on yli 20 astetta,
# jolloin asetetaan sen sijaan hailstorm-muuttuja todeksi.
if kosteus > 80:
    if lämpötila < -20:
        hailstorm = True
    else:
        raining = True

# Jos lämpötila on yli 20 astetta, aseta heatwave-muuttuja todeksi.
if lämpötila > 20:
    heatwave = True

# Tulosta lopuksi annettu lämpötila.
# Jos freezing–muuttuja on tosi, tulosta ”Pakkasta.”.
if freezing:
    print("Pakkasta.")

# Jos raining–muuttuja on tosi, tulosta ”Sataa.”,
# ja jos hailstorm–muuttuja on tosi, tulosta ”Sataa rakeita!”.
if raining:
    print("Sataa.")
if hailstorm:
    print("Sataa rakeita!")

# Jos heatwave –muuttuja on tosi, tulosta ”Helleaalto!”.
if heatwave:
    print("Helleaalto!")

# Jos sataa ja on hellettä, tulosta ”Kosteaa ja tukalaa.”
if raining and heatwave:
    print("Kosteaa ja tukalaa.")
