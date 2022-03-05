import random
from random import randint, shuffle
from algo import AC3, backtrack
from csp import CSP
grid2 = []

def randomGridGenerate():
    result = []
    positions = [0,1,2,3,4,5,6,7,8]
    values = [1,2,3,4,5,6,7,8,9]

    for i in range(9):
        line = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        a = random.randint(0, len(positions)-1)
        b = random.randint(0, len(values)-1)
        pos = positions[a]
        val = values[b]
        line[pos] = val
        positions.remove(pos)
        values.remove(val)
        result.append(line)

    return result

def getGridFromFile():
    grid2 = []
    path = input("Enter .txt file path :")
    print("Path is: " + path)
    
    file = open(path, "r")
    lines = file.read().splitlines()
    for line in lines:
        grid2.append(line.split(", "))        
    
    for i in range(9):
        for j in range(9):
            grid2[i][j] = int(grid2[i][j])
    return grid2

def printGrid(grille):
    for i in range(9):
        for j in range(9):
            print( str(grille[i][j]) + " ", end="")
            if (j%3==2 and j!=8):
                print("| ", end="")
        print()
        if (i%3==2 and i!=8):
            print("- - - - - - - - - - -")


def AC3NotEnough(csp):

    assignment = {}

    for cell in csp.coord:
        if len(csp.possibilities[cell]) == 1:
            assignment[cell] = csp.possibilities[cell][0]
    
    unassigned = []
    for cell in csp.coord:
        if cell not in assignment:
            unassigned.append(cell)

    assignment = backtrack(assignment, csp, unassigned)
    
    return assignment


def CommitSudoku():  
    if AC3(csp):
        print("AC-3 finished!")
        isFinished=True
        for values in csp.possibilities.values():
            if(len(values)>1):
                isFinished=False
                break

        if isFinished:
            print("Result:")
            for keys, values in csp.possibilities.items():  
                grid2[keys[0]][keys[1]]=values[0]
            printGrid(grid2)
        else:
            print("Starting backtracking...")
            assignement= AC3NotEnough(csp)
            print("Result:")
            for key, value in assignement.items():  
                grid2[key[0]][key[1]]=value
            printGrid(grid2)



choice = input ("Random initial grid (1) or chosen from txt file (2)?: ")
if (choice == "2"):
    grid2 = getGridFromFile()
    printGrid(grid2)
else:
    grid2 = randomGridGenerate()
    printGrid(grid2)

csp = CSP()
csp.genCoordinates()
csp.genConstraint()
csp.genBinaryConstraints()
csp.genPossibleValues(grid2)
CommitSudoku()