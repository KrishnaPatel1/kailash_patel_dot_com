from block import Block

def play_move(board, move):
    #remove spaces
    move = move.replace(" ", "")
    if move != '':
        #check if not recycling
        if move[0] == '0':
            if not validate_move(board, move[1:]):
                return [board, False]
            return [board, check_rotation(board, move[1:])]
        else: 
            card1 = board[-int(move[1]), ord(move[0].upper())-65]
            card2 = board[-int(move[3]), ord(move[2].upper())-65]
            # check if empty card 
            if card1.half != '' and card2.half != '':
                #TODO check if every card has been played from the players hands
                #TODO check if not last card played

                #check if correct halfs of same card
                if (card1.half == 'r' and card2.half == 'l') or (card1.half == 'l' and card2.half == 'r') or (card1.half == 'u' and card2.half == 'd') or (card1.half == 'd' and card2.half == 'u'): 
                    #empty the original card
                    board[-int(move[1]), ord(move[0].upper())-65] = Block('', '', '')
                    board[-int(move[3]), ord(move[2].upper())-65] = Block('', '', '')
                    if not validate_move(board, move[4:]):
                        #refill if invalid
                        board[-int(move[1]), ord(move[0].upper())-65] = card1
                        board[-int(move[3]), ord(move[2].upper())-65] = card2
                        return [board, False] 
                    return [board, check_rotation(board, move[4:])]      
    return [board, False]


# for each rotation create correct block/card
def check_rotation(board, move):
    if move[0] == '1':
        b1 = Block('red', 'full', 'r')
        b2 = Block('white', 'empty', 'l')
        board[-int(move[2]), ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65+1] = b2
    elif move[0] == '2': 
        b1 = Block('red', 'full', 'd')
        b2 = Block('white', 'empty', 'u')
        board[-int(move[2])-1, ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65] = b2
    elif move[0] == '3':
        b1 = Block('white', 'empty', 'r')
        b2 = Block('red', 'full', 'l')
        board[-int(move[2]), ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65+1] = b2
    elif move[0] == '4':
        b1 = Block('white', 'empty', 'd')
        b2 = Block('red', 'full', 'u')
        board[-int(move[2])-1, ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65] = b2
    elif move[0] == '5':
        b1 = Block('red', 'empty', 'r')
        b2 = Block('white', 'full','l')
        board[-int(move[2]), ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65+1] = b2
    elif move[0] == '6':
        b1 = Block('red', 'empty','d')
        b2 = Block('white','full', 'u')
        board[-int(move[2])-1, ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65] = b2
    elif move[0] == '7':
        b1 = Block('white', 'full', 'r')
        b2 = Block('red', 'empty', 'l')
        board[-int(move[2]), ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65+1] = b2
    elif move[0] == '8':
        b1 = Block('white', 'full', 'd')
        b2 = Block('red', 'empty', 'u')
        board[-int(move[2])-1, ord(move[1].upper())-65] = b1
        board[-int(move[2]), ord(move[1].upper())-65] = b2
    else: return False
    return True

# check if move is valid
def validate_move(board, move):
    # column doesn't exist
    if ord(move[1].upper()) > 71 or ord(move[1].upper()) < 65:
        return False

    # if first row
    if int(move[2]) is 1:
        if not check_first_row(board, move): 
            return False
    else:      
        if not check_space_below(board, move):
            return False

    if not check_space(board, move):
        return False
    
    return True

# check if move on first row is valid
def check_first_row(board, move):

    # make sure it is not placed horizontally on column G
    if int(move[0]) % 2 is not 0:
        if ord(move[1].upper()) is 71:
            return False
            
    return True

# check if space is occupied by another piece
def check_space(board, move):
    
    # orientation is vertical
    if int(move[0]) % 2 is 0:
        bottom_piece = board[-int(move[2]), ord(move[1].upper())-65]
        top_piece = board[-int(move[2])-1, ord(move[1].upper())-65]

        if str(bottom_piece) != "[---]" or str(top_piece) != "[---]":
            return False

    # orientation is horizontal
    else:
        left_piece = board[-int(move[2]), ord(move[1].upper())-65]
        right_piece = board[-int(move[2]), ord(move[1].upper())-65+1]

        if str(left_piece) != "[---]" or str(right_piece) != "[---]":
            return False

    return True

# check if space below is occupied by a piece
def check_space_below(board, move):
        
    # orientation is vertical
    if int(move[0]) % 2 is 0:
        bottom_piece_bellow = board[-int(move[2])+1, ord(move[1].upper())-65]

        if str(bottom_piece_bellow) == "[---]":
            return False

    # orientation is horizontal
    else:
        left_piece_below = board[-int(move[2])+1, ord(move[1].upper())-65]
        right_piece_below = board[-int(move[2])+1, ord(move[1].upper())-65+1]

        if str(left_piece_below) == "[---]" or str(right_piece_below) == "[---]":
            return False
    
    return True
