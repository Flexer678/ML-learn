import math
import random

board = [" " for x in range(9)]

def print_board():
    for i in range(3):
        print("|" + "|". join(board[i*3:(i+1)*3]) + "|")
        
        
def player():
    choice = input("pick a position (0-8)")
    try:
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = 'X'
    except:
        print(" your input should be between 0 and 8")

def empty_spots():
    return board.count(" ")

def isfull():
    return board.count(" ") == 0

def smartComputer():
    bestscore = -math.inf
    move =0
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board,False)
            board[i] = " "
            if score > bestscore:
                bestscore = score
                move =1
    board[move] =0
           
def minimax (board , ismaximizer):
    if winner("x"):
        score = -(empty_spots()+1)
        return True
    elif winner("O"):
        score = (empty_spots() +1)
        return True
    elif isfull():
        return 0
    #if computer plays
    if ismaximizer:
        bestscore = -math.inf
        for i in range(len(board)):
            board[i] = "O"
            score = minimax(board,False)
            board[i] = " "
            bestscore = max(bestscore,score)
            return bestscore
    else:
        bestscore = math.inf
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                bestscore = min(bestscore, score)
            return bestscore
              
        

def computer():
    #sees the avaulable moves and then places a puck
    available =[]
    for x in range(len(board)):
        if board[x] == " ":
            available.append(x)
    b = random.choice(available)
    b = int(b)
    board[b] = '0'

def winner(letter):
    #horizontal
    for i in range(3):
        #checks if the letter is equals to each cell
        #basically a for loop that checks if letter is quals to each cell
        if all(x==letter for x in board[i*3:(i+1)*3]):
            return True

    #vertical    
    for i in range(3):
        if all(x ==letter for x in [board[i%3 + 3*j]   for j in range(3)]):
            return True
    if all(board[x] == letter for x in [0,4,8]):
        return True
    if all(board[x] == letter for x in [2,4,6]):
        return True
        
        
def main():
    while True:
        print_board()
        print("   \n")
        player()
        if winner("x"):
            print("x winds")
            break
        print_board()
        isfull()
        print("   \n")
        computer()
        if winner("O"):
            print("O winds")
            break
main()
