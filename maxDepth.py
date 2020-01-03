# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

max_count = 0
count = 0
dir = [0, 1]

def dfs_find(tree_root):
    global count
    global max_count
    if tree_root == None:
        #print count
        if count > max_count:
            max_count = count
        return
    for i in [0,1]:
        if i ==0:
            count =  count + 1
            #print "111",count 
            dfs_find(tree_root.left)
            count =  count - 1
        else:
            count =  count + 1
            dfs_find(tree_root.right)
            count =  count - 1
    

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max_count
        max_count = 0
        if root ==None :
            return 0
        dfs_find(root)
        #count = 0
        return max_count
        