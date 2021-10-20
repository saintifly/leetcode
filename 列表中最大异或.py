class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Tri():
    def __init__(self):
        self.Trie = Node(0)
        self.PointStart = self.Trie

    def insertNode(self,val):
        self.Trie = self.PointStart
        for i in range(31,-1,-1):
            bit = 1 << i
            tmp = bit & val
            if tmp > 0:
                if self.Trie.right == None:
                    self.Trie.right = Node(1)
                    self.Trie = self.Trie.right
                else:
                    self.Trie = self.Trie.right

            else:
                if self.Trie.left == None:
                    self.Trie.left = Node(0)
                    self.Trie = self.Trie.left
                else:
                    self.Trie = self.Trie.left

        return self.PointStart


    def maxORNode(self,n):
        self.Trie = self.PointStart
        ret = 0
        for i in range(31,-1,-1):
            bit = 1 << i
            val = bit & n
            if val >0:
                if self.Trie.left !=None:
                    ret = ret + bit
                    self.Trie = self.Trie.left
                    continue
                if self.Trie.right !=None:
                   self.Trie = self.Trie.right
                   continue
            else:
                if self.Trie.right != None:
                    ret = ret + bit
                    self.Trie = self.Trie.right
                    continue
                if self.Trie.left != None:
                    self.Trie = self.Trie.left
                    continue
        return ret

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        a = Tri()
        out = 0
        for i in nums:
            b = a.insertNode(i)
        for i in nums:
            ret = a.maxORNode(i)
            out =  max(out,ret)
        return out