class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumPre = 0
        sumPreSame = {0:-1}
        MaxLen = 0
        for i,item in enumerate(nums):
            sumPre += 1 if item>0 else -1
            if sumPre in sumPreSame:
                MaxLen = max(MaxLen, i-sumPreSame[sumPre])
            else:
                sumPreSame[sumPre] = i
        return MaxLen