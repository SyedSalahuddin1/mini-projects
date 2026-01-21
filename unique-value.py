unique_numbers = set()

while True:
    user_input = input("Please enter a number: ")
    
    if user_input == "q":
        print("\tCounter Exited!")
        break
    
    if user_input.isdigit():
        number = int(user_input)
        unique_numbers.add(number)
        print(unique_numbers)
        # print(sorted(unique_numbers))
    else:
        print("Please enter a valid number or 'q' to quit.")
            
print("\n === Unique Values Summary ===")
print(f"Unique Values: {unique_numbers}")
print(f"Count of Unique Values: {len(unique_numbers)}")
