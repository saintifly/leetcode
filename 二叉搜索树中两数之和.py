# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # Definition for a binary tree node.
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
        for i,item in enumerate(self.ret):
            if k -item in self.ret[i+1:] or k -item in self.ret[:max(0,i-1)] :
                print(i,item,k)
                return True
        return False
