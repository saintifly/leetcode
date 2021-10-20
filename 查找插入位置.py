class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        start = 0
        end  = len(nums)-1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while (end -start >1 ):
            if nums[start+(end-start)//2] >= target:
                end = start+(end-start)//2
            else:
                start = start+(end-start)//2
        return start+1