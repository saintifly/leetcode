# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): 
    
    def isValidBST_left(self, root, root_minval, root_maxval):
        print root
        print root_minval,root_maxval
        if root is None:
            return True
        if root.left is None and root.right is not None:
            if root.right.val >= root_maxval or root.right.val <= root.val:
                return False
            #if root.right.left is not None and root.right.right is None:
            #    return False
            return self.isValidBST_left(root.right,root.right.val,root_maxval)
        if root.right is None and root.left is not None:
            if root.left.val >= root_maxval or root.left.val >= root.val:
                return False
            #if root.left.left is None and root.left.right is not None:
            #    return False
            return self.isValidBST_left(root.left,root.left.val,root_maxval)
        if root.left is None and root.right is None:
            return True
        if root.left.val >= root_maxval or root.right.val >= root_maxval:
            return False
        if root.left.val >=root.val or  root.right.val<=root.val:
            return False

        if self.isValidBST_left(root.left, root.left.val,root_maxval) is False:
                    return False
        if self.isValidBST_left(root.right, root.right.val,root_maxval) is False:
                    return False
        return True
    
    def isValidBST_right(self, root, root_minval, root_maxval):
        print root
        print "-----",root_minval,root_maxval
        if root is None:
            return True
        if root.left is None and root.right is not None:
            if root.right.val <=root_minval or root.right.val <= root.val:
                return False
            #if root.right.left is not None and root.right.right is None:
            #    return False
            return self.isValidBST_right(root.right,root_minval, root.right.val)
        if root.right is None and root.left is not None:
            if root.left.val <=root_minval or root.left.val >=root.val:
                return False
            #if root.left.left is None and root.left.right is not None:
            #    return False
            return self.isValidBST_right(root.left, root_minval,root.left.val)
        if root.left is None and root.right is None:
            return True
        if root.left.val <=root_minval or root.right.val <= root_minval:
            return False
        if root.left.val >=root.val or  root.right.val<=root.val:
            return False
        
        if self.isValidBST_right(root.left, root_minval,root.left.val) is False:
                    return False
        if self.isValidBST_right(root.right, root_minval, root.right.val) is False:
                    return False
        return True   
    
    
    def isValidBST_update(self, root, root_minval, root_maxval):
        print root
        print root_minval,root_maxval
        if root is None:
            return True
        
        if root.left is None and root.right is not None:
            if root.right.val <= root.val:
                return False
           # if root.right.left is not None and root.right.right is None:
           #     return False
            return self.isValidBST_right(root.right,root_minval,root.right.val)
        if root.right is None and root.left is not None:
            if root.left.val >= root.val:
                return False
            #if root.left.left is None and root.left.right is not None:
            #    return False
            return self.isValidBST_left(root.left,root.left.val,root_maxval)
        
        if root.left is None and root.right is None:
            return True
        if root.left.val >= root.val or root.right.val <= root.val:
            return False
        if root.val > root_minval or root.right.val < root_maxval:
            return False

        if self.isValidBST_left(root.left, root.left.val,root_maxval) is False:
                    return False
        if self.isValidBST_right(root.right, root_minval,root.right.val) is False:
                    return False
        return True
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        root_val = root.val
        ret=True
        if self.isValidBST_update(root, root_val,root_val) is False:
                return False
		###########################采用规避的方法，理论上应该使用递归遍历所有子树
        if root.left is not None:
            if self.isValidBST_update(root.left, root.left.val,root.left.val) is False:
                    return False
        if root.right is not None:
            if self.isValidBST_update(root.right, root.right.val,root.right.val) is False:
                    return False             
        return ret