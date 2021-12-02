# Implementation of a stack ADT
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Checks to see if stack is empty or not.
        :return: True if stack is empty. False otherwise.
        """
        return self.items == []

    def push(self, item):
        """
        Inserts an item at the top of the stack. In this case, the end of the list.
        :param item: Value to be added.
        :return: Nothing.
        """
        self.items.append(item)

    def pop(self):
        """
        Returns the last item in the stack which is the most recently addded. This is because the stack uses the
        first in first out logic.
        :return:
        """
        return self.items.pop()

    def peek(self):
        """
        To be used to view the most recently added item.
        :return: Returns the last element in the stack.
        """
        return self.items[-1]

    def size(self):
        """
        Checks the number of items in the stack.
        :return: Returns a number.
        """
        return len(self.items)