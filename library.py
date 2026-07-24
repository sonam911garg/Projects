import json

x = []
while True:
    a = input("Title? ")
    if a == "done":
        break
    y = input("Author? ")
    b = input("Returned, y/n? ")
    x.append({"title": a, "author": y, "returned": b})


print(x)

with open("library.json", "w") as f:
    json.dump(x,f)

    
with open("library.json", "r") as f:
    print(f.read())