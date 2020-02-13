class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        sum_d = [0]*len_nums
        sum_d[0] = nums[0]
        for i in range(1, len_nums):
            if nums[i]+sum_d[i-1]>nums[i]:
                sum_d[i] = nums[i]+sum_d[i-1]
            else:
                sum_d[i]=nums[i]
        return max(sum_d)