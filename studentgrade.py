import json

x = []
y = 0
count = 0

while True:
    a = input("name? ")
    if a == "done":
        break
    b = int(input("grade? "))
    y += b
    count +=1
    x.append({"name": a, "grade": b})

avg = y/count
print(count,y, avg)

with open("grade.json", "w") as f:
    json.dump(x, f)

with open("grade.json", "r") as f:
    print(f.read())