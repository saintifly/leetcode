class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = [None for _ in range(26)]
        self.isWord = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for i in word:
            ID = ord(i)-ord('a')
            if root.child[ID] == None:
                root.child[ID] = Trie()
            root = root.child[ID]
        root.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self
        for c in word:
            ID = ord(c) - ord('a')
            if root.child[ID] == None:
                return False
            root = root.child[ID]
        return root.isWord == True



class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.preTrie = Trie()


    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.preTrie.insert(i)


    def search(self, searchWord: str) -> bool:
        for i,item in enumerate(searchWord):
            for j in range(26):
                charItem = chr(j+ord('a'))
                if  charItem!= item :
                    wordnew = searchWord[:i]+charItem+searchWord[i+1:]
                    if self.preTrie.search(wordnew) == True:
                        return True
        return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)