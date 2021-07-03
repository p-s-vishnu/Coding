from typing import List

class BSTNode:
    def __init__(self, data, level=0):
        self.data = data
        self.level = level
        self.left = None
        self.right = None

    def print(self):
        """
        Preorder: Node, left, right
        """
        prefix = "|__" if self.level > 0 else ""
        space = " " * self.level * 4
        print(space, prefix, self.data)

        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()
    
    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = BSTNode(value, self.level+1)
            else:
                self.left.insert(value)
        if value > self.data:
            if self.right is None:
                self.right = BSTNode(value, self.level+1)
            else:
                self.right.insert(value)
        return None

    def contains(self, value):
        """ Node left right search
        """
        if self.data == value:
            return True
        if value < self.data and self.left is not None:
            return self.left.contains(value)
        if value > self.data and self.right is not None:
            return self.right.contains(value)
        return False

    def find_max(self):
        if self.right is not None:
            self.right.find_max()
        return self.data

    def find_min(self, value):
        if self.left is not None:
            self.left.find_min()
        return self.data
    
    def delete(self, value):
        pass


class BinarySearchTree:
    def __init__(self, values:List):
        self.root = BSTNode(values[0])
        for value in values[1:]:
            self.insert(value)

    def insert(self, value):
        self.root.insert(value)

if __name__ == "__main__":
    tree = BinarySearchTree([10,5,3,56,23,5])

    print(tree.root.print())