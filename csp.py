class CSP:
    binaryConstraint=list()
    clashingCells=dict()
    coord=list()
    possibilities=dict()

    @classmethod
    def genCoordinates(self):
        
        for row in range(9):
            for col in range(9):
                self.coord.append((row, col))
        return self.coord

    @classmethod    
    def genPossibleValues(self, grid):

        
        for cell in self.coord:
            
            if grid[cell[0]][cell[1]] == 0:
                self.possibilities[cell] = list(range(1,10))
                for othercell in self.clashingCells[cell]:
                    if ((grid[othercell[0]][othercell[1]] != 0) and (grid[othercell[0]][othercell[1]] in self.possibilities[cell])):
                        self.possibilities[cell].remove(grid[othercell[0]][othercell[1]])
            else:
                self.possibilities[cell] = [grid[cell[0]][cell[1]]]
    @classmethod
    def genConstraint(self):


        for cell in self.coord:
            self.clashingCells[cell]=[]
            for othercell in self.coord:
                if(othercell[0]==cell[0] and cell!=othercell):
                    self.clashingCells[cell].append(othercell)
                if(othercell[1]==cell[1] and cell!=othercell):
                    self.clashingCells[cell].append(othercell)
                if(getSquare(cell)==getSquare(othercell) and cell!=othercell):
                    self.clashingCells[cell].append(othercell)

    @classmethod
    def genBinaryConstraints(self):

        for cell,values in self.clashingCells.items():
            for othercell in values:
                if (cell,othercell) not in self.binaryConstraint:
                    self.binaryConstraint.append((cell,othercell))


def getSquare(cell):

        Squares = {1: [[0,1,2],[0,1,2]], 2: [[0,1,2],[3,4,5]], 3: [[0,1,2],[6,7,8]],
                4: [[3,4,5],[0,1,2]], 5: [[3,4,5],[3,4,5]], 6: [[3,4,5],[6,7,8]],
                7: [[6,7,8],[0,1,2]], 8: [[6,7,8],[3,4,5]], 9: [[6,7,8],[6,7,8]] }

        for key,value in Squares.items():
            if (cell[0] in value[0] and cell[1] in value[1]):
                return key