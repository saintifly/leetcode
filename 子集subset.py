class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            global resultList,path,visted
            resultList = []
            path =[]
            visted = [0]*len(nums)
            nums = sorted(nums)
            def dfsSub(nums):
                global path,resultList,visted
                if sorted(path) not in resultList and len(path)<=len(nums):
                    resultList.append(path)
                    # visted = [0]*len(nums)
                else:
                    return
                for i in range(len(nums)):
                    if nums[i] not in path:
                        path = path + [nums[i]]
                        visted[i]=1
                    else:
                        continue
                    dfsSub(nums)
                    path = path[:-1]
                return resultList
            dfsSub(nums)
            return resultList