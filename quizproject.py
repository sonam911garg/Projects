import json
x = {}

for i in range(1):
    ask1 = input("Bangalore state? ")
    ask2 = input("National Animal? ")
    ask3 = input("sky color? ")
    ask1 = ask1.lower()
    ask2 = ask2.lower()
    ask3 = ask3.lower()

    if ask1 == "karnataka" or ask1 == "kar":
        x[ask1] = "correct"
    else:
        x[ask1] = "incorrect"
    if ask2 == "tiger":
            x[ask2] = "correct"
    else:
          x[ask2] = "incorrect"
    if ask3 == "blue":
            x[ask3] = "correct"
    else:
         x[ask3] = "incorrect"


with open("quiz.json", "w") as f:
      json.dump(x,f)

with open("quiz.json", "r") as f:
      print(f.read())
