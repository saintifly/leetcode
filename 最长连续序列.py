class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        if nums==[]:
            return 0
        currenlen =1
        ret = 0
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                currenlen = currenlen+1
            else:
                ret = max(currenlen,ret)
                currenlen = 1
        ret =max(ret,currenlen)
        return ret