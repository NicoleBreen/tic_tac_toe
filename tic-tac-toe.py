import os

def display_board(board):
    # Fresh board after every turn
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display the Tic-Tac-Toe board
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

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

def place_marker(board, marker, position):
    board[position] = marker

# Test board
final_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(final_board)
place_marker(final_board, 'O', 5)
display_board(final_board)

