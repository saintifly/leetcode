class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sLen = len(nums)
        if sLen ==1:
            return nums[0]
        if sLen ==2:
            return max(nums)
        costMax = [0 for i in range(sLen)]
        costMax[0]=nums[0]
        costMax[1]= max(nums[0:2])
        for i in range(2,sLen):
            costMax[i] = max(nums[i]+costMax[i-2],costMax[i-1])
        return costMax[i]