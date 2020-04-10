#!/usr/bin/env python3
import sys

sys.tracebacklimit = 0


class node():
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op


class parser():
    def __init__(self, input):

        self.input_list = input.split(" ")

        # print(self.input_list)

    def AST(self):
        curr_node = node(None, None, "root")

        for i in self.input_list:
            # print(i.lstrip('-+'))

            if i.lstrip('-+').isdigit():
                new_node = node(None, None, i)
                if curr_node.op == "root":
                    curr_node = new_node
                elif curr_node.op == "*":
                    curr_node.right = new_node
                    if parent_node.op != None:
                        curr_node = parent_node

                else:
                    curr_node.right = new_node
                # print("integer",curr_node.op)
            elif i == "+":
                new_node = node(None, None, "+")

                new_node.left = curr_node
                curr_node = new_node
                # print("+",curr_node.op)
            elif i == "*":
                new_node = node(None, None, "*")
                parent_node = node(None, None, None)
                if curr_node.op.lstrip('-+').isdigit():

                    new_node.left = curr_node
                    curr_node = new_node
                else:
                    parent_node = curr_node
                    new_node.left = curr_node.right
                    curr_node.right = new_node
                    curr_node = new_node
                # print("*", curr_node.op)
            elif i == "-":
                new_node = node(None, None, "-")

                new_node.left = curr_node
                curr_node = new_node
                # print("-", curr_node.op)
            else:
                Exception("Not a valid operator")

        return curr_node

    def evaluate_AST(self, curr_node):
        # print(curr_node.op)

        if curr_node.op == "+":
            return (self.evaluate_AST(curr_node.left) + self.evaluate_AST(curr_node.right))
        elif curr_node.op == "-":
            return (self.evaluate_AST(curr_node.left) - self.evaluate_AST(curr_node.right))
        elif curr_node.op == "*":
            return (self.evaluate_AST(curr_node.left) * self.evaluate_AST(curr_node.right))
        else:
            return int(curr_node.op)


def main():
    while True:
        try:
            # Taking raw inputs
            text = input("")
        except EOFError:
            break

    object = parser(text)

    root_node = object.AST()
    output2 = object.evaluate_AST(root_node)

    print(str(output2))


if __name__ == '__main__':
    main()
