password = "123@Qaz"

attempts = 3

while attempts > 0:
    user_access = input("Please type in the correct Password or 'q' to quit: ")
    
    if user_access == password:
        print("User Acces Garuanteed, You're not a spam")
        break

    if user_access == 'q':
        print("Page Exited!")
        break
   
    attempts -= 1
    print(f"Wrong Password. {attempts} attempts left to Login!")
else:
    print(f"System Locked! You're a bot!")
        
    
       