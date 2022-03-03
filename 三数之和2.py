class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        inputListLen = len(nums)
        if inputListLen < 3:
            return []
        inputListSorted = sorted(nums)
        if inputListSorted[0]>0 or inputListSorted[-1]<0:
            return []
        ret = []
        for i in range(inputListLen):
            fixValue = inputListSorted[i]
            if fixValue == inputListSorted[i-1] and i>0:
                continue
            leftpoint = i+1
            rightpoint = inputListLen-1
            while(leftpoint < rightpoint):
                sumTree = fixValue+inputListSorted[leftpoint]+inputListSorted[rightpoint]
                if sumTree>0:
                    rightpoint = rightpoint-1
                    continue
                elif sumTree<0:
                    leftpoint = leftpoint+1
                    continue
                else:
                    if [fixValue,inputListSorted[leftpoint],inputListSorted[rightpoint]] not in ret:
                        ret.append([fixValue,inputListSorted[leftpoint],inputListSorted[rightpoint]])
                    rightpoint = rightpoint-1
                    leftpoint = leftpoint+1
        return ret