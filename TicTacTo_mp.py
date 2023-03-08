class TicTacTo:
    def __init__(self):
      self.board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
      ]
      self.player = "X"
      self.other = "O"
      self.current = self.other
   
    def display(self):
       for row in self.board:
          for col in row:
             print(col, end=" ")
          print()

    def board_full(self, current_state):
       for row in self.board:
          for col in row:
             if col == "-":
                return False
       return True
    
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
    
    def play(self):       
         while True:
            i = int(input("row to put mark on: "))
            j = int(input("column to put mark on: "))
            if self.board[i][j]== "-":
               if self.current == self.player:
                self.board[i][j] = "X"
                self.current = self.other
               else:
                self.board[i][j] = "O"
                self.current = self.player
            else:
               print("already marked!")

            self.display()

            if self.is_winner() == "X":
               print ("player 'X' wins")
               break
            
            elif self.is_winner() == "O":
               print ("Player 'O' wins")
               break
                     
            elif self.board_full() and self.is_winner()==None:
               print ("It's a tie!")
               break
        
           
game = TicTacTo()
game.play()