class Solution(object):
    ret = []
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global resultList,path
        resultList = []
        path =[]
        def dfsSub(nums,startIndex):
            global path,resultList
            resultList.append(path)
            for i in range(startIndex,len(nums)):
                path = path + [nums[i]]
                dfsSub(nums,i+1)
                path = path[:-1]
            return resultList
        dfsSub(nums,0)
        return resultList