# this file will create a blank board for use in the tic-tac-toe program
import sqlite3
from datetime import datetime

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
        winner = 'player 1'
        break
    playing = check_if_full(board)
    if not playing:
        break
    make_move(player2)
    if check_win():
        winner = 'player 2'
        break
    playing = check_if_full(board)
if not playing:
    print('Draw! Game Over!')
    print()

finished_board = '\n'.join(str(item) for item in board)
# print(row1)

def insertVaribleIntoTable(date, board, winner):
    try:
        sqliteConnection = sqlite3.connect('tic_tac_toe.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite tic_tac_toe.db")
        print()
        
        sqlite_create_table = '''CREATE TABLE IF NOT EXISTS Tic_Tac_Toe_Stats (
                                    date text PRIMARY KEY,
                                    board text NOT NULL,
                                    winner text NOT NULL);'''
        
        cursor.execute(sqlite_create_table)

        sqlite_insert = """INSERT INTO Tic_Tac_Toe_Stats (date, board, winner) VALUES (?, ?, ?);"""

        data_tuple = (date, board, winner)
        cursor.execute(sqlite_insert, data_tuple)
        sqliteConnection.commit()
        print("Game History: ")

        sqlite_select_query = """SELECT * from Tic_Tac_Toe_Stats ORDER BY date DESC LIMIT 10;"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total games:  ", len(records))
        print()
        print("Printing each game")
        for row in records:
            print("Date: ", row[0])
            print('Board:')
            print(row[1])
            print("Winner: ", row[2])
            print()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

now = datetime.now()
reformatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
insertVaribleIntoTable(reformatted_time, finished_board, winner)
