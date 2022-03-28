import numpy as np
import io

def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l


def sudoku(table):
    arr = []
    buf = io.StringIO(table)
    for i in buf.readlines():
        if i == '\n':
            continue


        line = i[:17].replace(" ", "")
        arr.append( [int(char) for char in line] )
        
    arr = np.array(list(arr))

    # count num of zeros
    num_of_zeros = np.where(arr==0)[0].size
    # print(num_of_zeros)

    # solv sudoku (with random array of num of zeros)
    fully_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for line in arr:
        print( fully_numbers - set(line))
        
    




Table =  """
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
"""

print(sudoku(Table))



