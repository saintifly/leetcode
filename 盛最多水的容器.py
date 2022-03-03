class Solution:
    def maxArea(self, height: List[int]) -> int:
        heightlen = len(height)
        if heightlen<2:
            return 0
        maxWater = min(height[0],height[-1])*(heightlen-1)
        leftPoint = 0
        rightPoint = heightlen - 1
        while (leftPoint<rightPoint):
            if height[leftPoint]<=height[rightPoint]:
                maxWater = max(maxWater,height[leftPoint]*(rightPoint-leftPoint))
                leftPoint = leftPoint + 1
            else:
                maxWater = max(maxWater,height[rightPoint]*(rightPoint-leftPoint))
                rightPoint = rightPoint-1
        return maxWater