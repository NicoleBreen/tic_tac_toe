import os
import random 

# Display the board
def display_board(board):
    # Fresh board after every turn
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display the Tic-Tac-Toe board
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

# Player marker choice
def player_input():
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, please choose either X or O: ')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f'Great! Player 1 is {player1} and Player 2 is {player2}')

    return player1, player2

# use random module to decide which player goes first
def choose_first():
    first_player = random.randint(1,2)

    if first_player == 1:
        return "A random choice has selected that Player 1 goes first!"
    else:
        return "A random choice has selected that Player 2 goes first!"
    
def space_check(board, position):
    pass

def full_board_check(board):
    pass

def player_choice(board):
    pass

# Place a marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# Define winning combinations and check if player has won
def win_check(board, mark):
    winning_combinations = [
        [1, 2, 3],  # Top row
        [4, 5, 6],  # Middle row
        [7, 8, 9],  # Bottom row
        [1, 4, 7],  # Left column
        [2, 5, 8],  # Middle column
        [3, 6, 9],  # Right column
        [1, 5, 9],  # Diagonal from top-left to bottom-right
        [3, 5, 7]   # Diagonal from top-right to bottom-left
    ]
    # Check each winning combination
    for combo in winning_combinations:
        if board[combo[0]] == mark and board[combo[1]] == mark and board[combo[2]] == mark:
            return True  
    
    return False  

def replay():
    pass

# Main game flow
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
print(RED + 'Welcome to Tic Tac Toe!' + RESET) # Welcome message

player1, player2 = player_input()  # Get player markers
first_player_message = choose_first()  # Determine who goes first
print(first_player_message)

final_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(final_board) # Display the board

# Example of placing a marker (this should be inside a game loop later)
#place_marker(final_board, player1, 5)  # Just a placeholder for player 1's turn
#display_board(final_board)