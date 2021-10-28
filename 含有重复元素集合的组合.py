class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        global resultList,path
        resultList = []
        path =[]
        candidates = sorted(candidates)
        def dfsSub(candidates,target,startIndex):
            global path,resultList
            sumPath = sum(path)
            if  sumPath>target or sum(candidates)< target:
                return
            elif  sumPath==target and path not in resultList:
                resultList.append(path)
                return
            for i in range(startIndex, len(candidates)):
                if path !=[] or i==0 or candidates[i]!=candidates[i-1] :
                    path = path + [candidates[i]]
                else:
                        continue
                dfsSub(candidates,target,i+1)
                path = path[:-1]
            return resultList
        dfsSub(candidates,target,0)
        return resultList