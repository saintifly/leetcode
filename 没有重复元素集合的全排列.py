class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global resultList,path
        resultList = []
        path =[]
        def dfsSub(nums):
            global path,resultList
            if len(path) >= len(nums):
                resultList.append(path)
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path = path + [nums[i]]
                else:
                    continue
                dfsSub(nums)
                path = path[:-1]
            return resultList
        dfsSub(nums)
        return resultList