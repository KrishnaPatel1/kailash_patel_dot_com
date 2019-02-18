#print board
def print_board(game_board):
    rows = game_board.shape[0]
    cols = game_board.shape[1]
    for row in range(0, rows):
        print(rows - row, end='\t')
        for col in range(0, cols):
            print(game_board[row, col], end='\t')
        print()
    print("", end='\t')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(0, cols):
        print(letters[i].upper(), end='\t')
    print()    