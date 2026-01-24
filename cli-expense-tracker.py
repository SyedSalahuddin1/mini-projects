expenses = [
    {
        "amount":1200, "category":"Food", "Note":"3 Times Food",
        "amount":800, "category":"Travel", "Note":"Petrol"
    }
]

def add_expenses(expenses):
    num_of_expenses = int(input("Please enter the amount of expenses: "))
    
    for i in range(num_of_expenses):
        print(f"Expense {i+1}: ")
        amount = float("Please enter the amount: ")
        category = input("Enter the Category: ")
        note = input("Enter the category: ")
        
        bills = {
            "amount": amount,
            "category": category,
            "note": note
        }
        
        expenses.append(bills)
        
    # return expenses
    
def view_expenses(expenses):
    if not expenses:
        print("No Expenses to Display")
        return 
    print("\n----All Expenses----")
    for i, expense in enumerate(expenses, 1):
        print(f"Expense {i}:")
        print(f"Amount: {expense['amount']}")
        print(f"Category: {expense['categroy']}")
        print(f"Note: {expense['note']}")
        
        
def total_expenses(expenses):
    if not expenses:
        print("No expenses to Display")
        return

    total = 0
    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expenses are {total}")
    return total

def category_expenses(expenses):
    if not expenses:
        print("No expenses to Display")
        return
    
    summary = {}
    
    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]
        
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
             
    print(f"\n----Category Summay----")
    for category, total in summary.items():
        print(f"{category}: {total}")
        
    return summary

def menu():
    expenses = []

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_expenses(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

