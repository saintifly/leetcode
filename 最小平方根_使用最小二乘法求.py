class Solution:
    def mySqrt(self, x: int) -> int:
             # 二分法
        if x <= 1: # 
            return x
        left = 0
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid**2 <=x and (mid+1)**2 > x:
                return mid
            elif mid**2 < x: # 数值偏小，需要扩大
                left = mid + 1
            elif mid**2 > x: # 数值偏大，需要缩小
                right = mid - 1
