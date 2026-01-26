def get_int(prompt):
    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter only number")
            

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter only floating numbers")
            
def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


class ExpenseTracker():
    def __init__(self):
        self.expenses = []
        
    def add_expense(self):
        amount =  get_float("Enter amount: ")
        category = get_string("Enter category: ")
        note = get_string("Enter note: ")
        
        expense = {
            "amount": amount,
            "category": category,
            "note": note 
        }
        
        self.expenses.append(expense)



# def add_expenses(expenses):
    
#     num_of_expenses = get_int("Enter number of expense: ")
    
#     for i in range(num_of_expenses):
#         print(f"Expense {i+1}: ")
#         amount = get_float("Please enter the amount: ")
#         category = get_string("Enter the Category: ")
#         note = get_string("Enter the note: ")
        
#         bills = {
#             "amount": amount,
#             "category": category,
#             "note": note
#         }
        
#         expenses.append(bills)
        
#     # return expenses
    
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

        choice = get_int("Enter your choice (1-5): ")

        if choice == 1:
            add_expenses(expenses)

        elif choice == 2:
            view_expenses(expenses)

        elif choice == 3:
            total_expenses(expenses)

        elif choice == 4:
            category_expenses(expenses)

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

