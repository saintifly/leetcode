class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        for i,item in enumerate(nums):
            for j,item1 in enumerate(nums[i+1:i+k+1]):
                if abs(item1-item) <=t : 
                    print(item1,item)
                    return True
        return False