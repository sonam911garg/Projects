import random
import json

x = random.randint(1,100)
count = 0

while True:
    y = int(input("number? "))
    if y == x:
        print("you won")
        break
    elif y > x :
        print("too high")
    elif y < x:
        print("too low")
    count += 1

with open ("number_guess.json", "w") as f:
    json.dump({"Answer": x, "count": count}, f)

with open ("number_guess.json", "r") as f:
    print(f.read())
