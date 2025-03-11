# 8. Pillow -moduulin käyttäminen työkaluna

# Tee ohjelma, joka käsittelee kansiollisen JPG-kuvia siten,
# että kaikki kuvat muutetaan mustavalkoisiksi kerralla toiseen kansioon.
#
# Huom: Ota erilliset kopiot kuvista joita käytät tässä ohjelmassa,
# värien poistamisen jälkeen värejä ei voi enää palauttaa!

import os
from PIL import Image

input_folder = 'pic_exercise8_8/input'
output_folder = 'pic_exercise8_8/output'

# Luo tuloskansio, jos sitä ei ole olemassa
os.makedirs(output_folder, exist_ok=True)

# Kuvan muuntaminen
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        img = Image.open(os.path.join(input_folder, filename))
        img.convert('L').save(os.path.join(output_folder, filename))
