"""
  File: intervals.py
  Description: this python file creates and sorts a list of tuples representing intervals, 
  condenses them down, and also sorts the condensed list based on the length of the intervals


  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 9/5/23
  Date Last Modified: 9/5/23

    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys

def merge_tuples(tuples_list):
    """Merge the tuples"""

    tuples_list.sort()

    i = 1
    list_length = len(tuples_list)
    while i < (list_length):
        if tuples_list[i][0] > tuples_list[i-1][1]:
            i += 1
            continue

        if tuples_list[i][1] > tuples_list[i-1][1]:
            tuples_list[i-1] = (tuples_list[i-1][0],tuples_list[i][1])

        tuples_list.remove(tuples_list[i])
        list_length = len(tuples_list)

    return tuples_list



def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """
    length_list = []
    final_list = []
    i_count = 0
    for i, thing in enumerate(tuples_list):
        length = abs(thing[0]- thing[1])
        length_list.append((length, thing))
        i_count += i


    length_list.sort()

    #for i in range(len(length_list)):
    for i, thing in enumerate(length_list):
        final_list.append(thing[1])

    return final_list



def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
