import json
x = []

while True:
    movie = input("movie")
    if movie == "exit":
             break
    
    genre = input("genre")
    watched = input("watched y or n? ")

    x.append({"movie": movie, "genre": genre, "watched": watched})
    
with open("movie.json", "w") as f:
         json.dump(x,f)

with open("movie.json", "r") as f:
         print(f.read())

