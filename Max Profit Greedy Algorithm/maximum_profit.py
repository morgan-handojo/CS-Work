"""

  File: maximum_profit.py
  Description: this is a greedy algorithm designed to calculate the maximum possible profit by purchasing a subset of the listed houses and selling them the next year.

  Student Name: Morgan Handojo
  
  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 11/13/2023
  Date Last Modified: 11/13/2023

  
  input file format:
  The first line is the amount of investment in million USD which is an integer number.
  The second line includes an integer number which is the number of houses listed for sale.
  The third line is a list of house prices in million dollar which is a list of integer numbers (Consider that house prices can be an integer number in million dollar only).
  The fourth line is a list of 1-year forecasted value increase for each of the listed houses in perce
"""
import sys


# Add Your functions here
def max_profit_func(money, num_houses, prices, increase):

    future_val = []
    for x in range(len(prices)):
        future_val.append(prices[x]*increase[x]/100)
    matrix = [[0 for x in range(money+1)] for x in range(num_houses+1)]

    for house in range(num_houses+1):
        for thing in range(money+1):
            if house == 0 or thing == 0:
                matrix[house][thing] = 0
            elif prices[house-1]<= thing:
                matrix[house][thing] = max(matrix[house-1][thing], future_val[house-1] + \
                                           matrix[house-1][thing-prices[house-1]])
            else:
                matrix[house][thing] = matrix[house-1][thing]

    return float("%.2f" % (matrix[num_houses][money]))




# You are allowed to change the main function.

# Do not change the template file name.

def main():
    """lol"""

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)


    # The third line is a list of house prices in million dollar which is a list of
    # \textit{integer numbers}
    # (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])



    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])
    # money = 12
    # num_houses = 4
    # prices = [6,3,4,5]
    # increase = [12,6,1,9]

    # print(max_profit_func(money,num_houses,prices,increase))




# Add your implementation here ....
    result = max_profit_func(money,num_houses,prices,increase)

# Add your functions and call them to generate the result.

    print(result)


main()
