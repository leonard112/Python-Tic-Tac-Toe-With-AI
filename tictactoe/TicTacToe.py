#Leonard Carcaramo 08/28/19
#Python Tic Tac Toe

import Modules #All Modules used are located here

x = "X" #String to represent player X on the board
o = "O" #String to represent player O on the board

xWin = False #control var to check if player X wins or not
oWin = False #control var to check if player O wins or not
moveCount = 0 #keeps track or number of moves (tie if moveCount == 9)

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] #moves are stored in this 2 dimensional array.

continueLoop = True #controls while loop below

while continueLoop:
    while xWin == False and oWin == False and moveCount < 9: #while no wins and number of moves is less than 9
        board = Modules.playerTurn(x, board) #player X takes turn
        moveCount += 1
        xWin = Modules.checkWin(x, board) #check if player X wins
        if xWin == True: #if player X wins
            Modules.displayBoard(board)
            print("You Win!")
        if moveCount == 9 and xWin == False and oWin == False: #check tie
            Modules.displayBoard(board)
            print("Tie.")
        
        if xWin == False and moveCount < 9: #make sure player X did not win, and number of moves have not reached 9
            if moveCount == 1: #make player O's move random for the first turn
                board = Modules.computerTurnRandom(o, board)
            else: #use heuristics for player O's turn
                board = Modules.computerTurnWithHeuristics(o, board) 
            moveCount += 1
            oWin = Modules.checkWin(o, board) #check if player O wins
        if oWin == True: # if player O wins
            Modules.displayBoard(board)
            print("You lose.")
            
    optionValid = False #controls while loop below
    
    while optionValid == False: #while user input is not valid
        playAgain = input("Would you like to play again 'yes/no': ")
        if playAgain == "yes": #if player wants to play again
            optionValid = True
            xWin = False
            oWin = False
            moveCount = 0
            board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        elif playAgain == "no": #if player does not want to play again
            optionValid = True
            continueLoop = False
        else:
            print("Invalid Input! Valid options are 'yes' and 'no' only.")