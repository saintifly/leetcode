class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        countList = []
        for i in set(nums):
            countDict[i] = nums.count(i)
            countList.append(nums.count(i))
        a = sorted(countList)
        return [j for j,v in countDict.items() if v in a[-k:]]
        