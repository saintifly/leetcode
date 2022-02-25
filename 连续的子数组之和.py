class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumPre = 0
        sumPreList = []
        sumPreSameNum = {}
        retCount = 0
        for i,item in enumerate(nums):
            sumPre += item
            if sumPre == k:
                retCount +=1
            if sumPre - k in sumPreList:
                retCount += sumPreSameNum[sumPre-k]
            if sumPre not in sumPreSameNum:
                sumPreSameNum[sumPre] =1
            else:
                sumPreSameNum[sumPre] +=1
            sumPreList.append(sumPre)
        return retCount