
def corf(z):
    x = input("C or F? ")
    y = x.lower()
    if y == "c":
        a = (z * 9/5) + 32
        return a
        
    elif y == "f":
        b = (z - 32) * 5/9
        return b

print(corf(54))



