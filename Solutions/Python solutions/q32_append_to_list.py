def add_expense():
    expenses = [1000, 2000, 1500]
    new_expense = 500

    if new_expense <= 0:
        print("Invalid expense")
        return

    expenses.append(new_expense)
    print("Updated Expenses:", expenses)

add_expense()