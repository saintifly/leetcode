class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedSet as SS
        ss = SS()
        for i,item in enumerate(nums):

            ID = ss.bisect_left(item)
            if 0 <= ID < len(ss):
                if abs(item - ss[ID]) <= t:
                    return True
            if 0 <= ID - 1:
                if abs(item - ss[ID - 1]) <= t:
                    return True

            ss.add(item)

            if k <= i:
                l = i - k
                ss.remove(nums[l])