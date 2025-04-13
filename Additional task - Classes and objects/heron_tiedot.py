# Lisätehtävä - Luokat ja oliot
# Lisätehtävä 2
from hero import Hero, Equipment

# Teen Python-ohjelma, joka näyttää yhden Heron kaikki tiedot sekä listan myös varusteista, sekä niiden ominaisuuksista.
# Herolla voi kerrallaan olla vain yksi ase (Weapon), suoja (Armor) sekä lisäväline (Accessory) käytössään.
# Voit hyödyntää Coloramaa lopputuloksen värittämiseksi!
from colorama import Fore, Style

# Varusteita
sword = Equipment("Excalibur", "Weapon", 10, 20)
armor = Equipment("Dragon Scale Mail", "Armor", armor_rating=15)
ring = Equipment("Ring of Speed", "Accessory", min_damage=1, max_damage=3)

# Laitan varusteet dictionaryyn
equipment_set = {
    "Weapon": sword,
    "Armor": armor,
    "Accessory": ring
}

# Sankari
hero = Hero("Arthas", "Warrior", 5, equipment_set)

# Tulos + Colorama
print(Fore.BLUE + Style.BRIGHT + f"Hero: {hero.name}")
print(Fore.CYAN + f"Class: {hero.character_class}")
print(Fore.YELLOW + f"Level: {hero.level}")
print(Fore.WHITE + Style.BRIGHT + "Equipment:")

for item in hero.equipment.values():
    if item.equipment_type == "Weapon":
        color = Fore.RED + Style.BRIGHT
    elif item.equipment_type == "Armor":
        color = Fore.GREEN + Style.BRIGHT
    elif item.equipment_type == "Accessory":
        color = Fore.MAGENTA + Style.BRIGHT
    else:
        color = Fore.WHITE

    print(color + f"{item.equipment_type}: {item.name}")
    print(color + f"  Damage: {item.min_damage} - {item.max_damage}")
    print(color + f"  Armor Rating: {item.armor_rating}")
