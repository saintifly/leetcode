class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ##这个数的前面是nusm[i]==num[i+1]
        ##这个数的后面也是nusm[i]==num[i-11]

        indexStart = 0
        indexEnd = len(nums)-1
        if len(nums)==1:
            return nums[0]
        while(indexStart < indexEnd-1 ):
            print(indexStart,indexEnd)
            indexMid =  indexStart+(indexEnd -indexStart)//2
            print(nums[indexMid])
            if nums[indexMid]!=nums[indexMid+1] and nums[indexMid]!=nums[indexMid-1]:
                return nums[indexMid]

            if indexMid%2==0 and nums[indexMid]==nums[indexMid+1]:
                indexStart = indexMid
            elif indexMid%2==0 and nums[indexMid]==nums[indexMid-1]:
                indexEnd = indexMid
            elif indexMid%2==1 and nums[indexMid]==nums[indexMid-1]:
                indexStart = indexMid
            else:
                 indexEnd = indexMid
             
        if nums[indexStart]!=nums[indexStart+1] and nums[indexStart]!=nums[indexStart-1] :
                return nums[indexStart]               

        if nums[indexStart] == nums[indexStart-1]:
            return nums[indexEnd]
        return nums[indexStart]