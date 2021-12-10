# this file will create a blank board for use in the tic-tac-toe program

board = [['-' for i in range(3)] for x in range(3)]
def print_board(board):
    print('Printing Board')
    for i in range(len(board)):
        print(board[i])
print_board(board)