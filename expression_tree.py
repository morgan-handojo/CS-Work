#  File: ExpressionTree.py

#  Description: this makes an expression tree and also evaluates it

#  Student Name: Morgan Handojo

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 10/16/23

#  Date Last Modified: 10/19/23

"""
input example: ( ( 8 + 3 ) * ( 7 - 2 ) )
"""

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack ():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

class Node ():
    def __init__ (self, data = None, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

    def print_node(self, level=0):
        if self.rchild is not None:
            self.rchild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.data)

        if self.lchild is not None:
            self.lchild.print_node(level + 1)

    def public_method(self):
        return True

class Tree():
    def __init__ (self):
        self.root = None

    def create_tree (self, expr):
        self.root = Node()
        current = self.root
        my_stack = Stack()
        expr_list = expr.split(" ")
        for item in expr_list:
            if item == "(":
                current.lchild = Node()
                my_stack.push(current)
                current = current.lchild
            elif item in operators:
                current.data = item
                my_stack.push(current)
                current.rchild = Node()
                current = current.rchild
            elif item == ")":
                if not my_stack.is_empty():
                    current = my_stack.pop()
            else: # if an operand
                current.data = item
                current = my_stack.pop()


    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated

    #['+', '-', '*', '/', '//', '%', '**']
    def evaluate (self, anode):

        current = anode

        if current.data in operators:
            if current.data == "+":
                return self.evaluate(current.lchild) + self.evaluate(current.rchild)

            if current.data == "-":
                return self.evaluate(current.lchild) - self.evaluate(current.rchild)

            if current.data == "*":
                return self.evaluate(current.lchild) * self.evaluate(current.rchild)

            if current.data == "/":
                return self.evaluate(current.lchild) / self.evaluate(current.rchild)

            if current.data == "//":
                return self.evaluate(current.lchild) // self.evaluate(current.rchild)

            if current.data == "%":
                return self.evaluate(current.lchild) % self.evaluate(current.rchild)

            if current.data == "**":
                return self.evaluate(current.lchild) ** self.evaluate(current.rchild)
        return float(current.data)

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, anode):

        if anode:
        # if node is an operator
            if anode.data in operators:
                return str(anode.data) + " " + self.pre_order(anode.lchild) + " " + \
                    self.pre_order(anode.rchild)
        # if node is an operand
            return str(anode.data)
        return ''

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, anode):

        if anode:
            # if node is an operator
            if anode.data in operators:
                return self.post_order(anode.lchild) + self.post_order(anode.rchild) + \
                    str(anode.data) + " "
            # if node is an operand
            return str(anode.data) + " "
        return ''




def main():
    # read infix expression
    # this takes in a txt file, usually input just looks like this: ( ( 8 + 3 ) * ( 7 - 2 ) )
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
