class Solution:
    def findMaximumXOR(self, nums):
        a = Tri()
        out = 0
        for i in nums:
            a.insertNode(i)
        for i in nums:
            ret = a.maxORNode(i)
            out =  max(out,ret)
        del a 
        return out

class TriNode():
        def __init__(self,left=None,right=None):
            self.left = left
            self.right = right

class Tri():
        def __init__(self):
            self.Trie = TriNode()

        def insertNode(self,val):
            Node = self.Trie
            for i in range(31,-1,-1):
                bit = 1 << i
                tmp = bit & val
                if tmp > 0:
                    if Node.right == None:
                        Node.right = TriNode()
                        Node = Node.right
                    else:
                        Node = Node.right

                else:
                    if Node.left == None:
                        Node.left = TriNode()
                        Node = Node.left
                    else:
                        Node = Node.left

        def maxORNode(self,n):
            Node = self.Trie
            ret = 0
            for i in range(31,-1,-1):
                bit = 1 << i
                val = bit & n
                if val >0:
                    if Node.left !=None:
                        ret = ret + bit
                        Node = Node.left
                        continue
                    if Node.right !=None:
                        Node = Node.right
                        continue
                else:
                    if Node.right != None:
                        ret = ret + bit
                        Node = Node.right
                        continue
                    if Node.left != None:
                        Node = Node.left
                        continue
            return ret