def display_board(board):
  """Displays the current state of the tic-tac-toe board."""
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()

def is_valid_move(board, row, col):
  """Checks if a move is valid (empty space on the board)."""
  return board[row][col] == ' '

def make_move(board, player, row, col):
  """Places the player's mark on the board."""
  board[row][col] = player

def is_winner(board, player):
  """Checks if a player has won horizontally, vertically, or diagonally."""
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True
  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  # Check diagonals
  if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
    return True
  return False

def is_board_full(board):
  """Checks if all cells on the board are filled."""
  return all(cell != ' ' for row in board for cell in row)

def get_player_move(board, player):
  """Prompts the player for a valid move."""
  while True:
    try:
      row = int(input(f"{player}'s turn. Enter row number (1-3): ")) - 1
      col = int(input(f"{player}'s turn. Enter column number (1-3): ")) - 1
      if 0 <= row <= 2 and 0 <= col <= 2 and is_valid_move(board, row, col):
        return row, col
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter numbers only.")

def play_game():
  """Manages the tic-tac-toe game loop."""
  board = [[' ' for _ in range(3)] for _ in range(3)]
  player1_name = input("Enter player 1 name: ")
  player2_name = input("Enter player 2 name: ")
  current_player = player1_name

  while True:
    display_board(board)
    row, col = get_player_move(board, current_player)
    make_move(board, current_player[0], row, col)

    if is_winner(board, current_player[0]):
      display_board(board)
      print(f"{current_player} wins!")
      break
    elif is_board_full(board):
      display_board(board)
      print("It's a tie!")
      break

    current_player = player2_name if current_player == player1_name else player1_name

# Start the game
play_game()
