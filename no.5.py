import random

def is_valid_choice(choice):
  return choice.lower() in ['rock', 'paper', 'scissors']

def get_user_choice():
  while True:
    choice = input("Enter your choice (rock, paper, scissors): ")
    if is_valid_choice(choice):
      return choice.lower()
    else:
      print("Invalid choice. Please try again.")

def get_computer_choice():
  choices = ['rock', 'paper', 'scissors']
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Tie"
  elif user_choice == 'rock':
    if computer_choice == 'scissors':
      return "User"
    else:
      return "Computer"
  elif user_choice == 'paper':
    if computer_choice == 'rock':
      return "User"
    else:
      return "Computer"
  else: # user_choice == 'scissors'
    if computer_choice == 'paper':
      return "User"
    else:
      return "Computer"

def play_game():
  user_score = 0
  computer_score = 0
  rounds_played = 0

  while user_score < 2 and computer_score < 2:
    rounds_played += 1
    print(f"\n--- Round {rounds_played} ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    winner = determine_winner(user_choice, computer_choice)

    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    if winner == "User":
      user_score += 1
      print("You win this round!")
    elif winner == "Computer":
      computer_score += 1
      print("Computer wins this round!")
    else:
      print("It's a tie!")

  if user_score == 2:
    print("\nYou win the game!")
  else:
    print("\nComputer wins the game!")

# Start the game
play_game()
