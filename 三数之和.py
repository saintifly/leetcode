class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        num = len(nums)
        if num < 3:
            return []
        retsult = []
        for i in range(num-2):
            left = i+1
            right = num-1
            sumLeftRight = 0
            target = nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            while (left<right):
                sumLeftRight = nums[left]+nums[right]
                if sumLeftRight == -target:
                    retsult.append([nums[i],nums[left],nums[right]])
                    while (left<right and nums[left]==nums[left+1]):
                        left+=1
                    while(left<right and nums[right]==nums[right-1]):
                        right-=1
                    left += 1
                    right -= 1
                elif (sumLeftRight < -target):
                    left +=1
                else:
                    right -=1
        return retsult