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

# Use random module to decide which player goes first
def choose_first():
    first_player = random.randint(1,2)

    if first_player == 1:
        return "A random choice has selected that Player 1 goes first!"
    else:
        return "A random choice has selected that Player 2 goes first!"

# Returns a boolean indicating whether a space on board is available.    
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

# Checks if board is full and returns a boolean
def full_board_check(board):
    return ' ' not in board[1:]

# Asks for players next position and then checks if it available with space_check()
def player_choice(board):
    position = 'WRONG'
    acceptable_range = range(1,10)
    within_range = False

    while position.isdigit() == False or within_range == False:
        position = input ("Please choose a numerical position (1-9): ")
        if position.isdigit() == False:
            print("Sorry, you must enter a digit")
        if position.isdigit() == True:
            if int(position) in acceptable_range:
                within_range = True
                if not space_check(board, int(position)):
                    print("Sorry, that position is already taken. Try again.")
                    within_range = False
            else:
                print("Sorry, that is not a valid position (1-9)")
                within_range = False

    return int(position)

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

# Asks user if they want to replay, sets to True if yes
def replay():
    again = input ("Would you like to play again? Enter Yes or No: ").lower()
    return again == 'yes'

# main game flow
while True:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    print(RED + 'Welcome to Tic Tac Toe!' + RESET)  # Welcome message

    # Get player markers (Player 1 and Player 2)
    player1, player2 = player_input()  
    
    # Randomly choose which player goes first
    first_player = choose_first()  
    print(first_player)

    # Initialize the game board
    final_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(final_board)  # Display the initial empty board

    # Set game variables
    game_on = True
    turn = "Player 1" if first_player == "Player 1 goes first!" else "Player 2"

    while game_on:
        # Player 1's turn
        if turn == "Player 1":
            print("Player 1's turn!")
            position = player_choice(final_board)  
            place_marker(final_board, player1, position) 
            display_board(final_board)  

            # Check if Player 1 wins
            if win_check(final_board, player1):
                print(GREEN + "Player 1 has won!" + RESET)
                game_on = False  
            elif full_board_check(final_board):
                print("It's a tie!")
                game_on = False
            else:
                turn = "Player 2" 
            
        # Player 2's turn
        else:
            print("Player 2's turn!")
            position = player_choice(final_board)  
            place_marker(final_board, player2, position) 
            display_board(final_board) 

            # Check if Player 2 wins
            if win_check(final_board, player2):
                print(GREEN + "Player 2 has won!" + RESET)
                game_on = False  
            else:
                turn = "Player 1"  

   # After the game ends, ask if the players want to replay
    if not replay():
        print("Thanks for playing! Goodbye.")
        break  # Exits loop if players do not want to replay
