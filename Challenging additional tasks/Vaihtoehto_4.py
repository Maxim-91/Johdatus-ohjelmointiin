# Vaihtoehto 4: Pokerikäden tarkistusohjelma

# Tee ohjelma, jolle voi syöttää viiden pelikortin arvot ja joka ilmoittaa täyttääkö kyseisten korttien muodostama korttikäsi
# värisuoran,
# suoran,
# täyskäden,
# värin,
# kolmosten,
# kahden parin
# tai parin vaatimukset
# Jos kortit muodostavat useita käsiä, tulostetaan korkein käsi.
# Jos mikään vaatimuksista ei toteudu, tulostetaan, mikä on suurimman kortin arvo

print("Risti on C (clubs), pata S (spades), ruutu D (diamonds) ja hertta H (hearts).\n"+
        "Korttien arvot merkitään seuraavasti: 2, 3, 4, 5, 6, 7, 8, 9, 10, jätkä J (jack), rouva Q (queen), kuningas K (king) ja ässä A (ace).\n"+
        "Eli esimerkiksi hertta kakkonen on H2 ja risti kuningas on CK.\n\n"
        "Esimerkkejä ohjelman toiminnasta:\n"+
        "Syötä kortit: H5 c8 s9 h7 D6\n"+
        "Kortit muodostavat suoran.\n"+
        "TAI\n"+
        "Syötä kortit: H5 c8 S2 h7 CA\n"+
        "Suurin kortti on ässä.\n")

# Muutetaan kortin merkkijonon puvuksi ja numeeriseksi arvoksi
def parse_card(card):
    suit = card[0].upper() # Korttipuku (H, D, C, S)
    value = card[1:].upper() # Kortin merkitys: numero tai kirjain (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
    value_map = {
                 "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                 "7": 7, "8": 8, "9": 9, "10": 10,
                 "J": 11, "Q": 12, "K": 13, "A": 14
                }
    return suit, value_map[value]

# Värin tarkistus
def is_flush(suits):
    return all(s == suits[0] for s in suits)

# Tarkistaa, muodostavatko arvot suoran, mukaan lukien erikoistapauksen A-2-3-4-5
def is_straight(values):
    values = sorted(set(values))
    if len(values) != 5:
        return False

    # Tarkastetaan normaalit ja "pienet" (A-2-3-4-5) suorat viivat
    return values[-1] - values[0] == 4 or values == [2, 3, 4, 5, 14]

def classify_hand(cards):
    suits = []
    values = []
    for card in cards:
        suit, value = parse_card(card)  # Muutetaan kortin merkkijonon puvuksi ja numeeriseksi arvoksi
        suits.append(suit)
        values.append(value)

    value_counts = {v: values.count(v) for v in set(values)}
    count_values = sorted(value_counts.values(), reverse=True)

    flush = is_flush(suits)  # Värin tarkistus
    straight = is_straight(values)  # Tarkistaa, muodostavatko arvot suoran, mukaan lukien erikoistapauksen A-2-3-4-5

    # Tarkistaminen vahvimmasta korttiyhdistelmästä heikoimpaan
    if flush and straight:
        return "Kortit muodostavat värisuoran."
    elif 4 in count_values:
        return "Kortit muodostavat neloset."
    elif 3 in count_values and 2 in count_values:
        return "Kortit muodostavat täyskäden."
    elif flush:
        return "Kortit muodostavat värin."
    elif straight:
        return "Kortit muodostavat suoran."
    elif 3 in count_values:
        return "Kortit muodostavat kolmoset."
    elif count_values.count(2) == 2:
        return "Kortit muodostavat kaksi paria."
    elif 2 in count_values:
        return "Kortit muodostavat parin."
    else:
        # Mikä on suurimman kortin arvo.
        max_val = max(values)
        reverse_value_map = {11: "jätkä", 12: "rouva", 13: "kuningas", 14: "ässä"}
        max_card = reverse_value_map.get(max_val, str(max_val))
        return f"Suurin kortti on {max_card}."

# Kysyn käyttäjältä ja tulostan funktioiden työn tuloksen
cards = input("Syötä kortit:\n").split()
if len(cards) != 5:
    print("Syötä täsmälleen viisi korttia.")
else:
    result = classify_hand(cards)
    print(result)
