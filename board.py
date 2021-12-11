# this file will create a blank board for use in the tic-tac-toe program

board = [['-' for i in range(3)] for x in range(3)]
player1 = [1, 'X']
player2 = [2, 'O']

playing = True


def print_board(board):
    print('Printing Board...')
    for i in range(len(board)):
        print(board[i])
    print()


print_board(board)


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
        print(f'**** Board[{row}][{col}] has already been selected. Please choose somewhere else on the board ****')
        print('**** Invalid choice. Please mark again! ****')
        print_board(board)
        return False
    else:
        return True


def diagonal_win(board):
    if board[0][0] != '-' and (board[0][0] == board[1][1] == board[2][2]):
        return True
    elif board[0][2] != '-' and (board[0][2] == board[1][1] == board[2][0]):
        return True
    else:
        return False


def horizontal_win(board):
    if board[0][0] != '-' and (board[0][0] == board[0][1] == board[0][2]):
        return True
    elif board[1][0] != '-' and (board[1][0] == board[1][1] == board[1][2]):
        return True
    elif board[2][0] != '-' and (board[2][0] == board[2][1] == board[2][2]):
        return True
    else:
        return False


def vertical_win(board):
    if board[0][0] != '-' and (board[0][0] == board[1][0] == board[2][0]):
        return True
    elif board[0][1] != '-' and (board[0][1] == board[1][1] == board[2][1]):
        return True
    elif board[0][2] != '-' and (board[0][2] == board[1][2] == board[2][2]):
        return True
    else:
        return False


def check_win():
    if diagonal_win(board) or horizontal_win(board) or vertical_win(board):
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
            print(
                '**** Invalid row or column. Please select row/col between values 0-2 ****')
            print('**** Invalid choice. Please mark again! ****')
            print_board(board)

    print()
    board[row][col] = player[1]
    print(f'Player {player[0]} added mark at the location {row},{col}')
    if check_win():
        print(f'Player {player[0]} wins! Game Over!')
        print()
    else:
        print_board(board)


while playing:
    make_move(player1)
    if check_win():
        break
    playing = check_if_full(board)
    if not playing:
        break
    make_move(player2)
    if check_win():
        break
    playing = check_if_full(board)
if not playing:
    print('Draw! Game Over!')
    print()
