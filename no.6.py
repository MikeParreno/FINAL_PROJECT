import random

def roll_dice():
  return random.randint(1, 6)

def play_round():
  player1_roll = roll_dice()
  player2_roll = roll_dice()
  print(f"Player 1 rolled: {player1_roll}")
  print(f"Player 2 rolled: {player2_roll}")

  if player1_roll > player2_roll:
    return "Player 1"
  elif player1_roll < player2_roll:
    return "Player 2"
  else:
    return "Tie"

def play_game():
  player1_score = 0
  player2_score = 0
  rounds_played = 0

  while player1_score < 2 and player2_score < 2:
    rounds_played += 1
    print(f"\n--- Round {rounds_played} ---")
    winner = play_round()

    if winner == "Player 1":
      player1_score += 1
      print("Player 1 wins this round!")
    elif winner == "Player 2":
      player2_score += 1
      print("Player 2 wins this round!")
    else:
      print("It's a tie!")

  if player1_score == 2:
    print("\nPlayer 1 wins the game!")
  else:
    print("\nPlayer 2 wins the game!")

# Start the game
play_game()
