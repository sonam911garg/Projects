import json
x = {}

while True:
    name = input("name? ")
    if name == "exit":
        break
    contact_number = int(input("number? "))
    x[name]= contact_number

print(x)

with open("contacht.json", "w") as f:
    json.dump(x,f)

with open("contacht.json", "r") as f:
    print(f.read())