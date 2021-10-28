class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global resultList,path,visted
        resultList = []
        path =[]
        visted = [0]*len(nums)
        nums = sorted(nums)
        def dfsSub(nums):
            global path,resultList,visted
            if len(path) >= len(nums):
                resultList.append(path)
                # visted = [0]*len(nums)
                return
            for i in range(len(nums)):
                if i>0 and visted[i]==0 and visted[i-1]==0  and nums[i]==nums[i-1]:
                    continue
                if visted[i]!=1:
                    path = path + [nums[i]]
                    visted[i]=1
                else:
                    continue
                dfsSub(nums)
                visted[i] = 0
                path = path[:-1]
            return resultList
        dfsSub(nums)
        return resultList