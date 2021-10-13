# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        global ret,flag
        self.ret = []
        flag = 0
        def dfs(Node:TreeNode):
            global ret
            global flag
            if Node == None:
                return
            dfs(Node.left)
            self.ret.append(Node.val)
            dfs(Node.right)
        dfs(root)
        self.min_i =  min(self.ret)
        self.i = self.ret.index(self.min_i)

    def next(self) -> int:
        if self.i <= len(self.ret):
            output = self.ret[self.i]
            self.i = self.i +1
        else:
            return None
        return output
    def hasNext(self) -> bool:
        if self.i+1 <= len(self.ret):
            return True
        else:
            return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()