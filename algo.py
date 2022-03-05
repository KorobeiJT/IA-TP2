def AC3(csp, queue=None):

    if queue == None:
        queue = csp.binaryConstraint

    while queue:

        (xi, xj) = queue.pop(0)
        if remove_inconsistent_values(csp, xi, xj): 

            if len(csp.possibilities[xi]) == 0:
                return False
            
            for Xk in csp.clashingCells[xi]:
                if Xk != xi:
                    queue.append((Xk, xi))
                    
    return True


def remove_inconsistent_values(csp, cell1, cell2):

    removed = False
    for values1 in csp.possibilities[cell1]:
        if not any([(values1!=values2) for values2 in csp.possibilities[cell2]]):
            csp.possibilities[cell1].remove(values1)
            removed = True

    return removed

def backtrack(assignment, sudoku, unassigned):

    # if assignment is complete then return assignment
    if len(assignment) == len(sudoku.coord):
        return assignment
    # var = select-unassigned-variables(csp)

    unassigned = []
    for cell in sudoku.coord:
        if cell not in assignment:
            unassigned.append(cell)
    cell = unassigned.pop(0)

    # for each value in order-domain-values(csp, var)
    for value in sudoku.possibilities[cell]:

       
        isConsistent = True
        for othercell, othervalue in assignment.items():

            # if the values are the equal and the cells are related to each other
            if othervalue == value and othercell in sudoku.clashingCells[cell]:

                # then cell is not consistent
                isConsistent = False

        if isConsistent:

            # add {cell = value} to assignment
            assignment[cell]=value

            # result = backtrack(assignment, csp)
            result = backtrack(assignment, sudoku, unassigned)

            # if result is not a failure return result
            if result:
                return result

            # remove {cell = value} from assignment
            del assignment[cell]
            unassigned.append(cell)
   
    # return failure
    return False