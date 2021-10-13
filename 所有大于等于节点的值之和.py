# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        global ret,sum
        sum = 0
        def dfs(Node:TreeNode):
            global ret
            global sum
            if Node == None:
                return
            dfs(Node.right)
            if Node !=None:
                sum = sum + Node.val
                Node.val =  sum
            dfs(Node.left)

        dfs(root)
        return root
