class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ret = len(nums)+1
        totalSum = 0
        for right,item in enumerate(nums):
            totalSum = totalSum +item
            while(totalSum>=target):
                ret = min(ret,right-left+1)
                totalSum = totalSum - nums[left]
                left = left+1
        return 0 if ret > len(nums) else ret