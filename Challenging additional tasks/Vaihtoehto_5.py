# Vaihtoehto 5: Excel-graafityökalu

# Teen ohjelma, joka lukee Excelin käyttämää tietomuotoa .xlsx, ja tekee sen pohjalta palkki- , piste-
# tai viivadiagrammin käyttämällä jotain Pythonin lisämoduuleista, kuten Matplotlib, Seaborn, Plotly tai Bokeh.
# Jos löydät jonkin muun moduulin joka soveltuu tähän, voit käyttää myös sitä.

import pandas as pd
import matplotlib.pyplot as plt

df = None

# Yritetään lukea oletustiedosto
try:
    df = pd.read_excel("data.xlsx")
except FileNotFoundError:
    print("Tiedostoa 'data.xlsx' ei löytynyt ohjelmakansiossa.")
    filepath = input("Anna Excel-tiedoston polku (esim. 'C:\\Documents\\tiedosto.xlsx'):\n")

    # Yritä lukea polkutiedosto käyttäjältä
    try:
        df = pd.read_excel(filepath)
    except Exception as e:
        print("Virhe tiedoston latauksessa:\n", e)

# Jos df saatiin ladattua
if df is not None:
    print(df) # Tulostetaan taulukko (DataFrame) konsoliin

    # Luodaan uusi kuva (figuuri) koolla 10x6 tuumaa
    plt.figure(figsize=(10, 6))

    # Piirretään pylväsdiagrammi käyttäen sarakkeita 'Name' (x-akseli) ja 'Salary' (y-akseli)
    plt.bar(df['Name'], df['Salary'], color='skyblue')

    # Asetetaan kaaviolle otsikko
    plt.title("Palkkadiagrammi työntekijöiden palkoista")

    # Asetetaan x-akselille nimi "Nimi"
    plt.xlabel("Nimi")

    # Asetetaan y-akselille nimi "Palkka (€)"
    plt.ylabel("Palkka (€)")

    # Käännetään x-akselin nimilaput 45 asteen kulmaan, jotta ne näkyvät paremmin
    plt.xticks(rotation=45)

    # Sovitetaan kaavion osat niin, että mikään ei leikkaannu
    plt.tight_layout()

    # Näytetään kaavio ruudulla
    plt.show()
else:
    print("Ohjelma lopetetaan, koska tietoja ei voitu lukea.")
