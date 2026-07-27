for expense in x:
    print(expense)
x.sort(key=lambda expense: expense["Category"], reverse=False)

print(x)