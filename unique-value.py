unique_numbers = set()

while True:
    user_input = input("Please enter the numbers: ")
    
    if user_input.isdigit():
        number = int(user_input)
        unique_numbers.add(number)
        print(unique_numbers)
    else:
        print("Please enter a valid number or 'q' to quit: ")
    
    if user_input == 'q':
        print("\tCounter Exited!")
        break

print("\n === Unique Value Tracker ===")
print(f"Total Characters: {len(unique_numbers)}")
