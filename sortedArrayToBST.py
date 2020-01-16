# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums ==[]:
            return None
        len_nums = len(nums)
        root_val = len_nums/2
        root = TreeNode(nums[root_val])
        root.left = self.sortedArrayToBST(nums[0:root_val])
        root.right = self.sortedArrayToBST(nums[root_val+1:])
        return root