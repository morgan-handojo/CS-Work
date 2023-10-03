"""
File: work.py
Description: compares efficiency of linear vs binary search, figures out
    the minimum allowable value of val for a given productivity factor (konstant) that 
    will allow at least num lines of code to be written

Course Name: CS 313E
Unique Number: 52590
Date Created: 10/2/2023
Date Last Modified: 10/2/2023
"""

import sys
import time


#   Input: val an integer representing the minimum lines of code and
#        konstant an integer representing the productivity factor
#   Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (val, konstant):
    """returns sum of the series (v + v // k + v // k**2 + ...)"""
    counter = 0
    my_sum = 0
    while val // (konstant ** counter) != 0:
        my_sum += val // (konstant ** counter)
        counter += 1

    return my_sum


# Input: num an integer representing the total number of lines of code
#        konstant an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, konstant):
    """performs linear search"""
    my_list = list(range(1,n+1))
    for thing in my_list:
        written = sum_series(thing,konstant)
        if written >= n:
            return thing
        
    return None



# Input: num an integer representing the total number of lines of code
#        konstant an integer representing the productivity factor
# Output: returns val the minimum lines of code to write using binary search
def binary_search (num, konstant):
    """performs binary search"""
    my_list = list(range(1,num+1))
    low = 0
    high = num

    while low <= high:
        middle = (low + high) // 2
        middle_value = my_list[middle]
        current_val = sum_series(middle_value, konstant)
        if current_val < num:
            low = middle + 1
        elif current_val > num:
            high = middle - 1

        else:
            return my_list[middle]
    # we want the previously used value before the final high/low shift that exits while loop
    return middle_value + 1



def main():
    """
    input would be like:
    3
    30 2
    72 10
    16 8
    """
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        num = int(inp[0])
        konstant = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(num, konstant)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(num, konstant)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
    main()
