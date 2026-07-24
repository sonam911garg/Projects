import random
import string
import json
import datetime
timestamp = str(datetime.datetime.now())
pool = string.ascii_letters + string.digits

x = int(input("how many characters? "))

y = "".join(random.choices(pool, k=x))

print(y)

with open("password.json", "w") as f:
    json.dump({"password": y, "timestamp": timestamp}, f)