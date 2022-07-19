# Battle Ship

# Imports randint funciton from random module
from random import randint

# Creates a 5x5 board to play on
board = []

for i in range(5):
  board.append(["O"] * 5)

# Joins the board for a cleaner UI [0,0,0,0,0] changed to [0 0 0 0 0]
def print_board(board_in):
  for row in board:
    print (" ".join(row))
# Creates a two random variables for ship position on game board
def random_row(board_in):
  return randint(0, len(board_in) - 1)
def random_col(board_in):
  return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# This will print the varibles to be seen when playing the game
"""print(ship_row)
print(ship_col)
"""
# Main function of game.  Ask user to guess four times.  The user can win, guess out of range or miss the ship.  Once the user guesses 4 times the game ends.
for turn in range(4):
  print('Turn', turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    elif (board[guess_row][guess_col] == 'X'):
      print('You guessed that one already.')
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if turn == 3:
      print('Game Over, Thank you for playing!')
  
    print_board(board)