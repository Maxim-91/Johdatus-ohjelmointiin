# Teen ohjelma, jossa on lista nimeltä inventory,
# joka koostuu muista listoista (fruits, berries ja vegetables)
fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

inventory = [fruits, berries, vegetables]

# Tulosta inventory-listan sisältö allekkain käyttäen silmukkaa,
# jonka sisällä on toinen silmukka.
for x in inventory:
    for y in x:
        print(y)
