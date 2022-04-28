
from ast import Pass, Return


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board, position, player):

     board[position[0]][position[1]] = player 
     return board



def check_for_winner(board, player):

    if (board[0][0] == player and board[0][1] == player and board[0][2] == player):
        return True

    elif (board[1][0] == player and board[1][1] == player and board[1][2] == player):
        return True

    elif (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True

    elif (board[2][0] == player and board[2][1] == player and board[2][2] == player):
        return True

    elif (board[0][0] == player and board[1][0] == player and board[2][0] == player):
        return True
 
    elif (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True

    elif (board[0][1] == player and board[1][1] == player and board[2][1] == player):
        return True

    elif (board[0][2] == player and board[1][2] == player and board[2][2] == player):
        return True


    else:
        return False


'''
Testing: 
'''
board = create_empty_board()

update_board(board, [1,1], "⭕️")

update_board(board, [2,2], "⭕️")

update_board(board, [1,2], "❌")

update_board(board, [2,1], "❌")

update_board(board, [0,1], "❌")

update_board(board, [0,2], "❌")

update_board(board, [2,1], "❌")

update_board(board, [0,0], "⭕️")

update_board(board, [2,0], "❌")

update_board(board, [1,0], "⭕️")

print_board(board)

pass

print("⭕️ WINS!")

