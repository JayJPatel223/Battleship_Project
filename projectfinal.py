from random import randint

# Set up the board
board_size = 5
board = [['O' for i in range(board_size)] for j in range(board_size)]
ship_row = randint(0, board_size - 1)
ship_col = randint(0, board_size - 1)

# Define function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Define function to check if a cell is valid
def is_valid(row, col):
    return row >= 0 and row < board_size and col >= 0 and col < board_size

# Define the main game loop
print()
print("The year was 3047, and after many years of extreme wars between Humans and AI, YOU are the last warrior standing against it, and only one battleship is left to destroy the AI power. YOUR job is to destroy the AI battleship and save the world before AI finishes you.")
print()
print("INSTRUCTION: Blast enemy's battleship by entering the values of rows and colums between 0 and 4")
print("# X is the missed position ")
print()
print("Battlefield during the start of the Game")
print_board(board)
print("")
for turn in range(25):
    print('Turn', turn+1)
    print("")
    
    # User's turn
    while True:
        try:
            guess_row = int(input('Guess Row (0-4): '))
            guess_col = int(input('Guess Col (0-4): '))
            print("")
            break
        except ValueError:
            print("Invalid input. Re-enter the values")
  
    if not is_valid(guess_row, guess_col):
        print('Oops, that\'s not even in the ocean.')
        
    elif board[guess_row][guess_col] == 'X' or board[guess_row][guess_col] == '*':
        print('Point already guessed.')
        print("Input new values.")
        
        while board[guess_row][guess_col] == 'X':
            guess_row = int(input('Guess Row (0-4): '))
            guess_col = int(input('Guess Col (0-4): '))
            print('Point already guessed.\n')
            print("Input New Values.\n")
            
            
    elif guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = '*'
        print()
        print_board(board)
        print()
        print("Congratulations! You sank AI's battleship!")
        print("You Won. You Saved the Human World.")
        break
    else:
        print('You missed AI battleship!')
        board[guess_row][guess_col] = 'X'
        print()
        print_board(board)
        print()

    # Computer's turn
    comp_guess_row = randint(0, board_size - 1)
    
    comp_guess_col = randint(0, board_size - 1)
   #comp guess row and column 
    print(f'AI guess is row {comp_guess_row} and column {comp_guess_col}')
    
    if board[comp_guess_row][comp_guess_col] == 'X' or board[comp_guess_row][comp_guess_col] == '*':
        print('This was already guessed.')
    elif comp_guess_row == ship_row and comp_guess_col == ship_col:
        board[comp_guess_row][comp_guess_col] = '*'
        print()
        print_board(board)
        print()
        print('Oh no! The AI sank your battleship!')
        print("You Lost!!, AI took over the Human World.")
        break
    else:
        print('The AI missed your battleship!')
        board[comp_guess_row][comp_guess_col] = 'X'
        print()
        print_board(board)
        print()

    if turn == 25:
        print('Game Over')
        print('The battleship was at row', ship_row, 'and column', ship_col)
        
