import datetime
import json

z = []
while True:
    x = input("City name? ")
    if x == "done":
        break
    y = int(input("Temp? "))
    timestamp = str(datetime.datetime.now())
    z.append({"name": x, "temp":y, "timestamp": timestamp})



with open("weather.json", "w") as f:
    json.dump(z,f)
with open("weather.json", "r") as f:
    print(f.read())