class Puzzle:
    def __init__(self,numbers):
      self.cells=[]
      self.blanklocation=0
      k=0
      for i in range(3):
          row=[]
          for j in range(3):
              row.append(numbers[k])
              if numbers[k]==0:
                  self.blanklocation=i,j
              k+=1
          self.cells.append(row)


    def printState(self):
        lines=[]
        horizontalline=("_"*(11))
        print(horizontalline)
        for row in self.cells:
            rowline="|"
            print(row)
            for col in row:
                print(col)
                if col==0:
                    col="."
                rowline=rowline+" "+col.__str__()+"|"
            # print(rowline)
            print(horizontalline)


    def isGoal(self):
        current=0
        for i in range(3):
            for j in range(3):
                if current!=self.cells[i][j]:
                    print("not goal")
                    return False
                current+=1
            print("goal")
            return True
    def legalMoves(self):
        pass
    def resultState(self):
        pass


numbers=[4,3,2,1,5,0,7,8,9]
puzzle=Puzzle(numbers)
puzzle.printState()
puzzle.isGoal()

