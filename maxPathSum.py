class Solution:


    def maxPathSum(self, root: TreeNode) -> int:
        import sys
        global ret
        ret = -sys.maxsize - 1  
        def dfs(root:TreeNode):
            global ret
            if root ==None:
                return 0
            left = max(0,dfs(root.left))
            right =  max(0,dfs(root.right))
            ret =  max(ret,left+right+root.val)
            return root.val+max(left,right)
        dfs(root)
        return ret