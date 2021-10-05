# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.Tree = root
        self.ChildList = []
    
    def insert(self, v: int) -> int:
        TreeNode_P0 = self.Tree
        TreeNode_P1 = TreeNode(v)
        self.ChildList.append(TreeNode_P0)
        tmp = 0
        while(self.ChildList[0].left !=None and self.ChildList[0].right !=None):
        #while(self.ChildList[0].left !=None and self.ChildList[0].right !=None and self.ChildList != []):
            if tmp ==0:
                self.ChildList.append(self.ChildList[0].left)
                tmp = 1
            else:
                self.ChildList.append(self.ChildList[0].right)
                tmp = 0
                self.ChildList.remove(self.ChildList[0])
        if self.ChildList[0].left ==None:
            self.ChildList[0].left = TreeNode_P1
        else:
            self.ChildList[0].right = TreeNode_P1
        return self.ChildList[0].val

    def get_root(self) -> TreeNode:
        return self.Tree



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()