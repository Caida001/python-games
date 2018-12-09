from random import randint
import time

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    print " "+board[1]+" | "+board[2]+" | "+board[3]+" "
    print "--- --- ---"
    print " "+board[4]+" | "+board[5]+" | "+board[6]+" "
    print "--- --- ---"
    print " "+board[7]+" | "+board[8]+" | "+board[9]+" "
    print "--- --- ---"



def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
    (board[4] == player and board[5] == player and board[6] == player) or \
    (board[7] == player and board[8] == player and board[9] == player) or \
    (board[1] == player and board[4] == player and board[7] == player) or \
    (board[2] == player and board[5] == player and board[8] == player) or \
    (board[3] == player and board[6] == player and board[9] == player) or \
    (board[1] == player and board[5] == player and board[9] == player) or \
    (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def is_board_full():
    if " " in board:
        return False
    return True

def get_computer_move(board, player):

# check for a win; loop through the board to see if there's a move can cause a win
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = player
            if is_winner(board, player):
                return i
            else:
                board[i] = " "


    # if center is empty, choose center
    if board[5] == " ":
        return 5
    else:
        while True:
            move = randint(1, 9)
            # if the move is blank, return otherwise try again
            if board[move] == " ": return move



print_board()
while True:


    # get X position
    choice = int(raw_input("choose a empty space for player X: "))

    if board[choice] == " ":
        board[choice] = "X"
        print_board()
    else:
        print("that space is taken")

    if is_winner(board, "X"):
        print_board()
        print "X wins!!!"
        break


    if is_board_full():
        print "A Tie !!!"
        break

    # get O position
    print("waiting for AI to make the move")
    time.sleep(2)
    choice = get_computer_move(board, "O")

    if board[choice] == " ":
        board[choice] = "O"
        print_board()
    else:
        print("that space is taken")

    if is_winner(board, "O"):
        print_board()
        print "O wins!!!"
        break

    if is_board_full():
        print "A Tie !!!"
        break
