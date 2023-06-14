class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string):
        p = self.root
        for s in string:
            if s not in p.children:
                p.children[s] = TrieNode()
            p = p.children[s]
        p.is_word = True
    
    def search(self, string):
        p = self.root
        for s in string:
            if s not in p.children:
                return False
            p = p.children[s]
        return p.is_word
    
    def search_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True
