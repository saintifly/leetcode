# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findpath(self,x,y):
        print x
        print y
        if x is None and y is not None:
            return False
        if x is not None and y is None:
            return False
        if x is None and y is None:
            return True
        if x.val != y.val :
            return False
        if x.left is None and y.right is None:
            return self.findpath(x.right,y.left)
        if x.right is None and y.left is None:
            return self.findpath(x.left,y.right) 
        for i in range(0,2):
            if i ==0:
                if self.findpath(x.left,y.right) is False:
                    return False
            else:
                if self.findpath(x.right,y.left) is False:
                    return False
            
        
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if self.findpath(root.left,root.right) is False:
            return False
        else:
            return True
        