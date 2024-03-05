import os

# this imports os to clear the console, and we import playMove to ask
#  the player for their move, then enters the puck to the board.



# feedback (oct 16)
# - try to move os stuff to connectgame.py
# - try to not import connectgame in board.py


def clr():
  os.system('cls' if os.name == 'nt' else 'clear')


# general clear function


class Board:

  def __init__(self):

    self._personDict = {
        #1 is player 1 and player 1 gets to go first
        1: "⬤",
        #2 is player 2
        2: "◯"
    }

    self._board = {
        # numbers at the top are the columns
        0: [1, 2, 3, 4, 5, 6],
        1: [' ', ' ', ' ', ' ', ' ', ' '],
        2: [' ', ' ', ' ', ' ', ' ', ' '],
        3: [' ', ' ', ' ', ' ', ' ', ' '],
        4: [' ', ' ', ' ', ' ', ' ', ' '],
        5: [' ', ' ', ' ', ' ', ' ', ' '],
        6: [' ', ' ', ' ', ' ', ' ', ' ']
        # all empty spaces are ' '
    }
    self._circleCountColl, self._circleCountD1 = 0, 0
    self._circleCountD2, self._circleCountRow = 0, 0
    self._history = []

  def change_position(self, x,y,x1,y1):
    self._board[x][y] = x1



  def is_full(self):
        for row in range(1, 7):
            for column in range(1, 7):
                if self._board[row][column] == ' ':
                    return False
        return True

  def display_board(self):
    #clr()
    print("""
  ░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗░█████╗░████████╗  ███████╗░█████╗░██╗░░░██╗██████╗░
  ██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗╚══██╔══╝  ██╔════╝██╔══██╗██║░░░██║██╔══██╗
  ██║░░╚═╝██║░░██║██╔██╗██║██╔██╗██║█████╗░░██║░░╚═╝░░░██║░░░  █████╗░░██║░░██║██║░░░██║██████╔╝
  ██║░░██╗██║░░██║██║╚████║██║╚████║██╔══╝░░██║░░██╗░░░██║░░░  ██╔══╝░░██║░░██║██║░░░██║██╔══██╗
  ╚█████╔╝╚█████╔╝██║░╚███║██║░╚███║███████╗╚█████╔╝░░░██║░░░  ██║░░░░░╚█████╔╝╚██████╔╝██║░░██║
  ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝░╚════╝░░░░╚═╝░░░  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝
  """)

    for x in self._board:
      print(*self._board[x], sep=" | ", end=" | \n \n")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")

  def enter_board(self, userInput, person):
    print(userInput)
    ypos = 0
    for ypos in reversed(self._board):
      try:
        if self._board[ypos][userInput] == ' ':
          self._board[ypos][userInput] = self.personDict[person]
          break
      except:
          break  

    self.win_check(person)
    #self.display_board()
    self.update_pieces_in_a_row(ypos, userInput, person)

  def update_pieces_in_a_row(self, ypos, userInput, person):
    self.piece_count(userInput, ypos, person)
  
  def get_valid_moves(self):
        valid_moves = []
        for column in self._board[0]:
            if isinstance(column, int):
                valid_moves.append(column)
        return valid_moves

            

  def piece_count(self, userInput, ypos, person):
    self._circleCountColl = self._circleCountRow = \
    self._circleCountD1 = self._circleCountD2 = 1
    rightDist, leftDist = 5 - userInput, 5 - (5 - userInput)
    botDist, topDist = 6 - ypos, 5 - (6 - ypos)

    # it just counts the amount of tokens in a certain direction x amount of times
    # the for loop breaks/stops when theres something other than its own token, stoping the counter
    # vertical win condition. can get away with this because there is gravity
    for x in range(botDist):
      if self._board[ypos+x+1][userInput] == \
      self._personDict[person]:
        self._circleCountColl += 1
      else:
        break
    # both are horizontal win condition
    for x in range(leftDist):
      if self._board[ypos][userInput-x-1] == \
      self._personDict[person]:
        self._circleCountRow += 1
      else:
        break
    for x in range(rightDist):
      if self._board[ypos][userInput+x+1] == \
      self._personDict[person]:
        self._circleCountRow += 1
      else:
        break
    # all 4 of these check the diagonal up right win condition or y = x diag
    for x in range(self.xy_diag_check(rightDist, topDist)):
      if self._board[ypos - x - 1][userInput + x + 1] == \
      self._personDict[person]:
        self._circleCountD1 += 1
      else:
        break
    for x in range(self.xy_diag_check(leftDist, botDist)):
      if self._board[ypos + x + 1][userInput - x - 1] == \
      self._personDict[person]:
        self._circleCountD1 += 1
      else:
        break
        # y = -x diag
    for x in range(self.xy_diag_check(leftDist, topDist)):
      if self._board[ ypos - x - 1][userInput - x - 1] == \
      self._personDict[person]:
        self._circleCountD2 += 1
      else:
        break
    for x in range(self.xy_diag_check(rightDist, botDist)):
      if self._board[ypos + x + 1][userInput + x + 1] \
      == self._personDict[person]:
        self._circleCountD2 += 1
      else:
        break

  def win_check(self, person):
    run = True
    if self._circleCountColl >= 4:
      print("\n \n~~~~~~~~~~~~~~~~ player " + str(person) +
            " has won vertically  ~~~~~~~~~~~~~~~~~~~~~~\n \n")
      run = False

    elif self._circleCountRow >= 4:
      print("\n \n~~~~~~~~~~~~~~~~ player " + str(person) +
            " has won horizontally  ~~~~~~~~~~~~~~~~~~~~~~\n \n")
      run = False
    elif self._circleCountD1 >= 4 or self._circleCountD2 >= 4:
      print("\n \n~~~~~~~~~~~~~~~~ player " + str(person) +
            " has won diagonally  ~~~~~~~~~~~~~~~~~~~~~~\n \n")
      run = False
    elif ' ' not in self._board[1]:
      #print(
      #    "\n \n~~~~~~~~~~~~~~~~ it's a draw buddy ~~~~~~~~~~~~~~~~~~~~~~\n \n"
     # )
      run = False
      #print(run)
    return run

  def is_draw(self):
    if ' ' not in self._board[1]:
      return False
    else:
      return True

  @property
  def circleCountD2(self):
    return self._circleCountD2

  @property
  def circleCountRow(self):
    return self._circleCountRow

  @property
  def circleCountD1(self):
    return self._circleCountD1

  @property
  def circleCountColl(self):
    return self._circleCountColl

  @property
  def getboard(self):
    return self._board
  # board info getter
  @property
  def board(self):
    return self._board

  # person info getter DOES NOT NEED GET IN THE FUNCTION NAME it is CONFUSING
  @property
  def personDict(self):
    return self._personDict

  @staticmethod
  def xy_diag_check(xDist, yDist):
    smallerCoord = xDist if xDist < yDist else yDist
    return smallerCoord

  # records all the player moves and updates the board.

  # connectBoard class is in the other file
  # HELP ME POLICE!!! THEY ARE GTA5ing my SHIT HELP ME HELP ME
