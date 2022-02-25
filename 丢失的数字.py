class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_val = len(nums)+1
        for i in range(max_val):
            if i not in nums:
                count = i
                break
        return count 