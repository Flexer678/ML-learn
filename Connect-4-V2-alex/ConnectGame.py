from Board import Board
import random
import time

class ConnectGame:
  def __init__(self):
        self._board = Board()
        #initial max depth
        self._maxdepth = 3

  def run(self):
      #  self._board.display_board()
        run = True
        person = 2
        try:
            self._maxdepth = int(input("enter your max depth:"))
            print("okay")
        except:
            print(" ")
            

        while run:
            self._board.display_board()
            #print(self._board.is_draw())
            person =2
            #time.sleep(1)
            self.player_move(person)
            run = self._board.win_check(person)
            
            if not run:
                break
            person = 1
           # self.ai_move( 8)   
            self.smart_ai_move(self._maxdepth)
            run = self._board.win_check(person)
          
            if not run:
                break


  def enter_piece(self, userInput, person):
        self._board.enter_board(userInput, person)

  def player_move(self, person):
        print(self._board._board)
       
        while True:
            try:
                userInput = int(input('Player ' + str(person) +
                                      ' : Which column do you want to put the ball in: ')) - 1
                if userInput in range(6) and self._board.board[1][userInput] == ' ':
                    self.enter_piece(userInput, person)
                    break
                else:
                    print("Invalid input")
            except Exception:
                print("Something went wrong")
                
  def ai_move( self, person):
     
      a =random.randint(1, 6)
      print("bot move" ,a )
      self.enter_piece(a-1, person)
      
      
  def smart_ai_move(self, max_depth):
     
      #self.enter_piece(random.randint(1, 6), 1)
      best_eval = -float('inf')
      best_move = 0

      for x in range(1, 7):
          for y in range(6):
              #fills the hiles that arent empty
              if self._board.board[x][y] == " ":
                  #print(self._board.getboard[x][y])
                  self._board.board[x][y] = self._board._personDict[1]
                  eval = self.minimax(0, False, max_depth)
                  self._board._board[x][y] = ' '
                  if eval > best_eval:
                      best_eval = eval
                      best_move = (x ,y)
      print(best_move)
      
      self.enter_piece(best_move[0]-1, 1)
      #return best_move
  
  def minimax(self, depth, is_maximizing, max_depth):

      #if person wins
    if  not self._board.win_check(2):
         # print("being called 1", self._board.win_check(self._board._personDict[2]))
          return -1
    elif  not self._board.win_check(1) :
          print("being called 2")
          return 1
      #checks if it is draw or reached its max depth
    elif  not self._board.is_draw() or depth == max_depth:
         # print("being called 3")
          return 0
    #print("whats going on here") 
    if is_maximizing:
        #  print('maximizing')
          max_eval = -float('-inf')
          for x in range(1, 7):
            for y in range(6):
                #print(self._board._board[x][y])
                if self._board._board[x][y] == ' ':
                    # Simulate the move for the maximizing player ('O')
                    self._board._board[x][y] =  self._board._personDict[1]
                    # Recursively call minimax for the next level with the minimizing player's turn
                    eval = self.minimax(depth + 1, False, max_depth)
                    # Undo the move
                    self._board._board[x][y] = ' '
                    # Update the maximum evaluation score
                    max_eval = max(max_eval, eval)
          return max_eval
    else:
        #  print("minimizing")
          max_eval = float('-inf')
          for x in range(1,7):
            for y in range(6):
                #print(self._board._board[x][y])
                if self._board._board[x][y] == ' ':
                    # Simulate the move for the maximizing player ('O')
                    self._board._board[x][y] = self._board._personDict[2]
                    # Recursively call minimax for the next level with the minimizing player's turn
                    eval = self.minimax(depth + 1, True, max_depth)
                    # Undo the move
                    self._board._board[x][y] = ' '
                    # Update the maximum evaluation score
                    min_eval = min(max_eval, eval)
          return min_eval
