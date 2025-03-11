# Tehtävä: Tee ohjelmasi koodiin seuraavanlainen dictionary
cafe = { "name": "Imaginary Cafe Oy",
         "website": "https://edu.frostbit.fi/sites/cafe",
         "categories":
             [
                "cafe",
                "tea",
                "lunch",
                "breakfast"
             ],
         "location":
             {
                "city": "Rovaniemi",
                "address": "Testikuja 22",
                "zip_code": "96200"
             }
       }

# Tulosta dictionaryn sisältö alla olevan esimerkin mukaisesti.
# HUOM! Noudata kirjoitusasuja täsmällisesti!
print(cafe["name"])
print(cafe["location"]["address"])
print(cafe["location"]["zip_code"], cafe["location"]["city"])
print()
print(cafe["website"])
print("Palvelut:", ", ".join(cafe["categories"]))


