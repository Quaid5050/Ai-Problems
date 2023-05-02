class  PuzzleState:
    def __init__(self,numbers):
        print("puzzle initialize")
        self.cells=[]
        self.blankLocation=0
        k=0
        for i in range(3):
            row=[]
            for j in range(3):
                row.append(numbers[k])
                if numbers[k]==0:
                    self.blankLocation=i,j
                k+=1
            self.cells.append(row)

    def printState(self):
        print("printstate")
        lines=[]
        horizontalline=("_"*(13))
        print(horizontalline)
        for row in self.cells:
            rowline="|"
            for  col in row:
                if col ==0:
                    col="."
                rowline=rowline + " "+col.__str__()+"|"
            print (rowline)
            print (horizontalline)


    def testMakePuzzle(self,numbers):
        print(numbers)
        k=0
        for i in range(3):
            row=[]
            print("i is -----------------{}".format(i))
            for j in range(3):
                print("value of k is {}".format(k))
                row.append(numbers[k])
                print(numbers[k])
                k+=1
            print("value of row is -----{}".format(row))
            self.cells.append(row)
        print("cells are {}".format(self.cells))

    def testPrintState(self):
        lines=[]
        hzline=("_"*(13))
        for row in self.cells:
            rowline="|"
            # print("row {}".format(row))
            for col in row:
                # print("col {}".format(col))
                if col==0:
                    col="."
                rowline=rowline+""+col.__str__()+"|"
            print(rowline)
            print(hzline)



    def isGoal(self):
        print("IsGoal--------?")
        current=0
        for i in range(3):
            for j in range(3):
                if current !=self.cells[i][j]:
                    print("not goal ")
                    return False
                current +=1
            print("goal found")
            return True


    def legalMoves(self):
        print()
        print("----- Legal Moves -----")
        #check blank location
        row,col=self.blankLocation
        legalMoves=[]
        if row!=0:
            legalMoves.append("up")
        if row!=2:
            legalMoves.append("down")
        if col!=0:
            legalMoves.append("left")
        if col!=2:
            legalMoves.append("right")
        print(legalMoves)

    def resultState(self,move):
        print("result state")
        row,col=self.blankLocation
        if move=="up":
            newrow=row-1
            newcol=col
        elif move=="down":
            newrow=row+1
            newcol=col
        elif move=="left":
            newrow=row
            newcol=col-1
        elif move=="right":
            newrow=row
            newcol=col+1

        else:
            raise "invalid move"
        newPuzzle=PuzzleState([0,0,0,0,0,0,0,0,0])
        newPuzzle.cells=[value[:] for value in self.cells]
        newPuzzle.cells[row][col]= self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol]=self.cells[row][col]
        newPuzzle.blankLocation=newrow,newcol
        # print(newPuzzle.blankLocation)
        # newPuzzle.printState()
        # print(newPuzzle.cells)
        isGoal=newPuzzle.isGoal()
        while not isGoal:
            newPuzzle.printState()
            newPuzzle.isGoal()
            newPuzzle.legalMoves()
            move=input("Enter move")
            newPuzzle.resultState(move)

class SearchProblem:
    def __init__(self,state):
        print("search problem class")
        self.puzzle=state
    def getStartstate(self):
        print("start state")
        return self.puzzle
    def getSuccessors(self,state):
        print("getSuccessors")

    def isGoalState(self):
        print("isGoalstate")

numbers=[5,1,2,9,0,4,6,7,3]
numbers2=[0,1,2,3,4,5,6,7,8]
puzzle= PuzzleState(numbers)
# puzzle.printState()
# puzzle.isGoal()
# isGoal=puzzle.isGoal()
# print(isGoal)
# puzzle.legalMoves()
# move=input("Enter move---")
# puzzle.resultState(move)

p=SearchProblem(puzzle)
state=p.getStartstate()
state.printState()







# puzzle.testMakePuzzle(numbers)
# puzzle.testPrintState()
