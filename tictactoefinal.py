print("WELCOME TO TIC TAC TOE")
print("Enter Y or y to play game\nEnter n or N to exit game\n")
while True:
    u = input("Enter your option:")
    if u not in ['y', 'Y', 'n', 'N']:
        print("Wrong input, ", end='')
        continue
    break

if u == 'n' or u == 'N':
    print("The game has ended!")
    exit()

while True:
    print("Press 1 to start the game ")
    while True:
        u = input("User option selected:")
        if u not in ['1', '2']:
            print("Wrong input, ", end ='')
            continue
        break
    single_player = '1'


    while u == single_player:
        print("Let's play TIC-TAC-TOE!!")
        import random
        def displayBoard(board):

            print(board[1] + '|' + board[2] + '|' + board[3])
            print('_|_|_')
            print(board[4] + '|' + board[5] + '|' + board[6])
            print('_|_|_')
            print(board[7] + '|' + board[8] + '|' + board[9])
            print('', '|', '|')
            print("\n")

        def isSpaceFree(board, move):
            if board[move] == ' ':
                return True
            else:
                return False


        def selectPlayerLetter():
            letter = ''
            while not (letter == 'X' or letter == 'O'):
                letter = input('\nDo you want to be X or O?')
                letter = letter.upper()
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']


        def whoGoesFirst():
            select_toss = int(input("\nPress 1 for heads and press 0 for tails: "))

            while True:
                if select_toss not in [1, 0]:
                    select_toss = int(
                        input("Wrong input\nPress 1 for heads and press 0 for tails: "))
                    continue
                break
            toss = random.randint(0, 1)
            if toss == 1:
                print("It was heads!")
            else:
                print("It was tails!")
            if toss == select_toss:
                print("Player has won the toss!\n")
                return 'player'
            else:
                print("Computer has won the toss!\n")
                return 'computer'
        
        
        def handleTurn(board, letter, move):
            if isSpaceFree(board, move):
                board[move] = letter
            else:
                print("The place has already been filled!")
                move = int(input("Please enter another place:  "))
                handleTurn(board,letter, move)
                return



        def checkForWinner(board, letter):
            return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))



        def getBoardCopy(board):
            board_copy = []

            for i in board:
                board_copy.append(i)
            return board_copy



        def getPlayerMove(board):
            move = ' '
            while move not in '1 2 3 4 5 6 7 8 9'.split():
                enter_move = input('Choose a place from 1-9: ')
                try:
                    enter_move = int(enter_move)
                except ValueError:
                    print("\nWrong input!\n")
                    continue
                move = enter_move
                if move > 0 and move < 10:
                     return move
                while True:
                     if move < 0 or move > 10:
                         enter_move = int(input('Choose a place from 1-9: '))
                         if enter_move > 0 and enter_move < 10:
                             move = enter_move
                             return move
                             break
                         
            
                else:
                    print(name,"choose correct option")



        def chooseRandomMove(board, movesList):
            possibleMoves = []
            for i in movesList:
                if isSpaceFree(board, i):
                    possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None



        def computerMove(board, computerLetter):
            if computerLetter == 'X':
                playerLetter = 'O'
            else:
                playerLetter = 'X'

            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    handleTurn(copy, computerLetter, i)
                    if checkForWinner(copy, computerLetter):
                        return i

            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    handleTurn(copy, playerLetter, i)
                    if checkForWinner(copy, playerLetter):
                        return i

            if isSpaceFree(board, 5):
                return 5

            move = chooseRandomMove(board, [1, 3, 7, 9])
            if move != None:
                return move

            return chooseRandomMove(board, [2, 4, 6, 8])



        def playAgain():
            u = input('Enter y to play again or press any other key to exit: ')
            if u == 'y' or u == 'Y':
                return True
            else:
                return False



        def isBoardFull(board):
            for i in range(1, 10):
                if isSpaceFree(board, i):
                    return False
            return True


        name = input("Please enter your name: ")
        name = name.upper()



        while True:
            the_board = [' '] * 10
            playerLetter, computerLetter = selectPlayerLetter()
            turn = whoGoesFirst()

            gameStillGoing = True


            while gameStillGoing:
                if turn == 'player':
                    displayBoard(the_board)
                    move = getPlayerMove(the_board)
                    handleTurn(the_board, playerLetter, move)

                    if checkForWinner(the_board, playerLetter):
                        displayBoard(the_board)
                        print('CONGRATS!', name, ',YOU HAVE WON THE GAME.')
                        gameStillGoing = False

                    else:
                        if isBoardFull(the_board):
                            displayBoard(the_board)
                            print("It's a draw!")
                            break

                        else:
                            turn = 'computer'


                else:
                    move = computerMove(the_board, computerLetter)
                    handleTurn(the_board, computerLetter, move)

                    if checkForWinner(the_board, computerLetter):
                        displayBoard(the_board)
                        print('COMPUTER HAS WON! You lose.\nBETTER LUCK NEXT TIME,', name)
                        gameStillGoing = False

                    else:
                        # Checking if the game is tied
                        if isBoardFull(the_board):
                            displayBoard(the_board)
                            print("It's a draw!")
                            break


                        else:
                            turn = 'player'

            if playAgain():
                break
            else:
                print("Thank you for playing Tic Tac Toe with us!")
                exit()
        break

        print("\n\nUser option selected if wants to play game again or wants to exit","\n","press n,N to exit","\n","press y,Y to play again")
        while True:
            u=input("Enter your option")
            if u == 'y' or u == 'Y':
                break
            elif u == 'n' or u == 'N':
                exit()
            else:
                print("Wrong input, ", end='')
                continue
    
    if u == 'n' or u == 'N':
        print("End game")
        break

    print("Thanks for playing again")
