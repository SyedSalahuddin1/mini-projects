import random
secret = random.randint(1, 101)

attempts = 0

while True:

    guess = input("Please enter the number or 'q' to quit: ")
    attempts += 1
    
    if guess == 'q':
        print("Game Exited!")
        break
    
    guess = int(guess)
    if guess == secret:
        print(f"You guessed the correct number, The number was {secret}")
        print(f"You took {attempts} to guess the correct answer.")
        
        secret = random.randint(1, 101)
        attempts = 0
        print("\nNew Round Started! Guess the new 'Number'!")
        
    elif guess > secret:
        print(f"Too High, try Lower")
    elif guess < secret:
        print(f"Too Low, try Higher")
        