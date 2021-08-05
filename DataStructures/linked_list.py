from typing import Any


class Node:
    data: Any
    next = None

    def __init__(self, value) -> None:
        self.data = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        out = []
        ptr = self.head
        while ptr is not None:
            out.append(str(ptr.data))
            ptr = ptr.next
        return f"Size: {self.size}| " + " -> ".join(out)

    def index(self, value, start=None, end=None) -> int:
        """
        Return zero-based index in the list of the first item whose value is equal to value.
        O(n)
        1. If value found return index
        2. value not found then Error
        3. LL is empty
        """
        ptr = self.head
        index = 0
        while ptr is not None:
            if start is not None and index < start:
                ptr = ptr.next
                continue
            if end is not None and index >= end:
                break
            if ptr.data == value:
                return index
            index += 1
            ptr = ptr.next
        raise ValueError("No such item found!")

    def insert(self, index, value):
        """
        Min 1 nodes in LL
        Scenarios
        1. LL is empty
        2. LL has few elements
        3. positive and negative index
        4. Head is getting inserted
        """
        ptr = self.head
        counter = 0
        node = Node(value)

        if (ptr is not None) and (index != 0):
            while counter < self.size and (counter + 1 < index):
                ptr = ptr.next
                counter += 1
            node.next = ptr.next
            ptr.next = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def prepend(self, value):
        """Special case of insert"""
        self.insert(0, value)

    def append(self, value):
        """Special case of insert
        """
        self.insert(self.size, value)

    def extend(self, ll):
        """ Extends a new linked list to source linked list
        O (m), m = len(self), n = len(ll)
        1. If L1 is empty and L2 is not
        """
        if not isinstance(ll, LinkedList):
            raise TypeError(
                f'{type(self).__class__.__name__} expected as parameter')
        ptr = self.head

        if ptr is not None:
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = ll.head
        else:
            self.head = ll.head
        self.size += ll.size

    def remove(self, index):
        """
        1. Head is being removed
        2. Only one element in the ll and it is removed
        3. index more or less than size
        """
        if index < 0 or index > self.size - 1:
            raise IndexError('Index out of range')
        if index == 0:
            # self.head will not be none in this case
            self.head = self.head.next  # auto garbage collection by python
            self.size -= 1
            return

        counter = 0
        ptr = self.head
        while ptr is not None:
            if counter == index - 1:
                ptr.next = ptr.next.next
                self.size -= 1
                break
            ptr = ptr.next
            counter += 1

    def pop(self):
        """Special case of remove"""
        return self.remove(self.size - 1)

    def clear(self):
        self.head = None
        self.size = 0

    # Algo
    def reverse(self):
        pass

    def sort(self):
        pass

    def copy(self):
        """ID, hash --"""
        pass


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(1)
    l1.append(10)

    l2 = LinkedList()
    l2.append(90)
    l2.prepend("Hello")
    l2.append("Worl")
    l2.prepend("D")

    print(l1)
    print(l2)

    l1.extend(l2)
    print(l1)

    l1.pop()
    l1.remove(0)
    print(l1)

    l2.clear()
    print(l2)
