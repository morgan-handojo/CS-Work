

#  File: TestBinaryTree.py

#  Description: This code test a binary search tree with several functions, input should be in form of an input file 
# and is a single line of integers separated by a space

#  Student Name: Morgan Handojo

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 10/23/2023

#  Date Last Modified: 10/24/2023


""" this is the code"""

import sys

class Node():
    # constructor
    """This class is a Node"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        """this prints node"""
        if self.lchild is not None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild is not None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        """gets height of node"""
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        if self.lchild is not None:
            return 1 + self.lchild.get_height()
        if self.rchild is not None:
            return 1 + self.rchild.get_height()
        return 1


class Tree():
    # constructor
    """this is the tree"""
    def __init__(self):
        self.root = None

    def print(self, level):
        """prints tree"""
        self.root.print_node(level)

    def get_height(self):
        """gets height of tree"""
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        """inserts to tree"""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        parent = self.root
        curr = self.root
        # finds location to insert new node
        while curr is not None:
            parent = curr
            if data < curr.data:
                curr = curr.lchild
            else:
                curr = curr.rchild
        # inserts new node based on comparision to parent node
        if data < parent.data:
            parent.lchild = new_node
        else:
            parent.rchild = new_node
        return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree
    # minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        """finds range of tree"""
        if self.root is  None:
            return "Undefined"
        if self.root.lchild is None and self.root.rchild is None:
            return 0
        current = self.root
        while current.lchild is not None:
            current = current.lchild
        minimum = current.data
        current = self.root
        while current.rchild is not None:
            current = current.rchild
        maximum = current.data
        return maximum - minimum


    def get_level(self, level):
        """returns a list of certian lavels values"""
        my_list = self.level_helper(level, None, [])
        return my_list

    def level_helper(self, level, anode = None, my_list = []):
        """ helper for get_level function"""
        if self.root is None:
            return []
        height = self.get_height()
        if level > height - 1:
            return []
        if anode is None:
            anode = self.root

        if level == 0 and isinstance(anode, Node):
            number = anode
            my_list.append(number)

        if level > 0:
            if anode.lchild is None and anode.rchild is not None:
                self.level_helper(level - 1, anode.rchild, my_list)

            if anode.rchild is None and anode.lchild is not None:
                self.level_helper(level-1, anode.lchild, my_list)

            if anode.rchild is not None and anode.lchild is not None:
                self.level_helper(level - 1, anode.lchild, my_list)
                self.level_helper(level-1, anode.rchild, my_list)

        return my_list

    def left_helper(self, level, anode = None, my_list = []):
        """ helper for get_level function"""
        if self.root is None:
            return []
        height = self.get_height()
        if level > height - 1:
            return []
        if anode is None:
            anode = self.root

        if level == 0 and isinstance(anode, Node):
            number = anode.data
            my_list.append(number)

        if level > 0:
            if anode.lchild is None and anode.rchild is not None:
                self.left_helper(level - 1, anode.rchild, my_list)

            if anode.rchild is None and anode.lchild is not None:
                self.left_helper(level-1, anode.lchild, my_list)

            if anode.rchild is not None and anode.lchild is not None:
                self.left_helper(level - 1, anode.lchild, my_list)
                self.left_helper(level-1, anode.rchild, my_list)

        return my_list




    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        """left side view of tree"""
        if self.root is None:
            return []

        height = self.get_height()
        out_list = []
        for x in range(height):
            level_list = []
            level_list = self.left_helper(x, None, [])
            out_list.append(level_list[0])
        return out_list


    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self, anode = None):
        """sum of leaf nodes on tree"""
        if self.root is None:
            return 0
        if anode is None:
            anode = self.root
        if anode.lchild is not None and anode.rchild is None:
            return self.sum_leaf_nodes(anode.lchild)
        if anode.rchild is not None and anode.lchild is None:
            return self.sum_leaf_nodes(anode.rchild)
        if anode.lchild is not None and anode.rchild is not None:
            return self.sum_leaf_nodes(anode.lchild) + self.sum_leaf_nodes(anode.rchild)
        return anode.data

def make_tree(data):
    """make tree"""
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    """the main"""
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    # line = "50 30 70 10 40 60 80 7 25 38 47 58 65 77 96"
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# # Another Tree for test.
#     line = sys.stdin.readline()
#     line = line.strip()
#     line = line.split()
#     tree2_input = list(map(int, line)) 	# converts elements into ints
#     t2 = make_tree(tree2_input)
#     t2.print(t2.get_height())

#     print("Tree range is: ",   t2.range())
#     print("Tree left side view is: ", t2.left_side_view())
#     print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
#     print("##########################")
# # Another Tree
#     line = sys.stdin.readline()
#     line = line.strip()
#     line = line.split()
#     tree3_input = list(map(int, line)) 	# converts elements into ints
#     t3 = make_tree(tree3_input)
#     t3.print(t3.get_height())

#     print("Tree range is: ",   t3.range())
#     print("Tree left side view is: ", t3.left_side_view())
#     print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
#     print("##########################")


if __name__ == "__main__":
    main()
