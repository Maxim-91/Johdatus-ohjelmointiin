# Lisätehtävä - Luokat ja oliot

# Teen tähän tiedostoon luokka nimeltä Product.
#
# Product –luokassa tulee olla seuraavat jäsenmuuttujat:
#  id (int), oletusarvo -1
#  name (string), oletusarvo "Nimi puuttuu"
#  category (string), oletusarvo "Muut"
#  price (float), oletusarvo 0.0
#  campaign (boolean), oletusarvo False

class Product:
    def __init__(self, id=-1, name="Nimi puuttuu", category="Muut", price=0.0, campaign=False):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.campaign = campaign

# Product –luokassa tulee olla metodi print_info(), joka tulostaa kaikki tiedot tuotteesta siistinä kokonaisena tekstinä
# Kategoria: Tuotteen nimi (ID) – Hinta pyöristettynä yhteen desimaaliin + € -merkki (jos tarjoustuote, tulostetaan perään: [TARJOUSTUOTE])
# eli esim:
# Kodinkoneet: Mikroaaltouuni 123X (ID:15) – 99.0€
# tai
# Puhelimet: Nokia 3310 (ID:35) – 129€ [TARJOUSTUOTE]
    def print_info(self):
        price = self.get_price() # Pieni lisätehtävä
        price_text = f"{round(price, 1)}€"
        campaign_text = " [TARJOUSTUOTE]" if self.campaign else ""

        print(f"{self.category}: {self.name} (ID:{self.id}) – {price_text}{campaign_text}")

# Pieni lisätehtävä:
# Teen luokkaan myös metodi get_price(), joka antaa erikseen tuotteen hinnan.
# Jos campaign-boolean on True, silloin hinta on 10% pienempi
    def get_price(self):
        if self.campaign: # Jos campaign-boolean on True
            return self.price * 0.9 # Hinta on 10% pienempi
        return self.price
