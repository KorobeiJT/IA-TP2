rows = "123456789"
cols = "ABCDEFGHI"

def genCoordinates():

    all_coords = []
    for row in range(9):
        for col in range(9):
            new_coords = (row, col)
            all_coords.append(new_coords)
    return all_coords

    
def genPossibleValues(grid, coords, constraints):

    possibilities = dict()

    for cell in coords:
        
        if grid[cell[0]][cell[1]] == 0:
            possibilities[cell] = list(range(1,10))
            for othercell in constraints[cell]:
                if ((grid[othercell[0]][othercell[1]] != 0) and (grid[othercell[0]][othercell[1]] in possibilities[cell])):
                    possibilities[cell].remove(grid[othercell[0]][othercell[1]])
        else:
            possibilities[cell] = [grid[cell[0]][cell[1]]]

    return possibilities

def getSquare(cell):

    Squares = {1: [[0,1,2],[0,1,2]], 2: [[0,1,2],[3,4,5]], 3: [[0,1,2],[6,7,8]],
               4: [[3,4,5],[0,1,2]], 5: [[3,4,5],[3,4,5]], 6: [[3,4,5],[6,7,8]],
               7: [[6,7,8],[0,1,2]], 8: [[6,7,8],[3,4,5]], 9: [[6,7,8],[6,7,8]] }

    for key,value in Squares.items():
        if (cell[0] in value[0] and cell[1] in value[1]):
            return key

def genConstraint(coords):

    ConstraintPerCells= dict()

    for cell in coords:
        ConstraintPerCells[cell]=[]
        for othercell in coords:
            if(othercell[0]==cell[0] and cell!=othercell):
                ConstraintPerCells[cell].append(othercell)
            if(othercell[1]==cell[1] and cell!=othercell):
                ConstraintPerCells[cell].append(othercell)
            if(getSquare(cell)==getSquare(othercell) and cell!=othercell):
                ConstraintPerCells[cell].append(othercell)
    
    return ConstraintPerCells


def genBinaryConstraints(constraintDict):

    allBinaryConstraint=list()
    for cell,values in constraintDict.items():
        for othercell in values:
            if (cell,othercell) not in allBinaryConstraint:
                allBinaryConstraint.append((cell,othercell))
    
    return allBinaryConstraint
