class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ret = 0
        left = right =0
        totalSum=1
        for i,item in enumerate(nums):
            right = i
            totalSum = totalSum*item
            while (totalSum >= k and left<=right):
                totalSum = totalSum//nums[left]
                left =left+1
            if left<=right:
                ret += (right-left)+1
        return ret