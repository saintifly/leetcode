class Solution:
    # def binary_search(self, nums, right,target):
    #     """二分查找"""
    #     left = 0
    #     while  left <= right:
    #         mid = left + ((right - left) >> 1)
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] > target:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return -1

    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # n = len(arr)
        # ret = 0
        # num_idx = dict()
        # for i, x in enumerate(arr):
        #     num_idx[x] = i
        # dp = [[0 for i in range(n)] for j in range(n)]
        # for i in range(1,n):
        #     for j in range(0,i):
        #         tmp = arr[i]-arr[j]
        #         if tmp in arr[0:j]:
        #             num = num_idx[tmp]
        #             dp[i][j] = dp[j][num] + 1 
        #         else:
        #             dp[i][j]= 2
        #         ret = max(ret,dp[i][j])
        # return  ret if ret>2 else 0
        n = len(arr)
        res = 0
        num_idx = {}
        for i, x in enumerate(arr):
            num_idx[x] = i
        
        dp = defaultdict(lambda : 2)
        for mid in range(n):
            for r in range(mid + 1, n):
                x = arr[r] - arr[mid]
                if x in num_idx:
                    l = num_idx[x]
                    if l < mid:
                        ID1 = l * n + mid
                        ID2 = mid * n + r
                        dp[ID2] = dp[ID1] + 1
                        if dp[ID2] >= 3:
                            res = max(res, dp[ID2])
        return res