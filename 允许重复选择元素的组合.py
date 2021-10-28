class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global resultList,path
        resultList = []
        path =[]
        def dfsSub(candidates,target,startIndex):
            global path,resultList
            if sum(path)>=target:
                if sum(path) ==target:
                    resultList.append(path)
                return
            for i in range(startIndex, len(candidates)):
                path = path + [candidates[i]]
                dfsSub(candidates,target,i)
                path = path[:-1]
            return resultList
        dfsSub(candidates,target,0)
        return resultList