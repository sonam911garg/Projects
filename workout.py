import json

x = []

while True:
    a = input("workout name? ")
    if a == "done":
        break
    b = input("sets? ")
    c = input("reps? ")
    x.append({"name": a, "sets": b, "reps": c})


print(x)

with open("workout.json", "w") as f:
    json.dump(x, f)
