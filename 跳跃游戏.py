class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        max_res = 0
        for i in range(nums_len):
            if max_res>=i:
                max_res = max(max_res,i+nums[i])
        if max_res >= nums_len-1:
            return True
        if max_res==nums_len-1 and nums[nums_len-1]>0:
            return True
        else:
            return False
