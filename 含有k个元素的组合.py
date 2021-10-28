class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        global resultList,path
        resultList = []
        path =[]
        def dfsSub(n,k,startIndex):
            global path,resultList
            if len(path)>=k:
                resultList.append(path)
                return
            for i in range(startIndex,n+1):
                path = path + [i]
                dfsSub(n,k,i+1)
                path = path[:-1]
            return resultList
        dfsSub(n,k,1)
        return resultList