class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            passNum = []
            resultRet = []
            out =[[]]
            tmp = []
            numsLen = len(nums)
            while(len(tmp)!=numsLen):
                for i in range(len(nums)):
                    if nums[i] not in tmp:
                        tmp = tmp + [nums[i]]
                    else:
                        continue
                    if set(tmp) not in resultRet:
                            resultRet.append(set(tmp))
                            out.append(tmp)
                    if tmp not in passNum:
                        passNum.append(tmp)
                        break
                    else:
                        tmp = tmp[:-1]
                else:
                    tmp = tmp[:-1]
                if tmp == list(reversed(nums)):
                    break
                if len(tmp)==numsLen:
                    tmp = tmp[:-1]
            return out