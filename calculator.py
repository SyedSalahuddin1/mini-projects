def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by Zero"
    return a / b 

def modulo(a, b):
    return a % b 

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%":modulo
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a Valid number!")
            
def calculator():
    print("Welcome to Newly Designed Calculator!")
    num1 =get_number("Enter First number: ")

    while True:
        num2 = get_number("Enter Second number: ")
                
        operation = input("Please enter the operation you want to perform or 'q' to quit: ")
        
        if operation in operations:
            result = operations[operation](num1, num2)
        elif operation == "q":
            print("Calculator Closed!")
            break
        else:
            print("Invalid Operation")
            continue
        
        print(f"The result of the operation you selected is {result}!")
        continue_with_result = input("Do you want to continue with the result or start fresh (Type C or F or 'q' to quit): \n") 
        
        if continue_with_result == "c":
            num1 = result
        elif continue_with_result == "f":
            num1 = get_number("Enter First number: ")
        else:
            print("Calculator Closed!")
            break
    
if __name__ == "__main__":
    calculator()
    