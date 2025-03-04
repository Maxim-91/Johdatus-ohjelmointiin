# Pyydän käyttäjää syöttämään numeron tai numeron nimen numerona
text = str(input("Syötä numerot tai numeroiden nimet (enintään 5 numeroa):\n"))

if text.isnumeric():  # Käyttäjä syötti numeron
    if len(text) > 5:
        print("Yli 5 numeroa syötettiin")
    else:
        text = text.replace("0", "nolla ")
        text = text.replace("1", "yksi ")
        text = text.replace("2", "kaksi ")
        text = text.replace("3", "kolme ")
        text = text.replace("4", "neljä ")
        text = text.replace("5", "viisi ")
        text = text.replace("6", "kuusi ")
        text = text.replace("7", "seitsemän ")
        text = text.replace("8", "kahdeksan ")
        text = text.replace("9", "yhdeksän ")
        print(text)

elif text.replace(" ", "").isalpha():  # Käyttäjä syötti tekstinä
    sanoja = len(text.split())
    if sanoja > 5:
        print("Yli 5 numeroa syötettiin")
    else:
        text = text.replace("nolla", "0")
        text = text.replace("yksi", "1")
        text = text.replace("kaksi", "2")
        text = text.replace("kolme", "3")
        text = text.replace("neljä", "4")
        text = text.replace("viisi", "5")
        text = text.replace("kuusi", "6")
        text = text.replace("seitsemän", "7")
        text = text.replace("kahdeksan", "8")
        text = text.replace("yhdeksän", "9")
        text = text.replace(" ", "")
        print(text)
else:
    print("Virhe. Syötä vain numeroita tai numeroiden nimet.")
