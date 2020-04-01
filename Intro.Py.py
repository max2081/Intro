from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = input("Guess Row: ")
print guess_row
guess_col = input("Guess Col: ")
print guess_col

if guess_row == ship_row and guess_col == ship_row:
  print "Congratulation! You sank my battleship!"
else: print "Unlucky, Miss"