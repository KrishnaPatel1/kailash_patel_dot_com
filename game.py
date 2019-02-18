import numpy
from win_condition import check_for_win
from printer import print_board
from block import Block
from move import play_move

#initialize board
board = numpy.empty((12, 8), dtype=object)
for i in range(len(board)):
    for j in range(len(board[i])):
        board[i, j] = Block()


#TODO implement game logic and loop with check for win condition

#TODO make sure move is legal (isn't hanging/ in midair) + isn't on top of another card
#TODO break the loop if a player wins
#TODO ask if player is dots or color
while True:
        move =  input("Where will you place your card? ")

        result = play_move(board, move)

        #TODO use ascii characters to print out more readable board

        # result[1] = True = good move
        # result[1] = False = illegal move
        if result[1] is True:
                print_board(result[0])
        else:
                print_board(result[0])
                print('Illegal move! Do not attempt that again!')

        check_for_win(result[0])
