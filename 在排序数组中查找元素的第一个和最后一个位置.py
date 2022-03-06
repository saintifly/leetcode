class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            return [bisect_left(nums,target),bisect_right(nums,target)-1]
        else:
            return [-1,-1]    