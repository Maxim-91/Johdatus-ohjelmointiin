# Teen ohjelma, jossa on seuraavanlainen lista, joka koostuu dictionaryistä (dict):
movie1 = {"name": "Komisario Palmun erehdys", "year": 1960}
movie2 = {"name": "Kauas pilvet karkaavat", "year": 1996}
movie3 = {"name": "Mies vailla menneisyyttä", "year": 2002}
movie4 = {"name": "Forrest Gump", "year": 1994}
movie5 = {"name": "The Devil Wears Prada", "year": 2006}
movie6 = {"name": "The Fifth Element", "year": 1997}
movie7 = {"name": "Alien", "year": 1979}

movies = [movie1, movie2, movie3, movie4, movie5, movie6, movie7]

# Jaottelen elokuvat kahteen uuteen eri listaan: 2000-luvun elokuviin, sekä sitä vanhempiin elokuviin
new_movies = []
old_movies = []
for movie in movies:
    if movie["year"] >= 2000:
        new_movies.append(movie["name"])
    else:
        old_movies.append(movie["name"])

# Tulostan näiden kahden listan sisältö alla olevan esimerkin mukaisesti
print("Seuraavat elokuvat on julkaistu 2000-luvulla:")
print(", ".join(new_movies))
print()
print("Seuraavat elokuvat on julkaistu ennen vuotta 2000:")
print(", ".join(old_movies))
