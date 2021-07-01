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

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass



if __name__ == "__main__":
    ht = HashTable()

    ht.put("a", 1)
    print(ht["a"])

    # ht.get("a")
