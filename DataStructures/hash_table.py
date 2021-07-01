class HashTable:
    """
    Insertion O(1)
    Lookup O(1)

    Two methods to prevent collision:
    1. Chaining
    2. Linear probing
    """
    def __init__(self):
        self.size = 1024
        self.index_list = [None] * self.size

    def get_index(self, value):
        hash_value = hash(value)
        return hash_value % self.size

    def __getitem__(self, key):
        index = self.get_index(key)
        # either None 
        if self.index_list[index] is None:
            return None

        # list
        for row in self.index_list[index]:
            # contains
            if key in row:
                return row[1]
        # does not contain key
        return None
        

    def __setitem__(self, key, value):
        index = self.get_index(key)
        # if None create a new list
        if self.index_list[index] is None:
            self.index_list[index] = []
        # else list then append
        self.index_list[index].append((key, value))

    def __delitem__(self, key):
        index = self.get_index(key)
        if self.index_list[index] is None:
            return None
        for row in self.index_list[index]:
            if key in row:
                del self.index_list[index]
        return None


if __name__ == "__main__":
    ht = HashTable()
    ht["a"] = 1
    ht["b"] = 100
    ht["c"] = 100
    ht["d"] = 1002
    ht["e"] = 1
    
    for row in ht.index_list:
        if row is not None:
            print(row)

    del ht['a']