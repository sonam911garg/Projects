expenses = []


def add_expense():
    while True:
        amount = input("Amount? (or type 'done' to finish): ")

        if amount == "done":
            break

        amount = int(amount)
        category = input("Category? ")
        description = input("Description? ")

        expenses.append({
            "Amount": amount,
            "Category": category,
            "Description": description
        })


def view_expense():
    print("\nExpenses:\n")

    for index, expense in enumerate(expenses, start=1):
        print(f"Expense {index}")
        print(f"Amount: {expense['Amount']}")
        print(f"Category: {expense['Category']}")
        print(f"Description: {expense['Description']}")
        print()


def delete_expense():
    number = int(input("Which expense do you want to delete? "))
    del expenses[number - 1]


def edit_expense():
    number = int(input("Which expense do you want to edit? "))

    field = input("What do you want to edit? (Amount/Category/Description): ")

    if field == "Amount":
        expenses[number - 1]["Amount"] = int(input("New amount: "))

    elif field == "Category":
        expenses[number - 1]["Category"] = input("New category: ")

    elif field == "Description":
        expenses[number - 1]["Description"] = input("New description: ")


def search_expense():
    search = input("Search category: ").lower()

    found = False

    for expense in expenses:
        if expense["Category"].lower() == search:
            print(expense)
            found = True

    if not found:
        print("No expense found")


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["Amount"]

    print("Total:", total)


def sort_expense():
    expenses.sort(
        key=lambda expense: expense["Amount"],
        reverse=True
    )

    print(expenses)


def average_expense():
    total = 0
    count = 0

    for expense in expenses:
        total += expense["Amount"]
        count += 1

    print("Average:", total / count)


def category_report():

    category_total = {}

    for expense in expenses:
        category = expense["Category"]

        if category in category_total:
            category_total[category] += expense["Amount"]
        else:
            category_total[category] = expense["Amount"]

    print(category_total)


def highest_category():

    category_total = {}

    for expense in expenses:
        category = expense["Category"]

        if category in category_total:
            category_total[category] += expense["Amount"]
        else:
            category_total[category] = expense["Amount"]

    highest = 0
    name = None

    for category in category_total:
        if category_total[category] > highest:
            highest = category_total[category]
            name = category

    print("Highest spending category:", name, highest)



while True:

    print("""
Expense Tracker

1. Add Expense
2. View Expense
3. Delete Expense
4. Edit Expense
5. Search Expense
6. Total Expense
7. Sort Expense
8. Average Expense
9. Category Report
10. Highest Category
11. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        edit_expense()

    elif choice == "5":
        search_expense()

    elif choice == "6":
        total_expense()

    elif choice == "7":
        sort_expense()

    elif choice == "8":
        average_expense()

    elif choice == "9":
        category_report()

    elif choice == "10":
        highest_category()

    elif choice == "11":
        break

    else:
        print("Invalid choice")