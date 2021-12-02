class Queue:
    def __init__(self):
        """
        A queue uses a first in first out logic. That means, items that appeared first are removed first.
        """
        self.items = []

    def is_empty(self):
        """
        Checks to see if the queue is empty
        :return: True: if queue is empty. False: Otherwise
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Adds an item to the queue.
        :param item: Value to be added to the queue.
        :return: No value is added.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove the first item on the queue
        :return:
        """
        return self.items.pop(0)

    def peek(self):
        """
        View the first item on the list
        :return:
        """
        return self.items[0]

    def __len__(self):
        return len(self.items)