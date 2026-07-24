import json
x = 0
a = 0
c = {}

while True:
    y = input("number? ")
    if y == "exit":
        break
    b = int(y)
    z = input("+ or -? ")
    
    if z == "+":
        x += b
    elif z == "-":
        x -= b
        a += b
        e = input("name? ")
        c[e] = b

with open("expense.json", "w") as f:
    json.dump(c, f)

print(x, a, c)