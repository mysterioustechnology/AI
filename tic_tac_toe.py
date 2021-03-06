def tic_tac_toe():
    """
    This program simulates the game of tic tac toe.
    """

    # get_valid_index
    # -----
    # Get row or column from user
    def get_valid_index(prompt):
        while True:
            index = input(prompt)
            if index == 'back':
               return 'back'
            if index == 'clear':
                return 'clear'
            try:
                index = int(index)
                if index >= 0 and index <= 2:
                    return index
                print("Must be 0 - 2 inclusive!")
            except ValueError:
                print("Must be an integer!")

    # game_is_over
    # -----
    # Return True if the game is over and False
    # otherwise. Print a message indicating who
    # won or whether there was a tie.
    
    #stop var setup
    stop = False

    def game_is_over(board):
        for i in range(3):
            # Check horizontal
            if board[i][0] == board[i][1] == board[i][2] \
                and board[i][0] != " ":
                print_board(board)
                #print(board[i][0] + " wins!")
                return True
            
            # Check vertical
            if board[0][i] == board[1][i] == board[2][i] \
                and board[0][i] != " ":
                print_board(board)
                print(board[0][i] + " wins!")
                return True
            
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] \
            and board[0][0] != " ":
            print_board(board)
            print(board[0][0] + " wins!")
            return True
        
        if board[2][0] == board[1][1] == board[0][2] \
            and board[2][0] != " ":
            print_board(board)
            print(board[2][0] + " wins!")
            return True
        
        # Check tie
        if " " not in board[0] and " " not in board[1] \
            and " " not in board[2]:
            print_board(board)
            print("Tie game!")
            return True
        
        # Not over yet!
        return False
        
    # print_board
    # -----
    # Print the board.
    def print_board(board):
        for i in range(3):    
            print(board[i])

    # Set up board
    board = []
    #Set up the board as a 3x3 grid of spaces
    for i in range(3):
        board.append([' ']*3)

    # x goes first
    turn = "x"

    # Play tic tac toe
    while not game_is_over(board) and not stop:
        print_board(board)
        print("It's " + turn + "'s turn.")
        row = get_valid_index("Row: ")
        if row == 'back':
            board = cash
            print("Undo!")
        if row == 'clear':
            stop = True
            break
        else: 
            col = get_valid_index("Col: ") 
        if board[row][col] == ' ':
            board[row][col] = turn
            cash = board
        else:
            print('Pick another space!')
            continue
        
        
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    return 'Game Over'