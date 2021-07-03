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
            return self.right.find_max()
        return self.data

    def find_min(self):
        if self.left is not None:
            return self.left.find_min()
        return self.data

    def delete(self, value):
        """
        - Leaf node
        - not a leaf or root: only left child
        - not a leaf or root: only right child
        - not a leaf or root: both right and left children
        - single element tree: found
        - single element tree: not found
        - Root node 
        """
        if value < self.data and self.left is not None:
            self.left = self.left.delete(value)
        elif value > self.data and self.right is not None:
            self.right = self.right.delete(value)
        else:
            if (self.left is None) and (self.right is None):
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            min_subnode = self.right.find_min()  # Alternate: switch with left max
            self.data = min_subnode
            self.right = self.right.delete(min_subnode)
        return self


class BinarySearchTree:
    def __init__(self, values: List):
        self.root = BSTNode(values[0])
        for value in values[1:]:
            self.insert(value)

    def insert(self, value):
        self.root.insert(value)

    def delete(self, value):
        return self.root.delete(value)


if __name__ == "__main__":
    tree = BinarySearchTree([10, 5, 3, 56, 23, 5, 59])

    tree.root.print()

    print(tree.root.find_max())
    print(tree.root.find_min())

    tree.delete(23)
    tree.root.print()
