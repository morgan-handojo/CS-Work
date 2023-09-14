"""
  File: spiral.py
  Description: this python file creates a 2D list base on a given dimension,
  and then sums the numbers of all adjacent indexes for an inputed value

  Student Name: Morgan Handojo
  Student UT EID: mlh5384

  Partner Name: Kara Fowler
  Partner UT EID: knf747

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 8/29/23
  Date Last Modified: 8/30/23

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n
"""

import copy

def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""
    lists = list(map(lambda _: 1, range(dim)))
    matrix = []
    thing_counter = 0

    for thing in range(dim):
        new_list = copy.deepcopy(lists)
        matrix.append(new_list)
        thing_counter += thing


    space = 1
    row = int(dim // 2 )
    column = int(dim // 2)
    move_counter = 0


    while space < dim**2 and dim > 0:
        #if space != (dim**2 - dim):
        if matrix[0][0] == 1:
            move_counter += 1
            #move right
            for thing in range(move_counter):
                space += 1
                column += 1
                matrix[row][column] = space
            #move Down
            for thing in range(move_counter):
                space += 1
                row += 1
                matrix[row][column] = space
            move_counter += 1
            #move left
            for thing in range(move_counter):
                space += 1
                column -= 1
                matrix[row][column] = space
            #move up
            for thing in range(move_counter):
                space += 1
                row -= 1
                matrix[row][column] = space

        else:
            for thing in range(move_counter):
                space += 1
                column += 1
                matrix[row][column] = space

    return matrix


def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """


    index_sum = 0

    if val < 1 or val > grid[0][len(grid) - 1]:
        return 0

    for thing in range(len(grid)):
        if val in grid[thing]:
            index_row = thing
            index_column = grid[thing].index(val)


    # middle row case
    if (index_row - 1) >= 0:
        index_sum += grid[index_row - 1][index_column]
        #lower row
    if (index_row + 1) < len(grid):
        index_sum += grid[index_row + 1][index_column]



    #if left edge for middle row
    if (index_column - 1) >= 0:
        index_sum += grid[index_row][index_column - 1]

        #upper row
        if (index_row - 1) >= 0:
            index_sum += grid[index_row - 1][index_column - 1]

        #lower row
        if (index_row + 1) < len(grid):
            index_sum += grid[index_row + 1][index_column - 1]



    # right edge for middle row
    if (index_column + 1) < len(grid):
        index_sum += grid[index_row][index_column + 1]
        #upper row
        if (index_row - 1) >= 0:
            index_sum += grid[index_row - 1][index_column + 1]
        #lower row
        if (index_row + 1) < len(grid):
            index_sum += grid[index_row + 1][index_column + 1]


    return index_sum





def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
