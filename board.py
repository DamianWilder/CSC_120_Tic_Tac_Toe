# this file will create a blank board for use in the tic-tac-toe program

board = [['-' for i in range(3)] for x in range(3)]
def print_board(board):
    print('Printing Board...')
    for i in range(len(board)):
        print(board[i])
    print()

print_board(board)

player1 = [1, 'X']
player2 = [2, 'O']

playing = True

def check_if_full(board):
    for i in range(3):
        for x in range(3):
            if board[i][x] in ['X', 'O']:
                continue
            elif board[i][x] == '-':
                return True
    return False

def check_move(row, col):
    if board[row][col] != '-':
        print()
        print('That space is already taken!')
        print_board(board)
        return False
    else:
        return True

def make_move(player):
    selecting_move = True
    while selecting_move:
        try:
            print(f'Player {player[0]}, make your move')
            row = int(input('Enter row number (0-2): '))
            col = int(input('Enter col number (0-2): '))
            selecting_move = not check_move(row, col)
        except:
            print('**** Invalid row or column. Please select row/col between values 0-2 ****')
            print('**** Invalid choice. Please mark again! ****')
            print_board(board)
            
    print()
    board[row][col] = player[1]
    print(f'Player {player[0]} added mark at the location {row},{col}')
    print_board(board)


while playing:
    make_move(player1)
    playing = check_if_full(board)
    make_move(player2)
    playing = check_if_full(board)

