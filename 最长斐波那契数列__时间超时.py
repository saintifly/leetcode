class Solution:
    def binary_search(self, nums, right,target):
        """二分查找"""
        left = 0
        while  left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        ret = 0
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(1,n):
            for j in range(0,i):
                tmp = self.binary_search(arr,j-1,arr[i]-arr[j])
                dp[i][j]=dp[i][j] = dp[j][tmp] + 1 if  tmp!=-1 else 2
                ret = max(ret,dp[i][j])
        return  ret if ret>2 else 0