# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        global ret,flag
        ret = None
        flag = 0
        def dfs(Node:TreeNode):
            global ret
            global flag
            if Node == None:
                return
            dfs(Node.left)
            if flag ==1 and ret==None:
                ret =  Node
                return
            if Node == p :
                flag = 1
            dfs(Node.right)
        dfs(root)
        return ret