#Leonard Carcaramo 08/28/19
#Modules for Python Tic Tac Toe

import Modules
import random

"""
Displays the data inside the board.
PARAM: "board" The 2 dimensional array that stores the players' moves.

Output:

  1  2  3
1[ ][ ][ ]
2[ ][ ][ ]
3[ ][ ][ ]

"""
def displayBoard(board):
    print("  1  2  3")
    row = ""
    rowNumber = 1
    
    for i in board:
        row += str(rowNumber)
        for j in i:
                row += "[" + j + "]"
        print (row)
        row = ""
        rowNumber += 1
print(" ")

"""
Takes user input for which coordinates the player would like to make his or her move.
PARAM: "x" String variable that represents player X.
PARAM: "board" the 2 dimensional array that stores the players' moves.

RETURN: 2 dimensional array that represents an updated version of the board.
"""
def playerTurn(x, board):
    continueLoop = True #controls while loop below
    
    while continueLoop:
        Modules.displayBoard(board)
        try:
            coordinate = input("Please enter the coordinate 'row,col' that corresponds to the space where you would like to make your move: ")
            
            if len(coordinate) == 3 and coordinate[1:2] == ",": #if input is properly formated
                #exception will be thrown here if coordinates are not integers
                row = int(coordinate[0:1])
                col = int(coordinate[2:])
                
                if row <= 3 and col <= 3 and row >= 1 and col >= 1: #if coordinates are not out of range
                    if board[row-1][col-1] == " ": #if the space on the board is free
                        board[row-1][col-1] = x
                        
                        continueLoop = False
                    else:
                        print("*** Specified coordinate is already occupied. ***")
                else:
                    print("*** Error! One or more Coordinates are out of range. ***")
            else:
                print("*** Error! Coordinates must be entered in 'row,col' format. ***")
        except:
            print("*** Error! Coordinates must be integers! ***")
            
    return board

"""
Random number generator used to choose a coordinate for the computer to take it's turn.
PARAM: "o" String variable that represents player O.
PARAM: "board" the 2 dimensional array that stores the players' moves.

RETURN: 2 dimensional array that represents an updated version of the board.
"""
def computerTurnRandom(o, board):
    continueLoop = True #controls do while
    
    while (continueLoop):
        row = random.randint(0,2) #randomly choose a row
        col = random.randint(0,2) #randomly choose a column
        
        if board[row][col] == " ": #if space is free
            board[row][col] = o
            continueLoop = False       
    return board

"""
Heuristics used to help the computer make the best move possible.
If the heuristics in this module cannot find a good move, a move will be made using the computerTurnRandom() module.
PARAM: "o" String variable that represents player O.
PARAM: "board" the 2 dimensional array that stores the players' moves.

RETURN: 2 dimensional array that represents an updated version of the board.
"""
def computerTurnWithHeuristics(o, board):
    bestRow = 0 #stores the index of the best row
    bestCol = 0 #stores the index of the best column
    
    rowScore = 0 #stores the score of the best row found
    colScore = 0 #stores the score of the best column found
    forwardDiagonalScore = 0 #stores the score of the forward diagonal
    backDiagonalScore = 0 #stores the score of the back diagonal
    
    #scores range from 0-4.
    #O will make it's move based on the row, column, forward diagonal, or back diagonal with the highest score.
    
    #counters
    xCount = 0
    oCount = 0
    blankCount = 0
    
    #Check rows
    for row in range(3): #for each row
        for col in range(3): #for each column
            if board[row][col] == "O":
                oCount += 1
            elif board[row][col] == "X":
                xCount += 1
            elif board[row][col] == " ":
                blankCount += 1
        if blankCount > 0: #if the row is not full
            if xCount == 2 and rowScore < 4:
                rowScore = 4
                bestRow = row
            elif oCount == 2 and rowScore < 3:
                rowScore = 3
                bestRow = row
            elif oCount == 1 and rowScore < 2:
                rowScore = 2
                bestRow = row
            elif blankCount == 3 and rowScore < 1:
                rowScore = 1
                bestRow = row
        xCount = 0
        oCount = 0
        blankCount = 0
        
    #Check columns
    for col in range(3): #for each column
        for row in range(3): #for each row
            if board[row][col] == "O":
                oCount += 1
            elif board[row][col] == "X":
                xCount += 1
            elif board[row][col] == " ":
                blankCount += 1
        if blankCount > 0: #if the column is not full
            if xCount == 2 and colScore < 4:
                colScore = 4
                bestCol = col
            elif oCount == 2 and colScore < 3:
                colScore = 3
                bestCol = col
            elif oCount == 1 and colScore < 2:
                colScore = 2
                bestCol = col
            elif blankCount == 3 and colScore < 1:
                colScore = 1
                bestCol = col
        xCount = 0
        oCount = 0
        blankCount = 0
        
    #back diagonal
    if board[0][0] == "O":
        oCount += 1
    elif board[0][0] == "X":
        xCount += 1
    elif board[0][0] == " ":
        blankCount += 1
        
    if board[1][1] == "O":
        oCount += 1
    elif board[1][1] == "X":
        xCount += 1
    elif board[1][1] == " ":
        blankCount += 1
        
    if board[2][2] == "O":
        oCount += 1
    elif board[2][2] == "X":
        xCount += 1
    elif board[2][2] == " ":
        blankCount += 1
        
    if blankCount > 0: #if the back diagonal is not full
        if xCount == 2 and backDiagonalScore < 4:
            backDiagonalScore = 4
        elif oCount == 2 and backDiagonalScore < 3:
            backDiagonalScore = 3
        elif oCount == 1 and backDiagonalScore < 2:
            backDiagonalScore = 2
        elif blankCount == 3 and backDiagonalScore < 1:
            backDiagonalScore = 1
    xCount = 0
    oCount = 0
    blankCount = 0
    
    #forward diagonal
    if board[2][0] == "O":
        oCount += 1
    elif board[2][0] == "X":
        xCount += 1
    elif board[2][0] == " ":
        blankCount += 1
        
    if board[1][1] == "O":
        oCount += 1
    elif board[1][1] == "X":
        xCount += 1
    elif board[1][1] == " ":
        blankCount += 1
        
    if board[0][2] == "O":
        oCount += 1
    elif board[0][2] == "X":
        xCount += 1
    elif board[0][2] == " ":
        blankCount += 1
        
    if blankCount > 0: #if the forward diagonal is not full
        if xCount == 2 and forwardDiagonalScore < 4:
            forwardDiagonalScore = 4
        elif oCount == 2 and forwardDiagonalScore < 3:
            forwardDiagonalScore = 3
        elif oCount == 1 and forwardDiagonalScore < 2:
            forwardDiagonalScore = 2
        elif blankCount == 3 and forwardDiagonalScore < 1:
            forwardDiagonalScore = 1
    
    #if the best row has the highest score
    if rowScore >= colScore and rowScore >= backDiagonalScore and rowScore >= forwardDiagonalScore:
        placed = False #checks if O has been placed or not
        
        for col in range(3):
            if board[bestRow][col] == " " and placed == False:
                board[bestRow][col] = o
                placed = True
                
    #if the best column has the highest score
    elif colScore >= rowScore and colScore >= backDiagonalScore and colScore >= forwardDiagonalScore:
        placed = False #checks if O has been placed or not
        
        for row in range(3):
            if board[row][bestCol] == " " and placed == False:
                board[row][bestCol] = o
                placed = True
                
    #if the back diagonal has the highest score
    elif backDiagonalScore >= colScore and backDiagonalScore >= rowScore and backDiagonalScore >= forwardDiagonalScore:
        if board[0][0] == " ":
            board[0][0] = o          
        elif board[1][1] == " ":
            board[1][1] = o 
        elif board[2][2] == " ":
            board[2][2] = o
            
    #if the forward diagonal has the highest score
    elif forwardDiagonalScore >= colScore and forwardDiagonalScore >= backDiagonalScore and forwardDiagonalScore >= rowScore:
        if board[2][0] == " ":
            board[2][0] = o          
        elif board[1][1] == " ":
            board[1][1] = o 
        elif board[0][2] == " ":
            board[0][2] = o
            
    else: #if for some reason this module could not find a good move, call computerTurnRandom() module
        return Modules.computerTurnRandom(o, board)
    
    return board

"""
Checks to see if specified player has won.
PARAM: "key" String variable to specify which player the code is checking for a win for.
PARAM: "board" the 2 dimensional array that stores the players' moves.

RETURN: boolean that indicates whether or not the specified player has won or not.
"""
def checkWin(key,  board):
    for row in range(3): #check rows for win
        if board[row][0] == key and board[row][1] == key and board[row][2] == key: #check row for win
            return True
    for col in range(3): #check columns for win
        if board[0][col] == key and board[1][col] == key and board[2][col] == key: #check column for win
            return True
    if board[0][0] == key and board[1][1] == key and board[2][2] == key: #check back diagonal win
        return True
    if board[2][0] == key and board[1][1] == key and board[0][2] == key: #check forward diagonal win
        return True
    
    return False