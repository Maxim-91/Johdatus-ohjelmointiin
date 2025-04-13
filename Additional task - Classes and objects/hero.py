# Lisätehtävä - Luokat ja oliot

# Lisätehtävä 2:
# Teen luokka, joka koostuu muista luokista.
#
# Teen Hero-luokka, jolla on
#  Name (string)
#  Character Class (string) vaihtoehdot: Warrior / Mage / Thief
#  Level (int)
#  Equipment (lista/dictionary)

class Hero:
    def __init__(self, name, character_class, level, equipment=None):
        self.name = name
        self.character_class = character_class  # Warrior / Mage / Thief
        self.level = level
        self.equipment = equipment if equipment is not None else {}

    def print_info(self):
        print(f"Hero: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print("Equipment:")
        for item in self.equipment.values():
            item.print_info()

# Ten lisäksi Equipment –luokka:
#  Name (string)
#  Equipment Type (string) – vaihtoehdot: Weapon / Armor / Accessory
#  Minimum Damage (int)
#  Maximum Damage (int)
#  Armor Rating (int)

class Equipment:
    def __init__(self, name, equipment_type, min_damage=0, max_damage=0, armor_rating=0):
        self.name = name
        self.equipment_type = equipment_type  # Weapon / Armor / Accessory
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.armor_rating = armor_rating

    def print_info(self):
        print(f"{self.equipment_type}: {self.name}")
        print(f"  Damage: {self.min_damage} - {self.max_damage}")
        print(f"  Armor Rating: {self.armor_rating}")
