import math
import copy
class TicTacTo_ai():

   def __init__(self):
      self.board = [
      ["-", "-", "-"],
      ["-", "-", "-"],
      ["-", "-", "-"],
   ]
      self.human = "X"
      self.ai = "O"
      self.current = self.human

   def display(self):
      for row in self.board:
         for col in row:
            print(col, end=" ")
         print()

   def score(self, current_state):
      if self.is_winner(current_state) == "X":
         return -10
      elif self.is_winner(current_state) == "O":
         return 10
      else:
         return 0
      
   def is_winner(self, current_state):
      for i in range(3):
         if current_state[0][i] == current_state[1][i] == current_state[2][i] != "-":
            return current_state[0][i]
      for i in range(3):
         if current_state[i][0] == current_state[i][1] == current_state[i][2] != "-":
            return current_state[i][0]
      if current_state[0][0] == current_state[1][1] == current_state[2][2] != "-":
         return current_state[0][0]
      elif current_state[0][2] == current_state[1][1] == current_state[2][0] != "-":
         return current_state[0][2]
      return None
   
   def board_full(self, current_state):
      for row in current_state:
         for col in row:
            if col == "-":
               return False
      return True
        
   def game_over(self, current_state):
      if self.is_winner(current_state) != None:
         return True
      elif self.board_full(current_state) == True:
         return True

   def available_move(self, temp_state):
      moves = []
      for row in range(3):
         for column in range(3):
            if temp_state[row][column] == "-":
               moves.append((row, column))
      return moves
               

   def min_value(self, current_state):
      if self.game_over(current_state):
         return {"value": self.score(current_state), "move": None}
      
      temp_state = temp_state = copy.deepcopy(current_state)
      #value = math.inf
      best_score = math.inf
      best_move = []
      
      for move in self.available_move(temp_state):
         temp_state[move[0]][move[1]] = "X"
         value = self.max_value(temp_state)["value"]
         if value<best_score:
               best_score = value
               best_move = move
      return {"value": best_score, "move": best_move}

   def max_value(self, current_state):
      if self.game_over(current_state):
         return {"value": self.score(current_state), "move": None}
      
      #value = -math.inf
      temp_state = copy.deepcopy(current_state)
      best_score = -math.inf
      best_move = []
      

      for move in self.available_move(temp_state): 
         temp_state[move[0]][move[1]] = "O"
         value = self.min_value(temp_state)["value"]
         if value>best_score:
            best_score = value
            best_move = move
      current_state[best_move[0]][best_move[1]] = "O"
      return {"value": best_score, "move": best_move}
   

   def play(self):
      while True:
         if self.current == self.human:
            i = int(input("row to put mark on: "))
            j = int(input("column to put mark on: "))
            if self.board[i][j] == "-":
               self.board[i][j] = "X"
            self.current = self.ai
         else:
            self.max_value(self.board)
            self.current = self.human
         
         self.display()
         print()

         if self.is_winner(self.board) == "X":
            print ("player 'X' wins")
            break
         
         elif self.is_winner(self.board) == "O":
            print ("Player 'O' wins")
            break
                  
         elif self.board_full(self.board) and self.is_winner(self.board)==None:
            print ("It's a tie!")
            break

game1 = TicTacTo_ai()
game1.play()