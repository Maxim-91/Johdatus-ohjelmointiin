from PIL import Image, ImageDraw, ImageFont

# Pieni lisätehtävä: Vaihda tekstin perusfontti Arimoon, ja nosta sen koko 18 pisteeseen
try:
    font_arimo = ImageFont.truetype("arimo.ttf", 18)
except IOError:
    font_arimo = ImageFont.load_default()  # Jos fonttia ei löydy, käytetään oletusfonttia

# Lisätehtävä: Anna käyttäjän vaikuttaa kuvassa käytettäviin väreihin
varit = {
    1: "blue",
    2: "red",
    3: "green",
    4: "yellow",
    5: "white",
    6: "black",
    7: "violet",
    8: "orange"
}
print("Valitse väri numerolla: 1 = sininen, 2 = punainen, 3 = vihreä, 4 = keltainen, 5 = valkoinen, 6 = musta, 7 = violetti, 8 = oranssi")
try:
    tausta_vari = varit[int(input("Anna taustavärin numero: "))]
except (ValueError, KeyError):
    tausta_vari = "violet"
try:
    teksti_vari = varit[int(input("Anna tekstin värin numero: "))]
except (ValueError, KeyError):
    teksti_vari = "orange"
try:
    kolmio_vari = varit[int(input("Anna kolmion värin numero: "))]
except (ValueError, KeyError):
    kolmio_vari = "white"
try:
    ympyra_vari = varit[int(input("Anna ympyrän värin numero: "))]
except (ValueError, KeyError):
    ympyra_vari = "blue"

# Teen kuva, jonka koko on 500 x 300 ja jonka taustaväri on violetti
img = Image.new('RGB', (500, 300), color = tausta_vari)
d = ImageDraw.Draw(img)

# Pyydän myös käyttäjältä lause joka piirretään kuvan vasempaan alanurkkaan oranssilla värillä
lause = str(input("Anna lause:\n"))
d.text((50, 250), lause, font = font_arimo, fill = teksti_vari)

# Piirrä kuvaan myös valkoinen kolmio, jonka sisällä on sininen ympyrä!
d.polygon([(300, 250), (200, 100), (400, 100)], fill = kolmio_vari)
d.ellipse((245, 100, 355, 205), fill = ympyra_vari)

img.save("kuva.png")
img.show()
