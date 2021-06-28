from typing import Any


class Node:
    data: Any
    next = None

    def __init__(self, value) -> None:
        self.data = value


class LinkedList:
    head: Node = None

    def __init__(self, value):
        self.head = Node(value) if value else value

    def index(self, value, start=None, end=None) -> int:
        """
        Return zero-based index in the list of the first item whose value is equal to x
        1. If value found return index
        2. value not found then Error
        3. LL is empty
        """
        ptr = self.head
        index = 0
        while (ptr is not None) and (ptr.next is not None):
            if start is not None and index <= start:
                ptr = ptr.next
            if end is not None and index >= end:
                break
            if ptr.data == value:
                return index
            index += 1
            ptr = ptr.next
        raise ValueError("No such item found!")

    def insert(self, index, value):
        """
        Min 2 nodes in LL
        Scenarios
        1. LL is empty
        2. LL has few elements
        3. positive and negative index
        4. Head is getting inserted
        """
        ptr = self.head
        counter = 0
        node = Node(value)

        if ptr is None:
            self.head = node
        while ptr is not None and (counter + 1 < index):
            ptr = ptr.next
            counter += 1
            
        node.next = ptr.next
        ptr.next = node

    def prepend(self, value):
        """Special case of insert"""
        self.insert(0, value)

    def append(self, value):
        """Special case of insert
        """
        self.insert(-1, value)

    def extend(self, ll):
        """l1.extend(l2) special case of append"""
        pass

    def remove(self, index):
        """
        1. Head is being removed
        """
        pass

    def pop(self):
        """Special case of remove"""
        return self.remove(-1)

    def clear(self):
        """Special case of remove"""
        pass

    # Algo
    def reverse(self):
        pass

    def sort(self):
        pass

    def copy(self):
        """ID, hash --"""
        pass
