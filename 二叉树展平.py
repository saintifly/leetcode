class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:    
        global ret
        head = TreeNode(0)
        ret = head 
        def dfs(Node:TreeNode):
            global ret
            if Node == None:
                return
            dfs(Node.left)
            ret.right = Node
            ret = ret.right
            Node.left = None
            dfs(Node.right)
        dfs(root)
        return head.right