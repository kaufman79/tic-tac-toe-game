# prompt: create a simple game

import random

# Define the game board
board = [" "] * 9

# Define the players
player1 = "X"
player2 = "O"

# Function to print the game board
def print_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# Function to check if a player has won
def check_win(player):
  winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ]

  for combination in winning_combinations:
    if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player:
      return True

  return False

# Function to get the player's move
def get_move(player):
  while True:
    try:
      move = int(input(f"{player}'s turn. Enter a number from 1 to 9: "))
      if 1 <= move <= 9 and board[move - 1] == " ":
        return move - 1
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Enter a number.")

# Main game loop
while True:
  # Print the game board
  print_board()

  # Get player 1's move
  move = get_move(player1)
  board[move] = player1

  # Check if player 1 has won
  if check_win(player1):
    print(f"{player1} wins!")
    break

  # Check if the board is full
  if all(square != " " for square in board):
    print("It's a tie!")
    break

  # Get player 2's move
  move = get_move(player2)
  board[move] = player2

  # Check if player 2 has won
  if check_win(player2):
    print(f"{player2} wins!")
    break
