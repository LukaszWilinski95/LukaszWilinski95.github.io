# from IPython.display import clear_output  - Use this for Jupyter

# Board design with clear_output at the beginning to clear previous games
def display_board(board):
    print('\n' * 100)  # or clear_output() if Jupyter
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# Defining players input (marker)
# First player chooses, second player gets remaining marker
def players_input():
    marker = ''
    # Keep asking Player 1 to select marker until valid marker (X or O) is selected
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, please choose if your marker is X or O: ').upper()
    # Assign markers to players based on Player 1's choice
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Updating state of the board by placing marker
def place_marker(board, marker, position):
    board[position] = marker


# Ensuring the input is in valid range and position is available - not already occupied by another marker
def player_choice(board):
    position = 0
    # Keep asking the player until a valid position (1-9) is selected
    while True:
        position_input = input('Choose your next position: (1-9) ')
        # Check if input is a digit
        if position_input.isdigit():
            # Convert input to integer
            position = int(position_input)
            # Check if the position is withing the range and available on the board
            if position in range(1, 10) and space_check(board, position):
                break
            else:
                print('Incorrect position! Please choose a number between 1 and 9.')
        else:
            print('Incorrect position! Please enter a number between 1 and 9.')
    return position


# Checking if specific position is empty or not
def space_check(board, position):
    return board[position] == ' '


# Checking if player with specified marker has won by veryfing all winning combinations on board - rows, columns, diagonals
def check_win(board, marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or  # Row 1
            (board[4] == marker and board[5] == marker and board[6] == marker) or  # Row 2
            (board[1] == marker and board[2] == marker and board[3] == marker) or  # Row 3
            (board[7] == marker and board[4] == marker and board[1] == marker) or  # Column 1
            (board[8] == marker and board[5] == marker and board[2] == marker) or  # Column 2
            (board[9] == marker and board[6] == marker and board[3] == marker) or  # Column 3
            (board[7] == marker and board[5] == marker and board[3] == marker) or  # Diagonal 1
            (board[9] == marker and board[5] == marker and board[1] == marker))  # Diagonal 2


# Checking if the game has ended in a tie - all positions on a board are filled with markers and no winning combinations provided
def check_tie(board):
    return ' ' not in board[1:]


# Main function of Tic Tac Toe game,
def tic_tac_toe():
    # Start the game board with empty spaces
    board = [' '] * 10
    # Selection of the marker
    player1_marker, player2_marker = players_input()
    # Set the marker for the current player to Player 1's marker initially
    current_marker = player1_marker

    # Main game loop
    while True:
        display_board(board)
        position = player_choice(board)
        place_marker(board, current_marker, position)
        # Check if the current player has won the game
        if check_win(board, current_marker):
            # Display the final state of the board
            display_board(board)
            # Announce the winner and exit the game loop
            print(f'Player with marker {current_marker} wins!')
            break
        elif check_tie(board):
            display_board(board)
            print('The game is a tie!')
            break
        # Switch to the other player's turn
        if current_marker == player1_marker:
            current_marker = player2_marker
        else:
            current_marker = player1_marker


tic_tac_toe()