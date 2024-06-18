import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a random number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    
    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You've guessed the correct number ({secret_number}) in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Your guess is too low. Try again!")
            else:
                print("Your guess is too high. Try again!")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

# Run the game
number_guessing_game()
