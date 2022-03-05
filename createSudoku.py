import turtle
from random import randint, shuffle
from time import sleep

grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print( str(grid[i][j]) + " ", end="")
            if (j%3==2 and j!=8):
                print("| ", end="")
        print()
        if (i%3==2 and i!=8):
            print("- - - - - - - - - - -")