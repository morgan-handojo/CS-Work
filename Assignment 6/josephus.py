"""
File: josephus.py
Description: computational representation of the Josephus problem using a circular linked list
Student name: Morgan Handojo

Course Name: CS 313E
Unique Number: 52590
Date Created: 10/9/2023
Date Last Modified: 10/10/2023
"""

import sys

class Link():
    ''' This class represents a link between data items only.'''
    def __init__ (self, data, next_link = None):
        self.data = data
        self.next = next_link

    def __str__(self):
        ''' Print the data contained in this link.'''
        return str(self.data)

    def public_method(self):
        ''' Print the data contained in this link.'''
        return 100


class CircularList():
    ''' Circular List'''
    # Constructor
    def __init__ ( self ):
        self.first = None
    # Insert an element (value) in the list
    def insert ( self, data ):
        '''Insert the data at the end of a circularly linked list.'''

        new_link = Link(data)
        if self.first is None:
            self.first = new_link
            new_link.next = new_link
            return
        current = self.first
        while current.next != self.first:
            current = current.next
        current.next = new_link
        new_link.next = self.first


    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        '''Find to which data is the link of a given data inside this linked list.'''
        current = self.first
        if current is None:
            return None

        # Search and find the position of the given data, the get the link if.
        while current.data != data:
            if current.next == self.first:
                return None

            current = current.next

        return current

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete ( self, data ):
        '''Removes the data from the list if exist and fix the link problems.'''

        current = self.first
        previous = self.first

        if current is None:
            return None

        while current.data != data:
            if current.next == self.first:
                return None

            previous = current
            current = current.next

        if current == self.first:
            if current.next == self.first:
                self.first = None
            else:
                self.first = self.first.next

        else:
            previous.next = current.next

        return current

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after ( self, start, elim_num ):
        ''' delete after'''
        current = self.find(start)

        if current is None:
            return None, None

        for i in range(elim_num-2):
            current = current.next

        deleted_link = current.next
        next_link = deleted_link.next
        deleted_data = deleted_link.data
        current.next = next_link

        return deleted_data, next_link

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__ ( self ):
        ''' str maker'''
        print_list = []
        if self.first is None:
            return str(print_list)
        current = self.first
        print_list.append(current.data)
        while current.next != self.first:
            current = current.next
            print_list.append(current.data)

        return str(print_list)

def main():
    ''' Main'''
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)



    # your code
    my_list = CircularList()
    for i in range(1,num_soldiers +1):
        my_list.insert(i)



    data = start_count
    while num_soldiers > 0:
        data, next_link = my_list.delete_after(data, elim_num)
        print(data)
        data = next_link.data
        num_soldiers -= 1


if __name__ == "__main__":
    main()
