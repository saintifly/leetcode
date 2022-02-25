class Solution(object):
    Max_rob = 0
    tmp_rob = 0
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums ==[]:
            return 0
        len_nums = len(nums)
        if len_nums ==1:
            return nums[0]
        sumList = [nums[0]] 
        sumList.append(max(nums[0], nums[1]))
        for i in range(2,len_nums):
            sumList.append(max(nums[i]+sumList[-2], sumList[-1]))
        return sumList[-1]