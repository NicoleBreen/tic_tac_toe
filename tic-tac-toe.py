import os

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

player_input()

# Test to see how placing a marker on the board would look
def place_marker(board, marker, position):
    board[position] = marker

final_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(final_board)
place_marker(final_board, 'O', 5)
display_board(final_board)

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