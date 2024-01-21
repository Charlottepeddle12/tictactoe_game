def display_title():
    '''
    Returns nothing
    -------
    Prints the title and empty grid (created with + strigns and \n)

    '''
    print("Welcome to Tic Tac Toe")
    print('+---+---+---+'+
        '\n|   |   |   |' + 
        "\n+---+---+---+" +
        '\n|   |   |   |' +
        "\n+---+---+---+" +
        '\n|   |   |   |' + 
        "\n+---+---+---+")
    
def game_board(): 
    '''
    Returns board 
    -------
    board : list
        The grid as a list with empty spaces where X and O will go

    '''
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]] 
    return board

def show_board(board):
    '''

    Parameters: board
    ----------
    board : list
        DESCRIPTION: list that is used to play the game and each spot in the lsit corrspondes to a space of 
        tje grid as seen below

    Returns nothing
    -------

    '''
    
    print()
    print('+---+---+---+'+
        '\n| {} | {} | {} |'.format(board[0][0], board[0][1], board[0][2]) + 
        "\n+---+---+---+" +
        '\n| {} | {} | {} |'.format(board[1][0], board[1][1], board[1][2]) +
        "\n+---+---+---+" +
        '\n| {} | {} | {} |'.format(board[2][0], board[2][1], board[2][2]) + 
        "\n+---+---+---+")
    
def x_turn(board):
    '''

    Parameters: board
    ----------
    board : list
        X's turn
        the crow and column is requested.
        if the space requested is an empy string, then X is added into the space.
        if the spot is already taken, a message states this and asks the user to pick again. 
        this loop is broken if the spot is empy though'

    Returns nothing
    -------

    '''
    while True:
        print("\nX's turn") #asks X to pick a row and column
        row = int(input("Pick a row (1,2.3): ")) -1
        column = int(input("Pick a column (1,2,3): ")) -1
        if board[row][column] == " ":
            board[row][column] = "X" 
            game_board()
            break
        else:
            print("Spot is already taken. Pick another spot")
            continue
            
def o_turn(board):
    '''

    Parameters: board
    ----------
    board : list
        SEE DOCSTRING FOR x_turn() FUNCTION

    Returns nothing
    -------

    '''
    while True:
        print("\nO's turn")
        row = int(input("Pick a row (1,2.3): ")) -1
        column = int(input("Pick a column (1,2,3): ")) -1
        if board[row][column] == " ":
            board[row][column] = "O" 
            game_board()
            break

        else:
            print("Spot is already taken. Pick another spot")
            continue
     
def check_tie(board):
    '''

    Parameters: board
    ----------
    board : list
        DESCRIPTION: number variable repsents how many spaces are taken up (by either X or O)
        each spot in the grid is iterated though, and if the space is not empty (not " "), then
        number is increased by 1.
        there are 9 spaces in the grid, so if all spaces are full without a winner, then it a tie
        a statement is printed saying it is a tie
        number is returned

    Returns nothing
    -------
    number : integer
 

    '''
    number = 0
    for row in board:
        for space in row:
            if space != " ":
                number += 1
    if number == 9:
        print("It's a tie! No one wins!")
        return number
    
def x_winner(board):
    '''

    Parameters: board
    ----------
    board : list
        DESCRIPTION: this function determiens if X is the winner
        all combinations for tic tac toe are considerd:
        vertically or horizontally across all rows, diagonally from corner to corner
        all spaces mentioned in the if/elif statemnts msut have X in it in order to be true
        if soemthing is true, a print statement prints X as the winner
        
        board[row][column] is used if you are confused about which number is column and which number is row
        

    Returns nothing
    -------

    '''
    
    if board[0][0] == board[0][1] == board[0][2] == "X":
        print("\nX wins!")
        return True
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        print("\nX wins!")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print("\nX wins!")
        return True
    elif board[0][0] == board[1][0] == board[2][0] == "X":
        print("\nX wins!")
        return True
    elif board[0][1] == board[1][1] == board[2][2] == "X":
        print("\nX wins!")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print("\nX wins!")
        return True
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        print("\nX wins!")  
        return True
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print("\nX wins!")
        return True
        
def o_winner(board):
    '''

    Parameters: board
    ----------
    board : list
        DESCRIPTION: SEE DOCSTRING FOR x_winner() FUNCTION
        this function determiens if O is the winner

    Returns nothing
    -------

    '''
    if board[0][0] == board[0][1] == board[0][2] == "O":
        print("\nO wins!")
        return True
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        print("\nO wins!")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print("\nO wins!")
        return True
    elif board[0][0] == board[1][0] == board[2][0] == "O":
        print("\nO wins!")
        return True
    elif board[0][1] == board[1][1] == board[2][2] == "O":
        print("\nO wins!")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print("\nO wins!")
        return True
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        print("\nO wins!")  
        return True
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        print("\nO wins!")
        return True
    
#contents in board_game(0 fucntion is assigned to board variable)
board = game_board()

#show board prints the board
show_board(board)

#go controsl the while loop. while go is "y", the loop will continue until a break statement
go = "y"

while go == "y":
    
    #x's turn to choose a spot
    x_turn(board)
    #board is prited with x palced in the board
    show_board(board)
    #checks to see if x is the winner, if so, it will break
    if x_winner(board) == True:
        break
    #checks for a tie, if so, it will break
    if check_tie(board) == 9:
        break
    #same as above, but for O istead of X
    o_turn(board)
    show_board(board)
    if o_winner(board) == True:
        break

#anytiem someone wins or a tie occurs, the loop will break 

#game over pritns after it ends  
print("\nGame over!")