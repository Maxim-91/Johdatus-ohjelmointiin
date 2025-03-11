import tkinter as tk

root = tk.Tk()
root.title("tk")

# Luon staattista tekstiä
tk.Label(root, text="Luku 1").grid(row=0, column=0)
tk.Label(root, text="Luku 2").grid(row=1, column=0)
tk.Label(root, text="Luku 3").grid(row=2, column=0)
tk.Label(root, text="Tulos:").grid(row=4, column=0)

# Käyttäjän pitää pystyä syöttämään kolmeen eri tekstilaatikkoon eri numeroita,
# jota lasketaan yhteen mikäli käyttäjä painaa ”Näytä tulos” –nappi

# Luon syöteelementtejä
entry1 = tk.Entry(root, width=20)
entry2 = tk.Entry(root, width=20)
entry3 = tk.Entry(root, width=20)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

# Luon 2 painiketta
calc_button = tk.Button(root, text="Näytä tulos")
close_button = tk.Button(root, text="Sammuta ohjelma", command=root.quit)

close_button.grid(row=5, column=0)
calc_button.grid(row=5, column=1)

# Luon "Label" tuloksen näyttämiseksi
tulos_label = tk.Label(root)
tulos_label.grid(row=4, column=1)

# Käytetään try-except käsittelyä virheiden käsittelyyn
def calculate_sum():
    try:
        # Summaan tiedot kohdasta 3 "Entry" ja kirjoitan tuloksen "Label"
        result = int(entry1.get()) + int(entry2.get()) + int(entry3.get())
        tulos_label.config(text=result)
    except ValueError:
        tulos_label.config(text="Virhe! Syötä vain numeroita.")

# Suorita laskentatoiminto, kun painiketta painetaan
calc_button.config(command=calculate_sum)

# Aloitan GUI-tapahtumasilmukan sovelluksessa, joka käyttää tkinteriä.
root.mainloop()
