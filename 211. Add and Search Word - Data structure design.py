class treeNode(object):
    def __init__(self):
        self.children = dict()
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = treeNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = treeNode()
                node.children[letter]=child
            node = child
        node.isWord = True
            
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root, 0)
    
    def dfs(self, word, root, depth):
        if not root: return False
        if len(word) == depth:return root.isWord
        if word[depth]!='.':
            return root != None and self.dfs(word, root.children.get(word[depth]), depth+1)
        else:
            for child in root.children.values():
                if self.dfs(word, child, depth+1):
                    return True
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
