class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while(start< end):
            mid = (start+ end)//2
            hours = sum( (p + mid - 1)//mid for p in piles)
            print(start,end,hours,mid)
            if hours<=h:
                end = mid
            else:
                start = mid +1
        return start