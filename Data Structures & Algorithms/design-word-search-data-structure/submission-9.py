class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root       
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word)
    
    def searchHelper(self, node: Optional[TrieNode], word: str) -> bool:
        if not node:
            return False

        if word == "":
            return node.isEndOfWord

        c = word[0]
        if c == '.':
            if len(node.children) == 0:
                return False
            for child in node.children.values():
                if self.searchHelper(child, word[1:]):
                    return True
            return False
                 
        else:
            if c not in node.children:
                return False
            node  = node.children[c]
            return self.searchHelper(node, word[1:])

        
class TrieNode():

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
